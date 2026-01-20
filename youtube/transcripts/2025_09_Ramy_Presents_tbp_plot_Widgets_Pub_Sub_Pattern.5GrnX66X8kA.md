Ramy Mounir: Yeah, so this is going to be more of a high-level presentation, but I'm also going to go into details about some of the, Tricks, just, the tricky parts, and how to come up, put together these visualizations together, and, use the widgets, and... The widget updaters and all of that stuff. it will go into the PubSub, and... Also, accessing data and all of that stuff.

you've all seen some of these interactive visualizations, how, basically using an episode, or using some widgets, you're able to control other widgets. Some of these are interactive, some of them control others and others, and some of them also only depend on others, and they don't control other widgets. So there's a... there's definitely some communication going on between these widgets. And in the past, I've... I've... when I started building these visualizations, I had all of those especially the ones that depend on each other, or send messages to each other, they needed to be in the same class. Or at least they needed to have some reference to be able to, talk to each other. for example. this is a subset of, the kind of messages that need to be sent, or, the dependency graph. Basically, the episode is going to control a lot of widgets. For example, the episode here controls this ground truth mesh visualizer, it controls this figure, it controls the... info widgets here, and a lot of others. what ends up happening is that you end up creating a huge class with a lot of these widgets. Very tightly coupled, and if you want to extract some of this functionality and move it to another plot, it's... it becomes, very difficult to do so. the idea here, with introducing PubSub is that we can actually decouple all of those dependencies. So when the episode changes, we don't define what happens when the episode changes. Instead, we just say, okay, the episode's just going to publish a message on the topic episode number. And then any other widget can subscribe to that topic, and say... and see, for example, that the episode has changed, and do stuff In their own class. we can now decouple all of that, communication. So again, here, with direct communication, basically. an episode directly controls other widgets. If you have widget 1 maybe as an episode slider, it directly controls some of these. if you want to add a new widget that depends on widget 1, you'd have to go into the callback function of when the episode changes in widget 1, and modify it so that it talks to Widget 5, or something like that. And this just makes it very difficult to add or remove any new widget, but also to extract functionality and reuse it somewhere else. That's what PubSub models give us. So basically, you can think of these as, the topics in the middle here as like a broker. It's... so you basically... the publisher, it only publishes... it only knows that its topic name is episode number, and it publishes it on the... on the... event bus, or the broker, basically. And if you have any subscribers to that topic, the message will get relayed to them. If you don't have, then the message will be lost, basically. So that's the idea. So you can basically very easily add a new subscriber and say, okay, I want this subscriber to depend on topic 2, or I want it to depend on topic 1 and 2, and it just listens to those topics. And then you can take that subscriber and move it to another plot, and as long as Someone is publishing those messages, then it should be able to work fine. And these are all split into different classes, so you could just copy that whole class, move it somewhere else, and it will work. I'll show an example of this at the end.

Niels Leadholm: Yeah, and maybe you'll cover this in a bit, but in terms of, the one-to-many Publisher to topic.

arrows, so is that... how complex can a topic be? Because naively, I would imagine a topic is just one variable. And it's just passing it into this kind of... Yeah, almost like a global namespace, but...

Ramy Mounir: You could publish multiple things if you want, it's... usually what I've used it for is just publishing one, on one topic, just to say, basically the state of this widget is this. But you could... you could publish multiple things on different topics. It depends on how you want the, resolution or the... this... for example, you could publish The, a hypothesis? on one topic, and just say this is the hypothesis, or you could publish it on multiple topics and say this is the hypothesis location, and this is the rotation. So that, if you have this granularity, then you can have multiple widgets only using this part, only listening to one topic and not the other. So it depends, really, on the granularity that you want to have.

Niels Leadholm: And I guess you could also have, two publisher widgets that affect a particular topic in the same... in different ways. I guess if the topic is, step number. then changing the step slider changes that. But also, if you change the episode, presumably that tends to change the step to zero, or something like that.

Ramy Mounir: Yeah. So the way I do it is that I make the episode change the step, and then the step publishes a step number again. it goes into this loop, but.

Niels Leadholm: Oh, okay, so it... okay, because that does seem maybe a bit cleaner. So then it's... it's a published topic. subscriber, and then it has its own publish to change the step. So then it wouldn't really be two arrows like this, it would be, like you say, like a loop.

Ramy Mounir: Yeah, The problem with that is that it... it can sometimes... because it's a loop, so the... Yeah, it takes more time to get to the equilibrium, basically, because the... once you... if the publisher sends to the step number, and then the step number changes and publishes, that takes two steps. It's like message passing in graphs.

Niels Leadholm: Yeah, okay.

Okay, interesting. So is there almost, an upper bound on the number of message passes? That are allowed before.

Ramy Mounir: I don't have that, but it's just... sometimes you'll see a lot of things changing, and they'll just reach as equilibrium. That's when I know that, but we can have debouncing to get rid of this as well. I've been thinking about it, but it's not really an issue so far.

Niels Leadholm: Yet. No, that's interesting.

Ramy Mounir: but there are actually some, I can have multiple publishers or multiple widgets publishing the same topic, just like here, for example, in here, I have these, the primary target, and then these arrows. These are 3 different widgets, these are 3 different buttons, but they're really changing something, that topic called current objects, which is, which hypothesis space are we looking at? Because you could be at an episode and a step, but you want to change which hypothesis space you're inspecting. It could be you want the mug, or you could want something else. the primary target always resets back to the... to the primary target of the... of this episode. And these can move, right and left, so they cycle through the objects, the hypothesis spaces. So they all can publish to the same, current object topic, so that is sometimes useful, right?

But anyway, so we have these, So we can look at this here as just a collection of widgets, and these widgets, like I said, they're independent, they only talk to each other only through the PubSub topics. So you can move them, take them into a different plot, and... re... reuse the functionality.

So let's go through some examples before we go into the actual code. if we just look at the episode, slider can... in this case, we only wanted to output an episode number, right? the way that I've defined this in code is using something called a state to messages. the widget class is going to call these function names that I've defined. So this is the pattern that I'm using, but I'll go through that later, but the only thing that we need to know here is that this is like a payload function, so that's where you define what topic is being published, and what is the value of that message on that topic. what message is being published, and what the value is. And we'll get more into details about this later. But the episode only publishes the episode number, and that's what we see here. It can publish multiple things, but right now it just only publishes the episode number. If we go to the step, now the step receives the episode number, and it publishes the step number. So publishing the step number is exactly the same way. I have the state two messages, and I'm just telling you to publish step number.

But receiving is a little bit more complicated, because I wanted... So I created these widget updaters, and you can have multiple updaters, you can have... There are very... there are a lot of scenarios where the widget can change based on what it's listening to, and sometimes you'll have multiple updaters, or you'll have one updater, you'll have Sometimes you have one updater that listens to multiple messages or multiple topics, and when it has messages, enough messages in all of them, it can update the step widget. In this scenario, we have one updater. What it's doing is it's listening to episode number. And once it gets a message, or if the episode number changes, it will call this callback function, which is, it's going to update the range, basically. because we have, episode 0 could have 50 steps, episode 1 could have 20 steps, or whatever, so we need to modify the range of the... of the step slider.

once the episode number changes, it calls this callback function. So that's a simple example here. Let's go to more complicated examples, like this correlation plot, for example, here. What's happening here is that this one is listening to four, topics. Episode number, step number, current object, which is basically what... which hypothesis space, and it's getting those from the buttons and the arrows that we had before. But also age threshold. So it's listening to those four, and if any of those change, it will call the function, updatePlot. Which is going to modify this widget. This is why I call them widget updaters. The only way you can modify the widget that you're on is through widget updaters, by listening to some Some topics, or some messages.

Niels Leadholm: And.

Ramy Mounir: go ahead.

Niels Leadholm: And just to clarify, And each widget, would it always have one widget updater, or could it potentially have multiple?

Ramy Mounir: It can have multiple. I have an example for that, but you can have multiple updaters, or you can have no updaters if you... for example, you're not listening to anything, but you're only publishing, just like the episode slider. It's not listening to anything, but it's only publishing The... which episode you're on.

Niels Leadholm: okay. And then, Yeah, maybe, again, it'll be an example of this, but I'm just curious now, so with the topic, so yeah, here is an example where if you change any one of these that's listening, it will Call the... callback.

Ramy Mounir: Yes.

Niels Leadholm: Presumably there's also a notation for if All four of these must change. In order to call the callback?

Ramy Mounir: Yeah, or, multiple...

Niels Leadholm: Couple of.

Ramy Mounir: required here, basically. if you list a topic, that means that if any of these topics change, you will call the callback.

Niels Leadholm: Okay.

Ramy Mounir: Required means that the... this topic is not really required for UpdatePlot to... to call it Zoom, right? Sorry, did you hear that noise, please?

Niels Leadholm: Yeah, I know.

Ramy Mounir: So basically, so required is basically saying that, I need to have this topic in my... in the list of messages that I send to update plot. So if you set it to required, then it's not going to call update plot until all of these messages are available. But, if you... but just by listing them here, if anyone, if any one of those changes, that basically says, call update plot. It's a... it's a... it's a tiny detail, and it's... In most cases, you only need required to be true. I have... I only needed it for one case, but, Yeah, it's a... it's a... I don't think it's worth time going through it, because always required is true is usually, sufficient.

Viviane Clay: Is there a difference between the variable changing versus the variable being available? I assume only one of these will change at any one point in time, but you need all four of them to update.

does it check... Oh, is this value in the middle circle right now available? And that's what the required...

Ramy Mounir: Yeah, so... the widget updater is going to keep an inbox of all of these. So it basically stores these messages, and only when all the required messages are available, it will update the plot. Sometimes you don't have, sometimes episode number is not... is not yet available in the inbox, but one of these change. And you still want to update the plot. that's the difference. sometimes you don't have episode number yet, and update plot doesn't really depend on it. you'd still send the message if... Step number changes, for example.

Viviane Clay: But if, all of them are available, but none of them have changed.

Ramy Mounir: Minimum.

Viviane Clay: blood.

Ramy Mounir: No.

Viviane Clay: Okay.

Ramy Mounir: Only when... only when it changes, because it's just going to be the same function being called again and again, doesn't matter. It doesn't...

Niels Leadholm: And and then the logic for all of them being required, that's specified in the inbox? If, if you... if you wanted that to be the case.

Ramy Mounir: yeah, so that's... the logic for this, inbox stuff is in the class of the widget updaters, and... You basically just set it to required equals true, and it will not send a message without all these four, basically.

Niels Leadholm: Oh, okay.

Ramy Mounir: Did I answer your question? Okay.

Niels Leadholm: Yeah.

Ramy Mounir: Now, the output, which is going to use, again, the state to messages, and again, you can really just, change, so you can customize this as much as you want.

So... here, I'm just sending out two messages. Sometimes, if I don't have a selected hypothesis, I send a message... I send a... on a topic called clear, selected hypothesis with a value of true. You could... or you can just say selected hypothesis with a value of none. It really depends on what... what you want to send. So this is, a payload function that can just... Take your... take the state of the widget, and you can modify it, or do anything to it, and then just... Send it.

Hojae Lee: Is the state to message supposed to be, like, a protocol? it must take in some state, and it must return... Some iterable autonomic messages.

Ramy Mounir: You can't just...

Hojae Lee: return at random. things,

Ramy Mounir: Yeah, it has to return a list of topic messages. Which is, because every one of these topic messages, it's going to iterate over them, and it's going to publish it. That's in the widget class, it's doing that. Here, you're just defining the payload function, but when you return those, it's going to go over those. And then the state doesn't have to be... I have this notion of a widget and a state, and the state of Some of those... it makes sense for some of these widgets to have states, for example, the slider, the state would be the value of that, or the button would be the value of that. Some of those widgets, they don't necessarily have a state, so it will... if it doesn't have a state, it will basically return sometimes none. Like this, and you just put whatever state you want in here, when you're defining that.

Hojae Lee: Okay, but it is, a very minimal contract that must return some editables of topic messages.

Ramy Mounir: Yeah, because all these messages are going to be published. if you don't have any messages to send, just return an empty list.

Hojae Lee: Okay.

Ramy Mounir: Or just don't have state-to-messages at all.

Okay, here's another, slightly different example. This one doesn't publish anything, so we don't have state-to-messages, but we have updaters. And this is one example where we actually need more than one updater. And the reason is. we need one updater that's going to update the mesh, and this one only listens to episode number, this, because this is the primary target mesh, so it only changes with the episode. if the episode changes, the primary target changes, and we want to update the mesh to some other object. But then, we also want to listen to episode number and step number, so if any of those change, we want to update the sensor on the object. we want to move the sensor to a new location. And I do this because if the step number doesn't change, I don't really need to update the mesh. It just... it doesn't make sense to do that. I have split the update mesh and update sensors, and I'm just defining what topics they need to listen to.

Niels Leadholm: Yeah, nice.

Ramy Mounir: Okay, so... that's basically a very high-level view, of, these, and... We can now go to, we can discuss more, on, low-level details of these things. These are the topics I plan on discussing. The first thing is, it's not really related to PubSub, but it's more related to TBP plots, or some helpers for accessing data, JSON data, from the detailed run stats. And then I'm going to talk about adding a plot into the registry. How do you register that plot using the CLI interface, which is pretty cool. And then creating widgets with widget ops, this is more involved. And then there are some tricks that I'm going to discuss about debouncing and deduplicating events, because we don't really... sometimes it becomes very, Yeah, so if you're changing the slide... the slider, value, it... it can just keep sending on messages, because every... every movement is just changing the value. So we don't want that, we want to gate, all of these outputs, and only send messages when necessary. That's... this here is going to touch on that.

Viviane Clay: Do all of the, it always depends on JSON files being logged?

Ramy Mounir: Yes, right now it does, but that's only part of it, so if you have another way of loading the data, it doesn't really need to depend on JSON.

you'll see I'm using something called Data Locator and data parser to parse the JSON and locate data, but if you are doing this online, then you can just have a different type of data locator.

Viviane Clay: Okay, cool.

Ramy Mounir: I've added a tutorial, for accessing data. It's right here. Which basically goes through this, the same stuff, but I'm going to, go through it again.

So basically, we have a structure like this. This is a very simple structure. Usually, our JSONs are much bigger, and they're, like, I don't know, 7, 8... the depth of the structure is usually a lot more. So this is why it's useful, but let's take this example here, a simple example. We have just a simple example, we have a dictionary, we have, one level here, we have the episode numbers, and then for every episode, we have a list of Dictionaries. second level is a list, and then the third level is another dictionary. if we want to access some data here... I def... so the way that I do it is I define a data locator, and in this data locator, I define all of the steps that I need to reach some data somewhere. So I say... so it's usually either a key or an index, a key for dictionary and an index for a list. So I say, this data locator has a step that is a key, and I'm gonna call it episode, and I'm gonna give it a value of episode 2, and then the second path step is index, it's going to be step, and value of 3, and then key. I'm gonna call it field, and I'm just going to get evidence. So if I run this with the parser, and I just say extract, and I give it the data locator, it's going to return the value. Basically, 0.5, which is... where we are. Now you can reuse that locator, but it's not really useful if you can't... Either quickly modify this data locator, or define it in a way where you can... where you know that you're... a lot of these are constants, and you just want to define the missing values.

I rarely use a full locator path like this, because... every data... all the data that I'm extracting really depends on some slider value, or some button, or some... something. I don't know what the episode is until I... I get the episode value from the slider. So what I ended up doing is, you can define the same locator, but you... in a partial way. This is inspired by partial functions from Python. So basically, what you would do is you would not specify a value here for whatever step that you're missing. So here, I don't know what the step is, and I'm going to rely on the slider later on to get it, so I can just keep that missing. And I can call the same function, parser.extract, and I give it the partial locator, and... And then now the step that I want. So you don't have to specify all of these steps again. So that would be the idea. And then, it returns... give it 70, 1, 2, 3, whatever, it will just return the right value. The other cool thing that you can do with this is that you can query the available options here. So instead of just having, Instead of extracting data, you can query what available episodes are at this step. The way this works is that you would have missing values, when you don't... you don't really know what the value here for episode is, and parser.query instead of parser.extract. This one will just go through these steps, and it will stop at the first missing value, and it will tell you these are all the available options for you. So you could use that to, It's useful when you're deciding, what is the range of the slider, or if the slider range changes based on... the step range changes based on the episode. You could use that to... to always query how many steps you have, or how many objects you have, what are the objects, stuff like that. But if you give it... if you give it an episode number, it will basically go to the next missing step, and it will give... will return to you the available options. for episode 1, we have three steps, 0, 1, and 2. For episode 2, we have four steps, 0, 1, 2, 3. Okay, I think this, this first part, I thought instead of just, going into the widget ops and all that stuff, without an example, I thought we could build this, make it as a tutorial and build this together.

so by the end of this, I think I have 30 more minutes of... yeah, maybe in 20 minutes we'll be done, and we should... Have built something like this.

and then if I didn't have enough time to finish it, these are... these are the commits. So I basically, I will share the slides, and you'll be able to, for every step, you'll be able to go through... you'll be able to find this commit and find the code for it. But it's basically... the first commit is just an initial setup, where I just set up the renderers and the CLI arguments and all that stuff, and then each one of these later commits are one for each widget. So there's one for the episode, one for the step, and one for this visualizer, and one for that. And you will see that, the diffs will show you that I don't modify any of the code of the previous commit. if I want to add the step, I don't modify the episode at all. If I want to add this, I don't modify any of the others. I wanted to split them like that so that you can see that there's no dependency going on.

Cool, so let's start with the initial setup.

renderers, so... this here, what we want to set up is... I don't have any widgets, I just have, three renderers. There's the main renderer over here, and then we also have two more, sub-renderers, or... they're also... renderers, they're just, in total, we have 3 renderers. And you create a new renderer every time you want to have a different camera, basically. if I want to have a different camera for, this... for this sub-renderer. I just basically have to create it as a renderer, otherwise I won't have a camera for it, and I can't move in this render independently from the others. So let's go to the setup for it.

the setup here is very simple. In order to register a plot. all you need to do is define this... there's any... a function, give it any name, I call it main, and I just register that plot with some... with this decorator, the registered decorator. And you just... this is the name of the plot, this is what you're gonna use in CLI to, plot it. And then a description, and this description is going to show, when you query all the available plots, it's just going to tell you this plot, and it does this plot, it does this. And then, if you have any arguments that go into the main function, you can define them here in a different function, and you have to decorate it with attach args, and give it the same name of the plot so it knows how to match it. And then it basically just adds these arguments, and the names of the arguments have to match, right? experiment logs there needs to match here, and... You get the point.

All of the code needs to fit inside of this main function, because this is the only function that's going to run, and you can dump all the code here, but I like to create an interactive plot class and run it... run the interactive plot class, so everything runs in the init of this class. But if you're doing a, a matplotlib or seaborne function, you can just put this stuff here. Doesn't matter. So this is the interactive plot. This is where I create the renderers. For example, so I have, like I said, I have 3 renderers. I learned this trick from Jose. It's actually very nice to be able to specify the render shapes inside the plotter. I used to do it because this shape here takes different ways of defining the renderers. You could do. to... a forward slash 1, it will just give you three renderers, it will split it into three views, and then two on the top and one at the bottom, or... there are different ways you can specify the shapes, but this is actually very useful.

renderer areas, you can say, okay, my first render is the whole screen, 00211, and then you can have two more renderers, like this.

the things that I'm defining here, and I usually just define all of them, except for maybe this one. Which is the YCB mesh loader. This is... I only use this when I want to load a YCB object from the dataset. Not something that... not a Monty model, but rather a YCB object. It's a class that makes it very easy. You just give it the graph object name, and it will just return to you a video mesh.

Data parser, this takes a path to the... to the log file, the JSON log file. publisher, this is the PubSub publisher, and this will be shared with all of the widgets later on, that's how they communicate together. They all have access to this event bus, then they can all publish and subscribe to the same topics and all of that. the plotter is a veto plotter, that takes the renderer areas. The scheduler is, the debouncer, the debounce, scheduler thing. I will talk about it in a minute or so.

And then, after you define all of these, you want to show the renderers that you have. we've defined three renderers, so we can go through them and show them. These renderers, they take, options. first of all, you can do, when you do at 0 or add one, that is basically saying, I want the first render, I want the second render, and In the same order that you defined them here.

And then you need to show that renderer, And if you want to show axes like these ones. Do you see my screen when I go between the PowerPoint and the...

Niels Leadholm: Yeah.

Ramy Mounir: Okay, so if you want to show axes like these, you need to provide that in the show function? And you can actually show, you can define the ranges for these, like X range, Y range, and so on. I usually put the Y range in between 1.45 and 1.55, and you probably know why. And basically. You can define a camera as well, or you can set reset camera to true, which is basically going to, Reset the camera, and it will find the objects, and it will just reset the camera to a place where it can see all the objects. I don't... I don't like to set it unless I... I don't have anything in there, and.

Niels Leadholm: Wait, the reset camera, so is that something in veto, or something you implemented?

Ramy Mounir: That's a veto thing.

Niels Leadholm: And did I understand that correctly? You said it finds something it can see?

Ramy Mounir: Yeah, so it will reset the camera to the objects in the scene, or something like that. Right now, we don't really have an object, so what it does is just... it probably just goes to a default position and focal point. Yeah, so the way that you define those camera parameters is a position and a focal point. A focal point is basically where it's looking at, and the position is where it is. If there's nothing in there, it probably just goes to 000 or 001. I like to, especially the main plotter, I like to know where it is, so I define the camera, dictionary, and I set resetCamp to false.

Viviane Clay: For these...

Ramy Mounir: is.

Viviane Clay: The first one, is that the kind of white background, basically, or what does that correspond to?

Hojae Lee: screen.

Ramy Mounir: Yeah, the main plotter, which is just basically 00211, the whole thing.

Viviane Clay: And is there any kind of notion of that it's being nested with the things that are plotted on top of it, or is there, no relationship of, this is the parent-child kind of plot?

Ramy Mounir: I don't think there is a... I think, Vito treats all of these renderers equal, equally,

Viviane Clay: There's just the order in which you add them in that order. They are layered on top of each other, but there's no dependency on... How they can access each other's data, or anything like that?

Ramy Mounir: No. There is no, there's none. Yeah, this is why... so basically, when you want to add an object to a specific renderer, you would just say self.plotter.add.render, and then.add. You basically... you're... you're finding that sub-renderer, and you're adding to it.

Viviane Clay: Yeah, and if you wouldn't add the very first one, what would happen? Would there just be...

Ramy Mounir: It will probably go to the first renderer, so usually when you don't do.add, I think it just goes to the zero, basically, so add zero by default.

Viviane Clay: Oh, no, if you would not do the whole, Nick, you don't do the 00211... plot, you only do the two axis windows. do you always need the kind of full-screen background?

Ramy Mounir: Alright. I don't really know what happens, Yeah, I could try it. I don't know.

Viviane Clay: No.

Ramy Mounir: Usually, just the final uploader. I think it will just go to... It... you might not have access to, just adding objects in... in that background.

Hojae Lee: If you don't define anything, it's the full screen, naturally. if you don't have any renderers, you would be using all the defaults, I'm guessing. And then, if you don't have In the render areas, if you don't have the first one, but only have the small screens. then you'll have, a main window with only information on those small screen areas, a little bit awkward.

Ramy Mounir: So you wouldn't be able to access that, the first plotter, so you can't really add up to it.

Hojae Lee: These are just, windows into, data, and they don't have any, relationship... it's, 3 computer screens showing.

And then you're saying, okay, in the computer... in my... in computer one, I want to show this, in computer 2, I want to show this. Yeah.

Viviane Clay: Yeah, okay, so the first one is not treated any different from the other ones.

Hojae Lee: Nope. It just happens to be full screen, but, you don't have to.

Viviane Clay: Yeah, okay.

Hojae Lee: it makes it so that you can, it makes a, overlay feeling, there's, you subdivided it up, but it's actually, covering, the second and third one is actually covering from the first one, so... you want to make sure that, like, when you're plotting, it doesn't, But what? paper.

Viviane Clay: Okay.

Ramy Mounir: Yeah, one other thing to, notice here is that I'm setting interactive So the interactive call, basically, once you say that this show, is interactive. it will stop, processing any code after that, so basically any code after... any changes to the UI is going to only depend on the events, so if something changes, if you interact with something, but it's, You just basically... this would be the last... when you set it to interact, this would be the last statement here, where anything after that is not going to be, Used for anything, because the code really stops here. This is why I'm making the first two not interactive, and then the last one interactive. any changes to the UI or anything like that happens after this line is going to be through the events. a slider changed that calls a callback, and then something that changes, but the interactive call... when you set this, make sure this is the last statement.

Okay, so that's basically how you get... This... the setup here. You have one plotter, and then you have two on top of that.

So let's start with creating the first widget, which is a slider, the episode slider. I'm showing down here, this is a video showing the topics, I'm just, for the sake of vlogging, I'm just showing the topics that get published when I change the slider. This is not what we eventually want, but this is just a demo so that I could show the benefits of debouncing and deduplicating. But that's what ends up happening when you just define this widget. So if we want to do this, let's go to the commit. For it. From a very high level, you'll see that I have a class that I added, Episode SliderWidgetOps. You can name it whatever you want, but it's... it needs to have some functions. And then I modified the interactive plot so that I could add this widget. the way I do that is... the only thing I added here is, this... piece of code that... basically, I have a function that says createWidgets, and I added the widget here in this specific pattern. We'll talk about it in a second. But I also go through the widgets, and I call the add function on that widget class.

And if I want to set a state for that widget, let's say I want to set the episode slider to zero at the beginning of the code, I could do that here as well. You can do whatever you want, this isn't just my, My way of doing it.

in the create widgets. Every widget that we're gonna add is just going to be a block like this. I am... there's a widget class. Let me just zoom in. There's a widget class. These are types, we can just ignore them for now. I'm saying that the widget is a slider, and that the state of this widget should be an int, but we can ignore that for now, it's just for type, matching.

So the widget class takes five things. It takes a widget ops. that's the most important part of the widget, really. That is what customizes the widget. It just basically... it says, this is a slider, and this is how we add it, this is how we remove it, this is how we extract the state, or set its state, and also these are the topics and everything, when you define the widget ops, that's the only thing that really makes this widget that widget. This is, the brains of the widget. And that is the class that we defined at the top. we'll get to that in a second. But also, the widget class takes the event bus, which is the publisher and subscriber. It also takes the scheduler for the debouncing and the only debouncing. And then some other, variables. I'll talk about these in a second. But let's visit this one, because this is the most important part of the budget ops.

as the name suggests, this is a widget operations, basically. And, it's a class. that's... So this class doesn't really need to have, the way that I've created it, it doesn't really... Trying to find the... So, the widget ops doesn't... they don't really have, any requirements, in them, so you could actually... the protocol for widget ops is empty. So if you go to WidgetOps, you'll see that the protocol is empty here. But the reason I'm defining it this way is because I'm adding all the other stuff as capabilities on top of that, because some would just... don't require you to... they don't need to publish. Other widgets, they need to... they need to publish, but they don't need to listen to topics. Some widgets, they don't... you don't need to set state and extract state, because they don't really have a state. all of these are capabilities that, if they exist... what happens is that when we're, type matching. It will look for if this function is available with this signature, and if it does, then this widget ops is also an instance of supports add. And if that is the case, then it will do different stuff. So if you have ads, then it will end up, calling the add function and doing some stuff. If you have, has... if you have stateToMessages function, it will basically publish the messages that you... that you put in state to messages. Otherwise, it really doesn't publish anything.

Let me go back here and give you an example.

Niels Leadholm: And I guess, yeah, at a high level, that... this is useful for, Type checking.

Ramy Mounir: It is type checking, but I'm using it as a way of, So I'm using type checking to also dictate the behavior of the widget, because if it doesn't have... so here's how I'm doing it. if it types... if it type checks against, for example, if it... if it finds this function in there, I can use... in the widget class, I can say something like... If it's not an instance of hasUpdaters. So if it type checks against hasUptators and successfully finds that function, then it will do stuff. If it can't find that function, it will just basically return an empty set. So you can actually use those, in the widget.

Niels Leadholm: Yeah.

Ramy Mounir: Yeah.

Niels Leadholm: Thanks.

Ramy Mounir: True. Okay, I think we'll just take some time to go through the first one, and then the next one is just going to be... we'll just go... we'll talk about the modifications, the changes, basically, of, What the step is, how the step is different from the episode, and all the other ones.

I create a function here, create locators, you don't need that, you can create it in it anywhere you... any way you like it. So this is basically where I define the locators.

In this one, I only have only a single locator. that just has one path, one step, which is episode, because I'm going to use that to query how many episodes we have, so that I can define the episode, the range of the slider. So this is a locator, and it just goes into self.underscore locators, and it just stays there so that I could use it throughout the code.

I have add. and I have extract state, and I have setState, and state to messages. These are the main functions that I need. Add is basically... this is where we add the widget to the plotter, right? If add exists, it's going to call that function, and that only happens at the beginning, when we do this.

So we call add, it's going to look for this function. If it exists, it's going to call it. And what ends up happening here is that... and of course, every widget is different, but the way that I wanted to do this is that I'm going to use the locator.

I'm going to get that locator for the episode, and I'm going to query basically how many episodes that we have, and I can use that to modify the X max for the range of the slider, and then I can use this VDO function that adds a slider to this plotter. I'm using plotter 0, because this is where I want my episode. Addslider requires a callback function, because that's basically when the slider changes, it's going to call this callback. So my widget class... creates a callback for it, and always you're going to have to... in the add signature, it's just going to give you a callback function, so you can directly pass it here. What happens is that when the... when the slider changes, it's going to call this callback, and that basically... the widget class now knows that the slider value has changed, and it will do stuff and publish stuff if it needs to, or whatever. it just needs to go through this, through my callback function that I'm defining in the widget class. This is... so yeah, if you're just defining a slider, you could just pass this callback to the addSliderCallback function, and it will just work fine. I have to do it this way, because I need to debounce those messages. I will talk about that in a second, debouncing.

But yeah, so this is how you add, and then you render. If you're changing anything to the visualization, you just need to render at the end, of changing that. So that is ads. There's extract. I have helper functions for the ones that we use a lot, like slider state, or... so setting slider state, or extracting slider state. I have helper functions for those, so you could just use those. That basically just takes the widget, and it knows how to use the If it's a slider, it knows how to extract the state from there, and if it's a... And then it also, for the setSliderState, it takes a widget and a value, and it knows how to, set the slider state. It's just a bunch of checks and stuff like that.

And then the state to messages. There's really nothing here. if you're going to rely on the state, then you need to tell it how to extract the state, right? if you're going to... if what you're going to publish relies on this state that you're getting from the widget class. then... You need to tell it, basically, how to extract this state. So you need to have an extractState function as well, because that basically just What happens here is that when it's ready to publish, it will look... it will extract the state using the extract state, and then it will send you the state that it has extracted. you could just... use that. Or you could just have, You can define this value however you want, really. This is the way I'm doing it within the widget class.

Viviane Clay: When you... when should you pass something in that state variable versus just doing self. Whatever on the class.

Ramy Mounir: I think that.

Viviane Clay: Some of your other example code you did solve. That episode or something?

Ramy Mounir: Yeah, if the... if this widget has a state. Sometimes widgets can have multiple states, so I... I tried not to... So for simple widgets, like an episode, it's easy to just use this functionality. It would extract state and define exactly how to extract the state from the slider, and then it will just provide that state here. Sometimes the state is a bit more complicated than that. Let's say you're passing a... you're selecting a hypothesis, and you're sending a whole pandas data frame, or a series, or something like that. then you can just ignore the state, and you can just pass in a state that is defined within the widget ops. So you can define your own states within widget ops, and you can say. when I'm publishing, I just want to say, if that selection has been made, just return self.thistate. Whatever you put here in the value is the message that's going to be sent, basically. it could be the states, if you're relying on the widget, to... extract that for you, or it could be, something else. You could put in true or false, whatever you want.

Viviane Clay: Crew.

Ramy Mounir: that's really it for the episode.

We've edited here. And we've defined the widget ops. All of the other ones are going to be just this same pattern. I'm going to add another widget here. And I'm going to define it, it's widget ops, and that's it. So if you want to extract some functionality, you can just take this whole widget ops, move it to another plot, and that's it. That's how I created this tutorial, basically.

Okay, so let's go... yeah, so let me also explain the debouncing a little bit. deduplicating. first, deduplicating.

the difference between this and what we had before is that here, in the widget class, I'm setting deduplicate to true, which means if the state is the same. it just doesn't, send a message again, right? because, That state can, before, what was happening is, even though we're moving it like this, the state is the same, and it's still just publishing messages, and that if you have an expensive callback function that is triggered by this event. Then it's going to become, non-responsive.

if you don't want that to happen, you can set deduplicate to true. And it will just only send a message after the state has changed.

Niels Leadholm: Yeah, I guess in this case, because it's not that clear in the video, the 0 to 1 only changes at the midpoint. Yeah.

Ramy Mounir: Yeah.

Niels Leadholm: So yeah, for the first half of the bar, it's all zero.

Ramy Mounir: Yep, but...

Niels Leadholm: As you showed in the example, it was just because the bar was moving, it was publishing loads.

Ramy Mounir: Yep. Yeah.

Exactly. But if we keep moving between 0 and 1, it will still publish a lot, and that's another thing. let's say you have 50 episodes, and every episode is just changing the mesh. And changing the mesh is actually an expensive operation, so as you go between them, it will very quickly become very non-responsive, because you're changing from 0 to 1 to 3 to 4, and that's not a problem with deduplication. The actual state is changing. that's where... that's why I need debounce, debouncing. What debouncing is, it... it basically... Postpones the firing of the topic until... the firing of the message, until, You become inactive, and, so... basically... here, let me show you.

So this is with debounce seconds greater than 0. What happens is that I'm moving between 0 and 1, and it just doesn't publish until I stop moving for 0.3 seconds. so it's like a throttle, but different in the way that the logic works.

yeah, I use this a lot because I don't want to... I don't want to send a message as I'm moving from episode 0 to episode 5. I just... I want it to wait until I'm stopped.

Niels Leadholm: Yeah, I remember you saying it was, like, lagging, particularly with, point clouds and meshes and stuff, if, every... Time this, slider moved.

Ramy Mounir: It was lagging, and it also would, depending on how expensive the call is, it... it will... the way that this happens is that it will just do it recursively, so if you just move quickly, very, quickly, it will basically just fail. It will reach recursion maximum depth, and it will just fail. yeah, so this is, helpful.

Okay, let's, I don't know how much time I have, I think I have, 2 minutes, but let's...

Niels Leadholm: Yeah, no worries if you go a bit over.

Ramy Mounir: Okay, so maybe it's just 10 more minutes,

Niels Leadholm: Yeah.

Ramy Mounir: let's add a new, episode, a new slider here, this step. Now, these are going to go quicker, because we already know the pattern, so let's go to the commit.

And the only thing I added here was this, widget ops for the step slider, and I added... a new widget class for it.

I'm just giving it this new class for the widget ops, and I'm saying I wanted to debounce with 0.3 seconds, I want it to deduplicate true. That's the only change here. Now here, we have a difference. The difference is that we have widget updaters, and this is something that we didn't have before. So the widget updaters for this step is basically... it's very simple here, it's just saying I'm going to listen to the episode number, and if that changes, I'm going to call this callback function. And the callback, I'm defining that here as one of the... Here, let's update slider range. I'm just passing this callback. So updaters work with also a very specific signature. The way that I thought about it is that updaters, they... when you call an update or callback, you want to modify the widget, so what you give it is the widget itself, so you can modify it. And you give it a list of the messages that you received. all of the ones that you were listening to here. all the required ones are going to be sent. So this one. Right now, we only have one, so this list is just only going to contain that same message, basically. So all of the updated messages, you're gonna get them here, and you're gonna get the widgets. You define what happens to the widget based on these messages, basically.

I... we got the episode number in here, so I'm going to decode these messages, I'm just... I'm just decoding it from the topic message into a dictionary. I just found it easier sometimes to do that. And, I'm going to change the widget range. From, it's now going to start at 0, and it's going to end at, this value. Now, this value, I'm using the dataparser.query to get, basically, how many steps we have, right? We went over queries before, but... This is my data parser. I'm in the data parser... for step, just doesn't have, episode number, because I don't know what the episode is. And what I'm looking to get is the step. so I'm going to query this by giving it the episode number that I receive. And these are constants, so I'm providing those, and it will just give me how many steps that I have here. And once I get... once I do that, I'm just setting the range, the widget range, to that, and I am, setting the state of the widget back to zero, because we don't... yeah, once the episode changes, I want to send it back to zero. And I surrender, that's all. I return back the widget, I always return back the widget, because this is the modified widget. it's basically, I get a widget, I modify it, I send it back. That's... that's the... That's the pattern for all of these, callbacks.

And I also send back a true or false. when I send back true, it publishes the new state. When I send back false, it just doesn't publish. That's... this is the whole pattern.

Viviane Clay: And, maybe I missed this, but... Why are you... why are plotter.add calling to 0? I thought 0 was the, blank screen.

Ramy Mounir: Yes, because this, slider is on the... is on the first... Oh, okay, that's on the background, okay. Yep. For the next two objects, we're going to call plotter.add1 and 2. This... the slider is on the background.

Niels Leadholm: Just out of interest, how clever is Vito about, positioning those? Does that take a lot of tweaking in practice to...

Ramy Mounir: no, so when you... I think it is actually very smart in terms of, so if you are... So these numbers, like 0.12, so here. when I say 0.1, so this is the position of the slider. When I say 0.1 on the X to 0.9, I think it scales with the size of the renderer, so it's nicer. You can take this whole thing and you just move it in a sub-renderer, and it will just scale and work nicely. So it is smart in that respect, but...

Niels Leadholm: Yeah. Okay, cool, thanks.

Ramy Mounir: Sure. Yeah, so that's it. This is it for the slider. if this works, we should have something like this. Basically, when you change the episode number. for example, episode 0, we have 27 steps. And if you change the episode number, it will set... go back to zero, and when you check, it will have 30 steps. So it's already updating the step, because it's listening to that topic. Okay, let's go to the.

Hojae Lee: just about the, smart thing, the... the... yeah, the positions of the sliders can be smart, but, little things, for example, the numbers, you can make the numbers show up or hide it. I found that out, but then you can't really, control where the number is place, you can't put it on the bottom, or you can't change the spacing. I had a situation where there was a number, but then I had a button on top of it, so it was hiding the number, occluding the number a little bit, so I had to manually, increase the, button a little bit higher, yadda I guess typical plotting problems, but yeah, You don't have full control over, every aspect, just FYI.

Ramy Mounir: Yeah, dates, So if you want to have more control, so this is, like I said, this is a... I may have not mentioned it, but this is a wrapper over VTK. VTK is created by Kitware, and it's very good. It's just... it's so much of a... a learning rate that, it's not very easy to learn VTK, but I suggest if you just want to customize this more, then VTK is the way to go.

Okay.

So let's create this here. So this is the... Flutter 1, basically, index 1. And what we want to have is, as we change the episode, it changes the object, the mesh, the primary target, and as we move the step slider, it changes the sensor position. And we're going to query that stuff from the data parser and display it. Okay.

Again, it's the same, exact, pattern, which is I added a class for the ground truth mesh widget, ops, and we added that down there for the... For the widgets. And... so what we're listening to here is we have updators, and what we're listening to is the... we have two updaters, one that will update the mesh. I may have mentioned this before already, so one will update the mesh. And it listens to the episode number, and this is just updating the primary target. And another one is going to listen to both of these, the step number and the episode number, and it will update the sensor. Now, this is the moving sensor. The locators are a bit more involved, but again, this just shows how easy it is to get data. So I've created 4 locators. The target, which is here, this only is missing the episode.

the steps mask, I need that to process the sensor locations, because these are, when I get the sensor location, I'm getting it from the, SM steps, so I need to also know which ones have been processed, so I get that from the steps mask.

The missing value here is also episode. Here, I have the missing value is episode and the SMStep. So when I call this, all I need to give it is episode and SMSTEP. And then I also have the patch location, and I'm getting that from this path here.

Yeah, so really, when it's time to update the mesh, this only listens to the episode number. again, I'm just removing the old mesh. And I'm adding the new mesh, that's... I'm calling the YCB loader, which I talked about in the beginning of this. It basically... I just give it the target ID, a string, basically, of the mesh that I'm trying to load. And it will create the widget for me. I rotate it based on the information I extracted from the data parser, and then I shift it. And... and then add it to the plotter. So now here we're using plotter.add.1. And then I render that plug. That's it. I don't want to publish anything, I just return widget again, and false.

that's how you update the mesh. to update the sensor, it's a similar thing, except that now I'm updating So here, in the init function, I created... These variables, gaze line and sensor circle, which are the red sphere and the gaze line. They're empty right now, but they're going to take line object... line widget, or line object, and a circle object.

I think this is wrong. I need to change that to sphere. But yeah, so updating the sensors is as simple as that. Getting the messages, and here I'm just going to get the sensor position and the patch position, and I'm just going to update the sensor circle and the gaze line, and make it look at the correct place.

Niels Leadholm: And what was the return bool again? The second, return?

Ramy Mounir: Basically, do we want to publish the state after we update the system?

Niels Leadholm: Okay, yeah, thanks.

Ramy Mounir: Yeah.

So... that's it. That's really all that it takes to create the... This, nice visualization.

And, let's do this last one quickly.

So again, the same kind of, Pattern. Just added a class for it.

And the updaters here are going to be listening now to the episode number and the step number. If any of those change, we will update the MLH. And it calls the update mesh. I'm defining a sensor circle here, so this is the object for the sphere, again, not circle. And I'm adding a little bit of text to the plotter at 2. I'm just adding that at the top. Just says MLH. The locators are simpler here, because I only need to extract the MLH, so I'm just defining that this MLH depends on the episode and the step. Both these in the middle are already fixed, the current MLH and LM0. But if you have, a slider here, you can also change that LM0 to something else. An update mesh is, that's... this is the only function I added. Basically, I remove the widgets that already exist, the existing widget for the object, and then the sensor circle, I also remove it.

And then I extract the MLH. Here, by giving it the episode and the step, and these are the MLH stuff. It's a dictionary when I extract it, so I'm getting the graph ID, rotation, and location. I add the object, rotate it, shift it into position. And add the sphere, for the sensor circle. And, again, plot. It's as simple as that. I already copied all of this code from existing other plots, so I know it works by just copying it over. As long as you can connect them through these, topics, episode number and step number, if you use that everywhere, then you can just use... then you can just... reuse the functionality. Or if... if I'm copying a widget from, a visualization from Hoji, and she's using episode num, for example, I could just rename that if I wanted to. It's not a big change. But yeah, as long as you use those, should be reusable.

That's it. This is, if you do that, you'll have this visualization. it's a bit of code to add all of these classes, but I think it just makes it easy to just extract functionality a little bit away, and it also makes the code very readable. You could go through the code and see what's going on. Yep, I think this is all.