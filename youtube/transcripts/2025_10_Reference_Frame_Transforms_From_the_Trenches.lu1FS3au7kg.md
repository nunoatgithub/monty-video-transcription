Scott Knudstrup: Alright, I'll give it a shot. a big topic, and Has a lot of interesting, tangents you can go on, no pun, I don't do those, I guess I'll kick it off, and we'll see how far we get.

let's see here... Share... I'm gonna present our view.

Niels Leadholm: Nice, I like the name.

Just all of... all of space.

Scott Knudstrup: Yeah. Okay, so let's go on... go ahead and... yeah, I didn't know what to call this thing, so spatial it is. I figured we could kick off by just talking about these sort of de facto conventions that are in Monty, and, some explicit, some implicit, and I think we can all probably agree it'd be better to be explicit about all the conventions that happen to be in play. That involves Cartesian coordinate, conventions, spherical coordinate conventions. Rotations... I'm sure everybody is aware that we have a lot of different ways of representing rotations, and I don't really have a lot prepared for that, but, obviously, the more we... the more we can do to try to, eliminated consistencies, and maybe one day abolish the scalar last quaternion from our codebase. Not that I'm taking a side on scalar first versus scalar last, but, if we're gonna pick one, let's just, let's just try to stick with it.

And, talk a little bit about... Transformations? Which are stable, so long as we agree on the conventions.

and a little bit about, reference frames, and a couple examples involving the Dyson agent and, targeting, finding the right actions to, position the Dyson agent to look at something. And let's just jump right into it. First off, There's a lot of different... A lot of different ways that you could, decide which ones are X, Y, and Z of these three axes. here I'm going to be using red for X. And green for, Y, and blue for Z. Z for blue, for Z. So this is our convention here.

Where we've got... you gotta imagine that this is, an agent or a sensor that's facing the mug. pointing to the right of us is the x-axis. The y-axis is pointing straight up. And the, z-axis is pointing behind us. This was a bit confusing to me when I, first came to the project, because who has, who has a negative axis of 24? It just seems very strange. It has the advantage, though, of... leaving the plane that you're seeing, like this, looking like normal, where you've got X going to the right and Y going up, and if you want to have a right-handed coordinate system. Which has... Benefits, and it's best to try to stay within them. You're going to, then there's only one direction for Z to go. You can't have a right-hand coordinate system with having right X to the right, Y up, and then Z forward. That would be a left-handed coordinate system.

Niels Leadholm: So... hang on, in the right-handed coordinate system... Which one is which?

Scott Knudstrup: a right-handed coordinate system means.

Hojae Lee: Your thumb is the X, your index is Y, and where you curl is where the Z should be. So if you put your thumb to the red. Green to the... index to the green.

Niels Leadholm: Yeah.

Hojae Lee: It tells you where the blue should be, which is the word, which makes sense.

Niels Leadholm: And I guess that makes sense, because it's pointing towards... if I held this at my head, then the Z is pointing back.

Hojae Lee: Yeah.

Niels Leadholm: That does seem to be the same. Yeah. Okay, cool.

Viviane Clay: Depends on how you rotate your hand,

Hojae Lee: Also, I should say that we must follow the right-hand rule, otherwise everything breaks. that's not a brick rule that we can break, I don't think.

Scott Knudstrup: Yeah, I... I'm not a physicist, it comes up in physics a lot, go talk to a physicist about electromagnetism or something, and they'll have things to say about the right-hand rule. All I remember is that, you can wrap your hand around, and that's the direction of mag... yeah, I didn't, I didn't really understand it at a... A deeper level of what it's like. Or what its importance is in, in terms of actual physical reality, but in terms of our, our conventions... The... there's two... nice things to know about right-handed coordinate systems. One is that if you're ever... Trying to remember which way positive rotation is about an axis. let's say I'm going to rotate around the X-axis here. just point your... imagine you're facing straight down it, so you're over here somewhere. I don't know if you can see my cursor... no, you can't see my cursor, but imagine you're off to the left of the screen, staring straight down the positive...

Viviane Clay: I can see your cursor.

Scott Knudstrup: What's that?

Viviane Clay: We can see your cursor.

Scott Knudstrup: So you can. Okay, so we're here, we're staring straight down. Then the remaining two axes are gonna be spinning counterclockwise.

So that's a feature of right-handed coordinate systems.

Viviane Clay: counterclockwise is positive rotation, and counterclockwise is negative.

Scott Knudstrup: Yep.

Viviane Clay: Yeah, so no matter which...

Scott Knudstrup: So if you want to know for example, you're trying to... remember, oh, which way is yaw? If I say yaw 10 degrees, am I gonna... and I'm facing this cup, is that gonna spin me this way, or is that gonna spin me that way? Part of me thinks it's gonna spin that way, because I'm just thinking, oh, it's yaw, and X is that way, right? X is positive over there, so I'm gonna positive spin, but no, it's not that way. You, stare down this Y-axis. Just mentally imagine it, then, These guys go counterclockwise in this direction, so positive yaw is spinning that way. Nope. Ramy: I do it is I just point my thumb in the direction of the axis, and then I just curl my fingers, that's the way the others.

Scott Knudstrup: everybody's got their way. I... that was the way that's, a lot of people use, and for some reason, I just, play with my hands and never quite... it just never really clicked for me, but thinking about staring down the axis, and then imagining the counterclockwise motion, that's what clicked for me, or at least helps me make sense of it.

Tristan Slominski: Disturbed your thumb. Down the axis, and then...

Scott Knudstrup: Yeah, I'm sorry, I clicked through my thumbnail. Alright, so the other thing to be aware of is that rotations are... this is just an interesting fact of three-dimensional space. They can be broken into two, two subgroups. There's left-handed rotations and right-handed ones, and you can't rotate a right-handed coordinate frame into being a left-handed one in the same way that you can't rotate your hands. I can't take a... so if you see... If you're struggling to make two images look the same. through rotation only, that means there's a good chance that, either your controls are bad, which is common in, programs for trying to get things to rotate properly, or there's a reflection of some sort. And, meaning They're opposite-handed.

here's some other common conventions. We have X... X to the left here, Y forward, Z up, I think this is Matplotlib, it's also Blender. So if you ever try to go plot stuff in Matplotlib, and it looks like this... Or, everything looks spun by 90 degrees. It's because it's in this coordinate system, and You can imagine rotating, taking this x-axis here, rotating this green guy, Towards the blue guy. And then we would have that. you can transform between map PlotLib data and Monty data through one rotation about the x-axis by 90 degrees. Here's another one. This is in, I guess this one's common in, flight?

Which is interesting, but... Point is... whether in, for example, Mujoko has a different, coordinate, 3D axes, convention, so any data that comes and goes from Mojoko is going to have to do the, corresponding transformation, or else things in Monty aren't going to work. We just have these assumptions built in, and they are due to habitat. which uses the OpenGL, very common 3D graphics convention, which is this one. So it's just some sort of something to keep in mind. Anytime you're interfacing Monty with any other kind of visualization tool or simulation tool, you just have to be, This is probably the first question you should ask yourself. Okay.

Any further thoughts on that, or... Go ahead.

Hojae Lee: Yeah, the rightyan rule is mathematically important. It's important because any rotation matrix, besides all the vectors having to be orthonormal, that the determinant has to be... if they're orthonormal, the determinant can be either plus 1 or minus 1, right?

Scott Knudstrup: Yeah.

Hojae Lee: Just linear algebra-wise. The right-hand rule specifies that the rotation matrix has a determinant of 1, so if you constructed a rotation matrix, you have a quaternion, and then put it to psi pi, as matrix, it will create a rotation matrix. with determined plus one, Unless you want to give up that and... Define everything in left hand, which means not using any of those conversions. yeah, just saying the importance of,

Tristan Slominski: we must follow the right-hand rule. It's not impossible, right? Unity uses left-handed coordinate system, and it's a pretty successful simulation engine. So it's just a headache of conventions. But they're also the odd child out, as far as I understand, for the most part. But this doesn't make it impossible, it just makes it...

Hojae Lee: You have to transform more. Yeah.

Niels Leadholm: And, I was curious, yeah, Scott, is... let's say we're working with some new tool, and it could be, yeah, a new simulation, but it could also maybe be something like... Yeah, I don't know, the VR, setup that was... tracking the coordinate of the tracker. Is there a systematic way that we can determine this if they haven't documented it well?

Scott Knudstrup: Yeah,

Niels Leadholm: I feel like the closest thing is, which I think is what we did in Crete, is,

Viviane Clay: between...

Niels Leadholm: Take the tracker and move it through space.

Scott Knudstrup: Yeah.

Niels Leadholm: okay, that's... that's doing Discord, axis, and this one is... that's okay, so Z is positive along that axis. that's basically what we ended up doing, but I don't know if there's something more elegant or foolproof.

Scott Knudstrup: Yeah, oh, no, that's, let me see if I can just pull up the, ExcalDraw really quickly.

Viviane Clay: I remember Niels, you were sitting in front of the... Screen, and just moving your hand in space.

Scott Knudstrup: that's exactly...

Niels Leadholm: Using sensory motor... Yeah. it's,

Scott Knudstrup: Exactly what all this stuff means, is that... If I can move... One... unit in some... who knows what that is? Reference for, coordinate system. And that ends up being, 100, and Monty. them... You know that, X with respect to... Whatever weird coordinate frame you've got.

That corresponds to... X hat. Let's call it X hat. And Monty?

And... just do this for each of the three dimensions, and you'll exactly get...

Niels Leadholm: map it out.

Scott Knudstrup: if you've got some rotation matrix, That goes from... B... DeManti?

These are the... that's the basis vector of B. With respect to Monty, that's the second basis. Vector of, I don't know. System B with respect to Monty, and that's just the definition here. So this is... this is exactly what you want to do, you just want to probe in each, axis to, Yeah.

Niels Leadholm: Okay, cool.

Hojae Lee: so in Monty, our Euler angles are in XYZ. Is that...

Scott Knudstrup: Oh, boy.

Hojae Lee: following, or... Okay, I know, okay. Okay, let's... I'll just wait, alright, let's continue.

Scott Knudstrup: let's go to... blunt.

Yeah, and sometimes you'll find stuff well-documented for these things, but you can always kind of figure it out the way that Nils is suggesting.

I do have a script that will convert between arbitrary, you tell it right up, down, write for, and I wanted to see if I could get into, a git gist or something before... before, this, but, I didn't. But I'll get... I'll put stuff, little utilities like that somewhere, so you can play with, and sometimes I'll use that. I'll say, RFU to RUB, and it'll give me a transformation matrix, meaning right forward up to, right up back or something, and it just, spits it out for you. This is gonna be handy when you want to rotate back and forth. Between, different, conventions. Alright, here's another one that's, That's, interesting. Spherical coordinates, they come up a lot when you're dealing with camera stuff. Or when you have to issue commands, say, yaw left by a certain number of degrees, or you're looking at some point in some sensor data, and you're trying to find the associated spherical coordinates for that point.

So there's a couple ways to decide to define what these angles are going to be. There's two of them. There's an azimuthal angle, Rotation about the y-axis, basically, so like this. And there's a elevation, or a polar angle, which is like this.

probably the way most of us learned it is in the sort of math-y, physics-y way. Actually, math and physics don't exactly have the same convention, but...

Niels Leadholm: For, sake of discussion, I'll just say this one down here.

Scott Knudstrup: Oops. It's probably the way we learned it, which is where we measure the azimuthal angle, From the x-axis. So if you've got... This is the point in space, by the way. I'm just looking at it as a Muthful coordinate, you go... you measure all the way from the x-axis, like this, and to get its polar coordinate, you measure down from the vertical axis, like this.

It's more common in, say, robotics and things like that to do it the way we do it, which is that since we're staring straight down this, negative axis, this negative z-axis like this, we measure The azimuthal coordinate, away... From the negative z-axis? spinning again in the sort of positive direction. And we measure the, elevation. up from the X to Z plane.

what that really means is that... so this is called the forward aligned zero-angle Axis Convention. That means... the azimuthal coordinate, and the... I'm not gonna say polar coordinate, because that... by context, they usually... that usually means coming down from the vertical axis, unless somebody else has other experience, but that's just from what I can tell. Usually they call it elevation. But down here, 0, in terms of the angles, they're aligned. So essentially, we're... the origin of these two, angles, angular coordinates, is straight down the center here. So that their zeros are aligned. As opposed to the math or physics one, where you've got a zero down this way, your... that's your azimuthal zero is that way, and your polar zero is up that way.

Let's see... yeah, I think that's... About, about all there is. one. But...

Niels Leadholm: Yeah, so I guess that means that in the math and physics one, that they're never Really, both zero. It's like cosine and sine, where, as one grows, the other one... shrinks or something, right? if you were facing in the direction of the red one. than the... what do you call it? Polar 1, or whatever. The one from the top would be non-zero. Whereas in the one that we use in Habitat, they can both be zero at the same time, and that corresponds to looking forward.

Scott Knudstrup: Yeah, I think that's right.

Viviane Clay: But wouldn't it be that if one of them is zero, the other one has no effect?

Niels Leadholm: Has no effect.

Viviane Clay: if you have 0 for the red one, the line is just up, so it doesn't matter how you rotate along the green one.

Niels Leadholm: That's a fair point, yeah.

Scott Knudstrup: rotating around the green one...

Niels Leadholm: I guess it depends on... you could still rotate...

Scott Knudstrup: Coordinate, right?

Viviane Clay: yeah, I'm talking about the math version now. I think in the robotics one, it's different.

Tristan Slominski: 0, 0 is undefined. it's not a point.

Scott Knudstrup: Say it again?

Tristan Slominski: 00 is undefined, it has to be 090.

Niels Leadholm: You can't get to 00.

Scott Knudstrup: Yeah, unless you're in the origin, So the...

Niels Leadholm: Yeah, because I think if you're a 3D object, you could still rotate about the green. Picture. Even if you're, Polar 1 is 0.

Viviane Clay: Yeah, you mean if, the little black dot is some kind of shape? Yeah. It'll rotate around its own axis?

Niels Leadholm: Yeah.

Viviane Clay: Yeah, if we're not just talking... But that's maybe mixing up...

Niels Leadholm: Back season. Points, yeah. Anyways, it doesn't really matter. I guess I was just, yeah, trying to... check my understanding. But yeah, this is a helpful visualization.

Viviane Clay: Sorry, Scott, I think I missed it. If I were to ever Google which convention is used where, what are the terms for these?

Hojae Lee: Forward angle zero... forward a line zero angle axis. That's the valve.

Scott Knudstrup: Borderline Zero Inkl Axis Convention.

Viviane Clay: Okay.

Scott Knudstrup: here's my word of warning about Googling. For, the transformations between the two, specifically, is that, you're just always going to have to do this, game, where you're like, okay, so they call that one the X, they call this one the Y, and, so you're always doing these, internal, substitutions for this axis and that axis. It can get confusing pretty quick. And when you see... if if part of your Googling involves the coordinate transformations between the two, that's where... Both conventions come into play.

the exact form of these, Transformations between the two depends on both conventions.

Niels Leadholm: like a combinatorial... Number of convention flavors.

Scott Knudstrup: Yeah. here they are, moving on.

No, just kidding. Redivide them yourself,

Hojae Lee: Oh, I just realized how... or I just come up with how to, remember the forward align... forward align zero angle. Is that in, forward? So basically, what you consider forward, which in... so we just said that in the first slide. Z is pointing into you, like your thumb, or not your thumb, but... So 4 means positive, like Z, and that's considered zero angle, so if something is looking at it without any rotation, zero angle.

Scott Knudstrup: so Ford is negative.

Hojae Lee: Ford. Yay.

Scott Knudstrup: You said?

Hojae Lee: No, forward, no, forward is positive Z.

Scott Knudstrup: 4 is negative.

Niels Leadholm: Not in Habitat.

Scott Knudstrup: Not Monty.

Niels Leadholm: No, Monty.

Scott Knudstrup: We're looking straight down the negative. So this is our camera here, this is our little camera for this room. We're staring this direction.

Hojae Lee: Oh, yeah, for this new negligence Z, yeah, but... But that angle, that... whatever... basically, whatever direction you're looking at is your rotation.

Scott Knudstrup: Yes, exactly. I think the way I think of it is exactly like that, which, if I'm a camera staring down this axis. Then dead center is 00 for both angles. Which you can just say,

Niels Leadholm: Makes a lot of sense from a robot perspective, whatever. Yeah.

Hojae Lee: Yeah.

Niels Leadholm: Yeah, it's just that it makes a lot of sense from a robot perspective.

Scott Knudstrup: Exactly. Yeah, It's like, how much do I have to rotate left? None. How much do I have to rotate up? None. That's zero.

Okay... Question.

Tristan Slominski: Are you gonna skip this again? Because I was gonna... I had...

Scott Knudstrup: Go ahead. Are you skipping it, or... No, I'm not skipping it. Okay, The access orders is pretty... Straightforward. As in... let's say you have a different, XYZ, you just simply swap out the... the letters. For the most part. And these, if you want to change them.

As long as you remember which one's the vertical axis, which one's the horizontal, and so on. The catch...

Niels Leadholm: as in... I'm sorry, so as in, Cartesian spherical... That first top left one could be rewritten as, right-handed axis squared plus up vector squared plus, backward?

Scott Knudstrup: Yeah. Yeah.

Niels Leadholm: And then just...

Scott Knudstrup: Backward, Whatever you call, this is the nice one.

Niels Leadholm: Yeah, that's the nice one. That's maybe not a good example. I guess the second one, it matters, but yeah.

Scott Knudstrup: Yeah.

Niels Leadholm: but...

Scott Knudstrup: the second one, you'll probably see this one written differently if you look up how to do this conversion, because most texts don't have the negative z-axis as forward. Because we do have the negative z-axis going forward, we have to drop this negative sign in here. And that actually converts us temporarily to left-handed, because it makes the determinant negative 1 by multiplying a coordinate by negative.

Tristan Slominski: Great question.

Scott Knudstrup: Which we then have to undo here.

Tristan Slominski: Question. You said drop the negative sign, and then you pointed that negative Z. What do you mean by drop?

Scott Knudstrup: Drop in, sorry.

Tristan Slominski: Okay, thank you.

Scott Knudstrup: You have to drop it from your stack of negative signs into this equation.

Tristan Slominski: Thank you, appreciate it.

Scott Knudstrup: Yep.

yeah, so that's, one thing to be aware of for this guy here. Trying to get the Azimuthal coordinate, that's a mouthful, Azimuthal. I'm trying to reserve yaw for, an action, like a displacement more than an actual...

Niels Leadholm: like rotation versus orientation. Yeah. Sometimes talked about.

Scott Knudstrup: Yeah.

Niels Leadholm: Thank you.

Scott Knudstrup: Okay, What's this ATAN2 business?

Most of us, I'm sure, have had contact with it at some point or another, but the brief answer is that If you've got a full circle. And let's say you're in this kind of situation, right here. And you're trying to find, this angle, phi. you would do, let's say tangent of phi is X over Z. therefore, phi is the argangent of X over Z. But what about... what happens if this actually is completely... Opposite, so it's in the opposite quadrant.

That would be arctangent of negative X over negative Z. So they cancel.

And things in opposite coordinates will give you the same... value from the regular arctangent function. That's the first sort of issue with it. if we want to recover an angle. From the entire circle. There's this special version called ATAN2. I think it was from the 60s, according to Wikipedia, which I just find funny that they made a sequel to a math function.

They didn't bother naming it anything else, like A10-2. Yeah, even better. instead of... it takes... it's a two-argument function, and it actually looks at the negative and positive signs of the input that you give it, and it assigns the correct, quadrant based on it. That's the first thing it does, and the second thing is, there's no division by zero problems. Because plenty of times, the denominator will be 0. if we're... in this case here. If we're staring straight to the right or straight to the left, we'd have 0 in the denominator. And, A to NT will just tell you, oh, we're... we're straight down this way, so it'll be, like. negative 90 over straight on the right. If the numerator was positive, and if the numerator was negative, and the denominator was 0, we're 90 degrees positive. So that's ATT2.

Niels Leadholm: Thank you, that's a really helpful explanation. That is really weird, that, doesn't seem like a math function, that definitely seems more like a...

Hojae Lee: He's a pupp.

Niels Leadholm: Piece of code.

Hojae Lee: maybe I didn't mention it, but it came up in floppy.

Scott Knudstrup: Oh, yeah.

Hojae Lee: Yeah, because, I think initially I implemented, flops for ATAN, and then I realized we're using ATAN2, So they're slightly... so ATAN2 is quote-unquote superior in a way that the output is, minus pi to pi, so minus 180 to 180, it covers a full circle, while for ATAN, just a normal ATAN, it's, minus 90 to 90. if you just do ATAN of a point that's 11, or that's 45 degrees from the x-axis, right? Counterclockwise, and... but if you do an A10 of minus 1 which is in quantum 3, like you just mentioned, that's also still 45, even though it's technically, 1, 215, right? if you go negative 1, in the XY coordinate system, so it fixes that. with the... yeah, so with the, yeah, A10, because it takes a ratio of the two. 1 over 1 is the same as negative 1 over negative 1.

Scott Knudstrup: yeah.

Niels Leadholm: But yeah, it's just weird. It seems like a lot of, if statements, rather than, A smooth, continuous mapping between to member spaces. I don't,

Scott Knudstrup: Yeah, it's weird. Yeah.

Tristan Slominski: I've...

Hojae Lee: But the printable tip is probably use 82. That's what I'd like to do.

Scott Knudstrup: If you only ever care about magnitudes.

Hojae Lee: then fine. Go ahead and use, ETAN.

Scott Knudstrup: But if you're on a plane. a full plane, a full circle? You want a tan, too.

Hojae Lee: Yep.

Scott Knudstrup: The sequel. Bigger and better. more complete.

Alright, I have these that are ready to get pushed into, Monty, because I just figure these are the ones we should use. This is the exact form we should use, always. unless there's some weird case, if there's some weird case, then you're responsible for it. But otherwise, if you need to, do mappings between Cartesian and spherical coordinates within Monty, within our conventions, these are the forms, so those will go up into, I think, transform utills is where I was gonna put that.

Alright, so then, mapping back from spherical to Cartesian. That does, also happen. And...

Viviane Clay: Just to make it a little bit concrete, so in Monty, where do we use those transformations? Is that when we want to go from Like, where we are in space to translate it to a movement vector off the camera, turning it up and down and left and right, or is that draw pitch...

Scott Knudstrup: The spherical coordinate would tell you basically how much yacht or pitch there is relative to your... 3D reference frame, your RG reference frame, so yeah, if you're...

Viviane Clay: Yeah.

Scott Knudstrup: Trying to figure out... there's a point over there, I'm facing like this. Whatever. like that, as a point over there, then these...

Viviane Clay: Yeah.

Scott Knudstrup: formula will give you...

Viviane Clay: For example, you're using this for the saccade work, you have a salient point over here in your field of view, and now you want to look at it, and so you have the salient point in spherical coordinates. Wait. in Cartesian coordinates, and you want to convert it into spherical so you know how to move the camera?

Scott Knudstrup: Yeah.

Viviane Clay: Okay, cool.

Scott Knudstrup: Exactly, I think I put it down here. Euler angles are mostly necessary when we're dealing with camera data, because there's projective geometry involved. but also the motor system, because we speak to the motor system in terms of angles. We can't just tell it Here's my point in space, we actually have to be explicit about how to get there. with an actuator.

Viviane Clay: the points in the code where we do have to do this, there's...

Scott Knudstrup: the saccade... saccading to targets, there is, Get good view, which is basically the same deal. And then... the... one of the other main areas, I'm just gonna point this out as a counterexample, is I was looking at... I think it's in the voting math, where there's this... there's two rotations, and we need to figure out, orientation between them. It's close, but in that world, you don't have to deal with Euler angles at all. You can just compute the... the rotation that takes you from one system to the other. You can just generate a matrix. And you don't have to deal with the headache of Euler angles. At all, because... Oiler angles are a bit of a headache. When you get them, the first thing you should ask yourself is, what order do I apply these in?

Hojae Lee: Yeah.

Scott Knudstrup: I first rotate around the x-axis, and then the y-axis, and then the z-axis, and the second question is, if I first rotate around let's say the x-axis, so I pitch up a bit. And then I'm going to rotate around the y-axis. Do I rotate around the new Y-axis? Because that's changed now. Or do I rotate around the... sort of... external y-axis, which is, I can demonstrate this in a bit later, but this is the difference between extrinsic and intrinsic. If it's intrinsic, it's you always rotate around the new axis. So I do... I apply the X rotation, and then I apply rotation around the new Y-axis, and so on.

when, for example, we're doing scipi.rotation from Euler, XYZ, and then some coordinates, if they're lowercase xyz, if I'm not mistaken, that's intrinsic. And we applied them in the order XYZ. this is something I didn't get to in this presentation, but... M... any sort of action-related space that we have in Monty right now, you want to be applying Y and then X.

But when it comes to trying to figure out, hey, what was that object's orientation that Habitat was doing? You want to be doing an order XYZ.

And then... and it... and intrinsically. So that's another, just, a trial and error thing. But, yeah, so if you see Euler angles, just... I hope bells go off for you. What order do I apply these in? And is it intrinsic, or is it extrinsic?

That's the...

Viviane Clay: SciPy forces you to specify it, because remember...

Hojae Lee: And whatever I... I don't know about XYZ yet.

Viviane Clay: Yeah. The first time I wrote it, I was like, oh, I don't know what this even means, I just want you to rotate it.

Scott Knudstrup: Yeah.

Viviane Clay: I'm like, oh, okay, yeah, it does matter. Thanks for asking me about this.

Scott Knudstrup: they always say, the order matters and things like that, but it's hard without, good visualization tools to... to internalize, what that means. But I'm gonna pull up, Blender later, and I can... show you guys how to use something like that as a visualization tool for this kind of thing, and make it a bit more obvious. I wish there was some kind of just online thing you could go to that I... just plug in, just play with rotations, that'd be cool, Cool thing, but I couldn't find one.

Niels Leadholm: And...

Hojae Lee: Does that still matter if it's done extrinsically?

Scott Knudstrup: The order of application?

Niels Leadholm: Yeah, I'm guessing it probably still does.

Scott Knudstrup: Yeah.

Hojae Lee: Yes,

Tristan Slominski: Or does it depend on, essentially the affordances of your effectors? It's if you pitch up and your effector can only go intrinsically, versus if you're on a platform and you pitch up and your effector can go like this would be extrinsic, but this would be intrinsic, right?

Scott Knudstrup: Yeah, so that... it was so confusing for me, because I'm so used to thinking about it as if you're, like, an airplane. the idea of why a gimbal lock would be a problem ever took me a while to understand, because I'm just not used to thinking about one actuator that can do one thing. mounted to a thing that... an actuator that can do another thing. I'm used to thinking about just these free-floating, spaceships, basically. They can always yaw around their own axis, and so I was like. So you... so you point up, what's the big deal? it's but, you lose the orthogonality of these,

Hojae Lee: Yeah, can we... is it possible to, talk to the motor system and... not angles, but just... I know you can say, oh, you can't just say, go, look at XYZ, and it will just do that for you. We have to, give it some kind of angle, okay, rotate, yaw, pitch, whatever, in 45 degrees, so that you can actually look at this, but... because... because Euler angles are my... my wish, is, I think I expressed this to you, is, Euler angles only for defining the cube and rotation faces, like the 000, 090, and, the final, human readable output, oh, here's a predicted orientation of the object at the end, but everything inside is just... we just use rotation matrix, and we don't need to worry about intrinsic reactions, because we just need to multiply by rotation matrix.

Scott Knudstrup: So I'm gonna make the case for the opposite, actually.

Hojae Lee: I don't know, open.

Scott Knudstrup: Yeah.

Hojae Lee: To use all the angles everywhere?

Scott Knudstrup: the case that I'm going to make, Unfortunately, I didn't have time to... Put any materials together on this, but... In a simulator, say, or robotics, Let's say you have a joint you can rotate around.

you define... that joint is defined by an axis of rotation and the amount, and that's it.

Hojae Lee: Okay, so there's... okay, so we do need to communicate through a motor system that way.

Scott Knudstrup: Yeah, and even internally, Majoko, for example.

Hojae Lee: Yeah.

Scott Knudstrup: When you issue a change.

Hojae Lee: Yeah.

Scott Knudstrup: all it does is make new joint coordinates. It just... if you say, I want to rotate 10 degrees around, I want this joint to rotate 10 degrees, it just adds 10 degrees to that coordinate. These are your generalized coordinates. It doesn't...

Hojae Lee: Yeah.

Scott Knudstrup: give you a 3D reference frame for each point along that, Got it. Jane, you compute it yourself. Given... the axis of rotation at that joint, and how much. this sort of forward pass, you can recover the full Cartesian reference frame for each node. But internally, it's all represented through just amount. And actually, I think the reason I'm making the case for thinking about it more seriously this way is because I think if we're trying to issue commands, if we're trying to actually learn Commands?

Hojae Lee: Yeah,

Scott Knudstrup: We want to be able to just, learn a parameter, this is how much you need to spin.

Hojae Lee: Yeah.

Tristan Slominski: but I think... I want to talk more about this, because... there's a future Monty, and there's today's Monty, and I don't think today's Monty should be using all their angles inside of it, except for as an output of the motor system. And the reason for that is.

our current learning modules don't have an embodied model at all, and so they just care about a point in space, and for that, we can use matrices or quaternions. when it... and that can be part of the goal state to their motor system. Motor system will then... it's motor system's responsibility to then take that space and figuring out how do I actually act on it, and that's where the conversion can happen, I think. In the future, Monty, and because motor system right now... we're essentially gonna hand it an embodied... what I call embodiment oracle. It's you magically know how your body's put together, and how to translate out in space into Using this embodied oracle that we just told you, this is what you are, how you are put together, and where you are. In the future, Monty, when that embodiment oracle becomes learned inside learning modules, that's when I... that's when maybe we might want to drift away and start doing what you're saying, but I think it would just become too complicated now. none of the learning modules today Have any business learning how to move.

Until we actually go after...

Scott Knudstrup: Agreement.

Viviane Clay: Say again? Okay.

Scott Knudstrup: I'm in 100 agreement on that. I just, I'm just dreaming forward, X number of months or years to when we are learning to control a motor system. I'm thinking, we have to do it in the coordinates of the actuators. And the coordinates of the actuators are angles, amounts, basically, if it's a rotate... rotating cuff. yes, in the time... for the time being, like, until we have, learning components that... learn how to do motor compands, there's no... there's no, reason to do anything in Euler angles or anything like that. What the...

Tristan Slominski: And I'm in your agreement with the future.

Scott Knudstrup: Yeah.

Viviane Clay: Yeah, that's how it is right now, right? goal state generators emit... locations, they don't emit Euler angles, as far as I remember, and learning modules, like hypotheses and all that, are all rotation matrices, so I don't think we are using Euler angles inside Monty right now, except for the human-readable output, like the logging.

Scott Knudstrup: Yeah.

Hojae Lee: Yeah. Yep.

Niels Leadholm: Yeah, and then in terms of the motor outputs, just to clarify, because you're saying two Euler angles, but are the spherical angles Euler angles, or...

Scott Knudstrup: Yes.

Niels Leadholm: Okay, nice.

Scott Knudstrup: Oiler ankles are... An amount of information about a certain accident.

Niels Leadholm: Agreed.

Scott Knudstrup: Yeah, and then here you just have two. Yeah.

Niels Leadholm: Rather than 3.

Scott Knudstrup: And we never use RADIUS. Or we haven't thus far. We're not doing full... Conversions? But, we just... so we just use these two when we, say, do actions, but... Yeah, I think... I think there's also... there's some literature out there about... vector cells and things like that. There's stuff going on in the brain that is... in this space, in this type of representation. And, I'm not an expert on that area. I read a little bit about it maybe a year ago, because I thought, whoa, that's interesting. But yeah, so they're... it's these things are in the brain, and you can make... you can imagine why. If I hear a bang over... over in this direction or anything like that, I only really need to know the... I don't need to know where that is in 3D coordinates, full 3D coordinates, I just need to know how much to move. To get there. Though you could use, the...

Niels Leadholm: the model? Free kind of stuff.

Scott Knudstrup: Yeah, exactly.

Niels Leadholm: It's interesting, because actually, with the insect, path integration talk I saw, they were trying to figure out whether ants, for example, use more, polar versus, Cartesian coordinates. And... and they basically... initially, they were like, oh, it's probably going to be polar, because it's simpler and stuff. But actually, they realized it's probably Cartesian. For various reasons. But I think that fits with, learning modules still being more, Cartesian, and I think this also fits with what you were saying, Tristan, that, within the Larry modules, they just care about points in space. And then, yeah, it's more like motor system, where it's okay, now I need to move this by a certain amount.

Tristan Slominski: I... I don't.

Scott Knudstrup: Yeah, sorry, go ahead.

Tristan Slominski: I do have a question about the... because you said a specific phrase. I just need to know how far to move at this angle, or whatnot. Are you sure it's how far to move, and it's not how much force to apply over how much time?

Scott Knudstrup: Yes. No, I'm not sure of anything, I just had an early game.

Tristan Slominski: But I just want to throw that in, right?

Scott Knudstrup: Yeah.

Tristan Slominski: It might not be communicated and move this many angles, it might be communicated as, flex this muscle this fast.

Scott Knudstrup: Yeah. It could be anywhere along that, I think ultimately it's going to be...

Niels Leadholm: That's probably, the final step in it, and that's probably why, if you think something's heavy, and you go to pick it up, then it's oh, your arm flies up, because you apply... a large forest or whatever, but But I guess what was informing that muscle contraction is probably something like, oh, I want to move my arm by this amount.

Scott Knudstrup: Yeah.

I think we've danced around this, argument a little bit. I'm always willing to entertain the idea that there's more polar happening than there... than... than we might expect, but I'm open to it, I don't really know, like... because when I think about situations where the depth is ambiguous, or unknown. Or even just on a flat plane, like I'm watching TV or something. I don't... have a sense of what the depth is. I'm not computing, or it's, something that's hundreds of meters away. It's I'm really just saccading between two points. I've got... they might as well be of infinite distance, or, or they could be close, but I can still saccade to them, because... all I need to know is the angular distension between them. So I think there are cases where it seems... this seems like there's strong cases sometimes for more polar representation when it comes to Cases like that, but, it's debatable.

Yeah, anyway. I... yeah, we all... we also did... I brought this up at the Focus Week, and you said, yeah, you could make... you could actually just adjust your saccade amounts based on an expect... The distance from you to that billboard, but... It feels like you're asking a lot of your depth your ability to compute depth. Especially on the fly. If you're trying to do all of your, eye motions In Cartesian coordinates, especially when V1 and the collicular surface is basically sitting there in... Angular coordinates... spiritual coordinates, more or less. So it feels, very easy to extract. If you need to do a real quick motor command from here to here, it's already in that... It's already in those coordinates, basically.

Viviane Clay: It seems like maybe the kind of more subquartical parts, like the sensor module and the motor system. can do spherical coordinates. Like, when you're doing saccardic to something salient over here, I agree with you, you probably don't have a very accurate depth estimate of that, and you probably don't need that to calculate how to move there. you don't need to go through Cartesian space, but that's more like a model-free movement that would be based only on sensor module information. Yeah. But then once you go to model-based movements, based on, actual structured models you learned. as in the learning modules, I would say it's probably gonna be Cartesian-based.

Scott Knudstrup: Yeah.

Hojae Lee: Yeah. Or I guess this might be a case where even if it, turns out some biologist found out that it's spherical, we might... Still stick to, matrices, base... Rotation in the learning module, just so for... computational benefits. Possibly. Damn. Yeah. but yeah, okay, yeah. I think I'll... I'm convinced, but yeah, and I think I didn't come to this kind of same conclusion, because I didn't work with the motor system yet. I'm still... I think I'm the last one, maybe, I don't know. I remember when you started this keyboard, it's I don't know anything about the motor system, and now you're the expert, and I'm still, I still don't know about the motor system, so maybe after my 2D sensor module.

Scott Knudstrup: Yeah, and hopefully, just submitting the... these transforms to Monty will make the process.

Hojae Lee: Yeah.

Scott Knudstrup: so you don't have to... Think this through every time.

Hojae Lee: I guess my ideal world is that there's no body, and our agent is just an infinitely small point, and, you can tell it to look at any XYZ, and it'll just do it.

Scott Knudstrup: Yeah.

Hojae Lee: But then it's that's very non-real world. Yeah. Yeah, anyway.

Scott Knudstrup: Oh, before I forget, I did want to say that the azimuthal angle is defined between... Jose mentioned this before, between, negative 1... negative 180... And... Positive 180. So you get the full circle? But the polar coordinate, that's just straight down to straight up. So you've got 90 degrees there. If you tip past...

Hojae Lee: Oh, yeah.

Scott Knudstrup: That's actually equivalent to as if you had done a 180 in yaw. Plus, a little bit in the opposite direction of puller, just something to keep in mind.

Hojae Lee: I think you just triggered, a calculus memory from high school. I just got a flashback.

Scott Knudstrup: You're welcome.

Hojae Lee: Yeah, thank you.

Scott Knudstrup: Okay, so here's something that was... do you have time for it? So this puzzled me. If you compute... phi here, this azimuthal coordinate, you only need X and Z. You can just look straight down from the plane. But when you want to compute the polar. angle, or I said I wasn't gonna say polar, but, elevation. You need to get... X and Z... involved. You need to get all three involved. So I think... okay, so my first mistake was just thinking you could do the same projection for the polar angle. why not? Just project this... What's special about... pitch, We live in a... in a world where, no one direction is, privileged over any other. why... what's special about... about the... About this, and so this is a bit of a mystery for me, but hopefully I can, clarify, maybe it makes... maybe it's completely intuitive for you, but for me, it was like... it... it...

Niels Leadholm: yeah, is it not just like the reason you were just describing, that there's a... The way the coordinate system is defined is... Is privileged for one of the... As in, if you tip backwards, then you're gonna start reverting to another... is it... or is it, related to that?

Scott Knudstrup: yeah, I hadn't thought about that, but yeah. It is basically,

Niels Leadholm: So one of them tasks that... Here's how I'm thinking of it.

Scott Knudstrup: This extraction maintains... like... Ortho... Orthogonality, in a sense.

Otherwise, These two things... can... Be non-independent.

When you, perform an action. So again, this kind of comes back to... we are in a... we're in a situation where we are... We have to... decide in advance we're gonna be performing a motion in a sequence. These are Euler angles. We have to... we have to think about the order in which we do things. when you do a... command, We're actually rotating our... polar plane. We're trying to get that dot onto this sort of meridian.

Niels Leadholm: Sorry, just to clarify, what is what? So the dot is...

Scott Knudstrup: So the DAW is the target we want to look at, for example.

Niels Leadholm: And the direction we're pointing in is the dashed line.

Scott Knudstrup: Yes. we need to... When we yaw, we're rotating that hole This... this vertical plane here, that's our... plane that we're gonna be moving our up-down guy in, our sensor, module, or whatever.

If you just project onto the... the YX plane to try to get that pitch amount. You're not taking into account the fact that Yang is going to change what that axis is.

This version of... The elevation coordinate? It's independent of Yah.

Niels Leadholm: As in, if you... if you perform a yaw, and then do this one... You're good. you're good, yeah.

Scott Knudstrup: Yeah.

Hojae Lee: Otherwise, what you'd have to do is...

Scott Knudstrup: Do this first yaw motion.

stop, take another measurement, now look... now compute the polar angle in the... in the really simple way, which is just project it onto the YX plane, and do the... do the motion. That's what... that's what would...

Niels Leadholm: That makes sense, yeah.

Scott Knudstrup: Yeah.

Hojae Lee: There.

Scott Knudstrup: Okay.

Let's play that out again, I can't waste... I can't have wasted having to learn how to do that in Blender. Okay. Yeah, I don't know.

Viviane Clay: animation.

Niels Leadholm: Yeah, really nice.

Viviane Clay: so do you... you always, you are first and then pitch?

Scott Knudstrup: Yes.

Viviane Clay: Okay, and if you did it in a reverse order, you'd get a different result,

Scott Knudstrup: if you did it in reverse order, you'd have to... Compute those angles differently.

You'd have to basically...

Viviane Clay: Yeah.

Scott Knudstrup: Flip the way that you do that,

Viviane Clay: Yeah, okay.

Scott Knudstrup: Yeah.

Niels Leadholm: Life would be terrible if we had to always, move like this.

Scott Knudstrup: Yeah, it's so much easier... In a way, to, here's a fun fact about rotations. Is there any... rotation like this, any Euler, series of Euler angles, you can do... That whole series of rotations?

there is an axis in space somewhere, a single axis, and a rotation amount that will get your reference frame from the original one to this one. So if we just magically had an actuator that happened to have that axis moving along that direction. then it would be easy. We would just say, okay, spin by that much, but we don't have actuators in every axis, in every direction, so we do have to, we do have to, Work within the confines that we have. For the, rotational axis that we do have. But that is a cool, fact about rotations.

I'll leave the exercise to the reader, to work out exactly how that works. Okay, so I figured we could give this a shot. And I'm gonna pull up... Blender.

And let's try this.

Viviane Clay: Which current convention does Blender use, by the way?

Scott Knudstrup: Coordinated convention is Z up. Next to the right.

Actually, can you tell me how small all this stuff is? can you see? This little widget up the top?

Hojae Lee: Yeah.

Viviane Clay: Yep.

Scott Knudstrup: Okay. If it's helpful, I can turn on... Axies to try to...

Viviane Clay: Remember where we are.

Scott Knudstrup: But... for... For the time being, I want to try to forget about that, just for the purposes of this little demonstration here.

Here's my little... To the... to a degree of freedom gimbal. Which is what the system is called, where you've got rotating... thing, a yang thing, and then mounted on top of that, you've got an actuator that moves in another direction. It's called, two degree of freedom gimbal, or a free gimbal sometimes.

You can't really tell right now, because these things are right on top of each other, and they're co-aligned. But... if I grab this sensor real quick, and... Pitch it, like that. you can see that these are starting to come apart. I've encoded sensor stuff in red.

And including this, ray here. That's pointing out it's a sort of targeting array that's in red for the sensor. And in black, here. is, the agent. So this is the agent's reference frame, and this is what he's pointing towards, exactly. And... This sideways one, that's our x-axis, they're always co-aligned. it looks black, but that's just because alpha blending is, The reason it looks grainy is because... of alpha blending, it just, looks a little bit funny, when you're trying to render it live like this. Alright, so I'm gonna reset.

Alright, our first goal... oh, and this, box here, I'm gonna get rid of it in a second, but that is our camera. I've mounted a camera onto the sensor, so we can actually go ahead and see what the sensor is seeing. Alright, so let's go ahead and simulate having to do this process. So I'm gonna go... determine what our yaw angle ought to be to get to that guy first, and then we're gonna try to get to that guy. But first, I'm gonna go into this top-down view here. And I'm gonna... in lieu of doing, trigonometry, I'm just going to... Grab my sensor here, and say. How much would my sensor have to yaw? In order to get to that. Okay, seems like about 30 degrees. Alright, great. Now, what if I were... Boop. Sorry?

What if I were over here? If I can't just do this. And try to figure out how much we'd have to pitch the sensor.

Okay, looks like...

Viviane Clay: Oops.

Niels Leadholm: Wait, was that the right one?

Scott Knudstrup: I'm sorry, yeah, sorry, you're right. I was like, shoot, did my demo change? Okay. Supposed to be about 40... 45 degrees, something like that.

Yeah, shoot, it was supposed to be 45. Alright, but this demo will work anyway. It's okay. Alright, so let's go ahead and execute that, now that we've computed it. So I'm gonna... Go ahead and yaw. this thing, I'm gonna yaw the agent, because the agent yaws. I am the agent who yaws. I'm teaching who you are.

Tristan Slominski: I got it.

Scott Knudstrup: So we're gonna go 30 degrees in this direction. And... and then we're gonna go ahead and pitch up. the sensor, I'm gonna grab my sensor. And pitch it up.

Bye... Alright, let me just go into camera view here. See how we're doing.

Pretty good, 45 degrees. Alright. We're right in the center there.

There's a little red dot from my targeter, but it's, it's dead on in the center, alright? all good, right? I guess maybe the quick... the quickest thing to demo here would be actually just to show Heh, that if I do this in reverse order.

Just gonna go ahead... Reset everything? So now I'm gonna... I'm going to pitch the agent first. By 45 degrees.

And then I'm going to swivel... the... Agent by... oop, wrong direction... 30. And if I look at the sensor, It should be slightly different.

Oh, no, it's not. Okay. Oh, okay, forget it. Oh, because they were coal lines to begin with, never mind, that matters more for the second pass. But anyway, alright, so now, we need to...

Tristan Slominski: The yaw was extrinsic, right? Agent never pitched with the pitch, that's why. yeah. Okay, but an extrinsic should work.

Scott Knudstrup: So now... but now we're no longer aligned. So if I try to do... I've got my sensor. And I've got its camera data. And I'm gonna try to figure out how much I need to pitch in y'all to get over to the second target. So I'm gonna try to simulate what we just did there. I'm gonna try to get a good... exact, Orthogonal projection of what the sensor is seeing. A bit tricky, but I'm trying to get that... Z-axis, straight on. Say, how much... Would my sensor have to yaw? I'm doing this the wrong way, by the way, on purpose. How much would my sensor have to yaw in order to... Get over to that point. To hit that thing.

It's 90 degrees. That's how much more sensor it would have to go, huh?

Tristan Slominski: You said you're doing it wrong. Are you saying you're yoing the sensor instead of the agent?

Scott Knudstrup: Yes, okay, got it, thank you. Trying to show what a mistake that could be made here. Alright, okay, I go, okay, great, 90 degrees would get me there. I'm gonna reset that. How much would my sensor have to pitch?

I'm gonna try to get... Exactly... dead on like that. Oh, it looks like I don't have to pitch at all. I'm already, right on target. Great. So if I just tell my agent to yaw 90 degrees. And I don't pitch at all.

it's, just go ahead and see what happens. Tell my agent. go, what did I say, 90 degrees? So we gotta go up to positive 60.

What's about here? We're way off. Okay? So this is why it's important that when you're computing the yaw amounts and pitch amounts, but particular, yaw amounts and stuff, you have to do it in the agent's reference frame. But then, and say, how much would the agent pitch? To get to this.

And then subtract the amount that I'm currently pitched at. Which is one of the reasons why it would actually be nice to have an internal memory of what the current joint angle is. Instead of having to recompute what the current agent pitch is, or sensor pitch, you just already have access to it, but that's another, Come another story.

Niels Leadholm: I guess is part of this inherent to the 2 Degrees of Freedom gimbal? Because I guess if you had a sensor that could yaw, then you could just do that.

Scott Knudstrup: Yeah.

Hojae Lee: Yeah, I was gonna ask, is it habitat where... or, like, where our sensor is attached to our agent in this 2DOF way, or can we make it, a ball and socket joint?

Scott Knudstrup: I don't think there's anything preventing us from doing that, but all the commands that are being issued for all this stuff within the codebase are all turn left, which is an agent yaw, turn left, turn right, and look up, look down. And those are sensor commands.

Hojae Lee: Okay.

Scott Knudstrup: to my knowledge, maybe it is... I'm not familiar with the way Habitat is... simulators, configured, so maybe... Can actually yaw independently on their own? But this is the... this is when I realized something was wrong with my understanding of Monty, and probably, geometry. So I was like, what is going on here? But I could not shake. the idea that an agent ought to be able to yaw along its own axes like this. That it actually had... or sorry, that the sensor would be able to continue using its own rotational so when I was trying to compute coordinates, They're usually not this extreme. But there would be... the targeting would be.

Hojae Lee: Yeah.

Scott Knudstrup: And it was because of this issue of trying to compute the amount of yaw it's natural, because the data you get comes from the sensor. It's in the sensor's reference frame. it ends up being in the world reference frame, but then you have to, forward map it into the sensor's reference frame to figure out how much to yaw. And then, so you go, oh crap, there's this mismatch. What exactly is going on here? And the issue is, you need to be thinking about how much to yaw. In the, agent's reference frame.

Hojae Lee: Yeah.

Scott Knudstrup: And, in terms of pitching. you could do that in the agent's reference frame, but you need to, obviously account for what the pitch currently is for the sensor. you ought to be able to do it just from the sensor's reference frame, and I do it in here just fine. I could, do it in the... do agent yaw in the agent's reference frame. and do sensor pitch in the sensor's reference frame, I tried it, and it was fine, but when I did it in Habitat, or in Monty, there's, slight differences, and, I'm still not really sure what's going on there, or... or if I made a mistake, because it's so easy to make little mistakes. You miss a sign or whatever, but.

Hojae Lee: Yeah, it's really...

Niels Leadholm: Nice with this visualization and intuitive, but I can totally see how this would be a pain to debug if, yeah.

Hojae Lee: Yeah, so theoretically, if the joint type is not 2 degrees of freedom, but 3 degrees of freedom, we would worry less about this, right? It depends on, the robot that we get, but I think a lot of our joints are... I'm just, trying to do weird joint things now.

Niels Leadholm: certainly eyeballs are more of a ball and socket than a... yeah. I'm assuming... I don't know if there's some weird... yeah, just some historical thing of when Habitat was implemented, because... or, the interface, because I'm sure we can do look left and look right, rather than turn left and turn right, i.e. sensor, if we wanted to.

Scott Knudstrup: Yeah.

Tristan Slominski: So here's another thing I want to pitch around this, right? Because this is just a historical path that got us here. But when I was thinking about, like, how would I do this from scratch or whatever, there would be just a single position action, and it just sets the entire pose in space, and that's it. And my question is, We just said... This is all very valuable for embodied... motor system, to Jose's point. We are in a simulator. everything, all our experiments... what are we trying to do today with Monty, right? Are we trying to control a body, or are we still trying to figure out how learning modules ought to work? And the reason I'm posing that is because we can probably substitute everything to be a single action, which is position 3D, and we give it where it needs to be and what pose it's in, and it just goes there. We don't need to do yaw, turn left, turn right, turn everything else. We can just say, just appear in this position. In a simulated environment, that might be enough for all the near-term experiments we want to do. And then we can tackle this when we wanna... Work with embodied things.

Scott Knudstrup: So I want to make 3 points really quickly. First is, we did a robotics hackathon. We are attempting to occasionally, do stuff in the real world. I don't know, maybe it makes sense to... to... I'm not pushing back, this is just, a sort of counter-argument. while we're trying to learn as much as we can, and develop as much as we can, and Fundamental research area. If we are going to try to validate or, get engagement in the robotics world somewhat, then maybe it's worth keeping in the back of the mind, and not... But... And in support of your point, the surface agent doesn't care about any of this stuff. It does set agent pose. It's just... it just does warp. It warps to where it needs to be. And... it's certainly...

Niels Leadholm: The, goal state does that, the jump to goal state.

Scott Knudstrup: Yeah. But the surface agent doesn't warp.

Niels Leadholm: It does, a complex four-step trig-based thing.

Scott Knudstrup: Oh, it does?

Niels Leadholm: Yeah.

That's at least my understanding. It basically does this thing where it looks at the next surface normal. Does... calculates what, rotation it needs to do to face that, and then shifts along a tangent, and all this kind of stuff.

Scott Knudstrup: Sorry, yeah, I should have clarified. It was when it's trying to execute a goal state.

Niels Leadholm: That's when the service agent.

Scott Knudstrup: Yeah, the jump to Gold State is exactly...

Niels Leadholm: what you're describing, Tristan, we were just like, we want to see what effect this has on learning modules, we don't care how it's achieving that. we're just gonna set the pose.

Scott Knudstrup: And I think if we had to work out all the kinematics of getting the finger to that point, that wouldn't... that wouldn't have been a productive use of time, for trying to figure out, I'm in agreement on that side. But I would just say, Having to think about this, I think ultimately was a good thing for me, personally.

Hojae Lee: Yeah.

Niels Leadholm: This is how hazing starts, Scott. You're like...

Scott Knudstrup: I don't know.

Niels Leadholm: I had to go through this, so everyone else should have to go through this.

Scott Knudstrup: I think it did help me think, have a longer-term view of what I think A motor system might look like that can learn.

I think people ought to be able to do anything they want within Monty with just warping. setting the Asian pose, sensor pose, yeah. As a totally, almost like a disembodied thing, like a point... a being of pure light that can just, you know, But at the same time, maybe there's some value to occasionally having to think about what contact with physical mechanisms is like. But that's more of, a personal matter than, an argument about...

Hojae Lee: with the whole, oh, I've been thinking of, I didn't give any credit to Embody, and I just think of Monty as this one-point thing that's, that you can give a position XYZ to them. that's the ideal, but technically, I guess if we think about, two sensor modules, or, more. then I don't want them to be, like, two separate things that just... they're together, they're... they must be connected to, an agent, or a couple agents, and there must be some relationship between... let's say one agent, and we have two sensors, I guess the easiest would be if, again, the joint is a ball and socket, 3 degrees of freedom, so things can be independent, but... In that sense, there is some sense of bodiness when we, like, when I think about more than one sensor module. At least I'm... at least I'm thinking about, like, how they are Related to each other in some sense. And probably, in real life, we probably don't want, things to be crashing, but I'm not gonna worry about that now.

Niels Leadholm: Yeah, and for what it's worth, we do already, even with our being of light, have issues with the jump to goal state, where it can appear inside of objects and stuff like that, and so there's some very crude... Code to try and deal with that situation. But, I guess the advantage of, Not just setting a pose is that you tend to do it as... more incrementally. And I think it does force us to think a little bit more about policies, but... Yeah. I don't know, I think it's a balance, and I think we've been... treading a reasonable balance so far, because I think you're right, Scott, there are advantages to thinking through these things, and it makes it easier if we actually want to do things like robotics and stuff like that, that it's not, the first time we've Ever.

Scott Knudstrup: had to do small continuous movements.

Niels Leadholm: But... yeah. We had the exact thought when we wanted to add the goal state thing, that it's we don't want to try and figure out how to get a surface agent to, move across the surface. that's gonna be super complex.

Hojae Lee: Is that what I'm supposed to be doing for two decayser modules?

It's gonna be super complex. It's related.

Niels Leadholm: In a local neighborhood, but at least you don't have to, move to the other side of a 3D.

Tristan Slominski: another argument... For it is also, For doing the teleport and the simulator until we actually focus on robotics is that robotics, it's not gonna... Disregard. I don't have a clear thought yet.

Niels Leadholm: I don't know if this is what you were thinking, but, I think there are a lot of these things that we wouldn't necessarily want to compute or even implement ourselves. inverse kinematics is, a huge field. There's also, reinforcement learning, neural network-based methods to move systems based on... so we could imagine Monty as, again, the cortex, and then all these other systems, whether it's evolution or... Boston Dynamics, or someone else that's implemented it. We just leverage that, and then it figures out how to actually move

Scott Knudstrup: Yeah.

Hojae Lee: Yeah, maybe 2 years later, once we figure out the cortex, we'll just hire a roboticist, and he or she can help.

Tristan Slominski: I guess I'm just discounting... The research effort on... Non-learning module learned embodiments.

this will all, I think all this is extremely relevant when we... commit to learning modules now, figure out how to model the body. But before that, it just seems, just dipping the toes in. But... but it just... it just feels like a friction. At any step before that. With the idea that when learning modules just say you need to appear here, any code between that makes that happen is just an expense that will need to, one, go away when learning modules learn the body, and two.

if we're in a simulator, Who cares?

Scott Knudstrup: Here's... here's another pitch, another angle, to think about, is... Warping?

Pretends like time isn't continuous. And we would eventually like Monty to figure out how to live in a continuous time world, and that involves... A lot of sensory input on the way towards accomplishing that goal state. Sensory input, which we may want to, I don't know, maybe we want to, cut down on what happens in the learning module, maybe not, there's going to be a lot of issues in terms of how learning modules function during the execution of motion and things like that in the continuous time world, where I think that's... And, Involves time, I think these things are fundamental to the brain. And even though the kinematic control maybe is something we can put off. the actual mechanisms that we use to position joints and things like that. Figuring out how to... have Monty behave in a continuous streaming sort of world where we don't warp. I think that actually is a non-artificial, And actually, a fundamental....

Tristan Slominski: Yeah, but I think... I think my challenge to that is, I think you're imagining warping as somehow just going huge distances for no reason. All I'm saying is, you can trace a path just by setting set post, and you can get everything you just said, just without worrying about how... move right, tangent, you're up, and whatever, I'd just be like, here, So I'm not advocating for ignore continuous motion. What I'm advocating for, if you're gonna do continuous motion, just... just say I'm on this path that I magically calculated, because I can.

Scott Knudstrup: Yeah, I'm... I'm good with that. I think that's a great, Sort of middle ground, where we could experiment with trying to figure out how to... to deal with continuous streams of information. Without having to... Fuss with actuators and things along... things like that.

Viviane Clay: Yeah, and Monty, we have already, or for Habitat, we already have the actions for set pose and set pitch for the agent, so it's easy to just use those actions wherever it's easier than using relative actions. But yeah, I do think it's still useful to understand these concepts and understand everything you just presented, Scott, because I feel like everyone has come in touch with these things before, not necessarily in terms of action policies, but also for visualizing things, for loading models into habitat, showing objects at the right location relative to the agent, stuff like that. So it's... yeah, I think the general topic of understanding all this is still, Useful. In a lot of ways.

Niels Leadholm: Yeah, and I'm not sure there... there's any reason we would want to go in and change the existing ones, but I think it's a fair point that if we want to add More action spaces than... Yeah, like you're suggesting, Tristan, yeah, just remember that we... we have ways to... Just set these things.

But.

Scott Knudstrup: I think from... from my perspective on, the daily work, is my... Goal for myself is just to, if there are these policies, look at policy, that makes assumptions about the... Kinematic chain. Then, just be clear about them. So... a future me doesn't try to just plug in, look at, thinking that it's going to act in a different way, or it's, it's going to pitch and then y'all, or something like that. as just a matter of practical, practicality. Trying to be as explicit as possible about the constructs that are assumed and actually required for different components, really just policies and parts of the motor system. And so that's my, plea, is that any bit of motor code Just says what the assumed kinematic chain is in the top-level doc string. Basically.

Niels Leadholm: That seems fair.

Scott Knudstrup: Yeah.

I don't think I have anything else.

Niels Leadholm: That's real nice, yeah. Yeah, really awesome.