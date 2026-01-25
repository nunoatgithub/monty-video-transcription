Alright, I'll give it a shot. It's a big topic with a lot of interesting tangents. I'll kick it off and we'll see how far we get.

Let's see here. I'm going to present our view.

Niels Leadholm: Nice, I like the name.

Scott Knudstrup: Just all of space. Okay, let's go ahead. I didn't know what to call this, so "spatial" it is. I figured we could start by talking about the de facto conventions in Monty—some explicit, some implicit. We can probably all agree it would be better to be explicit about all the conventions in play. That involves Cartesian coordinate conventions, spherical coordinate conventions, and rotations. I'm sure everyone is aware we have a lot of different ways of representing rotations. I don't have much prepared for that, but the more we can do to eliminate inconsistencies, and maybe one day abolish the scalar-last quaternion from our codebase, the better. Not that I'm taking a side on scalar-first versus scalar-last, but if we're going to pick one, let's try to stick with it.

Let's talk a little about transformations, which are stable as long as we agree on the conventions, and a little about reference frames, with a couple of examples involving the Dyson agent and targeting—finding the right actions to position the Dyson agent to look at something. Let's jump right into it. First off, there are a lot of different ways you could decide which axes are X, Y, and Z. Here, I'm going to use red for X, green for Y, and blue for Z. This is our convention.

Imagine this is an agent or a sensor facing the mug. Pointing to the right of us is the x-axis, the y-axis is pointing straight up, and the z-axis is pointing behind us. This was confusing to me when I first joined the project, because who has a negative axis of 24? It just seems strange. It has the advantage, though, of leaving the plane you're seeing looking normal, with X going to the right and Y going up. If you want a right-handed coordinate system, there is only one direction for Z to go. You can't have a right-hand coordinate system with X to the right, Y up, and Z forward—that would be a left-handed coordinate system.

Niels Leadholm: So, in the right-handed coordinate system, which one is which?

Scott Knudstrup: A right-handed coordinate system means—

Hojae Lee: Your thumb is X, your index is Y, and where you curl is where Z should be. So if you put your thumb to the red, index to the green—

Niels Leadholm: Yeah.

Hojae Lee: It tells you where the blue should be, which makes sense.

Niels Leadholm: And I guess that makes sense, because if I held this at my head, then Z is pointing back.

Hojae Lee: Yeah.

Niels Leadholm: That does seem to be the same. Okay, cool.

Viviane Clay: Depends on how you rotate your hand.

Hojae Lee: Also, we must follow the right-hand rule, otherwise everything breaks. That's not a rule we can break.

Scott Knudstrup: I'm not a physicist, but it comes up in physics a lot. Talk to a physicist about electromagnetism and they'll have things to say about the right-hand rule. All I remember is you can wrap your hand around, and that's the direction of the magnetic field. I didn't really understand it at a deeper level or its importance in physical reality, but in terms of our conventions, there are two nice things to know about right-handed coordinate systems. One is that if you're ever trying to remember which way positive rotation is about an axis—let's say I'm going to rotate around the X-axis—just imagine you're facing straight down it. Imagine you're off to the left of the screen, staring straight down the positive—

Viviane Clay: I can see your cursor.

Scott Knudstrup: What's that?

Viviane Clay: We can see your cursor.

Scott Knudstrup: So you can. Okay, so we're here, staring straight down. Then the remaining two axes are going to be spinning counterclockwise.

That's a feature of right-handed coordinate systems.

Viviane Clay: Counterclockwise is positive rotation, and clockwise is negative.

Scott Knudstrup: Yep.

Viviane Clay: So no matter which—

Scott Knudstrup: If you want to know, for example, which way is yaw—if I say yaw 10 degrees and I'm facing this cup, is that going to spin me this way or that way? Part of me thinks it's going to spin that way, because I'm thinking, "Oh, it's yaw, and X is that way, so positive spin," but no, it's not that way. You stare down this Y-axis, mentally imagine it, and then these go counterclockwise in this direction, so positive yaw is spinning that way.

Ramy: I just point my thumb in the direction of the axis, then curl my fingers—that's the way the others go.

Scott Knudstrup: Everybody's got their way. That's the way a lot of people use, and for some reason, I just play with my hands and it never quite clicked for me, but thinking about staring down the axis and imagining the counterclockwise motion helps me make sense of it.

Tristan Slominski: Point your thumb down the axis, and then—

Scott Knudstrup: Yeah, I'm sorry, I clicked through my thumbnail. The other thing to be aware of is that rotations—this is just an interesting fact of three-dimensional space—can be broken into two subgroups: left-handed rotations and right-handed ones. You can't rotate a right-handed coordinate frame into a left-handed one, just like you can't rotate your hands. If you're struggling to make two images look the same through rotation only, there's a good chance that either your controls are bad, which is common in programs for rotating things, or there's a reflection. That means they're opposite-handed.

Here are some other common conventions. We have X to the left, Y forward, Z up. I think this is Matplotlib; it's also Blender. If you ever try to plot stuff in Matplotlib and it looks spun by 90 degrees, it's because it's in this coordinate system. You can imagine rotating the x-axis here, rotating this green axis toward the blue one, and then you would have that. You can transform between Matplotlib data and Monty data through one rotation about the x-axis by 90 degrees. Here's another one, which is common in flight.

The point is, for example, Mujoco has a different 3D axes convention, so any data that comes and goes from Mujoco will need the corresponding transformation, or else things in Monty won't work. We have these assumptions built in, and they are due to Habitat, which uses the OpenGL convention, a very common 3D graphics convention. It's something to keep in mind. Anytime you're interfacing Monty with any other visualization or simulation tool, this is probably the first question you should ask yourself.

Any further thoughts on that? Go ahead.

Hojae Lee: The right-hand rule is mathematically important. Any rotation matrix, besides all the vectors being orthonormal, must have a determinant of either plus 1 or minus 1. The right-hand rule specifies that the rotation matrix has a determinant of 1. If you construct a rotation matrix from a quaternion and convert it to a matrix, it will have determinant plus one, unless you want to define everything in left hand, which means not using any of those conversions. That's the importance.

Tristan Slominski: We must follow the right-hand rule. It's not impossible—Unity uses a left-handed coordinate system, and it's a successful simulation engine. It's just a headache of conventions. They're the odd child out, as far as I understand, but this doesn't make it impossible, just more complicated.

Hojae Lee: You have to transform more.

Niels Leadholm: I was curious, Scott, if we're working with a new tool, maybe a new simulation or something like a VR setup tracking the coordinate of the tracker, is there a systematic way to determine this if it's not well documented?

Scott Knudstrup: 

Niels Leadholm: I think the closest thing is what we did in Crete.

Viviane Clay: Between...

Niels Leadholm: Take the tracker and move it through space.

Scott Knudstrup: 

Niels Leadholm: That's doing Discord axis, and this one is Z positive along that axis. That's basically what we ended up doing, but I don't know if there's something more elegant or foolproof.

Scott Knudstrup: Let me see if I can pull up ExcalDraw quickly.

Viviane Clay: I remember, Niels, you were sitting in front of the screen, just moving your hand in space.

Scott Knudstrup: That's exactly—

Niels Leadholm: Using sensorimotor—

Scott Knudstrup: Exactly what all this means is, if I can move one unit in some reference coordinate system, and that ends up being 100 in Monty, you know that X with respect to whatever coordinate frame you've got corresponds to X hat in Monty. Do this for each of the three dimensions, and you'll get—

Niels Leadholm: Map it out.

Scott Knudstrup: If you've got a rotation matrix that goes from B to Monty, those are the basis vectors of B with respect to Monty. That's just the definition. This is exactly what you want to do: probe in each axis.

Niels Leadholm: Okay, cool.

Hojae Lee: In Monty, our Euler angles are in XYZ, is that—

Scott Knudstrup: Oh, boy.

Hojae Lee: Following, or—okay, let's continue.

Scott Knudstrup: Let's go to—

Sometimes you'll find things well-documented, but you can always figure it out the way Niels is suggesting. I have a script that will convert between arbitrary conventions—you tell it right, up, down, right, forward—and I wanted to get it into a gist or something before this, but I didn't. I'll put utilities like that somewhere so you can use them. Sometimes I'll use that: I'll say RFU to RUB, and it'll give me a transformation matrix, meaning right-forward-up to right-up-back, and it just spits it out for you. This is handy when you want to rotate between different conventions.

Here's another one that's interesting: spherical coordinates. They come up a lot when dealing with camera stuff or when you have to issue commands, like yaw left by a certain number of degrees, or you're looking at a point in sensor data and trying to find the associated spherical coordinates.

There are a couple of ways to define these angles. There are two: the azimuthal angle, which is rotation about the y-axis, and the elevation or polar angle. The way most of us learned it is the math or physics way. Actually, math and physics don't have exactly the same convention.

Niels Leadholm: For the sake of discussion, I'll just say this one down here.

Scott Knudstrup: Oops. It's probably the way we learned it, where we measure the azimuthal angle from the x-axis. If you have a point in space, you measure from the x-axis, and to get its polar coordinate, you measure down from the vertical axis.

In robotics and similar fields, it's more common to do it the way we do: since we're looking straight down the negative z-axis, we measure the azimuthal coordinate away from the negative z-axis, spinning in the positive direction, and we measure the elevation up from the XZ plane.

What that really means is this is called the forward-aligned zero-angle axis convention. The azimuthal coordinate—I'm not going to say polar coordinate, because by context that usually means coming down from the vertical axis, unless someone has other experience, but that's just from what I can tell. Usually, they call it elevation. Down here, zero in terms of the angles means they're aligned. Essentially, the origin of these two angular coordinates is straight down the center here, so their zeros are aligned. In contrast, in the math or physics convention, your azimuthal zero is one way, and your polar zero is up that way.

Niels Leadholm: So in the math and physics convention, they're never really both zero. It's like cosine and sine—when one grows, the other shrinks. If you were facing in the direction of the red one, the polar one from the top would be non-zero. In the convention we use in Habitat, they can both be zero at the same time, which corresponds to looking forward.

Scott Knudstrup: I think that's right.

Viviane Clay: Wouldn't it be that if one of them is zero, the other has no effect?

Niels Leadholm: Has no effect.

Viviane Clay: If you have zero for the red one, the line is just up, so it doesn't matter how you rotate along the green one.

Niels Leadholm: That's a fair point.

Scott Knudstrup: Rotating around the green one...

Niels Leadholm: I guess it depends; you could still rotate...

Scott Knudstrup: Coordinate, right?

Viviane Clay: I'm talking about the math version now. In the robotics one, it's different.

Tristan Slominski: Zero, zero is undefined. It's not a point.

Scott Knudstrup: Say it again?

Tristan Slominski: Zero, zero is undefined; it has to be zero, ninety.

Niels Leadholm: You can't get to zero, zero.

Scott Knudstrup: Unless you're at the origin.

Niels Leadholm: If you're a 3D object, you could still rotate about the green, even if your polar one is zero.

Viviane Clay: If the little black dot is some kind of shape, it'll rotate around its own axis?

Niels Leadholm: Yes.

Viviane Clay: If we're not just talking points, but that's maybe mixing things up.

Niels Leadholm: Anyway, it doesn't really matter. I was just checking my understanding. This is a helpful visualization.

Viviane Clay: Sorry, Scott, if I were to Google which convention is used where, what are the terms for these?

Hojae Lee: Forward angle zero, forward-aligned zero-angle axis. That's the valve.

Scott Knudstrup: Borderline zero-incl axis convention.

Viviane Clay: Okay.

Scott Knudstrup: Here's my word of warning about Googling the transformations between the two: you're always going to have to do this internal substitution game, where one source calls an axis X, another calls it Y, and so on. It can get confusing quickly. If your Googling involves coordinate transformations between the two, that's where both conventions come into play.

The exact form of these transformations depends on both conventions.

Niels Leadholm: Like a combinatorial number of convention flavors.

Scott Knudstrup: Yes. Here they are—moving on. No, just kidding. Redivide them yourself.

Hojae Lee: I just realized how to remember the forward-aligned zero angle. Basically, what you consider forward—in the first slide, Z is pointing into you, like your thumb. Four means positive Z, and that's considered zero angle, so if something is looking at it without any rotation, that's zero angle.

Scott Knudstrup: So forward is negative.

Hojae Lee: Forward is positive Z.

Scott Knudstrup: Four is negative.

Niels Leadholm: Not in Habitat.

Scott Knudstrup: Not Monty.

Niels Leadholm: No, Monty.

Scott Knudstrup: We're looking straight down the negative. This is our camera here for this room. We're staring in this direction.

Hojae Lee: For this, negative Z, but whatever direction you're looking at is your rotation.

Scott Knudstrup: Yes, exactly. If I'm a camera staring down this axis, then dead center is zero, zero for both angles.

Niels Leadholm: Makes a lot of sense from a robot perspective.

Hojae Lee: Yes.

Niels Leadholm: It makes a lot of sense from a robot perspective.

Scott Knudstrup: Exactly. How much do I have to rotate left? None. How much do I have to rotate up? None. That's zero.

Okay, question.

Tristan Slominski: Are you going to skip this again? I had—

Scott Knudstrup: Go ahead. Are you skipping it? No, I'm not skipping it. The axis order is straightforward. If you have a different XYZ, you just swap out the letters, for the most part, if you want to change them.

As long as you remember which one is the vertical axis, which one is the horizontal, and so on. The catch—

Niels Leadholm: As in Cartesian spherical, that first top left one could be rewritten as right-handed axis squared plus up vector squared plus backward?

Scott Knudstrup: Yes.

Niels Leadholm: And then just—

Scott Knudstrup: Backward, whatever you call it, this is the nice one.

Niels Leadholm: That's the nice one. Maybe not a good example. The second one, it matters.

Scott Knudstrup: Yes.

Niels Leadholm: But—

Scott Knudstrup: The second one, you'll probably see written differently if you look up how to do this conversion, because most texts don't have the negative z-axis as forward. Because we have the negative z-axis going forward, we have to drop this negative sign in here. That actually converts us temporarily to left-handed, because it makes the determinant negative one by multiplying a coordinate by negative.

Tristan Slominski: Great question.

Scott Knudstrup: Which we then have to undo here.

Tristan Slominski: Question. You said drop the negative sign, and then you pointed at negative Z. What do you mean by drop?

Scott Knudstrup: Drop in, sorry.

Tristan Slominski: Okay, thank you.

Scott Knudstrup: You have to drop it from your stack of negative signs into this equation.

Tristan Slominski: Thank you, appreciate it.

Scott Knudstrup: Yep.

That's one thing to be aware of for this. Trying to get the azimuthal coordinate—I'm trying to reserve "yaw" for an action, like a displacement, more than an actual rotation.

Niels Leadholm: Like rotation versus orientation. Sometimes talked about.

Scott Knudstrup: Yeah.

Niels Leadholm: Thank you.

Scott Knudstrup: Okay, what's this ATAN2 business?

Most of us have had contact with it at some point, but the brief answer is: if you've got a full circle, and you're in this situation, trying to find this angle phi, you would do tangent of phi is X over Z, therefore phi is the arctangent of X over Z. But what happens if this is in the opposite quadrant?

That would be arctangent of negative X over negative Z, so they cancel. Things in opposite coordinates will give you the same value from the regular arctangent function. That's the first issue. If we want to recover an angle from the entire circle, there's a special version called ATAN2. I think it was from the 60s, according to Wikipedia, which is funny—they made a sequel to a math function.

Instead of a single argument, it's a two-argument function. It looks at the negative and positive signs of the input and assigns the correct quadrant. That's the first thing it does. The second thing is, there's no division by zero problem. Plenty of times, the denominator will be zero. In this case, if we're staring straight to the right or left, we'd have zero in the denominator. ATAN2 will just tell you we're straight down this way, so it'll be negative 90 if we're straight on the right and the numerator is positive, and if the numerator is negative and the denominator is zero, we're 90 degrees positive. So that's ATAN2.

Niels Leadholm: Thank you, that's a really helpful explanation. That is really weird, that doesn't seem like a math function, that definitely seems more like a—

Hojae Lee: He's a pup.

Niels Leadholm: Piece of code.

Hojae Lee: Maybe I didn't mention it, but it came up in floppy.

Scott Knudstrup: Oh, yeah.

Hojae Lee: I think initially I implemented flops for ATAN, and then I realized we're using ATAN2. ATAN2 is superior in that the output is minus pi to pi, so minus 180 to 180, covering a full circle, while ATAN is minus 90 to 90. If you do ATAN of a point that's 1,1, or 45 degrees from the x-axis, counterclockwise, but if you do ATAN of minus 1, which is in quadrant 3, that's also still 45, even though it's technically 215. If you go negative 1 in the XY coordinate system, it fixes that. With ATAN, because it takes a ratio of the two, 1 over 1 is the same as negative 1 over negative 1.

Scott Knudstrup: Yeah.

Niels Leadholm: But it's just weird. It seems like a lot of if statements, rather than a smooth, continuous mapping between member spaces.

Scott Knudstrup: Yeah, it's weird.

Tristan Slominski: I've—

Hojae Lee: The practical tip is probably use ATAN2. That's what I'd like to do.

Scott Knudstrup: If you only ever care about magnitudes—

Hojae Lee: Then fine, go ahead and use ATAN.

Scott Knudstrup: But if you're on a plane, a full plane, a full circle, you want ATAN2.

Hojae Lee: Yep.

Scott Knudstrup: The sequel. Bigger and better. More complete.

Alright, I have these that are ready to get pushed into Monty, because these are the ones we should use. This is the exact form we should use, always. Unless there's some weird case, then you're responsible for it. But otherwise, if you need to do mappings between Cartesian and spherical coordinates within Monty, within our conventions, these are the forms. Those will go up into, I think, transform utils.

Alright, mapping back from spherical to Cartesian also happens.

Viviane Clay: Just to make it a little bit concrete, in Monty, where do we use those transformations? Is that when we want to go from where we are in space to translate it to a movement vector off the camera, turning it up and down and left and right, or is that draw pitch—

Scott Knudstrup: The spherical coordinate would tell you basically how much yaw or pitch there is relative to your 3D reference frame, your RG reference frame. So, if you're trying to figure out—there's a point over there, I'm facing like this, then these formulas will give you—

Viviane Clay: For example, you're using this for the saccade work. You have a salient point over here in your field of view, and now you want to look at it, so you have the salient point in spherical coordinates—wait, in Cartesian coordinates—and you want to convert it into spherical so you know how to move the camera?

Scott Knudstrup: Yeah.

Viviane Clay: Okay, cool.

Scott Knudstrup: Exactly. I think I put it down here. Euler angles are mostly necessary when we're dealing with camera data, because there's projective geometry involved, but also the motor system, because we speak to the motor system in terms of angles. We can't just tell it, "Here's my point in space," we actually have to be explicit about how to get there with an actuator.

Viviane Clay: The points in the code where we do have to do this, there's—

Scott Knudstrup: The saccade—saccading to targets, there is "get good view," which is basically the same deal. One of the other main areas, as a counterexample, is in the voting math, where there are two rotations and we need to figure out the orientation between them. In that world, you don't have to deal with Euler angles at all. You can just compute the rotation that takes you from one system to the other. You can generate a matrix and don't have to deal with the headache of Euler angles, because Euler angles are a bit of a headache. When you get them, the first thing you should ask yourself is, what order do I apply these in?

Hojae Lee: Yeah.

I first rotate around the x-axis, then the y-axis, and then the z-axis. The second question is, if I first rotate around the x-axis, so I pitch up a bit, and then rotate around the y-axis, do I rotate around the new y-axis, since that's changed now, or do I rotate around the external y-axis? This is the difference between extrinsic and intrinsic rotations. If it's intrinsic, you always rotate around the new axis. I apply the x rotation, then apply rotation around the new y-axis, and so on.

For example, when using scipy.rotation from Euler, XYZ, and then some coordinates—if they're lowercase xyz, that's intrinsic, and we apply them in the order XYZ. This is something I didn't get to in this presentation, but for any action-related space in Monty right now, you want to apply Y and then X. But when trying to figure out an object's orientation, like what Habitat was doing, you want to use the order XYZ, and do it intrinsically. That's another trial and error thing. If you see Euler angles, you should ask: what order do I apply these in, and is it intrinsic or extrinsic?

SciPy forces you to specify it. The first time I wrote it, I didn't know what it meant—I just wanted to rotate it. It does matter. Thanks for asking about this.

They always say the order matters, but it's hard to internalize what that means without good visualization tools. I'll pull up Blender later and show how to use it as a visualization tool for this, to make it more obvious. I wish there was an online tool where you could just play with rotations, but I couldn't find one.

Does that still matter if it's done extrinsically?

The order of application? I'm guessing it probably still does.

Yes.

Or does it depend on the affordances of your effectors? If you pitch up and your effector can only go intrinsically, versus being on a platform where your effector can go extrinsically or intrinsically—right?

That was confusing for me, because I'm used to thinking about it like an airplane. The idea of why gimbal lock would be a problem took me a while to understand, because I'm not used to thinking about one actuator mounted to another actuator. I'm used to thinking about free-floating spaceships that can always yaw around their own axis. So you point up—what's the big deal? But you lose the orthogonality of these axes.

Can we talk to the motor system not in angles, but just in terms of position? You can't just say, "go look at XYZ," and it will do that for you. We have to give it some kind of angle—rotate, yaw, pitch, whatever—so you can actually look at this. My wish is to use Euler angles only for defining the cube and rotation faces, like 000, 090, and the final human-readable output, showing the predicted orientation of the object at the end. But internally, we just use rotation matrices and don't need to worry about intrinsic reactions, because we just multiply by the rotation matrix.

I'm going to make the case for the opposite, actually.

To use all the angles everywhere?

The case I'm going to make—unfortunately, I didn't have time to put materials together on this—but in a simulator or robotics, say you have a joint you can rotate around. That joint is defined by an axis of rotation and the amount, and that's it.

So we do need to communicate through a motor system that way.

Yes, and even internally, in Mujoco, for example, when you issue a change, all it does is make new joint coordinates. If you say, "I want to rotate 10 degrees around this joint," it just adds 10 degrees to that coordinate. These are your generalized coordinates.

It doesn't give you a 3D reference frame for each point along that. You compute it yourself, given the axis of rotation at that joint and the amount. Through this forward pass, you can recover the full Cartesian reference frame for each node, but internally, it's all represented through just the amount. The reason I'm making the case for thinking about it this way is because if we're trying to issue commands, if we're trying to actually learn commands, we want to be able to just learn a parameter—this is how much you need to spin.

But I want to talk more about this, because there's a future Monty and there's today's Monty. I don't think today's Monty should be using all their angles inside, except as an output of the motor system. The reason for that is...

Our current learning modules don't have an embodied model at all, so they just care about a point in space. For that, we can use matrices or quaternions, and that can be part of the goal state to their motor system. The motor system is responsible for taking that space and figuring out how to act on it, and that's where the conversion can happen. In the future, Monty will essentially have what I call an embodiment oracle—you magically know how your body is put together and how to translate out in space using this oracle. In the future, when that embodiment oracle becomes learned inside learning modules, maybe we might want to drift away and start doing what you're saying, but I think it would just become too complicated now. None of the learning modules today have any business learning how to move.

Until we actually go after—

Scott Knudstrup: Agreement.

Viviane Clay: Say again? Okay.

Scott Knudstrup: I'm in 100% agreement on that. I'm just dreaming forward, X number of months or years, to when we are learning to control a motor system. We have to do it in the coordinates of the actuators, and the coordinates of the actuators are angles, amounts—basically, if it's a rotating cuff. For the time being, until we have learning components that learn how to do motor commands, there's no reason to do anything in Euler angles or anything like that.

Tristan Slominski: And I'm in agreement with the future.

Scott Knudstrup: Yeah.

Viviane Clay: That's how it is right now, right? Goal state generators emit locations; they don't emit Euler angles, as far as I remember. Learning modules, like hypotheses and all that, are all rotation matrices, so I don't think we are using Euler angles inside Monty right now, except for the human-readable output, like the logging.

Scott Knudstrup: Yeah.

Hojae Lee: Yeah. Yep.

Niels Leadholm: And then in terms of the motor outputs, just to clarify, because you're saying two Euler angles, but are the spherical angles Euler angles, or—

Scott Knudstrup: Yes.

Niels Leadholm: Okay, nice.

Scott Knudstrup: Euler angles are an amount of information about a certain axis.

Niels Leadholm: Agreed.

Scott Knudstrup: Here you just have two.

Niels Leadholm: Rather than three.

Scott Knudstrup: And we never use radius, or we haven't thus far. We're not doing full conversions, but we just use these two when we do actions. I think there's also some literature out there about vector cells and things like that. There's stuff going on in the brain in this type of representation. I'm not an expert on that area. I read a little about it maybe a year ago because I thought it was interesting. These things are in the brain, and you can imagine why. If I hear a bang over in this direction, I don't need to know where that is in full 3D coordinates; I just need to know how much to move to get there.

Niels Leadholm: The model? Free kind of stuff.

Scott Knudstrup: Yeah, exactly.

Niels Leadholm: It's interesting, because with the insect path integration talk I saw, they were trying to figure out whether ants, for example, use more polar versus Cartesian coordinates. Initially, they thought it would be polar because it's simpler, but actually, they realized it's probably Cartesian for various reasons. I think that fits with learning modules still being more Cartesian, and this also fits with what you were saying, Tristan, that within the learning modules, they just care about points in space. It's more like the motor system where it's, "Now I need to move this by a certain amount."

Tristan Slominski: I don't.

Scott Knudstrup: Sorry, go ahead.

Tristan Slominski: I do have a question because you said a specific phrase. I just need to know how far to move at this angle, or whatnot. Are you sure it's how far to move, and not how much force to apply over how much time?

Scott Knudstrup: Yes. No, I'm not sure of anything; I just had an early guess.

Tristan Slominski: But I just want to throw that in, right?

Scott Knudstrup: Yeah.

Tristan Slominski: It might not be communicated as "move this many angles"; it might be communicated as "flex this muscle this fast."

Scott Knudstrup: Yeah. It could be anywhere along that. Ultimately, it's going to be—

Niels Leadholm: That's probably the final step in it, and that's probably why, if you think something's heavy and you go to pick it up, your arm flies up because you apply a large force or whatever. But I guess what was informing that muscle contraction is probably something like, "I want to move my arm by this amount."

Scott Knudstrup: Yeah.

I think we've danced around this argument a little bit. I'm always willing to entertain the idea that there's more polar happening than we might expect, but I'm open to it. I don't really know, because when I think about situations where the depth is ambiguous or unknown, or even just on a flat plane, like watching TV, I don't have a sense of what the depth is. I'm not computing it, or it's something that's hundreds of meters away. I'm really just saccading between two points. They might as well be of infinite distance, or they could be close, but I can still saccade to them because all I need to know is the angular distance between them. So I think there are cases where there's a strong case for more polar representation, but it's debatable.

I brought this up at the Focus Week, and you said you could actually just adjust your saccade amounts based on the distance from you to that billboard. But it feels like you're asking a lot of your ability to compute depth, especially on the fly. If you're trying to do all of your eye motions in Cartesian coordinates, especially when V1 and the collicular surface are basically sitting there in angular coordinates—spherical coordinates, more or less—it feels very easy to extract. If you need to do a quick motor command from here to here, it's already in those coordinates.

Viviane Clay: It seems like maybe the more subcortical parts, like the sensor module and the motor system, can do spherical coordinates. When you're doing a saccade to something salient over here, I agree, you probably don't have a very accurate depth estimate, and you probably don't need that to calculate how to move there. You don't need to go through Cartesian space, but that's more like a model-free movement based only on sensor module information. But once you go to model-based movements, based on actual structured models you learned, as in the learning modules, it's probably going to be Cartesian-based.

Scott Knudstrup: Yeah.

Hojae Lee: Or I guess this might be a case where even if some biologist found out that it's spherical, we might still stick to matrices-based rotation in the learning module, just for computational benefits. Possibly. I think I'm convinced, but I didn't come to this same conclusion because I didn't work with the motor system yet. I think I'm the last one. I remember when you started this keyboard, you said, "I don't know anything about the motor system," and now you're the expert, and I still don't know about the motor system. Maybe after my 2D sensor module.

Scott Knudstrup: Yeah, and hopefully, just submitting these transforms to Monty will make the process easier.

Hojae Lee: Yeah.

Scott Knudstrup: So you don't have to think this through every time.

Hojae Lee: My ideal world is that there's no body, and our agent is just an infinitely small point. You can tell it to look at any XYZ, and it'll just do it.

Scott Knudstrup: Yeah.

Hojae Lee: But that's very non-real world.

Scott Knudstrup: Oh, before I forget, the azimuthal angle is defined between negative 180 and positive 180, so you get the full circle. But the polar coordinate is just straight down to straight up, so you've got 90 degrees there. If you tip past—

Hojae Lee: Oh, yeah.

Scott Knudstrup: That's actually equivalent to doing a 180 in yaw, plus a little bit in the opposite direction of polar. Just something to keep in mind.

Hojae Lee: I think you just triggered a calculus memory from high school. I just got a flashback.

Scott Knudstrup: You're welcome.

Hojae Lee: Yeah, thank you.

Scott Knudstrup: Here's something that puzzled me. If you compute phi, the azimuthal coordinate, you only need X and Z. You can just look straight down from the plane. But when you want to compute the polar angle—or elevation—you need to get X, Y, and Z involved. My first mistake was thinking you could do the same projection for the polar angle. Why not just project this? What's special about pitch? We live in a world where no one direction is privileged over any other. What's special about this? This was a bit of a mystery for me, but hopefully I can clarify. Maybe it's completely intuitive for you, but for me, it wasn't.

Niels Leadholm: Is it not just like the reason you were describing, that the way the coordinate system is defined is privileged for one of the axes? If you tip backwards, then you're going to start reverting to another. Is it related to that?

Scott Knudstrup: I hadn't thought about that, but yes, basically.

Niels Leadholm: So here's how I'm thinking of it.

Scott Knudstrup: This extraction maintains orthogonality, in a sense. Otherwise, these two things can be non-independent when you perform an action. This comes back to being in a situation where we have to decide in advance that we're going to perform a motion in a sequence. These are Euler angles. We have to think about the order in which we do things. When you do a command, we're actually rotating our polar plane, trying to get that dot onto this sort of meridian.

Niels Leadholm: Sorry, just to clarify, what is what? So the dot is—

Scott Knudstrup: The dot is the target we want to look at, for example.

Niels Leadholm: And the direction we're pointing in is the dashed line.

Scott Knudstrup: Yes. When we yaw, we're rotating that whole vertical plane. That's our plane for moving our up-down axis, our sensor module, or whatever.

If you just project onto the YX plane to try to get that pitch amount, you're not taking into account the fact that yaw is going to change what that axis is. This version of the elevation coordinate is independent of yaw.

Niels Leadholm: As in, if you perform a yaw and then do this one, you're good.

Scott Knudstrup: Yeah.

Hojae Lee: Otherwise, what you'd have to do is—

Scott Knudstrup: Do the first yaw motion, stop, take another measurement, now compute the polar angle in the simple way—just project it onto the YX plane and do the motion. That's what would happen.

Niels Leadholm: That makes sense.

Scott Knudstrup: Yeah.

Hojae Lee: There.

Scott Knudstrup: Okay.

Let's play that out again. I can't have wasted learning how to do that in Blender.

Viviane Clay: Animation.

Niels Leadholm: Yeah, really nice.

Viviane Clay: So you always yaw first and then pitch?

Scott Knudstrup: Yes.

Viviane Clay: Okay, and if you did it in reverse order, you'd get a different result.

Scott Knudstrup: If you did it in reverse order, you'd have to compute those angles differently. You'd have to—

Scott Knudstrup: Flip the way that you do that.

Viviane Clay: Yeah, okay.

Scott Knudstrup: Yeah.

Niels Leadholm: Life would be terrible if we had to always move like this.

Scott Knudstrup: It's so much easier. Here's a fun fact about rotations: for any series of Euler angles, there is an axis in space and a rotation amount that will get your reference frame from the original to the new one. If we had an actuator aligned with that axis, it would be easy—we'd just spin by that amount. But we don't have actuators in every direction, so we have to work within the confines of the rotational axes we do have. That's a cool fact about rotations.

I'll leave it as an exercise to the reader to work out exactly how that works. Okay, let's give this a shot. I'm going to pull up Blender.

Let's try this.

Viviane Clay: Which current convention does Blender use, by the way?

Scott Knudstrup: Coordinated convention is Z up, next to the right.

Actually, can you tell me how small all this stuff is? Can you see this little widget up at the top?

Hojae Lee: Yeah.

Viviane Clay: Yep.

Scott Knudstrup: Okay. If it's helpful, I can turn on axes to try to—

Viviane Clay: Remember where we are.

Scott Knudstrup: But for the time being, I want to try to forget about that, just for this demonstration.

Here's my two degree of freedom gimbal, which is what the system is called when you've got a rotating thing, a yaw thing, and then mounted on top of that, an actuator that moves in another direction. It's called a two degree of freedom gimbal, or sometimes a free gimbal.

You can't really tell right now because these things are right on top of each other and they're co-aligned. But if I grab this sensor and pitch it, you can see these are starting to come apart. I've encoded sensor stuff in red.

Including this ray here, which is a sort of targeting array in red for the sensor. In black is the agent. This is the agent's reference frame, and this is what he's pointing towards. The sideways one is our x-axis; they're always co-aligned. It looks black, but that's just because of alpha blending. The reason it looks grainy is because of alpha blending; it just looks a little funny when you're trying to render it live. Alright, I'm going to reset.

Our first goal—oh, and this box here, I'm going to get rid of it in a second, but that's our camera. I've mounted a camera onto the sensor so we can see what the sensor is seeing. Let's simulate this process. I'm going to determine what our yaw angle ought to be to get to that target first, and then we'll try to get to the next one. First, I'll go into this top-down view. Instead of doing trigonometry, I'll just grab my sensor and see how much it would have to yaw to get to that. Looks like about 30 degrees. Alright, great. Now, what if I were—sorry?

What if I were over here? If I can't just do this, I'll try to figure out how much we'd have to pitch the sensor.

Viviane Clay: Oops.

Niels Leadholm: Wait, was that the right one?

Scott Knudstrup: Sorry, you're right. I was like, did my demo change? Supposed to be about 45 degrees, something like that.

Yeah, it was supposed to be 45. This demo will work anyway. It's okay. Let's go ahead and execute that, now that we've computed it. I'm going to yaw the agent, because the agent yaws. I am the agent who yaws.

Tristan Slominski: I got it.

Scott Knudstrup: So we're going 30 degrees in this direction, and then we're going to pitch up the sensor. I'm going to grab my sensor and pitch it up.

Let me just go into camera view. See how we're doing.

Pretty good, 45 degrees. We're right in the center.

There's a little red dot from my targeter, but it's dead on in the center. All good, right? Maybe the quickest thing to demo here would be to show that if I do this in reverse order—

Just going to reset everything. Now I'm going to pitch the agent first by 45 degrees.

Then I'm going to swivel the agent by—wrong direction—30. If I look at the sensor, it should be slightly different.

Oh, no, it's not. Okay, forget it. Oh, because they were co-aligned to begin with. That matters more for the second pass. Anyway, now we need to—

Tristan Slominski: The yaw was extrinsic, right? Agent never pitched with the pitch, that's why. Yeah. Okay, but an extrinsic should work.

Scott Knudstrup: Now we're no longer aligned. If I try to do—I've got my sensor and its camera data. I'm going to try to figure out how much I need to pitch and yaw to get over to the second target. I'm going to try to simulate what we just did. I'll try to get an exact orthogonal projection of what the sensor is seeing. It's a bit tricky, but I'm trying to get that Z-axis straight on. How much would my sensor have to yaw? I'm doing this the wrong way on purpose. How much would my sensor have to yaw to get to that point, to hit that target?

It's 90 degrees. That's how much more the sensor would have to go.

Tristan Slominski: You said you're doing it wrong. Are you saying you're yawing the sensor instead of the agent?

Scott Knudstrup: Yes, thank you. Trying to show what a mistake that could be. Okay, 90 degrees would get me there. I'm going to reset that. How much would my sensor have to pitch?

I'm going to try to get exactly dead on. Looks like I don't have to pitch at all. I'm already right on target. Great. So if I just tell my agent to yaw 90 degrees and don't pitch at all—

Let's see what happens. Tell my agent, what did I say, 90 degrees? So we go up to positive 60.

About here. We're way off. This is why it's important that when you're computing the yaw and pitch amounts, especially yaw, you have to do it in the agent's reference frame. Then, ask how much the agent would pitch to get to this.

And then subtract the amount that I'm currently pitched at. This is one reason why it would be useful to have an internal memory of the current joint angle. Instead of recomputing the current agent or sensor pitch, you would already have access to it, but that's another story.

Niels Leadholm: Is part of this inherent to the 2 Degrees of Freedom gimbal? If you had a sensor that could yaw, then you could just do that.

Scott Knudstrup: Yeah.

Hojae Lee: Is it Habitat where our sensor is attached to our agent in this 2DOF way, or can we make it a ball and socket joint?

Scott Knudstrup: I don't think there's anything preventing us from doing that, but all the commands being issued in the codebase are turn left (agent yaw), turn right, and look up, look down. Those are sensor commands.

Hojae Lee: Okay.

Scott Knudstrup: To my knowledge, maybe it is... I'm not familiar with how Habitat simulators are configured, so maybe sensors can actually yaw independently. This is when I realized something was wrong with my understanding of Monty and probably geometry. I couldn't shake the idea that an agent ought to be able to yaw along its own axes, that the sensor would be able to continue using its own rotation. When I was trying to compute coordinates, they're usually not this extreme, but the targeting would be.

Hojae Lee: Yeah.

Scott Knudstrup: It was because of this issue of trying to compute the amount of yaw. It's natural, because the data you get comes from the sensor in the sensor's reference frame. It ends up being in the world reference frame, but then you have to forward map it into the sensor's reference frame to figure out how much to yaw. Then you realize there's a mismatch. The issue is, you need to be thinking about how much to yaw in the agent's reference frame.

Hojae Lee: Yeah.

Scott Knudstrup: In terms of pitching, you could do that in the agent's reference frame, but you need to account for the current sensor pitch. You ought to be able to do it just from the sensor's reference frame, and I do it here just fine. I could do agent yaw in the agent's reference frame and sensor pitch in the sensor's reference frame. I tried it, and it was fine, but when I did it in Habitat or in Monty, there were slight differences. I'm still not really sure what's going on there, or if I made a mistake, because it's so easy to make little mistakes, like missing a sign.

Hojae Lee: It's really...

Niels Leadholm: Nice with this visualization and intuitive, but I can see how this would be a pain to debug.

Hojae Lee: Theoretically, if the joint type is not 2 degrees of freedom but 3 degrees of freedom, we would worry less about this, right? It depends on the robot, but I think a lot of our joints are... I'm just trying to do weird joint things now.

Niels Leadholm: Certainly eyeballs are more of a ball and socket than a... I'm assuming, unless there's some historical reason from when Habitat was implemented or the interface, because I'm sure we can do look left and look right, rather than turn left and turn right, i.e., sensor, if we wanted to.

Scott Knudstrup: Yeah.

Tristan Slominski: Here's another thing I want to pitch around this. This is just a historical path that got us here. When I was thinking about how I would do this from scratch, there would be a single position action that sets the entire pose in space, and that's it. My question is, this is all very valuable for embodied motor systems. We are in a simulator. All our experiments—what are we trying to do today with Monty? Are we trying to control a body, or are we still trying to figure out how learning modules ought to work? The reason I'm asking is because we can probably substitute everything to be a single action, which is position 3D. We give it where it needs to be and what pose it's in, and it just goes there. We don't need to do yaw, turn left, turn right, or anything else. We can just say, appear in this position. In a simulated environment, that might be enough for all the near-term experiments we want to do. Then we can tackle this when we want to work with embodied things.

Scott Knudstrup: I want to make three points quickly. First, we did a robotics hackathon. We are attempting to occasionally do things in the real world. Maybe it makes sense to—I'm not pushing back, this is just a counter-argument—while we're trying to learn and develop as much as we can in this fundamental research area. If we are going to try to validate or get engagement in the robotics world, then maybe it's worth keeping in mind. In support of your point, the surface agent doesn't care about any of this. It sets agent pose. It just warps to where it needs to be.

Niels Leadholm: The goal state does that, the jump to goal state.

Scott Knudstrup: Yeah. But the surface agent doesn't warp.

Niels Leadholm: It does a complex four-step trig-based thing.

Scott Knudstrup: Oh, it does?

Niels Leadholm: Yeah.

That's my understanding. It looks at the next surface normal, calculates what rotation it needs to face that, then shifts along a tangent, and so on.

Scott Knudstrup: Sorry, I should have clarified. That happens when it's trying to execute a goal state.

Niels Leadholm: That's when the surface agent—

Scott Knudstrup: Yeah, the jump to goal state is exactly—

Niels Leadholm: What you're describing, Tristan. We just want to see what effect this has on learning modules; we don't care how it's achieving that. We're just going to set the pose.

Scott Knudstrup: If we had to work out all the kinematics of getting the finger to that point, that wouldn't have been a productive use of time for figuring things out. I agree on that side. But having to think about this was ultimately a good thing for me, personally.

Hojae Lee: Yeah.

Niels Leadholm: This is how hazing starts, Scott. You're like—

Scott Knudstrup: I don't know.

Niels Leadholm: I had to go through this, so everyone else should have to go through this.

Scott Knudstrup: I think it helped me develop a longer-term view of what a motor system might look like that can learn.

I think people should be able to do anything they want within Monty with just warping, setting the agent pose, sensor pose, as a disembodied thing, like a point or a being of pure light. At the same time, maybe there's value in occasionally considering what contact with physical mechanisms is like, but that's more of a personal matter than an argument about the system.

Hojae Lee: I've been thinking of Monty as this one-point thing that you can give a position XYZ to. That's the ideal, but technically, if we think about two sensor modules or more, I don't want them to be two separate things. They must be connected to an agent or a couple of agents, and there must be some relationship between them. Let's say we have one agent and two sensors. The easiest would be if the joint is a ball and socket, three degrees of freedom, so things can be independent. In that sense, there is some sense of bodiness when I think about more than one sensor module. At least I'm thinking about how they are related to each other. In real life, we probably don't want things to be crashing, but I'm not going to worry about that now.

Niels Leadholm: For what it's worth, even with our being of light, we have issues with the jump to goal state, where it can appear inside of objects and similar problems. There's some very crude code to try and deal with that. The advantage of not just setting a pose is that you tend to do it more incrementally, and it forces us to think more about policies. I think it's a balance, and we've been treading a reasonable balance so far. You're right, Scott, there are advantages to thinking through these things, and it makes it easier if we want to do things like robotics, so it's not the first time we've ever had to do small continuous movements.

Niels Leadholm: We had the exact thought when we wanted to add the goal state, that we don't want to figure out how to get a surface agent to move across the surface. That's going to be super complex.

Hojae Lee: Is that what I'm supposed to be doing for two decaser modules? It's going to be super complex. It's related.

Niels Leadholm: In a local neighborhood, at least you don't have to move to the other side of a 3D space.

Tristan Slominski: Another argument for doing the teleport in the simulator until we actually focus on robotics is that robotics is not going to... Disregard. I don't have a clear thought yet.

Niels Leadholm: I don't know if this is what you were thinking, but there are a lot of these things that we wouldn't necessarily want to compute or implement ourselves. Inverse kinematics is a huge field. There's also reinforcement learning, neural network-based methods to move systems. We could imagine Monty as the cortex, and all these other systems—whether it's evolution, Boston Dynamics, or someone else—have implemented it. We just leverage that, and it figures out how to actually move.

Scott Knudstrup: Yeah.

Hojae Lee: Maybe two years later, once we figure out the cortex, we'll just hire a roboticist, and they can help.

Tristan Slominski: I guess I'm just discounting the research effort on non-learning module learned embodiments.

This is all extremely relevant when we commit to learning modules and figure out how to model the body. Before that, it just seems like dipping the toes in, but it feels like friction at any step before that. When learning modules just say you need to appear here, any code that makes that happen is just an expense that will need to go away when learning modules learn the body.

If we're in a simulator, who cares?

Scott Knudstrup: Here's another pitch, another angle to think about: warping pretends like time isn't continuous. We would eventually like Monty to figure out how to live in a continuous time world, and that involves a lot of sensory input on the way to accomplishing that goal state. Sensory input, which we may want to cut down on in the learning module, maybe not. There will be issues in terms of how learning modules function during the execution of motion and things like that in the continuous time world. These things are fundamental to the brain. Even though kinematic control may be something we can put off—the actual mechanisms we use to position joints and things like that—figuring out how to have Monty behave in a continuous streaming world where we don't warp is actually fundamental.

Tristan Slominski: I think my challenge to that is, I think you're imagining warping as just going huge distances for no reason. All I'm saying is, you can trace a path just by setting set pose, and you can get everything you just said, just without worrying about how to move right, tangent, or up. I'd just be like, here. I'm not advocating for ignoring continuous motion. If you're going to do continuous motion, just say I'm on this path that I magically calculated, because I can.

Scott Knudstrup: I'm good with that. I think that's a great middle ground, where we could experiment with figuring out how to deal with continuous streams of information without having to fuss with actuators and things like that.

Viviane Clay: In Monty, or for Habitat, we already have actions for set pose and set pitch for the agent, so it's easy to use those actions wherever it's easier than using relative actions. I still think it's useful to understand these concepts and everything you just presented, Scott, because everyone has encountered these things before—not just in terms of action policies, but also for visualizing, loading models into Habitat, and showing objects at the correct location relative to the agent. Understanding all this is still useful in many ways.

Niels Leadholm: I'm not sure there's any reason to change the existing ones, but it's a fair point that if we want to add more action spaces, like you're suggesting, Tristan, just remember that we have ways to set these things.

Scott Knudstrup: From my perspective in daily work, my goal is that if there are policies that make assumptions about the kinematic chain, just be clear about them. That way, a future me doesn't try to plug something in, thinking it's going to act differently, or that it's going to pitch and then yaw, or something like that. As a matter of practicality, try to be as explicit as possible about the constructs that are assumed and required for different components, especially policies and parts of the motor system. My plea is that any motor code states the assumed kinematic chain in the top-level docstring.

Niels Leadholm: That seems fair.

Scott Knudstrup: Yeah.

I don't think I have anything else.

Niels Leadholm: That's really nice. Really awesome.