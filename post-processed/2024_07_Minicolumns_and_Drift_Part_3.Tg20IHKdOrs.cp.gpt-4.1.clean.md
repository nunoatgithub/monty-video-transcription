I was exploring the idea that you have two ways of doing this: one is having the same set of cells with two phases, or having the same set of minicolumns where, in one layer, it's dense and in the next layer it's sparse. Are we, on some level, assuming that the cylinder has overlap with the can, or has no overlap? These two are different. In terms of the actual populations, does the cylinder have overlap with the can in both examples? In the example where you're doing it on different phases, these are the exact same cells.

In the example based on the tank paper, they're the exact same minicolumns or grid cells. Imagine a grid cell has both: the classic grid cell and, below, a bunch of other cells—whether you call them mini or not. The path integration works on that set.

But they're actually physically different cells.

Yes, they're physically different cells.

Does that make sense?

In one case, you look at it in one part of the phase, and in the other part of the phase, you have a completely different representation. Here you look at one set of cells, then you look at the other cells underneath it—it's a different representation. There are commonalities between them, but they're overlapping populations. The sparse one is a subset of the non-sparse pattern. In this case, the sparse pattern is not a subset; it's a different set of cells entirely. If we're dropping cells from the representation to be more specific, then they have to be a subset. No, it's more like you have a dense measurement. Looking down at the tank paper, you're looking at these cells acting like grid cells, and the question is, under them in the column, there's another set of cells that are co-aligned but sparser. When you do path integration, path integration has to work on this set, like a little minicolumn. The minicolumn is path integrated, and then we pick a subset. That's possible. The minicolumns could be path integrated. I don't see a problem with that. You path integrate the whole set, but this is a difference: this is not the same cell as this one. When this one is active, this one's always going to be active. When this one's active, only some or fewer of these are going to be active.

Something like that.

So these aren't exactly the same scenarios. This is literally the same set of cells at different phases; the other is literally a different set of cells. But if you think about their vertical co-alignment, they're overlapping. I'm trying to figure out the implications of these two ideas. What would allow us to do classification? Would it allow us to do something else? A lot of ideas come to mind.

What are the problems? Let's say we want to be able to avoid relearning points on common objects. That doesn't solve the problem. Let's say I start by learning—why would I start a new object? Why would I pick a cylinder versus another shape? If I do the prediction based on these, any prediction based on the cylinder would be common between the can and the coffee cup. Sometimes I'll want to make a prediction about something unique, like a handle. How would I know to do that? I move my finger around and have a unique representation down here and a less unique one up here. Why wouldn't I learn every feature on the cylinder using this representation? Why would I say, "Only on the smooth, common parts do I use this one," and how do I know when to make a prediction based on this one?

Here's an idea. What if we assumed it was this method, where you go through phases? At one moment, you have the cylinder, then the can, then the cylinder, then the can. Every phase, if this prediction is correct, I just ignore this. I don't want to learn anything here—don't learn a unique thing for the can because it's correct for the cylinder. But if this is not correct, then you want to learn this one. You say, "Hey, that's not a Lego cylinder, that's something unique." I'll use the representation for the cup. I found a feature that says it has to be the cup.

As I go through learning, I've learned a cylinder already. I don't know how that happened, but I learned a cylinder. I'm going around, and now I present a new object. It's an incorrect prediction, but I already felt I was on the cylinder, so it must be a variation of the cylinder. I'm going to learn that on the cylinder, there's a unique representation for this. I've had that unique representation all along—cup in cup—but I just ignore it here and pay attention there. Now I'm predicting cylinder, but then I get to the cup and have a prediction unique for the cup. Therefore, this was a cylinder with a handle on it. We always learn on the generic one until the generic one does not become plausible. The general idea is to stick with the denser one. I'm trying to solve the problem of not relearning all the common points on objects. As soon as I know I'm on a cup versus a cylinder, or if I knew I was on a can, I would make a different prediction. As soon as I latch onto something—it's a can, a cup, a football—I have this alternate, unique representation.

That's only speaking about learning a morphological model, or because the cylinder can be different colors as well, even if you're on the main part of the cup. You would still make different predictions depending on which cup it is, for example, based on the color being sensed. You're getting ahead of where I'm thinking with this mechanism, because I have a mechanism that represents a base object and a non-base object. I'm not thinking beyond that at this point. Would it not work? Are you thinking of examples that wouldn't work? No, I'm just thinking it will be more involved once we take into account features like color. Basically, I'm alternating between a generic SDR and a specific SDR. With a specific SDR, I can associate it with anything, like color. I can just associate whatever the input is at that time with this specific SDR, so I don't see why it would be different with color or anything else. It's just a matter of which kind of location I'm representing it as—am I using the generic one or the specific one?

I just mean we would basically never use the generic one. We use it anytime we don't have a specific prediction.

To predict the morphology.

I'm not even stuck on morphology. I'm just saying I'm altering representation here.

All I'm saying is I have a generic representation, and if I've learned that and now I have something which is an incorrect prediction, then I will switch to the specific version to make that prediction. For the specific version?

When I think about it practically, the prediction will almost always be off in some features for the cylinder. If we're on a can, we will sense the redness of the can, which might not be in the generic model, and we will sense the riffle structure of the can, the little wavy structure. So what's wrong with learning that? Nothing's wrong with learning that. I'm just saying it will be rare that it actually matches the generic model exactly.

Does it have to? The generic model might be purely morphology, just very rough morphology. I like that, actually, because otherwise it wouldn't be very generic.

I really like this idea. It's nice because everything can be decomposed into these basic object shapes. If you look at drawing books, they compose the scene into cylinders and circles and things like that. But if you're oscillating like this, and once we take all the different features into account, it feels like we almost never make an accurate prediction with the generic model for what we're actually sensing. What if we say this one is only morphology? This is where you're going. It's only morphology. Somehow, we are able to learn this without paying attention to features. That's right. That means they're not connected the same. I was thinking, are you thinking of this happening with the grid cells or in layer 2/3 right now? I don't know. I'm really confused at this point, because when we were talking about it being in layer—like with the idea that made a lot of sense to me, because that way we only have morphology in that generic model, and it just tells us how we path integrate along that three-dimensional shape.

Let's review layer four here. It's composed of minicolumns, and those minicolumns represent the same orientation of a feature. That's all they represent. I believe minicolumns are defined by these bipolar cells, which are a separate set of cells that connect vertically across all these. The spatial pooling occurs on these, not on the other cells. Each one represents a minicolumn. These cells exist just like this; they have literally no tail. This is where the spatial pooling occurs from. These cells are picking around with lots of synapses, and they can learn too. If I want to purely learn morphology, I would be trying to learn with these cells. These represent an orientation at a location—like an edge at this location in space. These cells themselves know nothing about color or texture or any other detail; it's just pure orientation. Then these are the details of what is at that orientation, at that location. These cells would represent orientation plus feature plus location, because they're getting location from down here.

If I had—I'm trying to remember where my generic and specific SDR are here. Let's say it's in layer 6A, and then there's a layer of cells here, which is the classic grid cells, and then a layer of cells underneath, which is more sparse. Now we're going back to this idea: two things on top of each other, not in time.

These grid cells could connect to these, and these could connect to others. Would that work? My grid cells aren't very unique, but I could learn to associate. That's the way grid cells work—they can re-anchor. There aren't that many combinations, because they're not sparse enough. There are a fair number of combinations, but not millions or billions or trillions. So you could say there's some number of ways that grid cells can re-anchor. It's a limited set. They may correspond to the number of ways I can represent morphology. As I go through these locations, I can say there's an object, an edge, or something at some orientation at that location. That's all I know. They would be path integration with basic morphology, featureless shapes, something like that. Then these hypothetical sparse cells I made up also path integrate in the sense that the same alignment would actually put it, but they're farther, and so this should be unique. This should be unique with representation of location, and that would be associated with these.

I like that idea. Would this also explain how we can path integrate on three-dimensional objects? For example, how do I know if I go once around a cup and return to the original location? Would grid cells in layer 6A learn specific path integration properties, such as how you move on a cylindrical object, and use that to communicate with upper layer 4? Orientation should be sensed next. That sounds complicated. I'm partially lost and don't fully understand the question.

Basically, grid cells are usually explained in two-dimensional space for navigation tasks, but the question is how they would work on a three-dimensional object, where you can move around and end up in the same location. In the past, we discussed learning grid cells for different spaces, and now we might be encoding general morphology or the abstract object. So, as a general question: how do we represent three-dimensional space versus two-dimensional space? We've talked about this before. There's evidence suggesting that grid cells don't handle three-dimensional space very well. For example, with a cube, you remember the six faces, but not where the faces are relative to each other. I can remember individual faces, but I can't recreate their spatial relationships. It's hard to do. That's what I'm referring to—we might not be representing the whole three-dimensional space and the object within it, but instead an unrolled surface of the object.

With a cube, you don't really unroll it in the sense of learning each face sequentially. If I showed you a cube with two pictures on the sides, I generally can't remember which picture is relative to which. I can remember each picture, but I can't say their relationship unless there's a story connecting them. I might see the cube from one view and notice a pattern, but I can't remember or recreate another view. I can only create the space on Zoom, but I can't draw or remember what's on one space versus another.

I've always wondered if we're just remembering a series of two-dimensional patches that are somehow stitched together. But you do know that if the dice is turned around four times, you're back at the same spot.

I don't remember the sequence of what I see as I do it. That's pretty rare.

If it were just a series of four images and something on the other side, you might be able to do it. Can we put that aside for a moment? Let's try to finish this one. Maybe you're onto something, but you'll have to help me understand your solution because I'm confused by it.

Where are they? Where were they on this one? So you have these—are these bipolar cells? I always forget which ones they are. They're not the chandelier cells; I forget.

There are theories that they drive these other cells. At this level, these cells are representing just orientation, with no features, and this would be a dense representation. I could re-anchor these based on the basic orientation of the room or the morphology of the object. We could always form a unique representation here.

You would associate that with these other cells, which is also a unique representation. How do I pick a unique representation here? I guess I pick a random set here and a random set there.

Imagine I'm going to draw this a little differently to make it look more parallel. The idea is you have a set of grid cells—classic grid cells—and then a set of ones underneath.

Maybe just a few; it doesn't have to be a lot. This is a unique location because these sparser cells are picking one of many under each grid zone.

I want path integration to occur. Path integration could occur for these, but I don't think it occurs for the others as easily.

If I move from location to location, I have a different set of sparse patterns here. I don't know how I would predict the correct sparse pattern given a location where I have a sparse pattern here and then move to the next location. How do I know which sparse pattern down here to activate? I don't think I would know unless I learned the connections between them, but I can't really do that.

The thing I'm trying to do is, when I'm on an object and move to a new location, I want to be able to make a specific prediction at that new location. That means I have to path integrate and select the D cells correctly.

Could that be done with the layer 4 connection? If layer 4 projected back down here, it could. So what would that tell me? It would give information on which object we think we're on. Then I'd have to learn—not path integration, but more like, if I know what the feature is, then I know my location. I want to be in a situation where I'm at some point on an object, I move, and I want to predict the next feature. Layer 4 is not active yet, so I can't rely on what's here. This will only represent the previous location, so it can't tell me my new location yet. I want to path integrate to the new location.

I thought the new location comes from the grid cells. I'm just thinking about how to path integrate the sparse version here.

Are you thinking of this as minicolumns underneath? I'm not certain. It could be like minicolumns, because then underneath the grid cells doing the path integration, each grid cell would have a minicolumn, and the inhibitory connections would be between other Layer 4 cells. But how do I know when my minicolumn changes? Sparse activation, minicolumn changes. How do I know which cell in the next minicolumn will become active? I can predict which column to go to next, but I can't determine which cell will be selected in that column.

Could this be selected by the inhibitory connections between Layer 4 and Layer 6? It could be. I think I have an idea how to do this. Actually, forget that these are minicolumns.

Remember in the tank paper, we had basically six grid cell modules, and there was a little cluster of activity in each one.

The idea is that these move around as a group. You re-anchor and pick a different set to move around as a group.

That's what it looked like. Then I imagined there was another cell underneath each of these—an active cell below it—and those were more sparse.

Imagine the whole path integration. Let me rephrase it. The way I've always thought about minicolumns in the past is you have a random cell in each one that's active, and the next moment you have a different random cell in each one that's active, with no correlation. But what if, in this case, I had a cell here, and under this cell, another one, and under this cell, another one? Path integration. These would be separate little layers. Path integration means that, just like these cells all move in path integration, the next layer down would also move in path integration, and so on.

The active cell moves within the same layer. It can't change to a different one here. It's not a random choice. Let's say I have six active cells here, and underneath, there are more than six—let's just say six for a moment. Then, underneath, I have two in the next layer down, and underneath that, another two, and so on. Imagine the layers of cells are really thin. I'm making this up. The two cells here move around just like these do, and the two cells below that move around just like these do. I'm not picking from the whole set; I'm just picking these two to move around, and so on. Then I can do path integration because each cell is path integrating correctly. It's not randomly jumping up and down. I'm not picking a minicolumn and then an active cell in it. They have to stay within their own thin layer of cells. I'm not just picking some random SDR out of a set of minicolumns, which is what we've been doing in the past.

This is interesting. I'm not sure if you're following this. Our usual way is to say, here's a bunch of minicolumns, pick one in each column randomly, and that gives you a random SDR. But when I learn a sequence in temporal memory, I can learn a sequence between this random SDR and the next SDR. That doesn't work for path integration, because I need a sparse representation where, when I do path integration, I always get the correct next sparse. There must be a determined next sparse representation. I can't just pick one randomly. It has to be determined in the mechanism. It can't just be learned, because I need to move through the object space in the sparse representation of the object. I have to predict, based on the motor input, the next SDR location. I can't just pick random cells to do that. I need a mechanism for picking the next sparse representation. That's the problem I'm trying to solve.

Even if I just had each little layer—I'm not sure if this is possible—but each layer of cells, an individual cell in one of these sparse layers, would be path integrated. It would move to one of the next columns.

It would move to one of the next columns based on path integration, and I have to be able to predict where it's going to be. I need to go from a sparse pattern to a sparse pattern to a sparse pattern deterministically, based on motor input. If I imagine these are thin slices that are sparse, instead of six, just say there are two active in each little layer. Then each layer path integrates, each cell moves to the next column, just like these up here do, and it's deterministic.

I don't know if the numbers work out, but it would be deterministic. Let's say I had 15 layers of cells—not atypical. If I have two active in each one, that's two to the fifteenth space. It's not huge, but it might be fine. At any point in time, I have to think through this. I might have to do this.

How does it help us to have these layers? The thing we saw in the Tank paper is not sparse. There are only so many combinations. What we want is to have, simultaneously to this representation, a very sparse representation so we can make specific predictions. For example, given this location on a particular object, I need a very sparse representation. The challenge is how to have a sparse representation where the path integration is deterministic: if I tell you the current sparse representation and the direction to move, it deterministically tells you the next sparse representation, and the grid cells determine the next grid cells. These aren't sparse, but they would create the sparse representation, whatever the path integration method is. That would apply to each layer here, whether it's done through a minicolumn or another way. I haven't specified yet; I'm just considering possible cellular representations that would work.

Imagine under each of these, in the first layer, only two cells are active. That's not a very good representation—there are two extra cells active. Let's say all the cells in that layer try to path integrate, but only these two are active. If I had a whole bunch of layers, say 15 cells deep, and in each layer only two cells are active, and in each layer the same path integration occurs, then I might solve my problem. But how do you pick the two cells that are active? It could be random to start with, but if it's random, how is it path integrating once I've locked onto those cells?

Suppose you pick two at random and now you're moving in a certain direction. That means those two active cells would have to move. Only these cells move; there are other cells here which aren't active. When I do path integration, the active cells move to the next cell over, which becomes active. It's not that the cell moves, but within this group, the active cell changes. It's selected by being co-located with something, but I don't know how it would work yet. I'm just trying to see if the representation makes sense.

Let me rephrase the problem. When you have a sparse SDR, you need a deterministic path integration mechanism that, given any sparse SDR, does the right thing every time, even if you've never been there before. That's what path integration requires. In our original paper, we assumed there were lots of grid cell modules, each anchored independently. Then each one did path integration, so you'd always have the correct result. Once you figure out which is the active cell in each module, the whole thing would move.

We don't see this often. We assume there are maybe 20 grid cell modules, but what we actually see is six. That's not very many. If there are 20 different locations in a grid cell module, 20 different cells that tile the space, then there would be 20 to the sixth different ways of representing location.

But it doesn't look like that.

I'm sorry, I'm not able to communicate this clearly.

It's even worse because in the Tank paper, you wouldn't find two active cells. There are six grid cell modules. The assumption that there's a sparse, non-random selection in here is not just an assumption—you showed that you can't randomly choose a location in each module. These are all linked together. If this cell is in the upper left corner, the corresponding active cell in another module will also be in the upper left. So you only get one; you have a very limited number of locations you can represent this way—20, 30, however many cells there are in each module. These are redundant; they're not building a unique representation. They're just copies of the same thing, all moving together. You can't represent much uniqueness here.

So the question is, how do you get a unique SDR where path integration always provides the next unique SDR? This method, which we didn't invent, suggests that if you have many grid cell modules, each anchored independently, you'd have a high representational space and path integration would work. Given a unique SDR, you'd get the correct unique SDR for the motor. But that doesn't seem to exist, so I'm trying to come up with something else that might work similarly.

Now, thinking about it, in theory, this is like one grid cell module that's redundant because they're not really representing different things. It's just six for redundancy. You could argue that underneath it, there's another, and another, and so on. If I had 15 or 20 of these, it would be like what we had in the original paper: if you assume each one is anchored independently, that's what we described. But that's not what I was hearing from Tank and others.

I don't know. It wasn't clear. I have the impression that maybe I got off track since we saw some missing ones. I started imagining this was sparser and mentioned that the cells underneath here were sparser than these cells. This is close to what we described in the original paper: it would require the cells in this module and that module to be anchored independently. Then it would match our original paper, but there's not a lot of evidence for this.

The layer idea you just had up there—how would those get the extra information that's not in the six grid cell modules right now?

Up here, I'd like the 15 layers underneath to have a unique SDR for each location. If the grid cell module doesn't have enough representational capacity, would those 15 layers get the movement input additionally, or would they only base their two active neurons on the grid cell? I might have made a fundamental error here, so let me back up. Do you see the equivalent of what we had in our first paper and what we have here? If we implemented what we had in our first paper, these would be independently anchored. Do you see why we'd have a sufficient representation? Because we might have a choice of, say, 20 different locations here, and if we had 15 of these things, you'd have 20 to the 15th different unique representations depending on how they're anchored. That's a big enough number.

So that's the first question. Does that make sense? Yep. I got down a crazy tangent, thinking these guys aren't just like this.

There was no evidence of that. There's a whole other grid cell module, another grid cell module under it, and another grid cell module under it.

That would be anchored differently because if this is right below this, and we're talking really small distances—maybe one cell with 10 microns between layers, like one cell body—then some imaging would show multiple active cells. You'd see some cells just below the border and some just above, and you'd see two cells next to each other that looked like they were active at the same time, or two cells in the same module. You'd see one active from this guy down here, another up here, and you might capture both at the same time. He didn't see that, right? It wasn't like that. He never saw two in the same module active. But we did see that if you look down below this, at some point some of these cells disappeared, which might have suggested he was actually going down into this layer and just under the border, and he caught one of these cells that was off. He said he was measuring part from here and part from here. These things aren't perfect layers; they're wiggly, so he was capturing this part here and maybe these parts up here. This one is sparse. I asked him about that, and he said it might be, but he didn't know. That's when I started thinking it doesn't look like what we hoped in the beginning.

So maybe something different is going on.

Then I was trying to see if the numbers work out. This is all very speculative. Would the numbers work out if I assumed there was a dense, regular grid cell array up here, and underneath it there were multiple cells, but only one of those was selected, or just a few? These would all move as a group. They wouldn't be independently anchored, but they would be sparse anyway.

I'm assuming the grid cell mechanism, the path integration, will move all of them in the same direction, as opposed to being independent and separately anchored.

Clearly, the mathematically simplest one is assuming these are all independent grid cell modules, each anchored differently.

There wasn't much happening.

Do you know if any more papers came out from that lab since then? They probably have. When I talked to Tiger about this, it was very typical. I think he was curious why I'm interested in this stuff because it wasn't interesting to him.

That's my recollection.

Not very strong, but you try to explain why this might be useful, and it usually falls on deaf ears.

They're not thinking about unique SDRs for location representation. They're trying to explain basic grid cell function.

He said, yeah, there could be cells underneath there. He said maybe it's in the paper. He said, "I'm only looking at the right thin layer." I asked, "How do you know where you are?" He said it's difficult to say. They just took a layer where it looks like grid cells and mapped them out. I think I asked him what if he went further down. He said, "I don't know, I'd probably see the same thing." I asked, "Why is that one not showing?" He said, "I don't know." I asked, "Could it be that you were on the layer below?" He said, "I don't know, could be." He might have further papers. You could look for his lab, Tank lab.

I'm driving this right now purely from a map representation point of view—what would be required for our models to work.

Let me do the numbers really quickly.

Let's say, how many ways can you pick two out of six? Let's say 15. You have 15. 15 times 15.

That was like 15, 15, 6, 25. Those 15 or 15, right?

15.

What is 15 to the 15th power?

That would be approximately 4.3789 times 10 to the 17th power. That's what I would have said if I assumed there were 15 cells here spaced out, roughly about 10 microns apart. So you have a total layer thickness of 150 microns, which is reasonable. That's about a sixth of the total.

Then you assume there were two out of each of these, so sparsity is maintained throughout the columns. You might have two to the 17th representations you could form, something like that.

All this goes back to the idea that we have two representations: a very sparse one and a not sparse one.

Let's leave it at that. Is it possible? Yes, it's possible. The numbers could work out if that was true. Then you'd associate the less sparse one with the orientation.

Unless you're doing something that's okay. Sorry, I was looking for more papers. Here's an idea: what we've just proposed is a layer of grid cells that look like real grid cells, and underneath them, you have sparse versions where only two out of each module are active or something like that.

We were talking about how layer three would be more dense and layer two would be less dense. There seems to be some parallelism there. You are looking for general mechanisms that might apply elsewhere.

The only point of that is this represents the generic shape, and then this is the unique object locations.

This next one goes up to the bipolar cells. This is the lower layer three. Remember, there's a separate—let's just imagine this for a moment. This would be specifying the minicolumns in layer four.

Between these two cells, you'd be learning and inferring the basic shape of the object. Between this set of cells and another set, you would be learning the morphology. This connection is basically learning morphology, and this set of connections is for specific objects and features.

That's a very nice solution to not relearning similar morphologies for similar objects—not relearning cylinders for every cylindrical object. You just learn the specific features on that shape. There's a limited memory here; you can only learn so many shapes. But there are only so many basic shapes, maybe. It's going to be pretty limited.

I'd be interested to walk through the numbers and see how much generalization it would exhibit on its own, because you don't get a lot of specificity here, so it would be really blobby shapes. I'd have to think about what the representation is. But for each one, we have a very unique pattern. Does this solve something for us?

In some sense, you don't want to learn every point on an object. If I'm going around the coffee cup, I'm not really learning features; I'm learning the morphology. The morphology doesn't have much uniqueness until I hit something different. In all cases, I could learn the general morphology once and make predictions on the general morphology for any object that fits. You don't have to learn every point on common objects.

Remember how we talked about having a separate feature and morphology model, and mixing and matching them? Do we have an idea for putting different features on the same morphology? I don't think so, but this could be an idea. That is the same thing, isn't it? I forgot about that. This is a morphology model.

It's a rough morphology model. We might still want to learn detailed ones, but there could be all kinds of variations. Instead of all these cells projecting to all these cells, it could be laminar projections, in which case you might have a gradient between generic and specific. I'm trying to imagine possibilities. Let's say there's a morphology model based on grid cells and feature columns, column orientation. Essentially, the edge is at this angle at this location, another edge at another location, and so on. I'll have to tweak this to get it to work well. But then there's a sparse pattern here and a sparse pattern there.

This sparse pattern has to do path integration. I have to move to the correct new sparse pattern. That's a requirement of the model. But then I'm always able to pair a unique location with any kind of unique feature.

When you say the sparse pattern needs to do path integration, do you mean it just needs to be consistent? For example, when I move from A to B once and then move from A to B again, it will be the same SDR. It also means if I've moved from A to B and then from B to A, I have to go back to the same one I started with. Or if I move from A to B to C to D to A, I have to come back to A. It doesn't have to be a predictable change in the SDR; we could just associate three random SDRs with those three locations. But then, how would it know? It wouldn't be able to do path integration. If I go from A to B to C and then back to A, how would it know? It has to know to go back to A. I can't learn that; I have to just know it. I have to know that I'm back in the same location.

Couldn't the TZA modules do that part? I'm just saying the sparse pattern has to exhibit the same property. Could we just associate random SDRs with the representation? If I associated a random one with every location, then when I go back to A, I can't predict the random one. It can't be random. If the activation in the grid cell module is the same, wouldn't it then reactivate that? Originally, this grid cell module up here is not sparse. It's not very sparse. Those cells, in the tank paper, there were six. These are all working in a predictable form. If you go from A to B, you always come back to here, right?

What if we just associate a random SDR with each of these possible states of the grid cell module, and whenever the grid cell module is in the same state again, you can't—well, you could do that, but it can't be learned. At some point, it has to very quickly say, "I know how to do this," even if I've never been there before. One of the beauties of grid cells is that even if you've never been to a location, it forms the right representation. Maybe it would work the way you said, but that random association would have to work. Maybe it would work. Perhaps. We can all agree, though, that it has to come back to the same unique pattern.

I think the main issue is that one of the requirements, maybe not written yet, is that we don't want to have unions of possible locations. We want to have locations unique to the object. We would have different SDRs associated with the same state of the grid module, depending on which object we're on.

The grid module only has a certain number of states it can be in. But this should be unique to each object, right? We might have the exact same state of the grid module, but we want a different SDR down here because we're on a different object.

You're right. I forgot about that. How do we do a unique per object? Touching on that opens a big hole in the theory. In some sense, each one of these layers of cells has to be anchored.

Which two cells are active in those layers? I'm getting confused, but keep going. Start again.

You were talking about—yeah, I wasn't even talking about the different layers right now. What I was proposing was, what if we just associate the random SDR down here with each of the possible states that the grid cell module can be in?

In the beginning, when we don't know which object we're on, we would have multiple random SDRs active here for each of the possible objects. That would be a union of possible locations. I don't know if we want that or not, but that was the idea I was suggesting.

Then the path integration would be done by the grid cell module. If we go from A to B to C, back to A, this would be back in the original state, and the association to the specific SDR would reactivate that same SDR we had active when we were at A. I'm just getting lost a little bit here.

We have to do two out of the six modules, two cells out of each six modules. We randomly choose them— which two cells are active. I wasn't even talking about the two out of each layer; I was just saying disregard the layer and just pick a high-dimensional sparse SDR down here. But I'm not sure how it works if you just pick a high-dimensional sparse SDR down there. He was trying to tell me how it would work. Maybe I'm missing some constraint. If I have a unique pattern here, I have to come back to that unique pattern after I've moved around and come back in space. How would I do that if I just pick the random set here? The first time it will be a random set, but it will be associated with the state that the return module is in. So whenever the grid cell module is in that same state again, it reactivates the same SDR. But sometimes I want to activate a different SDR if you're on a different object. That's why we're saying if we don't know yet which object we're on, we would activate a union of SDRs down here. But if I knew what object I'm on, how do I know which one to pick here? That's a good question. We have to solve that problem anyway. Earlier, there's a suggestion that layers—three projects down to six. So this is the object, either that or the layer four connection.

I'm running out of steam here. It's a good germ of an idea, right?

I guess my brain's not working well. We can take a break. We should probably also get to coding a little bit. What time is it? It's already 4:15. I'm not going to stay late.

I think this might be the end of the day for me.