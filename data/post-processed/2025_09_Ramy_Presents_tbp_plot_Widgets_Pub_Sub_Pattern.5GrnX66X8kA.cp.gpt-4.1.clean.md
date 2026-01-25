So this is going to be more of a high-level presentation, but I'll also go into details about some of the tricky parts and how to put these visualizations together, use the widgets, the widget updaters, and all of that. It will cover the PubSub pattern and accessing data.

You've all seen some of these interactive visualizations where, by using an episode or some widgets, you're able to control other widgets. Some widgets are interactive, some control others, and some only depend on others without controlling them. There's definitely communication between these widgets. In the past, when I started building these visualizations, especially those that depend on or send messages to each other, they needed to be in the same class or at least have some reference to communicate. For example, this is a subset of the messages that need to be sent or the dependency graph. The episode controls many widgets—for example, the ground truth mesh visualizer, this figure, the info widgets, and others. What ends up happening is you create a huge class with many tightly coupled widgets, making it difficult to extract functionality and move it to another plot.

The idea with introducing PubSub is to decouple all those dependencies. When the episode changes, we don't define what happens directly. Instead, the episode just publishes a message on the topic "episode number," and any other widget can subscribe to that topic, detect the change, and act within its own class. This decouples all communication. With direct communication, an episode directly controls other widgets. If you have widget 1, maybe as an episode slider, it directly controls some widgets. If you want to add a new widget that depends on widget 1, you'd have to modify the callback function for when the episode changes in widget 1 to make it talk to widget 5, for example. This makes it difficult to add or remove widgets and to extract and reuse functionality elsewhere. PubSub models solve this. The topics in the middle act as a broker. The publisher only knows its topic name, like "episode number," and publishes it on the event bus or broker. Any subscribers to that topic will receive the message; if there are none, the message is lost. This makes it easy to add a new subscriber and specify which topics it depends on. You can move that subscriber to another plot, and as long as someone is publishing those messages, it will work. These are all split into different classes, so you can copy a class, move it elsewhere, and it will work. I'll show an example of this at the end.

Niels Leadholm: Maybe you'll cover this in a bit, but in terms of the one-to-many publisher to topic arrows, how complex can a topic be? Naively, I would imagine a topic is just one variable, almost like a global namespace.

Ramy Mounir: You could publish multiple things if you want. Usually, I use it for publishing one thing on one topic, just to indicate the state of a widget. But you could publish multiple things on different topics. It depends on the resolution you want. For example, you could publish a hypothesis on one topic, or you could publish its location and rotation on separate topics. With this granularity, multiple widgets can listen to only the parts they need. It depends on the granularity you want.

Niels Leadholm: I guess you could also have two publisher widgets that affect a particular topic in different ways. If the topic is "step number," changing the step slider changes that, but changing the episode might reset the step to zero.

Ramy Mounir: Yes. I make the episode change the step, and then the step publishes a step number again. It goes into this loop.

Niels Leadholm: That does seem cleaner. So it's a published topic, a subscriber, and then it has its own publish to change the step. It wouldn't really be two arrows; it's more like a loop.

Ramy Mounir: The problem with that is, because it's a loop, it can take more time to reach equilibrium. If the publisher sends to the step number, and then the step number changes and publishes, that takes two steps. It's like message passing in graphs.

Niels Leadholm: Okay. Is there an upper bound on the number of message passes allowed before...?

Ramy Mounir: I don't have that, but sometimes you'll see a lot of things changing until they reach equilibrium. We can use debouncing to address this, but it hasn't been an issue so far.

Niels Leadholm: That's interesting.

Ramy Mounir: There are actually cases where I can have multiple publishers or multiple widgets publishing to the same topic. For example, here I have the primary target and these arrows—three different widgets, three different buttons—but they're all changing the topic called "current objects," which determines which hypothesis space we're looking at. You could be at an episode and a step, but want to change which hypothesis space you're inspecting. It could be the mug or something else. The primary target always resets back to the primary target of this episode. These can move right and left, cycling through the objects or hypothesis spaces. They all can publish to the same "current object" topic, which is sometimes useful.

We can look at this as a collection of widgets. These widgets are independent and only communicate through the PubSub topics. You can move them, take them into a different plot, and reuse the functionality.

Let's go through some examples before we look at the actual code. If we look at the episode slider, in this case, we only want to output an episode number. The way I've defined this in code is using something called "state to messages." The widget class calls these function names that I've defined. This is the pattern I'm using, but I'll go through that later. The important thing here is that this is like a payload function, where you define what topic is being published and the value of that message. We'll get into more details about this later. The episode only publishes the episode number, and that's what we see here. It can publish multiple things, but right now it only publishes the episode number. If we go to the step, the step receives the episode number and publishes the step number. Publishing the step number works the same way. I have the state to messages, and I'm telling it to publish the step number.

Receiving is a bit more complicated. I created these widget updaters, and you can have multiple updaters. There are many scenarios where the widget can change based on what it's listening to. Sometimes you'll have multiple updaters, or one updater that listens to multiple messages or topics. When it has enough messages in all of them, it can update the step widget. In this scenario, we have one updater. It's listening to the episode number, and once it gets a message or if the episode number changes, it calls a callback function to update the range. For example, episode 0 could have 50 steps, episode 1 could have 20 steps, so we need to modify the range of the step slider.

Once the episode number changes, it calls this callback function. That's a simple example. Let's look at more complicated examples, like this correlation plot. Here, it's listening to four topics: episode number, step number, current object (which hypothesis space), and age threshold. It's getting those from the buttons and arrows we discussed before. If any of those change, it calls the function updatePlot, which modifies the widget. This is why I call them widget updaters. The only way you can modify the widget you're on is through widget updaters, by listening to some topics or messages.

Niels Leadholm: And—

Ramy Mounir: Go ahead.

Niels Leadholm: Just to clarify, does each widget always have one widget updater, or could it have multiple?

Ramy Mounir: It can have multiple. I have an example for that. You can have multiple updaters, or none if you're not listening to anything and only publishing, like the episode slider. It's not listening to anything, just publishing which episode you're on.

Niels Leadholm: Okay. Maybe you'll show an example, but I'm curious: with the topic, if you change any one of these it's listening to, will it call the callback?

Ramy Mounir: Yes.

Niels Leadholm: Is there a notation for requiring all four of these to change in order to call the callback?

Ramy Mounir: Yes, or multiple required here. If you list a topic, it means if any of these topics change, you'll call the callback.

Niels Leadholm: Okay.

Ramy Mounir: "Required" means this topic is not really required for updatePlot to call it. Sorry, did you hear that noise?

Niels Leadholm: Yeah, I know.

Ramy Mounir: "Required" means I need to have this topic in my list of messages to send to updatePlot. If you set it to required, it won't call updatePlot until all of these messages are available. But just by listing them, if any one changes, it calls updatePlot. It's a small detail. In most cases, required being true is sufficient. I only needed it for one case, but it's usually enough.

Viviane Clay: Is there a difference between the variable changing versus the variable being available? I assume only one of these will change at any one time, but you need all four to update. Does it check if the value is available in the middle circle right now, and is that what "required" means?

Ramy Mounir: Yes, the widget updater keeps an inbox of all of these. It stores these messages, and only when all the required messages are available will it update the plot. Sometimes episode number is not yet available in the inbox, but one of these changes, and you still want to update the plot. That's the difference. Sometimes you don't have episode number yet, and updatePlot doesn't depend on it, so you'd still send the message if step number changes, for example.

Viviane Clay: But if all of them are available, but none have changed?

Ramy Mounir: Minimum.

Viviane Clay: Blood.

Ramy Mounir: No.

Viviane Clay: Okay.

Ramy Mounir: Only when it changes, because it's just the same function being called repeatedly. It doesn't matter otherwise.

Niels Leadholm: And the logic for all of them being required, that's specified in the inbox? If you wanted that to be the case.

Ramy Mounir: Yes, the logic for this inbox stuff is in the class of the widget updaters. You set it to required equals true, and it will not send a message without all four.

Niels Leadholm: Oh, okay.

Ramy Mounir: Did I answer your question? Okay.

Niels Leadholm: Yeah.

Ramy Mounir: Now, the output uses the state-to-messages function, and you can customize this as much as you want.

Here, I'm just sending out two messages. Sometimes, if I don't have a selected hypothesis, I send a message on a topic called clear_selected_hypothesis with a value of true. Or you can just say selected_hypothesis with a value of none. It depends on what you want to send. This is a payload function that can take the state of the widget, and you can modify it or do anything to it, and then send it.

Hojae Lee: Is the state-to-message supposed to be like a protocol? It must take in some state, and it must return some iterable of topic messages.

Ramy Mounir: Yes, it has to return a list of topic messages. Each of these topic messages will be iterated over and published. That's handled in the widget class. Here, you're just defining the payload function, but when you return those, it will go over them. The state doesn't have to be anything specific. I have this notion of a widget and a state, and for some widgets, it makes sense to have states. For example, the slider's state would be its value, or the button would be its value. Some widgets don't necessarily have a state, so if it doesn't, it will sometimes return none. You just put whatever state you want in here when defining it.

Hojae Lee: Okay, but it's a minimal contract that must return some iterables of topic messages.

Ramy Mounir: Yes, because all these messages are going to be published. If you don't have any messages to send, just return an empty list.

Hojae Lee: Okay.

Ramy Mounir: Or just don't have state-to-messages at all.

Here's another, slightly different example. This one doesn't publish anything, so we don't have state-to-messages, but we have updaters. In this example, we actually need more than one updater. We need one updater to update the mesh, and this one only listens to episode number because this is the primary target mesh, so it only changes with the episode. If the episode changes, the primary target changes, and we want to update the mesh to another object. We also want to listen to episode number and step number, so if either changes, we want to update the sensor on the object and move the sensor to a new location. If the step number doesn't change, I don't need to update the mesh. It doesn't make sense to do that. I've split the update mesh and update sensors, and I'm just defining what topics they need to listen to.

Niels Leadholm: Yeah, nice.

Ramy Mounir: That's basically a high-level view of these. We can now discuss more low-level details. These are the topics I plan on discussing. The first is not really related to PubSub, but more to TBP plots or helpers for accessing JSON data from the detailed run stats. Then I'll talk about adding a plot into the registry, how to register that plot using the CLI interface, which is pretty cool. Then creating widgets with widget ops, which is more involved. There are some tricks about debouncing and deduplicating events, because sometimes, if you're changing the slider value, it can keep sending messages with every movement. We want to gate these outputs and only send messages when necessary. This will touch on that.

Viviane Clay: Does it always depend on JSON files being logged?

Ramy Mounir: Yes, right now it does, but that's only part of it. If you have another way of loading the data, it doesn't need to depend on JSON.

I'm using something called Data Locator and data parser to parse the JSON and locate data, but if you're doing this online, you can have a different type of data locator.

Viviane Clay: Okay, cool.

Ramy Mounir: I've added a tutorial for accessing data. It's right here. It goes through the same stuff, but I'll go through it again.

We have a structure like this. This is a very simple structure. Usually, our JSONs are much bigger, with a depth of seven or eight. That's why it's useful, but let's take this simple example. We have a dictionary, one level with episode numbers, and for every episode, a list of dictionaries. The second level is a list, and the third level is another dictionary. If we want to access some data here, the way I do it is I define a data locator. In this data locator, I define all the steps needed to reach some data. It's usually either a key or an index—a key for a dictionary and an index for a list. I say this data locator has a step that is a key called episode, with a value of episode 2. The second path step is index, step, value 3, and then key, field, and I get evidence. If I run this with the parser and say extract with the data locator, it returns the value, basically 0.5. Now you can reuse that locator, but it's not really useful if you can't quickly modify this data locator or define it in a way where you know a lot of these are constants and you just want to define the missing values.

I rarely use a full locator path like this because all the data I'm extracting depends on some slider value, button, or another variable. I don't know what the episode is until I get the episode value from the slider. What I do is define the same locator in a partial way, inspired by partial functions from Python. You don't specify a value for the step you're missing. Here, I don't know what the step is, so I'll rely on the slider later to get it and keep that value missing. I can call the same function, parser.extract, with the partial locator and then the step I want. You don't have to specify all the steps again. That’s the idea. If you give it 70, 1, 2, 3, whatever, it will return the right value.

Another useful feature is querying the available options. Instead of extracting data, you can query what episodes are available at this step. When you have missing values and don't know the value for episode, you use parser.query instead of parser.extract. This will go through the steps, stop at the first missing value, and tell you all the available options. This is useful when deciding the range of a slider, or if the slider range changes based on the episode. You can always query how many steps or objects you have, and what those objects are. If you give it an episode number, it will go to the next missing step and return the available options. For episode 1, there are three steps: 0, 1, and 2. For episode 2, there are four steps: 0, 1, 2, and 3.

I thought instead of going straight into widget operations, we could build this as a tutorial together.

By the end of this, I think I have about 30 more minutes—maybe in 20 minutes we'll be done—and we should have built something like this.

If I don't have enough time to finish, these are the commits. I'll share the slides, and for every step, you'll be able to find the corresponding commit and code. The first commit is just the initial setup, where I set up the renderers, CLI arguments, and so on. Each later commit is for a specific widget: one for the episode, one for the step, one for the visualizer, and so on. The diffs will show that I don't modify any code from previous commits. If I add the step, I don't modify the episode at all. If I add something else, I don't modify the others. I split them this way so you can see there's no dependency.

Let's start with the initial setup.

For renderers, what we want to set up is three renderers. There's the main renderer and two more sub-renderers. In total, we have three renderers. You create a new renderer every time you want a different camera. If I want a different camera for a sub-renderer, I create it as a renderer; otherwise, I won't have a camera for it and can't move in this render independently. Let's look at the setup.

The setup is simple. To register a plot, define a function—any name, I call it main—and register that plot with the registered decorator. This is the name of the plot you'll use in the CLI to plot it, and then a description. The description shows when you query all available plots, explaining what the plot does. If you have arguments for the main function, define them in a different function, decorate it with attach_args, and give it the same plot name so it matches. The argument names must match as well.

All the code needs to fit inside the main function, since it's the only function that runs. You can put all the code here, but I like to create an interactive plot class and run it, so everything runs in the init of this class. If you're doing a matplotlib or seaborn function, you can just put the code here. This is the interactive plot where I create the renderers. For example, I have three renderers. I learned this trick from Jose—it's useful to specify render shapes inside the plotter. This shape can be defined in different ways. For example, a forward slash 1 gives you three renderers, splitting into three views—two on top and one at the bottom. There are different ways to specify the shapes, but this is very useful.

For renderer areas, you can say the first render is the whole screen, 00211, and then have two more renderers like this.

The things I'm defining here, I usually define all of them except maybe the YCB mesh loader. I only use this when I want to load a YCB object from the dataset, not a Monty model. It's a class that makes it easy: give it the graph object name, and it returns a video mesh.

The data parser takes a path to the log file, the JSON log file. The publisher is the PubSub publisher, shared with all widgets for communication. They all have access to this event bus and can publish and subscribe to the same topics. The plotter is a veto plotter that takes the renderer areas. The scheduler is the debouncer or debounce scheduler, which I'll discuss in a minute.

And then, after you define all of these, you want to show the renderers you have. We've defined three renderers, so we can go through them and show them. These renderers take options. When you do add 0 or add 1, that is basically saying you want the first or second renderer, in the same order that you defined them here.

You need to show that renderer, and if you want to show axes like these, you need to provide that in the show function. You can define the ranges for these, like X range, Y range, and so on. I usually put the Y range between 1.45 and 1.55, and you probably know why. You can define a camera as well, or you can set reset camera to true, which will reset the camera and find the objects, placing the camera so it can see all the objects. I don't like to set it unless I don't have anything in there.

Niels Leadholm: Wait, the reset camera, is that something in Veto, or something you implemented?

Ramy Mounir: That's a Veto thing.

Niels Leadholm: Did I understand that correctly? You said it finds something it can see?

Ramy Mounir: Yes, it will reset the camera to the objects in the scene, or something like that. Right now, we don't really have an object, so it probably just goes to a default position and focal point. The way you define those camera parameters is a position and a focal point. The focal point is where it's looking, and the position is where it is. If there's nothing in there, it probably just goes to 0,0,0 or 0,0,1. Especially for the main plotter, I like to know where it is, so I define the camera dictionary and set resetCamp to false.

Viviane Clay: For these...

Ramy Mounir: Yes.

Viviane Clay: The first one, is that the kind of white background, or what does that correspond to?

Hojae Lee: Screen.

Ramy Mounir: The main plotter, which is just basically 0,0,2,1,1, the whole thing.

Viviane Clay: Is there any notion of it being nested with the things plotted on top of it, or is there no parent-child relationship?

Ramy Mounir: I don't think there is. I think Veto treats all of these renderers equally.

Viviane Clay: There's just the order in which you add them. They are layered on top of each other, but there's no dependency on how they can access each other's data?

Ramy Mounir: No, there's none. When you want to add an object to a specific renderer, you would say self.plotter.add.render, and then add. You're finding that sub-renderer and adding to it.

Viviane Clay: If you wouldn't add the very first one, what would happen?

Ramy Mounir: It will probably go to the first renderer. Usually, when you don't do add, I think it just goes to zero by default.

Viviane Clay: If you don't do the 0,0,2,1,1 plot, and only do the two axis windows, do you always need the full-screen background?

Ramy Mounir: I don't really know what happens. I could try it. I don't know.

Viviane Clay: No.

Ramy Mounir: Usually, just the final uploader. I think it will just go to... you might not have access to adding objects in that background.

Hojae Lee: If you don't define anything, it's the full screen, naturally. If you don't have any renderers, you would be using all the defaults. If you don't have the first one in the render areas, but only have the small screens, then you'll have a main window with only information on those small screen areas, which is a little bit awkward.

Ramy Mounir: So you wouldn't be able to access the first plotter, so you can't really add to it.

Hojae Lee: These are just windows into data, and they don't have any relationship. It's like three computer screens showing.

Then you're saying, in computer one, I want to show this, in computer two, I want to show this.

Viviane Clay: So the first one is not treated any different from the other ones.

Hojae Lee: Nope. It just happens to be full screen, but you don't have to.

Viviane Clay: Okay.

Hojae Lee: It makes it so you can have an overlay feeling. You've subdivided it, but the second and third one are actually covering from the first one, so when you're plotting, you want to make sure it doesn't overlap in a problematic way.

Viviane Clay: Okay.

Ramy Mounir: One other thing to notice is that I'm setting interactive. The interactive call, once you say that this show is interactive, will stop processing any code after that. Any changes to the UI will only depend on the events. If you interact with something, this would be the last statement here; anything after that is not used, because the code stops here. This is why I'm making the first two not interactive, and the last one interactive. Any changes to the UI after this line will be through events, like a slider change that calls a callback. When you set this, make sure this is the last statement.

Okay, so that's basically the setup. You have one plotter, and then you have two on top of that.

So let's start with creating the first widget, which is a slider—the episode slider. Down here, I'm showing a video displaying the topics that get published when I change the slider. This is just a demo to show the benefits of debouncing and deduplicating; it's not the final goal. That's what happens when you define this widget.

If we want to do this, let's go to the commit. At a high level, I added a class called EpisodeSliderWidgetOps. You can name it whatever you want, but it needs to have some functions. I also modified the interactive plot to add this widget. The only thing I added here is a piece of code that calls a function, createWidgets, and I added the widget in this specific pattern. We'll talk about it in a second. I also go through the widgets and call the add function on that widget class.

If I want to set a state for that widget, for example, set the episode slider to zero at the beginning, I can do that here as well. You can do whatever you want; this is just my way of doing it.

In createWidgets, every widget we add is just a block like this. There's a widget class. Let me zoom in. These are types; we can ignore them for now. I'm saying the widget is a slider, and its state should be an int, but that's just for type matching.

The widget class takes five things. It takes widget ops, which is the most important part. That customizes the widget—it defines that this is a slider, how to add it, how to remove it, how to extract or set its state, and the topics. When you define widget ops, that's what makes this widget unique. This is the brains of the widget, and that's the class we defined at the top. We'll get to that in a second. The widget class also takes the event bus (the publisher and subscriber), the scheduler for debouncing, and some other variables. I'll talk about these in a second, but let's focus on widget ops.

As the name suggests, widget ops are widget operations. It's a class. The way I've created it, it doesn't really have any requirements, so the protocol for widget ops is empty. If you look at WidgetOps, the protocol is empty. The reason I'm defining it this way is because I'm adding other capabilities on top of that. Some widgets don't need to publish; others do but don't need to listen to topics. Some don't need to set or extract state because they don't have a state. All of these are capabilities that, if they exist, are detected during type matching. If a function is available with the right signature, then this widget ops is also an instance of supports add. If that's the case, it will call the add function and do the corresponding actions. If you have a stateToMessages function, it will publish the messages you put in stateToMessages. Otherwise, it doesn't publish anything.

Let me give you an example.

Niels Leadholm: At a high level, this is useful for type checking.

Ramy Mounir: It is type checking, but I'm also using it to dictate widget behavior. If it type checks against, for example, hasUpdaters and finds that function, it will do certain things. If it can't find that function, it just returns an empty set. You can use those in the widget.

Niels Leadholm: Yeah.

Ramy Mounir: Yeah.

Niels Leadholm: Thanks.

Ramy Mounir: True. We'll take some time to go through the first one, and then the next will cover the modifications and changes—how the step is different from the episode, and so on.

I create a function called createLocators, but you can create it however you like. This is where I define the locators.

In this case, I have a single locator with one path and one step, which is episode. I'm going to use that to query how many episodes we have, so I can define the range of the slider. This locator goes into self._locators and stays there for use throughout the code.

I have add, extractState, setState, and stateToMessages. These are the main functions I need. Add is where we add the widget to the plotter. If add exists, it calls that function, which only happens at the beginning.

We call add, it looks for this function, and if it exists, it calls it. Every widget is different, but the way I want to do this is by using the locator.

I'm going to get the locator for the episode and query how many episodes we have. I can use that to modify the X max for the range of the slider, and then use this VDO function to add a slider to the plotter. I'm using plotter 0 because that's where I want my episode. Addslider requires a callback function; when the slider changes, it calls this callback. My widget class creates a callback for it, and in the add signature, it gives you a callback function you can pass directly. When the slider changes, it calls this callback, so the widget class knows the slider value has changed and can publish or process as needed through the callback function defined in the widget class. If you're just defining a slider, you can pass this callback to the addSliderCallback function, and it will work fine. I have to do it this way because I need to debounce those messages, which I'll discuss in a second.

This is how you add and then render. If you change anything in the visualization, you need to render at the end. That's add. There's extract. I have helper functions for common tasks like slider state—setting or extracting slider state. These helper functions take the widget and know how to extract or set the state if it's a slider. It's just a series of checks.

For state to messages, if you're going to rely on the state, you need to tell it how to extract the state. If what you're going to publish relies on the state from the widget class, you need to have an extractState function. When it's ready to publish, it extracts the state using extractState and sends you the extracted state. You can define this value however you want; this is how I'm doing it within the widget class.

Viviane Clay: When should you pass something in that state variable versus just doing self.whatever on the class?

Ramy Mounir: I think that—

Viviane Clay: In some of your other example code, you did self.episode or something?

Ramy Mounir: Yeah, if the widget has a state. Sometimes widgets can have multiple states. For simple widgets like an episode, it's easy to use this functionality. It extracts and defines exactly how to get the state from the slider and provides that state here. Sometimes the state is more complicated. For example, if you're selecting a hypothesis and sending a whole pandas DataFrame or series, you can ignore the state and pass in a state defined within widget ops. You can define your own states within widget ops and specify what to return when publishing. Whatever you put in the value is the message sent. It could be the state from the widget or something else, like true or false.

Viviane Clay: Cool.

Ramy Mounir: That's really it for the episode.

We've edited here and defined the widget ops. All the others follow the same pattern. I'll add another widget, define its widget ops, and that's it. If you want to extract functionality, you can take the whole widget ops, move it to another plot, and that's how I created this tutorial.

Let me explain debouncing and deduplicating. First, deduplicating.

The difference here is that in the widget class, I'm setting deduplicate to true, which means if the state is the same, it doesn't send a message again. Previously, even if the state was the same, it kept publishing messages, which could trigger expensive callbacks and make things non-responsive.

If you don't want that, set deduplicate to true, and it will only send a message after the state changes.

Niels Leadholm: In this case, it's not clear in the video, but the 0 to 1 only changes at the midpoint.

Ramy Mounir: Yeah.

Niels Leadholm: For the first half of the bar, it's all zero.

Ramy Mounir: Yep.

Niels Leadholm: As you showed in the example, because the bar was moving, it was publishing loads.

Ramy Mounir: Yep.

Exactly. If we keep moving between 0 and 1, it will still publish a lot. For example, if you have 50 episodes and each episode changes the mesh, which is an expensive operation, moving between them quickly becomes non-responsive because the state is actually changing. That's why I need debouncing. Debouncing postpones the firing of the message until you become inactive.

With debounce seconds greater than 0, if I move between 0 and 1, it doesn't publish until I stop moving for 0.3 seconds. It's like a throttle, but the logic is different.

I use this a lot because I don't want to send a message as I'm moving from episode 0 to episode 5. I want it to wait until I've stopped.

Niels Leadholm: I remember you saying it was lagging, particularly with point clouds and meshes, if every time the slider moved.

Ramy Mounir: It was lagging, and depending on how expensive the call is, it will just do it recursively. If you move very quickly, it will reach recursion maximum depth and fail. This is helpful.

Okay, I don't know how much time I have—maybe 2 minutes—but let's continue.

Niels Leadholm: No worries if you go a bit over.

Ramy Mounir: Maybe just 10 more minutes.

Niels Leadholm: Yeah.

Ramy Mounir: Let's add a new episode, a new slider here, this step. These will go quicker because we already know the pattern, so let's go to the commit.

The only thing I added here was widget ops for the step slider, and I added a new widget class for it.

I'm giving it this new class for the widget ops, setting debounce to 0.3 seconds, and deduplicate to true. That's the only change here. Now, we have a difference: widget updaters. This is something we didn't have before. The widget updaters for this step are simple—I'm going to listen to the episode number, and if that changes, I'll call this callback function. The callback is defined here as one of the updaters. Let's update the slider range. I'm just passing this callback. Updaters work with a specific signature. When you call an updater callback, you want to modify the widget, so you give it the widget itself to modify, and a list of the messages you received—all the ones you were listening to. All the required ones are sent. Right now, we only have one, so this list will just contain that message. All the updated messages are here, and you get the widgets. You define what happens to the widget based on these messages.

We got the episode number in here, so I'm going to decode these messages from the topic message into a dictionary. I find it easier sometimes to do that. I'm going to change the widget range. It's now going to start at 0 and end at this value. This value comes from dataparser.query to get how many steps we have. We went over queries before. This is my data parser. In the data parser for step, it doesn't have episode number because I don't know what the episode is. I'm looking to get the step, so I'll query this by giving it the episode number I receive. These are constants, so I'm providing those, and it will give me how many steps I have. Once I do that, I'm setting the widget range to that and setting the state of the widget back to zero, because once the episode changes, I want to reset it. I return the widget, always returning the modified widget. That's the pattern for all these callbacks.

I also send back a true or false. When I send back true, it publishes the new state. When I send back false, it doesn't publish. This is the whole pattern.

Viviane Clay: Maybe I missed this, but why are you calling plotter.add to 0? I thought 0 was the blank screen.

Ramy Mounir: Yes, because this slider is on the first—oh, that's on the background. For the next two objects, we're going to call plotter.add1 and 2. The slider is on the background.

Niels Leadholm: Just out of interest, how clever is Vito about positioning those? Does that take a lot of tweaking in practice?

Ramy Mounir: No, I think it is actually very smart. For these numbers, like 0.12, when I say 0.1, that's the position of the slider. When I say 0.1 on the X to 0.9, it scales with the size of the renderer, so it's nicer. You can move this whole thing in a sub-renderer, and it will scale and work nicely. It is smart in that respect.

Niels Leadholm: Okay, cool, thanks.

Ramy Mounir: Sure. That's it for the slider. If this works, we should have something like this: when you change the episode number, for example, episode 0 has 27 steps. If you change the episode number, it will go back to zero, and when you check, it will have 30 steps. It's already updating the step because it's listening to that topic. Okay, let's go to the—

Hojae Lee: About the smart thing—the positions of the sliders can be smart, but for little things, like the numbers, you can make the numbers show up or hide them. I found that out, but you can't really control where the number is placed; you can't put it on the bottom or change the spacing. I had a situation where there was a number, but then I had a button on top of it, so it was hiding the number a bit. I had to manually increase the button height. Typical plotting problems, but you don't have full control over every aspect, just FYI.

Ramy Mounir: Yeah, so if you want more control, this is a wrapper over VTK. VTK is created by Kitware and it's very good. It's just a steep learning curve, so it's not very easy to learn VTK, but if you want to customize more, VTK is the way to go.

Okay.

Let's create this here. This is Flutter 1, index 1. As we change the episode, it changes the object, the mesh, the primary target, and as we move the step slider, it changes the sensor position. We're going to query that from the data parser and display it.

Again, it's the same exact pattern: I added a class for the ground truth mesh widget, and we added that down there for the widgets. What we're listening to here is we have updaters—two updaters, one that will update the mesh. One listens to the episode number and updates the primary target. Another listens to both the step number and the episode number and updates the sensor. This is the moving sensor. The locators are a bit more involved, but this shows how easy it is to get data. I've created four locators. The target is here; this only is missing the episode.

The steps mask is needed to process the sensor locations. When I get the sensor location, I'm getting it from the SM steps, so I also need to know which ones have been processed, which I get from the steps mask.

The missing value here is also episode. Here, the missing value is episode and the SM step. When I call this, all I need to give it is episode and SM step. I also have the patch location, which I'm getting from this path.

When it's time to update the mesh, this only listens to the episode number. I'm just removing the old mesh and adding the new mesh. I'm calling the YCB loader, which I mentioned earlier. I give it the target ID, a string of the mesh I'm trying to load, and it creates the widget for me. I rotate it based on information from the data parser, then shift it and add it to the plotter. Here we're using plotter.add.1, and then I render that plug. That's it. I don't want to publish anything; I just return the widget again and false.

That's how you update the mesh. To update the sensor, it's similar, except now I'm updating the sensor. In the init function, I created these variables: gaze line and sensor circle, which are the red sphere and the gaze line. They're empty right now, but they'll take a line object and a circle object.

I think this is wrong; I need to change that to sphere. Updating the sensors is as simple as that: getting the messages, getting the sensor position and the patch position, and updating the sensor circle and the gaze line to look at the correct place.

Niels Leadholm: And what was the return bool again? The second return?

Ramy Mounir: Basically, do we want to publish the state after we update the system?

Niels Leadholm: Okay, thanks.

Ramy Mounir: Yeah.

That's it. That's really all it takes to create this visualization.

Let's do this last one quickly.

Again, the same kind of pattern. Just added a class for it.

The updaters here are going to be listening to the episode number and the step number. If either changes, we update the MLH. It calls the update mesh. I'm defining a sensor circle here—this is the object for the sphere, not a circle. I'm adding a bit of text to the plotter at 2, just at the top, which says MLH. The locators are simpler here because I only need to extract the MLH, so I'm defining that this MLH depends on the episode and the step. Both in the middle are already fixed: the current MLH and LM0. If you have a slider, you can also change LM0 to something else. Update mesh is the only function I added. I remove the widgets that already exist—the existing widget for the object and the sensor circle.

Then I extract the MLH by giving it the episode and the step. These are the MLH values. It's a dictionary when I extract it, so I'm getting the graph ID, rotation, and location. I add the object, rotate it, shift it into position, and add the sphere for the sensor circle. Then plot. It's as simple as that. I copied all of this code from other plots, so I know it works by just copying it over. As long as you connect them through these topics—episode number and step number—if you use that everywhere, you can reuse the functionality. If I'm copying a widget from a visualization from Hoji, and she's using episode num, I could just rename that if I wanted to. It's not a big change. As long as you use those, it should be reusable.

That's it. If you do that, you'll have this visualization. It's a bit of code to add all of these classes, but it makes it easy to extract functionality and makes the code very readable. You can go through the code and see what's going on. I think this is all.