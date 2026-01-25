so. There are several things I can, Go over one is, I guess the figures and stuff in the white paper. everyone of the research team should be very familiar with them and how it works. So if that would be helpful, I can go over them so you know how to explain them to someone else. To, another thing I thought would be cool to start off with is a bit of a history, lesson on the, graph learning module. 'cause I feel like it gives some of the background that you wouldn't usually get, but it helps frame some of the discussions we often have, go the displacement matching versus feature set location matching kind of question. so I might actually start with this one if, no one has an objection. And then the last thing, I think that's a good idea actually. Yeah. Okay. Yeah. Also, 'cause the code, that's how it evolved and yeah, in general I think that's useful context. Yeah, and you'll come across stuff from all of them, when you go through the code. and then, yeah, lastly, definitely wanna go over like the evidence graph, LM code, at least like this part of what attributes we have and how they actually interact with each other and, effect matching. So yeah, I started like a blank X calendar draw just in case people wanna, ask questions on the whiteboard or I need to draw something. So I'm just gonna share the link in the Slack coding channel if someone wants to join there.

so yeah, let me start with a brief history of graph matching in Monty.

so this is a writeup. it's on old Leaf, but also the PDF is in our Google Drive.

Basically we have three types of learning modules in Monte at the moment. We have the displacement lm, we have the feature LM and the evidence, lm. So displacement graph LM uses edges in the graph. Hang on, let me see if you have the graph picture in here. Here we go. So this is a graph, I think you're all familiar with this. in Monty we define graph as nodes at locations. nodes have features stored at them, which can be like point normals and curvature directions. Those define the pose of that node, so like the point normal and the two ortho normal, orthogonal, curvature directions basically span up a local reference frame for that point and thereby define the orientation of that point.

and then they can also store other features like color or curvature amounts. And then we can have edges in the graph, which are basically connections between the nodes, edges.

and we go some older plots. Edges can be up in, in different ways. you can either lay them down as you're sensing, so they are put down in the path that you're going over the mug or the kind of default behavior you had was, nearest neighbors. So each node would connect edges to its nearest neighbors when we add a graft to memory.

and so when we do matching, we get, we always get a sensation and then a movement and the next sensation and a movement and the next sensation, and we get those relative to the body. So we get a location relative to the body movement, next location, relative to the body movement and so on. And so when we try to recognize an object, we can either take these movements and try to match them to the edges stored in the graph. Or which is what the displacement graph LM does. Or we can take our nodes in the graph as initial hypotheses and then test the movements as hypotheses and then look at the location where we end up at.

dunno if that was the clearest explanation.

maybe it's worth describing that, point pair feature thing that was used for the displacement because, yeah, let me draw on the, because the displacement weren't, you might think of displacement as like just a vector. And so it's oh, you're just matching this movement vector to any one of these edges, which is just a vector. But, but they were more specific than that. The displacement were basically a line connecting to. Reference frames, and that was this, kind of rotation invariant structure. That's the displacement. So it's a lot more, specific than just like a random or than just like a movement. yeah. Yeah. Let me, and so if you, see PPF in the code point pair feature, that's what that's referring to, that kind of 3D structure. Yeah. So basically, let's say we're in the world. We have this blue cylinder. can you guys see what I'm drawing on? Xra? I should probably, oh, I can't even see what I'm drawing. Oh, here we go.

Maybe I'll share it like this.

So we're seeing this blue cylinder, our sensors, let's say here, and then our sensorimotor moves to here. So now we have two locations and we have a displacement between these two locations.

so now how do we use these two locations that are relative to the body in order to recognize this object, which is stored in the models reference frame? One option, which is the displacement matching alarm, is we take this displacement that we observed and we try to compare it with all of the edges that are in the mark. So it might be this one, it might be the other way around. It might be here, it like it could be this way, flipped around this way, so we can compare it to all of these edges that we have stored in the graph. And then over time we sample more and more displacement like a chain of displacement and it becomes more and more unique of where on the object we might be. And like Niels mentioned, this has a really nice property. because as we found out is, if we can rec, if our points in the graph have orientations, like this, and we have a displacement between these two points, we can represent this displacement in an orientation invariant way using point pair features. So basically we can have a unique description of this displacement that is independent of its orientation. So if this displacement is observed. Anywhere in the world, at any orientation, it will have the exact same values. It's basically the length of the displacement and then the angle, the, so it's the length and then the angles between, I think some of these points here, I forget which exactly. it's described in this, paper. I think, and just to remind myself, I guess this assumes that the, reference frames for the local points that either said are unique, as in if they were ambiguous about a certain axis or something, you would still need to like sample multiple hypotheses for different rotations.

no, you never have to sample a rotation hypotheses.

But, what if you, it's like not d like. What if it's symmetric? Like often we don't actually know, if it's based on principle curvature or if there is no principle curvature then and you just have the point normal. Oh yeah. If the principle curvatures are not defined, then yeah, you can't uniquely define the point pair feature. or even when they are defined in their symmetric, like their mirror symmetric, then they would almost be two point pair features, either two point pair features stored, or you would test them under those two hypotheses. Yeah, so I guess it, it reduces the space, but it, in practically it cannot totally eliminate the need to test multiple hypotheses of, rotation. But you would basically just store two edges in the graph if you have a, if you have, since we can't, uniquely define the curvature directions. We would just store two point pair features for every edge. Or if there's, if you we're on a flat surface and we have no principal co, like principal curvatures are equal, we would just define eight or 10 pair features for that edge. But then at recognition time, we don't have to cycle through hypotheses, we just have to compare to more point pair features in the graph. Okay. So we've kinda stored all possible hypotheses in the graph.

Yeah, exactly. Anyways, sorry, it's a bit of an aside, but, so while we're Yeah. Talking about, yeah. So this approach, that's a really nice feature because we could recognize objects independent of location, orientation at scale, without cycling through hypotheses, which we have to do at the, with the current solution that we have. So the current solution that we have is features at locations.

where basically we start out with saying, okay, I could be here, or I could be here, or I could be here. All of these become hypothesis. actually we would probably not say these three because there we would detect like an edge as a curvature. So since we're also detecting features, we only look at the ones that are consistent with features. So we might say we are anywhere around the cylinder.

oh, as if a delay. Okay. And then we take the displacement that we sensed and we start at the point where the hypothesized location would be and apply that displacement.

and then that becomes the search location. We look at the search location, in a certain radius around that search location. We find, the points stored in the graph and we clear the features that are stored at these points. And we will do this for any of these type, for these hypothesized locations. And for each location, we have some hypothesis orientations too. So here we might say, okay, let's look here, but also let's look in the other direct here. And some of them might end up totally off the object and some of them might.

and hopefully the correct ones would always end up on the object and you would observe matching features there.

The displacement one, you said, it's agnostic to scale. I didn't get that because I think you, you also mentioned that the displacement, like the length of the displacement is important. So if it was like at a different scale then like how, I think that the length would be different or no? Yeah. So basically how we did the, in that case, I know. So I will get to the big drawback of this and given that drawback you, like probably when I explained this solution, you'll see the big drawback already. But basically what we would do is we have a bunch of displacement stored in the graph, and then we get, some of them might be longer, some of them might be shorter, and then we get an incoming displacement and we would just scale it to the length of each of these. Like I. Each of those edge hypotheses would have a different scale factor. And then when we get the next hypothesis, we would apply that initial scale factor to it. if we started with this one and the next one would be like super scaled over here and it would not match this short edge here anymore, you're making use of the fact that they're all scaled by the same parameter, which is Yeah, exactly. We all get scaled the same way. Cool. Yeah.

yeah, so it's not the same orientation where the representation we use for it is just in variant orientation, but basically we can just have one scale factor for each edge and keep applying that for all, subsequent displacement.

Okay.

The last iteration, the evidence-based LM is very similar to the feature at location lm. The main difference is with the feature at location lm we would like, if we test the hypothesis and then like we look here and there's no feature observed, we would then eliminate that hypothesis from the possible hypothesis, and that was brittle with noise. so we transitioned to the evidence based L where instead of just eliminating a hypothesis, when we get one inconsistent observation, we instead keep like an evidence count for each hypothesis. And we increment that evidence count with every step.

And then there were saturations on the evidence lm, where we made it just a lot more efficient and added extra features to it. Like in the beginning, we would test every hypothesis at every step in a giant four loop, and it would take 10 hours to run, like an experiment filled with four objects.

then we, vectorized everything. Now it's all, matrix multiplications, and we only update the top 20 of hypotheses at every step or top 80.

yeah, those are some bigger updates to the evidence matching. And yeah, and I think that top 80 had probably a pretty big, like I remember you found it had a big impact on the flow, like the runtime. And it's again, I think, what we were talking about earlier, because it's not, fixed. It's not, it doesn't mean that 80 of possible points are always gonna be tested, in which case, by definition, it's only gonna reduce the compute by a fifth. It's like anything that's within 80 of the max, which might only be 10 of points, it might only be two points on an object that are that close to the max. And anyways, yeah. Yeah. Just in case it wasn't clear to anyone how that, it feels like at the beginning of it, it will be, those points that will be tested will be a lot, and as, oh yeah. All, points will be tested basically. Yeah. And then as you narrow down, it becomes, yeah. It gets fast very quickly. The first step is still quite slow, usually.

have a question. Yeah. sorry. Yeah, go ahead. Just targeting some of the code bits specifically. It, seems like in the code that the rotation for each location doesn't change. Am I wrong about that?

what do you mean? The rotation for each location? So there's a field for like locations, a field for lo sorry, locations, rotations, evidences and things like that we save with the detailed logger. And when you save at the end of episode, you get, an evidence count for every per location, per step. You get locations per location per step, but we're only seeing one rotation per location and it's not on a per step basis. Yeah. So, that's because our hypothesis is always talking about the orientation of the object. So basically. we have, maybe not green. Let me, so we have our hypothesis, and there we have, location on object, orientation of object and evidence.

And so then we have like tons of hypotheses we might say. Okay. Just, I could maybe just, sorry, I scroll down slightly on your computer. Oh, sorry. If people are watching on here. Nice.

So for example, for the location, it might say, okay, I might be here or I might be here or I might be here. And then for the orientation it's global. For the whole object, it might say, I think the cylinder is upright, or I think the cylinder is 45 degree oriented. Or I think the cylinders like 90 oriented. so as we move over the object, the location where we hypothesize we are on the object will change, which is why this changes over time. But the hypothesis orientation of the object is not changing. because if the sensors moving over the object, we still assume the object has the same orientation no matter where we put our sensorimotor on there. Does that make sense? I think so, yeah. So like it's not an orientation of that feature. Or yeah, it's an orientation that impacts that feature, like that point normal, for example. But it's not like specific to that particular feature that's being sent there. It's not like we're trying many orientations at each time step, or are we are in parallel because you'll have all these different hypotheses, initialized, and you're like, assuming you're maintaining all the hypotheses and you're not like eliminating them through like that evidence percent threshold or whatever, like the whole episode, you're gonna be like, I have that one hypothesis that the mug is upside down. I'm gonna move all locations. How does that fit with that kind of hypothesis? How does other hypothesis at this angle, how and integrating over that.

okay. And then, yeah, and so they're basically, and, that's the issue that Ramy's Kind of identified and is, working on, is the fact that that makes our post hypotheses very dependent on the first sensation because, if we sense a surface, and we know a surface can be oriented a, certain number of ways with the object model we have, but like one way if I'm sensing a surface here, one of my hypotheses is not that the object is like here or whatever, it might be like rotated about this axis. And, that's what kind of determines the initial hypothesis. I see. I think I understand. Yeah. But this is where we sample eight around a rotation and we try to select, which one of these is most exactly aligned with the first observation. Exactly. And so in most of the cases, like with the can here.

we would, be sensing, we'd have the first sensation, which has a pose, to defined by the point normally curvatures. And that pose gives us usually two possible orientations. Basically saying, if I'm on this location, on the can, and I'm sensing this curvature, the can is either upright or it's upside down because I'm sensing this curved surface. and there's no other way I could sense that on this location of the cup. if the can was turned 90 degrees than the first principle, curvature would also be rotated 90 degrees.

and so yeah, the only exception to that is, like Neil mentioned, if we're on a flat surface or a circular surface, then the principle curvatures are equal. So they don't tell us anything about the directions in which they point. Okay. And, then the nice thing is even then we don't like uniformly sample all possible rotations of the object.

if I'm sensing this, although it could be rotated about the Axi, I don't sample, this is a possible hypothesis, this is a possible, blah, blah, blah. That, that is something you can do in the code, which I think is called uniform hypothesis sampling. yeah. But even then, in order to make that tractable, it does it at increments of 30 degree orientations. Or something like that. So in practice it doesn't really do a great job as well as being computationally expensive. Got it. Yeah. You always have a point normal. So that already tells you a lot about the potential orientations of the object.

Okay. So yeah, we have a bunch of hypotheses and we can update all of them at the set, at each time step. And we can do all of that as like one large matrix multiplication.

which, what do we do at the moment?

hypothesis by default, sampled as all of the points on the, in the graph, or are we sampling from the points on the graph?

yeah. So right now the way we initialize this hypothesis basis, we add one hypothesis for the location, for each of the points in the graph. Okay. And then for each of these locations, we add either two or I think eight, possible orientations depending on how the pr principal curvatures are defined. Okay. So if the, graph is too dense, we'll have too many hypotheses. And if it's too spar. Yeah, exactly. Yeah. And, I guess, yeah, it's worth mentioning that, yeah, when the hypotheses are initialized for that reason, they're on the nodes in the graph. But once we start moving, of course there's no guarantee that we're gonna be on top of exact exactly where a node in the graph is, and that's where the kind of nearest neighbor matching starts coming in.

yeah, and one thing that I guess, yeah, we talked about a long time ago is to re-anchor hypothesis. So basically, like you say, right now, if the graph is too dense, you have way too many hypotheses. But also if the graph is too sparse. You have too few hypotheses. Like what Neil said, if I'm only starting with, these points, these few points that I drew in this illustrative graph, but actually my sensorimotor first sense down here, I'm drawing Green Point, but it's taking time to show up. I'm sensing down here, like far away from these other points and then I'm moving.

it, I'll have a harder time recognizing that object. So one thing that could be done is, like when you sense very distinct features on an object, like the point where the handle meets the cup or I don't know, some other distinct features, you could re-anchor two distinct features stored in the cup. and that could help with that. But yeah, we, haven't really gotten, very deep into that idea.

just to wrap it up on the displacement matching, problem, I don't know if everyone is already aware of it. but basically the issue is in order to recognize this object, you have to sample the displacement that are stored in the cup. You can't sample other displacement. So if I sample this green point, there's already no chance for me to recognize this cup. Basically, if I move like over here and then over here, like there are just no displacements that match in the graph. So I would just not be able to recognize this object.

and that's a pretty big limitation because in order to deal with that, we would have to have a very dense graph with an all to all sampling of edges, which is just a combinatorial explosion. And yeah, just, it just didn't seem tractable.

one thing we talked about is what we thought about is maybe at some point having a hybrid approach where we store like significant displacement in the graph. Like a face you would store like displacement between eyes and the nose and the mouth. and then you store features at locations. And that way you could very rapidly make a general inference of the object, like quickly in, for a phase. If you move from eye to nose, you could have action policies that are aimed for sampling these specific displacement. but you could still recognize the face if you made a different series of displacements, using the feature location approach. But yeah, that's where this idea got killed, so yeah, here's the comparison. So basically all of the three approaches are location, variant. All of them are rotation invariant. Although features at locations need to explicitly test different rotations. only the space model is scaling varying, with these, I guess we could explicitly just scale as well as a hypothesis, but we've never tried that and it, would add a lot more computations, like it would scale linearly.

we can't sample new displacement with this one. We can do that with, the features at locations approach because we have a reference frame of locations that we can interpolate between, we can sample new locations as well. We don't have to sample the exact nodes stored in the graph, we can sample any on the object. dealing with noise was only really possible with the evidence-based approach. and another nice advantage of the evidence-based approach is that can give you a most likely hypothesis at every step. So with the other two approaches, which are I guess maybe a bit more like HTM, you have a union of possible, matches at every step like this. All that's possible. And then if you get an inconsistent observation, that gets removed from the Union of Possibilities. But with the evidence-based approach, you always have a most likely hypothesis. Even if you're not sure what you're sensing yet, you can start making, like model-based, actions on test hypothesis for instance. Does that make sense?

Yeah, maybe it's worth, yeah, it was really nice overview. Maybe it's worth talking a bit about the, transformation of information coming in because that also relates to the thalamus stuff we were talking about last, brainstorming. And I think that's something that, that can be confusing in the code is like these kinds of transformations of features and stuff.

Yeah.

maybe I'll just drop here.

How to best explain, because I guess the thing that we were talking about just now, we have this kind of global hypothesis for the rotation of the whole object that each hypothesis you can think of as a different, that's like a reference frame. We have an orientation for the object and we're moving through that. We're getting these features that oppose coming in, but those are initially in a sensors reference frame.

Yeah.

let me ma make the nerve analogy real quick first and the thalamus, 'cause we mentioned it.

so we have incoming location and orientation relative to the body.

and in layer six we would have a hypothesis of the objects, location and orientation.

So that would be hypothesis of where we are on the object and how the object is oriented relative to the internal model of the object. And so that hypothesis, we have the backward portion from layer six to the, and the, theory is that backward projection can modify the input that goes to the relay cells and then rotate that input that then goes into layer four, and other layers.

so basically this is where the transformation would happen between the objects reference frame and the body reference frame. So now where does this happen in Monty?

maybe I should, show this in the code in a moment, but, yeah, basic, I guess we get to your point, Neil, about having different rotations and orientation hypotheses of each object.

can I copy something on Ali drawing?

Yes. Awesome. Okay. So we have all these hypotheses.

we have, the incoming location and orientation.

technically in Monty we have the buffer, which calculates the displacement, in the cortex. We might just get the displacement as input.

but yeah, for a moment, let's just talk about location orientation that comes in.

so I'm waiting for my iPad to update the, drawing. but, so basically we have one sensation, it's in body centric reference frame, and we have all of the hypotheses that we wanna test.

and what we basically do is we take this one sensation, we multiply it with this large hypothesis matrix, and we get an output of all the new hypothesis.

this might not be so easy to draw. Maybe I'll just go to the code for it.

yeah, and I don't know if it would be helpful if, we can make it more concrete in terms of say the, yeah. With the sensorimotor module, it's getting a, depth map and then it's extracting this point cloud and then from the point cloud and it's extracting point normal and principle curve directions. So that's gonna be a location and like a, mini reference frame.

but then we're combining that with information from Habitat about where the sensor is.

that's the sort of body centric, location. I believe that we start with to get the, body centric location.

Yeah. As in like the, what we do, the transform the location that's actually passed in.

y you mean what we do in the transform? Yeah. That to 3D location form.

Yeah. Like the coordinate system. When we say that's body centric, I think it's really habitat centric or Yeah, I think, yeah, in this case it's relative to the origin of habitat. Of habitat. Yeah. It's like a, it's an external kind of coordinate system, but in a robot it would, be relative to, the torso or the hand or something like that. Yeah. So we, there's this variable called world coordinates and you can turn it off and on.

yeah, whether you want it to be in world coordinates or, not. and basically what it does, if it isn't world coordinates, it takes into account the, it gets the sensor locations and orientations and agent location orientations in the world, and then applies those transformations, to the point cloud that we're sensing, to turn them into world coordinates or like basically to calculate out the sensorimotor and agent movement from the point cloud that the camera image is getting.

Because from the camera image Yeah. That image. And that doesn't tell us where in the world it is at all.

Yeah. And then, but then I guess the nice thing about Monty, because it's using an object centric, recognition system with movement, we don't need to do that. You could just have the location could literally be in like the coordinate system. Like it just needs to be consistent across movements. that we know the orient orientation of the sensorimotor and that we have the movement information.

if, my incoming location is if, my location and orientation is relative to my fingertip, I feel something here. As long as I have a movement, the location doesn't really matter, but the orientation is what needs to be tracked.

because we're gonna integrate it in, in an internal, reference frame.

You mean you're talking about it's not to just send displacement.

Yeah. Displacement and, orientations. But it's, not displacement. It's like movements. It's not like a displacement, like we're matching an edge. It's just like we've moved through, space. placement to me always includes location and orientation changes. yeah. So if I'm just talking about location changes, I'm talk, I would say translation. but displacement, already includes an orientation change. if I rotated my finger and moved it that would be included in the displacement. But yeah, we talked about before whether we can just, just communicate placements instead of locations in a common reference frame. And I, there are these issues with it where like it'll make interaction with the environment very difficult, right. Because you don't know where in the world you are.

yeah, and like voting and stuff like that. No, that's true. Yeah. But yeah, I think that's more on the like sensorimotor module stuff. so yeah, maybe I'll focus on the evidence module for now and then we can, get back to that, sometime. But yeah, I think we talked about it before also in the sense of whether that's maybe a difference between the where and the what pathway that The what pathway does access to, body centric coordinates. For common coordinates. It just gets displacement maybe. But yeah, I don't know. That's very speculative.

But yeah. So I guess in terms of the code in general, it's this world coordinate thing, which is just like common reference frame.

Yeah.

so yeah, we get these locations in a common reference frame and then we call update possible matches, which loops over, objects in memory. we use multithreading for this in most cases. since we can update the evidence for each object in parallel or total independent. The brain could do this in parallel too. and we call update evidence. the dark string, helps explain everything a bit. I would basically start with zero evidence for all of the hypotheses. So a flat prior could be different in the future. if I'm in the kitchen, I have some priors that I will see certain things there, and won't see certain other things.

but we start with zero evidence for anything, for everything. and then the features and displacement either add or subtract evidence.

I think this should say pose features.

and then features like color can only add evidence. They can subtract evidence. That way we can recognize the same morphology in different colors, and then. Evidence is weighed by the distance of hypotheses to the point in the model. there are also votes which are handled somewhere else. And here, this is the point of maybe at some point we do a hybrid approach where we can also use displacement to, infer like an objects orientation more rapidly.

if we're on the step, we initialize the hypothesis space, and initialize the evidence using the first observed feature. otherwise we update the hypothesis. So that's what we, do here. So if the displacement is none, so we have not moved yet, we basically call, get initial hypothesis space. to get that we use the fe features that we observe, which are like the point, normal and curvature direction.

And we update the first evidence for it. the more interesting part, what we mostly do, we have actually moved already. So now, we go here, we have a displacement, and we do a couple of, yeah. Alright, so we, this is a bit detailed on like the different channel input channels.

but basically this is the interesting part. We have all of these possible poses, which are orientations. and in order to test this displacement, we have to rotate the displacement. By each of the rotation hypotheses. So basically this is a matrix of different rotation matrices.

and we multiply, like we take the dot product of these rotation matrices and the incoming displacement, and then we have to calculate the search locations, which is where in the graph do we wanna check the stored features? Where might we be after this displacement? in, in order to get those search locations, we take a location hypothesis, and we add the rotator displacement to it.

so yeah, let me draw this real quick.

And maybe I can just find it on the screen. so hang on. I think there was also, yeah, I was gonna say there was some figures in the paper that might be worth using. Yeah.

So that list of possible poses that is changing right. On each time step and, no possible poses stay the same at every time step. Only the evidence for them changes. Okay. But possible locations update. So basically, possible pose is just used to get a list of rotated displacement. That's like a temporary variable that we only use in this step. self thought possible poses is not modified. And then we calculate search locations by taking the possible locations and adding the rotated displacement on them. So basically we have an observation here, this pose and a displacement. And we have all of these possible locations on the cylinder that we could be at, and we take this displacement and we rotate it by the post hypotheses and add it to that location.

hang on. This is the first step. So this's just initializing it as show the search location. But then we have these, like for e we have initialized post hypothesis for every location on the object, or several of them, this point has two possible orientations of the object. If I'm at this location and the cylinder, it's either, upside, right side up or upside down. and then we get the displacement, use the displacement to rotate, use the post hypothesis to rotate the displacement. We add the displacement to the hypothesis location, and that's the search location. So you can see here.

if I was at this location here, I hope you can see my pointer. If I was at this location here, I might now either be up here or down here. And if I was at the top of the cylinder, there are more hypotheses. So there we have this, these kind of circles of where we might be next. And that's why in like these animations, the search locations or the hypothesis can go off the object because a lot of them will be wrong. And a lot of them, when we actually apply, the displacement will end up off of the object.

and then we look at the features stored at these posts, at these search locations. And for instance, if they're actually off of the object, that's negative evidence, low likelihood, if the feature doesn't match, that's like the color's wrong. That's. No evidence for that. If the color is right and the features are right, that's high evidence like here. and then we do the same thing. So now we moved actually like sideways. So again, we have all of these different hypotheses of where we might be and what the rotation would be. we apply the rotation to the displacement, draw a line here, give us the search locations. At each of these points, we look in the graph. How do the points store nearby in the graph compare to the observed features? And we use that to update the evidence. Do we compare to the average of these points, the closest KS or do we compare it to just the, best one? Yes. Good question. So basically, we have a search radius. So here's the example of, Hypothesis that we're at this location, there are two orientations. We have this displacement. We rotate the displacement by the post hypotheses. We get two possible locations, and for each location we look in a certain search radios, we look at all the points in the radio and update the evidence. Like we calculate the distance one between the search location and the point in the graph, and also the feature difference between the points in that. And that gives us kind of an evidence value for each of the points in the radius. And then we take the best match within that. So the maximum value Okay. is it do any better if we do, with the average or, like no, it does worse with the average because, the find us. Like you might be in an area on the object where features change quickly, like right before the edge of the mug. So you would actually get quite negative evidence if you compare it to the, points in the graph up there. Or if you have a very flip object, you might actually have point normal set are opposite, storage in that search radios, you don't wanna, you don't want that to drag down your evidence if there's something that matches your observation in that radios, that's evidence for this object. Okay, that makes sense.

and so when there's some, so when you do find that you've done a displacement, you find a point that matches nicely, which location has its evidence updated? The one you left from, or the one you arrived at?

evidence. Yeah. So ba location basis, right? So yeah, so basically, this row here in the hypothesis, the possible locations on the object gets updated at every step. So with every displacement we update where we might be on the object.

so basically this evidence keeps count of like basically evidence for path that we took on the object.

or yeah, to answer a question, it would be the evidence for the location that we ended up at. Okay. So the evidence for that, we actually are at that search location that we tested.

And if we did something like re-anchoring, it might be changing the location to the point where we get the maximum feature match. Exactly. Yeah. Yeah. Rather than rather our location being like the point somewhere in space that we think we are after path integration. Yeah.

there some more detailed things I think. Yeah, it's in the documentation but not in the paper. But basically the search radios can be informed by the sensed curvature. So if we have a very flat surface that we're sensing, we don't really need to sample points in a circle sphere. We can sample points along the surface, only so we can use the, point normal that we are sensing to inform whether like we, we can use the point normal to squish. The search radios from a, circle into a sphere that is like going along the surface of the object.

if that makes sense.

So basically we're like, how we do it on a technical level is we adjust like our distant distance measure. like the way we weigh the distance, the search point to other points in the graph is, being squished by, the point normal direction. Okay. so here we threshold, like on the flat surface, we would get, only points in the graph that are actually on a, on the surface. And then if it's, like a round curvature, then we do it more of a circular search.

So then we have all of the search locations. Then this is where we do the evidence update. Thresholding. That's the part that's for efficiency, that we don't need to actually update all of the hypothesis, only the most likely ones. so get a threshold, this where was, we get hypothesis IDs to test.

and then yeah, if there actually are hypothesis to test, which might always be the case, if it's an object that's already very impossible, we will not test anything.

we will then get the search locations that we wanna test. and yeah, we calculate the evidence for these search locations using the features that were observed, and give those evidence. We clip that evidence to not be small or zero.

and yeah, basically add the evidence to the existing evidence, and weigh it by like the past weight and the present weight.

and that's the part Ramy that, you played around with, last week. Basically, if past weight and present weight add up to one, then the evidence is bounded. It will never go outside of the range minus one and two. If past and present weight add up to more than one, it's unbounded in the current default setup. Both are set to one, so they add up to two. So evidence can grow infinitely high in theory, which I. Basically, if we, bind the evidence values, we have a finite memory horizon. And with the current action policies, that doesn't work so well because basically the memory horizon is too short to actually explore a large part of the object or to actually sense the whole shape of the object. but eventually I think this is the more elegant solution, and how the brain must be doing this. 'cause yeah, neurons can't fire infinitely much, or like you have like hysteresis, which is bounded, I would say.

but yeah, I think this, only a bounded evidence values only really work well if you have either a very efficient, action policy or some kind of replay of. past significant features or something like that. Yeah. And maybe with like hierarchy as well and more unique features, that would help as well, because yeah, right now everything is sensing point normals, in kind of local surfaces. And yeah, even if you jump to the other side of an object, you're still gonna feel a point normal. Like it's a, the displacement will be different for different objects and stuff like that, but it's still not that unique. It's not like you move somewhere and it's oh, this is a handle and something very, yeah. Yeah.

In general, it, it fits well with, Will's strategy during the TBP Olympics that you want to, if, if you're not getting very good features coming in.

That's right. Yeah.

so yeah, I feel like there's a lot more to cover, but I've already been talking for about an hour or so. I don't know if we should take a break at some point and keep going at some other point, or if you wanna ask some specific questions.

yeah.

Does it ever happen that the search radiuss, doesn't have any points to test? And then how does, how do you handle that?

yeah, it doesn't, just don't, yeah. It's basically if you, yeah, if you end up off of the object, there'll be nothing in there and you get minus one evidence.

but you could be a very course model and you're not off the object, but you're, on the surface. But the model is to course.

yeah, so that's why you have to set that. so we have this parameter called max match distance, and that's basically like the radius of the search thing. And it is usually set pretty large, like for the coffee mug, I think it's like a fifth or something between a fifth and a 10th of the height of the coffee mug. as far as I remember. So it's like definitely way bigger than the distance between points in the graph. if you set that too small then, that problem, can definitely happen. But, so basically as you make the, graph more sparse, you would have to, if you make it too sparse, you would have to increase the max match distance, but you would have to make it bearish for that. So ideally, we would wanna make it, as a function of the ness or the sparsity of the points in the graph.

Yeah. That could be idea. Yeah.

Yeah, that's actually a great idea. I've, been trying to start thinking about if we build a platform for this, we don't want people to have to adjust all of these different parameters and understand them and do we simplify this thing? So yeah, making the max match distance just a function of sparseness of the graph or this distance between points in the graph that, that would be, I think that would work well.

it also could be a learned thing, right? Because. each object could come with its own distance. 'cause depends because you're only matching what you learned. Yeah. So once you learned and determined at that point you determine what the distance is and that for you always use that distance for that object. I, right? Yeah. Yeah. So yeah, I think it would make sense to have that, like an object specific parameter probably. Or at least yeah, something from the object model function. one topic I didn't get into at all is like the object models and constraint graphs versus unconstrained graphs. but that's another topic. But basically we have already other parameters for graphs. Like how large can that size wise, how, many points can they have at max? and. What else? Yeah. How much spatial resolution can they have at max? So the max match distance could be, based on one of these parameters as well.

one more question. I, noticed that the evidence is split, it's split by the graph IDs and that results in the need for this, for loop over the objects. And I'm wondering if it's more efficient to vectorize everything and have something similar to the channel mapping hypothesis, whatever, just to know where, which, which hypothesis are, for this graph Id make something separate and basically just have vectorize all of the evidences. would that make it more efficient or what would be the problems in doing that?

yeah, that's an interesting question.

off the top of my head, I don't see an issue with doing that. I'm sorry, Ramy, can you repeat the question? Vectorize the evidences, for, yeah, that part. So now we have to do this for loop over all of the evidences and then we are just updating a graph ID by graph id. I think we're doing it parallel, but it seems like it'll be more efficient to have all of the evidences in one vector and then we can just apply. So basically when we think about hypothesis, you'll only be in one vector instead of separated by the graph ID so that we don't have to loop over them. it's the same, same efficiency, step that Viviane took to go, to basically high. She went one step into, grouping all these hypothesis together and making them one vector and then applying the transformations on that one vector instead of a for loop. But now we're doing it another step where we would have all of the graph ID hypothesis together, in one vector, and then we could just apply one transformation. We're have to do this for, loop, for the graphs. It'll be especially helpful when we have a lot more, objects we won't have to look. Does that make sense? Yeah. I guess in gen, the, what if the number of objects changes? I guess it, would it still work then? If so, then I think it makes sense. Yeah, it's basically the same cases for the input channels. I never noticed the parallels because I did those things at totally different times. but yeah, like Ramy says, for the input channels, we, basically put up possible location and orientations for the channels into one large vector. And we just store the mapping between them, like which IDs correspond to which channel. and if we add another input channel, the case that we mentioned, that Ra Ramy mentioned earlier, where we add a hypothesis to the hypothesis space or a input channel, we just append to all these lists, to the mapping and to those, and we could do the same thing, for over graph IDs as well.

I don't know if at some point, like hardware wise, you run into some limits. You don't wanna do the matrix multiplication that large anymore, but Yeah. Yeah. I don't know. Yeah, I think, especially if we're using GPUs at some point, then probably the bigger the matrices the better up to a limit.

and, yeah, I guess question what that limit would be. Yeah. Yeah. And in general, I think resizing, tensors is, not as trivial as like appending to lists 'cause it needs to reallocate, memory. But, actually, I don't know. Maybe it's, fine.

but yeah. Yeah, I think we could definitely explore something like that at one point to accelerate it further.

Yeah, then we could do multi threading over learning modules instead.

Interesting idea. Yeah. It would be a two level, mapping, instead of that, so we'd have to the graph ID and then from the graph ID to the channels or, I could we just have two separate mapping. yeah.

Yeah. And I guess right now with the, only testing some of the hypotheses that kind of, dynamically builds smaller, vectors, right? That we then, update, yeah, basically we have the evidence threshold, which gives us hypothesis IDs to test, and then we index with these IDs to get a new list of search locations. Create a new, yeah. I guess that would be a bit prob problematic. We would then, if we do it for all of the objects in the same thing, we would then have to separate out the search locations into the differents reference frames to test them, or we would, yeah. So we don't have a ragged list, a ragged array, because each one have a different number of locations.

Yeah, we would have to separate them into separate arrays, so maybe at that point it wouldn't be more efficient anymore. alternatively we could do the kind of biological whatever where, we have one giant reference frame and there at very far locations from each other.

Yeah. In a fixed capacity almost, or, yeah, yeah. Yeah. I think it would be a bit more involved than just applying the same mechanism as to the input channels.