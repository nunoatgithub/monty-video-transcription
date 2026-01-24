Jason Carver: Luckily, I do have some familiarity with particle filters. I haven't implemented one in 20 years, but I did implement it once. A paper I really liked was the Thrun paper from 2001 that MixedRMCL was based on. I was pleased to see it referenced in the Thousand Brains Project paper. It was a fun connection. There are always details, like how to actually use the sensor data to update the observation. One place I was getting stuck was trying to apply the sensor data to all the observations or hypotheses at once. I was trying to do it in one fell swoop, rather than looking at one hypothesis at a time. It's almost trivial to update a single hypothesis with the off-object observation.

Niels Leadholm: Basically, they'll all be integrating movement and think they're somewhere in that object's reference frame. They'll get the sensor data, and if a hypothesis is being updated, it receives the sensory data, which may or may not match what was learned at nearby points. Once a hypothesis moves through space in this reference frame and receives sensory data, it looks at its learned neighbors to see if anyone matches what it's getting. If it's nowhere near anyone, that's an out-of-model situation, where the point has moved far away. If it's strictly off-object, that implies there are some learned points nearby, but it's getting an observation that says, "I'm sensing nothing." That's where we want a high prediction error. In some ways, it's good; in some ways, it's computationally expensive. As long as the hypothesis is considered good enough to continue updating, we'll move it with the incoming movement data and pass that sensory information. We don't need to work out the correspondence between the hypotheses being updated and something like a ray of vision. 

Jason Carver: I think when you move the sensor on a single hypothesized model—

Niels Leadholm: Yeah.

Jason Carver: Let's talk about distance sensors, because a touch sensor is even more trivial. With a distance sensor, you move it, and the depth of the model is different in different places. Moving the eye, that's the process where you have to find where it lands on the model. I had in my head the idea of rays deciding where the sensor lands on the model.

Niels Leadholm: Right now, we have the depth information, and together with the location of the sensor, we have the location being sensed.

Jason Carver: I'm talking about just in the model.

Niels Leadholm: Without recognizing the model, we have a new location and the previous location, and that's the displacement in world space.

Viviane Clay: Basically, the whole process of taking account of depth already happens in the sensor module. We're already in the transform before it gets to the sensor module. I think maybe it's useful if we use a whiteboard for some of this.

Niels Leadholm: Sounds good.

Viviane Clay: Do you mind if I make this off-object, out-of-model one?

Niels Leadholm: No, please.

Viviane Clay: Okay. I'll just post this link in the Zoom channel.

Jason Carver: So you're not predicting where the sensor would land on the model; you're looking at where the sensor actually landed and then figuring out—

Niels Leadholm: Between those two points, yes. It assumes there is depth information. At the moment, it benefits from all the path integration, accounting for how much the sensor moved and the new depth estimate. The more noiseless that is, the better. That gives us a new location we're sensing at, which is the location of the feature being sensed. In that sense, it's not that different from the finger. Whether we're physically touching it or seeing it at a distance, the location of the feature is out there in the world. It's not in the retina space or something like that. If we have an old observation and a new one, we can calculate that displacement in world space, or it could be egocentric space relative to the robot. We have that displacement, and the learning module has a hypothesis about the orientation of the object. It can use that to transform the displacement based on different hypotheses. Different hypotheses will move in different ways on the object, depending on how the object is oriented.

Jason Carver: This is a question to make sure I'm understanding what you're saying.

Niels Leadholm: Yeah.

Jason Carver: If I have a model of these glasses and I move my eye—my distance sensor—to the side here—

Niels Leadholm: Yeah.

Jason Carver: Let's say there are two different models, one with only one of these and one with both. I look at the glasses at the side, and one of them is missing or folded. My distance sensor lands on the further of the two.

Niels Leadholm: Yeah.

Jason Carver: That is what gets sent to the hypotheses, and that's going to end up matching both models—the one with and without the hook that's closer to me—even though my mental model of the glasses would tell me that the one with the hook closer to me should actually—

Niels Leadholm: There should be a—

Jason Carver: There's something obscuring your vision. So the fact that we're using where the sensor actually lands and just moving to there in the model ignores the fact that there's an obscuring feature in front of it in the other model.

Niels Leadholm: Yeah.

Jason Carver: Okay, but that's how it works right now, and that's fine. I just want to make sure I understand how.

No, that is a good example. There's no way of accounting for this kind of ray of vision, and that's come up. I don't think we've really discussed it in this exact setting like you described, but it's come up in terms of, say, you want to test a point now. You may have seen we have a policy that suggests, "Oh, I should move to the handle," things like that. But we've thought, depending on where we are on the object, you would have to move in different ways to actually see it. Sometimes there might be some self-occlusion, and sometimes there might not be. Where is that kind of knowledge stored? It could be anything from a scene-level representation accounting for both models over your sensors, or maybe you have models of how your eyes work and how they sense and understand this concept of self-occlusion. We don't want to wrap that up into a single learning module, but for some reason, a distant learning module has this sense that if I view from certain directions, it'll be obscured. We don't have, I guess this is the short answer, a way of dealing with that.

The main thing is that the cortical messaging protocol, whatever the learning module expects, is basically just a 3D location and orientation in space of where the sensor is sensing. It doesn't expect where the agent is that the sensor is attached to, but it expects the location of where the sensor is sensing. For example, in monkeys, there are spatial view cells. They fire whenever the monkey looks at a specific location in the room, and it doesn't matter from where the monkey is in the room or where the eyes are in the sockets; it just matters what location in the room the monkey's looking at. That's what we expect as the input for the learning modules.

To make a brief diagram of what kind of info is available at what point: we have the environment with the entire object, and then we have the sensor, like a little camera patch, that sees a small part of the environment. In most of our experiments, we get an RGBD camera image and a location of the sensor. The sensor location is the camera that's up here and looking at this location. That would be the location here, plus the RGBD image. Then we apply a transform, and the plan is to eventually wrap this transform into the sensor module, but this is how it looks right now. The transform takes the depth image and the sensor's location and combines the two to calculate an array of 3D locations, saying where in space each pixel is—adding the depth values together with the sensor location. Then we have an array of each pixel, where it is hitting the object in space, and that gets sent to the sensor module. The sensor module turns it into a cortical messaging protocol, which takes the location stored at the center pixel of the patch and uses the rest of the pixel locations to calculate the surface normal and curvature directions to define the orientation in space. It also takes the color at the center pixel and some features.

To rephrase what you were saying earlier, Viviane, and relevant to the glasses example: if the learning module is sensing this mug and it senses this inside wall, it doesn't know if it's up here and that's why it's sensing it, or that it's here and there's a hole in it and that's why it's sensing it. It just knows, "I'm getting something at this location."

Our intuition right now is that would almost be another learning module's job—to learn this idea of occlusion and what that means for particular sensors. I think it's an interesting question.

Yeah, I guess it's similar to having a different object occlude yours and keeping in your mind that there is another object behind it.

It's not something we would represent at the input level. You might have a higher-level learning module that has a scene representation that there is something behind it because it has seen it previously at that location. Like Niels mentioned, maybe at the output level, when you calculate an action, you might use that kind of scene model to calculate that you need to go around or something like that.

But at the input level, it doesn't really matter.

Yeah, I guess it could even help build intuition about where the hierarchy should break down. If something can occlude another thing, then maybe it should actually be different sub-objects that are built together. I shouldn't speculate too much, because I have no idea what I'm talking about. There was one tangent—I think it was Niels who said something about this problem being solved already in a multi-object scene.

Yes.

If you go onto a subject and come back, my first thought in response is: if we just treat off-object as a distant wall or something, which I think you've also brought up, does that mean everything's already solved if we just feed in a different wall with a surface normal pointing at us? Does that mean this is already solved and we don't have to do anything special here? I guess that's always a question to ask at the beginning: are we doing a special case for something that doesn't need a special case?

Niels Leadholm: For example, with the surface agent, it may be relatively close to the object and sense nothing. Part of that already working relies on the fact that it's really far away. It fits with the idea that there are no morphological features—like when I look at the sky or into a black well, I don't get a sense of a surface. When my finger is just moving in space, I don't sense a surface there. At a certain level, the change is relatively small. We just need this special case where morphological features are set to none. Much of the existing feature matching and location updating logic remains the same. If I sense nothing at a distance and my sensor moves far, I'm out of the reference frame, which currently results in negative evidence.

I think we still need to change it, but at that level, it's not a big change. It's more about the knock-on effects.

Jason Carver: Okay.

Niels Leadholm: These are great questions. You definitely understood the problem well.

Jason Carver: There were maybe some slight differences. I wanted to go over the high-level plan. This is almost more of a process or project engineering view: what are the steps we do? Viviane did that first summary of sending the observations to the learning module, even when you're off-object. Then, step two is for the learning module to process the empty observation, whether you're in or out of model. I wrote that down as Phase 1 and Phase 2A and B.

Step one is sending the observation to the learning module. If you cut it off at the learning module, you can make all the changes in a refactor that shouldn't actually change anything. That's sometimes a nice feature of a big change—nothing should actually change in the output behavior.

I was imagining that for phase one, and then Phase 2. This may go a little differently from how you wrote it up, Niels. I was thinking of doing the out-of-model movement, where you ignore in-model movements and just do the out-of-model movement, keeping the hypothesis around for at least a few steps. That should basically not affect the behavior from before.

Niels Leadholm: That one will, just because right now, there's negative evidence right away as soon as you move out of model. That's why we think it might slow down inference or convergence a little, because if you're far from any learned points, you immediately get the maximum negative evidence, minus one on that step. Here, there would be a delay. It could still be done as a refactor, with a hyperparameter for how many steps before it becomes detracting. If you set that to zero or one, it should give the same effect. That's one way to do it as a refactor.

Jason Carver: This shouldn't change anything if you go out of model, but the real observation is still on an object, right? We're only dealing with the case where both are true: you've gone out of model and out of object.

Niels Leadholm: It will change performance. Out of model is, in some sense, orthogonal to off-object.

Jason Carver: Right.

Niels Leadholm: It can be out of model whether it's off-object or not. In both cases, we want to clamp the evidence. Whether it's gone off and is looking at a distant object, or gone off and is looking at a void, we still want to clamp it for a few steps to give it a chance to move back.

Jason Carver: But if you go off-model but are on something at the same distance as before, you should still do the negative evidence, right?

Niels Leadholm: No, not if you think you're off-model. Off-model means we can't say anything, because for that particular model, we can't predict anything. Whether we're sensing something real or not, it's also a practical point. For example, with the "I" and the vertical line, or the "7" and the "1," there could be different things we sense when we move to that space where we're expecting something. Often it won't be off-object; often there will be something there.

Jason Carver: The one model should not get negative evidence when you move to the 7 bar.

Niels Leadholm: For those brief steps, that's correct, even if it was a 7.

Viviane Clay: Why wouldn't it?

Jason Carver: The real thing you're looking at is a 7, you have a model of a 1, and you move to the bar at the top of the 7. The 7 will improve, but the 1 should just be on ice.

Niels Leadholm: Clamped briefly, yes. Then it'll start getting negative evidence.

Jason Carver: Okay.

Niels Leadholm: I think we have to do it that way.

Jason Carver: Okay.

Viviane Clay: The one just doesn't have a prediction about that location.

Niels Leadholm: Yes. I don't think we want the intersection of off-object and out-of-model to be an even more special condition. It relates to whether you store that there's nothing there. How do you know whether to predict off-object or something else? Are we meant to be storing that everything else is off-object? It might not be. I think that'll work if we do it like that. Inference might be a little slower at first because of putting everything on ice for a couple of steps.

Jason Carver: Okay.

Viviane Clay: I just looked again at the code for sending off-object observations to the learning module. Currently, if we're not on the object, morphological features are set to an empty list. When we construct the state instance that's the output of the sensor module, morphological features are an empty list. This might actually be enough.

Niels Leadholm: Might already be enough, yeah.

Viviane Clay: I'm checking if features will be in there. There might just be the object coverage feature, because that's part of this if branch. I don't think it would include color right now; not sure if we want to add that. Then useState will be set to false because onObject is false, and invalid signals is set to true.

The sensor module outputs this state, which will have a location and an empty list for morphological features, which is what we want. Monty, the class that wraps around sensor modules and learning modules and routes the information, looks at the useState flag. If it's false, it won't add this to the learning module inputs. I think the first point of change is to remove this if statement, and that should make those be sent to the learning modules, although this will also make other things be sent to the learning modules that we still don't want to send.

Jason Carver: What about that bit where we set the flag?

Viviane Clay: We could also just set useState to true there, or just remove this part. That might be better.

Niels Leadholm: And the invalid signals, what does that cover otherwise?

Viviane Clay: Sometimes...

Niels Leadholm: Got multiple things?

Viviane Clay: Issues with extracting the surface novel.

Jason Carver: Yeah.

Viviane Clay: The feature changes module also sets useState to false if there wasn't a significant change in features.

Niels Leadholm: That one is fine, so we don't want to interfere with the feature change sensor module. I'm just wondering whether we could unify—if the signal is so corrupt that you can't process morphological features, maybe it's worth treating that as off-object or as a null observation.

Jason Carver: Yeah.

Niels Leadholm: Do we still get that word?

Jason Carver: When would that happen? Is it because there's a weird distribution of depth data in a single sensor patch?

Viviane Clay: I think it's really special cases, and I'm not sure we would want to treat it as off-object. I think it happens very rarely, but if I remember right, it's something like if you look at the surface dead on and then the matrix, there's some division by zero or something like that.

Niels Leadholm: Okay.

Viviane Clay: It can happen with surf channels and principal curvature.

Niels Leadholm: Okay, so then I guess we just want to make sure that isInvalid is not true in the case of off-objects.

Viviane Clay: Yeah.

Niels Leadholm: In the...

Viviane Clay: Very ugly. Not invalid. Maybe something like that.

Niels Leadholm: With the logic above, the if-else and stuff, did you say morphological features is being set as that empty dictionary if we are off-object?

Viviane Clay: Yeah.

Niels Leadholm: Okay, yeah, if on-object.

Viviane Clay: Yeah.

Niels Leadholm: So valid signals... but isn't this where the check happens for valid signals? Maybe we don't want to change that. Or it feels like we need to catch that separately. We can maybe just make a note for it; we don't necessarily need to figure it out right now.

Viviane Clay: Wait, what? I think.

Niels Leadholm: I'm just saying, we want to catch true invalid signals, which is the weird depth data.

Viviane Clay: But then...

Niels Leadholm: We don't want to set isInvalid for off-object. That's why.

Viviane Clay: I feel like...

Niels Leadholm: We need an additional if or something like that.

Viviane Clay: Oh, yeah. We'd probably not want to set this to false whenever onObject is false.

Niels Leadholm: Yeah.

Viviane Clay: We just want to set that to false if object covers...

Jason Carver: We actually want it true there, right? If we're off-object, it's a valid signal.

Viviane Clay: Yeah.

Jason Carver: I think I'm making it confusing now, because I renamed it to Valid Signals.

Niels Leadholm: They're right.

Viviane Clay: On whether we try and tricks.

Niels Leadholm: There's also a lot of double negatives. Not invalid.

Viviane Clay: That's why I changed it, but if we rename that now, then we have to rename it everywhere in this function and invert what it returns. Not to make it more confusing for now, but basically what we'd want to do is if this thing is true, then invalid signals is true. If onObject, we do this; otherwise, we set morphological features to an empty list, but invalid signals are still false, and in that case, useState would only be false if they're actually invalid signals.

Niels Leadholm: Yeah, that looks right.

Viviane Clay: There's another way—it could also be done within this function, the onObject check. That way, we could still return color, for example, or other non-morphological features.

Niels Leadholm: Maybe that's a nice to have.

Viviane Clay: More fun, but there won't be as many. We won't have curvature magnitude and stuff like that if we're off-object. I think it's not that important for now. The important thing is we'll still get XYZ locations, and if we set this flag to true, it will automatically be routed to the learning modules. I'm not sure, this is so long ago, but it looks like we already have a lot of code in the buffer to deal with incoming on-object and off-object observations.

We already store the onObject value, which right now should only be true. The optimistic view would be that changing this, the buffer will already deal with getting those, and we'll already store for each step whether we were on or off the object. It might have to be changed; I'm not sure if it filters by on object.

Niels Leadholm: That's one of the tricky things about all this.

Viviane Clay: It already has functions like get all locations on object, where it takes all the locations and filters by whether we were on the object or not.

Niels Leadholm: Yeah.

Viviane Clay: Which confuses me—why we wrote all this if we're not already doing that.

Niels Leadholm: I'm trying to remember if this stuff predates a point at which we did pass off-object observations. Then we found that was causing an issue. Or is it because this buffer also stores sensor module data? It doesn't, right? It should just be—

Viviane Clay: Couldn't.

Niels Leadholm: It's a bit mysterious.

Viviane Clay: Something to uncover.

Niels Leadholm: Yes, but like you say, maybe it will already handle some of it. At its core, some of that was presumably written for filtering and logging, so we could observe what hypothesis changes happen when we were on object and things like that. But as you say, Viviane, in our memory, we've never been passing off-object observations, so that's always a list of ones or TRUEs, matching the length of steps.

Jason Carver: The buffer doesn't include things like when you're moving the surface to the sensor, to the object, because sometimes there are steps where you're not doing any inference, right?

Niels Leadholm: It might be that it includes—even if it doesn't include sensor model stuff, it may include basically every time the learning module could be stepped, including when it's off-object.

Viviane Clay: Maybe a good place to start debugging and testing would be this unit test called TestMovingOffObject and Back. It runs pretty fast, you don't have to run an experiment, and it uses fake data to move beyond the object and back on, just to see what happens.

Jason Carver: That's great.

Viviane Clay: It won't cover changes to what the sensor module outputs, because here we're not using a sensor module—we're just manually creating fake messages and setting morphological features to onObject zero and useState false. But it might give some insights on what the learning module does with that.

Actually, maybe it's not the best place, because this doesn't even invoke the multi-class, so it doesn't include any filtering. Here, we're just directly stepping the learning module and giving it the information.

It might still be a good test for very specific changes, but it wouldn't test the end-to-end pipeline of how Monty passes observations between sensor and learning modules.

Niels Leadholm: What was the one where we stepped through the learning modules? That kind of impasse the sensory. I don't think it's in Monty Base.

Viviane Clay: In EvidenceLM test, we have one where we actually do a full—

Niels Leadholm: Experiment.

Viviane Clay: Yeah, test moving off objects is the name of the test. I think the way we do it there is to run a full experiment, but we pre-define the actions so that the actions take us straight off the object.

Yeah, this is probably the best test to start with.

Sorry, it's been a while since I looked into that.

Jason Carver: No, this is great. This is still way faster than if I was just guessing, so this is great. I also, just as prep for this meeting, did some poking around and found some unexpected behavior, which is perfect because I get to ask about it now.

I did—what's the easiest way? I guess I could share my screen. I made a change on handle failed jump, where I just delayed the fail step. I switched it to always treat it as successful, and then added this cued action that happens at the beginning of that same function to reorient it. The idea is that it will reorient at the beginning of the next step.

Niels Leadholm: So you can get that off-object observation. Okay.

Jason Carver: Let me see if I can—

Niels Leadholm: Unfortunately, that whole policy is a bit of a mess.

Jason Carver: I just added this concept of a cued action at the beginning. This isn't how the actual change would go; this was just me trying to understand.

Niels Leadholm: I think it's a nice way to test it.

Jason Carver: The surprise for me was, I got the log that says there's no object visible, and then the next log is supposed to say I'm now moving to the object, but instead, there was a huge gap. It would say, "Warning: no object visible in step 7," and then somewhere later—

Niels Leadholm: After a bunch of steps.

Jason Carver: Then it was returning to the previous position. I don't understand when this code is triggered, basically.

Niels Leadholm: The motor system is really complex and a bit of a mess. There's different logic for handling off-objects from a motor system point of view. To summarize, the distant agent, when saccading around, in most versions, if it goes off the object, it moves back on and reverses the last action. That should be on the next loop, so it should give it a chance to pass the observation. Like you noted, the jump to goal state fail happens within the embodied environment and doesn't give a chance to pass out, which is why you were making that change. For the surface agent, if it's off object, it will try to look for the object. In particular, the finger shifts around until it tries to bump into the object. That logic might be catching earlier than yours, so for this test, you might need to move that even earlier. If the observation is none, there's an if statement really early on that will trigger. It's called something like—

Jason Carver: So this is the environment interface. It does the execute jump attempt pretty early. I don't think the first step is triggering, so this is right away. The queued action is right at the beginning. I don't see, unless this moves into a different class, how I could make it happen any earlier. I don't understand how to make it happen any—

Viviane Clay: It might generally be easier to debug with the distant agent because that one more frequently just moves off the object, and then we just revert its action.

Jason Carver: Okay.

Viviane Clay: I think with the surface agent, it's more difficult because whenever it's off the object, it's usually that something went wrong—it fell off or something. So it happens less frequently and usually in some weird edge cases.

Niels Leadholm: Can I see the change in the code you made, by any chance?

Jason Carver: Yeah. This one?

Viviane Clay: Are you sharing a—

Niels Leadholm: We're seeing a terminal.

Jason Carver: This is the patch. The patch is showing in the terminal with the changes.

Niels Leadholm: Oh, okay, which line?

Jason Carver: Did you want to see the new code all integrated, or just the changed lines?

Niels Leadholm: I don't mind, this is fine. Right now, I see an added line on 755, a change to the warning.

Jason Carver: Oh, yeah, sorry, you're right. I was only looking at the—here, let me just do this. I'll show all the changes from main, which includes others. I was trying to isolate it a little bit.

Niels Leadholm: Yeah, no worries.

Jason Carver: Great.

Niels Leadholm: Okay, if self-queued action is not known, so this is embodied data. I wonder if I'm actually this. That was within pre-episode.

Jason Carver: This is called—

Niels Leadholm: Pre—

Jason Carver: Hey, Al.

Niels Leadholm: Pre-episode. You'd want it to be within the next call, I think, if queued action is not none, rather than pre—oh, no—

Jason Carver: Cutex. So let me—

Niels Leadholm: Yeah.

Jason Carver: Pull this up. Execute jump attempt is in the next—

Niels Leadholm: Yeah.

Jason Carver: But then, at the beginning of execute jump attempt is the—

Niels Leadholm: Oh, this is where you're doing it, okay.

Jason Carver: Yeah.

Niels Leadholm: I don't think execute jump attempt will be executing again on the next step.

Jason Carver: Okay.

Niels Leadholm: So I think what you want to do—

Jason Carver: Take—

Niels Leadholm: Take that out, and you can literally put it before the—

Jason Carver: Way up here.

Niels Leadholm: Exactly, if you put it there.

Jason Carver: Yeah, cool.

Niels Leadholm: And I think you'll catch it.

Jason Carver: Yeah, there was something about the driving goal state probably being set to none, right?

Niels Leadholm: Exactly. Once that's been attempted, it releases that or resets it.

Jason Carver: Okay. So then hopefully the warnings will be back-to-back in the same steps. This won't take—cool. Actually, I think I can pause it here. Oh, that almost happened too fast. Wait, let's see. It appears—wait, let's see—because we want it to be in the next step, but now it's happening. Returning to previous position, it's happening—there's no step change between those two lines.

Niels Leadholm: That's probably just something about the step counter. Would be my guess.

Jason Carver: Okay.

Niels Leadholm: It probably is the next step, but somehow the step counter's not being iterated. I don't know.

Jason Carver: Open. But I think it's a good idea.

Niels Leadholm: Like Vivian says, distant agent's probably a good place to start because it's a bit simpler. I think this is a nice idea for testing, basically passing the off object between these goal state things, which is what we eventually want to do. Parallel to this, but probably not happening anytime soon, we are disentangling this so you actually have a full loop. If we're going to have this kind of resetting, like you've done here, it would happen on the next step. I may have to run soon, but was there any other—

Jason Carver: Yeah.

Niels Leadholm: We can definitely do—

Jason Carver: Google a lot.

Niels Leadholm: Asynchronously as well. Feel free to post loads of questions or point out things that are doing weird stuff.

Jason Carver: Great, yeah, there's questions about how the learning module knows if it's in a learning state, because you said not to use this effect if it's learning. I'll just give previews of things if there's not time to answer them. There's—I can figure.

Niels Leadholm: Briefly on that, we have a buffer that you save, and when you are learning, at the end of learning, you update the model. That might just be a case of anything that has this null morphological feature doesn't get added.

Jason Carver: Filtering it.

Niels Leadholm: That buffer, or we filter it later at the point of updating the model, something like that.

Viviane Clay: Niels, if you want, I can stay on and answer most of these questions.

Niels Leadholm: Are you okay?

Viviane Clay: Yeah.

Niels Leadholm: Okay, cool. Or just as much as you have time for.

Viviane Clay: Yeah.

Niels Leadholm: Happy to...

Viviane Clay: Just to know, whether it's in learning or inference state, there should be a flag for the learning module that tells it whether it should update its models or not. Let me quickly look up the name of it.

Models...

Jason Carver: I had in my head that it was agnostic to the idea of being in a learning state or not.

Viviane Clay: From an experimental point of view, it is. Let me share my screen again. Most of it is pretty—

Niels Leadholm: I'll see you guys later. Really nice meeting you, Carver. I'm sure we'll touch base again soon.

Jason Carver: Sounds good.

Viviane Clay: See you later, Niels.

Where's the normal learning module code? Here we go.

Let me just say, add graph to memory, that should be it.

No, this is just—

Jason Carver: It wasn't the—let's see, no.

Viviane Clay: Maybe build graph is the right place to start.

Build model... Sorry, this is a bit of a mess.

Update memory... Almost there. Here we go.

In the post-episode function of the learning module, there's no difference during matching, inference, or anything like that. In the post-episode call, we check if the mode of the learning module is train, and we have more than zero observations in the buffer. Then we call self.updateMemory. The only difference between training and evaluation is whether we call self.updateMemory at the end of an episode.

If you go deep into the update memory class, at some point you get to the place where the graph is being built. Somewhere here, get infos for graph updates, and that calls get all locations on object. That's one of the buffer functions that looks at which IDs in the location array are actually on object and returns those.

Jason Carver: Maybe that will work already, it just needs to be verified.

Viviane Clay: It's already done.

Jason Carver: The filter, yeah.

Viviane Clay: Yeah. Hopefully.

Jason Carver: Okay, cool.

So there's the feature change filter and questions about what to do when you go off object for that, and whether you pass that in or not. The feature change filter is on the sensor module side?

Viviane Clay: Yeah.

Jason Carver: My intuition is the features changed a lot if you moved off the object, but that's just my intuition. Do we send the data if you move off object or not? I guess you don't have any access to the model at that point. This is Model 3, right?

Viviane Clay: Yeah, so we check the feature change in the sensor module, and if there was a significant feature change, we set useState to true. I don't think we want to change anything about that. We still don't want to send observations up if there was no feature change. If there's a feature change, we want to send it. Let me check if we're actually looking at off-object here.

If we put it into the delta thresholds, here's a thing: if we're not on the object, then it will automatically say false here. Which is probably something that needs to be changed. Otherwise, you'd have to run all of the experiments without the feature change filter, or the feature change filter will just filter out all these observations, even if you set it to true in the other part of the code.

Jason Carver: That's a filter that's on a lot of—it's like a default or modern filter.

Viviane Clay: Yeah, it's a default.

Jason Carver: Okay.

Viviane Clay: And—

Jason Carver: So it makes sense to run it through the normal data pipeline if it's off object.

Viviane Clay: One thing you could do for a first kind of testing is just set it to true here.

Jason Carver: That's the most basic—

Viviane Clay: But then—

Jason Carver: Great.

Viviane Clay: I think the nicer solution would be to do the same thing we do here and see if—

Jason Carver: Yeah.

Viviane Clay: If the last feature was on object and the current one is off, return true. If last and current are different, return true; otherwise, false. So if you're just moving in empty space, you're not sending all of these. You're really just sending when you move off and when you move back on.

Jason Carver: Perfect.

Okay, and then there was Undo Last Action.

It was called Fix Me Undo Last Action in the Motor Policies. It looks like this doesn't need to change, because I think it's saying, in the step we're in right now, change the thing we did in the previous step, which is what we want. We went off before, and now we want to go back on object, and that seems totally fine.

Viviane Clay: Yeah, I agree, I think we can leave this how it is. That's also one of the reasons using the distant agent with this kind of policy might be an easier way to debug, because this case happens a lot more often, where we turn the camera too far off the object, and then the next step it gets reversed.

Jason Carver: Okay, I just wanted to double check that I understood that it's not somehow doing that all within the same step.

Viviane Clay: No, it should send us to the learning module first, and then undo the last action. But maybe something to keep in mind, to double-check.

Jason Carver: I'm not sure right now, 100. Sounds good.

And then the other things were, I didn't even really know enough to know what to ask exactly, except to help me see and understand where the evidence is applied to a hypothesis. I probably could figure that out, but I think it would help to just help.

Viviane Clay: Yeah, for sure.

Let me go there. If you go into Models and Evidence Matching, you'll find the hypothesis updater.

Jason Carver: It's named in a way that—now I'm embarrassed that I asked.

Viviane Clay: Oh, no, we're not there yet. This is just the first part of how to get there. There's a function called updateHypotheses. That function calls displaceHypotheses and computeEvidence, which is a function of the hypothesis displacer. It's a file right above it here. That's really the one that does all the heavy lifting. We should probably split it into two functions, since having an "AND" inside a function name is not a good sign.

Jason Carver: Good cue.

Viviane Clay: But it does exactly those two things. It takes the current hypotheses and rotates, or it takes the amount and direction we moved, and rotates it by the pose hypotheses. Then it takes the current hypothesis locations and adds those rotated displacements to all of them. This is where we update all the hypotheses in parallel, so those are two big matrix operations to update all of them at the same time. We end up with an array of search locations in the model's reference frame.

We filter them with the evidence update threshold for computational efficiency, so we don't test all of them.

The next step is to calculate the evidence for each of these locations, and that happens in this function. We also rotate the pose-dependent features by the pose hypotheses first, then search for the nearest neighbors in the model's reference frame. This is the most expensive operation in Monty. It takes all these search locations of where we might be on the object, and for each location, it looks in the object model to find which points are nearby. Does that make sense?

Jason Carver: I think so. For this off-object observation, that'll just be a special case. At first, I was thinking it's a distant wall, or maybe it won't be. No, it won't really be a split, because we'll still have the location.

So we'll still be searching for the—

Viviane Clay: Yeah, so what'd be—

Jason Carver: We're in a particular location in the hypothesis, but we're looking for those previously saved points that are somewhere nearby that location in the hypothesis, right?

Viviane Clay: Yeah, so we basically—

Jason Carver: Okay.

Viviane Clay: Here, the black dots are the model, so we saved a bunch of points of where this object exists in our model. We have a bunch of hypotheses in the beginning; we could be on any of these locations on the object, in two possible orientations. Then the sensor moved, so we apply that movement to each of those gray hypotheses, and we get a bunch of possible locations after the movement, which are the gray dots here.

Maybe the next picture is useful. This is just the example of one hypothesis, where we could be at this location, and the cylinder might either be upside down or right side up, the two possible orientations. Then we move like that. We apply that movement in this direction and in this direction, so there are two possible locations we could be at. For each of these possible locations—they're called the search locations in the code—that's what was the output of that call before, and what we pass in here.

Jason Carver: And so for each of these locations, we basically then search in a radius.

Viviane Clay: For the nearest points in that radius in the model. Here we have these three points now. For the three points in that radius, we calculate the physical distance between the search location and these points, the feature difference, and pose difference—do those points actually store the same orientation, the same color, and whatever other features you have? Those get added up, and the best match gets identified, so whichever one is closest and has the best feature match.

However close it matches determines how much evidence is being added through this hypothesis.

Jason Carver: So this is a place where the distance and surface sensors are going to be really different, right? The distance sensor is going to give us a location really far off our model, probably, when it moves off object.

It'll be the location that the distance sensor gives us—like the horizon.

Viviane Clay: Yeah.

Jason Carver: So the search radius will just give us nothing.

Viviane Clay: Exactly, it will basically be—can I draw on this? If we moved off the object from here, it would be like that. Yellow is maybe the worst color to draw in.

It would be like this, and this would be a search location. There's a radius around it, and there's nothing in the radius, so what would happen right now is it gets a penalty of negative 1 for the symposis.

Jason Carver: I don't think it will be—what I'm saying is, with a distance sensor, the depth of that point will probably be far away, right? So the translation won't just be perpendicular to you, it'll also be away from you.

Viviane Clay: Yeah, you mean it would go all the way back?

Jason Carver: Yeah.

Viviane Clay: Yeah.

Jason Carver: Done soon.

Viviane Clay: Also, for the surface agent, you might see a similar thing. If the surface agent has a kind of maximum depth it can see, which is not very far, it would just be that maximum depth that it gets. It couldn't be super far back in the distance, but it would still be off the object, and you would still not get any morphological features.

Jason Carver: Yeah, I guess what I'm— but the location sent with the surface sensor and the null morphology could be right next to the surface, right? You can move just off of that cylinder.

Viviane Clay: That's true.

Jason Carver: You're playing a game with, is the search radius big enough? Will the search radius catch the edge of this object, even though it's not supposed to, even though you really are off of it?

Viviane Clay: That's a good point. For the surface agent, it could be a pretty small location change. There might still be a point in the search radius, even though we're not getting morphological features.

Jason Carver: And we don't want to give it a heavy penalty for that.

It looks like there should be a point there, but there's not, which in these other examples should be heavily penalized, but here it shouldn't.

Viviane Clay: That's what I think Neil called the edge case.

Jason Carver: We're not sure yet how much of a negative effect this will have.

Viviane Clay: On performance, because you wouldn't really want to penalize it just because the search radius is so large that it still picks this up.

Jason Carver: If you want to get fancy, the surface normal could tell you how bad it is that you're off-object but expect to be on it. If the surface normal is pointing away from the observation, that's actually...

Viviane Clay: We have something a little bit like that.

Jason Carver: Okay.

Viviane Clay: I've been meaning to think about if we can improve this more. When we do the search radius of the nearest neighbors, it's usually not a perfect circle, but instead, it's like a squashed sphere.

Jason Carver: Okay.

Viviane Clay: It goes along the surface, perpendicular to the surface normal. If the surface normal is this, then the search radius would be perpendicular to it, so a sphere around the surface.

Jason Carver: But that's the surface normal that you've sensed, right? Our off-object won't have any surface normal. We only get the surface normals for the actual hypothesis, right?

Viviane Clay: Yes, so one possible solution could be that if there's no morphological feature, so no surface normal, the search radius becomes very small. Would that work? Maybe that would solve the edge case, but ruin all the other cases. Once things get noisy...

Jason Carver: I can imagine it being a problem.

Viviane Clay: Right now, the idea would be to see how big of an effect that would have. If it is an issue, try to think about ways we could solve that. But it might be more of an edge case. Does that clarify where the evidence gets updated?

Jason Carver: That was excellent.

Viviane Clay: I didn't go further. Basically, just the last step: once you have the nodes in the search radius, the next lines of the code will find the distance to them, calculate the feature difference between them, and then calculate the evidence from that.

Jason Carver: Okay.

Viviane Clay: This is where no points were found in the search radius.

Jason Carver: Okay. Cool. The last thing was that I still have a vague idea that we're stepping through the environments, and then Monty, and then the environment. There's the diagram that I can look up, but I wanted to be able to see in one place where the whole flow is. Sometimes it seems like, for example, the sensor is allowed to take multiple steps within a single Monty step, because I saw some code where inside of the step, it called the next step inside of the sensor. I was just trying to figure out when that is allowed, or trying to wrap my head around the flow and the ordering of things. Is it always policy, then motor, then sensor, then learning module within a single step, or something like that?

Viviane Clay: Maybe.

Jason Carver: Sensor, and then there's time motor?

Viviane Clay: This is a different view of this class diagram, which is more about how these classes are related to each other.

Jason Carver: Correct.

Viviane Clay: Flow of information through things. I'll start here. We have the environment, which is habitat, that renders the objects, the simulator. Then we have an environment interface around that, which controls the simulator. There we specify things like which object to initialize in which episode, what orientation it should have, and delete the previous object when the next episode starts. That also steps the agent through the environment. When it gets an action from the motor system, it steps the environment and gets a new observation from the environment. That observation gets sent to the sensor module. The sensor module checks, extracts features and poses, but it can also do other things, like check if there was significant feature change.

If there was no significant feature change, for example, then it wouldn't be sent to the learning module. We would skip the step in the learning module and step the motor system right away, send the next action. If we are not looking at that, then usually the sensor module output would go to the learning module. The learning module would use those features at locations to update its hypotheses, and then it might output a suggested action to the motor system. The motor system would translate that, so the learning module would output a target location in space. The motor system would translate that into whatever the agent is capable of. If it's a camera that can only tilt, or a touch sensor that can move along the surface, it would translate that to the specific language of that agent and send it to the environment.

Jason Carver: For model-free movements, sometimes the sensor module can do movements itself, or send... Can you give one example where we're skipping over to the model?

Viviane Clay: Let me see if I have a good diagram. This was a result of a brainstorming session, so it's a bit...

Jason Carver: Okay.

Viviane Clay: It's a bit older, because then we still had that data load and data set; now that's the environment interface. Maybe the sympathy.

Jason Carver: If I remember correctly.

Viviane Clay: Sorry?

Jason Carver: Thanks to Anna, if I remember correctly.

Viviane Clay: Exactly. Very good. We have three action loops. One is the reflex loop that goes directly from the environment to the motor system. No further information processing happens. It's like a safety loop: if you touch something really hot, it goes back, you don't need further processing. The most interesting ones are the model-free and model-based loops. Model-free is when you send the sensor module output directly to the motor system, and then the motor system determines what to do.

And model-based goes through the learning module, which figures out what to do next and sends a goal to the motor system. Just because the next action is based on sensor module information doesn't mean it can't go to the learning module too. Most of the time, we do model-free actions, moving along the direction of principal curvature or along the rim of the cup, which only requires knowing what the sensor is currently sensing and doesn't need any models. The motor system bases its actions on what the sensor module is sensing, but we're still processing and updating hypotheses in the learning module.

Jason Carver: Okay.

Viviane Clay: Yard.

Jason Carver: Could you take me to the code in Monty where it's...

Viviane Clay: Yeah.

Jason Carver: House and Lucy.

Viviane Clay: Yeah, for sure.

The Monty class handles most of these things.

Let's see, where did it go?

Jason Carver: That was interesting. The step—there were different kinds of step.

Viviane Clay: Yeah, I guess the most high-level overview of the order of things is here in this Monty class.

Basically, we have an unusual matching step, which is where we actually process things in the learning module. We aggregate sensory input, get whatever raw observations we get from the environment, and pass that through the sensor modules. Let me double check if that's true. We get the observation from the environment, which is the RGBD camera image, and then we loop over the sensor modules.

We get whatever observation is for that sensor module, step the sensor module to get the processed output, and append that all into an array, which is then assigned to sensor module outputs in the Monty class.

Jason Carver: It's also doing the learning module outputs in here, too.

Viviane Clay: Yeah, so if you think of Monty as a hierarchy of sensor modules at the lowest level and learning modules at all the levels, it's not like you process only at the highest level of the hierarchy. All learning modules get stepped at the same time. The highest level one might not get any input for a couple of steps because the input needs to propagate through the hierarchy first, but this part just looks at what is the current learning module output from the previous step so it can become the input for the next step. In Monty, there isn't really a clear hierarchy. A learning module output can go to another learning module's input, but it could skip a level or several levels in the hierarchy. We collect all the outputs from the sensor modules and learning modules from the previous state and then put them as input to all of them at the same time. Does that make sense?

Jason Carver: Gotcha. Yeah, totally.

Viviane Clay: Okay. Like you said, we also loop up all the learning modules called getOutput, and that depends on what state they were in before. At the very first step, that would just be nothing, or even at the first 10 or 20 steps, while the learning module doesn't have a certain hypothesis yet, it won't produce an output. We have these two lists. Where was the abstract class for the overflow? Then we would step the learning modules.

Again, we loop over all the learning modules and extract what inputs should go to that learning module. The important part is figuring out which type of step we want to do right now. We have a matching step and an exploratory step. We apply that to the sensory inputs, doing learningmodule.step with sensor inputs.

The rest is just some logging. We pass the sensor data into the learning module step, and that's where all the hypothesis updates happen. After that, we vote. After all the learning modules have updated their hypotheses, we check them all again to see their current vote on what they're sensing and update them based on that. Then we pass the goals, going back to all the learning modules and asking where they want to move next. Each learning module produces a target location in space. Sensor modules can also do that. We pass that to the motor system, which resolves which one to execute and where to go, then outputs an action to the environment. This is just to check whether an episode should be done or not, if Monty is confident in what it's sensing.

Jason Carver: Yeah, this is great. That's super helpful. And then exploratory versus matching—I don't need to step through the exploratory, but just to understand the difference at the high level.

It's really not that important; we're basically doing it to save compute. After Monty has recognized an object, it wants to learn more about it. If Monty is in the training phase and supposed to update its models, it might recognize the mug after just moving a little bit and say, "Oh yeah, that's the Thousand Brains mug. Let me update my model with some new points I just saw." But since these new points were used to recognize it, they're not going to add much extra information about the object, and there are very few points, so it would be quite slow to learn that way. 

So after it's recognized, we explore it a bit more. Eventually, one of our goals is to have better exploratory policies that look at where the model is underrepresented or where there is the highest uncertainty, and then go there to learn more about that part of the mug. Right now, we just move randomly, collect more points, and since we're just exploring and already recognize the object, we don't want to spend every step updating hypotheses again. We clamp that part of the code to not update hypotheses. Eventually, we might want to keep doing that, because in an environment with many objects, we might move on to a different object and want to recognize that again. For now, it's just a useful thing for the current setup to save time. Conceptually, it's not an important feature of Monty; it's more about running experiments faster.

Great, this is all super helpful. That covers my list of questions for now. Thank you so much—really valuable.

Yeah, thank you. It's a pretty steep learning curve, I know. Definitely cool that you're up for it and diving deep in.

I liked it when you said you wrote this down a few years ago as a quick to-do item, and then the more you look into it, the more you realize it will take a bit.

Yeah.

A little bit of thought.

Yeah, it's probably one of the hardest items you could have picked. Maybe it turns out it just works, but it feels like we came back to it many times, always confused ourselves, and then decided to hold off for now. It would be really cool to have that in the code.

Yeah, I didn't even know I was jumping in the deep end, but here I am.

Yeah. Definitely feel free to write anytime you run into questions, and we can also schedule another meeting. Maybe after the holidays, since I'm taking some time off too. It's really cool that you're up for this challenge.