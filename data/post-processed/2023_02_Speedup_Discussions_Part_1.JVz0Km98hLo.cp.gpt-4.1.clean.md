Okay. I prepared a few slides.

I'm trying to keep it short and hopefully have more time for discussion and input from everyone. The goal of today's meeting is to show the kinds of computations we're doing in Monty, especially those that are taking a lot of time, and see if the Mega team has any ideas for speeding them up. We might be able to leverage some of their work, sparsity, or other techniques. At the end, we can also consider whether it makes sense to have more Mega-Monty cross-team meetings and explore any synergies between the teams.

No one needs prior knowledge about what is happening inside Monty. I'll give a quick outline of where we are right now, what's going on with runtimes, and the operations we're running. At the moment, if we have a learning module that knows about 10 objects, it takes about 0.1 to 4 seconds to perform a step. A step is getting one observation from the environment and using it to update the internal state of the learning module.

To recognize an object, you usually need to perform many steps. Is it in serial or parallel? Are you running on multiple CPUs? I'll get to that in a second. Will you also explain why there's such a big range from 0.1 to 4 seconds? It depends on how many hypotheses are being initialized. For example, depending on how noisy the observation is and what part of the object the observation is on, it initializes different numbers of hypotheses, and then different amounts of hypotheses need to be updated at every step.

If we have five learning modules, that number gets multiplied by about five. Here, I don't have a range because I just took the average from one experiment. On average, they are about 2.5 seconds per step. If we know about 77 objects, it gets a lot slower because now we have to update evidence for each of the 77 objects—about 1 to 15 seconds per step. For five learning modules, it again scales by about a factor of five.

Given that we have to take multiple steps to recognize an object, when the learning module knows about 10 objects, you usually have to take fewer steps because there are fewer objects to disambiguate. It takes about 0.3 to 3 minutes to recognize an object if we have a set of 10 distinct objects. If we have 10 very similar objects, it can take up to 15 minutes to recognize an object, which is quite long. For 77 objects, depending on which object we're looking at, how similar it is to other objects, and how ambiguous the viewpoint is, it can take between 1 to 86 minutes to recognize an object. I think we can do a lot better, and we need to if Monty is ever to be applied in the real world. Recognizing an object in less than 86 minutes—the length of a soccer game—is necessary.

Are these times single CPU, or is this Lambda using multiple CPUs? These times are from running on Lambda with 16 CPUs.

Quickly about the terms: we have steps—the first numbers I showed—so one step is getting an observation, updating the internal state, and then moving to get the next step. We have a variable number of steps in an episode, which ends if we recognize the object or if we recognize that we don't know this object. We have a number of episodes within an epoch, which in our case is always going through the whole dataset of objects once, and then we can run multiple epochs, for example, testing different orientations of each object.

Steps in a typical experiment: first, we loop over episodes in an experiment. Ben parallelized this part, so if we're evaluating, we can run every episode in parallel on a different CPU on the Lambda node. That doesn't work during training because the order matters when learning. But since we're mostly evaluating right now, this helps speed up that part. While we haven't reached a terminal state, we first go over all the sensors the agent has and collect observations from these sensors. Then we loop over the learning modules and perform a matching step for each learning module. This loop could also be parallelized, but it isn't right now because no one has done it yet, and we thought it's not the highest priority since we don't have as many CPUs as episodes.

For each matching step within one learning module, we loop over the objects in memory, and for each object, we update the evidence given the observation. For the loop over objects, we use multithreading, and the evidence update is vectorized—mostly large matrix multiplications. The learning module sends outputs: the object it thinks we're on, its pose, a vote, and a motor command. Then we look again over learning modules to receive votes, which could again be parallelized. Receiving votes again loops over objects and updates the evidence using the vote. Here again, for the loop over objects, we use multithreading, and the evidence update is factorized. Finally, we check whether we've reached a terminal condition. Getting the sensory observation takes about 0.01 seconds, which is fast compared to the rest. The slowest step is updating the evidence for each learning module given an observation, which takes about 0.01 to 0.05 seconds per object. Scaling that by 77 objects and five learning modules adds up to about two to five seconds; with multithreading, it takes about one second. The update using votes is a bit quicker because we threshold the votes to make it faster—overall, about 0.05 seconds with multithreading. If we use all votes and don't threshold them, it's a bit slower than the first update.

Overall, taking as many steps as needed to recognize the object, it takes about one to eight minutes for episodes where we don't time out.

How many steps is that usually?

It's usually between 20 and 200 steps. We have a maximum of 500 steps, which is when we reach timeout.

Since we already have these outer loops parallelized or using multithreading, for this presentation I'll focus on the evidence updates, which are currently the slowest part of the code. Is this clear so far?  
Very clear. I have one question: when you say multithreading, what mechanism are you using?

We use Python multithreading, the map—fullmap or something it's called.

I'd have to check real quick.

Yes, we use threading, the thread. That is not preemptive.

So, is this using Python threads then, Luis or Kevin?  
Yes, this is Python thread, that's not preemptive threading. These are not real threads. There will be a lock and a GIL. That's why I was asking, because at deeper levels, you want to distribute things. You can use affinities and various things, because at any one CPU, you only have direct hardware support for two threads at a time. Anything more than that is put into queues. But if you're using Python threads, as Luiz just pointed out, it's not the most efficient mechanism for the hardware. It's only running on one CPU. I think it's not even real threads.  
Correct, it's yielding.

When they say they're running on multiple CPUs, how is that being distributed?  
Episodes are running on multiple processors.

This is the parallelization part: each episode is its own process, and within that process we do the multithreading. The multithreading seems to be doing something, right? Because it's up to five times faster than without it.  
Yes, it's definitely faster, so it seems to be doing some good.

It can't be one CPU, though.  
It depends. We need to wait until we see what's going on under the hood, because the difference in multithreading will be impacted by different things, depending on what the operators actually are. The advantage of that thread is there's some I/O.

Because it's going to yield to GIL, and GIL is going to wait just for the I/O. There's nothing else to wait for. Let's look at the code, and then we can back up a level if that makes sense.

If we actually run a profiler on one episode, in this episode we have five loading modules, and this is not using multithreading because the profiler doesn't deal well with that, so it's a bit slower than it usually would be. It looks at the time taken by the top 15 functions. As you can see, the longest time is taken by the KD tree search, which is the first topic.  
Is that Python KD tree? Is that implemented in Python?  
No, it's using C, yes, SciPy.  
All right.

Today I have two topics that I think could be sped up. One is KD tree search, and the second is everything else—matrix multiplications, evidence updates that are vectorized.

There are a few other ones, mostly rendering the observations in Habitat, adding an object, and things like that. I think I can figure those out on my own.

Let's jump in on the first one if there are no questions for now.

I've used KD trees a lot, mostly in C implementations, so I can take a look at that. I don't know how SciPy implements it. Usually SciPy implements a lot of their stuff with C on the back end, and it's just a Python interface. I'd have to look to see how that's being done. The SciPy one, I checked on, and we upgraded SciPy so we used the C back end. We had to create a version of SciPy so we could use the C back end. I guess it's probably a pretty decent implementation.  
One question would be if KDTreeSearch is actually the best way to get what we want, or if there's maybe a better way.  
What are you using it for right now?  
That's the next slide.  
Is Einstein, like Einstein summation, or is that an eigenvalue summation or something else?  
I'll also show that on a slide. It's basically doing a dot product with three dimensions.

First, the shapes and sizes of the matrices we're working with, as a primer for the next slides:  
- Number of points in the model: usually around 500 to 5000, depending on the size of the object  
- Number of hypotheses: between two and eight times larger than the number of points in the model  
- Number of nearest neighbors: usually 5 or 10  
- Number of features the sensor module is detecting: usually between 5 and 15  
- Number of incoming votes: if we only take the highest percentile of votes, about 1 to 200; if we use all votes, it can go up to 200,000, which is a lot slower  
Wow, that's like a small metropolitan area.  
I don't understand how the incoming votes can be that high.  
What's the logic, how do they get that big?  
It's basically all the possible hypotheses. If we have 4,000 hypotheses from five learning modules, it's 40,000 times five incoming votes for possible poses. That's in the worst possible scenario, where everything is equally probable. The hypotheses are the locations on objects, so it could be the same. There's a limited number of objects, but a lot of places.  
Locations and pose, right?  
Yes, that's why hypothesis is two to six times larger than the model, because for every location on the model, we have two to six possible poses.  
Got it, thank you.

Finding the nearest neighbor: what we do right now is use KDTreeSearch. The problem we're trying to solve is, we have an array of search locations. In this picture, given two hypotheses (the two gray arrows), we would have two search locations, the green dot up here and down here.

H would be the number of hypotheses, in this case two, and they are in 3D space (XYZ coordinates). Then we have model locations, which would be all the black dots—N, again in 3D space. We want the IDs of the k nearest neighbors of these search locations. For example, if k is three, we want the IDs of these three points in the search radius. What we want returned is of shape H, K.

Maybe I'll pause here for a moment. All right. So, a KD tree typically works by doing a spatial bifurcation. You take half of the elements and put them on one side, half on the other, with a dividing plane. Anything with X less than this, or X greater than that, gets separated into a binary tree. Then you do the next split on Y, then on Z, and repeat. It's like an octree decomposition, is that correct? We basically build this location tree at the start of an experiment. We already know the model of the object in this case, because we're just evaluating. So, we build the KD tree once, and at every step, we query the tree with the hypothesis locations. You can stop that decomposition at any stage. For example, if you want to go until you have only 10 leaf nodes left, you can search through that, or you can continue to decompose until you have only one object on each leaf node. One of the optimizations you can do in the KD tree search is to terminate it early if you want a group of things that are local, that are nearby.

Is that during building or querying? That would be during the building phase. That's how it's structured. The building is not that big of a deal because you only have to do it once. It's more the querying that's important. But it would be a parameter you set during building that would affect the speed of the query. We have leaf size set to 40. Did you try to vary that to see if it speeds things up? If I set it lower, it was lower, but yes.

How many points do you have in that again? N is around 500 to 5,000. I'm going to ask a question: can you just use a lookup table? We've got a bunch of memory on this thing, two terabytes. Can I just use a lookup table? The search locations are not identical to the locations in the model; they're just nearby. Before we used KD tree search, we just did the difference, then linear norm, and then the minimum. That was definitely a lot slower. You could do what Lawrence is saying.

Basically, just create a huge discretized space into a small mesh, and for each voxel, you have your neighbors, the list of Ks. With 5,000 elements, even keeping the list of 40 is a small tree. Then you don't store any mesh at all. Is there no connectivity information between the adjacent points? Is this a list of points?

Building a mesh would be one way of speeding that up a lot, because for each point that you register, or even if you're detecting a point in between stored points, you can still figure that out pretty quickly by connectivity.

So you have the graph. I think Lawrence's idea is a good one. When would you create that list? After training, at least instead of the tree, you just replace the tree with the structure. You replace the tree at the start, and that is basically a single step: you do your training, then you build a tree, and then all your inputs are based on that. Because it's static, it will be really simple. You've got a bunch of memory—let's use it. You just have to figure out how to index it. Indexing is the tricky part. But as you say, if you know what your parameter space, your spatial space, is, you just chop it up into bits. Actually, the other thing you can do is, there are images representing each voxel. You can just round it, and that's it. I think it'll be very fast then.

The other thing you can do to accelerate it using this implementation right now, a quick and easy thing, is to cache those nodes. If you're only moving a short distance on the object for each step, you can reuse those lookups and go straight to the leaf node to see if your nearest neighbors are still in the vicinity.

But Eric, I think Lawrence's idea would take out all of them—there'd be no tree to begin with. Exactly, but if you just wanted to implement something to accelerate what you've got right now, just to see if it makes any difference, you could cache the tree nodes that you're finding in the KD tree search and reuse those until they are no longer valid, then pop back up one node in the tree and go back down to find the neighbors.

I'm not sure that would help. That assumes you're going to look at the same node over and over again in sequence. I'm not sure that'll help, and I'm not sure you even have access to that. It's a locality-based caching, basically. If you're a cod, then you're going to see disparate stuff—that's the problem. It's not going to be continuous; it depends on the length of this cod. You're right. But also, another thing I thought of: it implies changing the KD tree implementation, and I don't think I want to get there.

So just so I get it right, what you suggested, Lawrence, is to discretize the space into voxels and then use those as a lookup table whenever we get a new point. See if that looks one at the floor. That's what I said: lookup table. You know the point you're on, and you just look up all the adjacent points. But within this resolution, you don't care. You lose that much resolution. You're not in, "I know which ones are close, which ones you wouldn't." Information too—whether it's 1.15 inches versus 1.16 inches—you might actually get different nearest neighbors, but here you would still get the same. So it would be slightly lossy, but that would be okay.

How would that scale into the future? Do we want to worry about that now? I wouldn't worry about it. You can look up terabytes—5,000 bodies. You can stay on the ladder. At the point it starts to fail, you can start hashing techniques. You can hash as well.

The good thing is, I was trying to imagine scaling to human brains, but the learning modules themselves don't continue to scale; they don't go to maximum. To make bigger brains, you need more learning modules. This speeds up the operation of a single learning module. So, my question—I've answered my own question. If you wanted really big brains, this wouldn't be a limiting factor. No, and I wouldn't be surprised if neurons do something like this. That's essentially what they do. I was trying to think how this relates to neurons. I haven't gotten there yet, but you may be reaching a conclusion. I think it's very similar to what neurons do.

That makes me happy that my neurons are doing lookup tables. That's basically what an SDR is. Within some resolution you match, and then you do something. That's basically what we're talking about.

We're solving both your problems. We're solving two Monty problems. We're making it more neural.

This is great. Has anyone seen an objection to this idea? No. There might be a couple of other things algorithmically I could suggest, but if you're happy with the lookup tables, that's probably it. I think it's going to be really hard to beat lookup tables. It's one of the rules. If you've got the bandwidth for it, it answers the interview question. The only thing I would add is, if you have three dimensions, there are several ways of creating the index. One way is to suppose your indices were 256, so you have one byte for X, one byte for Y, one byte for Z—three bytes. The way you want to sometimes think about this is the implication on the underlying cache memory structure. There's an alternative format where you interleave the bytes. There's a name for it—I want to call it a Hamiltonian path. It basically improves locality. If you're hitting around one particular area, there's a greater probability you'll be on the same cache line looking for the next one. In fact, that's what they do in texture maps these days.

So Kevin, this is all in Python. No, you misunderstand. It's a simple bit twiddle on the index you use to look something up. What we will have done with this is knock down the runtime here so that now it's in the Einstein, and things like this. I think what would be cool is to try and implement this, see where the timing is, and then we can do additional optimization. My guess is this would be like the 10th hottest operation now. I think the only concern I have is the resolution loss, because right now we have pixel, we're going to voxel. There's a volume in there.

If you're using a uniform discretization of space, the points are separated not by how many are in each set, but by the space itself. If you know the maximum dimensions, like a bounding box, you can subdivide it into, say, 32 by 32 or 256 by 256, and that gives you the voxels automatically, with a set volume for each one. For example, in this picture of the mug, the point marked in green will include points on both the inside and outside of the mug because of the volume. The voxel's location in memory is encoded in the actual XYZ or IJK coordinates of the point itself. You can determine where in space it will be based on how you subdivide—each division is like a bit, left or right, zero or one. As you subdivide, you add another zero or one, indicating which side of the cut plane you're on, which leads you to a single voxel, a single leaf node. The position in XYZ space tells you exactly where it will be in memory.

If you have the memory space, it's a very fast lookup and a very fast hashing algorithm. In this case, would we not care about storing fewer points because we have the discretized voxel space and just want to indicate for each voxel whether the object exists there? Does the surface intersect the voxel? That's what you want to store—a bit, one or zero, indicating if the surface of the shape intersects the voxel at that location. Is that what we're saying? I thought it was just replacing the KD tree search. We still want to know the ID of the point where we have stored the feature. I think it's just taking the XYZ, hashing it to an index, and looking it up. What we're proposing is an optimization: giving the tree a static structure and building a lookup table out of the tree.

If you want to do incremental learning, you could still modify the table without rebuilding it every time. You can modify it locally, which gives a lot of flexibility. Viviane was asking about having more points, but it seems like the size of your box could be modified too. It's actually faster than rebuilding a KD tree. Are there any libraries you would recommend? Let's start with a dict, but you could use an LSH library. LSH is another way to scale if you want to handle massive objects or points. Locality sensitive hashing is a lossy technique where, instead of avoiding collisions, you hash to points in space that are similar. Many people use it in transformers now. Anshman was a big proponent of LHF, which is also a solution to many problems. There are several open source implementations for that. I just looked up FAST LSH, Ash, and Python—there are a bunch of them.

That would be better than a crude partition of space because you're trying to encapsulate a surface, but with a partition you pay the penalty of a volume, whereas with LSH you can store only the locations that make sense, not all the empty space. You wouldn't store the empty space. With a dict, you only store where the points are. "What is a dink?" Just joking—lookup table, hash table. When you first said lookup table, I thought you meant carving up space into volumes, each represented in memory. No, you don't want to do that—it's more like a hash table. I understood the same thing as Kevin, so that's why I was confused. Oh, I'm sorry.

You take the location, hash it to get to a point, and then you have the five points right there. Viviane, quick question: the inputs to the KD tree search—are those global XYZ coordinates or object-specific coordinates?

Object-specific.

So you have a point on an object and you're querying for nearby points based on distance from the initial search point.

Distance and direction, right. Thanks a lot. Should I move on? The next slide is—let's not go downhill. Lawrence and I are 11 days apart. This is still related to the KD tree search, but I want to check if this would change anything with what you're recommending. When we're voting, we have a similar problem, but the main difference is that we have to build the location tree at every step from the incoming votes. We have a bunch of incoming votes and we want to query in that space. Would it still be fast to build up this discretized voxel space at every step, or would something else be better in that case?

Do you have to build a tree that's being created?

Yes. We get votes of shape V times three, and if we threshold them—around 20 to 200—then in that space, we query these locations from the hypotheses.

But this is the part of the loop that was much faster already, right? Yeah. Okay. Is it using a completely different KD tree here or the same KD tree as in the previous slide? It's a different KD tree. In the previous slide, we could build the tree once at the start of an experiment from the model of the object, but now both the hypothesis locations we use to query and the tree we need to query change at every step. Here, we have to build the tree or the voxel space or the lookup table at every step. The first one was the evidence update from the sensory data, and this one is the evidence update from the module voting. Exactly. But didn't you say that loop was already pretty fast? Faster, but not as fast. If we threshold the votes, it's pretty fast because V is only up to 200 elements, so it's fast to build the tree, but if we use all the votes, which can be up to 200,000, then it's slower.

Is there an advantage to using 200,000? Would you like to use more than 200,000? Or does it rapidly fall off? It's a minimal advantage, but not enough to justify the time cost. Neurons couldn't do that, right? They couldn't process 200,000 votes. Is the thresholding based on an evidence measure or a confidence measure? Yes, only the most confident hypotheses get communicated to other learning modules. On average, how many votes is that per module? It's between one and 200 usually. So you actually do have a lot, depending on how symmetrical. If this is being done by unions and an SDR, you can't get that high a number. You can't form a unit of 200 hypotheses. You might be able to form a unit of 50.

That doesn't mean you couldn't do better than the neurons, but the neurons are going to plateau at a lower number. The main problem is if, like Eric says, we have a very symmetric object, then all of the poses are about equally likely. If we then threshold the evidence, they will all be.

Would there be a way of compressing those? Would there be a way of consolidating those for which the evidence is all the same for a set of votes? Like having a list for the given evidence, all these possibilities are there so you don't have to expand it out when you do the compression. When voting with other modules, if there's no way to distinguish two votes from two hypotheses based on the evidence, then they're functionally equivalent. There should be a way of compressing that down. We have a mechanism to detect symmetry—if two poses have consistently the same predictions, they're classified as symmetric after a certain number of steps, but until then, it takes a number of steps to communicate a lot of thoughts.

I'm almost tempted to say the right solution is to not have so many hypotheses. It's like Laura and Albert Beck. Right now, with the thresholding, it's actually pretty fast, so it might not be the highest priority to optimize this one. I agree.

Moving on, just one last note on the KD tree search radiuses. We only want points in a given radius, specified by the maximum match distance, but we also want to get a matrix. If we just query the radius, we get a ragged list since each point's radius contains a variable number of neighbors. What we do now is create a query for k nearest neighbors to get an array of shape H times K, and then we mask all the entries that are too far away.

There might be a better solution. Is this still relevant if we use the lookup table?

In the lookup table, it can also happen that within a given radius, there can be a variable number of neighbors. Is that a problem? It's not obvious. You can't use the matrix operations directly because they expect a fixed size. You can't just put zeros there?

The two options would be either to fill up with zeros, but if only one point has a hundred neighbors, the matrix gets huge for all the ones that just have two neighbors. The opposite is to cut it off at a certain number of neighbors and mask the ones that are not what we said to do earlier when talking about the lookup table—pick some number of points. That problem applies to the lookup table as well. It's a universal thing. If we did the query radius, in principle, we'd have fewer points in some cases. I didn't look at how many cases there are more points than k in the radius. It depends on how dense our models are.

Maybe I'll move on, since this one isn't as much for speed. Now, just a quick question. Right now, you're assuming you can't assign any importance to the points—they're all equal as contributing evidence, right?

What if you relax that assumption?

The points get eliminated based on the evidence not fitting the hypothesis, right?

They contribute to additional hypotheses, but in large flat areas, if you eliminate some points, you have gaps in your model. If you had something higher order than just a point, you could allow for something to substitute for a large flat area instead of many small points.

This is the isolation problem I mentioned earlier. That will come in more when we add hierarchy, so points. Also, when we build the models, we take into account how fast features change in an area. On a flat surface, we store fewer points in the model than in a part of the object where it curves and features change a lot. I wouldn't necessarily postpone it to when you think of hierarchy, because then you're getting into assemblies of parts. If your fundamental primitive is becoming burdensome because it's too low in information content and you need a lot of them before you get something out of it, you would need to replace it with something that has more structure, so you don't need so many representations to yield a hypothesis.

It's something that's not a point, but just for argument's sake, a rectangle. As long as it's flat enough, it's the rectangle, and the descriptor for the rectangle could substitute for a myriad of points if things are flat enough. If you go down to pixel points, you'll run into combinatorics, so unless you do some kind of abstraction—which I don't think is the same as hierarchy—it's going to be a problem until you can efficiently represent an area of a surface by a few parameters instead of hundreds of points.

That's exactly what I was talking about in my research meeting last week: how do you discretize a space using as few points as possible? You can use fewer points the more high-order information you're given. For example, in addition to getting the point, you're also given the gradient or the curvature. You can then extrapolate away from that point and represent a very large area near there if those features remain constant. If the features start to change—if the curvature or gradient changes—then you might need to drop in another point to capture that change, and you could interpolate between those two points to get a smooth transition. Maybe that's a good topic for another research meeting to get into more.

Because we only have about 10 minutes left, I want to get to the second topic real quick and see if there are any other thoughts on that.

Now, the matrix operations.

The one that takes the longest is the Einsam operation, which we use to get angles between the hypotheses and the observation. Since we use unit vectors to calculate the angle, we just need to take the dot product between two vectors and then apply our cost to it. We want to do this for all hypotheses, poses, and their neighbors in one step.

That means we need to apply the dot product between the hypothesis nearest neighbors, which is shape H times K times three, and the transformed observations point normal. The three are the XYZ coordinates of the point normal, which is a unit vector. As an output, we want a matrix of size H times K. Einsam is basically just an efficient version of running a for loop over all hypotheses and then applying the dot product between the hypothesis point normal and the transformed observation point normal.

We also apply normal dot products, for example, to rotate displacements by the hypothesized poses. In that case, we have the possible rotations, which are three by three rotation matrices, and we have as many of them as we have hypotheses. Then we apply the dot product between that and the sensed displacement, which is a displacement in XYZ coordinates.

It's not a unit vector in this case; it's just a displacement. We get a matrix of size H times 3. We also apply matrix multiplications, for example, to get the rotation matrices from our pose hypotheses. In this case, we have the poses stored in all the nodes—number of nodes in the graph times three. Then we have the sensed pose, which are also three unit vectors; they are orthonormal. We apply a matrix multiplication between them to get N three by three rotation matrices. Then we have the standard operations like addition, subtraction, arccos, and multiply to do a range of different things. Here, the dimensions always stay the same. We also have some reduced operations, like applying the maximum to get the highest evidence in the nearest neighbor radii.

If we boil this down to just the size of the matrices, there are two things that could be places to optimize. One is that we don't need to test all hypotheses at every time step. Right now, since it's just matrix multiplications, we update the evidence for every hypothesis at every step, but in theory, we could mask a lot of the rows in the first axis, H. Some entries in K are also masked, as I mentioned—if fewer than k neighbors are in the radius, we mask these entries. I don't know if you have any thoughts on that.

What are you using to do the matrix math? NumPy. With the first one, how many rows are you trying to ignore on average, what percent? That seems like it's just brute force doing a lot of stuff it doesn't need to do. Theoretically, we could ignore a lot of these. For example, we could only look at the N highest evidence hypotheses—10, 100, 1,000, whatever—but it would definitely be lower than H, which is usually between 1,000 and 40,000. Especially towards later steps in the episode, this would probably just be five or so high-evidence hypotheses. You only care about a very sparse subset of the rows. I don't know if there's an efficient way to do that.

The advantage of updating all of them at every time step is that you can easily recover a hypothesis, even if you get several inconsistent observations.

I'm not sure how relevant that actually is or if it's worth the computation.

I'd have to look at the math to see if anything pops to mind. I would try to minimize the number of times you're calling arccos and sine and so forth, because those are inherently slower than the built-in addition and multiply operations. It's just because of the way they're implemented—they're usually lookup tables or something like that, since they're not something you can implement in transistors directly like addition, subtraction, and multiplication. When they're really computing the arccos and you've got floating point numbers, they start with a lookup and then there's probably a polynomial iteration on it. They're expensive operations. Newton iteration. It's not a single operation. There are a variety of optimizations people use to compute that. The easiest thing is to take the dot product, which you say is normalized, and then just go to a lookup table to get you in the ballpark.

If you're comparing distances, such as computing two distances to determine which is smaller, don't sum all the squared components and then take the square root. Instead, compare the squared distances directly. The square root is an expensive operation, and you can compare the squared distances since one will be larger than the other. This approach saves computations if you don't actually need the distance value and are just comparing two distances. However, this can introduce a coordinate bias.

From the profiler, the slowest operations, especially when multiplied by how often they're performed in the algorithm, are the Einsum and, surprisingly, the Maximum operation.