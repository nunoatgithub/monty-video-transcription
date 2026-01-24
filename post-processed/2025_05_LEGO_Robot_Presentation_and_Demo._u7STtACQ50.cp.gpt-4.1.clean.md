Okay, everybody see this? Hi, we're team Everything is Awesome, Rami and myself.

There we go. Explain the team's origin, please. In the beginning, we got some Legos, bought a bunch of stuff, and started assembling it into a platform. This is the platform actually running. This is our robot assembly—one of our motors and part of our motor system. We calibrated it scientifically to see how fast it could go. We calibrated it well. The other part of the robot is a sensorimotor module. This is the elevator that goes up and down. In the background, you can see the sensorimotor with the camera and the depth with the RGB camera and the depth camera on it. That's what the robot looks like combined.

We did a lot of debugging. This is an example of debugging the depth sensorimotor. You can see different depth resolution versus RGB resolution. Every dark point is an RGB point, and the depth sensors were more pixelated, worse. Some lessons learned: early on, we reminded each other not to eat the dataset since some of it was edible and in the kitchen, so we separated it from the rest of the food we planned on eating. Another lesson learned was that building something with Monty end to end was really great. We had to write and understand every single part of the Monty system. Rami and I are now much more familiar with how the whole system works. I understood TER for a little bit, so that was great. There's a resource that really helped with intuition—some of the Monty framework things. There are some ideas for action refactor I want to do after we're done, noticing too many resets happening before an episode. In simulation, you never notice it, but with a robot, you wonder why it's doing so many resets before it starts. That was a neat finding. We ran into the same problem, spent too much time on it, and decided we'd always have to press the button twice before starting the experiment. We had to take two pictures because the first picture would always be black for some reason. I removed the extra reset. Our coding approach was to fork the entire Monty repository and hack whatever we needed to. That was convenient and worked well for the hackathon.

Picking coordinates that make the problem easy helped. Our robot has a central platform that rotates and a part that goes up and down. Our units are the robot radius, and we are on the unit circle, which simplified a lot of things. That was super helpful.

Next, debugging and visualizations. I realized early on that having very good visualizations and debugging goes a long way in something like this. We started working on some nice visualizations. You'll see that in the next few slides. We were able to see the sensors' positions live as they made movements, as well as the current MLH or what Monty thinks is happening, the rotations, and all of that. We had some trouble with the coordinate systems. For the get state of the agent, we used a different coordinate system than Monty, thinking it would still work fine, but it did not plug well with the depth to 3D. We ended up changing all our computations for the get state of the agent. That's where we started looking into cos too.

We tried model scaling, using a different scale than what was in the provided dataset. That did not work very well, and I'm not sure why. We added code into the grid object model so you can scale the model by a scale factor, and it will scale the mesh and recalculate the KT3 and everything, but that still did not help much. We ended up training our models, but the models we trained are very sparse and may not work very well. The idea is that if we train a dense model, it will work better, but you'll see we still have reasonable performance.

Early on, we had a lot of networking issues. The reason was multiple routers, and if clients are connected to different routers, they can't talk to each other. We needed a router, but couldn't make it connect to the internet except through a hacky solution: plugging it into a WiFi extender, which gave internet to the router, and then we could connect to the router.

The cool thing about what we built is that we could decouple the simulator from Monty itself. We tried running two different mons on the same hardware. Tristan and I were running experiments at the same time and fighting for the hardware, which was very cool to see. The sensors would move—I would give a command to move somewhere, and Tristan would move it somewhere else, and we'd start arguing about needing the resources. The depth camera gave us a lot of trouble—too much troubleshooting and debugging went into that. Debugging setup goes a long way.

With troubles changing the scale of the existing dataset, we ended up training on the dataset ourselves. If you don't recognize it, that is a cup. This is training sped up 40 times. On the left, you see the visualization being built, and on the right, you see the robot using a training policy to orbit around the object from the bottom up and scan it. That was the idea behind it.

This is what the final scan for the cup looked like. It does end up looking like a cup, but the handle is a bit detached from the cup. We had some trouble with the depth information and maybe the focal point or field of view. It's a perfect circle, but the handle is a little separated. Our evaluation works fine with the trained models, but maybe this is why scaling the meshes didn't work well—because they're different. During inference, we can see this is a different kind of visualization where I'm plotting the current MLH in real time. If you can figure out the rotation, this is where it thinks the sensorimotor is compared to where the mug is. It was able to figure out that the cup was right side up, but it could not figure out the rotation on the y-axis, or where the handle is.

But it could separate the cup from all the other objects in the dataset, which is good. We used a policy based on random actions. We had to rewrite it a bit to use our actions, but as you can see in the video, those actions are just purely random—up, down, and rotating around the object. The sensor is always guaranteed to be on the object in these cases. If you're off the object, how does it know? There's a transform, so based on the depth, it knows. If the depth is too far, then you're not on the object. We go through building the semantic labels based on the depth.

Is this the time for the live demo, or does that come after all the presentations? Maybe we wait until after the presentations and pick one object to demo on. Sounds good. That's it. Nice. Great job. Looks really cool.

Can I ask those same two questions? How did your project demonstrate Monty's capabilities, and how do you see the application you're working on for the future? Demonstrating Monty's capabilities, I think this is probably the first system that has actual movements in the world, instead of just scanning over an image. It's not like we're taking an image and moving a patch over it—the patch itself is moving through the world, which is very different from what we had before. It's demonstrating a different side of Monty's capabilities with an actual motor. This thing works as a sensorimotor.

Just one point about the patch: in previous presentations, you saw a full image being taken. Here, Monty only sees those dots—there's no image of the cup, nothing else. Monty learns just from those dots on the left, and based on that, it learns to recognize objects. There's no full picture given to Monty at any point.

In terms of future capabilities, this is a first step. Just like with the drone team, there are opportunities to explore boating, which I think is important. We're building this with Lego, so it's easy to add a different sensorimotor from a different angle, and we can move it independently or together as part of one agent. They can move like two sensorimotor patches on a finger together, or as different hands looking at different parts of the mug. It's very extendable the way we set it up.

It's the first time Monty is working with a motor in the real world, which is huge. For us, it's a great setup to test Monty in the real world. Right now, anything more complex or involving movement has to be tested in simulation. Now we have a real-world test bed, and we can give it any kind of object—we don't have to create a simulated object dataset. We can pick something from the kitchen and put it on the platform to see what Monty does.

It also scans very nicely and very fast, but it's still sparse compared to what I would expect. The meshes you gave us are very nice and dense, but this is sparse. The fact that it still works with those sparse models is mind-blowing to me.

Does it work at any speed? If you slow down or speed up the motor, does it still have the same results? Slowing it down is always easier. Speeding it up, we're running at a high speed, but we're limited by how long it takes to transfer the image wirelessly from the sensors to the computer and process them. This is actually the bottleneck. One of the challenges was sending bigger images to stitch the depth camera with the RGB, sending both from the Raspberry Pi to the computer, and then stitching those. We found that if we just send the patches and do the computations for which patch we want—sending smaller images across the network—it goes much faster. Monty is much faster than the bottleneck of sending images. So it works fine at high speeds.

To Monty, it doesn't matter how fast you move or in what pattern you move over the object. You don't need to have seen that pattern before during training. It can generalize to any speed of movement as long as, as Rami says, the transfer is fast enough.

You're muted. We can speed up inference by giving Monty multiple sensors. If I have a thousand sensors looking at something, it can be recognized instantaneously rather than having to move, or you can move it once. Once we put this in hardware, it could go very fast. Another thing about demonstrating future capabilities is that we have zero precise movement. When the elevator goes up, we ask it to go a certain distance, but it goes whatever distance it manages. There's minimal precision when it rotates; if we ask it to rotate by seven degrees, it does whatever it wants. As a result, we are able to work on proprioception and ensure Monty is still processing where the object actually is. What we're demonstrating is that you don't need precise movement as long as you know where you end up. The policies still work and can infer and train objects, even with imprecise motor control, which is a new demonstration outside of simulation.

There were times when the rotation robot, the one that rotates the platform, wasn't even moving. It tries to move, but it looks like it doesn't have enough power, or we're just doing small steps. Because we're using proprioception, we're getting the position of the agent, so it doesn't matter. It would just add points at that same location, or depending on how the object is built, it doesn't need to add these points. The lesson learned is that getting an accurate position of the agent is more important than moving the agent somewhere accurately. As long as you can get the position accurately, it doesn't matter.

That was helpful.

Yeah. Awesome. Looks great.

That's how they got their name. Everything's awesome. That was Tristan's idea.

What you're observing now is its end; it's resetting into the starting position.

Cool.

Oh, wow. Already Hot Sauce is the most likely hypothesis—things that might be Monty's heart. I don't know. Oh, it's neck and neck. And back, neck and neck with what? I can't see. Now Hot Sauce is in a clear lead, but there was Monty's heart as well for a few steps. Monty's what? Oh, Detective Hot Sauce. Good job. That's pretty awesome. Nice. Wow. Let me share my entire screen; that will be better.

Pick another one. Can you do the mug? They already did the mug. Let's do something different. Okay, Spam. We can do something. Yeah, do the Spam. Ours are pretty quick. Hold on. Let me just turn off the— I wanted to share because I wanted also to see. There we go. All right. What's on the— okay. Yeah. Here we go again. It's resetting.

Terry, by the way, the Spam can here is called potted meat can. Really? Full name in the dataset. Okay. No product placement.

By the way, you can see the models in the upper right corner of the visualization. That's all that Monty knows. That's cool. Interesting. That's sparse.

It's between the two visualizers. It keeps saying global matching step three. We didn't debug those logs. Maybe what's happening is the camera is above the object, so it wasn't getting any sensorimotor input and was just bypassing the learning module. Oh, nice. There you go. Boom. What else do you want to identify? How about the Numenta brain? This one is a little different setup. You have the platform. I don't think this one works very well. Do you have the platform?

Yeah. It is the top platform, right? I don't remember. Just put it on the top platform. We have an extra platform for this one because our sensorimotor didn't go far enough to see it on the platform we built.

Presumably, the platform is kind of part of the model. Although, we're not sure if this is the platform we used or if we used a different one. We'll find out. Cool.

Testing robustness. This subject is also very small, but the patch is sometimes just off the object, and for that reason, it doesn't work. Hopefully, it will not fling the brain off the platform either. It's pretty light. We don't have many tolerances built in. A flying brain.

Don't see Monty's brain in hypothesis space. This one might not work. We'll see. Right now, the sensorimotor is above. When you see stuff like this, it's just not getting any data because our policy is just purely random movements.

Also, the time-of-flight sensorimotor works best with shiny objects. Objects that are not metallic don't give good data.

Sorry. Visualization.

I think it's a tuna soup can. This is why—tuna soup can—wait, tomato soup or tuna can? Tomato soup, probably. Okay. You got an example of a failure mode. That's not bad for three. Awesome. Do we get a second try on the path? What if we get the brain? No, it's actually pretty good about the brain. We just put it on the bottom, right? Yeah, just normally. The heart, sorry. It's pretty good at recognizing Monty's heart, and you can see the image of its model of the heart. That's pretty cool. Do you want to try the Spam can again? Should we try one more? Hopefully, we have a little bit of success. Sounds good. I'll stop sharing as soon as this completes. In Monty, when you rotate, is it moving the agent around the circle? Yes, we are faking it—orbiting an object.

There we go. Monty's heart. Monty heart.