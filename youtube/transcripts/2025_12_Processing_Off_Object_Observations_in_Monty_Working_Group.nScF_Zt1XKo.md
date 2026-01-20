Jason Carver: So yeah, so luckily, I do have some familiarity with, particle filters. I haven't, implemented it in 20 years, but I did implement it once. It was one of my, actually, a paper I really liked, the Thrun paper from 2001 that MixedRMCL was, like... I was really pleased to just see it by chance in the... in the Thousand Brains. Project paper. But it was... it was a fun connection. Yeah, there's always the details of, like, how do you actually use the sensor data to update the observation? And I think one place that I was getting stuck was trying to apply the sensor data to all the observations, or to all the hypotheses at once. I think that's what I was... I was trying to do it, in one fell swoop. Rather than it's oh, yeah, if you're just looking at one hypothesis at a time, it's almost trivial to update that hypothesis with the off objects, yeah, observation.

Niels Leadholm: Yeah, so I guess it's Yeah, basically, they'll all be integrating movement, and They'll all think they're, somewhere in that object's reference frame. And then they're just going to get that sensor data. So if a hypothesis is being updated, it's going to get the sensory data Which may or may not match what was learned at nearby points. And so once a, a hypothesis moves through space. In this kind of reference frame, and then it's receiving sensory data, and it's basically gonna look at its kind of learned neighbors To see, does anyone match what I'm getting? But if the... if it's nowhere near anyone, then that's this out-of-model situation, where it's like the point has moved, super far away. And then if it's the... more, strictly just off-object, that, implies that, okay, it's moved, there's some learned points nearby. But it's getting this observation that's, saying, oh, I'm sensing nothing. And that's where we want this high prediction error. But I guess what... in some ways it's good, in some ways maybe you could say it's, computationally expensive, but, As long as the hypothesis is considered, Good enough to continue updating. We're gonna move it with, the incoming kind of movement data. And then, yeah, pass that sensory information. So we... we don't need to work out, what is the correspondence between The hypotheses that are being updated, and something like, a ray of... Of, vision or anything like that, if, that helps. So it's... Yeah.

Jason Carver: Yeah, I think... I think, When you move... so when you move the sensor on the... on a single hypothesized... a single model.

Niels Leadholm: Yeah.

Jason Carver: And let's talk about distance sensors, because I think a touch sensor is, even more trivial, right? a distance sensor, you move it, and... and... obviously, the depth of the model is different in different places, moving the eye, right? That's the process where I was like, oh, you have to find where the, like, where it lands on the model. Yes, you're right. that I had in my head of the rays deciding where the sensor is landing on the model.

Niels Leadholm: right now is we have the depth information, which, together with the location of the sensor, we have the location that's being sensed.

Jason Carver: I'm talking about just in the model.

Niels Leadholm: Without recognizing the model, we have a location, a new location, and then we have the previous location, and then that's that displacement in the world space.

Viviane Clay: yeah, basically the whole taking account dev already happens in the sensor module. we're actually already in the transform before it gets to the sensor module. So I... actually, I think maybe it's useful if we use a, just a whiteboard for some of the.

Niels Leadholm: Sounds good, yeah.

Viviane Clay: Do you mind if I make this offer object out of model one,

Niels Leadholm: No, yeah, please.

Viviane Clay: Okay.

Okay, I'll just post this link in the Zoom channel.

Jason Carver: Okay, so you're not... you're not predicting where the sensor would land on the model, you're looking at where the sensor actually landed, and then figuring out... Yeah.

Niels Leadholm: between those two points, okay. Yeah, so it assumes that there is depth information. And then, of course, it... it benefits from, at the moment, that... all the kind of path integration. So that's both, accounting for how much the move... the sensor moved, and also what is the new depth estimate. obviously the more noiseless that is, the better. But, basically, that's gonna just give us a new location. And then... that we're sensing at. that's basically... that's, the location of the feature that's being sensed. And but in that sense, it's not that different, from the finger. Because it's whether we're physically touching it, or we're seeing it a distance. the kind of location of the feature is... is out there in the world. It's It's not, I don't know. in the retina space, or something like that. it's And then that means... oh, yeah. I was just gonna say, and then, yeah, so if we have an old observation like that, and then a new one, then we can do that, calculate that kind of displacement in world space. Or it could be, egocentric space relative to the robot or something. But anyways, we have that kind of displacement, and then... The learning module has a hypothesis about the orientation of the object. And then it can use that to transform That displacement, based on different hypotheses. And so different hypotheses are going to move in different ways on the object, based on different hypotheses about how the object's actually oriented.

Jason Carver: Okay. Can I... this... this is a question to make sure I'm understanding what you're saying.

Niels Leadholm: Yeah.

Jason Carver: Which is... if I... if I have a model of these glasses... Yeah. and I move my eye... my distance sensor to the... To the... the side here.

Niels Leadholm: Yeah.

Jason Carver: And let's say there are two different models, one with only one of these, and one with both.

I... I look at... I look at the glasses at the side here, and one of them is... is missing, or is folded, or whatever. And so my distance sensor lands on the further of the two.

Niels Leadholm: Yeah.

Jason Carver: So... that is what gets sent in to the hypotheses, and that's actually going to end up matching both models, the one with and without The... the hook that's on... that's closer to me.

Even though my mental model of the glasses would tell me that the one with the hook closer to me should actually...

Niels Leadholm: There should be, like, a.

Jason Carver: There's something scary, your vision yeah. Yeah. So... we're... so the fact that we're using where the sensor actually lands, and then just moving to there in the model ignores the fact that there's an obscuring feature in front of it in the other model.

Niels Leadholm: Yeah.

Jason Carver: Okay, but that's how it works right now, and that's... that's fine, I just want to make sure I understand how.

Niels Leadholm: No, that is a good, it's a good example to yeah, exactly. yeah, there's no... yeah, basically there's no way of accounting for this kind of ray of vision and... that's come up, I don't think we've really discussed it in this kind of exact, setting like you described, but it's come up in terms of, Say you want to test a point now, you may have seen we have, a policy that kind of suggest, oh, I should move to the handle, things like that. But we've thought, okay, depending on where we are on the object, you would have to move in different ways in order to actually see it. sometimes there might be some self-occlusion, and sometimes there might not be. And where is that kind of knowledge stored that, okay, and, yeah... It could be maybe anything from more like a scene-level representation that's accounting for both models over... about your sensors, maybe you have, models of how your eyes work, and how they, sense and understand this kind of concept of self-occlusion, or, Yeah, things like that, but... Because I guess we don't want to wrap up It might be too much to try and wrap that up into kind of a single learning module, but it that, for some reason, that, a distant learning module has this, sense of, if I view from certain directions, it'll be obscured. But anyway, so we... we don't have, I guess this is the short answer, a way of dealing with that, but, yeah.

Viviane Clay: the main thing is that the cortical messaging protocol, so whatever learning module expects, is basically just a 3D location and orientation in space of where the sensor is sensing And it doesn't expect where the agent is that the sensor is attached to, but it expects the location of where the sensor is sensing. for example, I think in monkeys, there are these, what's it called, spatial view cells? They basically fire whenever the monkey looks at a specific location in the room, and it doesn't matter from where the monkey is in the room, or, like, where the eyes are in the sockets or anything, it just matters where in the room, what location in the room the monkey's looking at. And that's what we expect as the input for the learning modules. try to make a very brief diagram of what kind of info is available at what point. So basically, we have the environment where we have the entire object, and then we have the sensor, so a little camera patch, for example, that sees a small part of the environment. And in most of our experiments, we basically get an RGBD camera image. And a location of the... of the sensor.

So that's, the sensor location is, It's actually the thing of, The camera that's up here and looking at... At this location. So that would be the location of this here, plus the RGBD image. And then we apply a transform, and the plan is to eventually wrap this transform into the sensor module, actually, but this is how it looks right now. But, so basically the transform takes this, depth image and the sensor's location and uses... combines the two to basically calculate an array of 3D locations, basically saying where in space is each pixel? So basically adding the depth values together with the sensor location. So then we have, an array of each pixel where it is, basically hitting the object in space, and that gets sent to the sensor module, and then the sensor module turns it into a critical messaging protocol, which is... it basically takes the location that's stored at the center pixel of the patch. And then it uses the rest of the pixel locations to calculate the surface normal and curvature directions, to define the kind of orientation in space. And then it takes, the color at the center pixel, too, and some features.

Niels Leadholm: and so to maybe rephrase what you were saying earlier, Vivian, and relevant to the glasses example, is If the learning module is sensing this mug. and it senses this inside, wall. It doesn't know if it's up here, and that's why it's sensing it. or that it's here, and there's, a hole in it, and that's why it's sensing it. it just knows, okay, I'm... I'm getting, something at this location, And... yeah.

And at least I think our intuition right now is... is that would almost be, like, another learning module's, job, is to learn This idea of, occlusion and what that means for particular sensors, but... Yeah, I think it's an interesting question, though.

Jason Carver: Yeah, I guess it's similar to having a different object occlude yours and keeping in your mind that there is another object behind it, like... yeah.

Viviane Clay: Yeah, it's it's not something we would represent in the input level. But at the, you might have a higher-level learning module that has, a scene representation of where... that there is something behind it. Because it has seen it previously at that location. And then, yeah, like Nios mentioned, maybe at the output level, when you calculate an action. You might use that kind of scene model to calculate that you need to go around, or something like that.

But at the input level, it doesn't really matter.

Jason Carver: Yeah, I guess it could even help build intuition about, like, where the hierarchy should break down. if something can include another thing, then maybe it should actually be different sub-objects that are built together. I don't... I shouldn't do too much speculation, because I have no idea what I'm talking about. Oh, okay, and there was one kind of maybe tangent, I couldn't find... I think it was, Niels, that you said something about... This problem is solved already in a multi-object scene, if you go on to a.

Niels Leadholm: Yes.

Jason Carver: subject and come back. I didn't... I guess the first... my first thought in response to that is... can't... if we just treat off object as a... as, a distant wall or something, which I think you've also brought up. Does that mean everything's already solved if we just actually... if we just feed in a different wall with, say, a surface normal pointing at us, and... does that mean this is already solved and we don't have to do anything special here? I guess that's always a question to ask at the beginning, is are we doing a special case for something that doesn't need a special case?

Niels Leadholm: Yeah, I guess it's... it's just for example, with the surface agent, then... It may be relatively close to the object, and it's sensing nothing. So it's not always... because it... part of that kind of already working relies on the fact that it's, it's really far away. And... But then I guess the other thing is just, yeah, it fits with the feeling that, okay, yeah, there are no morphological features. Like, when I look at, at least I don't get a sense of a surface when I look at the sky, maybe? Maybe there's something, or in a kind of black well. But, and certainly when my finger's just, covering in space, I don't have a sense that there's, a surface there. But I think it points to that, at a certain level, the change is relatively small. That, We just need this kind of special, oh, it's none for morphological features. And then a lot of the kind of stuff that's already there in terms of, feature matching and updating the location and stuff like that, yeah, updating the location, it's oh, okay. I sense nothing at a distance, now my sensor has moved super far, okay, now I'm way out of reference frame. Right now, that's gonna get negative, evidence, and things like that.

I think we do still need to change it, but I think it, yeah, it points to that. It's... At that level, it's not that big a change. It's more just that it has all these kind of knock-on effects, Yeah.

Jason Carver: Okay, yeah. Huh.

Niels Leadholm: Yeah. But no, yeah, these are, yeah, great questions. I think you definitely, yeah, understood the... the problem well, Oh.

Jason Carver: There was, there were maybe some slight differences... I guess I wanted to go... Over the, the high-level plan... This is almost more of, a process project engineering... view of it, of, what are the steps that we do, and Vivian did that first summary of, sending the observations to the learning module, even when you're off-object, and then... step two, in the learning module, process the empty observation, whether you're in or out of model. I wrote... I wrote that down in my notes as, Phase 1 and Phase 2 A and B, and I think, actually.

that sort of step one of sending the observation to the learning module, if you then cut it off at the learning module, then you can make all the changes in a full... in a refactor that doesn't... shouldn't actually change anything, right? Yeah. that, that's, sometimes a nice, element of, or feature of a big change. It's nothing should actually change, in the output behavior.

So I was imagining that for that, phase one, and then Phase 2, and this maybe goes a little bit different from then how you wrote it up, Niels, was I was thinking of doing the out-of-model movement. Where you just... So basically, ignore in-model movements, and just do the out-of-model movement, where you do that job of keeping Keeping the hypothesis around for at least for a few steps. Which again, I think should basically... not affect... The behavior from how it was before.

Niels Leadholm: That one will, I think, just because, right now, that gives, right now, there's negative evidence right away, as soon as you move out of model.

but, oh, okay. And that's why we think it might... I think that was a comment that it might slow down inference a little. Or, convergence, a little, because right now. we yeah, if you're far from any learned points, you immediately get, I think it's actually the maximum negative evidence, minus 1 on that step. Whereas here, there, yeah, basically be this delay. So that one... It could be... it could still be done as a refactor, in that you probably have a hyperparameter, which is, like, how many steps Before the nevi... the, it becomes, Detracting, and if you basically set that to, 0, or 1, or whatever, then... then it should give the same effect. Would be one way to do it as a sort of refactor.

Jason Carver: And this shouldn't change anything if you go out of model, but the real observation is still on an object, right? That's still the same. We're only dealing with the case where both are true, you've gone out of model and out of object.

Niels Leadholm: as in, it will... it will change performance, So out of model is, in some sense... yeah, this is why it's complex. Out of model is, in some sense, orthogonal to off-object, in that...

Jason Carver: it.

Niels Leadholm: It can be out of model whether it's off-object or not. And in both cases, we would want to... Clamp the evidence.

So whether it's... it's gone off... And it's looking at a distant, object. Or it's, gone off and it's looking at a void. We still want to clamp it for those few steps, just to give it a chance to move back.

Jason Carver: But if you go off-muddle, but are on something at the same distance as you were before, then you should still do the negative evidence, right?

Niels Leadholm: No, cause, No, not if you think you're off-model. off-model, is basically saying, okay, we can't say anything, because we don't... For that particular model, we can't predict anything. Okay. And whether it's... whether we're sensing kind of something real, or, Because, yeah, with the... and it's also yeah, I guess from a practical point of view, that example of, the I and the vertical line, or the 7 and the 1, I don't know if that was helpful, but, There could be, different things That we sense when we move to that space where we're expecting something, And, Often it won't be off-object.

often there will be something there.

I guess it is.

Jason Carver: The one model should not get negative evidence when you move to the 7 bar.

Niels Leadholm: Yeah, for those, brief, yeah, that's correct, and even if it was a 7.

Viviane Clay: Why wouldn't it?

Jason Carver: the real thing you're looking at is a 7, you have a model of a 1, and you move to the bar at the top of the 7. Obviously, the 7 will improve, but you're saying the 1 should just be on ice.

Niels Leadholm: Plamped briefly, yeah. And then it'll start getting negative evidence.

Jason Carver: Okay.

Niels Leadholm: I think we have to do it that way.

Jason Carver: Okay.

Viviane Clay: Yeah, the one just doesn't have a prediction about that location.

Niels Leadholm: Yeah. But yeah, basically, I don't think... I don't think we want the intersection of off objects and out of... Model to be, like, an even more special condition. Yeah, and because it it relates to... This whole thing of, do you store, that there's nothing there? Like, how do you know whether to predict off-object or something else? are we meant to be storing that, oh, everything else is off-object, but it's it might not be. Yeah, there might just be something, I think that'll work, if we just, Yeah, if we do it like that. But it just means that, Yeah, it's just the things, inference might be a little slower at first, because of the... kind of putting, as you say, everything on ice for a couple steps.

Jason Carver: Okay.

Viviane Clay: And yeah, I just had a look again at the code for the sending, concretely sending the... of object observations. To the learning module. And so what we currently have... Is, So if we're not on the object, morphological features will be set to an empty list, And... When we construct this kind of state instance that's the output of the sensor module. We basically have morphological features be an empty list, This might actually have... This would... I... okay.

Niels Leadholm: Might already be enough, yeah.

Viviane Clay: This... I'm just looking if features will be in there. I think there might just be... this object coverage feature in there, because that's part of this if branch.

I think it wouldn't actually include color right now, not sure if we want to add that. But then useState will be set to false, because onObject is... False, and also invalid signals is set to true.

And the sensor module opposite this state, which, yeah, it will have a... Location, an empty list for morphological features, which is what we want. But then Monty, the kind of pair... the class that wraps around sensor modules and learning modules and routes the information. When it routes the information from the sensor modules to the learning modules, it looks at this useState flag, and if it's false, then it won't Add this to the learning module inputs. I think this will be the, first point of change to... yeah, basically remove this if statement, and then that should make Those, to be sent, to the learning modules, although... This will also make other things be sent to the learning modules that we still don't want to send there.

Jason Carver: What about that, bit where we set the flag?

Viviane Clay: Yeah, we could also just set you stay to true in that... we could just move... Just remove this part here. I think that might be better.

Niels Leadholm: Yeah, and also, the invalid signals, what does that cover otherwise?

Viviane Clay: Sometimes...

Niels Leadholm: Got multiple things?

Viviane Clay: Issues with extracting the surface novel.

Jason Carver: Yeah.

Viviane Clay: And, the feature changes, M, I think, also sets your state to false if there wasn't a significant change in features.

Niels Leadholm: Yeah, which... that one is fine, so we don't want to interfere with that one, the feature change sensor module. I'm just wondering whether... We could unify, If, If the signal is so corrupt that you can't really process morphological features. Maybe it's worth just treating that as Op objects, or This kind of null observation as well.

Jason Carver: Yeah,

Niels Leadholm: Do we still get that word?

Jason Carver: So when... like, when would... when would that happen? what's the... I guess it's... is it because there's just, A weird distribution of depth data in a single sensor patch.

Viviane Clay: Yeah, I think it's really special cases, and I'm not sure we would want to treat it as of object, because, yeah, I... I think it happens very rarely, but if I remember it right, it's something... if you look at the surface dead on or something, and then the matrix, there's some division of zero, or something like that.

Niels Leadholm: Okay.

Viviane Clay: It can, I think, can happen both with surf channels and principal curvature.

Niels Leadholm: Yeah. Okay, so then I guess we just want to make sure that is invalid, is not true, Yeah.

In the case of objects.

Viviane Clay: And, yeah.

Niels Leadholm: In the...

Viviane Clay: Very ugly. Not invalid. Maybe something like that.

Niels Leadholm: Because are we, with this, the logic above, the if-else and stuff. Did you say morphological features is being set as that empty dictionary if, we are off-object.

Viviane Clay: Yeah,

Niels Leadholm: Okay, yeah, if on object,

Viviane Clay: Yeah.

Niels Leadholm: But, so it almost... so valid signals... Okay, but isn't this where the check happens for valid signals? we maybe don't want to change that. Or it feels like we need to catch that separately, something like that. But we can maybe just make a note for it of this, we don't necessarily need to figure it out right now.

But, it's right.

Viviane Clay: Wait, what?

I think.

Niels Leadholm: I'm just saying, I guess we, yeah, we want to catch true, invalid signals, which is the thing you were talking about, the kind of weird depth data.

Viviane Clay: But then...

Niels Leadholm: We don't want to set is invalid. for, if it's just off-object. That's why I think.

Viviane Clay: I feel like...

Niels Leadholm: We need, an additional if, or something like that.

Viviane Clay: Oh, yeah. we'd probably, yeah, not just want to set this to false whenever an object is false,

Niels Leadholm: Yeah.

Viviane Clay: Yeah, we just want to set that to false if, object covers...

Jason Carver: We actually want it true there, right? We want it... if we're off-object, it's a valid signal with just.

Viviane Clay: Yeah.

Jason Carver: I think I'm making it a bit confusing now, because I renamed it to Valid Signals.

Niels Leadholm: They're right.

Viviane Clay: on whether we try and tricks.

Niels Leadholm: There's also a lot of double negatives. Not invalid.

Viviane Clay: Yeah, that's why I changed it, but if we rename that now, then we have to rename it everywhere in this function and invert what it returns.

Not make it more confusing for now, but, yeah, basically what... we'd... want to do is... if this thing is true.

Then invalid signals is true.

And then, if on object, we do this, otherwise we set morphological features to an empty list, but... Invalid signals are still... Falls, and in that case... Your state would only be false if they're actually in odd signals.

Niels Leadholm: yeah, that looks right.

Viviane Clay: Then, there's another... we could... it could also be done within this function. The unobject check. And then that way, we could still return color, for example, we could still return non-morphological features.

Niels Leadholm: Yeah, that... maybe that's like a... Nice to have, but...

Viviane Clay: Yeah, more fun. But yeah, there won't be as many, anyways, we won't have curvature magnitude and stuff like that if we're off-object, Yeah. I think it's not that important for now.

But the important thing is we'll still get XYZ locations, and we can... Then, if we set this flag to true, it will automatically be routed to the learning modules. Here. And then... I'm not sure, this is so long ago, but it looks like we already have a lot of code in the buffer to deal with incoming. On object... off-object observations.

We already store the onObject value, which right now should only be once, or only be truths. But, if... if... I don't know, the optimistic view would be that changing this... The buffer will already... deal with getting those, and we'll... oh, wrong file. And we'll already store for each, step whether we were on or off the object. And then... Yeah. It already, the... Oh, okay, this might have to be... Changed, I'm not sure if it filters by on object.

At.

Niels Leadholm: Yeah, that's one of the... I think, the tricky things is... is all this.

Viviane Clay: Yeah, so it already has functions like get all locations on object. Where it takes all the locations, and it filters it by whether we were on the object or not.

Niels Leadholm: Yeah.

Viviane Clay: Which kind of confuses me, why we wrote all this, if we're... Not already.

Niels Leadholm: Yeah, I'm trying to remember if this stuff predates, if there was... if there was a point at which we did pass off object observations.

And then we found that was causing an issue.

Or, is it because... does this buffer also store sensor module?

If this buffer is... Yeah, it doesn't, right? It should just be...

Viviane Clay: couldn't.

Niels Leadholm: It's a bit mysterious.

Viviane Clay: Yeah. Something to uncover.

Niels Leadholm: Yes, but... Yeah, like you say, maybe it will already handle some of it, but... Because, yeah, I think at its core, some of that was presumably written for, filtering, logging, so that we could be, like. Okay, we're just gonna observe what hypotheses changes happen when we were on object and stuff like that, but... but as you say, Vivian, generally, we've never been past... or... In our memory, we've never been passing off-object observations, so that's always a list of ones or TRUEs at... of the length of steps, basically.

Jason Carver: The buffer doesn't include things like when you're moving the surface. To the sensor, to the object, like... Because sometimes there are steps where you're not doing any inference, right?

Niels Leadholm: It might be that it includes... even if it doesn't include sensor model stuff, it may include... basically every time... I think that's what it... maybe is that, every time the learning module could be stepped. Including when, it's off-object.

Viviane Clay: Yeah, maybe a good place to start, debugging and testing would actually be this unit test here, called TestMovingOff Object and Back. Yeah, because that runs pretty fast, you don't have to run an experiment or anything, and it, uses just fake data to move... Beyond object and off and back on, and just seeing, what happens.

Jason Carver: Yeah, that's great.

Viviane Clay: And yeah, it won't, cover if you make changes to what the sensor module outputs, because here we are not using a sensor module, we're just manually creating some fake, messages and setting morphological features to... on object to zero and useState to false. But, it might give some insights on what the... Learning module does with that.

Oh, actually... Yeah, maybe it's not the best place, because this doesn't even invoke the multi-class, so it doesn't include any filtering. this one, we're just directly stepping the learning module and actually giving it the information.

Maybe... It might still be a good test for... for very specific changes, but, It wouldn't attest the kind of end-to-end pipeline of how Monty passes the observations between sensor and learning modules.

Let's see...

Niels Leadholm: What was the one where we stepped through the learning modules? That kind of, impasse the sensory. I don't think it's in Monty Base.

Viviane Clay: Oh yeah, here, in EvidenceLM test, we have one, I think, where we actually do a full...

Niels Leadholm: experiment.

Viviane Clay: yeah, test moving off objects is the name of the... Test. And I think the way we do it there is that we run a full experiment. But we pre-defined the actions that will be taken, so that the actions just take us straight off of the object.

Yeah... Yeah, this is probably the best test to start with.

Sorry, it's, been... it's been a bit of a while since I looked into that.

Jason Carver: No, this is great. this is still way faster than if I was just... Swimming around trying to guess at it, so this is great. I... I also, just as prep for this meeting, I did some, poking around and, found some unexpected behavior, which is perfect, because I get to ask about it now.

I did, What's the easiest way? I guess I could share my screen. But I did, A change on handle failed jump? Where, I just delayed the... the fail step. I just treated... I just... I switched it to just always treat it as successful, and then added this, cued action that happens at the beginning of that same function.

to, reorient it. The idea being, like, oh, it'll reorient it at the beginning of the next step.

Niels Leadholm: Yeah, so you can get that off-object observation. Yeah, Okay.

Jason Carver: Yeah, here, let me... I can... maybe I can.

Niels Leadholm: Yeah, unfortunately, the... Yeah, that whole... Policy is a bit of a... mess.

Jason Carver: so I just added this, concept of acute action at the beginning, and... this isn't how the actual change would go, this was just me trying to understand.

Niels Leadholm: No, I think it's a... yeah, it's a nice way to test it, yeah.

Jason Carver: and the surprise effect for me was, it... so I got this new... I got the, the log that says, there's no object visible, and then the next log is supposed to be, the one saying, okay, I'm moving... I'm now moving to the... To the object, but instead, it was showing up with, a huge gap. it would say, warning, no object visible in step 7. And then somewhere down in.

Niels Leadholm: Oh, after a bunch of steps.

Jason Carver: then it was, like, returning to the previous position. So, I just, I don't understand something about, like, when this code is triggered, basically.

Niels Leadholm: Yeah, what that probably is, yeah, the motor stuff is... is, Yeah, it's really complex, and a bit of a mess. It's... but basically, they're... There's different logic for handling off-objects from a motor system point of view, to summarize them, the, distant agent tends to, when it's, saccading around, in most versions, if it goes off the object, then it moves back on. It reverses the last action. But that should be on the next loop, and so it will... It should give it a chance to pass the... the observation. And then, like you noted. the fail, the, jump to goal state fail, That happens all within... the kind of environment, embodied environment, and so it doesn't give a chance to pass out, which is why, yeah, you were making that change. But then there's also... For the surface agent, if it's off object, it will try and look for the off... for the object. And in particular, the finger, you can imagine it's shifts around. Until it tries to bump into the object. So what might be happening is that logic is getting that's catching... Earlier than your, so you might... for the purpose of this kind of test, you might need to move that even earlier. So I think it's something like, if the observation is none, or something like that. There's some sort of if statement really early on. And then I think that will trigger, It's called something like.

Jason Carver: So this is the... so this is the environment interface. does the execute jump attempt pretty early. I don't think the first step isn't triggering, right? So this is pretty much right away. And then this queued action's, right at the beginning of that. I don't see... unless this moves into, a different... class somewhere. I don't see how I could make it happen any earlier. I don't understand how to make it happen any.

Viviane Clay: It might generally be easier to debug with the distant agent. Because that one, more frequently just moves off the object, and then we just revert its action.

Jason Carver: Okay.

Viviane Clay: I think with the Surface Agent, it's... But... More difficult, because whenever it's off the object, it's usually that something went wrong. it fell off or something. So it happens less frequently, and... It usually happens in some weird edge cases,

Niels Leadholm: Can I see the change in the code you made, by any chance?

Jason Carver: yeah. This one?

Viviane Clay: Are you sharing a.

Niels Leadholm: We're seeing a terminal.

We're seeing, that's coming often.

Jason Carver: This is the patch. The patch is showing in the terminal with the changes.

Niels Leadholm: Oh, okay, which line.

Jason Carver: Did you want to see the... did you want to see the new code all integrated, or just the changed lines?

Niels Leadholm: I don't mind, actually, this is fine, but right now, the way I see it, there's an added line on 755, a change to the warning.

Jason Carver: Oh, yeah, sorry, you're right, I was... I was only looking at the... here, let me just do... let me just do this. I'll show all the changes from main, which includes others. I was trying to isolate it a little bit,

Niels Leadholm: Yeah, no worries.

Jason Carver: Great.

Niels Leadholm: Okay, If self-queued action is not known, so this is embodied data. Yeah, I wonder if I'm actually this. So that was within pre-episode.

Jason Carver: This is called...

Niels Leadholm: Pre...

Jason Carver: Hey, Al.

Niels Leadholm: pre-episode... So you'd want it to be within the next call, I think, if queued action is not none. Rather than pre... Oh, no...

Jason Carver: Cutex. So let me.

Niels Leadholm: Yeah.

Jason Carver: pull this up.

execute jump attempt, is in the next...

Niels Leadholm: Yeah.

Jason Carver: But then, at the beginning of execute jump attempt is the.

Niels Leadholm: Oh, this is where you're doing it, okay.

Jason Carver: Yeah.

Niels Leadholm: I don't think, Q... I don't think execute Jump Attempt will be executing again, On the next step.

Jason Carver: Okay.

Niels Leadholm: So I think what you want to do.

Jason Carver: take...

Niels Leadholm: that... take that out, and... You can literally put it before the...

Jason Carver: Way up here.

Niels Leadholm: Exactly, if you put it there.

Jason Carver: Yeah, cool.

Niels Leadholm: And I think you'll catch it, yeah.

Jason Carver: Yeah, there was something... there was, Something about... yeah, the driving goal state is probably set to none, right?

Niels Leadholm: Exactly, yeah, I think the way it is, that once that's been attempted, it releases that, or resets it,

Jason Carver: Okay.

yeah, so then hopefully the warnings will be back-to-back in the same steps.

This won't take... Cool. Actually, I think I can pause it here. Oh, that almost happened too fast. Wait, let's see. And it appears... Wait, let's see... Because we want it to be in a... in the next step, But now... Now it's happening... Returning to previous position, it's happening... there's no step change between those two lines.

Niels Leadholm: So that's probably a... just something about the step counter or something. Would be my guess.

Jason Carver: Okay.

Niels Leadholm: It probably is the next step, but... but somehow the step counter's not being iterated, or... I don't know, yeah.

Jason Carver: Open. But I think it's a good idea.

Niels Leadholm: I think, like Vivian says, Distant Agent's probably a good place to start, just because it's a bit simpler, and then, but I think this is a nice idea for testing with, Yeah, the... basically passing the off object between these, goal state things, which is what we eventually want to do. The other thing is, parallel to this, but probably won't happen anytime soon, we are disentangling this so that you actually have, a full loop. So that, if we are going to have this kind of resetting, for example, like you've done here, it would happen on the next On the next step. But, yeah. I may have to run soon, unfortunately, but But yeah, but was there any... Kind of other...

Jason Carver: Yeah,

Niels Leadholm: we can definitely do...

Jason Carver: Google a lot.

Niels Leadholm: Asynchronously as well, obviously feel free to post loads of... loads of questions and, or yeah, point out things that are doing weird stuff.

Jason Carver: Great, yeah, there's questions about the... how the learning module knows if it's in a learning state, because you said not to use this effect if it's learning. Yeah. So I guess I'll just give, previews of things if there's not time to answer them.

There's... I can figure.

Niels Leadholm: That might be something, just, briefly on that one, so we have a buffer that you save, and then when you are learning, at the end of learning, you update the model. But so that might just be a case of, anything that has this null morphological feature doesn't get added.

Jason Carver: filtering it.

Niels Leadholm: That buffer, or... or we filter it later at the point of kind of updating the model, something like that.

Viviane Clay: Yeah, Niels, if you want, I can stay on and answer most of these questions.

Niels Leadholm: Are you okay?

Viviane Clay: Yeah.

Niels Leadholm: Okay, cool. Or yeah, just as much as you have time for, and then.

Viviane Clay: Yeah.

Niels Leadholm: Yeah, and then, but also, yeah, happy to...

Viviane Clay: But yeah, just to know how... Whether it's in learning or inference state, there should be a flag for the learning module as well that tells it whether it should update its models or not. Let me just quickly look up the name of it.

Models...

Jason Carver: I had in my head that... that it was, like, agnostic to the idea of being in a learning state or not.

Viviane Clay: Yeah, that...

Jason Carver: From an experimental point of view, there is some kind of...

Viviane Clay: Yeah, so from an experimental point of view, it is... let me share my screen again, real quick. Yeah. So most of it is, yeah, pretty.

Niels Leadholm: I'll, yeah, I'll see you guys later, but, yeah, really nice meeting you, Carver, and yeah, I'm sure we'll touch base again soon.

Jason Carver: Sounds good.

Viviane Clay: Yeah, see later, nails.

Where's the... where's our... Normal learning module code. Here we go.

let me just say... Add graph to memory, that should be it.

beer... Let's... No, this is just...

Jason Carver: It wasn't the... let's see, no.

Viviane Clay: Maybe build graph is the right place to start.

Build model... Sorry, this is a bit of a mess.

Update memory... Almost there. Here we go.

in the post-episode function of learning module, so there's no difference, during, matching inference, anything like that. But in the post-episode call, we check if the mode of the learning module is train, and we have more than one observation, or more than zero observations in the buffer. Then we call, self.updateMemory. And basically, the only difference between training and evaluation is whether we call self.updateMemory at the end of an episode.

And then, if you go deep into the update memory class, as I just went, out of... You should, at some point get to the place where the graph is... being built, yeah, somewhere here, get infos for graph updates, and that then calls get all locations on object. And that's one of the buffer functions that then, yeah, basically looks at the... which, IDs in the location array Are actually on object, and returns those.

Jason Carver: Okay, so maybe that also will work already, it just needs to be verified.

Viviane Clay: It's already done.

Jason Carver: the filter, yeah.

Viviane Clay: Yeah. Hopefully, maybe, hopefully.

Jason Carver: Okay, cool.

So there's the feature change filter and, questions about what to do when you go off object for that. And whether you pass that in or not. So the feature change filter is on the... sensor module side?

Viviane Clay: Yeah.

Jason Carver: I guess my intuition is the features changed a lot if you moved off the object, but that's not based on anything other than my intuition. so do we send... do we then send the data if the feature... if you move off object? or not. And... I guess you don't have any access to the model at that point. This is Model 3, right?

Viviane Clay: Yeah, so we check the feature change in the sensor module, and then if There was a significant feature change, we set useState to true. And... I don't think we want to change anything about that. we still don't want to send observations up if there was no feature change. And... Yeah, if there's a feature change, we want to send it... let me just check if we're actually looking at off-object here.

I think if we put it into the... Delta thresholds, we actually... Oh, here's a thing. If we're not on the object. Then it will automatically say false. here. Which is probably... Something that needs to be changed. Because... Otherwise... either you would have to run all of the experiments without the feature change filter. Or otherwise, the feature change filter will just, filter out. All these observations, even if you set it to true in the other part of the code.

Jason Carver: Okay, and that's a filter that's on a lot of ex... it's like a... it's like a default or modern filter,

Viviane Clay: Yeah, it's a default, yeah.

Jason Carver: Okay.

Viviane Clay: and

Jason Carver: So it makes sense to say, oh, this is a feature... or to, run it through the normal data pipeline if it's auth object.

Viviane Clay: Yeah, so one thing you could do for a first kind of testing is just set it to true here.

Jason Carver: That's the most basic...

Viviane Clay: But then...

Jason Carver: Great.

Viviane Clay: I think the nicer solution would be... To do the same thing we do here, and see if...

Jason Carver: Yeah.

Viviane Clay: If the last feature was on object, then the current one is off, return true. If the... if basically if last and current are different, then you return true and otherwise false. So if you're just moving an empty space a bunch, you're not sending all of these. You're really just sending when you move off and when you move back on.

Jason Carver: Perfect.

Okay... And then there was, Undo Last Action.

it was called Fix Me Undo Last Action in the Motor Policies. to me, it looks like maybe this is... this doesn't need to change, because I think it's saying... In the step we're in right now. change the thing we did in the previous step, which I think is what we want. that's, that's fine, that's... that is what we want to do, right? we went off before, and now we want to go back on object, and that's... that seems totally fine as a...

Viviane Clay: Yeah. Yeah, and I think... Yeah, so I agree, I think we can leave this how it is. And then, yeah, that's also one of the reasons using the distant agent with this kind of policy might be an easier way to debug, because this case happens a lot more often, where we go, we turn the camera off, too far off the object, and then the next step it gets reversed.

Jason Carver: Okay?

Okay, yeah, I just... I guess I wanted to double check that I understood that that it's not somehow... Doing that all within the same step.

Viviane Clay: Huh. Yeah, no... It... I don't think so, I'm just... Thinking through it again. we'll call this if the current observation is not on the object.

It might be doing it in one step now.

No. I... yeah, it should send us to the learning module first, and then... Under the last action. But, yeah, maybe something to keep in mind, to double-check.

Jason Carver: I'm not sure right now, 100. Sounds good.

And then the other things were I didn't even really know enough to know what to ask exactly, except... to, Help me see and understand where the evidence is applied to a hypothesis. I probably could figure that out, but I think it would help to just, help.

Viviane Clay: Yeah, for sure.

Yeah, let me go there. So if you go into Models and Evidence Matching, You'll find the hypothesis Updater.

Jason Carver: Yeah, it's named in a way that... and now I'm embarrassed that I asked.

Viviane Clay: Oh, no, it's, we're not there yet, This is just the first part of how to get there. So there's a function called updateHypotheses. And that function... calls displaceHypotheses and compute evidence, which is a function of the hypothesis displacer. It's a file right above it here. And if you got that function. That's really the one that does all the heavy lifting. And, yeah, I think we should probably split it into two functions, since having an AND inside of a function name is not a good sign.

Jason Carver: Good cue, yeah.

Viviane Clay: Yeah. But anyways, it does exactly those two things. It takes... The current hypotheses and rotates, or it takes the current, amount that we moved, and the direction we moved, and rotates it by the pose hypotheses. And then it takes the... the current... Hypothesis locations, and adds those rotated displacements to all of them. And this is where we, update all the hypotheses in parallel, so those are, like, two big matrix operations, to update all of them at the same time. And so then we have an array of search locations in the model's reference frame.

We filter them with the evidence update threshold right now for computational efficiency, so we don't... Test all of them.

But, yeah, basically the next step is then to calculate the evidence for each of these locations, and that happens in this function. And for that, we basically... We also rotate the, post-dependent features by the post hypotheses first. And then we search for the nearest neighbors in the model's reference frame. So that's... This is the, most expensive operation in Monty. I think... It basically takes all these search locations of where we might be on the object, and then for each location, it looks in the object model, which points in the model are nearby that location. Does that make sense?

Jason Carver: yeah, I think so. for this off-object observation... that'll just be a special case, Because at first, I was thinking, oh, it's a distant wall, Or maybe it won't be. What? No, it won't really be a split, because we'll still have the location.

So we'll... we'll still be doing... we'll still be searching for the...

Viviane Clay: Yeah, so what'd be...

Jason Carver: We're in a particular location in the hypothesis, but we're looking for those previously saved points that are somewhere nearby that location in the hypothesis, right?

Viviane Clay: Yeah, so we basically.

Jason Carver: Okay.

Viviane Clay: Here, the black dots are the model, so we saved a bunch of points of where this object exists in our model. And then, we have a bunch of hypotheses in the beginning, we could be on any of these locations on the object, in, two possible orientations. And then the sensor moved, so we apply that movement to each of those gray hypotheses, so then we get a bunch of possible locations after the movement, which are the gray dots here.

And then... Maybe the next picture is useful, This is just the example of one hypothesis, where we could be at this location, and the cylinder might either be upside down or right side up, the two possible orientations. And then we move like that. So we apply that movement in this direction and in this direction, so there are two possible locations we could be at. And for each of these possible... they're called the search locations in the code.

that's what... that's what, What was the output of that call before, and what we pass in here.

Jason Carver: And so for each of these locations, we basically then search in a radius.

Viviane Clay: for the points, the nearest points in that radius in the model. So here we have these three points now. And then for the three points in that radius, we would calculate, one, the physical distance between the search location and these points. And the feature difference and pose difference, so do those points actually store the same orientation, and the same color, and whatever other features you have? And then those get added up, and the best match gets identified, so whichever one is closest and has the best, feature match.

And, however close and... it matches determines how much evidence is being added. Through this hypothesis.

Jason Carver: So this is a place where the distance and surface sensors are gonna be really different, right? So the distance sensor is going to give us a location, really far off of our model, probably, when it moves off object.

it'll... it'll be the location that the... Distance sensor gives us will be, like, the horizon.

Viviane Clay: Yeah.

Jason Carver: So that'll be, like, very clearly... the search radius will just give us nothing.

Viviane Clay: Exactly, yeah, it will basically be, can I draw on this? So yeah, if we moved off the object from here, it would be like that. Oh, yellow is maybe the worst color to draw in.

It would be like this, and then... This would be a search location, there's a radius around it, there's nothing in the radius, so what would happen right now is it gets a penalty of negative 1. For the symposis.

Jason Carver: I don't think it will be... What I'm saying is that the... Won't the depth be... like, the... with a distance sensor, the depth of that point will be probably far away, right? So the translation won't just be perpendicular to you, it'll also be, like... Away from you.

Viviane Clay: Yeah, you mean it would go, like, all the way back?

Jason Carver: Yeah...

Viviane Clay: Yeah.

Jason Carver: done soon.

Viviane Clay: Although, also for the surface agent. You might see a similar thing... if the service agent it has a kind of maximum depth it can see, which is not very far. It would just be that maximum depth that it gets. So yeah, it couldn't be, like, super out back in the distance, but it would still be... Usually, it would still be off the object, and you would still not get any morphological features.

Jason Carver: Yeah, I guess what I'm... but the location sent with the surface sensor... And the null morphology could be... right next to the surface, right? You can move just off of that cylinder.

Viviane Clay: That's true.

Jason Carver: you're playing a game with, is the search radius bigger? Is... big enough... will the search radius catch The edge of this object, even though, it's not supposed to be Even though you really are off of it.

Viviane Clay: yeah, that's a... that's a good point. Yeah, for the surface agent, it would just be... yeah, it could be a pretty small location change. And then, yeah, there might still be a point in the search radius. Even though we're not getting morphological features.

Jason Carver: Yeah, and we don't want to give it... A heavy penalty for that.

It looks like, oh, there should be a point there, but there's not, which would nor... which, in these other examples, should be heavily penalized, but here seems like.

It shouldn't.

Viviane Clay: Yeah, that's the... what I think Neil's called the edge case.

Jason Carver: Okay, Yeah, we're not sure yet how much of a negative effect this will have.

Viviane Clay: On performance, because, yeah, like you say, you wouldn't really want to penalize it just because the search radius is so large that it still picks this up.

Jason Carver: The other thing, I guess if you want to get fancy, the surface normal could tell you some information about how bad it is that you're off-object, but... but expect to be on it. if the surface normal is pointing at... away from the sense... from the observation. Yeah, that's actually...

Viviane Clay: We have something a little bit like that, and...

Jason Carver: Okay.

Viviane Clay: Been meaning to, try and think about if we can improve this more. But yeah, basically, when we do the search radius of the nearest neighbors, it's usually not a perfect circle like this, but instead, it's like a squashed sphere. That goes...

Jason Carver: Okay.

Viviane Clay: along the sur- like, perpendicular to the, surface normal. So if the surface normal is, this... Then the search radius would be perpendicular to it, so a sphere around the surface. And...

Jason Carver: But that's the surface normal that you've sensed, right? And our off object won't have any surface normal. We only get the surface normals for the actual hypothesis, right?

Viviane Clay: yeah, so I guess one thing... One possible solution could be... That if there's no morphological feature, so no surface normal. The search radius becomes very small.

would that work?

Maybe you wouldn't. Maybe that would... Maybe that would solve the edge case, but, ruin all the other cases. Once things get noisy...

Jason Carver: Yeah, I can imagine it being a problem.

Viviane Clay: Yeah... Yeah, so I guess right now the idea would be to just see how big of an effect that would have. And then, if it is an issue, try and think about ways we could... we could solve that. But it might be more of a, yeah, edge case, But yeah, does that kind of clarify where the evidence gets updated?

Jason Carver: Yeah, that was excellent.

Viviane Clay: Okay, yeah, I didn't go further, yeah, basically just the last step, once you have the nodes in the search radius. The next lines of the code will do the, Finding the distance to them, and calculating the feature difference between them, and then calculating the evidence from that.

Jason Carver: Okay.

Viviane Clay: Okay. And yeah, this is where... No points were found in the search radius.

Jason Carver: Okay.

Cool. And then... the... I guess the last thing was that I still have kind of a vague idea that we're stepping through the environments, and then the... And then... no, Monty? No, the experiment, Monty, and then the environment... this is the... There, there's the, diagram that I can go look up, but... but I don't... I don't feel like I... I wanted to be able to see in one place where the whole... Flow is of... knowing that there's... because sometimes it seems like, for example, the sensor is allowed to take multiple steps within a... within a single, step, Monty step, because I saw... I saw some code somewhere where inside of the step, it, called the next step inside of the sensor, and so I... I was just trying to figure out, when... when is that allowed, or... or I was just trying to wrap my head around the... The, flow, and even the ordering of things, is it always... so it's always, policy, and then... Or, motor, and then sensor, and then learning module within a single step, or, that kind of thing.

Viviane Clay: Yeah, so maybe.

Jason Carver: sensor, and then there's time motor?

Viviane Clay: There's... this is a different view of this kind of class diagram, which is really more about how these classes are related to each other.

Jason Carver: Correct.

Viviane Clay: Flow of information through things. I'll start here, maybe. So we have the environment, which is, in this case, habitat, that renders the objects, the simulator. And then we have an environment interface around that, which basically controls the simulator. there we specify things like, Which object should you initialize in which episode, and what orientation should it have, and delete the previous object when the next episode starts, kind of thing. And then... That kind of also steps the agent through the environment. And when it gets an action from the motor system, it steps the environment, and it gets a new observation from the environment. And that observation gets sent to the sensor module. And then the sensor module checks it extracts features and poses, but it also can do other things, like check if there was significant feature change.

if there was no significant feature change. for example, then it wouldn't be sent to the learning module. We would skip the step in the learning module and step the motor system right away, send the next action. Go here, but... If we are not looking at that, then usually the sensor module output would go to the learning module. The learning module would use those features at locations to update its hypotheses, and then it might output a suggested action to the motor system, and then the motor system ex... Translates... so the learning module would output a target location in space. And then the motor system would translate that into, whatever the agent is capable of. If it's a camera that can only tilt, or a touch sensor that can move along the surface, it would translate that to the specific language of that agent, and send it to the environment.

Jason Carver: Okay. And for, model-free movements, sometimes can the sensor module can, do movements itself, or, send... Can you give one example where we're skipping over to the model.

Viviane Clay: Yeah, so I think, Let me see if I have a good diagram of... But... somewhere... No... yeah, maybe here. This was a result of a brainstorming session, so it's a bit...

Jason Carver: Okay, yeah.

Viviane Clay: Yes, it's a bit older, because we... then we still had that data load and data set, now that's the environment interface. But maybe the sympathy.

Jason Carver: If I remember correctly.

Viviane Clay: Sorry?

Jason Carver: So thanks to Anna, if I remember correctly.

Viviane Clay: Yeah, exactly, yeah. Very good. So basically, we have three, action loops. One is the reflex loop that goes directly from the environment to the motor system. And... no kind of further information processing happens. It's the... if you imagine a safety loop, where, if you touch something really hot, it goes back, you don't need to do any further processing. But then the most interesting ones are the model-free and model-based loops. Model 3 is, you basically send the sensor module output directly to the motor system, and then the motor system determines what to do.

And model-based, as it goes through the learning module, and the learning module figures out what to do next, and sends a goal to the motor system. And just because you sent this, and the motor... the next action is based on sensor module information, doesn't mean it can't go to the learning module 2. actually, most of the time, we do model-free stuff, we move along the direction of principal curvature, or something like that. along the rim of the cup and stuff like that, and that only requires knowing what the sensor's currently sensing, it doesn't need any models. the motor system is basing its actions on what the sensor module is sensing, but we're still processing and updating hypotheses in the learning module.

Jason Carver: Okay.

Viviane Clay: Yard.

Jason Carver: Is, could you... yeah, it would, even, also, can you take me to the code in Monty, where it's...

Viviane Clay: Yeah.

Jason Carver: House and Lucy.

Viviane Clay: Yeah, for sure.

the Monty class kind of... Handles most of these things.

let's see... Where'd it go?

Jason Carver: That was interesting. The step... it was like, the step is... there were different kinds of step.

That sucks.

Viviane Clay: Yeah... Yeah, I guess the most... High-level overview of the, order of things is here in this, monthly class.

And basically, we... An unusual matching step, which is the steps where we actually process stuff in the learning module. We would aggregate sensory input, so basically get the... whatever Whatever raw observations we get from the environment, and then pass that through the sensor Modules. Let me just double check if that's true. Yeah, so we... we basically get the observation from the environment, which is the RGBD camera image. And then we loop over the sensor modules.

Get whatever observation is for that sensor module. And, step the sensor module to get the processed output. And then append that all into an array, which is then assigned to sensor module outputs in the multi-class. And... Interesting.

Jason Carver: It's also doing the learning module outputs in here, too.

Viviane Clay: Yeah, so it's, if you think of... Monty as, a hierarchy of sensor modules at the lowest level, and then learning modules at all the levels.

It's not like to process at the highest level of the hierarchy, if the high-level learning module It's not like the highest level learning module is only called, you have to call them in succession of the level of hierarchy they're in, but instead, all learning modules get stepped at the same time, and it's just that The highest level one might not get any input for a couple of steps, because the... input needs to propagate through the hierarchy first, but basically, this part here Just looks at what is the current learning module output from the previous step, so that it can become the input for the next step. And that's because in Monty, there isn't really a clear hierarchy. You... learning module output can go to another learning module's input, but it could skip a level in the hierarchy, or... several levels in the hierarchy, it wouldn't mind. So basically, what we do is collect all the outputs from the sensor modules and learning modules from the previous state that they were in. And then put them as input. To all of them at the same time, again. Does that make sense?

Jason Carver: Gotcha. Yeah, totally.

Viviane Clay: Okay. So yeah, like you said, we also loop up all the learning modules called getOutput. And that depends on what state they were in before. At the very first step, that would just be nothing, or even at the first I don't know, 10 or 20 steps, while the learning module doesn't have a certain hypothesis yet, it won't produce an output. And then, yeah, we have these two lists. And then... Where was the abstract class for the overflow? Then we would step the learning modules.

And... Yeah, that's a bit hard to... Yeah, here. So again, we loop over all the learning modules. And we extract what inputs should go to that learning module. And then the important part is this one here, or this one. We figure out which type of step we want to do right now. We have a matching step, an exploratory step. And then we apply that to... The sensory inputs, where we do learningmodule.step with, sensor inputs.

And then the rest is just, some logging stuff. That's not that important. And... yeah, so we pass the sensor stuff into the learning module step, and that's where all the hypothesis updates happen. Where was the strict class again? And then, after that, we vote. after all the learning modules have updated their hypotheses, we go and check them all again, see, hey, what's your current vote on what you're sensing?

And update them based on that. And then we pass the goals, so then we go back to all the learning modules and say, hey, where do you want to move next? And then... Each landing module produces a target location in space. Sensor modules can also do that. And then we pass that to the motor system, and the motor system basically resolves, okay, which one am I gonna execute, where am I gonna go? And then outputs an action to the environment. And yeah, this is just to check whether an episode should be done or not, if Monty is confident in what it's sensing.

Jason Carver: yeah, this is great. That's super helpful. and then exploratory versus matching... is... We don't... we don't have to... I don't need to step through the exploratory, but just to understand the difference at the high level.

Viviane Clay: Yeah, it's really not that important, it's basically... we're basically doing it to save compute. essentially, after Monty has recognized an object. it wants to learn more about it. if Monty is in training phase, so it actually is supposed to update its models, it might recognize the mug after just moving a little bit. It says, oh yeah, that's the Thousand Brains mug. let me update my model with some new points that I just saw. But since these new points were, like, they were used to recognize it, they're not gonna add a lot of extra new information about the object, and there are very few points, so it's... it would be quite slow to learn that way. So what we do is, after it's recognized, we explore it a bit more, and... eventually, one of our goals is to have some better exploratory policies, that basically look at, okay, where is my model underrepresented? Where do I have highest uncertainty? So let's go there and learn a bit more about this part of the mug. We don't do that right now, we just move randomly some more, collect more points, and since we're just exploring, we already recognize the object. We don't really want to, spend every step updating hypotheses again, so that... we just clamp that part of the code to not update hypotheses. Eventually, We might wanna... keep doing that, because if we're in an environment with many objects, we might move on to a different object, and we want to recognize that again, so it might just be some kind of useful... thing we're using for the current setup to save some time, but... Conceptually, it's not... not that important. It's not really an important conceptual feature of Monty, it's more of a, let me run my experiments a bit faster, kind of thing.

Jason Carver: Great. Cool. Yeah, this is all super helpful, and... Yeah, I think... I think that's, covers my list of, questions for now.

Yeah, like I said, thank you so much.

Really, valuable.

Viviane Clay: Yeah, for sure. Yeah, thank you. this is, it's a pretty steep learning curve, I know.

Yeah. Definitely. Cool that you're... you're up for it, and diving deep in...

Jason Carver: I liked it when you said, you're, like, you wrote this down a few years ago, oh yeah, this will be just, a quick, to-do item to take care of later, and then the more you look into it, oh, this... this'll take a little bit.

Viviane Clay: Yeah.

Jason Carver: A little bit of thought.

Viviane Clay: And, yeah. Yeah, it's probably one of the hardest items you could have picked. One of the, I don't know, maybe not. Maybe it turns out it just works, but it feels like we came back to it many times, it was always... we always confused ourselves again, and then decided, okay, let's hold off for now. But, it would be really cool to have that, finally. In the code,

Jason Carver: Yeah. Yeah, I didn't even know I was jumping in the deep end, but here I am.

Viviane Clay: Yeah. So yeah, definitely, feel free to write anytime you run into questions, and we can also schedule a next meeting. Maybe after the holidays, because, Yeah, I'm taking some time off, too. But, yeah, really cool that you're... you're up for this challenge.