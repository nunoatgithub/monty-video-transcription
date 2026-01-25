There wasn't anything super specific. We still have a bunch of open questions. Viviane made some really nice updates to the document, cleaning up the written notes and making the diagrams not handwritten. We also had the neuroscience questions from last week—about four or five. There was some discussion in the group, but I'm not sure if anyone has done any reading beyond what we discussed there. We can approach any of these as we want. One thing we discussed is that it might be useful to review the existing model of how we think behavior might be working, just to clarify any uncertainties.

Maybe on the neuroscience one—what were you going to say?

I was just going to say that on Ram's radar, we had a couple of comments about how the two models can be learned and applied independently. In the recap of our current framework, we talked through that again to make sure everyone is on the same page, since that's one of the two key ideas. I just want to make sure everyone understands that part. That would be great. I feel a little lost. No worries, it's complicated. Also, Jeff has been working on writing up a version of this to be published, so we can start publishing these research meetings in more of a patent disclosure style. That's where I took these diagrams from, and hopefully we can share that this week.

I can talk through the current state, but maybe it's better if someone else tries to explain it, both because of my voice and to test your understanding.

I can try. Sure.

Should I try and share my screen? Where's the document? Let's see. I feel like those figures might be helpful. It should be shared again in the research meetings channel on LinkedIn, I think.

Yep.

Can you see this?

Yes.

Okay.

In the cortical column, we have a layer 6A where there are reference frames. These are pathable, and it's basically just a physical location with respect to the object. It's a reference frame with respect to the object. Any movement of the eye or sensorimotor movement is transformed and used to change the location in this reference frame. There are other movements, like a local movement change, which is basically a visual stimulus move or an object changing, and that will go into layer 3.

There are a lot of parallels between the morphology and the behavior model. In summary, there are two reference frames: one for the behavior and one for the location, and one for the morphology model. They move in synchrony, but the behavior one is associatively linked to changes of the object—some movement of the object. The morphology model is associatively linked to features like colors, edge orientations, or edges. Everything you're saying is correct. Just to clarify, the purple ones are the behavior model errors and the morphology one—I wrote "object model" instead of "morphology model," but we use those terms interchangeably right now. Go on. The associative connections between the two layers—between movement, location, and whether it's static or changing features, the movement features—determine whether this is a morphology model or a behavior model. In a similar way to how we pull features at locations into object IDs, we would be pulling movement at locations into behavior IDs.

These would go to the higher level, or we could discuss that after. The timing here, we think, comes from matrix cells and encodes the intervals between each change. It's basically encoding how long it takes between these changes, like a tempo, and that works for both feature change and static features.

The temporal part doesn't go into the morphology model, at least not as we've discussed so far. The neuron that sends its apical dendrites to layer 1 is only in the behavioral model. Only for the behavioral model do we have a temporal sequence of changes. For the static one, since it's static, nothing changes over time, so we don't have a connection to layer 1. As we observe the objects and the movement of the eye, I think it doesn't matter.

The intervals between when we get these static features don't really matter. At this point, no, because the eye movement is already integrated in layer 6A. How we move over the object and in what sequence doesn't matter for recognizing the object, so we don't need to learn a temporal sequence there. In that sense, a melody would be a behavior, then?

Yes.

Okay. Jeff is in the document. Should we ask, since he's looking at the same document, if he wants to join the Zoom as well?

Just write in, read fake letters.

Hi.

I don't know if we can see or not.

Okay.

This is the part I understand, even though I've described it very differently in my writeup because I was trying to propose a different thing. I'm interested in this now, so I understand that these movements are in physical 3D space. Basically, what we're learning are changes at locations—these locations describe relative positions in physical 3D space. If we're modeling changes there, they'll be tied to whatever morphology is defined by the relative locations.

This is the part where I'm getting confused. The morphology model—maybe that's a bit of the terminology confusion. When we say that this green one defines morphology, it's in the sense that it stores the point normals, curvature directions, curvature, and all these static features at those locations that define the morphology of the object. Only the locations themselves aren't part of the morphology model. Movements relative to each other in space are encoded in the behavior model. They don't represent anything about the morphology of the object; they just represent which parts move at what points in time, in which directions, or which points change their features, but not the features themselves. Does that make sense? Yeah, it makes sense.

But there are still relative locations. For the morphology model, we're storing edges at these relative locations, and that's how we understand the full model. When we're dealing with a behavior model, we're storing the movements also at relative locations.

In some sense, these relative locations would not be the same if you're talking about a different model.

For example, it ties in with how you apply behavior to an object, which depends to a certain degree on its morphology. If there's no way to map those two, then it's not clear that you can map that behavior onto it.

Take a ball—a sphere can have the hinge behavior, but that happens by mapping parts of a ball that approximately look like a hinge and splitting it in half. If you took the top curve of the ball and the bottom curve of the ball, that's not really a hinge; that's something different. So I feel like there is an implicit morphological model there, but that's part of how the behavior maps onto it.

Maybe the way we use "morphology" is a bit ambiguous. When we talk about the object model, that's really more than just the relative locations to each other, which is what you sometimes mean by morphology. The point you raised—Neil said the object has to have the correct shape to apply the behavior—is something that just naturally comes out of it. We won't anchor the reference frame of that behavior to an object if those changes at those relative locations are not occurring because the object doesn't exist at these locations. For a behavior to be applied to an object, the object needs to exist at those locations, and the changes need to be happening at those relative locations. But it doesn't need to know anything about the object model itself, or it's not tied to that object model. You can still apply it even to these artificial setups, like the ball. You can make the hinge small enough to fit onto the ball and then imagine parts of the ball moving.

But only parts of the ball. You would not be able to map it onto the new relative locations that are defining the ball.

I wouldn't be able to move the upper hemisphere of the ball up and down to mimic that behavior. It will still be tied to the relative locations of the stapler. Why? Because, just like you said, it is only going to move parts of the ball that adhere to this relative location. Otherwise, it wouldn't be able to, but it's nothing to do with the stapler. This column doesn't even need to have a model of the stapler to recognize the hinge behavior. It's really just the changes at locations in a sequence of changes at locations, and these locations are in a reference frame that is unique to that behavior. All of those locations are unique to that behavior, and it moves through that space in the sequence that it's learned for that behavior. Then it can apply that—it doesn't know anything about the stapler at all. It might have learned that behavior on the stapler because it observed it there first, but there's no connection right now between the two models.

It doesn't know it's a stapler, but it knows the relative locations, which is what's confusing me. I feel like we are building associative connections between the relative locations. I know we're not storing any features there, but they are still defining how the stapler looks because the movements are stored at these relative locations. If the relative locations are changing, for example, if you change from a stapler to a laptop, the hinge becomes a different kind of hinge, but it's the same behavior. They don't tell you how the stapler looks; they tell you maybe where the stapler exists, but they have no information about the surface, curvature, point norms, or color. They don't store any information about how the stapler looks, only where it observes changes.

Maybe places also exist on a different object, because a different object would have different places where you want to apply the same movements. To paraphrase, this gets more into the outstanding open questions: if we apply a behavior to a novel object, how do we predict the appearance of that object as it moves? We've talked about potential solutions, like anchoring point to point, but I don't think the current model solves all of that. It's useful to have that framing so it's clear what we've discussed and what might be right, and what are open questions we need to brainstorm and understand better.

It sounds like your questions are more about this open question. Your description was really good and accurate for the current model. I just want to say I don't think I did a very good job in my writeup explaining what I was aiming for, but this exact point is what I was trying to solve. When I say apply behavior on a different morphology, this is the open question I'm trying to address. Maybe in my presentation, I could do a better job of explaining how to do that. That's a good distinction to make because it's something we haven't figured out yet. Thanks, Neil, for pointing that out. This proposal is incomplete. It has some nice properties, and the one I was focusing on is that the two models are quite independent, but we need to make them a bit more dependent, and we haven't figured out how to do that yet. For example, I've learned the hinge behavior on the stapler and have a general hinge behavior model, but how do I apply it to a different object and make predictions about the features on that object? That's an open question.

In my presentation, I might try to define a behavior space where they might not be aligned in physical 3D space. It might deviate from our current understanding, but just take it as a proposal. It might even be useful to do a spectrum—maybe start with the Pacman behavior on the clock or stapler on a laptop, where they are similar, and then go from there because it's more intuitive. If what you're proposing can solve it in the more general case, that's great, but before jumping into the hardest cases, like applying a stapler behavior to a very different object like a sphere, maybe start with the more intuitive ones.

Is that kind of learning a new behavior? One more point: if you scroll down to the lower figure, the one that's much more complicated, the two reference frames are only really aligned in their space when we learn the new object and behavior. Then we move through the two reference frames in synchrony with the same input, laying down points and learning about it. When we recognize them, we can recognize them independently at different locations and orientations. For example, if you look at the yellow arrows that go back down to the orientation layer six B, it might be a different one for the object model we're recognizing than for the object behavior we're recognizing. I might have recognized the hinge on the stapler and then recognize the hinge on the door, which is a totally different orientation. We'll need to modify the movement that goes into the two different reference frames in a different way. There might also be different scales, like applying the hinge to a smaller part of another object. They're not always aligned or exactly the same in physical terms. They also anchor differently—one is anchored to the behavior, the other to an object. The movement will move them in synchrony, but they'll be different representations.

This makes sense.

On this diagram, one thing we can discuss is something that ViiV and I were just discussing in the document: whether L5 might also work as a location for the behavioral model, which we've talked about in the past. L3 and L5 tend to have really strong reciprocal connections. Some people think it's two parallel pathways in the brain—L4 and L6, and L3 and L5—but L5 and L6 have really strong reciprocal connections, so it fits. Even if the movement information is coming in at the border between the two, that also fits with both of them path integrating based on sensorimotor movement.

and then motor output fits that. If we talk about goal states and the goal states matching the behavioral states, or using it to plan movements, in the Mento paper they discuss the two parallel systems and the right L5B reciprocal connections. L5A and L5B are often confusing. In primates and rodents, according to the Archic paper, they're reversed: L5A are the large cell bodies, intrinsically bursting, and in primates those are the goal outputs. I would imagine that in primates, L5B is handling the behavioral state space, and L5A takes that information and proposes a goal state that gets sent out. In case that helps with the presentation, the change here is that these are magnocellular projections. From what I've read, these go to 4C alpha or 4C beta, something like that. If we're talking about blobs, from what I've read, these are coming from cellular, but I don't know if they represent change. If we have both of them in 6A, they could still be making associative connections with 4C alpha and 4C beta.

Just separate it in sublayers. That would be interesting to discuss. The inputs—I'm not sure if you have that paper.

One paper I thought would be interesting to quickly show is Gilbert et al. from 1977. It's a good example where they looked at response properties across different layers of cortex and saw a pattern: really small receptive field movements in the shallower layers, and much larger receptive fields for detecting movement in the deeper layers. When we talk about L6 integrating movement from the sensorimotor system versus the superficial layers detecting movement of an object feature, this is the kind of data that comes from that.

As with anything, it's complicated in terms of which layers are actually doing what. Everything between L3 and 4C seems to have some degree of movement detection.

Let me share this. This was in one of the writeups: magnocellular goes to 4C alpha and parvocellular goes to 4C beta, which fits nicely. If we want to have associative connections with layer 6A, I think it would just make associative connections with both, and then would go into the interblobs in layer 2/3.

I'm trying to find the latest copy of the paper. The hierarchy paper is under our personal email addresses, so I always have to log out.

I can invite you with your CVP1, or another address. I think we've hit the maximum, and Supertie is the owner of the document. I'm going to move it to another document to format it properly. If it's possible to move it to TBP stuff, that would be great.

Do you remember, Viviane, the sources on magnocellular input? Was that from the Cortex textbook you were showing?

No, that was from a paper that tracks them from the retina, from the ganglion cells all the way to the striate cortex.

These are the ones I have here right now. Do you mean those, Niels?

Or what specifically? Let me look at your giant PDF. It was just a question of movement—where that's actually coming in.

My giant PDF has several images from different papers that show different things, so it doesn't necessarily give clarity. Here's one of the papers I reference in the heterarchy paper. It shows magnocellular to layer 4C alpha, parvocellular to 4C beta. That's consistent with what you're saying, Rammi. They also go to the blobs. There's a lot of text about that. There's controversy about whether the magnocellular and parvocellular pathways stay segregated even when they get into V2, and there are arguments for both yes and no.

What is a blob? I'm not familiar with that term.

Niels had a nice figure for it. Let me pull it up. Basically, these are cells that are sensitive to color. Under certain stains, they form blob-like structures, which is where the name comes from. In general, when we talk about minicolumns, Jeff often pointed out that you see this indicated with orientation. All the cells in L4 tend to respond to the same orientation, but maybe that minicolumn structure goes through all the layers, so they're detecting all motion in a certain direction as well. This fits with the idea that these are all cells sensitive to a particular color. They're conspicuous in that they're almost everywhere except for L4. Even though they're representing features like color, they're actually outside the classic feature detection layer. L4 is more about orientation, and these might be neurons that respond weakly to color and bias the column when color information is present—more likely to see a banana if it's yellow, for example. From the corneal cell, the signal goes into these blobs and represents blue, yellow, and so on, from the retinal ganglion cells. They might use some color, but if you look at the images, one shows that the koniocellular cells project to the blob and magnocellular to 4C beta or alpha.

Yes.

They show inter blobs as a blob-shaped thing too. I thought it was just a space between blobs.

There's another distinction in V2, which I don't fully understand. These layers—the thick, thin, and pale layers—and projections from different parts of V1 go to different layers in V2. This seems like the next version of blobs, but I don't understand them very well.

What book is this figure from? Is it from a paper?

Yes. I don't remember which paper, but I've seen it in multiple ones. I could send you some references.

I'm just wondering if it was the book on color vision. Maybe, I'm not sure. I can look it up. I think it was making the argument that these pathways stay segregated even into V2.

Viviane, that might be something worth querying with Jeff. We want to update those figures because the layout in general—how we represent the movement information coming in—is often shown at the border between L3 and L4, but we'd want an actual citation for that.

Here's the other one I referenced, where the retinal ganglion cells go to the magnocellular ones in LGN. Here it seems like layer 4B.

Even though they show micro for C, they show movement being extracted from that somehow. Here it's still in 4B. The dividing lines in the figure don't correspond clearly to the labels on the right-hand side.

For example, 4A is written on the border between one color and another, so what does that mean? What is 4A?

Maybe that's the point—there are functional divisions, and maybe they're focusing on the functional ones. This one is just about functional segregation.

The movement projection that goes into 4C alpha is different from the behavior ID that gets pulled into a more superficial layer. You would still want the behavior ID to be in layers 2/3. This helps because one of the issues I was worried about is whether we're expecting too much of L3. Is it going to do behavior ID, object ID, and motion detection? If it's doing motion detection, it's not clear why it's then passing that information on to the next cortical column in the hierarchy.

We once thought maybe that was a form of skip connection, but I think we said we can't have the behavioral model in layer 4 because the time matrix projections don't reach layer 4—only the neurons in layer 3 have the apical dendrites.

I also suggested maybe the behavior model is in layer 4, but that was the argument against it.

So the high-level behavior model could still be in L3, if that's the kind of pool representation, but I don't know if that necessarily is. What needs the L1, the matrix L input? Do these apical dendrites synapse on 6A as well, or just 5/1?

The ones that come from the matrix, the L1.

I don't think 6A, I think 5. I think L3 and L5 are the ones that classically send dendrites, and L2, but 6 and 4, not so much. That's my understanding at least.

The reason I'm asking is because if the reference frame is attached to or tied to the changes, maybe there's a way to get this indirect signal of overlaps through the reference frame.

I think it would have to get it through the associative connections.

So that's some more neuroscience questions to think about and maybe look into.

It feels like maybe we're narrowing the space where these things could exist. I think it would be worth going more in depth into the literature on what we know about the anatomy and connectivity of especially layers 2/3.

It's a shame that people often look at them combined, but it would be useful to figure these questions out.

Maybe go through the open questions one by one, read through them, and see where we're stuck.

That's a good idea. Just to get a high-level overview of all the things we need to figure out, and then we can go away and think about them.

I'll briefly go over them. Intersect if you have thoughts on any of them, but we can also just collect them. The question of whether we can learn associative connections between the reference frames is a smaller question, but it might give us insights into how they inform each other and how we can apply a behavior on a term morphology. Mostly, I was thinking if I recognize an object's model and I've learned its behavior, I should be able to predict its behavior model already. I don't have to infer the behavior again. There seems to be an association we could learn. If I see the stapler and it's not moving, I know what behavior it can have because I've seen it moving before.

Could the behavior also inform the object? You said you're not sure that would make sense, but why wouldn't it? I couldn't think of a good example where you see the behavior, but maybe if you see a shadow of something moving, it gives you some idea of what object it might be. It makes sense that it could at least bias the recognition of an object.

This would really be more an association between the behavior ID and object ID.

If you recognize the behavior ID, it increases the likelihood of a certain object, or the other way around.

I don't see any reason why we can't learn it the other way around. The video Will shared during the retreats with the motion capture points—walking—would be an example of a behavior performed by a person.

That's a good example.

Niels, I feel like this deserves to be its own point.

If Jeff joins in 10 minutes, maybe we can ask him about this.

and maybe revisit also, I'll look at whether there's anything on the different sublayers of L4 and if some have more connectivity to L6 versus L5, depending on the literature.

Let me quickly go over the other ones. This one is smaller: can multiple behaviors be detected at the same time? That's more of a side question. The big one is, are there compositional object behaviors? Like we have compositional objects, so for compositional objects, we have this concrete idea from the hierarchy paper: the object ID gets sent to layer four of the higher level and becomes a feature on that model. We have backward projections, and we calculate the relative orientation of the child object to the parent object and send that up. But is there an analog for the behavior model? Or do we not actually learn behavior models in a compositional way, but instead just recognize higher-level behaviors? That was the question we discussed at the end of last week's research meeting. For that one, it might be useful to define what we mean by hierarchical or compositional behavior.

The open question is about a behavior where the child's behavior directly impacts the parent or vice versa, as opposed to a self-contained behavior.

What I mean is where the behavior ID becomes a feature on a higher-level behavior. You can learn behaviors at this higher level as well, which is why this purple part is here. You can learn a behavior model here, but does this model, when you have behavior IDs as features coming in, actually use them? There are many cases where that would be true.

For example, with a car, you have something low-level like the handle on the door, then opening the door, then turning on the car, then moving it. These are all interrelated in some higher compositional object, and that higher compositional object can have behaviors like driving.

You could argue those are all behaviors applied at different locations on the car, but it might be necessary to learn causality between different behaviors or how they're connected. Otherwise, it gets complicated, like trying to model an entire object with one reference frame. We want to split it up.

I don't see a fatal issue with having nested behaviors. The second question is whether the behavior ID actually becomes a feature on the object model, since it's static, or on the behavior model, since the behavior model encodes changes. By that definition, it would only encode if the object ID or behavior ID changes from one step to another. When it stays static, it would be part of the object model, which is confusing.

Then we had a question about applying temporary masks. That was an attempt at solving how to make predictions about objects—how to apply the object behavior to a new object morphology, like masking half of the stapler and rotating that part.

This is an open question.

I should probably move the next one down, since it's related to the previous one: whether behavior ID is treated the same way as object ID in the lateral and backward connections, and how we communicate timing in the behavior. Do we only communicate the behavior ID, or do we communicate behavior ID plus where we are in the sequence of the behavior?

Maybe we can write "sequence location" or "sequence point" to clarify the difference between seconds and sequence. Can we vote on just "position"?

Position sounds better.

Now these are better ordered. The next one is related to the temporary mask: the more general question of how we predict morphology in the middle of a behavior, like we discussed earlier. It's a big unsolved question. Even in the case of an object we've learned, like the stapler, even if we've learned the hinge behavior, it's not obvious how to predict what the stapler will look like at a particular location, let alone applying hinge to a new object. Our proposal currently allows us to recognize behaviors and objects independently, but it doesn't allow us to make predictions.

A related idea is that maybe object behaviors can help us segment objects into sub-components. If we see a part of an object move, that might indicate a child object. This fits with compositional behaviors: the more complex a behavior or object change, the more likely we are to segment it into child objects with their own behaviors. Jeff often gives the example of a transformer model—if it's something that does many things, you might understand each component and how they fit together. I don't think segmentation necessarily requires a compositional behavior model, but it does require hierarchy, since we have child and parent objects. I would think of it as recognizing the behavior in the high-level column.

We had an example of a chair where something hinges off the back. We recognize the behavior and that informs us to split the object into sub-components, which then become parts of a composition object. The object being decomposed is the object model, not the behavior model.

Maybe, or both. Say it's a rocking chair with a button that lifts something up. The rocking is the behavior of the parent object, but then we may separate out that, at this location, there's another smaller object with its own behavior, which is to flip up, and you can press a button on it.

That flip-out button would be the behavior recognized at a specific location. To your point about whether it's the change that's passed, the behavioral ID, or the change of behavioral ID that's passed up, it seems to fit with the idea that if the behavior influences the higher level, it's because there's a change happening that's interesting. If they're totally independent—the button flips up, you can press it, and it turns red—that's just a feature at a location that can be different at different times. But if pressing the button causes the chair to start spinning, then the change in behavioral state is informing the high-level behavior. For example, a keyboard might have two behaviors: you can type in "query" or "VRA" or "Colmac," and there's a light on the keyboard. If it's blinking, the behavior of the keyboard is different; if the light is green or red, it changes the behavior of the whole keyboard. The change of the light from red to green is a type of behavior for the light, and the state of whether you're typing into "Bo" or "V Mac" is a behavior of the keyboard.

That kind of reminds me of the big open question: how do we predict morphology based on behavior? It seems like where we are in the behavioral sequence needs to give us a state, like whether the light is on or off tells us what the morphology model should expect.

In your case, I don't know if the letters change when the light switches, or if you just see something else. The whole layout changes, so the position and behavior of the keyboard changes, not just the layout of the keys. That would be completely different, and you would just adjust to it. If the light is on, the way you use the keyboard is completely different—you type in a completely different layout, or you can just change languages and type in a different language.

That seems like a version of predicting different features based on which stage in the behavioral sequence we're in.

In terms of hierarchy and predicting optic morphology, maybe we don't want to go down this route, but if you represent a stapler as a compositional object with an upper arm and a bottom arm, the totality of the behavior of the upper arm is that it can rotate and move through space, but it cannot deform within that object. That makes it easier because the relative positions of objects do not change; the whole thing can move and reorient in space. That's a state that gets passed up to a higher-level region, which might model the motion of that relative to the bottom one. If you have the child object, it can tell you, given an orientation of the stapler arm, where things are. But it also feels constraining, because we don't want to break everything up into children and parents. With a really complex object, like a balloon that you can squeeze in any dimension, how do you model that?

High-level behavior can be decomposed into just a change of orientation if we keep going down the layers, but I'm not sure that actually works. In the stapler object, there still has to be some sort of change that's more than just the orientation and position of the whole object, so I'm not sure it helps that much.

It still feels like the solution to predicting morphology has something to do with associating locations between models. The more complex the behavior, the more you have to learn these associations to predict what feature you would see. If it's a simple behavior, you can fairly easily map what you would expect to see after the behavior has happened, in terms of features at locations.

Definitely a big topic to think more about.

I’ll move on to the next question so we can go through them all. This one is about movement within the behavior reference frame being path integrable. You can observe a behavior at different locations, and it doesn't matter in which order you go through them. This is like a reference frame: we have one for the object, but we also have a sequence of states or changes. The question is whether that is path integrable or if it's really just a sequence, requiring you to learn different sequences for more complex things, like the behavior of a joystick. Do you have to learn many different sequences for moving the joystick back and forth, or can you learn a more general state space for the joystick? Maybe those aren't mutually exclusive; if you can represent something as a composition of small sequences, that is basically a path integrable space. For example, if you learn that moving the joystick up results in a certain state, that's a sequence at the time you learned it. If you can chain that with other transitions, you can probably do path integration. What we want to avoid is having to learn, for example, "two times right, five times up, two times left," as one sequence, and then represent a totally different sequence separately.

They may not be as separate as that.

That's a good point—these sequences might be combinable.

Hey Jeff. Hi there. I'm sorry, I was told something this morning at the last second and forgot to tell everyone. Sorry to join so late. I can't tell if you can see me or not.

Yeah, we can see you. I'm just standing outside on my phone.

No worries. We just had a high-level discussion about neuroscience and other topics, and now we're going through the existing open questions and discussing them, mainly to revisit and think more about them.

We already went through the main questions around object behavior models. The remaining ones are longer-term questions about actions, goals, representations, and anatomy. Now that you're here, it may be worth revisiting a couple of topics we discussed. Niels had an interesting proposal—Niels, do you want to talk about the layer five behavior idea?

I wasn't on the call; I was doing something else. I actually wrote a response to that.

Okay, cool.

I wrote a lengthy response because I was thinking about it. I just had to meet a contractor right away, so I apologize. I thought it was a really interesting idea, and you'll see I posted a lengthy response.

There's a lot to like about it. We've often talked about layer five as the place where behavior would be represented because of the motor output projections. Maybe over the hackathon, since we focused on the space being path integrable, it naturally led to thinking about layer six. In my mind, for the two reference frames—the morphology reference frame and the behavior reference frame—they would likely or almost certainly share minicolumn definitions. I'm continuing to work on the idea that minicolumns are the basis of grid cells, and that the cells in the new column all represent movement in a similar direction. You would want both the behavior and morphology referencing to be updated simultaneously by the same movement vectors. If we say layer 5B minicolumns are the reference banks for the morphology model, and layer 6A minicolumns are the reference banks for the behavior model, they would share the same minicolumns. The difference is that both layer 5B and layer 6A would be updated simultaneously, but they anchor separately. The input to the column goes between layer five and layer six, projecting upward and downward at the same time, defining the same minicolumns but anchoring them separately. Layer 5B also has long-range connections, so it would be voting on behaviors. That all makes sense.

Wouldn't it technically still be different movement vectors for the two? For example, if the behavior model is recognized in a different orientation than the object model, they are transformed differently in the thalamus since it's in the object's reference frame. That's a possibility we discussed. I don't know if we know there's enough down projections for that. It would be nice if it has that flexibility.

Interesting. In some ways, it fits with the alignment of behavior and morphology—you probably can't apply a behavior to an arbitrary morphology if there's no way for them to align. The orientation also has to be aligned for them to match. For example, the hinge must be aligned; you could have a hinged vertical on an object and a hinged horizontal on another object. In that case, both the morphology performing the hinge behavior and the behavior itself are oriented together. You might have learned a stapler model and the hinge behavior on the stapler in one orientation, but then you see a door hinging in a different orientation. You're not recognizing the stapler; you're recognizing the door. The morphology of the hinge on the door is also oriented. If it were a stapler, it would be oriented the same way, but the behavior would be rotated. I'm not sure I fully understand that. You might be right, but I'm missing it.

Let's say I have a classic old light switch with a little thing you flip up and down. Now I mount that on another object where it's horizontal.

So both the morphology and the behavior are rotated in that case, right? No, but the object it's on is different. I have two objects: one toy has a switch horizontally, and one toy has a switch vertically. Wouldn't they require two different behaviors to turn on the switch? You might be right, Neil. It's not obvious to me. In that case, it feels like a child object—if the switch is represented as an object, it can be oriented differently in space. That's true if it's a child object, but we can't say all behaviors are on child objects because they have to exist in every column.

The nice thing about this proposal is you can recognize behaviors at different locations, orientations, and scales on different objects. That would require the behavior model to send separate hypotheses down to the thalamus to rotate into its reference frame.

Here's an idea: what if there were two separate orientations? One of the interesting things about the thalamus is that its layers seem to come in pairs. This is a half-baked idea, but I think that's also what Viviane has been suggesting—that there are two different movements. Exactly. This is what I drew here: two different orientations are recognized and projected, and they separately rotate the incoming movement that goes in. I haven't seen this figure—maybe I have, but I don't remember there being two different orientations. That was only in the complex version. Actually, the two different orientations are in this one as well. Those two are supposed to be different, but there's nothing indicating the difference, right? Oh, I see—the little details. I didn't really pay attention to those.

But it doesn't say what the mechanism is. I didn't follow through on it. This would basically mean two separate columns. If I had two hierarchically arranged columns with different orientations—a child orientation versus a parent orientation—then the behavioral and morphology models might have two different orientations.

You'd need two projections back to the thalamus, and the thalamus would have to do two different transformations, unless Niels is right and I'm misunderstanding his point. I'm just thinking about whether it's necessary. It seems like it is, but I could be wrong. It's an extra complexity. We don't love to have complexity, but maybe it's necessary. That might simplify the idea of having one of them in layer 5B, so we don't have to assume they get exactly the same movement. I think they have to be updated the same, don't they? The input to the thalamus is the same, but then it gets rotated into their respective reference frames. For what it's worth, these could be separated in time if needed. They can have different orientations and different scales. That's an issue we've never really dealt with, but it has to be addressed.

Given your argument, and maybe convincingly so, these things really aren't tied together. They have to be driven from the same basic movement vector going into the thalamus, but after that, they have to be translated separately—movement in the behavior frame versus movement in the morphology frame, with different orientations and scales. Then I wondered, how is the thalamus going to do both of those things? The thalamus comes in layers, and there seem to be two of every type.

Maybe that explains why there are two layers of every type—what's the point of that?

Even for the left and right eye, I believe there are two left and two right eyes.

That could explain why you have multiple layers in the thalamus. The scale example convinces me, because that one definitely needs to change. This requires other things too: the projections to the thalamus have to come from different places. There have to be two orientation projections to the thalamus—one to each layer. That's not out of the question; it's just not something I know about. Maybe someone has observed that.

And then, revisiting the microcircuit, Rami brought up the interesting point that if you look at a lot of the literature on the magnocellular input and the movement input, it tends to be in L4C, at least in V1, this lower part of L4, whereas we've often shown it coming in at the border between L3 and L4. I was just wondering, do you remember, was that kind of an indirect reason? If you look at the responsiveness of cells, V1 is unique to primates, and I have zero theory about what those extra layer four cells are doing. When you look at it, they say there are three projections that come in; they're typically not broken out as magnocellular or parvocellular. Maybe people know that, but I don't. There's the one that's the typical lower layer three/layer four, and the border between layer five and layer six. That's what they say. I imagine that would be non-primates, or not vision—could be whiskers, could be rat, could be cat vision. When it comes to the striate, I have no idea what's going on. I've never heard a cohesive theory about what's happening, and I haven't thought about it myself. I don't know if that impacts what you just said, but I just try to avoid that. No one knows what's going on.

Some people have argued that the labeling of those striate layer four cells is incorrect. They say, "Oh, do people say there are multiple layer fours? That's not right. Some of them should be considered not layer four, but more like layer three or multiple layer three." I heard that argument made once. I was just looking at a figure from Thompson et al.—Alex Thompson. Is that like L6? Huge paper. Maybe this was partly where some of this comes from, because this seems to suggest the magnocellular input should drive both lower and upper layers, but with different receptive field sizes. It's driving the overall movement of the sensorimotor in layer six, and it's detecting the movement of the object in layer three.

These don't show that. Again, this is the striate layer, so all bets are off as to what these really are. It's hard to say. It's interesting because this even seems to suggest you get the parvocellular input into layer six as well. It seems there's almost overlap in where they all project, except for this slight breakdown. There's so much here; sometimes it's mind-boggling. I don't know what to make of it. Sometimes you have to look at the real details—are they just following axons, could these be projecting to inhibitory cells? There's a ton that's unknown, and there are multiple cell populations in each layer, so which are they projecting to? It's crazy. I always feel more comfortable when we deduce the function must exist than when we propose where it exists. The "where" is half guesswork, and you hope it's right, but sometimes the data you're working on is all screwy and it's hard to know. But we can deduce logically that certain functions have to happen, and therefore there must be a cell population that does it.

It was interesting that in the Thompson image, she didn't make any distinction between the two layers. She only saw the projections coming in.

That was an interesting idea—that there might be evidence that the differences between those two layers mean they're not just equivalent duplicates, which you don't typically see in nature.

While we're on open questions, I like to remind everyone that we think layer 6A is the reference frame for morphology, but we have no explanation for why layer 6A projects back to the thalamus. I don't remember one, and that's a major projection.

Why does the thalamus need to know where we are in an object? That's essentially the question. Here, the projections—doesn't this fit with the idea that this back projection is the orientation of the object, and this back projection is the orientation of the behavior? Both are separately applied to the magnocellular pathway, but what they say is the same cell in layer 6A will bifurcate, as shown here, and send a projection to layer four. Again, this is the striate cortex, so I'm not going to pay too much attention to all the details, but the general rule is the layer 6A cell will project to layer four and also to the thalamus. If it's orientation, that's great, but we're using that as the location signal for morphology.

Isn't it just a location, like an association? I can see sending the orientation to the thalamus, but I don't know why I would send the location. Could it be something to do with scale—maybe the grid cells are somehow detecting scale? I thought about that because it's a very unique representation, basically representing a unique point on a unique object. In the world, there are a gazillion of these things, and it's a high burden to expect the thalamus to recognize them. It's like an SDR, with many variations in the world. If that's correct, it's hard to imagine that the thalamus, which is a pretty small object, could learn to recognize something unique at every location. On the other hand, if you point out that scale is one of those things you might vary by location, just like orientation is something you vary by location, maybe that's the answer.

I think that's something we've talked about before. I'm still thinking—did we? I think your concern at the time was that the SDR was too complex or something like that. It's just too much to ask. I can't expect the thalamus to remember every location and every object and do something about it. It's just not possible.

It could be that there are some locations which are important to note, where you might have a different scale or orientation to consider at that location. We have to remember this, but it can't be every location because it seems like too much to ask the thalamus to learn. There aren't that many cells in the thalamus compared to the cortex.

I haven't been too worried about it; I just included it. As we were talking about things we don't understand, like voting between sensors—such as two hands—the idea you proposed before, we're talking about the projections to the S, right? I don't know how that would help. The sensorimotor system would need to know where the other sensorimotor system is to be able to do that. I have trouble imagining that's happening in the thalamus.

That has to occur someplace, but I have trouble imagining it being the thalamus.

That's a big open question, Robin, as to how we know the relative locations of objects.

We've had lots of good questions to think about. I posted some text on that document a little while ago. Now that we've had this conversation, I'd like to retract some of the idea that the two minicolumns in layer six—the two morphology and the behavioral model—should be the same. Viviane convinced me that's not true, so I should retract that.

Okay.