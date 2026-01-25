Ramy Mounir: the first to mention this, last week, so I'm just putting it in some slides with visualizations so we can maybe discuss this more.

And... the work that has been done at Numenta, back then with HTM and, temporal memory, was a learning of a sequence of features. These are ordered features, like A, B, C, D, or, learning a melody, with features. They were not at specific locations, but they're only at relative locations, just going from one to another, and we did not really have control over the sequence transitions, so we were just, passive listeners, to the melody, and it's just going through one feature to another. So the only thing the model can predict is really What is the next feature, given the feature that we're at, and the context, or, like, where we're coming from? Which sounds a lot like what LLMs are doing. LLMs, there's difference in how we store the context. LLMs, they... you just have to, every time, just feed it all of the context, and just, it will predict the next token. With temporal memory, the context is already stored in this forward projection. As we go from one token to another, the SDR itself is storing the context for us. Which is very nice, because you don't have to backpropagate or do any of those, tricks. But that was limiting in some sense, because we could not actually add actions into this. We could not go from A to C, or we could not go from A to D. Usually, we don't need to in these kinds of, if it's a melody, we don't need to go from A to C or A to D. But when it's an action... when it's a... if we're learning morphology and we have action, for example, we want to... we have sensor movements, and we want to control, where to go to next, we need to extend this theory. We need to add, locations and a reference frame. the idea is that for now learning a morphology, it's the same concept, but now we have action. We can go from one feature to another. we control the sequence transitions with actions. And the idea is that if we start at one feature, we put that in the reference frame at the bottom here. And then the action is going to take us into a different location in the reference frame, so we need to understand what this action means, basically. We need to... that's... that's in the reference frame itself. It's embedded knowledge in there. we... it just takes us from one feature, and then we map the... we use the action to take us to another place, and then we put the other feature in there, and then we do the same thing over and over again, until we build a model of the cup. we have something like this. Now, this is something that LLMs can't do, or any other model out there. This is... we're building a structured reference frame using the actions that... basically a sensory model framework, and we're using those actions to lay out those features in the correct spatial positions.

so that was extending, sequence memory into morphology, and I think we agreed last time that there... there are parallels from this and learning behaviors. One thing before I go into that.

is the idea that these... we need to understand what these actions mean, and this, to me, was something I've been thinking about this morning, which is... it's just... it's an idea that I haven't thought through, but what if the, actions... what if the input to Layer 6 was, mostly about actions, rather than a movement itself. So it's what if we associate the actions with the movement in the reference frame at this input? it's like presynaptic representation would be the actions, and then postsynaptic would be the movement, and that's what we're associating. I'll talk about that later, and maybe at the end of the presentation. But that's just some insight that I had while I was putting this together.

any questions so far about this part? I think we all agree on this.

Jeff Hawkins: I just... I just commented on the... I was there, too, for a while, thinking, oh, maybe the, maybe there's a different interpretation of Layer 6, we're taking actions moving through Layer 6.

I'm gonna present... I don't want to step on what you're going to present, but I moved away from that yesterday, or 2 days ago. Okay. I'm a propose... that was a lot of problems with that idea. It kept tripping me out. I couldn't make it work. It didn't make sense, so I have an alternate proposal, but that's not to take away what you're presenting, Yeah. But.

Ramy Mounir: one kind of evidence that I had for this, or, it's not really evidence, but what kind of insight and support of this would be, the layer 5 motor output in V1 that goes back into Layer 6 in the region 2. And I thought, this is a reference copy of the motor output that we had from the lower region, and it's going... it's being mapped into a change in the location of the reference frame in the higher region.

Jeff Hawkins: but it still could just be just movement in space, right? It doesn't have to be something else.

Ramy Mounir: Yeah.

Anyway, this is not the main focus, but, just... the parallels, basically, between the morphology and behaviors. similarly, when we're learning a behavior, we're looking at a sequence of behavior states, and, The definition of a state itself is... it has its own reference frame, a spatial reference frame, and it's basically pulling spatially those changes at locations in the reference frame. So it's... it's each one of those is a morphology, and we're doing, second-order pooling of some sort, but we still have to have... a reference frame to store those changes at these different locations. But if you look at the higher order transitions between those states, it looks a lot similar to what we had before. we can have a behavior that's unfolding in front of us. We don't really have control over how to go from one state to another. These are just... The transitions are just laid out in front of us, and we cannot freely control that transition. But there are other examples of behaviors where we can actually control the transitions. Let's say we're opening and closing the stapler. Then the stapler is just... it could be closed, and we're just opening. This is... So we can just basically go through the states in a shuffled manner, or an unordered manner, which is similar to going through learning a morphology By disregarding the actual, order of the states, or, the sequence, the features in the sequence. similarly here, we control the sequence transitions with the actions. one action could take us from here to there, and then another action could take us from here to there. And this may not be the same behavior that we learned or observed by just looking at it, being open and closed, either by someone else or just play... played in an animation.

we actually can control that, we can control the transitions. similarly, I was thinking that we can map those actions in some reference frame. I know we haven't agreed on this yet, but I'm just saying that actions are being mapped to locations in reference frames, similarly to how this happened in morphology. But it would be a 1D reference frame, but just because we can control those transitions, we can learn to map the actions into state transitions like this. So a movement in the reference frame.

And then, again, I was thinking here, we would associate actions with the movements, I want to learn, how to go from here to there. I need to really understand what this action means, or associate it with some, with the change in the reference frame location.

This is... I think this is a big open question. How do we do that? How do we associate? Some... some action.

Jeff Hawkins: I'm gonna pro- I'm gonna propose a solution to that today.

Ramy Mounir: Okay, cool, yeah, nice, it's... yeah, I've been thinking about it.

Jeff Hawkins: That's basically the main thing I'm gonna try and propose today.

Ramy Mounir: Nice.

Viviane Clay: Yeah, I think it's good to clarify, this is the question we're trying to solve, this is the problem. space. We have talked a lot about modeling behaviors that are just a sequence before and have a pretty good solution, but now, how do we do behaviors that involve actions? And yeah, I think those slides visualize it very nicely.

Ramy Mounir: Nice, okay. It's just, one insight is that it seems similar to morphology, and I was just suggesting that maybe we still have the same problem with morphology, basically learning how actions translate into movements in the reference frame. This is something that we're also, if we can't solve it for behaviors, if we can solve it for morphology, we'll be able to solve it for behaviors.

Jeff Hawkins: I don't know, I view it as... I didn't view that as an unsolved problem for the morphology models. I thought we have a pretty good idea how that's happening. it's literally... you can start off by thinking if it's just a single sensor patch, you can think of it just movement of the sensor patch through space. And.

Ramy Mounir: Yeah.

Jeff Hawkins: That... that's... and then it... that movement vector updates the grid cells, and... I agree there's a seeming parallel here, but I'm not sure if you think that is an unsolved problem on the left bottom corner.

Ramy Mounir: we I think we still have to translate between, an eye muscle movement, which is going to be an action. So the action is not really in the reference frame, but rather, I'm thinking of it as, a muscle movement for the eye to turn it Right. Translate into a different location in the reference frame. But, just a week ago, we talked about how.

Jeff Hawkins: we know that the cortex doesn't control muscles, right? and we talked about the very colliculus, and how If you specify... if the... if the movement relative to the object is translated to a movement relative to the body.

then the optics, things like the spray calichos can handle all the complicated machinery to actually get the sensor to the right position. So that's... that's... that's one direction.

Anyway, I just want... I'm not sure, there might be a problem here, but I didn't... I'm not aware of the major difficulty on the bottom left corner. Okay.

But, the challenge is, it seems like the bottom right corner is similar, but I'm gonna argue at the moment it's not. It's different.

Ramy Mounir: Okay.

Jeff Hawkins: I didn't... I didn't understand that until 2 days ago, so it's a new idea.

Ramy Mounir: Yeah, this was everything I wanted to present. I think we can start discussions from here. That'd be a nice segue into what Jeff has,

Jeff Hawkins: I think it's a good intro.

Ramy Mounir: Thanks.

Jeff Hawkins: Yeah. I just, just a few more words on it. as we said last week, at the end of our focus group, focus week, it wasn't another week, or three days, what do we call it, focus session. Mini-week, mini session. It's more than a mini session. It just struck me how, at least myself, I've been thinking about this incompletely. we've been talking all these discussions about behaviors, as you said, and we've always... we've always... the model we came up for modeling behaviors is always a high-order sequence model. Even the stapler, we viewed it as a high-order sequence of behavioral, of movements or changes in the object, but in reality, as you point out there, it's not a high-order sequence. You can move it up and down, like I described in an old document I wrote a few days ago. And so that the idea that, hey, there's... we never really dealt with the equivalent of a sensory motor... I don't want to call it a sensory motor. We haven't dealt with the equivalent of the fact that most behaviors are tied, are not... are not self-generated. They're not high-order sequences. Even when we talked about, a light switch turning on a light bulb, that's... that's... the light... if the light bulb went on and off periodically every 3 seconds, then we... then we could say, yeah, that's a high-order sequence, like a traffic light. But if the light goes on when I flip a switch, that's not a high-ris sequence. Yet, it's also a movement that's not in... it's it's not a movement in the behavioral model, it's not a movement in the... if you don't looking at the lamp, the thing to turn the lamp on is occurring somewhere else in the world. And it was like, this was the... the epiphany that it felt like last week was like, oh, we haven't really understood That there's this division between high-order behavioral sequences and non-high-order behavioral sequences. And if we think about that, then some of this stuff will come figure it out. Anyway, I'm just repeating some of the things you just said in different language.

So why don't I share my screen? I'm gonna use, ExcalDraw here. So yeah, I'll be good. Let's see on the first thing I did... As we talked about, I'm showing here two columns, or two learning modules, but in the language of biology, so columns. And, I'm showing one learning morphological models, which we spend an awful lot of time on, so that should not be new. And then one showing behavioral models. If you've been following this, you know that, originally we thought these might be combined, and then Vivian said they could be... they maybe should be separate, and I never really felt comfortable with that. And, one of the reasons I didn't feel comfortable with separating the morphology models from the behavior models is I just didn't know how they'd interact. I... that was just one of the reasons. I just didn't know how these two would... before, they were co-located, you could understand it a little bit better, but I just... I didn't... I couldn't work it through of how these two would relate to each other. Because, obviously, I learned behavioral models as part of some morphology... some morphology someplace. Anyway, so the first exercise I did was, just to start off on the left here. writing down the kind of things we know about morphology models. And if behavioral models are identical, we should be able to map the same... onto the same columns, the same functions, we should be able to map them to behavioral stuff. just to remind ourselves sticking to the left side here, let me bring up my little... this is... this is our standard object here. We have features coming in, which would be represented in many columns. I, we'll just call them morphological features. We associate them with the location. I'm not showing the input to the change in the location. So these end up being SDRs that represent a particular morphological feature on a particular object at a particular location. Recently, we've... we've always talked about pooling these morphological features, these are the different points on the object, that you could pull them and create an object ID. And then recently, as we've been thinking about it, we said, hey, you know what? When we have when we have objects exchange, like the stapler, the stapler can stop in different positions, and and we can do... and we can do flash inference on the stapler that's open or closed or in between. So that required us to actually, if the... if the movement of the object stops moving. then all of a sudden, we can start learning the morphological features again, and then we'd have a state ID, so this would be, like, the keyframes. this would be like, oh, what the staple... what is the stapler? The staple is open, the staple is closed. It's still a morphological model, so you get an overall stapler, you have different positions that the stapler might be. And these would... you could vote on both of these, right? It's clear now that the... it's the object state ID, which is the one that gets passed into the higher order column as a... as a child object. if I put a picture of the open stapler on the coffee cup. I would learn it as the open stapler, not as the closed stapler. I'd say that's the thing that... so the... I'd have to be able to associate this keyframe or this object state, as the child to a parent. So this, in some sense, is the major output of the column, is this object state. That would be, in the staple example, again, open, close, or anywhere we see it in between. Other objects could be, the traffic lights on or off, or switches up or down, or something like that.

the only reason we actually, just to review, the only reason we actually really need the overall object ID, which would be, like, stapler. Is that we can say the word, we can think about it as a stapler, and so there seems to be a representation in the brain somewhere that, it's a stapler, which is... which you could just, by pooling over the object state IDs, or pooling over all, over these things, you get an ID, but it's now actually... it's clear that the object state is actually more important, at least for hierarchy, in compositional modeling. So that's where we were. I put a little note down here in the bottom. And I said, a morphological column is self-contained, that it can learn sensory motor models in high-order sequences. Oh, I didn't mention the high-order sequences. If it turns out that we observe the object over and over again in the same order. like I move my finger in a particular order over an object, then the features would come in the same order, as Rami just showed, and it would be high-order sequence. And the neural mechanism we came up with for the, for temporal memory, it learns high-order sequences, and it learns sensory motor sequences. So this... the same basic temple memory algorithm, we've shown this over and over again, can learn, sensory motor models, and it can learn high-order sequences by just... by just, associating Sdr is one after another in this thing. down again to the bottom here, I say a morphological column is a self-contained. It can learn sentimos models and high-order sequences And in some sense, we can think of this all by itself, that you don't really need anything else. If you give enough time to learn, this thing could learn. Morphology mod... morphology models.

Viviane Clay: And we can also learn higher-order sequences of the object's state IDs, in case of the behaviors that just unfold.

Jeff Hawkins: Oh, that's interesting, I hadn't thought about that.

Yes, we could.

Viviane Clay: isn't that the, the idea of the behavior models we talked about so far? That we would basically just learn as... for sequence of states.

Jeff Hawkins: but, it wasn't temple... the behavioral models we've run so far is not a temporal sequence of states, it's a temporal sequence of Changing features. Alright, the huge difference between this model on the left and this model on the right is that these features are static features. Think of them as the parvacellular cells from the retina. They're static. It's only when things stop moving that you get this, so nothing's moving at this point. And then what we've talked about for the behavioral models is just the opposite. It's like the feature is when the input, the thing that's input into layer 4 is only when, the feature's changing. You have a morphological feature that's changing. This would be, like, the magnet side of the cells. And so this might be an edge, this could be... this would only be an edge moving, and if the edge wasn't moving, you wouldn't get a feature here. But here, if the edge is moving, you don't get a feature, but if the edge is static, you get a feature. Here, if the edge is static, you don't get a feature, but if the edge is moving, then you do get a feature. That was...

Viviane Clay: Yeah, but there we would... we could, we would also learn a sequence of behavior state IDs.

Jeff Hawkins: so I just was... I was picking apart maybe one of the words you used there. I didn't show that here, but I suppose we never talked about this, but I don't... maybe we did, I don't remember. I don't... I suppose there's no reason, we could just say, sequences can be learned here too, right?

Viviane Clay: Yeah, because, in the case of a structured model, it would... going through a sequence of states, it would be much more efficient to learn a sequence of state IDs instead of A sequence of all the possible features at all the possible locations, that you could be anywhere, and moving your sensor arbitrarily over that behavior at the... while the.

Jeff Hawkins: Yeah.

Viviane Clay: are softening. it would be easier to just say, okay, now you're in behavior state X, so expect these features if you go to that location.

Jeff Hawkins: You lost me there. I want to make sure this doesn't... if it's... I'm trying to understand if what you just said is going to cause problems or what I'm going to say in a moment, Do you want to say that again?

Viviane Clay: Cool.

Jeff Hawkins: I... Let's just start for... let me just back over a second. This is... this is an SDR, Object State ID. And I suppose... if, if an object... let's say an object was the traffic light, and so it just went through a series of instantaneous changes, something like that, then you would have, the red state, the green state, and the yellow state here. And I think you're saying, you could learn the sequence at this level right here.

Viviane Clay: Yeah.

Jeff Hawkins: Is there anything else you're saying about that?

Viviane Clay: No, that's the main point. It might not be relevant for what you're about to talk.

Jeff Hawkins: Yeah, I don't...

Viviane Clay: Yeah.

Jeff Hawkins: Yeah.

It is... it's a confusing thing for what I'm going to talk about right now. I'll just... I'll just... I'll just say that If... if the temple memory algorithm, if this is... If this works... here's... Yeah.

you... in theory, you could learn sequences up here. If this is an SDR, and you have transitions of SDRs, you could just learn that sequence. I wasn't counting on... I wasn't thinking that, so that's... that's a new thing for me.

Viviane Clay: I was just thinking, for our behavior, it would be better to learn there, because... You're still having the location representation, and you can still move arbitrarily through that location space, so it'd be very hard To, at the same time, represent a sequence in layer 4, while also, predicting different features for different locations.

Jeff Hawkins: the, Layer 4 would be the following. Imagine I'm touching a coffee mug. or pen, and I just... I've developed a habit of touching it in the same sequence over and over again. I fidget with the pen, and I move my finger over and over again.

If I did that, then Layer 4 would basically.

Viviane Clay: Yeah.

Jeff Hawkins: maybe... yeah, it's a little confusing. The way we've defined it, that as the finger is moving. this model wouldn't get any data, because as the finger's moving, we were over... we're now in the behavioral model, right?

Viviane Clay: Yeah.

Jeff Hawkins: It's a little confusing. I think it becomes more... the whole idea of sequences over here is a little bit confusing. It makes a lot more sense in the behavioral models.

Viviane Clay: Oh, yeah, I was saying it for both, also for the behavior model, that Behavior would be learned as a sequence of states instead of a sequence of incoming features.

Jeff Hawkins: I'll protect it.

Viviane Clay: Because you're not seeing the same.

Jeff Hawkins: Let's go over there, because I think... I think even what a state is weird. Okay, everything on the left here. is going to be basically built on static morphological features. That is, think again about the private cells. He just says, only respond when there's nothing changing On the sensor patch. And everything over here is the opposite. Everything over here is based on Times, things that are changing. The central... the morphological feature is changing, it's not static anymore. And everything's based on that, so when we think about... talk about behavior states and object states, I think we have to keep that in mind, the whole thing. Let me just try to walk through this a bit, and let's see if it becomes clearer.

What we... what we did... Prior in our behavioral models, we just said, okay, let's just substitute here, instead of these Static features, we're going to put in these dynamic or changing features. And if the object isn't moving, there's nothing going on in this model. Nothing. Only when the object starts moving. Do we start modeling something here? And the object starts... stops moving again, then this model stops. There's nothing going on here anymore. It's only active during active changes. we did that, and we said, okay, if we just use the same mechanism we had in the behavioral... in the morphology model. The main difference would be time, because there's a sequence of time going on here, but other than that, we could... we could basically pull whatever features are moving, this would be all the edges that are moving on the stapler. all those edges that are moving at certain locations, then we could pull that, and we would get a behavioral ID. We can say, oh, that's the stapler opening, something like that. Or this is someone walking. That kind of thing.

I asked that, I asked myself, is there an equivalent to be... so that's what we had before. We had these two items. And we also use the location. The location's still... where is the sensor on the object? So that's... that's not gonna help us for anything else. It just says we're looking at the staple at some point, that point's moving. Other columns are looking at different points, and those parts are moving. If you pull... if you then take all that, and you pull them, and you do a pooling together, you'll get, an object of a hinge, for example. instead of being stapled, I wrote it down as, oh, we talked about that's... that's a hinge behavior. And then I... then I asked myself, what would be the equivalent of a behavioral state? over here, we had the object state, which is, the state was, open or closed. Those are two morphologies. Is there an equivalent to a behavioral state on... on a behavior. This is not obvious, and so I'm not sure I know the answer to that question, but I said to myself, if you think about the, the behavioral state is a subset of the overall behavior, right? this is the stapler, different positions the stapler can be. This is the overall behavior of a hinge And maybe... maybe the state of different states that could be occurring is that the hinge is moving up or the hinge is moving down. Those are the two states you could have. Both of those are part of hinge, right? And it doesn't... and at any point in time, place, the hinge may be moving up or moving down, If I were to ask myself, what's the equivalent of the object state which is, open and closed, but now I'm talking about changes. This is the best I could come up with.

Viviane Clay: But I thought... I thought we already had behavioral states, and a sequence of states that define the behavior ID. depending on where you are in the stapler or hinge opening behavior, you'd expect different changes at different locations. At first, you'd expect the changes along this.

Jeff Hawkins: but remember, with the stapler.

I could... I could say the staple is at 45 degrees. But that doesn't tell me how it's gonna move. It could go up or down from there.

Viviane Clay: Yeah, but we still have a representation of states, within the hinge behavior, there are different states of the hinge moving, and then, yeah, it's...

Jeff Hawkins: So what are those... what are... what are those different states?

Viviane Clay: where we would expect the changes to happen? at any point in time, where would we expect changes to happen?

Jeff Hawkins: Is that... that seems like it's, the same thing I'm saying here, right? if I have observed a hinge, Let's say this hinge goes between 0 and 90 degrees. at zero degrees, it can only go up. At 90 degrees, it can only go down. And in between, it could go up or down. I don't know. It depends on how it's moved.

if you want to call it... that's pretty much what I'm calling a behavioral state. It's it...

Viviane Clay: Yeah, so I guess how I thought of the behavioral states were, like, I'm just copying a picture next to yours, I can move it in a moment again. each of these slices would be a behavioral state, and then all of those pulled together would be the behavior ID, and then so far, we only talked about transitioning through those in time, so a certain amount of time passing means now we expect movement to happen here instead of... further down. And... but now. We want to be able to actively move the stapler, so now we would have to figure out different kind of transitions between these. behavioral states.

Jeff Hawkins: I'm not sure how that's disagreeing with what I'm saying. I'm confused.

Ramy Mounir: Can I... are you saying, Jeff, that we only have two behavior states for the whole, movement of the, behavior hinge of the stapler?

Jeff Hawkins: Maybe... maybe. Here's what I'm... here's what I'm saying. I'm trying... I started with our model here on the left, and I said, what if behavioral models are identical? They have the exact same... and I'm not sure this is true, so I'm just saying, what if they were identical physically? there's the same neural machinery. then I should be able to... take everything I know on the left side here and find the equivalent in a behavior model on the right. Because let's assume, maybe incorrectly, assume that they all have... we have the same basic Cortical column. What would that imply?

and that's what this exercise is. I started out, up to... up until recently. I hadn't really been thinking about the equivalent of this layer here, this object state ID. We didn't even understand this from morphology models until pretty recently, oh yeah, we need to do, keyframes, Learn what the object looks like if it stops in between. Over here, nothing... nothing here is representing what the object looks like. There's nothing here about looking morphology. It's just, points that are moving. And so I'm just saying, what would be equivalent to this guy? In the hinge case. If I just have a hinge. and the hinge is rotating on a pivot point, and let's say the hinge goes between, 0 and 90 degrees, the only thing I could think that's equivalent to behavioral states is that at any point in between 0 and 90 degrees, there are two possible directions this hinge could be moving. It could be moving up or moving down. At the 90 degree opening, it could only move down, the 0 degree opening, it could only move up. This is not a main part of what I'm presenting here today. This is just... I would... if I had to... I was just trying to put words on what would be the equivalent of this. over here. Now, Vivian, you've been thinking about it more than I have in this diagram here.

But, if you think about this, if you call this a behavior... one of these planes a behavioral state. then, that state, you don't know which way it's gonna go, right? It could go up, so I would say the equivalent of this diagram is that I'm at this position. And at this point, there are, this could go one way, or it could go the other way. if I'm looking at some point. In... in the... at some point in the behavioral model, there are two possible ways it could go. It could be going this way, and I guess I was calling those states.

Viviane Clay: Yeah, I agree with that. I just... I just thought that was, like, what we already had in the current behavior theory, but only that, so far, we basically just had one set of transitions that were possible, and that those were through time. Corrections.

Jeff Hawkins: Maybe the difference here is I started out from a different way of looking at it. I started out by looking at it. How would I map these onto these layers? What is it? And I never thought about that. This, to me, was always... when we talked about this, it was always this conceptual idea. And I'm just... I'm just saying, hey, it actually can be represented by these... these... these neurons right here. And if I was... that's... that's all... that's all I'm saying. Okay, yeah. This isn't right. I just... I just looked at it from a different point of view. I said, let me... let me find the mapping here. Where do these things fit in the... in the model?

Yes, the way you've described these, as long as you're agreeing that if the stapler had its self-motivation, if the stapler just did its own thing, and I didn't have to touch it, it just went up and down, then I would move through these states in a high-order sequence.

Viviane Clay: Yeah.

Jeff Hawkins: Yeah,

Viviane Clay: Basically, before we just had these errors up here, and then now we're talking about how can we also have those down here and use different.

Jeff Hawkins: but it also... it means at any point, I could stop moving up, and I could move down again. I could just go up a little.

Viviane Clay: Yeah, exactly.

Jeff Hawkins: Not good.

Viviane Clay: back.

Jeff Hawkins: So it's not it's not like I just want to jump to the end state. there isn't... in a... in the general case, there is no end state, necessarily. I could just be opening it halfway, and then I... and then I would just be closing out a third. We kept talking about, oh, there's some goal... maybe we can still get there, there's a goal we want to get there, but... but the model itself isn't always, in this order.

Viviane Clay: yeah, so if you're in the middle slice, you have two possible actions available to you, going backwards or forwards, and those are different actions. Yeah, I guess I just wanted to... I was just confused, because you said we only had the behavior ID before. And that would, in itself, wouldn't be sufficient to predict which features to see at what location we would.

Jeff Hawkins: it would be if you learned the secrets If you learn the sequence here,

Viviane Clay: Yes, yeah, so you still need to know, you still need to represent where you are in the sequence, or infer where you are in the sequence.

Jeff Hawkins: this is the first time today that we've ever discussed maybe having sequence IDs, sequences in the behavioral state. representation. I never considered that before. up to now, to me, sequences are always in this Layer 4 And that works.

It works. But, I hadn't thought about, oh, maybe we're learning sequences of state IDs here, which is possible too, so that's a new item for me. It's not the main point of what I want to talk about today. So I... at best, hopefully we're in agreement. What we're saying is, hey, I'm just trying to map this onto, layers of, if we have a model in layers of cortex here, we should have something very equivalent here, what are they? And just... just state it like that.

It would also imply that, of course, many columns are voting on both This would be like, oh, this is a hinge, but this would be more like, oh, the hinge is moving up, and the hinge is moving down. That's what the voting would be doing there.

now the main thing I wanted to get to here It's just this text down at the bottom here. Which is... it's just essentially saying a behavior column can learn behaviors that are high-order sequences. as Rami started out, and we talked about last week, but often behaviors are caused by other behaviors and events occurring elsewhere. That is, this is not a self-contained column. If I'm modeling this paper. and someone wants to open the stapler, that's not here. That's... I can't represent that. it's tempting to think, oh, at one point, I think, oh, my finger's touching the stapler, so I just move my finger. But that's not true. If you think about, the light again, or most things in the world, I might be modeling a lamp here, and... and the thing that's changing this... it's changing... making the lamp change, or something change, is elsewhere. It's not in this column, right? It could be anything, really. I turn the flame up on my stove, I rotate a knob. It's, that knob is not the flame. So how... so there's a general thing that... These models can be driven by external events that are not contained within this model. And there's not really an equivalent over here, is I don't need to know anything else besides the object I'm modeling and... and where my sensor is to learn a model of the... and make predictions about morphological models. But here, behavioral models are driven largely by external events. So that is the big difference, and the question then is... the first thing I had to do is say. pay no attention to this movement location here. It has nothing to do with changing the behavioral states. This is just part of this model. And... and... and don't think about it like, oh, this is my finger, how does my finger move the stapler up? That's the wrong way to think about it, because I can move the stapler up with my other hand, or with... with a stick, or with, something else, right? there's... there's got to be an external signal that's telling this guy, what it... what... what behavior should be exhibited. And so every time we've talked about, like, all these things, turning the light switch, or, what are the other ones we talked about? Anyway, there's a ton of them, right? You do something, and it causes an action elsewhere. So that was the first... so the first big insight is, we need... this is insufficient on its own, and... and the things that could control this behavior could be anywhere. it could be anything. If I want to turn a light on, I could move a switch. on the light, I can move a switch, it's on the other side of the room, I could clap my hands, I could say, hey, Alexa, turn the light on. there's almost unlimited ways of things that behaviors might be created that this object can change, and so I have to have some sort of way of broadcasting behaviors from elsewhere. I have to be able to associate the behavior of the switch with the behavior of the lamp. Or anything, really. There's no... and I started working through examples. It's really complicated, because sometimes, a behavior, if I'm rotating a dial, I could have a dial that I rotate the dial imagine I rotate... as I rotate the dial, the stapler goes up and down as I rotate the dial. So there's a continuous movement of the dial that corresponds with the continuous movement of the stapler. Or I could push a button, and the staple moves up, and I push a button, and the staple moves down. Or I could have an up, down, and a button, and a down button. there's... and so there's all these combinations between sequences and behaviors that are tying to other sequences of behaviors. So we need a general mechanism To coordinate, behaviors in one part of the world to behaviors in another part of the world. So this is the, proposal I have. I want to, in this case, just focus first on the right-hand side. This is, again, is our behavioral model. And, I'm showing the left side here to say, if this is happening at the right, what would be the equivalent on the left? But let's start with the right. This is the behavioral model we have here. And so the first thing I can say is, We need some sort of broadcast information, because this guy could learn to change his state based on almost anything else. I'm gonna... I'm gonna propose that there is some broadcast information, and it's a... it's gonna be learned as a causal association, that if something... some other behavior occurred in the world. it's going to be broadcast, and then if my behavior changes, this column changes, I'm going to learn the causal association. It's going to be time-order dependent, that is, that if something else had to happen first, then if I change, I can learn that might have caused me to happen.

there's two things, This goes back to the other stuff I was talking about last week, and I wrote this quickly last night, so hopefully it's... the language may be messed up. I might have to walk through it carefully.

what is broadcast? I'm going to propose one of the things that's broadcast is an attended area, an egocentric space. Now, I proposed this as required earlier. Remember, I talked about, This is, how I... I talked about attention. Attention is just, this area, an egocentric space, and we can use that to learn morphology models. We can learn that to learn, compositional structures. We haven't spent a lot of time talking about it, but I've developed this in my head pretty deeply, so I'm just going to state it there, that we needed... I needed this idea to even learn morphology models, that you attend to an area in space. And then, when you attend to that area in space, then you... then the columns in the cortex infer what's in that area. Do you remember? It was like, like I was at the intersection, and I'm looking around the intersection, and it could be a static intersection, but I would attend to different objects in the intersection, and as I attend to those objects, those would be typically things that aren't always there, like a car or bicycle. That the rest of the cortex says, what's in that area? And it can be multimodal, it says, okay, there's a bicycle in that area, or there's a car in that area. the same thing can be happening here with behavioral objects. I could be attending to an area in space. And I could recognize a morphology object, or the... or I could be... the cortex could be recognizing a behavioral object in that space.

it doesn't really matter. Once you get to this broadcast, we could say they're almost identical. You could say there's... there's... some people are saying, oh, what's in this space? Oh, it could be morphology, it could be behavior. We don't have to make a distinction. There's just some object that's been recognized there. And, so I said here in this next sentence, the inferred object can be morphological or behavioral. And what's broadcast is, I go, okay, tend to this location space. This guy might say, oh, there's an open stapler there. And this guy might say, oh, I'm observing a hinge opening in that space. You get one of those two. I don't think you get both.

there's a lot packed into that already here. did anyone not understand what I just said there, or is it... did I say something confusing?

You gotta really get this idea that you... we've decided we're gonna tend to some area in space. And then the cortex as a whole says, whoever's observing that space, or wants to observe that space, or can move the observed space, come and tell us what you're observing there. And you're going to get this... these either behavioral state ID or an object state ID.

Ramy Mounir: I'm just wondering, why can't we have both? Are they voting together, or... Audio cutouts? D.

Jeff Hawkins: In Vision, you've got... these parvaccell and magnocellular cells are either-or, you can't have both. It's either, it's either... if the magnicellular cells are firing, then the private cellular cells aren't firing, and the proper cellular cells are firing, then the cellular cells aren't firing. It may not be that black and white, but that's how it's often described, and it's how I've been viewing it. So I haven't thought about yet... I haven't gone any deeper yet to say, oh, what would happen if I had both of them gone? It's possible, I don't know. But I'm just going for the moment. The key idea here is not that. The key idea here is that you have this attended space. Within that attendance space, Imagine you're, like, the hippocampus or something, and you say, okay, let's attend to this space.

and everybody who can attends to that space, and the cortex as a whole tries to return back the largest model it can find. It says, oh, I see a staple here, or I see a hinge opening here. Whether it... whether you can do both, I don't know. I've been thinking about it as not both at the same time.

Ramy Mounir: Okay.

Hojae Lee: Oh, so broadcast signal... I'm sorry, I'm trying to understand... is... What's coming into the column?

Jeff Hawkins: Let me tell you what broadcast single is. Layer 2 and Layer 3, they project broadly. we think of them as voting if you're in the same region. We think of them as, Layer 3 going to Layer 4, and the next region as... as a feature, but voting is really what I'm talking about. These...

Hojae Lee: These cells can... they can spread broadly.

Jeff Hawkins: and just for the moment, I assume they go everywhere. They won't. In practicality, they won't, because not everything is associatively possible. But just assume that... That, in parts of the cortex, people... all these cells are voting, and they're trying to reach a consensus, and whenever they reach that those axons spread broadly. They're available to everybody. anyone could learn, it's just some weird... it's just some, SDR out there, but if you're looking at it, you could learn it. You could say, oh, look, there's this SDR, I'm going to associate this with my thing. this causes... this thing that I'm saying is broadcast. These are being broadcast. Okay. But they're also coming in on apical dendrites. this is basically... this guy could say, look, I'm observing this. But... but someone else is saying, but I say, I'm observing some behavior, the stapler is opening. But a moment ago, someone said, oh, or, I just... I just flipped the switch up. there was a, I'm attending, so I attended some area, the switch went up. Now I attend to the staple, and the stapler goes up. Or, you go back and forth, so there's this sort of, you're alternating, I think I said it, by attending to a series of areas, there's an action occurring at point... location A, and then there's another action occurring at point B, and another action occurring at point A, or C, and another action occurring at point D. By going through a sequence of these. That, assuming that there's a time, dependent sort of plasticity up here, then this guy says, I'm observing a behavior, what was the most recent behavior? That occurred. And I'll associate my behavior with that most recent behavior. But this does... this requires attending to things. again, the child learning that a light switch turns the light on. They have to attend to the light switch, then they attend to the light, then they attend to the light switch, then they tend to the light, and they tend to the light. They... it's not like I just flip the switch on and I'm not even thinking about it. It's like, when you're learning this stuff, you have to attend to these things. it's literally, you can think of the brain just sitting out there, it's attending to novelty. All the time, it's attending to the novelty. It could be an unexpected object, or it could be, an unexpected action or behavior. And... because it's not incorporated in someone's model yet. So again, if I'm at the intersection, there's a whole bunch of things in the intersection that are static that are... that are always there. there's certain signs, and the lines on the road, and maybe there's some even actions that are always there, like the traffic lights are changing. But let's assume it's just morphological features at the moment. Now, a new morphological feature comes along, I attend it, or maybe there's a behavior someplace, something is changing someplace, and I go look at that.

the point is, you're just constantly going between these novel things in the world. And you're trying... and then, by... you're doing it in an order. But it's... it's not a high... it's not necessarily a high, order sequence, necessarily, but it could be just like, oh, the switch goes... was up, and now the light turns on. But you do have to... you do have to attend to these different... you have to attend, and attend, and it learns... learns causal... It's trying to learn causal relationships through the things you attended.

Hojae Lee: I see where you're going. I also like what broadcast channels are.

Jeff Hawkins: Yeah, broadcasting is not... it's just the same actions that are voting. It's not... there's really no difference.

Ramy Mounir: Are these coming from the thalamus, like matrix cells, or are they coming from neighboring columns?

Jeff Hawkins: The desk coming... it doesn't even have to... a column's anywhere The... Columns anywhere.

I could... I could tend to a light switch, And... I can imagine this. I can even attend to the light switch. I'm not in the dark, and so I'm attending to it with my fingers, and I... and so I'm attending, so there's some place, and I flow this switch.

I'm getting off your question, Rami, I'm sorry.

Ramy Mounir: I'm just wondering, I'm just wondering, is this, anatomically, is this, a layer 6 to layer 1?

Jeff Hawkins: No, these are layers, these are Layer 2 to... Layer 2, and let's say this... Layer 2 and Layer 3, just start there.

Ramy Mounir: Okay.

Jeff Hawkins: Those are the things we're broadcasting. Which we already do. We're already sending it to other columns. If... if they go to... if they go to the, imagine Layer 3 projects to layer 3. If the... if the axons that project... from layer 3 cells project to... the basal dendrite to layer 3 cells in another column, that's voting. That's... that's... that's I'm... we're trying to come to an agreement here. But if the layer 3 cells project to apical dendrites. Of another column. That's the causal association.

I didn't draw that here, I should have drawn that. That's a distinction. It's you can imagine... you can imagine this... these cells here, these can go three places. They can go straight over to here, to another... another column, not a behavioral column, but to another morphology column, let's say, and they're voting. They can go... the same axons can go and project to layer 4 in another region, and that's... that's a compositional structure, but these same axons can go up to layer 1 and go over to... and anyone can look at them, so anyone who's looking... all the columns in the cortex, in theory, could be saying, oh, there's this open stapler, or they could all be saying, there's a... there's a hinge that's opening.

That's available to everybody. the same action could go to layer 4, could go to layer 3, and go to Layer 1.

Ramy Mounir: I just didn't know about the anatomical projection from Layer 3 to 1.

Jeff Hawkins: I don't know about it either, I'm making it up, right? I do know that these things are... these things go all over the place, right? They do go all over the place, and you see there's no... there's not... they're not neat. We do know specifically that there is this, Layer 3 to Layer 3 sometimes, and there's also layer 3 to Layer 4 in the hierarchy. I'm proposing here, and perhaps this is a prediction of the theory, is that, these, these, especially here, these behavioral states, are... are going up to Layer 1. In some sense, it has to have... you have to solve this problem. We have to solve the problem. How do I associate one behavior with another behavior? And there is no... A prior knowledge about where these behaviors will be.

what they are. Mark.

We just... it's this occurred. I need to... I need to learn that.

This is a way of doing it. This is a way of doing a sort of causal association, between these things.

Viviane Clay: I remember the kind of anatomical evidence I showed last week. There was, like... this was talking about feedback connections, but they did go from layer 3 to layer 1. And... And layer 6 to layer 6 and 1, Yeah, it... My... there was definitely some kind of connectivity.

Jeff Hawkins: look, there's a huge number of details I'm skipping over here, which I don't know the answer to. But the big idea that I felt was a big idea. was just, first of all, understanding that we... we can't under... we can't resolve the behavioral paradigm, like, how do I learn light switches turn on lights within a column? We have to involve actions in two different parts of the world. I have to observe some sort of behavior in one part of the world, and associate with behavior in another part of the world. I have to do that by attending to them in sequence. And then I have to be able to broadcast the behavioral The recognized behavior in one part of the world with the recognized behavior in another part of the world. And therefore there has to be this, this sort of time-order dependent causal association, and I needed a way to differentiate that from, voting.

I do remember once that there was at least one paper, which was talking about apical dendrites. And they were talking about reinforcement learning or something like that, but they showed anatomical evidence that there is this, time order dependent, like, with... you have to, How's it work? That, when a cell fires, it sends an apical, a dendritic spike up the apical dendrites, and there was this time order, for that to learn, they already had the... the synapses up here already had to be active. it's the pattern had to be active before this guy could learn that pattern. This guy firing learns that pattern. there was this causal association time order going on in apical dendrites. Apical dendrites are very complicated, layer 1's complicated, it's not a uniform thing, there's lots of structure up there that we could talk about, but... but... so I'm not saying all apical dendrites do this. But it would make sense in this case, at least in this case of behavioral state ID.

And maybe even object ideas. One, one key item I... that I refer to here.

No, right down here, this one.

I said, by 10 to a series of errors, codal associates can be learned between any combination object ID, object state ID, behavior ID, and behavioral state ID. Imagine these... these four green lines here are all being broadcast.

Simultaneously, And when a column comes along, and it wants to try to learn a causal association. It could... it could assign... it could pick from any one of these that are active, any one that makes sense. it's interesting. It'd be saying, oh, if I see an object, I might predict a behavior somewhere else. Or I say, oh, I only see the sta... when the stapler is in the open position, I predict the behavior somewhere else. Like, when the... if I see an open stapler, then I expect the door to be open. When I see a closed stapler, I expect the door closed. So I could be... I could be associating object states together. And then I could say, oh, when the, when the, when the stapler is being, raised, then I can associate it with an object, or an object state, or with a... So there's these four things, and you can mix and match them. The associated memory wouldn't care. You can come through all kinds of, screwball examples of things we can do where you have either objects or behaviors associated with either objects or behaviors. And so the system says it doesn't really matter, anything that repeats over and over again can be learned.

That's one of the most exciting things about it. It's a very broad idea. It goes back to the fact that even though we think of these two columns as different morphological features, and and behavioral, morphological models, behavioral models. Once they're broadcasting information. it... there's... they look identical. No one knows that the information up here, where it's coming from. They just say, hey, I can associate it with any one of these things. it gives you this really great combination of abilities to Mix and match. To learn things. Did that make sense? Did anyone follow that?

Hojae Lee: yeah.

Jeff Hawkins: Okay.

Hojae Lee: No, it's very powerful,

Jeff Hawkins: it's very powerful. It's really very powerful, even though the details are fuzzy in different places. I had a couple questions that immediately jumped up to me.

One is, I still, I have ideas about this, but how is the attended area broadcast? How is that... how is that implemented? I don't want to go into it today, but this... all of this requires... everything I've been doing recently requires that we're constantly going through attentional areas and egocentric space. and columns have to know how to get to that area, or observe in that area, whatever. Another question I had was, how does reverse causality work? Like, how do I go from saying, okay, I've learned that when I flip the switch, the light goes on. How do I then say, I want the light on, I need to flip the switch? this is a... this is a time-ordered sequ... causality here, so it wouldn't work. how do I do that? I don't know, maybe this is something machine learning people understand. Yeah, that's...

Viviane Clay: That's the thing I was trying to answer last Friday with the... With the neurons integrating the goal with the current state.

Jeff Hawkins: maybe... maybe I could be more... maybe I'd be more receptive to that idea now, because I... I didn't really understand to what you were talking about last week. But now, if I can phrase it this way, if I can say, okay, what if this picture I've shown here is correct? and these... these apical dendrites and these apical dendrites are doing what I'm saying they're doing. Then you could... and then you could... then you could... maybe I'll understand your... your... your argument better, or what you're trying to get to. Because I didn't understand this is what it was, this reverse causality. I guess... I'm sorry, I just didn't... I didn't have the right framework to think about it.

By the way, there's a nice... another nice thing here, too, if I can just keep going on. This has to do with multimodal learning. Like how you can visually recognize an object when you've only learned it via touch.

And I think... This has nothing to do with behaviors, but it has to do with this basic mechanism I just talked about.

this has always puzzled me, how does... I can reach my hand in a box and feel an object and almost visualize it as I'm doing it? And then later, I can look at the object and recognize it. I've never seen it before. So as you learn an object with, let's say, with one sentence, let's say be a set touch. You attend to a series of egocentric locations. And the somatic system also broadcasts the features it inferring. It's like saying... the somatic system is saying, oh, I'm observing this feature, and, I'm observing this feature. These features could be simple. They could be... they could be complex features, oh, there's a handle, or it could be a simple feature, oh, there's an edge. Those are both... could work in this... these... this... at the bottom line, you could say the object I'm recognizing is an edge. So that's broadcast.

And then the visual columns are not getting an input necessarily, right? But they also know where the attended area is in body-centric space. And in some sense, the visual columns can say, oh, I would be a... I would... I'm in that space, even though I'm not getting anything, I would if there was some light coming in. And so I... actually, I think when you're doing this experiment, you would be... your eyes would actually be focused in the area where your fingers are, even though you... even though you can't see anything. And the visual columns would be saying, okay, I'm in that area, I know where I am in the ecocentric space, I know what feature's being observed. Because the somatic system is broadcasting it. So I can learn that, a somatic edge is a visual edge. And, I've learned that in the past. Therefore, I can build up a model of the object, even though I'm not seeing it. I know where we are in ecocentric space, I know where I am in that ecocentric space, I know what features are being observed there, that all information is available to me, even though I'm not getting any information.

And I said, here, this form of learning would work better if the visual system moves eyes to the attended area.

you can attend to an area visually without moving your phobia to that point. You can fixate on a point and attend to the side. But it's not very good, because your acuity off to the side's not very good. of course, usually when we attend to something, we move our eyes to it. And so I would... I would predict that if you were doing this experiment. You would be subconsciously moving your eyes to wherever your finger is, as if the eyes would be looking at them, because then... then those columns know where in the egocentric space they're looking.

So this ties into this whole same theory. It just says, yep, that's what we're doing all the time. We're attending areas in space, I'm learning... I can learn morphology objects this way, I can... I'm learning multimodal this way, I'm learning behavioral models this way, I'm associating behaviors with behaviors. And all with the same basic mechanism.

Alright, I'm done. That's it.

Viviane Clay: Yeah, I like that idea that, yeah, I think it's a nice solution to the multimodal kind of learning and sharing of models without having to have any connectivity between those models while learning. Basically, just... it's just attention to different spaces.

Jeff Hawkins: and broadcasting of whatever feature was observed by whoever. Could observe.

Viviane Clay: yeah.

Jeff Hawkins: That required by... to get stuff to work, you had to previously Touch objects while looking at it at the same time.

Because you had to associate The visual edge with the tactile edge.

So that... So that when there's a tactile edge, it predicts a visual edge, and there's a visual edge, it predicts a tactile edge, if the column is in that same location.

Ramy Mounir: So how big is the extent of these Layer 1 projections? I'm just wondering, can they... you mentioned that they can connect, across modalities as well. And I'm just wondering... Is it, is that something that we know that they extend, this far across modality and across.

Jeff Hawkins: we talked about a lot of this in the heterarchy paper, and maybe Vivian would remember it better than I do. We do know that there's connections that go across different sides of the brain, from the left side to the right side.

we know, that they're very diffuse. They, I wouldn't say that every Layer 3 cell projects to every column in the cortex, that's not true. But they are pretty extensive. And also, this is... This is just, this is a sort of a placeholder for actual... the actual connections. There might be, there's other stuff we don't know, there's Layer 5 to layer 5 cells, and so on, I do think what we can say is that, generally, anything that projects to Layer 1 goes long distances.

Ramy Mounir: Bye.

Jeff Hawkins: It goes long distances. That's a general rule.

and often, there are many cells of which predict a layer 1 in multiple parts of the cortex.

it'll send an accent up to this area, then it'll keep going, the white matter, it'll send an accent up to another area. as a general rule, this is where... this is where signals are sent long distances. That's the general rule. But I'm not prescribing this is the only place, or exactly, I think if it's a... what I like about this idea is it theoretically hangs together. It's almost like I can't see it working any other way.

In some sense, these functions have to be implemented someplace. And this is my best guess for how it's implemented. But if it's not like this, it's gonna be something else.

Viviane Clay: Can I maybe just summarize in my own words how I understand the key idea to make sure? We're on the same page.

Jeff Hawkins: Yeah.

Viviane Clay: yeah, from what I understand, there are two key ideas here. One, maybe the biggest one, is that for learning, state-to-state transitions We can get a widely broadcast signal of things that happened. It could be time past, it could be, a certain behavior has been recognized, it could be an object is recognized, it could be, an action has been executed. And we can... that... we can associate that thing that happened as context with a certain behavioral state or object state. And when that thing happens, we'd predict that state. Is that...

Jeff Hawkins: And if it's a behavioral state, it could be tied to a behavioral sequence.

Viviane Clay: yeah, I could kick off a sequence. Yeah, time conditions.

Jeff Hawkins: it'd be like, there's two sort of examples. Imagine I push a button, and the staple automatically opens, or maybe I have a dial which rotates, and every position of the dial associates with the position of the staple, that kind of thing.

Viviane Clay: Yeah.

Jeff Hawkins: but what you said is correct.

Viviane Clay: They inform, oh, you're in the first state of the stapler opening behavior now, because Button was pressed, and then... That behavior is a temporal sequence, purely, so that would just go through that... through time and make predictions.

Jeff Hawkins: it could start a sequence of behaviors. Or it could just make a single behavior change.

Viviane Clay: Yeah, and then the second one being that... we're just attending and inferring in a certain area of egocentric space, and even columns that don't get actual sensory input would still be attending to that area, and they might still get broadcast features from other columns, or broadcast state IDs from other columns, and can therefore Also learn, even though they're not getting sensory input.

Jeff Hawkins: But not all columns would be attending that... to that location, right? It's not like all columns are due this, it's Some columns will be attending to that space, but others wouldn't be. Even if, I'm just saying, take visual columns in V1 or V2. They can't... I don't think they can all attend to the same location in space. Can they? My assumption is that they have this sort of spatial array, and, they... they... they... physically, they can't get input from all... from all, I can't...

Viviane Clay: Yeah.

Jeff Hawkins: so my assumption is that I physically can't get the I can't get all my visual columns to attend to the same space and get input from that area, getting, they just can't get the light if they're not looking in the right direction. So I assume that was the same... the same situation while attending. that...

Viviane Clay: yeah, it could, maybe... They just wouldn't do anything, but theoretically, if they're not getting input, maybe they could all attend to that area.

Jeff Hawkins: You're right, they could.

Viviane Clay: And then, they wouldn't all be learning, because they wouldn't be all connected to whatever is getting that input.

not all visual columns would be connected to the column in your finger that's touching The mug.

Jeff Hawkins: I guess, in my mind, the definition of attention is You specify an area in egocentric space, And the columns... The columns that are actually Receiving, or could be receiving information from that space. If they weren't blocked. Would, they would be able to learn and vote. And now you're bringing up the idea that, Maybe all the comms could... could attend to that space and learn.

I don't think so.

Viviane Clay: But, yeah, I guess I was just wondering what would determine.

Jeff Hawkins: No, I'm pretty... I would say pretty certainly not. I can come up with examples why I don't think it's gonna work. but, okay, that's a... that's a detail, but let's for the moment say that The... some columns will be... would... would be receiving them for that space, so they could have... that's interesting. I'm imagining that...

Viviane Clay: I guess the reason I was thinking about it that way is because it would solve some of the issues around model sharing that we were talking about, that, if I learn something with my finger, I also know it with my other finger, or, I don't have to look at each object with my periphery as well to learn it. The peripheral columns can still learn about them, roughly.

Jeff Hawkins: it's interesting, I'm doing a little thought experiment right now. I'm imagining I'm looking at... A new object, visually. It's some odd shape I've never seen before. And I'm asking myself, could I learn to recognize that object by touch? I think probably I could.

if it wasn't too complicated, but I could. Then I'm saying, okay, what I'm learning, if I'm looking at it visually, and I'm attending the different features, saying, oh, it's got a bump over here, and a funny thing over here, it's like some weird shape. While I'm doing that, Am I imagining, my right index finger touching it?

Viviane Clay: Yeah, I was just thinking, actually, if we have learned the model in our visual column, in the, foveal vision column. We could, with this mechanism, we could recognize it with any part of our body just by... That part, broadcasting the features to the visual column that has the model.

the model wouldn't even need to exist in any of our tactile columns. We would just visualize it.

Jeff Hawkins: so then it gets a little complicated, because, obviously the sensors are not equivalent, I can't... I can't learn to differentiate Matte versus shiny finish, or for gloss finishes with touch. Or I can't learn color with touch. I can't, so if I say, oh, there's a red circle here. printed on the cup, the... the somatic system's gonna say, I don't know what a red circle is. I've never... we've never co-located and observed red circles together, because I don't get an input from red circles, it's I'm just... I'm just pointing out a fine... a little bit of finesse on this. Not everything can be shared. Because not everything can be observed in different senses.

So if the... if the differentiating feature of an object is it's... it's... if it's... if it's colors and it's, texture, it's finished, then I won't be able to learn that via touch.

Yeah, I see where you're getting. It may go back to my thought experiment. So I'm thinking... I'm looking at the object, I'm attending to different parts in the visually on the object, and so I'm like, oh, this... there's a bump here, and this here, and that here. And those features I'm observing are features that the somatic system knows. oh, I know what an edge feels like, I know what a curve feels like, I may even know what a handle feels like. as I'm observing these different parts, these are things that can be shared with a somatosensory system. The question is, could I be learning could I be... the somatosensory system is not getting any input. Could I be learning what models of this object are all my fingers at once? could I somehow imagine they're all attending to that space? Your argument is that the information is there.

And I agree with that. It doesn't feel like I do that, though, but maybe I don't... Anyway, I don't think... anyway.

Viviane Clay: Yeah, I guess I withdraw my suggestion that they could all be learning it. Now, actually, I think it would be much nicer just saying they don't all have to learn it, because when we're doing inference. they can just share this... the feature knowledge, and the column that knows it can infer it to.

I think that's actually a really powerful idea.

Yeah, that would solve some of these model shares.

Jeff Hawkins: And then, this gets, the example I often use, My walking in the dark. Between my bedroom and my bathroom. I learned that model visually.

I don't think I ever... Unlike a blind person, I never walked In the dark, learning the model practically. But when the dark occurs, My visual model predicts a visual feature at some point in my body space. And I can use any part of my body to go out and see if that feature is there. basically goes, oh yeah, there should be a vertical edge at this corner of the room here. I know what it looks like, I've seen it. But I can't look at it now, so send something... send someone over there to see if there's anything anybody could look at. I think that's what you're talking about, it's I can infer... I can infer the visual model of my room with tactical, just because... because I'm still using the visual model. I'm imagining seeing the edge there, and I say, then I should be able to touch the edge.

Viviane Clay: Yeah.

Jeff Hawkins: I should go to that space, and we all know that I should be feeling a vertical edge, so that's what I should be seeing, that's what should be there, and I can use any part of my sensory organs to figure that out. I could be a bat and using echolocation, saying, I should be... I should... Imagine there's an edge there.

Scott Knudstrup: I can imagine your model of the room Could be pretty good, visual only. But if you were to turn the lights off. And force yourself to learn it tactilely as well. Your model probably just gets better and better. So having a better and better world model of this object could be tantamount to collecting not just sharing visual information, but if you can collect a version that's tactile-only and visual-only, then you're triangulating a really high-resolution model of the subject and the world. that's equivalent to saying, oh, I can.

Jeff Hawkins: I'm holding a coffee cup, and I can feel its texture and its heat, and I can see its colors, and these are all combined. But remember, there's not one model, right? There are lots of models. and some models have color, some models have heat, some, texture. So it's more like you're not building one unified model, Scott, you're building... you're... you're enhancing the different models you have. And so you can... you can be better at, Mixing, matching modalities, or differentiating, things.

Scott Knudstrup: so I'm... Totally, yeah, it's like a distributed, Different views of the same... each... the somatosensory system, the visual system, each one is, a... Or auditory, they... You're almost getting different views. Which can be combined and collected. and sharpen, so I can... I can... There's probably a certain amount of fuzziness that you can allow for, if it's, the visual system. Trying to broadcast to the somatri sensory system. Probably can be somewhat inexact. We don't probably need...

Jeff Hawkins: all it is.

Scott Knudstrup: Fidelity on our location.

Jeff Hawkins: All it has to be is association in the voting neurons. That's it. There's no other knowledge. It just, I could associate a sound with... certain... behaviors, or I can associate a sound with certain physical objects, or I can... a sound could invoke a behavior, I... I don't know, it's It's a very general-purpose thing. You can... you can... you have all these models, and they can learn on their own, but they can also... you can... I don't know if Vivian said it nicely, you can, you can substitute a sensory system For the one that was learned. Anyway, this whole thing is just changing the way I think about the... when we started out this whole endeavor many years ago, I always said there's two things we have to learn. We have to learn what a cortical column does. And once we figure out what a quarter of a column does, then we have to learn how they work together. So we spend most of our time learning how what a co-worker column does, and we have pretty good theory about that. Pretty good understanding, and now we... we just... what I'm... what I feel like I'm doing now is we're learning more and more about, oh, how do they work together? It's more, it's not so simple, it's not just voting. It's oh, there's attentional areas. And then we're sharing this information, and there's this, and there's hierarchy, but I think we're adding lots of pieces to it now, right? we've got... we've got the voting, we've got the causal associations I've just added today, and we've got the compositional structure. Maybe there's more, but... We're really filling in a lot of the details about, how comms work together, and this whole idea of a tensional space As a sort of key foundation for both, behavior and learning is a big idea, in my mind. It's oh, I didn't think about that in the past.

Viviane Clay: Yeah, it's funny, I think, Scott, you just, on Monday's technical research meeting, I think you brought it up, but we were talking a bit about how, maybe we need to shift focus a bit more to the connectivity between columns instead of a single column being able to do everything, and maybe behaviors are just such a complex thing. not many mammals with columns can actually perform, tool use and things like that, so maybe it does require some kind of more sophisticated connectivity or additional... maybe it is not something that a single... every single column is actually able to do on its own.

Jeff Hawkins: That's where I started right today. I said, behavioral college can't do this on their own, right?

Viviane Clay: Yeah. And, yeah, I guess this kind of... idea of... learning causal associations, through widely broadcast signals. Maybe think a bit more about, okay, we have this general purpose algorithm, we just figured out how that general purpose algorithm fits both morphology models and behavior models, and it... the column doesn't even know what it needs to be. It's still the same algorithm, or it doesn't even know what it's modeling, it's the same thing. could we actually fit that onto some of our more sophisticated behaviors? maybe the motor cortex actually learns about Using tools or certain things, and learns that through causal associations with behavior models, instead of individual behavior comps, needing to learn that, and then maybe the kind of motor outputs that come from early sensory areas are really just about moving the sensor, and not about affecting any achieving any goals, or manipulating the world.

Jeff Hawkins: Yeah, I'm not sure I followed all that, but I think in this case, the layer 6 of the movement vectors... remember, I was proposing just recently that all columns are basically morphology columns driven by center. And so the... the location of Layer 6A is going to be identical everywhere. They're not... it's still going to be a location in space of an object. That's never gonna change. I'm moving away from the idea that the locations could be Something other than physical locations and space. I'm not sure if you were going in that direction or not, I didn't follow that completely. But again, every column... yeah, go ahead.

Viviane Clay: Oh, no, I wasn't going in that.

Jeff Hawkins: Okay.

Viviane Clay: It will still be locations. It would just represent actions at locations, maybe, instead of Morphological features or changes.

Jeff Hawkins: I think you were hitting at the beauty of this is that Colin doesn't even know what it's doing. It doesn't need to know what sense the organism is. It doesn't need to know if it's learning behaviors or morphology.

It doesn't... and, the key things are that multiple columns have to be... that are observing the same object. Have to vote. Ones that are observing different objects have to have the compositional projections, And... And then, behaviors or changes in the world have to be, causally associated in a time-order-dependent way. With other... other changes in the world.

But they don't know what those changes are, they don't know nothing, right? Nobody knows what any of this stuff means. It's just you can think of it that way. Looking at the same object, looking at compositional objects, two different objects, or two different behavioral objects, or even It could be even morphology objects, looking at it in time order dependent, That would be your behavioral... what this doesn't... it's interesting, this doesn't answer anything at all like how you do sophisticated behavior, like solving problems. It... it...

Viviane Clay: Yeah.

Jeff Hawkins: It gives a foundation for which to answer those questions.

Viviane Clay: Yeah, I feel like I tried to jump right to the producing the behaviors, but now I want to rethink what I came up with, given, first solving, okay, this solves, how do we learn? given an action or something happened, what state we will have next. And now, going back and rethinking, okay, now we have learned a model, like a causal model of the world, how do we now use it to cause change in the world? How do we use it to figure out which actions to take to get into a certain state that we want to go into, and how do we broadcast goals?

Jeff Hawkins: I don't answer... those are interesting questions. But the beauty here is that the actions needed to solve a particular problem can be implemented... anybody who is able to make that action occur. It doesn't have to be a particular part of the... the... the... The body or, the cortex, any, any... anybody who's... can make an action occur. can be used to solve a problem. we've separate out the... the embodiment? In some sense.

It's more about just, okay, I need to have this behavior, and then I have to create this behavior, and these locations. This behavior, and then this behavior, and then this behavior. And then we can ask ourselves, oh, how do I create that behavior? who's going to make it happen? Oh, try the switch, or, talk to Alexa. Something, I don't know.

Scott Knudstrup: I just thought of, a counterexample, that I had thought of quite a while ago, which was... It's when someone, draws a letter on your back. And you can know... you can imagine what the letter was. I remember this challenged me a while ago, because it's a different sensory patch with each... there's no... it's like the opposite of a finger dragging along something, right? Because you've got... each patch on your... of skin on your back is perceiving a different input, so you're not moving a sensor. So it's like the opposite end of the spectrum, but I think this broadcasting idea seems to solve that. Because all you really need to broadcast is a location in an egocentric space along with a feature. If your visual system can reconstruct what, say, the letter B, if someone draws the letter B on your back, if all it's receiving is a feature and a location in an egocentric space, then the visual system can reconstruct The letter that's being drawn on your skin. So without the need for a single sensor that's being dragged along.

Jeff Hawkins: I lost your audio there. I lost your audio there for a few seconds. Did anyone else lose it?

Viviane Clay: Your audio was gone, too. once again.

Hojae Lee: I don't know. No, they seem to be working. They haven't beeped at me yet. Okay. I saw your mouth move, I didn't hear anything, but I heard everything Scott said.

Jeff Hawkins: Scott, can I just... can I just rip on that example? I thought it was an interesting one.

Viviane Clay: Yeah.

Scott Knudstrup: Sure.

Jeff Hawkins: so what's going on there? As someone's moving, I don't think the skin on my back can recognize a line. when someone does that, I I visually imagine it's almost like a pencil moving it along in a direction, right? I can't see the whole stroke yet. All I'm seeing is the actual movement of their finger on my back. And it's almost like visual, right? Someone's drawing my back, I'm trying to... I visualize what it looks like. And...

Viviane Clay: If you missed what Scott said, I think it might be worth for Scott to repeat the potential solution, because I think it goes in...

Jeff Hawkins: Okay.

Viviane Clay: Does exactly that.

Jeff Hawkins: I'm sorry.

Viviane Clay: Maybe, Scott, if you can...

Scott Knudstrup: Sure, yeah, I think... I think we're probably saying the same thing, which is,

Viviane Clay: Yeah.

Scott Knudstrup: If it's a sequence of... Features an egocentric space being broadcast out of your somatosensory system. And you're just... if the visual system is receiving them, it can basically reconstruct What it would be seeing from this collection of features and locations in ecocentric space.

Jeff Hawkins: And I'm just saying, this broadcast...

Scott Knudstrup: And sharing solutions seems like a really nice solution to this problem.

Ramy Mounir: The only...

Jeff Hawkins: The only... that's good, alright. The only twist I might put on that is that I think what's being broadcast is not a morphological feature, it's a... It's your behavioral state, ID.

A line moving up. type of thing.

cause you, unless... Because that's what's happening, right? You're either... but other than that, I think exactly right, right? It's,

Scott Knudstrup: So in a way, it also... and the middle ground, so if there's a sensor moving, a single sensor patch moving around. That's what we've... primarily been working with. And there's... on this other end, many sensors receiving a little bit of information, so that's someone drawing on your back, so each part of your back is a different patch. Maybe something like flashing furances in the middle. Where... You've got a bunch of features, or a bunch of sensory patches receiving a bunch of information at once.

Jeff Hawkins: I'd be... I bet you...

Scott Knudstrup: Yeah.

No, I don't know, I'm just thinking that maybe there's...

Jeff Hawkins: your skin is actually lots of different types of sensors, right? And, I don't know, there's half a dozen of them. And some are responsive to movement. And some are responsive to pressure. And so the mix of these things changes at different points in your body. on your back, I imagine, I'm just imagining. That the... the most important thing on your back is to detect movement. Something like, something's touching you, or something's changed back there. There's a bug walking on you, or... it's because we don't really use our backs to infer morphology very much, it's just like in the retina. In the retina, the parvicellular cells are focused on the fovea, and then when you get to the outside, it's mostly magnicellular cells. Same thing would be occurring on the back. The equivalent of your back would be mostly magneto cells, with low resolution, just like in the fovea. So your back is like the outside of the retina, the outside of the retina, and your fingertips are like the fovea. I'm just... just riffing on the same idea here. But... but you may not even be able to... I was... I was trying to imagine, what if someone actually could touch your back with the letter A all in one place, right? You could just touch it. I don't... after they touch you, I think it goes away. You're I'm leaning against this chair behind me, but I don't feel the chair. Because it's only really detecting changes. I'm not constantly feeling like, oh, what's that pattern on my back? It's no, it's more oh, I move and it's changing. I think your back may be restricted almost completely to behavioral, features.

Viviane Clay: I've been... I was curious... M2 flash inference?

Jeff Hawkins: What's that?

Viviane Clay: Your back can't do flash inference?

Jeff Hawkins: I would bet no.

Scott Knudstrup: But I've always been curious about... I don't know any blind people to talk to, maybe someone on YouTube can weigh in the comments, or you guys, but, reading braille. Like, how much can someone lay down their finger on a braille letter or word without movement, and be able to... Know what that word is, or do they have to drag it a little bit,

Jeff Hawkins: I don't know, I do know.

Hojae Lee: The answer is in Principles of neuroscience.

Scott Knudstrup: Is it? Oh, it's still propping up my monitor,

Jeff Hawkins: What's the answer? Do you have to.

Hojae Lee: Yeah, fingers. so if the braille spacings are less than, I think 1 millimeter, so I think our finger has gratings, if it's less than that, then it can't distinguish two dots, from one, first of all. yeah, so there's a little bit of a scale issue there, so you can't print the braille two spoils. And the other is that the sensitivity, of, your fingertip is highest, but if you go down, your finger, it's much less sensitive, so that's another thing.

Jeff Hawkins: the fingertip is the area of highest acuity, right?

Hojae Lee: yes, and also lips, so you can do flash imprints with your lips if you want to. That might be why babies put stuff in their mouth, I don't know.

Jeff Hawkins: I'm not a good switch to flash inference, it's just it's higher acuity, so you can, But the interesting question here is. is... when people are reading with Braille, are they moving their fingers over the... I think the answer is yes. They're moving their fingers over the dots, not... they don't press their finger down, then push their finger down, and push their finger down. They move, they slide it over. And, I'm pretty certain of that. And, And the question is, I've... I tried to do this once. I tried to... because I did... I did a project with blind people. we worked on it for about 9 months, and, we're trying to do sensory substitution device. And what I did... what I learned is, if I... if I just put my finger on a... on a braille character. I couldn't recognize one from the next. This is impossible. I just couldn't do it. Now, the question is, if I practice it over and over again, could I do it? Or is it that I really need to also practice moving my finger? That's an interesting question. I don't know the answer to that one. But I do think... I think they get much, much... they... if you... when you first start doing it, you're not very good at all, and you're... and then with practice, you get better at it.

Hojae Lee: Yeah, but, yeah, if you're curious, about the smaller sensory system, Chapter 18 is about reflectors of the smaller sensory system, about... goes into, the part that, you mentioned about, if somebody were to write a letter A, that's But we're... none of our sensors are moving, it's related to... it's at, exterior reception. So there's the three functions of... it says, the three functions of the somatosensory system is proprioception, exteroception, and interoception. Interoception is, Measuring what's happening in your body, organ, I didn't really focus on that part. But, they can definitely be extra reception without proprioception when somebody else touches you, you probably know where your body is, but, you're still getting sensation from the outside world, and I think that's still possible to, go to your brain and build a model, which I think could be why, our visual system could recognize... or not visual, but, like, why we could recognize, an A if somebody wrote that on their back.

Yeah, and then, about...

Jeff Hawkins: I know that... Go ahead.

Hojae Lee: Yeah, about touch being only recognizing changes, I didn't read this in detail, but, there's some mechanoreceptors... I guess it depends on, the, how the mechanoreceptors in your skin works. If it's only, for example. detecting vibrations, or changes in pressures, and yeah, that natural.

Jeff Hawkins: No, I know that there are definitely ones that are not... there are definitely ones that are, pressure sensitive. I guess the question is are they represented equally, elsewhere in the body?

Hojae Lee: Yeah.

Jeff Hawkins: You can do, another thought... Another experiment would be, like... Okay, someone's not moving their finger on your back, but they're touching a series of dots.

I would detect that, there must be those pressure sensors, obviously they're back there. it's interesting, then you would visualize that row of dots and try to imagine what it looked like, right? It'd be you'd try to imagine in some sort of visual space, but... That row of dot... It said he couldn't. Imagine I watched you write a letter on a piece of paper. But your pen didn't have any ink. can try to imagine Someone drawing on a piece of paper, but there's no ink in the pen. And this is like riding on your back. you have... you can't see the line, you just see where the tip is, and so you'd have to... it'd be difficult, right? You'd have to follow it very carefully.

and imagine the line that would have been drawn if it did get drawn. I'm just saying that's the equivalent of drawing on your back. Yay.

Viviane Clay: Yeah,

Jeff Hawkins: It's not easy to do, because you have to continually attend to it.

Viviane Clay: Yeah, it sounds like that's actually the main reason why we can't do, if you press the letter K on the entire back, you can't do it, because... Maybe that sharing mechanism only works sequentially attending to different locations. you can do dots in sequence, and in sequence, attend to these different locations also with your visual cortex and visualize it, but you can't share all of these locations at once.

Jeff Hawkins: The visual cortex. Yeah, this theory... by the way, just go back to the theory we're talking about here. It says that you attend to an area And you infer what's in that area. But if you can't infer what's in that area, you have to go smaller attention areas. You have to narrow it down until something's inferred. in the case here.

Your back may only know, movement and pressure at points. It doesn't know... it hasn't learned anything else. when you tend to that error, that's the highest thing it could... it could send to you.

It's if I was reading Braille, and if I don't know braille, I have to attach almost each dot separately as I go around to, oh, there's a dot here, there's a dot here, there's a dot here, there's a dot... But only after you learn the letter, then you can do, voting, and you can recognize it all at once. And then you say, oh, there's a letter A here. So this all fits with this. The idea is that you have to... you have to narrow down to there's a common recognize that the thing you're attending to, the area you're attending to, there's somebody recognizing something there, and in terms of your back, the best you can do is a dot or movement. There's nothing else that the back knows how to recognize.

Ramy Mounir: It's interesting, I'm thinking more now about learning, not inference, and I'm wondering if someone draws, some weird shape. where would this model be stored? It's not being drawn on a specific column, Is it another column that's observing all of them at the same time?

Jeff Hawkins: so here's what I think is going on in a big picture. Imagine you're at... The hippocampus, and the hippocampus is attending to some area. And saying, what's there? And then it tends to some other area, and what's there? What comes back could be a very low-level feature, or it could be a high-level feature, depends on who... if someone's able to recognize it.

At that point. You're broadcasting to everybody, everybody's getting... everybody who could be attending to that area in physical space. is... is getting... here's a feature at this... here's a feature that you know at this particular location. Here's a feature that you know at this location in space.

The learning would occur at the hippocampus, and it would occur to anybody below there who could actually... who could be... Observing that location in space, and would know what that feature is. So it could be learning a lot of places all at once.

Viviane Clay: But yeah, I think that's a... it's a really... it's a really nice, new, powerful idea that solves a lot of our previous problems.

Hojae Lee: Yeah. Both for learning and inference.

Scott Knudstrup: One thing I'm a little confused by? Or... not thinking through properly. Is how every column is having access to egocentric location.

And not... Not getting... It feels untransformed by, an object reference frame.

Jeff Hawkins: so if you look at my questions on the... Excalibur. On the right here, I have two questions, and the first is, how's attended area broadcast?

And I think that's the question you're asking, in some sense.

Scott Knudstrup: Yeah.

Jeff Hawkins: mechanistically, I don't know, but theoretically, it's pretty straightforward. There has to be a common egocentric reference frame, or a representation of space. We saw that, by the way, in the superior clicus. It, on its surface, mapped a region of space around the body.

And then, A column has to be able to take a location it has in an allocentric space. and say what it is in the egocentric space, and then similarly, you have to say, given an egocentric location, what is... what... is that... is that where... is this column in that region? You know what I'm saying? Is it... is it in there? So you just... the egocentric space becomes the... The common language between all columns. And how that exactly works, I don't know, we've talked about things like, All over those weird parts of the cortex that are in between, Oh, gosh, I'm losing my brain.

Scott Knudstrup: cleaner.

Jeff Hawkins: With,

Hojae Lee: describe the function.

Jeff Hawkins: we don't know the function. It's lots of parts of the cortex broadcast to it, their physical structures are that are, like, below... they're in the white matter, almost like a... They're not a cortex, but there are a lot of cortex predictions. Yeah, the classroom. I think that was one of them. Anyway, there's... there's somebody who has to implement this physical space. It seems like... I don't know, I don't know how that's done.

Viviane Clay: it's...

Jeff Hawkins: It just...

Viviane Clay: Yeah, but... and it seems That location, egocentric space, still needs to be transformed into object-centric space. In the receiving column, right? If the visual columnist trying to infer something from based on how the touch sensor is moving. You still want to transform it into the object it's recognizing. It's reference frame.

Jeff Hawkins: I think... we've talked about this before, I think the way that the brain might do this is not transfer locations, but it just has to transfer movement vectors. And therefore, it's a much simpler transformation, and so the columns have to infer where they are based on movement. No one tells them where they are. And so it... the transformation is oh, we can't really share locations. But we can... it's much easier to share directions of movements. And translate those. And and everybody has to infer the correct location based on that. Monty today doesn't do that, right? Monty does location transforms, right?

Viviane Clay: would we even need to take a location or movement representation in the column that's getting sensory input? Couldn't we just look at... Whatever place we represent the attention in, which might actually be in the thalamus, and see which area of space is being attended to, and broadcast that location to the column.

Jeff Hawkins: I didn't follow that. Sounded good, but I didn't follow it.

Viviane Clay: So I feel like we don't need to send a location from the touch column to the vision column. We just need to send... A location from the attention map to the vision column.

Jeff Hawkins: no column talks directly to another column. it all goes egocentric, but how is... how is that done in neuroscience? I... I don't know. I don't... I don't have, oh, here's the part of the brain that's doing that.

Viviane Clay: Yeah, but yeah, there wouldn't need to be a lot of, column, too egocentric, too object-centric transformations that need to happen, because... It would be coming from outside the neocortex into the column that's not receiving sensory input. Directly.

Jeff Hawkins: But it would still have to go through the egocentric space, right?

Viviane Clay: Yeah, so it would already be in the egocentric space, right? the attention map would be in egocentric space?

Jeff Hawkins: The intention map is an egocentric space.

just... we can riff on that a little bit. imagine I was out there looking at, the intersection. And then something starts to move. everything is static, and something starts to move, so I immediately tend to the thing that's moving. What does that mean? I would attend There's a bunch of columns now that are... That are detecting change. they're like, just, changing features. And... the area prescribed by those changing features is the area I want to tend to.

it's bounded by... The changing morphology features.

That's... that's... so that's... that's one way of, so it's not necessarily, what does it mean to attend to an area? I have a bunch of columns, they know where they are. those columns may be know where they are in space, in some... in a reference frame that, maybe it's a hippocamp, I don't know, but... and that becomes the area that's broadcast. It's like saying, okay.

these... these... this is the boundaries of... of where... I don't know how that works, but it's not like some morph... it's not some blob of sphere in space. It's... it's defined by the edges of the thing that's moving. That's the part you want to attend to, and if things are inside of that, you want to know what's going on. Actually, it's just... those are the features you have to determine. I'm thinking out loud right now, it's interesting.

Also, imagine the world isn't changing. This is something that you guys have been working on, Rami, I think, in particular. Imagine the world is not changing, but there's a bunch of objects out there. What do we attend to? It's easiest if we can find a contiguous border around something.

Then we could say, oh, there's a... I don't know what this object is, but there's a contiguous border on it. That's the area we need to attend to. If there's a bunch of overlapping things that are not... that are... that are not recognized, then it becomes really hard to know what to attend to. And then you'd... then you'd have to zoom down smaller and smaller. Until you recognize something. I'm just mentally thinking through the mechanism here. I think it works pretty well, actually. Anyway, it's an interesting question what Monty should do. Monique, again, could take on what's... is already taking a shortcut, in some sense, by just working in locations. And, using, Cartesian coordinates, which might be just fine.

Viviane Clay: yeah, I feel like those were two big ideas today. I just want to go away and think more about, like, how they... what impact they have. the other open questions. That we have. I feel like we might be able to untangle some other things.

Jeff Hawkins: What would be the... what would be the next big question you want to think about in terms of this?

Viviane Clay: I guess, in terms of actions, the next big question would be how do we use these causal associations, or these models of causality to figure out actions, to output, to go from one state to another?

Jeff Hawkins: Okay.

Viviane Clay: I know if I... if this action input comes in, my stapler states from state... changes from state A to state B. I know that now, but now I have the goal to close the stapler.

Jeff Hawkins: Alright, so this is my second question. I had on the right there, how does reverse causality work?

Viviane Clay: I want the light on.

Jeff Hawkins: How do I know I have to flip the switch?

Viviane Clay: Yeah.

Jeff Hawkins: Machine learning tell us anything about this? is this, part of reinforcement learning, or has this topic been... It seems like something that people would have thought about.

Viviane Clay: Yeah, definitely.

Yeah, I have to...

Jeff Hawkins: Alright. I think I don't. and that was...

Scott Knudstrup: I think with the... the light on.

Jeff Hawkins: Switch flip? Yeah?

Scott Knudstrup: It's almost The switch in the up position is associated with the light on, and the switch in the off position is associated with light off, right?

They're just pairwise associations. It doesn't even really seem like time is an important factor here.

Jeff Hawkins: what if I... what if the switch is just a button? And it's a momentary button. I push the button, there's no state of the switch.

Scott Knudstrup: True.

Jeff Hawkins: So I've... the button turns the light on. I've learned that. Now I say, oh, I want to turn the light on. those things I've labeled causal association, time order dependent, the projections of layer 1, They just go one way.

Viviane Clay: Yeah, I think... Yeah. So I think... I think what people do in machine learning often is you learn two functions, a forward model and a backward model. One is to, given two states, you output which action. transitions you from the... between those two states. And the other function is the forward model, which is given a state and an action. You predict the next state. And... The forward model is basically what you just proposed here. We have a current state and an action, or whatever other input, and we predict the next state. And what we would need is the inverse model, which is we have a current state and a goal state, and we predict the action in between. But as far as I know, I'm not sure they are ever, one function. There are, like, usually two functions that are being learned. from the same data, but they're still two functions, so it might still require a second mechanism, like layer 5 neurons learning, given current state and goal state, output this action. That's a bit like what I proposed on Friday.

Jeff Hawkins: Sorry, I never said listen to that again.

just briefly, because I'm going to work on this problem. briefly, on Friday, you were saying the apical dendrites could represent, the desired state.

Viviane Clay: Yep. And then the... closer to the cell body, there we would have the current state, and then if desired state... if we have a certain current state, and then a desired state comes in at the apical dendrites, that would cause a layer 5 neuron to burst fire and output an action.

Jeff Hawkins: Alright, I think that's a good problem.

To think about.

Scott Knudstrup: Do we still have this issue, though, where we're asking the cortex to possibly learn associations a little too quickly? Because there was that issue of, let's say we have a dial controlling the stapler. Or a button controlling a stapler. You can learn that association, instantly.

Jeff Hawkins: I'm... remember, every... all learning starts in the hippocampus. This is my new... my new mantra.

The hippocampus will learn these things rapidly, instantly. They only... but it takes practice For, as you repeat these things for these more sophisticated morphological models, they're to be learned lower down. we, imagine all this stuff is happening in the hippocampus first, and all the rest of the learning is basically just Supporting that, in some sense.

So I don't think that's a problem right now. the details.

Scott Knudstrup: Okay.

Jeff Hawkins: Or it needs to be thought about more, but...

Scott Knudstrup: I think it might have implications for what the action being sent out is of a column. Because, as we talked about, the potential range of actions that could close the stapler could be enormous. Do we want to learn them all pairwise in a column, or,

Jeff Hawkins: No, it just...

Scott Knudstrup: I'm just thinking, may... There's... maybe there's just some mediator step, like...

Jeff Hawkins: No, you don't either.

Scott Knudstrup: Whatever, or...

Jeff Hawkins: You don't need it. It's just basically... it's anything that... an action that's followed by another action can be learned. So as long as you're broadcasting it. nobody... the only thing that... it's... you could... you could learn any... if I have 150,000 columns, and they're all broadcasting their layers 2 and Layer 3, then any correlation between them can be learned. So there's no... you don't need an arbitrary, it's the...

Scott Knudstrup: I was thinking of the hippocampus as the mediator, because of its short term... because of its ability to create very rapid associations, which could eventually be migrated to the hippocamp... or to cortex, I don't know how.

Jeff Hawkins: I think I know how. it's not immediate, just think all learning starts in the hippocampus. It's everything. Morphology models, everything starts... it all requires attending to some space. And then, learning these connections, And... and then, through practice, we can talk about how it gets relearn down in the cortex, but we've touched on that already some here, you can learn one modality and learn another modality. I don't think the... I don't think the speed of learning is a problem here.

I just think we need a mechanism that says, oh, how does this reverse causality work? how...

Viviane Clay: The one thing I was... One thing I was thinking today, and I have to think through this a bit more. is whether another kind of type of model could be learned in, for example, the motor cortex, which is representing actions at locations, and there we could learn, general models of more complex actions, pincer grasp, and you would learn, a pincer grasp with your fingers, but then you might learn that same thing with chopsticks. You can effect the same change with chopsticks, or you can effect the same change with thongs, tongs, in the kitchen, this kind of thing, too. there are several ways you can pinch something and to pick it up, and those could all be associated with the same type of action output of a column that wants to transition from state A to state B that Yep.

Jeff Hawkins: But why do you... why does it have to be different in the motor cortex? I can imagine things only being learned in the motor cortex, but... but does it require a different mechanism there?

Viviane Clay: No, the columns work exactly the same. I was just thinking maybe that model's kind of... some more... higher order action sequences, or something like that.

Jeff Hawkins: Yeah, I think this attentional window thing solves all these problems. Eventually, in some sense, whether I want an action or I'm observing something in an attention window, if someone can handle the thing I want, they're going to give me back the most sophisticated answer they can.

but if I can't, then I have to tend to smaller pieces. maybe if I want to grasp something, the, the... my fingers, the models of my fingers can do that very rapidly. No problem at all, but if I can't use my fingers, I have... then I have to attend to it very carefully. I have to say, oh, okay, pick up a chopstick in my left hand, pick up a chopstick in my right hand, then move them together. It's a much more, it... I'm taking advantage of whatever behaviors I do have available to me. Or I could learn to pick something up by attending these things from visual spaces, a person who's paralyzed could, I think the... The sophistication of the body behaviors from the cortex point of view is that, you could learn complex things in one part of the cortex, but then you have to break them down into pieces that are already known in other parts of the cortex. I don't know how to describe that better, but... I think... Yeah, I don't have to... But maybe the other part is there's parts of this that are done subcortically, like we saw at the hip... with the superior colliculus, and so how much of, stuff is subcortical? walking, I think, is almost all subcortical. The cortex doesn't really know how to do that.

you don't even know how you're balanced. There's no cortex balancing.

Viviane Clay: Yeah.

Jeff Hawkins: Standing upright.

Viviane Clay: Yeah, maybe it's not a kind of different type of model or anything, I was thinking, lots of behaviors might require you to, pinch something or to, to pick up, or if you want to squeeze an object, or squeeze a button, a lot of that requires this, so there must be some kind of more general model of that specific kind of pinching behavior. That you can then learn in the behavior model. To associate with that. With a bunch of different state transitions that all requires basic behavior.

Jeff Hawkins: Where the auditory output can't pinch. But there's... but there's.

Viviane Clay: Yeah, or yeah, maybe the pinching grasp is also subcortically learned, and it's just associated with an action output from.

Jeff Hawkins: that's why I brought it up, but I think in general, I think different parts of the cortex will have different abilities. Both for inference and for motor output. It depends what's learned, and if you... if you require a part of the cortex to do something that it hasn't learned as well, then it takes finer attentional detail and more time. just like you can... you can recognize a letter on your back. that's... maybe I won't use that one, but, yeah, if you're trying to... you're trying to turn the light switch on with your elbow, that is going to take more attention, because you haven't learned those behaviors. But if I... if I'm holding a switch in my hand, and... and I want to turn it, my hand knows how to do that, type of thing. Hand columns on how to do that. Anyway, I think... I think this system accommodates a whole variety of abilities. across modalities, And in some modalities, things will be better, in some modalities, you'll take more attention and time. To achieve the same result.

I think... I think thinking about reverse causality is a... It's an interesting one.

Viviane Clay: Yeah, another thing I want to think a bit more about is how these ideas that we, discussed a lot in the past weeks around the hippocampus especially, plus also attention. could apply to Monty, and how we could incorporate those there.

Jeff Hawkins: Yeah, I think, mind you'll have to have the equivalent to the attentional space.

Viviane Clay: Yeah.

Jeff Hawkins: It has to do that.

Viviane Clay: and yeah, right now, Monty is basically the hippocampus, so it learns everything fast, but right.

Jeff Hawkins: I think that's fine, too Again, in my mind, the only reason that the rest of the brain doesn't learn fast is that it just... it takes too much neural machinery to learn fast. Too much energy and too much,

Viviane Clay: Yeah, and I guess it can have advantages for things lower in the hierarchy to learn slower, because if. If the low-up levels change their representation, everything above has to relearn how to interpret its input, yeah, once we have, more deeper hierarchy, and Monty, it might.

Jeff Hawkins: Boom.

Viviane Clay: necessary to slow down learning at the lower levels?

Jeff Hawkins: if you think about some future implementation of our work in some sort of embodied system or robot or something like that, you could just swap in and out different models willy-nilly, and all of a sudden, the same The same embodiment can become an expert piano player, or expert carpenter, or, I don't know, whatever, right? These are just models, you can swap them in and out.

oh, that just made me think of that.

With money, we can do everything. We can just learn fast, we can just swap out the whole thing, put a new upgrade to the system.