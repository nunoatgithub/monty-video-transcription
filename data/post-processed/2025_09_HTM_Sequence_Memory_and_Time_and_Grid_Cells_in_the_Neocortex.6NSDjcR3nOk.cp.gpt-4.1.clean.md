JHawkins: Early in our research, many years ago, I was thinking about melodies. This might have been before we started the Menta. I realized the brain has a recurring problem: it must represent things commonly observed in the world, and it must also represent them uniquely in different contexts. You need two different representations—one for the thing you're observing, and another that's unique to the context. These must be tied together. In a melody, notes or intervals repeat, but you need a unique representation at each point in the melody. This generalizes to sensorimotor processing as well. This was the genesis of sequence memory.

The basic idea, suggested by anatomy and physiology, is that if you take a layer of cells—this is a neuroscience presentation, so we have to interpret how to implement this in Monty—many columns represent features in a non-unique way. Input from a sensor, like ears or eyes, forms a representation as a set of mini-columns. If you sense the same thing again, the same mini-columns become active.

These features can appear on multiple objects and at multiple locations on an object. For example, visual edges in V1 can appear at different locations on different objects, or intervals in a melody. Biology suggests a column of cells can only represent a limited number of these features. In V1, you might see oriented edges—point normals or edges of an object—at intervals of maybe every 10 degrees, so there are about 36 or 18, depending on how you look at it. Some mini-columns will be active because they're clustered. For a particular orientation, several mini-columns will be active to varying degrees depending on their position. There's a general belief in a "Mexican hat" inhibition between mini-columns. If you look at this as a two-dimensional sheet of tissue, with only one dimension shown, you'd have a bump of activity centered around the current feature, with adjacent mini-columns representing slightly different features. As you observe things, this bump appears in different locations on the tissue. Multiple bumps are needed for this to work. In the picture, I show four mini-columns active, but in reality, there would be many mini-columns and multiple bumps of activity, all representing the same thing. It's redundancy; I didn't draw a full picture of this.

Niels Leadholm: Just to clarify, multiple bumps in each kind of hypercolumn? Each column?

JHawkins: Yes, I'll skip ahead to show the next slide. Remember the tank paper about mini-columns? I've got grid cells, and we've discussed this picture before. It shows one grid cell module, which contains six repetitive units—six mini grid cell modules. Each of these six units is a complete tiling of space. In this case, they observed six bumps of activity in the grid cell module, one in each of the six quadrants, all representing the same thing. As a bump moves—these are grid cells—if the location changes, a bump might move off to the right, and more bumps appear on the left. To make the system work, you can't have just one bump of activity, because at the edge, there aren't enough cells involved. This picture is a grid cell module, but I think the same thing happens in cortical columns, both in Layer 6 and Layer 4. You end up with multiple bumps of activity, which is necessary for the numbers to work and to handle the edges of columns, where bumps disappear and reappear on the other side. In the previous slide, I showed just one area, as a 1D picture—a bump of activity in a 1D set of mini-columns. In reality, the grid cell module picture is equivalent to what's happening in the cortex: every cell is a mini-column, there are more than shown, and multiple sets are doing the same thing.

Is that the visual cortex?

Niels Leadholm: In visual cortex, as you move through the column, parallel to the surface of the cortex, you get a gradual change in orientation.

JHawkins: 

Niels Leadholm: But then you would have, let's say this is the preferred orientation here. Eventually, you have a repetition of that over here.

JHawkins: I'm not seeing anything you're drawing. Where are you drawing?

Niels Leadholm: I'm using my hands.

JHawkins: Oh, I'm sorry.

Niels Leadholm: So this is the column.

JHawkins: You have the preferred orientation here.

Niels Leadholm: And then as you move along the surface—oh, do you want me to...

JHawkins: I lost my Zoom screen. Where is it? I no longer see anything about Zoom.

Niels Leadholm: If you stop there, you'll go either way.

JHawkins: That's going to cause problems. There we go.

Niels Leadholm: Okay, you see me?

JHawkins: Yep.

Niels Leadholm: If this is the column, you have a preferred orientation here. As you move along the surface, that gradually shifts and eventually repeats. What you're saying is, firstly, this orientation is similar to that one, and that's the kind of Mexican hat in a certain area, with multiple columns. Later on in a column, the other hat is where that same orientation appears again, assuming the only input was this bar.

JHawkins: That's general; I didn't make that up. A lot of people speculate that's how it works, but no one's really articulated it the way we talk about it. The idea is that there's a Mexican hat inhibition between many columns, which explains why they're bunched together. It also explains how many different representations a column can have, because it's within that spectrum of a Mexican hat inhibition before you get the next bump.

Those things all play together, but I think you've got it right. You can imagine looking down on the surface of a cortical column, like the picture I showed of the grid cell, and you'd have several bumps of activity, all representing the same thing. With a new input, you'd have another set of bumps in different locations, but they're also representing the same thing. Anybody else have further questions?

Hojae Lee: Is it that all the bumps together create a unique representation for that edge?

JHawkins: No, we'll get there in a moment.

Niels Leadholm: I guess the sparsity in the mini column will be critical for that.

JHawkins: Are you seeing my picture again now?

Hojae Lee: Yeah, your slide 1.

JHawkins: It's funny, because when I switch, it changes my sound. Suddenly, my sound is my computer again. I don't know why that's happening. You guys can hear me still?

Ramy Mounir: We can hear you.

JHawkins: Now it's coming back in; it's like it's randomly switching my speaker in and out. Do we have an understanding of this, or more questions?

Niels Leadholm: Just a quick question, still on the shape of the bumps. As a sanity check, a lot of Numenta's previous work and publications didn't necessarily have this bump. The idea was there, but one feature would be a random selection of mini columns, then another random selection.

JHawkins: We were testing out the mechanism I'm about to describe. We weren't really applying it in any particular instance.

Niels Leadholm: I just wanted to check my understanding.

JHawkins: If I could go back with a magic wand, I could make all the things we presented in the past equal to what we have today, but it's not, so we didn't talk about that. In fact, we would test the system sometimes with thousands of objects, features, or mini columns. Each one could be a random distribution of mini columns. It wasn't like that—bumps and all this kind of stuff.

JHawkins: This is how you basically represent a feature in a non-unique way. Going back to your question, Jose, the different bumps do not add any new representational capacity. At this point, they just add some redundancy.

Hojae Lee: But the next thing is going to make a big difference.

JHawkins: The key insight is that if you assume not all the cells in this minicolumn—again, we're talking about one layer of cells, so I'm labeling it as layer 4 here—there may be anywhere between 10 and 20 neurons in a mini-column in that layer. If you activate only one of those cells, like the blue dots here, and not all 10 or 20, then you're able to create a unique representation of that feature. You're still activating the same mini-columns, but by picking one of 10 or one of 20 cells, you get very high representational content. Imagine you had 6 bumps of activity, each with 5 active mini columns. You pick 1 out of 10, so that's 10 to the 30th—the number of things you can represent by selecting one of these cells in each mini column. We worked through a lot of the math on this. You could pick them randomly, and it would still work, and they wouldn't interfere. This was the basic idea: if you picked one cell per mini column, you'd end up with a unique representation of the same thing. These two representations would be co-located in the cortex—at the columnar, minicolumn, or cellular level—but would be two different representations of the same thing. You could have many different ways of representing this feature in different contexts in the world, and each one would be very unique. That was the basic idea. We did a lot of work to make sure the numbers worked out, and they did. It seemed like the brain picked just the right set of things to make it all work.

Hojae Lee: By representing the same thing, let's say you can select different cells within a mini column.

JHawkins: In the active mini columns.

Hojae Lee: In the activation column, let's say that represents color red. Even if different cells are activated, it'll still be color red.

JHawkins: If you looked at it—red's not a great example, but we could use it. Let's think of it as an edge of an object. The active mini column just represents some sort of edge at 30 degrees.

Hojae Lee: Okay.

that edge could be in different places on the same object—the 30-degree edge. It could also be on many other objects. In fact, there are only about a dozen different edge orientations you can observe. It's going to be one of those dozen, but what you want is a representation that is unique for a particular object at a particular location, and unique across all objects and locations. This is exactly what we see in border ownership cells. They look at one of those blue dots and indicate that this cell is always active at the tail end of the tiger, at this location on a tiger. How could that cell in V1 be active only at this location on the tail of a tiger? It's because it's a unique location on a unique object. These cells, even the blue dots, are not unique themselves—they're more unique than the mini columns, but it's the combination that's unique. In the case of border ownership cells, one of these blue dots would always appear at this particular point on the tiger and wouldn't appear in most other places, though it might occasionally appear elsewhere.

Hojae Lee: Okay, fine.

JHawkins: Does that make sense?

Hojae Lee: Yeah, so even if we have selected different cells, it will still represent the 30-degree edge. It will just be active in a different context or location.

JHawkins: The gray dots are your common feature edge.

Hojae Lee: You.

JHawkins: And the blue dots are the unique representation of that feature.

Hojae Lee: Okay.

Niels Leadholm: And for what it's worth, that fits really well with neurophysiology studies, like the Hubel and Wiesel experiments. I can't remember if you've come across those, Hoji, but when they—

Hojae Lee: Good luck.

Niels Leadholm: Orientation preference in cats.

Hojae Lee: Yet.

Niels Leadholm: When you penetrate the probe down perpendicular to the surface of the cortex, all of those neurons seem to respond to the same orientation. That seemed really weird at the time, because it looked like a waste of information. Then, if you go perpendicular, you get that gradual shift in preference of orientation.

JHawkins: I always thought that was a very weird thing too, Neil. I looked at it and thought, that can't be right. Why would the brain make all these cells do the same thing? The standard answer people gave was that it's redundancy, but that doesn't make sense. Other things happen when they get all those cells in the mini column to respond—the blue dots respond when given sinusoidal gratings, which are non-objects. There's nothing unique about them. But they noticed that when the animal observed a realistic image, the classic receptive fields, which were defined by looking at sinusoidal gratings, went out the window. Cells didn't respond as expected. They said, this blue cell responds to an edge at 30 degrees because we proved that with the sinusoidal grating, but then they show the animal real-world images, and that cell often doesn't respond at all when there's a 30-degree edge. They wondered what was going on. This explains all that. By the way, it doesn't have to be one cell per mini column. It could be 2 out of 20. There's nothing magic about that number; it just has to be sparse.

Hojae Lee: So this allows us to represent a 30-degree edge in many different contexts.

JHawkins: Yes, a gazillion subconsciously.

Hojae Lee: Yeah.

JHawkins: It doesn't mean you can remember them all, but the representational capacity is there.

Hojae Lee: Okay.

JHawkins: It's very large. We need that. If you think about an interval in a melody, there are thousands of melodies, each with many notes, and that particular interval appears many times in different places and contexts. Maybe there are only 12 melodies, or 25 intervals, or 12 notes—whatever you want to call it. There's a limited number of things that go in a melody, yet each time a new note comes in, you need a unique representation for that input at that location in that melody. That was the genesis for this idea. To make a sequence memory or a model of sequences, it's pretty simple. You just have to associate the active neurons at one moment in time with the active neurons at another moment in time. I'm not showing that here; I'm just showing one set of active neurons. But if you go through a sequence, you would have a series of these activations—these blue cells and the mini columns—and each time, each note or element in the sequence would be different. If you just associate one pattern to the next through horizontal connections, you would learn to associate pattern A with pattern B, then pattern B with pattern C, and so on, in a high-order sequence.

Viviane Clay: When we talk about the Layer 1 input for the specific timing between elements in the sequence, are you thinking of that as being an additional conditioning?

JHawkins: Yes.

Viviane Clay: The current element biases or predicts the next element, but that only works if the correct timing signal also comes in Layer 1?

JHawkins: I was thinking of showing that in this figure, but it's so complicated, I didn't have time to do it. I thought, I bet Vivian or someone is going to ask me about it. My prediction is correct. I'm not showing that here. What I'm showing here is just the transition from note A to note B, or element A to element B to element C, and so on. But, as in melodies and other things, there's usually timing between those, so you don't want to just run through these sequences as fast as you can. You need some way of gating the transition between one element and the next. That would be the Layer 1 input, which I'm not showing here.

And of course, it's complicated. I won't get into the complication, but the basic idea is that when you're at an element in the sequence, it predicts the next element. You also want to know when it's going to occur, so the next set of cells would be depolarized, but you wouldn't expect a note to come in until the correct timing signal is presented on the apical dendrite. I didn't show that here because we were just talking about locations.

Are there questions about that?

Viviane Clay: Just to double-check, we're not misunderstanding how location in the sequence or element in the sequence can be represented. You say ordinal location cannot be decoded, but the SDR is unique to that element in the sequence, right? We know where in the sequence we are, but there isn't a common representation for the first element. It is decodable.

JHawkins: If I had my magic wand, I could look at the SDR—the activation of these cells—and say, that is the 23rd note in Beethoven's 5th Symphony. But I can't; I'd have to have a magic wand or have learned an association with that, which we'll see in a second.

Viviane Clay: It's like how the locations are unique to the object as well. A specific location representation doesn't necessarily translate to other objects because it's unique to them.

Niels Leadholm: There's no such thing as a zero location.

JHawkins: That was another big thing. There's no sense of zero location sequence, no sense of origin in the grid cells. This is where Vivian and I got a little confused, because this is encoding the location on the object, but it's not like anyone reads it. You can't read it out and say, let's go to the fourth location. You can just say, I have an SDR, and you and I know it's the third location and it predicts the fourth one, but I can't say, look, what's at the sixth location in the sequence. You just can't go there.

Viviane Clay: But two columns could vote on it; they could form associations between their specific unique SDRs at that point in time.

JHawkins: I don't think they would, but you could. That still wouldn't tell you the location. There's no way of reading out, "this is the nth element in the sequence." You can't read it in the SDR. You can associate—if I had a separate column just keeping track of ordinal numbers, then yes, I could associate with that ordinal number.

Viviane Clay: I agree that there isn't a 1, 2, 3, 4, 5 representation anywhere, but why would you not think they could vote on us?

JHawkins: You said another column. In my next reveal here, the SDR is voting on location, so can I just jump ahead to that? This is the basic mechanism we had for the model of sequences. We tested this a lot to make sure it worked, and the numbers worked out. We didn't do anything realistic with it.

When it comes to modeling objects and sensorimotor learning, it's the exact same thing. We're using the same cells—let's say layer 4 here. We have the feature, we form a unique representation of it, so we have the non-unique representation at the mini columns (feature not unique), then we have feature-unique object location.

In the previous model sequences, as long as A follows B, and C follows B, and so on, you can learn that in a high-order sequence. But now we want to do sensorimotor learning. The order in which the patterns appear is not a high-order sequence, and therefore, in layer 4 itself, it cannot predict what's the next input. It doesn't know that. Our basic model for modeling objects, which we're all familiar with, is you have a second layer of cells that represent the location. We're pairing the location with the pattern in layer 4. In this section, cells labeled 6A were representing location, and this is how I viewed it. I've always felt like the grid cells themselves are not unique. They do not represent a unique location object. They're like one of 15 or 16 possible locations, and they repeat over and over again. That's very much like the orientation columns in Layer 4—very similar. It's a non-unique representation of location, so I've always viewed it this way: the minicolumns down in lower layers, some of them are going to represent grid cells themselves. If you had a separate set of cells underneath them—the blue dots—then you could make a location that's unique to both the object and the location on the object. This is speculative because it's not generally observed. I'll come back to that in a moment. But this is what's required, theoretically, to make this whole system work. You have to have a non-unique location, which is grid cells. Those are updated by movement, and then you pick a unique version of each one of those things in the same bumpy way as we see in grid cells. Now I can pair the unique location with the unique feature above. Since the blue dots in layer 4 and layer 6A are both unique to the object and to the location on the object, one is updated by sensory input and one by movement of the sensor, but they're equivalent. In some sense, they both are unique to the location and the object. Therefore, if you know one, you can predict the other, and if you know the other, you can predict the previous one. This is the genesis of our basic idea about how sensorimotor modeling works. I've convinced myself, maybe correctly or incorrectly, that you have to have this unique location to make the whole system work. It wouldn't be sufficient just to use grid cells, which are not unique. You have to have another representation which is unique. If you assume that's the case, then you can imagine a parallel construction between the upper layers and the lower layers, just like this, and now this will work. Inference is a matter of sensing and moving, sensing and moving. You're updating both of these things simultaneously, and as you go, you narrow down the choices that match both the sensors and the movements of the sensors. Yes, go ahead.

Viviane Clay: How does the different anchoring of the grid cells play into that? Does that create an extra amount of unique representations?

JHawkins: It only does if you have multiple grid cell modules. At one point, we thought we could get unique locations by using multiple grid cell modules. That's in our first paper on this topic. But it never really worked—there weren't enough grid cell modules, and it didn't look like you could access all of them. They had substantially different scales, which was also a problem. We kept looking for more grid cell modules, thinking they could exist in more places, and that would solve the problem. You could have multiple grid cell modules in a column, each anchoring differently. That was one idea, but it never worked out because there weren't enough cells or grid cell modules.

That's how we started. This is an alternate approach. This says there's another way to get a unique representation of location: think about grid cells as more like the activation of a mini column, where unique cells fire for each of those grid cells, as shown here. If I had to guess today, I think this scenario is more likely than the one with multiple grid cell modules. I can give some reasons why I think that's the case.

Ramy Mounir: Cool.

JHawkins: The important thing is you have to have a unique location.

Ramy Mounir: A quick question about the model of objects. We wouldn't need to learn associations or transitions between multiple consecutive layer 4 representations in this case, right? Because we're making associations with layer 6.

JHawkins: That's a great point, Rami. You don't need that. If I'm moving my fingertip randomly over an object or in different directions, then layer 4 can't learn any transitions. However, the layer 4 cells are still the same, and those axons still go horizontally, so in this picture, they're still there. The point is that this system can flow between sensorimotor inference and learning, and sequence inference and learning. For example, if I move my finger the same way every time I pick up an object, I learn to play with the object the same way each time. I can pick up my pen and play with it in the same way. Then the sequence in layer 4 would be a high-order sequence because I would be going through the same motion every time, and therefore I could learn it as a high-order sequence. It would be both a sensorimotor sequence and a high-order sequence. I see evidence of this all the time: when we practice something, we go from being totally reliant on thinking about how to move our fingers to being able to just play out a sequence naturally. Imagine this is now a layer 5 column, which is the motor output of a column. If I practice the same motor output over and over again, it'll naturally learn to play that as a sequence, as opposed to individual sensory movements. You can go back and forth between these two representations. They're not mutually exclusive.

Niels Leadholm: That's another example.

Ramy Mounir: I'm wondering if we could generalize the same system we're using for models of objects and use it for models of sequences by just having a 1D grid cell in layer 6A, and learning the transitions between going from 1 to 2 to 3 to 4. If we're building associations with the features in layer 4, that could drive the sequence learning in layer 4.

JHawkins: I didn't follow that in the beginning.

Ramy Mounir: If we assume we have a 1D grid cell in layer 6A and we're just learning a sequence—not a model of objects—and we're building associations between layer 4 and layer 6A, could we learn the sequence by just having those associations and learning the transitions in the grid cells, from location 1 to location 2 to location 3, driving the activations in layer 4?

JHawkins: I don't think you can learn the sequences in layer 6.

Hojae Lee: Basically, you want to add—

Niels Leadholm: That would be advantageous if there was something about the movement through the space. One example we talked about is with songs. Like you were saying, Jeff, in layer 4 you would just learn note-to-note. But maybe displacements through tonal space or something is movement in layer 6. What you're saying, Rami, is more like the movement forward in the sequence, whether that's time or action.

JHawkins: In layer 6, you don't always know what's going to go in the same direction.

Ramy Mounir: Unless it's a sequence of time.

JHawkins: Any kind of sequence we learn down there has to be of the sparse representations, of the population.

Ramy Mounir: I assume with Hebbian learning, we're just talking about two representations at layer 6A that always happen.

JHawkins: It would be the blue dots we're talking about over here, right?

Ramy Mounir: It'll be similar to layer 4. They would still form associations because we still go from one representation to the next. Even in locations, it would be just location 1 to 2 to 3. It's unique to the sequence. It would still form those transitions.

JHawkins: Maybe it confuses me by talking about 1D grid cells. If I just look at the picture I have in front of me and follow a particular sequence of patterns, moving my finger in the same way over and over again, then in theory, you could load this sequence in layer 6A in the same way we learned in layer 4. Is that what you're saying?

Ramy Mounir: Yeah.

JHawkins: That could be. The one slight hesitation I have goes back to some of those Thompson papers. I don't want to rely too much on her work, but it's all I have.

They just—when you talk about the connections in Layer 4, everyone says all the cells send horizontal axons to all the other cells, so the horizontal green thing is there. It's very clear. But when you look at Layer 6A cells, she often describes these cells as having very vertical axon branches. They don't seem to send horizontal axons throughout Layer 6A.

I don't know if that's true or not, but that's the only reason I didn't draw that arrow there. I haven't seen someone say, yes, in Layer 6A, all the cells send horizontal axons across all the other cells. If I'd seen those words, I would have drawn the horizontal green arrow in Layer 6A too. It doesn't mean it's not like that; I just don't know.

Ramy Mounir: That's interesting.

JHawkins: It's just unknown to me. There's a lot that's not shown here. It's not shown how grid cells come about here. For that, as I've talked about in the past, there seems to be a need for these one-dimensional sets of cells that fire at different phases—the different frequency of the speed. So there's a lot more that has to exist for these grid cells to exist. That other thing is a bit like—if you recall, we debated about it—I drew it as a set of cells in the minicolumn, each one firing at the same rate but at different phases. Then there was a separate argument in the literature that it could be different dendrite branches firing at different phases. There's a lot of mystery here. I don't know the answer to them.

Niels Leadholm: I was recently reading or watching some talks on how insects, like bees, perform path integration. I've been meaning to share my notes on that. I think that can be interesting as well, because they have a fairly primitive form of path integration, but it still does the job. It's also, I think, neurally simpler to implement than full-on grid cells.

JHawkins: You want to make sure it's as powerful.

Niels Leadholm: Whether it's powerful enough is the question.

I'll share that soon. It was interesting how they find a solution to, if I found some interesting flowers here, how can I follow a path?

JHawkins: From an arbitrary starting location and back to it. One of the general themes we've talked about, and I've observed, is that some of these mechanisms start out for very specific problems that animals have to solve. They're not very general solutions. Then, over evolutionary time, especially in mammals and humans, we've taken these specific solutions—navigating environments, going from flower to flower—and made a very generic version of the same mechanisms, which are now much more powerful and can be used to model anything. I'm always gravitating toward mechanisms that are very generic. You have to be careful when studying something like an insect. You might have a solution that works really well for certain things the insect does, but it wouldn't work for modeling coffee cups with logos on them and things like that.

I always, when I look at simpler non-mammals, keep in mind that it could work great for this ant or bee, but what about more complex cases?

Niels Leadholm: It always appeals to me because that works in these absolutely tiny brains. Whereas the entorhinal cortex is a decent chunk of brain, just getting something that will fit inside a column is an interesting problem.

JHawkins: I think.

Niels Leadholm: As an interesting problem, but—

JHawkins: But—

Niels Leadholm: I agree with you.

JHawkins: We just don't want to get fooled into thinking our brains do it the same way bees do. Anyway, this picture I've shown here is, from an abstract theoretical point of view, very broad. It can be applied to anything. This is just about forming representations and forming unique representations, and this mechanism solves sequences and sensorimotor, high-order sequences and sensorimotor sequences, and it can go back and forth between them. That's some of its appeal to me.

Viviane Clay: I like the elegance and simplicity of it, and how it brings back the HCM mechanism into the picture. I'm just trying to think through concretely using it for object behaviors now. I think the main reason I drew, in the diagrams I made, location and sequence as a separate representation versus stored in the associations in Layer 4 was because—I just started thinking about it right now, so maybe if I think about it for a few more minutes, I'll figure it out—but the issue I see with this is, how does the sequence work in combination with the location representation?

I have a unique representation in Layer 4 for that location at that point in the sequence. But then, I move my sensor to somewhere else on the object, so the Layer 6A representation changes, but whatever feature I predict in Layer 4 at that location depends on which state in the behavior I'm in. If I don't have a separate representation of the behavioral state, I currently don't see how that works.

JHawkins: Let me see if I can rephrase your statement. If we wanted to bring in behaviors, which are another type of sequence—behavioral models—how does that lay on top of this?

Viviane Clay: Like a sequence of states of an object, basically.

On the surface, it's not clear to me why it wouldn't fit onto this, but I haven't walked through it yet.

Niels Leadholm: It feels like it requires hierarchy in this setup, because the object-level state—the object-level state would be the input to Layer 4.

JHawkins: Can I make the—

Niels Leadholm: Something like that.

JHawkins: If Layer 6A is a direct implementation of location, now we're talking about location and spacetime—four dimensions. If Layer 6A could represent time, then Layer 4 doesn't have to change.

Viviane Clay: So the—

JHawkins: You could add it to Layer 4, but it seems to me that, given I'm calling Layer 6A location, then it's a location in spacetime.

Viviane Clay: Is that what you're suggesting, that the time is actually encoded in Layer 6A and not—

JHawkins: I wasn't—first of all, time in terms of how much time between elements in a melody? We're talking about something different here. We're talking about where we are in a behavioral sequence, right?

Viviane Clay: Yeah.

JHawkins: I hadn't thought about that, or I can't remember what I thought about it at the moment. I'm trying to recall. I don't have a preconceived notion right now, saying that's how we're going to handle that. I'm just thinking, in this mechanism, where would it be? How would I know where I am in this sequence?

Niels Leadholm: Is there a reason we'd want to treat songs and behaviors differently? It would be nice if it's the same...

Viviane Clay: Yeah, that's why I drew the sequence representation as a separate thing. It wouldn't be a 4D space in layer 6A. I think I put it in layer 5B, but it could also be a separate representation, layer 4, or even layer 3, since that connects and sends apical dendrites to layer 1. But it could be a very simple representation—just a one-dimensional next-step kind of representation that's always the same if we're at the same location in the sequence of a particular behavior. If I'm at that location in the sequence of that behavior, that tells me, for all of the locations in that object's reference frame, which features to expect.

JHawkins: If I'm following you, there are two approaches we can take. One is, you start with this diagram at the bottom of this figure and say, I'm going to make sure Layer 6A is actually representing space-time. Therefore, the representation in Layer 6A is unique to both the location, the object, and where I am in the sequence of the behavior. The other approach is to have an external signal, a sequence signal of the entire behavior, and that would be an additional factor to incorporate to make a prediction. Does that make sense, those two basic ideas?

Viviane Clay: Except for the external part. Do you mean external to the column, or outside?

JHawkins: I'm just saying it's not here in this picture.

Viviane Clay: Oh, yeah.

JHawkins: I didn't.

Viviane Clay: So basically, just someplace that disentangles the current state from the current feature on the object, or the current location on the object.

Niels Leadholm: Yeah, it feels a little like how, in the same way that we have a local feature and then the object ID, there's a similar thing for the input in L4, like the sequence that might be playing out there, versus the state of what the column is representing.

Viviane Clay: Yeah.

Niels Leadholm: A global one.

Viviane Clay: Yeah, state is almost like a sub-ID of the object, or something like that.

JHawkins: The state would have to go through a sequence.

Viviane Clay: Yeah.

Niels Leadholm: But that sequence could be semi-independent of what's happening in L4?

Viviane Clay: Oh, actually, do you remember when we talked about behavior models and morphology models being in the same column?

JHawkins: Yeah.

Viviane Clay: We put the behavior models in layer 3, because Layer 3 forms these apical dendrites to Layer 1. Maybe Layer 3 could be learning the sequence of states, and each state is a pooling over the activations in layer 4, the object ID, and then we might have a pooling over states for the global object ID.

JHawkins: That's interesting. That's an interesting idea.

Viviane Clay: And then Layer 3 could still be using the kind of associative mechanism that you drew on Layer 4 for predicting the next element in the sequence—the next state representing SDR.

JHawkins: It would...

Niels Leadholm: Or layer 5, because that also has apical dendrites in L1.

JHawkins: The theorist in me would like the following to occur: I would like the representations in these two layers, Layer 4 and Layer 6A, to be unique to both the object, the location, and where you are in the state of the behavior. That would be the cleanest way.

Viviane Clay: Yeah, I think it would be in that example.

JHawkins: So the question is, if it was Layer 3 representing the behavioral sequence, is that what you're suggesting?

Viviane Clay: Yeah, so basically you could think of it as the SDRs in layer 4 are unique to the location, object, and state, but then we pool over those in layer 3. We pool over all the SDRs in layer 4 that correspond to the same state of the same object. That's the object state representation. Then we can learn a sequence of object state representations that is conditioned on time coming from...

JHawkins: I got that. The question then I had was, how do I get Layer 6A to be unique to state as well?

Viviane Clay: Yeah, it would have to connect to the Layer 3 state representation.

JHawkins: Yeah, I don't know if it does. It might, I don't know.

Niels Leadholm: It connects to Layer 5 a lot. I'm still unclear why it needs to be Layer 3, but I don't think that matters too much.

JHawkins: You're saying maybe Layer 5 is that state?

Viviane Clay: Yeah, so in the original diagrams I made, I put it into layer 5B and used those apical dendrites. I just thought back, because I just read the document we wrote back then where we put the behavior model into Layer 3, so I thought that could be an option too, but either one, I think.

JHawkins: Yeah, I like this idea. Let me see if I can rephrase your proposal. There's another set of cells that represents the behavioral state. I imagine it would be unique to the object and the point in the state space where you are in that, right? I assume it's unique to the object, or it's unique to the behavior—maybe, I don't know, think about it. Isn't the idea with behaviors that they are objects?

Niels Leadholm: Because we have columns that are dedicated to behaviors.

JHawkins: Was Vivian's—I thought she just abandoned that.

Viviane Clay: No, I didn't. The state SDR would be unique to the object or behavior model, depending on what the column is getting as input.

JHawkins: Okay, so we have a column that's just modeling behaviors.

Viviane Clay: Yeah.

JHawkins: We're talking about that now.

Viviane Clay: Yeah.

JHawkins: And so Layer 4 is representing changing features.

Viviane Clay: Yeah.

JHawkins: Layer 6A is representing where in space those changing features are occurring, and the other cell is indicating where we are in the sequence of these changes.

Viviane Clay: Yeah.

JHawkins: It's an interesting idea. It feels like it needs more development. It's one of those ideas you consider, then realize there may be some problems with it. It just feels a bit too simple or early.

Niels Leadholm: I think it would be helpful to think through a sequence represented in Layer 4 versus a sequence happening in, say, Layer 5 behavioral state.

With that separation, it's not clear why you need any sequence memory in Layer 4.

Viviane Clay: In my mind, this was how we thought about it before, and that's how I showed it.

Niels Leadholm: Yeah, I agree.

Viviane Clay: Everything.

Niels Leadholm: I think this is how we've been talking about it, but now we're trying to bring back sequence memory in Layer 4. The question is, how do they fit together? Do we need both? That's what's not clear to me.

JHawkins: I'm not sure why you're saying to bring back sequence memory in Layer 4. Oh, because these are behavioral.

Niels Leadholm: Because we've not really been talking about that. I agree with you, Vivian. When we've discussed behavioral sequences, it's been at the object level. We've said, "This is the state we're in, and if we go to this location in our reference frame, we'll predict a particular moving feature," or something similar.

Viviane Clay: Yeah.

Niels Leadholm: That's different from the HTM sequence memory.

Viviane Clay: But why couldn't we have the same mechanism in a different layer, like Layer 3 or Layer 5? Especially since, as far as I remember, Layer 4 doesn't really have apical dendrites.

JHawkins: There's a complication. That's been the classic view, because stellate cells do not have them, but now more people are finding pyramidal cells in Layer 4, so some cells in Layer 4 get input from Layer 1.

Viviane Clay: Okay.

JHawkins: Not most of them. For what it's worth.

I didn't follow your conversation a second ago. Maybe you can try saying it again, and let me see if I understand. Is this about why we might or might not need sequence memory in Layer 4?

Niels Leadholm: For the past few months, we've been talking about behaviors, time, and all this stuff. You have a different kind of state of the object or the behavior. For example, a stapler is opening, so now it's in a more open state, and that's where we learn, in this behavioral model, some moving features at a particular location. That's where, as you say, it's a space-time model, because the location in the reference frame and the point in the sequence determine what features we predict.

That was always at a global, object level. The model is now in this particular state, and that's what conditions our prediction. Sequences in classical HTM are more low-level sequences—note A, then B, then D, or whatever. That's why it feels to me like if we're going to have both, maybe it's something about hierarchy. The output of a lower-level learning module would be low-level in the receiving one. Or, and I think this is what you're arguing, Vivian, maybe we don't need sequence memory in Layer 4. But I think it would be helpful to have an example of a behavior where we want both—the low-level sequence and the global level.

JHawkins: I'm not sure what you mean by low-level sequence; that's confusing me.

Hojae Lee: Neil, sorry.

Viviane Clay: I think it's whether we learn a sequence of input features that come into Layer 4, or whether we learn a sequence of states of the entire object. The object ID is represented in Layer 2/3, and that object or behavior goes through a sequence of states, and those states influence all of the features and locations on that object.

JHawkins: Yeah. Let me throw out an idea, maybe it'll help. The way I would prefer this to look—again, elegance is often valuable, but sometimes it's wrong—is that if I have three layers of cells, maybe the third layer is representing this behavioral sequence. I would love them to all work exactly the same way. They all have many columns, they all form these sparse representations, and they can associate with each other via the vertical blue-green arrow, but they would also all have the ability to learn patterns within their own layer, as in the horizontal green arrow. It's available if it's useful; if it's not useful, it's not learned.

I never see harm in having these horizontal connections, which are a prevalent feature for most layers. The one exception might be Layer 6A, but it's common in Layer 3 and Layer 4. If every layer of cells has this basic architecture, then every layer can learn high-order sequences of whatever it's representing, and if it can't, it's not useful.

That's not specifically addressing the question you were talking about, which I'm still confused about, but I think—

Viviane Clay: I think that means there isn't really an issue with allowing Layer 4 to learn sequences, but also being able to learn sequences of object states in a different layer, disentangled from it.

JHawkins: I think, again, I'm not really following Neil's argument, but the general idea is there's no harm in having it there, and then you can ask under what conditions these horizontal connections would be useful.

Niels Leadholm: Then it's also a question of, in general, we've been talking about how time is obviously helpful, or maybe critical, for many of these sequences. Does that mean both Layer 4 and whatever layer is representing object-level state are getting time input?

JHawkins: I don't know. Interesting question.

Niels Leadholm: Maybe it would be helpful to try and think about how we would represent a song if state is at the global level.

JHawkins: Is state a global level thing? It's in the...

Niels Leadholm: That's how we've often talked about it.

JHawkins: Couldn't it just be a voted-on layer?

Viviane Clay: If we have a song, we could just learn it in layer 4. Maybe, as Jeff says, every layer has the ability to learn sequences, and if it's sufficient to learn a sequence in layer 4, then those neurons might form more dendrites to layer 1 to get the timing. But if it's a sequence of object or behavioral states that require more pooling over multiple locations, then we would learn it in a different layer as a sequence there.

JHawkins: Yeah.

Niels Leadholm: It's great if we're just not understanding it clearly enough, because it feels messy that both of these are learning. It's not super clear to me why it would happen sometimes in one layer and sometimes in others.

JHawkins: I'm not following everything you guys are thinking about, but it may be helpful, continuing with the thought I had earlier—imagine you have multiple layers, 2, 3, whatever. They all work on the same mechanisms. The differences between them: they all have these horizontal connections, they can potentially form associative connections between them, like the vertical green arrow, and some may or may not have time. But they're updated by different things. In this diagram, one's updated by sensory features, and the other's updated by movement vectors. They're all the same, but different things update them, and maybe some of them can use time and some can't. That doesn't violate the basic principle I'm trying to achieve here. You could look and say, what if I had three layers of cells? Layer 3 gets time, Layer 4 doesn't, and Layer 6—I don't think it does, but you don't know. My point is, the idea that you have these multiple representations, each layer has a representation, each one is trying to predict the next input, and each one is driven by some different driving force. Then they all settle together. That's a very powerful idea.

I just don't understand what you guys are—so I'm just saying time does not have to be necessary for all these things to work under the same mechanisms. It doesn't necessarily require that all the layers have time. It requires some of them have time, but not all of them.

Hojae Lee: I think this goes back to one of the earliest ways we thought about behavior, which was that Layer 4 gets the features, Layer 6 gets movement, and Layer 3 gets the changes. Those being the driving forces.

I think I copied a slide to the Zoom chat, or posted a screenshot to Zoom chat, where all the layers work as a mechanism. There's no reason why the behavior model cannot be in a child LM, and so basically, we thought of—

JHawkins: Should we go look at this diagram? Are you showing it?

Hojae Lee: Sure, yeah.

JHawkins: Did Bob stop sharing then?

Hojae Lee: Okay.

JHawkins: You said you posted an image. I didn't know if you were talking about that.

Hojae Lee: Yeah, on a Zoom chat. Everybody opens it? It's like a slide.

JHawkins: How do I get it to be big here?

Tristan Slominski: Could you just share your screen, Hoji?

Hojae Lee: Yeah, sure. That's a good idea. There we go.

JHawkins: Excellent. Yeah, that's good.

Hojae Lee: So I think that idea of feature going to layer 4, and then changes going to Layer 3 was—

JHawkins: I'm sorry, what are we looking at on this image now, Jay?

Hojae Lee: Oh, this compositional plus behavior model.

JHawkins: Okay.

Hojae Lee: At some point, there was an argument that the behavior model cannot be in the child LM, but must be on the parallel line.

Viviane Clay: I think that was just about when we apply a behavior to a morphology model.

Hojae Lee: Okay.

Viviane Clay: We could use that connection, but the chat LLM could still have learned—

Hojae Lee: Shuttle.

Viviane Clay: Yeah, but then, I think that's when we put both models in the same column, still.

Hojae Lee: Okay.

JHawkins: But I'm not sure. That might still be where our current leanings are, having them in different columns. If you want to make an argument why—I'm open to discussion about alternate flavors.

Hojae Lee: Personally, I think features going to Layer 4 and changes going to Layer 3 means the behavior model and morphology model can exist in the same column. The reason we separated it out was because we didn't want to keep track of two different reference frames for the behavior model and the morphology model.

JHawkins: That was one of the big reasons.

Hojae Lee: Yep.

Viviane Clay: And because there wasn't really a reason to keep it in the same reference frame, in the same column.

Even if we send the changes to Layer 3, that still doesn't solve the problem we have right now. Just because I am detecting a change at one location and know which change to expect next at that location, if I don't have a separate state variable, then I don't know what change to expect after I move my sensor somewhere else.

Hojae Lee: Yeah.

JHawkins: I'm sorry, but Vivian, my recollection was part of what Jose said is that one of the real things that pushed me over to the dark side of having two different columns—a behavioral column and a morphology column—was because it required two separate reference frames, and that seems almost impossible. Hoji, are you suggesting there's a way of solving this with one reference frame?

Hojae Lee: I'm just wondering where we're converging to, because I feel like we started with one, then went to another, and now are coming back to the first one.

Niels Leadholm: I think we're still saying one, because we're still talking about behavior models. We're not talking about morphology right now.

Viviane Clay: We're just talking about having different states in a behavior model.

Hojae Lee: Okay. Independent of the morphology model. So we still have two different columns: one that contains a morphology model, and the other that contains a behavioral model. We still don't know exactly how to use a behavior model to predict the features for the next step in the process.

JHawkins: Were you saying we don't know how those two models interact, the behavioral model and the morphology model?

Hojae Lee: It sounds like it's an open question, but I might be wrong.

JHawkins: Yeah, I don't know.

Viviane Clay: We've talked—

Niels Leadholm: We talked about that, but that's a different topic from what we're discussing today.

Hojae Lee: I'll happen.

JHawkins: Although I've embraced Vivian's suggestion of having separate behavioral columns.

Viviane Clay: I don't see why it's the dark side. I feel like it's much more elegant.

JHawkins: I know.

Viviane Clay: Same mechanism.

JHawkins: But now we've basically divided columns; the whole cortex has two types of columns.

Viviane Clay: And, many times... columns.

JHawkins: I know.

Niels Leadholm: They're all columns still.

Viviane Clay: They're all columns; they just get different inputs.

JHawkins: Alright, I'll just state it. I've accepted your logic, but there's something that still slightly bothers me about it. I'm not like, "Oh, yeah, that's it." It's okay, it seems to work, it's pretty good. There's something irking about it. It's okay to think about. I don't want to revisit it completely, but if we stumble upon something that makes us question it, then I don't mind pursuing that a little bit.

Niels Leadholm: Just on what we were discussing earlier, I don't have a great drawing, but I've got some things to point at. Can I try to get at what maybe the open question feels like?

JHawkins: Sure.

Niels Leadholm: If I share my screen.

JHawkins: I'm confused by that. Oh, great. Thank you. This clears it up right away.

Niels Leadholm: Basically, we've been talking about different kinds of sequences and behaviors. We've been talking about things, as you describe often, Jeff, as a higher-order sequence—it could be a song, a sequence of letters, whatever. We also talk about things like staplers opening and closing. For the moment, just see this one on the right. In general, this is a kind of behavior or sequence modeling column. If we say it's learning songs through HTM, then we would say it's getting A, then B, and these are coming into layer 4, and then it's learning this kind of transition structure, which may or may not be conditioned on time. If it's more like a stapler, then that's where we talked about the input feature actually being a changing thing, learned at a location. That's where we would learn a bunch of local flow patterns here, and then a bunch of local flow patterns there, and those local flow patterns are associated with a different global state, or state for the entire object, with the conditioning.

JHawkins: The entire behavioral object.

Niels Leadholm: Yeah, the behavioral object. Sorry, not stapler—this is a behavioral object. This is the lever kind of behavior, or the hinge behavior.

That's going to tell us, based on where we are in the hinge behavior sequence, which is some kind of more global thing, and where we are in the reference frame, we can know what we should predict—like some flow patterns here, or in a different location. In this diagram, where's the information about where we are in the sequence?

I guess we've discussed different locations of that in the past. Both Layer 3 or 2 and 5 have come up as candidates. The advantage of 3 is it maybe makes it easier to communicate to higher levels.

JHawkins: They have 5 pitches as well. Okay.

Niels Leadholm: But it's always felt to me like Layer 5 would be nice, just because that's the kind of motor output, and the connection between behavior and action is so close. Anyway, I think that's the starting point for what Vivian and I were talking about, or at least what I was trying to say. Today, we were talking about HTM, and it's a different kind of sequence, almost like a different kind of behavior. It's still time-conditioned and all this stuff. So then the question is, is it really something different? Maybe sequence learning is happening in multiple layers, and it's just a case of whichever ones have associative connections and maybe have access to time—they can do it.

What I was trying to say was, if you imagine there is a global state, but we don't actually represent the transitions between states here. Instead, you feed the hypothesized state up, and that becomes more like an input, like A or B. If this higher-level column is actually keeping track of the sequence, then it could condition the lower-level one and say, "Oh, you are in this state," or "Now you're in this state." And so then this behavioral model—

JHawkins: But why did you dismiss the idea that it could be learned locally in the first column—the sequence?

Niels Leadholm: It just feels a little bit like having multiple reference frames, or I don't know, it just feels weird to me that songs are learned in a totally different way from—

Viviane Clay: Staplers opening and closing, and maybe they are? It would be the exact same mechanism, just applied to a different layer.

Niels Leadholm: But that's what I mean by that.

Viviane Clay: They're different.

Niels Leadholm: Weird then—

Viviane Clay: It's—

Niels Leadholm: Learn in a different layer.

Viviane Clay: And it wouldn't be a different reference frame, it would just be a sequence.

JHawkins: Again, going back to the argument I made earlier, I think every layer, in theory, could learn sequences if it made sense for them. It's not like I'm representing it as an inherent property of a bunch of cells, so it's not like I'm doing extra ones or at a second place. Whatever it's representing, if it can learn sequences, it learns sequences.

I don't know, I guess I'm not ready to jump into the hierarchy yet until I understand why it doesn't work in R1.

Niels Leadholm: For example, now we need multiple layers to have access to time. But we've also talked about how, for time to make sense, it needs to receive feedback from the columns to tell the matrix cells whether to speed up or slow down. So now we also need multiple layers projecting to the matrix cells to tell them whether to speed up or slow down. It just feels like it brings complications by having every layer be able to do this.

JHawkins: Maybe not. It's not clear that's true. All these layers are connected together. It would be sufficient as an ensemble of layers that they tell the matrix cells what to do. Not every—as long as there can be somebody who can represent the group correctly, then—

Niels Leadholm: Yeah.

JHawkins: By the way, learning sequences doesn't always mean you have to learn the timing of the elements.

Niels Leadholm: Sure. But at least we know there are things like this that we want to have time for.

JHawkins: It's funny, because when you show those two pictures, my first reaction is to want to make them the same. I want to see why ABDFA is the same as stapler opening and closing.

Niels Leadholm: That's what I'm trying to get at with the hierarchy. It just feels like if this state is passed to this one, and that's what's conditioning, or that's the one that's keeping track, then the actual kind of sequence is just being learned here.

JHawkins: I don't know. To me, the hierarchy—we've found one good reason for hierarchy so far, and that's compositional structure. If we want to view sequence memory as somehow compositional structure, I'd be happy to talk about it that way. But it's not clear to me we're talking about that. I'm still confused.

Niels Leadholm: Maybe that is one way to look at it, because in the sense that a song is a higher order sequence of very simple objects—it's just direct sensory inputs, it's notes.

JHawkins: It is.

Niels Leadholm: In closing, it's a sequence of a morphological object, so it makes sense that the input, in sum, has to be an entire object. In this case, hinge behavior has to be a representation of many different changes going on at once. In order to represent a behavior as complex as a stapler—

JHawkins: That could be. It has to be.

Niels Leadholm: Compositional.

JHawkins: You could argue that's a difference in quantity, or you could argue, as you're saying, it's a difference in quality. I'd rather shoot for the difference in quantity—one's one-dimensional, one's two-dimensional, or something like that.

Niels Leadholm: Yeah.

JHawkins: Grid cells represent one-dimensional objects, and they represent two-dimensional objects—the same grid cells. Why couldn't I do the same thing in a single column? It could be representing one-dimensional sequences and two-dimensional sequences. I'm always hesitant to jump the hierarchy until I've absolutely proven it.

Niels Leadholm: Yeah, I know it also has—

JHawkins: The nice thing about hierarchy is I could say, I need two columns because the columns are representing two different objects. They're representing two different objects, and I'm trying to find the relationship between them. That, I'm willing to hang my hat on. Old expression. I don't know what it means.

Ramy Mounir: Thank you. Do we lose the location-by-location basis of changes if we just pull over object states like this? Because what you're describing sounds like second-order pooling. We pull from features into an object state, and then from object state into object behavior. I think we discussed this in the first retreat, but we ended up saying that we want those changes to be at a location-by-location basis.

Niels Leadholm: I'm not sure. I need to think about it, but the location-by-location basis is captured more in the top-down connections.

Viviane Clay: I think it would work. If R2 would learn the sequence of states, it could inform R1 which state to expect, and R1 still has a model of which locations to expect, which feature set for each of the states. But it's a lot of machinery required for a very simple task of learning a sequence.

Niels Leadholm: I agree with you, Jeff, if this is the hinged behavior, then what is this? I'm not proposing this because I think it's perfect. When we were talking about it, this is basically me thinking out loud about how songs and staplers are different. I want to try to understand them. What are my intuitions for how to do that?

JHawkins: I just didn't follow how you got to that. In my head, I'm going to reserve hierarchy for when two learning modules are representing two different objects. That could be two different behavioral objects, or two different physical morphology objects. But they've got to be two different objects. I can't use the hierarchy as the convenience of, oh, we need to put something and stick it over there. That doesn't work for me. That's the lure of the death of hierarchical solutions. I don't like that. It's not clear to me. I'm not keeping up with you, but it's not yet clear to me what the problems are with doing this with one learning module. You've jumped ahead of me.

Niels Leadholm: I agree, it's possible. I think, as you often say, sometimes you just have a feeling that something feels off.

JHawkins: Okay, but I'm not sure what it is. I look at sequences in the stapler, and I think those are really the same thing. You're telling me they're different things. I'm not sure why they're different things. They seem like they could be the same thing, or I certainly would like them to be the same thing. Why would I make a distinction between them? I don't know. That's a tough one.

Niels Leadholm: If we maybe, for the time being, embrace the idea that Layer 4 and Layer 3 or 5, wherever the state is represented, and maybe any layer can just learn sequences. If we have repeated transitions, then they will learn that through associative connections.

JHawkins: It's natural, nothing has to be done.

Niels Leadholm: And then it can also be time-conditioned.

JHawkins: Where did we end up on the idea that the low—I'm sorry, my memory is really bad. We were talking about Layer 6A as potentially being 4-dimensional space-time, or just three-dimensional space. Did we come to a—

Viviane Clay: I would argue for it just being three-dimensional space, because that's what we need to path integrate through, and then having separate representation for a sequence, because there we don't need to be able to move through it arbitrarily.

JHawkins: The last sentence didn't make sense to me.

Viviane Clay: In the sequence, we only move from the current element to the next element. In 3D space, we have to be able to move through it arbitrarily.

JHawkins: We do that with the movement vector, right? Grid cells—but why couldn't they? In the grid cell literature, there's a lot of evidence that grid cells represent episodic time. Sequences of time—your episodic memories are sequences of things. My first reaction would be, can I get grid cells to represent space and time? Why is that hard? I need to path integrate through space-time; I can path integrate using movement connectors. That's the hard part, but we know it works. Now, what I have to do is add another "movement vector," which is just time, and that's something I can't control—it just moves ahead on its own. But it's another type of movement. Is it possible? It's not clear to me that grid cells couldn't path integrate through spacetime.

Viviane Clay: I guess you could represent it as a fourth dimension, but movement along the fourth dimension would be very different from movement.

JHawkins: It would be.

Viviane Clay: For you.

JHawkins: It would be. The thing that drives it would be different, right? I don't know. The literature on grid cells suggests they represent time sequences as well as other things. They're very flexible about what they represent in our episodic memories. Episodic memories are often sequences of things—almost always.

I think the evidence suggests that at least grid cells in the entorhinal cortex represent space-time.

For me, it warrants thinking about it a little bit—how would I, what would the mechanism be if I had to add time as another path-integrating factor?

Niels Leadholm: Maybe, just to carry this discussion forward, nothing concrete, but we often talk about examples where it's easy to path integrate through a sequence or a behavior, and instances where it's not. Things like songs, rhymes, or the alphabet—A, B, C, D—it's very easy to go in one direction, but very hard to go in the other.

JHawkins: That would be like the time movement is only in one direction, whereas physical movement of the sensor can be backwards and forwards.

Viviane Clay: We could have it learned in the—

JHawkins: Just think of time as a—

Niels Leadholm: If we can't path integrate or go back through time in the representation, what is the advantage of having that as part of the path?

JHawkins: We need a way of representing—if I'm trying to get to Layer 6A representing space-time, that would be the simplest solution for me. Then, when it projects to Layer 4, it says, "Here's what I predict at this point in spacetime," as opposed to this point in space, and then Layer 4 has to integrate time from someplace else. If Layer 6 can incorporate spacetime—four dimensions—then Layer 4 works just as it does today. I don't have to do anything differently.

Niels Leadholm: I can't.

JHawkins: It just feels—

Niels Leadholm: We're already struggling to fit a grid cell, or a path-integrating cell, into a column, and now it also has to represent time. It feels like we have a straightforward neurological basis if state is just conditioning apical dendrites—another input.

JHawkins: After our last research meeting, I tried to come up with a mechanism. I spent a day and a half on this, trying to come up with the actual neural mechanisms that would allow neurons to make different predictions under different times and contexts. I couldn't solve the problem. I just couldn't come up with an answer. It doesn't mean there isn't an answer; I just couldn't come up with it at that time.

Niels Leadholm: Was this apical conditioning?

JHawkins: It does sound simple, and then I tried to work out the details, and I couldn't get it to work. Maybe I was just having a bad day.

Niels Leadholm: What was the issue that came up?

JHawkins: I was afraid you were going to ask me that. I don't remember. I was deep into it, taking notes, thinking and scribbling. I have to go back and look at it again, but it just didn't pop out at me. It sounds like it ought to be simple, but I was trying to figure out—if I have these calcium spikes and back calcium spikes, how could the neuron behave differently under these different conditions? How could the apical input enable one set of basal dendrite behaviors, and another apical input enable a different one? I just couldn't figure out how to make that work.

Ramy Mounir: Anyway—

JHawkins: I—

Viviane Clay: I feel like it should definitely be possible to do it with 4D grid cells, but it seems a bit much for such a simple thing. We could just have unique representations for each state and then use the sequence memory algorithm to associate the current state with the next state.

JHawkins: I got it. But I'm going to go back to the idea that grid cells in the entorhinal project seem to do this. We could look at the literature about them encoding sequences and so on. They seem to be extremely flexible. They can represent one-dimensional space, two-dimensional space. We don't know if they can represent three-dimensional space—the verdict is still out on that. But we do know they represent time, or sequences, and episodic memories, which are sequences of events. It might be possible that when you try to understand how grid cells solve space-time, not just space, it may make them simpler. The addition of this requirement may suggest an answer—it's much simpler than we thought. That happens sometimes.

Viviane Clay: One thing that could be nice about it is that we might have sequences for behaviors that aren't just transitioned by time, but instead are action conditions. Opening the stapler is usually not something that just happens on its own, but you apply an action and that makes it change states. If we had a general grid cell mechanism, it could learn how actions transition you through state space.

JHawkins: Yeah.

Ramy Mounir: So that means Layer 3 is now going to be pulling—the most general thing would be a behavior ID, but if it's not really moving, then it would be just an object ID. With 4D grid cells, Layer 3 has the ability to pull and just represent the API. If I have 4D grid cells, it's possible that Layer 4 and Layer 3 have no idea about this.

JHawkins: They don't know; they're just associated with some SDR coming from Layer 6. They have no idea what that means. Anything beyond that is going to work the same. The pooling will be the same, pulling over things that are occurring in one dimension, two dimensions, four dimensions. They don't know.

Ramy Mounir: So it could be a behavior ID or an object ID.

JHawkins: It would be an ID representing all these patterns, whether they're three-dimensional space or space-time.

Niels Leadholm: Just one thought, tying back to the conversation we were having the other day about a generic reference frame versus a reusable reference frame versus specific predictions.

JHawkins: I'm sorry, I don't remember that. What's the reusable?

Niels Leadholm: That was the conversation about mugs, how you learn many different mugs, and then you might get a class of objects that all have the same reference frame.

JHawkins: So the idea that classes of objects could all have the same reference frame.

Niels Leadholm: Yeah, but then the state would help you predict deviations from that. That feels relevant to this discussion, because it's the same thing. If, at least a naive implementation of a 4D grid cell, is literally adding an additional dimension, you have this explosion in how much you need to represent and learn. With something more like what we discussed, over time, in different states, a lot of the information you've learned about an object is redundant. You can reuse that, and the state conditioning just needs to tell you what is different. That's clear, at least in my head, how that would work with the state being separate, rather than adding this fourth dimension.

JHawkins: It's funny, I almost jumped to the opposite conclusion.

Niels Leadholm: Okay.

JHawkins: My first thinking is, how would I add that to Layer 6? How do I think about Layer 6 in a way that encompasses the different classes of cups? You might be right, Niels, I don't know, but I was thinking, what does it mean to have this path integrable space thing? I just felt time is one other dimension we could add. I see your point.

Viviane Clay: That's a good point. I think that is a strong argument for it being separate, so we don't have to relearn all the things that stay constant.

JHawkins: Why would it force us to relearn something if I didn't do that?

Viviane Clay: Not in the behavior models, because there we're only storing changes, but if we have a morphology model that has different states, those different states might only differ in small variations. Like the opened and the closed stapler—if you have a morphology model of both, we don't really need to relearn how the bottom of the stapler looks.

JHawkins: I know that, right?

Niels Leadholm: Partly it depends on how the spacetime grid cells work. But if we at least agree that in Monty, with 3D Cartesian space, and then we add the temporal dimension, we have to replicate all the information that's learned at every new slice of time. Then we have a significant increase in the amount of information we're trying to represent and learn.

JHawkins: We know we haven't...

Niels Leadholm: Maybe there's some way that—maybe it's only the grid cells that change over time that differ.

JHawkins: It's possible that you could still have 4D grid cells and then a separate class representation. We still haven't resolved how to learn these behavioral models. A single column doesn't seem to be able to do that, and it's just not enough time to learn everything. It could represent it, but it can't—that was another issue we haven't resolved. It clearly takes a bunch of columns working together to learn these behavioral sequences, and we don't know how that's happening either. That's a hole in the theory, no implementation. That may not be a problem for Monty, but Monty couldn't do anything.

Viviane Clay: 

Ramy Mounir: Something that complements what Niels was saying.

Viviane Clay: Good.

Ramy Mounir: Back then when we talked about this, I also suggested that what we're seeing here is basically the location being a generic location, and then for the different instances of this object, we have a specific SDR for these locations. I also suggested that this location basically represents time the same way, where the generic location is not changing, but the specific would be—as it moves, it's just changing which cells in the mini column. So it's representing time in that way. And then, if we assume—

JHawkins: I'm not feeling that's representing time. Wouldn't the pose or the orientation representation be changing as well as when that lid goes up? So wouldn't the square rotate with the—

Ramy Mounir: That would be in the features. I'm talking about the location in 6A. Maybe—Jeff, you said that Layer 6A doesn't have these connections that may represent transitions, but I'm saying—

JHawkins: I said only that.

Ramy Mounir: 

JHawkins: The Thompson paper didn't suggest them, so that doesn't mean anything. It's just one data point, so I'm not hanging my head around it.

Ramy Mounir: But I'm suggesting that maybe if they exist, then we could learn connections between states the same way.

JHawkins: As a high-level comment, I would agree with that. I'm not sure how that relates to the picture of the stapler here.

Ramy Mounir: It's just that, if we're going to say, this is basically what Niels was also suggesting, that if we're going to represent 4D grid cells, we could just represent the time axis as a distortion in the location, or a variability from some generic location. Did I get what you were saying?

JHawkins: Yeah, that.

Niels Leadholm: I think one thing I need to understand better is that, in my mind, the bottom of the stapler would be the same, and you would need to represent the parts that are changing. When you described it, you mentioned that the location on the tip of the stapler that's moving is constant. I'm not saying that's wrong, but it feels different, and I just want to clarify.

JHawkins: I thought we broke off the top of the stapler and we're using the existing model for the stapler, just restricting at the top. In that case, it's the same object, just rotating.

Ramy Mounir: This doesn't assume hierarchy. We're assuming it's one object, which is why I had the balloon example for distortion. We can't break this into multiple objects, but we can represent how these locations change or distort over time.

Niels Leadholm: Maybe it helps to use the language of a behavioral model. All we're representing here is local flow patterns. There's no concept of a stapler head, at least not in the hinged behavior model.

JHawkins: This would be like an object such as a balloon. In some sense, you could argue it's not changing shape at all; you're just looking at it at different scales and seeing a flow between those scales. I can see a balloon that's close to me and further away, and of course, it changes in size, just like this image does. But I assign the exact same reference frame to them; I just scale it.

Viviane Clay: But there are other distorting behaviors.

JHawkins: I know that. But in this particular case, sometimes when we use examples with simpler explanations, it's not a good idea. It's better to focus on the more complex ones.

Niels Leadholm: All...

Hojae Lee: All roads, all discussions lead back to the can of worms. I was just going to say that. Should we talk about worms?

JHawkins: Of course...

Viviane Clay: Briefly... oh, god.

JHawkins: The can of worms is equivalent to a crumpled t-shirt in both the behavioral and morphology models. Sorry.

Viviane Clay: On the 4D topic, at least in my mind, in terms of Monty, no matter how it's done in the brain—whether the fourth dimension is part of the grid cell representation or a separate sequence representation—we'll end up with models that are four-dimensional. We have three-dimensional locations in space, and then an orthogonal, totally separate, fourth dimension of states or time in which we learn these things. In Monty, we have the usual models, but all the XYZ locations for each feature are conditioned on the state. Depending on the state or the element in the sequence, you expect different features or changes at locations. For inference, when we try to determine where we are, those hypotheses would extend into the fourth dimension, so we would have to infer both the state and the location on the object in that state. Conceptually, it's valid to think of it as 4D space. The question is how it would be implemented in the brain.

JHawkins: I'll go back to something I think Neil said earlier, or someone did. Layer 6 is highly interconnected with Layer 5. If Layer 5 is representing movement, movement is also behavioral states. I'm trying to get Layer 6A to represent 4D locations, and locally, you'd have your signal at Layer 5 that might help Layer 6 represent 4D space. I'm just suggesting that.

I think it's worth trying to get Layer 6 to represent 4D space. That could be separate from states or classes of objects. A tall cup doesn't become a squat cup; that's not a behavior, just two different flavors of an object. That could be separate from things that change and morph into each other.

Niels Leadholm: Or...

JHawkins: Did we make any progress today?

Niels Leadholm: Maybe I misunderstood what you said, but if we were to be devil's advocate for spacetime grid cells, then a class would just be the grid cells that are active for the reference frame that's active for the different objects it could morph into, because they would share the same spacetime space.

JHawkins: Are you advocating for it, or not?

Niels Leadholm: I'm advocating for it, because it begins early.

Viviane Clay: That's the advocate.

Niels Leadholm: That's right. Okay, fine.

JHawkins: You can...

Niels Leadholm: Heavenly advocate for spacetime grid cells. There's that. The other thing is, for behaviors that aren't just sequences—things like the joystick, or the complexity of objects that can go through time or their behavioral sequences in different directions, go through behavioral space in different directions.

JHawkins: But they're not sequences. That's a very different thing. To me, that is not a behavior. That is just something that can move in the world.

Niels Leadholm: But somehow we can understand and model it.

JHawkins: That's right, but to me, that could be equivalent to picking up my cup and moving it to a different part of the table. There's no inherent property of the cup, and if I have a joystick and can move the top in different directions, it's limited, but it doesn't seem like there's a set behavior for it. I have a limited area where I can put my cup on the table, and a limited area to move the joystick top.

Niels Leadholm: Isn't a stapler just a one-dimensional version of that, a more limited one?

JHawkins: No, but the fact that it is limited is the difference. The fact that there's...

Viviane Clay: Thank you.

JHawkins: The fact that it is a high-order sequence is the difference. It can be learned as a sequence, whereas the movement of the joystick or the movement of the cup on the table cannot be learned as a sequence. You can form a sequence from joystick movement if you just do left, left. You could learn it that way. You might learn, while playing a game, that you do certain patterns really quickly. I used to have that when I was a kid.

Viviane Clay: Not good.

JHawkins: As a kid, I had this Plexiglass Cube, which is a three-dimensional maze. You could see into it, and it was divided into maybe 10 by 10, so about a thousand cubes inside. It had all these passages. You'd put a ball on one end and try to rotate the cube in different dimensions to get the ball out the other end. It was very hard to do because you couldn't really see the passages too well, since it was all plexiglass. I learned how to do this blindly. I just learned how to rotate this thing over and over again. It always comes out, and then the fun of it was over. Why do I bring that up? It's something that started out as a very complex, hard-to-solve behavioral problem, and it became a high-order sequence. I guess that's why I'm bringing it up. It became a complex, high-order sequence. It took about 30 seconds to do.

Niels Leadholm: That's interesting. I think that ties in nicely with some things we've talked about before. Even things like a t-shirt—the first time you're folding a t-shirt, you need to learn a temporary reference frame or representation of the t-shirt in its current state. It's a very deliberate, model-based thinking of how this thing needs to move to a particular location, but over time, you develop a pattern for folding a t-shirt: you grab it by these points and follow this sequence. Maybe there was never really a learned model for the former. You leveraged simpler models through a slow process to behave intelligently, but it's very slow, and there's not a behavioral sequence you can just use.

JHawkins: I would agree with that. In the beginning, you just—

Niels Leadholm: And so maybe the joystick is the same. It takes a while, and eventually you just learn a mapping between pushing up on the joystick and your character moving forward.

JHawkins: That's a step. I don't like the joystick for these reasons. It doesn't represent a behavioral sequence to me, yet it is a way of using behaviors to affect changes in the world elsewhere. It's a sort of goal-oriented behavior, which I think is a good example, but we haven't really tackled that one yet. I'd rather put the joystick into that category. It's a going behavior—how do we learn how the joystick controls the world to achieve a goal? It's not the behavior of the joystick; it's how the joystick interacts with other objects.

Hojae Lee: One more thing that would simplify, Jeff, the 4D grid cells model even further is if we represent layer 6A with XYZT, and also layer 4 with all the features and the changes. For example, one change we're trying to extract from sensor modules is optical flow. Instead of the changes going into Layer 3, changes are just another type of feature. Then we could keep the existing layer 4, 6, and whatever model comes out is a morpho-behavioral model. It's not a separate morphology or a separate behavior model; it just has all of it. I think that would be even further. I'm not saying that's right or that we should do it that way, but—

JHawkins: I think—

Hojae Lee: Simplifying.

JHawkins: OJ, I want to make sure—I think you were arguing for the nicety of using 4D grid cells, because everything else flows out. Whatever happens, it works.

Hojae Lee: Yeah.

JHawkins: Is that not what you were saying?

Hojae Lee: That's what I want to say. I went back and forth on whether separating out space and time was better. At first, I liked that idea because it seemed like it would give us more flexibility in terms of using one independently from the other, but now, maybe representing as XYZT, I'm moving more toward that idea after this meeting. Thank you.

JHawkins: You're putting a warmest vote on four-dimensional grid cell. Is that what you're doing?

Hojae Lee: Yeah, I'm just saying that if we have four dimensions and also include change as a feature, then I'm taking that even further in terms of grouping everything together, which might not be the right idea.

Viviane Clay: In my mind—

Hojae Lee: I like it, I like that.

Viviane Clay: It's really whether we have XYZT. I feel like we need that, but whether T is represented in the grid cells or somewhere else—

Hojae Lee: Yeah, the tuple XYZ all together, in the crystals.

Viviane Clay: Yeah.

Hojae Lee: Yeah.

Niels Leadholm: Just to be clear, what was your reason for preferring that?

Hojae Lee: Let's say that if we are representing grid cells, if the grid cells represent space-time, and also in Layer 4 we're representing features and changes, then with the existing mechanism we have with the green arrows in layer 4 and the vertical arrows between layer 4 and 6, before, with just features and just space, we were creating a morphological model. But if layer 4 can receive features and changes, and Layer 6 can receive space and time, then those two combinations can create a combined morpho-behavior model.

JHawkins: So you're going back to the idea that we don't have a separate behavioral column. We have behaviors and—

Hojae Lee: Maybe we don't have a separate morphology and behavioral model; maybe it's just one thing.

Viviane Clay: But then we can't apply different behaviors to different objects if they're just in the same model.

Hojae Lee: I haven't thought about that.

JHawkins: It'll—

Hojae Lee: I know that somebody was going to—

JHawkins: Going back to the figure that Rami showed earlier, at one point, we decided the only way to—when we were still working on the idea of unified morphology and behavioral models, we reached the conclusion that behaviors can be applied to other models, but it requires hierarchy.

Hojae Lee: You can't do it within the column.

JHawkins: So the behavioral model in one column could direct morphology in another column. Now, I'm not saying that's right, but that's how we got to that picture that Rami showed.

Hojae Lee: Yeah.

Niels Leadholm: For what it's worth, it doesn't feel to me like we need time in the grid cells to have behavior or morphological models. That's not the blocker. I guess it's the blocker if we want to fit it into L4 and L6. To paraphrase, an argument for having time grid cells is that it prevents having to represent time in another layer, if that's a disadvantage.

JHawkins: You're throwing time into the L6 bucket, and in theory, no one else should know about it. But this is not time as in the matrix cells—let's be really clear about that. This is sequences. This is time sequences. That's what it represents. It's not timing.

Viviane Clay: It's more like state space, maybe.

Hojae Lee: Yeah.

Viviane Clay: Discrete states in a sequence.

JHawkins: It's a sequence of states that are learned in one dimension.

That would be a lovely outcome if, somehow, we made layer 6 cells represent space and time, and then everybody else doesn't have to change. Somehow, we could get a single learning module that learns both behavioral models and morphology models. I would love that, but I'm not dismissing Viviane's idea.

Niels Leadholm: I still feel like that's a separate question—whether a single column can learn both behavior and...

JHawkins: But if it came out...

Niels Leadholm: Even if we represent time in layer 5, or layer 3, we can still learn both in one column. In principle, we can learn both in one column. The issue was...

JHawkins: There were problems that made us think about moving to two separate columns.

Niels Leadholm: I agree, but I feel like those are separate from having somewhere to represent time.

JHawkins: Maybe I should stop using the word "time." It's really representing something different. I want to distinguish it from matrix cells, which represent timing.

Viviane Clay: I've been calling it "state," because I feel like that applies more to morphology models. You can have different morphological states and different behavioral states.

JHawkins: But in this case, it's states that flow through time—the states that change through time.

Viviane Clay: You traverse state space in one direction.

Niels Leadholm: It may also be action condition, as we sometimes talk about. It might not necessarily be time that pushes you through it.

Viviane Clay: No, it's an order sequence.

JHawkins: Yeah.

It's funny, because thinking very theoretically, you might say objects have different states, even different classes. If they transition in a uniform way, we would learn it as a sequence. There's some potential hope for unifying classes and behaviors—classes are the steps along a behavioral sequence. But if you don't have a behavior, you could still have different morphology of an object representing different classes, and if they do transition through time, then you'd learn it. If they don't, then you wouldn't learn it.

It's an interesting idea.

I'm going to have to write notes after this meeting. There's too many things we talked about.