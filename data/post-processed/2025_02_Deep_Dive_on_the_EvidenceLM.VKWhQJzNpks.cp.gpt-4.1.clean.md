There are several things I can go over. One is the figures and material in the white paper. Everyone on the research team should be very familiar with them and how they work. If that would be helpful, I can review them so you know how to explain them to others. Another thing I thought would be useful to start with is a bit of a history lesson on the graph learning module, since it provides background that helps frame discussions we often have, like the displacement matching versus feature set location matching question. I might actually start with this one if no one objects. I think that's a good idea. Also, the code evolved in this way, and in general, I think that's useful context. You'll encounter material from all of them when you go through the code. Lastly, I definitely want to go over the evidence graph LM code, at least the part about what attributes we have and how they interact and affect matching. I started a blank X calendar draw in case people want to ask questions on the whiteboard or if I need to draw something. I'll share the link in the Slack coding channel if anyone wants to join.

Let me start with a brief history of graph matching in Monty.

This is a writeup. It's on old Leaf, but the PDF is also in our Google Drive.

We have three types of learning modules in Monty at the moment: the displacement LM, the feature LM, and the evidence LM. Displacement graph LM uses edges in the graph. Let me see if the graph picture is here. Here we go. This is a graph, which I think you're all familiar with. In Monty, we define a graph as nodes at locations. Nodes have features stored at them, such as point normals and curvature directions. These define the pose of the node, so the point normal and the two orthogonal curvature directions span a local reference frame for that point and define its orientation.

They can also store other features like color or curvature amounts. We can have edges in the graph, which are connections between the nodes.

We have some older plots. Edges can be created in different ways. You can lay them down as you're sensing, so they are put down in the path you're moving over the mug, or the default behavior is nearest neighbors. Each node connects edges to its nearest neighbors when we add a graph to memory.

When we do matching, we always get a sensation, then a movement, then the next sensation, and so on, relative to the body. We get a location relative to the body movement, next location relative to the body movement, and so on. When we try to recognize an object, we can either take these movements and try to match them to the edges stored in the graph, which is what the displacement graph LM does, or we can take our nodes in the graph as initial hypotheses, test the movements as hypotheses, and look at the location where we end up.

Maybe it's worth describing the point pair feature used for the displacement. You might think of displacement as just a vector, matching this movement vector to any one of these edges, which is just a vector. But they were more specific than that. The displacement was basically a line connecting two reference frames, and that was a rotation-invariant structure. That's the displacement. It's more specific than just a random movement. If you see PPF in the code—point pair feature—that refers to that kind of 3D structure. 

Let's say we're in the world and have this blue cylinder. Our sensor is here, and then our sensorimotor moves to here. Now we have two locations and a displacement between them.

How do we use these two locations, relative to the body, to recognize the object stored in the model's reference frame? One option, which is the displacement matching LM, is to take this observed displacement and compare it with all the edges in the model. It might be this one, or the other way around, or flipped. We can compare it to all the edges stored in the graph. Over time, we sample more and more displacements, forming a chain, and it becomes more unique as to where on the object we might be. This has a nice property: if our points in the graph have orientations and we have a displacement between them, we can represent this displacement in an orientation-invariant way using point pair features. We can have a unique description of this displacement that is independent of its orientation. If this displacement is observed anywhere in the world, at any orientation, it will have the same values. It's basically the length of the displacement and the angles between some of these points. It's described in the paper. This assumes that the reference frames for the local points are unique. If they were ambiguous about a certain axis, you would still need to sample multiple hypotheses for different rotations.

No, you never have to sample a rotation hypothesis.

What if it's symmetric? Often we don't actually know if it's based on principal curvature, or if there is no principal curvature and you just have the point normal. If the principal curvatures are not defined, then you can't uniquely define the point pair feature. Even when they are defined and are mirror symmetric, there would be two point pair features. Either you store two point pair features, or you test them under those two hypotheses. It reduces the space, but in practice, it cannot totally eliminate the need to test multiple rotation hypotheses. You would basically just store two edges in the graph if you can't uniquely define the curvature directions. We would store two point pair features for every edge. If you're on a flat surface and the principal curvatures are equal, you might define eight or ten pair features for that edge. At recognition time, you don't have to cycle through hypotheses; you just compare to more point pair features in the graph. We've stored all possible hypotheses in the graph.

That's a nice feature because we can recognize objects independent of location, orientation, and scale, without cycling through hypotheses, which we have to do with the current solution. The current solution uses features at locations.

We start by saying, "I could be here, or here, or here." All of these become hypotheses. We probably wouldn't say these three because we would detect an edge as a curvature. Since we're also detecting features, we only look at the ones consistent with features. We might say we are anywhere around the cylinder.

Then we take the displacement we sensed, start at the hypothesized location, and apply that displacement.

That becomes the search location. We look in a certain radius around that search location, find the points stored in the graph, and clear the features stored at these points. We do this for each hypothesized location. For each location, we have some hypothesis orientations too. We might look here, but also in the other direction. Some might end up totally off the object.

Hopefully, the correct ones always end up on the object, and you observe matching features there.

You said the displacement is agnostic to scale. I didn't get that, because you also mentioned the length of the displacement is important. If it was at a different scale, wouldn't the length be different? Basically, we have a bunch of displacements stored in the graph. Some might be longer, some shorter. We get an incoming displacement and scale it to the length of each of these. Each edge hypothesis has a different scale factor. When we get the next hypothesis, we apply that initial scale factor to it. If we started with one and the next is super scaled, it wouldn't match the short edge anymore. You're making use of the fact that they're all scaled by the same parameter. Exactly, they all get scaled the same way.

It's not the same orientation; the representation we use is invariant to orientation, but we can just have one scale factor for each edge and keep applying that for all subsequent displacements.

The last iteration, the evidence-based LM, is very similar to the feature-at-location LM. The main difference is that with the feature-at-location LM, if we test a hypothesis and don't observe a feature, we eliminate that hypothesis, which is brittle with noise. So we transitioned to the evidence-based LM, where instead of eliminating a hypothesis after one inconsistent observation, we keep an evidence count for each hypothesis and increment it with every step.

There were improvements to the evidence LM, making it more efficient and adding extra features. In the beginning, we tested every hypothesis at every step in a giant for loop, which took 10 hours to run an experiment with four objects.

Then we vectorized everything. Now it's all matrix multiplications, and we only update the top 20 or top 80 hypotheses at every step.

Those are some bigger updates to the evidence matching. The top 80 had a big impact on runtime. It's not fixed; it doesn't mean 80 possible points are always tested. Anything within 80 of the max might only be 10 points, or even two points on an object that are that close to the max. At the beginning, all points are tested, but as you narrow down, it gets fast very quickly. The first step is still quite slow, usually.

I have a question. Just targeting some of the code bits specifically: it seems like in the code, the rotation for each location doesn't change. Am I wrong about that?

What do you mean? The rotation for each location? There's a field for locations, a field for rotations, evidences, and other things we save with the detailed logger. At the end of the episode, you get an evidence count per location per step. You get locations per location per step, but we're only seeing one rotation per location, and it's not on a per-step basis.

That's because our hypothesis always refers to the orientation of the object. We have our hypothesis, which includes location on the object, orientation of the object, and evidence. We might have many hypotheses. For example, for location, it might say, "I might be here, or here, or here." For orientation, it's global for the whole object—it might say, "I think the cylinder is upright," or "I think the cylinder is 45 degrees oriented," or "I think the cylinder is 90 degrees oriented." As we move over the object, the hypothesized location changes, but the hypothesis for the object's orientation does not change. If the sensor is moving over the object, we still assume the object has the same orientation, no matter where we put our sensorimotor on it.

It's not an orientation of that feature; it's an orientation that impacts that feature, like the point normal, for example. But it's not specific to that particular feature being sent. We're not trying many orientations at each time step, or we are in parallel because you'll have all these different hypotheses initialized. Assuming you're maintaining all the hypotheses and not eliminating them through an evidence percent threshold or similar, throughout the episode, you might have a hypothesis that the mug is upside down and move all locations. How does that fit with that kind of hypothesis? How do other hypotheses at this angle integrate over that?

That's the issue Ramy identified and is working on: our post-hypotheses are very dependent on the first sensation. If we sense a surface, and we know a surface can be oriented a certain number of ways with the object model, but if I'm sensing a surface here, one of my hypotheses is not that the object is here or whatever—it might be rotated about this axis. That determines the initial hypothesis. This is where we sample eight around a rotation and try to select which one is most exactly aligned with the first observation. In most cases, like with the can, the first sensation has a pose defined by the point normal and curvatures, and that pose usually gives us two possible orientations. If I'm on this location on the can and sensing this curvature, the can is either upright or upside down because I'm sensing this curved surface, and there's no other way I could sense that on this location of the cup. If the can was turned 90 degrees, the first principal curvature would also be rotated 90 degrees.

The only exception is, as Neil mentioned, if we're on a flat or circular surface, then the principal curvatures are equal, so they don't tell us anything about the directions in which they point. Even then, we don't uniformly sample all possible rotations of the object. If I'm sensing this, although it could be rotated about the axis, I don't sample every possible hypothesis. That is something you can do in the code, called uniform hypothesis sampling. But even then, to make it tractable, it does it at increments of 30-degree orientations. In practice, it doesn't do a great job and is computationally expensive. You always have a point normal, which already tells you a lot about the potential orientations of the object.

We have a bunch of hypotheses and can update all of them at each time step, as one large matrix multiplication.

Are hypotheses by default sampled as all the points in the graph, or are we sampling from the points on the graph?

Right now, the way we initialize the hypothesis basis is by adding one hypothesis for the location for each point in the graph. For each of these locations, we add either two or eight possible orientations, depending on how the principal curvatures are defined. If the graph is too dense, we'll have too many hypotheses; if it's too sparse, we'll have too few. When the hypotheses are initialized, they're on the nodes in the graph, but once we start moving, there's no guarantee we'll be exactly on a node, and that's where nearest neighbor matching comes in.

One thing we discussed a long time ago is re-anchoring hypotheses. If the graph is too dense, you have too many hypotheses; if it's too sparse, you have too few. For example, if I'm only starting with a few points in an illustrative graph, but my sensorimotor first senses far away from those points, I'll have a harder time recognizing the object. One thing that could be done is, when you sense very distinct features on an object, like where the handle meets the cup or other distinct features, you could re-anchor to those features stored in the cup. That could help, but we haven't explored that idea deeply yet.

To wrap up on the displacement matching problem, the issue is that in order to recognize this object, you have to sample the displacements stored in the cup. You can't sample other displacements. If I sample this green point, there's no chance for me to recognize this cup. If I move over here and then over there, there are just no displacements that match in the graph, so I wouldn't be able to recognize this object.

That's a significant limitation because to address it, we would need a very dense graph with all-to-all sampling of edges, which leads to a combinatorial explosion. It just didn't seem tractable.

One idea we considered was a hybrid approach where we store significant displacements in the graph, like in a face you would store the displacement between the eyes, nose, and mouth, and then store features at locations. This way, you could rapidly make a general inference of the object. For a face, if you move from eye to nose, you could have action policies aimed at sampling these specific displacements, but you could still recognize the face if you made a different series of displacements using the feature location approach. That's where this idea ended. Here's the comparison: all three approaches are location variant, all are rotation invariant, although features at locations need to explicitly test different rotations. Only the space model is scaling variant; we could explicitly scale as a hypothesis, but we've never tried that, and it would add a lot more computation, scaling linearly.

We can't sample new displacements with this one. We can do that with the features at locations approach because we have a reference frame of locations that we can interpolate between. We can sample new locations as well; we don't have to sample the exact nodes stored in the graph, we can sample any on the object. Dealing with noise was only really possible with the evidence-based approach. Another advantage of the evidence-based approach is that it can give you a most likely hypothesis at every step. With the other two approaches, which are maybe a bit more like HTM, you have a union of possible matches at every step. If you get an inconsistent observation, that gets removed from the union of possibilities. With the evidence-based approach, you always have a most likely hypothesis. Even if you're not sure what you're sensing yet, you can start making model-based actions to test hypotheses, for instance. Does that make sense?

Maybe it's worth talking a bit about the transformation of information coming in, because that also relates to the thalamus discussion from the last brainstorming session. That's something that can be confusing in the code—these kinds of transformations of features.

Let me make the nerve analogy real quick, since we mentioned the thalamus.

We have incoming location and orientation relative to the body.

In layer six, we would have a hypothesis of the object's location and orientation.

That would be a hypothesis of where we are on the object and how the object is oriented relative to the internal model of the object. That hypothesis has the backward projection from layer six, and the theory is that this backward projection can modify the input that goes to the relay cells, rotating that input before it goes into layer four and other layers.

This is where the transformation happens between the object's reference frame and the body reference frame. Where does this happen in Monty?

In Monty, we have the buffer, which calculates the displacement in the cortex. We might just get the displacement as input.

For now, let's just talk about location and orientation that comes in.

We have one sensation in the body-centric reference frame, and we have all the hypotheses we want to test.

We take this one sensation, multiply it with this large hypothesis matrix, and get an output of all the new hypotheses.

With the sensorimotor module, it's getting a depth map, extracting a point cloud, and from the point cloud extracting point normals and principal curve directions. That's a location and a mini reference frame.

Then we combine that with information from Habitat about where the sensor is.

That's the body-centric location we start with.

When we transform the location that's passed in, the coordinate system is body-centric, but in this case, it's really habitat-centric—relative to the origin of Habitat. In a robot, it would be relative to the torso or the hand. There's a variable called world coordinates, and you can turn it off and on.

Whether you want it to be in world coordinates or not, if it isn't in world coordinates, it takes into account the sensor locations and orientations and the agent's location and orientation in the world, then applies those transformations to the point cloud being sensed to convert them into world coordinates. This essentially calculates the sensorimotor and agent movement from the point cloud that the camera image is capturing.

The camera image itself doesn't tell us where in the world it is.

The advantage of Monty, since it uses an object-centric recognition system with movement, is that we don't need to do that. The location just needs to be consistent across movements, as long as we know the orientation of the sensorimotor and have the movement information.

If my location and orientation are relative to my fingertip and I feel something, as long as I have the movement, the location doesn't really matter, but the orientation needs to be tracked.

We're going to integrate it in an internal reference frame.

You're talking about not just sending displacement, but displacement and orientations. It's not just displacement like matching an edge; it's about moving through space. Displacement includes both location and orientation changes. If I rotate my finger and move it, that's included in the displacement. We discussed whether we could just communicate placements instead of locations in a common reference frame, but there are issues with that, as it would make interaction with the environment difficult because you wouldn't know where you are in the world.

Voting and similar processes are affected by this. That's more related to the sensorimotor module, so I'll focus on the evidence module for now. We also discussed whether this might be a difference between the "where" and "what" pathways—the "what" pathway might only have access to body-centric coordinates and just get displacement, but that's speculative.

In terms of the code, there's this world coordinate concept, which is just a common reference frame.

We get these locations in a common reference frame and then call update_possible_matches, which loops over objects in memory. We use multithreading for this, since we can update the evidence for each object independently. The brain could do this in parallel too. We call update_evidence. The dark string helps explain everything a bit. I would start with zero evidence for all hypotheses—a flat prior, though this could change in the future. For example, if I'm in the kitchen, I have priors about what I might see there.

We start with zero evidence for everything, and then features and displacement either add or subtract evidence.

This should say pose features.

Features like color can only add evidence; they can't subtract evidence. That way, we can recognize the same morphology in different colors. Evidence is weighted by the distance of hypotheses to the point in the model. There are also votes, which are handled elsewhere. At some point, we might use a hybrid approach where displacement helps infer an object's orientation more rapidly.

When initializing, we set up the hypothesis space and initialize the evidence using the first observed feature. Otherwise, we update the hypothesis. If displacement is none—meaning we haven't moved yet—we call get_initial_hypothesis_space using the observed features, like point, normal, and curvature direction, and update the first evidence for it. The more interesting part is when we've already moved. Now, with a displacement, we process the different input channels.

The interesting part is that we have all these possible poses, which are orientations. To test the displacement, we rotate the displacement by each of the rotation hypotheses, creating a matrix of different rotation matrices.

We take the dot product of these rotation matrices and the incoming displacement, then calculate the search locations—where in the graph we want to check the stored features, or where we might be after this displacement. To get those search locations, we take a location hypothesis and add the rotated displacement to it.

Let me draw this real quick.

Maybe I can find it on the screen. There are some figures in the paper that might be useful.

The list of possible poses changes at each time step; no possible poses stay the same at every time step, only the evidence for them changes. Possible locations update. Possible poses are just used to get a list of rotated displacements—a temporary variable used in this step. self.thought_possible_poses is not modified. We calculate search locations by taking the possible locations and adding the rotated displacement. We have an observation, a pose, and a displacement, and all these possible locations on the cylinder. We take the displacement, rotate it by the pose hypotheses, and add it to the location.

This is the first step, just initializing the search location. For each initialized pose hypothesis for every location on the object, or several of them, a point might have two possible orientations—right side up or upside down. We get the displacement, use the pose hypothesis to rotate the displacement, add the displacement to the hypothesis location, and that's the search location.

If I was at this location here—I hope you can see my pointer—I might now either be up here or down here. If I was at the top of the cylinder, there are more hypotheses. We have these circles of where we might be next. That's why, in these animations, the search locations or hypotheses can go off the object, because many of them will be wrong. When we actually apply the displacement, many will end up off the object.

We then look at the features stored at these search locations. For instance, if they're actually off the object, that's negative evidence—low likelihood. If the feature doesn't match, such as the color being wrong, that's no evidence. If the color and features are right, that's high evidence, like here. We do the same thing after moving sideways. Again, we have different hypotheses of where we might be and what the rotation would be. We apply the rotation to the displacement, draw a line, and get the search locations. At each of these points, we look in the graph to compare the points stored nearby to the observed features, and use that to update the evidence. Do we compare to the average of these points, the closest KS, or just the best one? Good question. We have a search radius. For example, if the hypothesis is that we're at this location and there are two orientations, we have a displacement, rotate it by the pose hypotheses, and get two possible locations. For each location, we look in a certain search radius, check all the points in the radius, and update the evidence. We calculate the distance between the search location and the point in the graph, and also the feature difference. That gives us an evidence value for each point in the radius. We take the best match—the maximum value.

Does it do any better if we use the average? No, it does worse with the average, because you might be in an area on the object where features change quickly, like right before the edge of a mug. You would get quite negative evidence if you compare to the points in the graph up there. Or if you have a very flipped object, you might have point normals that are opposite in that search radius. You don't want that to drag down your evidence if something matches your observation in that radius; that's evidence for this object.

When you do a displacement and find a point that matches nicely, which location has its evidence updated—the one you left from or the one you arrived at?

Evidence is updated on a location basis. This row in the hypothesis—the possible locations on the object—gets updated at every step. With every displacement, we update where we might be on the object.

This evidence keeps count of the evidence for the path we took on the object.

To answer the question, it would be the evidence for the location we ended up at—the evidence that we are actually at that search location we tested.

If we did something like re-anchoring, it might change the location to the point where we get the maximum feature match, rather than our location being the point in space we think we are after path integration.

There are more detailed aspects. It's in the documentation but not in the paper. The search radius can be informed by the sensed curvature. If we have a very flat surface, we don't need to sample points in a circle or sphere; we can sample points along the surface. We can use the point normal we are sensing to inform whether we squish the search radius from a circle into a sphere that follows the surface of the object.

On a technical level, we adjust our distance measure. The way we weigh the distance from the search point to other points in the graph is squished by the point normal direction. On a flat surface, we get only points in the graph that are actually on the surface. If it's a round curvature, we do a more circular search.

We have all the search locations, and this is where we do the evidence update and thresholding. For efficiency, we don't need to update all the hypotheses, only the most likely ones. We get a threshold and hypothesis IDs to test.

If there are hypotheses to test—which might not always be the case, especially if the object is already very improbable—we will not test anything.

We then get the search locations to test, calculate the evidence for these locations using the observed features, and assign those evidence values. We clip the evidence so it is not too small or zero.

We add the evidence to the existing evidence and weigh it by the past and present weights.

That's the part Ramy worked on last week. If past weight and present weight add up to one, the evidence is bounded and will never go outside the range minus one to two. If past and present weight add up to more than one, it's unbounded. In the current default setup, both are set to one, so they add up to two, and evidence can grow infinitely high in theory. If we bind the evidence values, we have a finite memory horizon. With the current action policies, that doesn't work well because the memory horizon is too short to explore a large part of the object or sense the whole shape. Eventually, I think this is the more elegant solution and how the brain must be doing this, because neurons can't fire infinitely, or you have hysteresis, which is bounded.

I think bounded evidence values only work well if you have either a very efficient action policy or some kind of replay of past significant features. Maybe with hierarchy and more unique features, that would help as well, because right now everything is sensing point normals on local surfaces. Even if you jump to the other side of an object, you're still going to feel a point normal. The displacement will be different for different objects, but it's still not that unique. It's not like you move somewhere and immediately recognize a handle or something very distinct.

In general, this fits well with Will's strategy during the TBP Olympics: if you're not getting very good features coming in, you need to adjust your approach.

I feel like there's a lot more to cover, but I've already been talking for about an hour. I don't know if we should take a break and continue later, or if you want to ask specific questions.

Does it ever happen that the search radius doesn't have any points to test? How do you handle that?

If you end up off the object, there will be nothing in the search radius and you get minus one evidence.

You could have a very coarse model and still be on the surface, but the model is too coarse.

That's why you have to set the max match distance parameter, which is basically the radius of the search. It's usually set pretty large—for the coffee mug, I think it's between a fifth and a tenth of the height of the mug. It's definitely bigger than the distance between points in the graph. If you set it too small, that problem can happen. As you make the graph more sparse, you have to increase the max match distance, but you have to balance it. Ideally, it should be a function of the sparsity of the points in the graph.

That's actually a great idea. If we build a platform for this, we don't want people to have to adjust all these parameters. Making the max match distance a function of the sparseness or the distance between points in the graph would work well.

It could also be a learned parameter. Each object could come with its own distance, depending on what you learned. Once you determine the distance for an object, you always use that distance for that object. It would make sense to have an object-specific parameter, or at least something from the object model function. I didn't get into object models and constraint graphs versus unconstrained graphs, but that's another topic. We already have other parameters for graphs, like maximum size and maximum spatial resolution. The max match distance could be based on one of these parameters as well.

I noticed that the evidence is split by graph IDs, which results in a for loop over the objects. Would it be more efficient to vectorize everything and have something similar to the channel mapping hypothesis, just to know which hypotheses are for which graph ID, and vectorize all the evidences? Would that make it more efficient, or what would be the problems in doing that?

Off the top of my head, I don't see an issue with that. Ramy, can you repeat the question? Vectorize the evidences? Right now, we have to loop over all the evidences and update by graph ID. I think we're doing it in parallel, but it seems like it would be more efficient to have all the evidences in one vector and just apply transformations. When we think about hypotheses, they'd all be in one vector instead of separated by graph ID, so we wouldn't have to loop over them. It's the same efficiency step that Viviane took by grouping all the hypotheses together and making them one vector, then applying transformations on that vector instead of a for loop. Now, we could do the same for graph ID hypotheses, putting them all in one vector and applying one transformation, instead of looping over the graphs. This would be especially helpful when we have more objects. Does that make sense? In general, if the number of objects changes, would it still work? If so, then it makes sense. It's basically the same as for the input channels. For input channels, we put all possible locations and orientations into one large vector and store the mapping between them, indicating which IDs correspond to which channel. If we add another input channel or hypothesis, we just append to the lists and the mapping, and we could do the same for graph IDs.

At some point, hardware-wise, you might run into limits where you don't want to do matrix multiplications that large anymore. If we're using GPUs, probably the bigger the matrices the better, up to a limit.

The question is what that limit would be. In general, resizing tensors is not as trivial as appending to lists because it needs to reallocate memory, but maybe it's fine.

We could definitely explore something like that to accelerate it further.

Then we could do multithreading over learning modules instead.

Interesting idea. It would be a two-level mapping instead, so we'd have the graph ID and then from the graph ID to the channels, or we could just have two separate mappings.

Right now, with only testing some of the hypotheses, that dynamically builds smaller vectors that we then update. Basically, we have the evidence threshold, which gives us hypothesis IDs to test, and then we index with these IDs to get a new list of search locations. That could be problematic. If we do it for all of the objects in the same thing, we would have to separate out the search locations into the different reference frames to test them, so we don't have a ragged list or ragged array, since each one has a different number of locations.

We would have to separate them into separate arrays, so maybe at that point it wouldn't be more efficient anymore. Alternatively, we could do something more biological, where we have one giant reference frame and the locations are very far from each other.

In a fixed capacity, almost. I think it would be a bit more involved than just applying the same mechanism as to the input channels.