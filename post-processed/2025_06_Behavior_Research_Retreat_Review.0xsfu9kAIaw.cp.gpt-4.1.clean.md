Welcome everyone to the post-brainstorming week research meeting. Are you going to summarize the 20 hours of research in the next couple of minutes? That's the idea, although it won't be a particularly concise overview. We'll be working through the notes we wrote last week and the provisional conclusions we reached about object behaviors. We'll probably disagree and argue about some of those, and new discussion points may come up because of that.

Tristan and Will, you probably haven't had a chance to watch any of the material? No, I haven't. I was ill yesterday and didn't do anything.

This was the first time we did one of these brainstorming weeks entirely remotely. We had four days, each with a four-hour session to brainstorm individually and then a four-hour session to meet and discuss. Some discussion happened through PowerPoint, but much of it used Excalidraw, which worked well for remote whiteboarding. Vivian added helpful boxes showing the different days, and you can see how we progressed through various concepts. It would be too much to go through all of this again, and we'd be covering the same ground. While brainstorming, at the end of each day, we tried to capture any reasonable ideas or provisional conclusions in gray text to indicate they were tentative and worth remembering. The main idea today is to go through this text, check for any disagreement or confusion, and refer to diagrams or figures that informed the discussion where relevant.

Are there any questions or comments?

This will probably take the whole meeting, but if there's more time, I thought more about the proposal I made last time about optic distortions. I noticed an issue with it that I could discuss briefly, along with a potential solution, but no worries if we don't get to that. For context, for those who weren't there last week, there were a few different ideas discussed. The most important was Viviane's proposal on the last day about distortion maps and how those could be used.

That's what's conveyed here. At a high level, it's about taking concepts for how a parent can influence information coming into a child learning module and bringing that into one learning module as a way of dealing with object distortions.

In some ways, it could be nice to start with that because we could always go through these comments offline, whereas the discussion you're proposing is harder to do offline. We can also start at the top of the questions and naturally get to the one around object distortions, and I can go over it then. Sounds good. I don't want to take away from the summary.

The first thing we looked at was how to actually learn object behaviors in a reasonable amount of time. As we've discussed many times, it's challenging given their complexity, as well as how we quickly do inference and the relationships of voting. One topic was whether sharing knowledge across columns might enable more efficient learning. We had an extensive discussion about the role of hierarchy for learning, particularly at the highest level. It wasn't directly related to object behaviors, but it was still an interesting discussion about learning.

The reason it wasn't that related is because the solution applies to both static and behavioral objects, and it was easier to talk about static objects. The problem becomes more apparent with behavior models, as it's difficult to observe everything about a behavior.

In typical fashion, the first sentence is already a bit confusing: the way we can use hierarchy to infer objects with a column that hasn't learned the object yet doesn't make sense. This means we can remove the requirement for all the lower-level columns to learn a model of each object. They will only learn the object through high repetition, but we can already make predictions based on models learned quickly in higher regions.

I think this relates to the figure you pulled up before and the example of learning an object through touch and then inferring it through vision, where we have a high-level model of the general features. Each of the subcomponents has models in both touch and vision. You know how an edge looks and how an edge feels, but you don't have a model of the compositional object in the lower columns yet; you only have that in the higher column. We discussed that, and I think we also concluded that we're learning at different resolutions, where it's okay to learn in parallel at different granularities. If you need to learn details of the lower-level objects, you do that through repetition.

Exactly. That's what's stated here: a high-level model has low resolution and fewer learning locations, so it can be learned quickly, while a high-resolution, low-level model generally requires many observations and is learned more slowly. We discussed how the high-level model might even be more like a hippocampal complex in biology. This was the first point we already discussed, so I've moved it down.

One tends to attend to coarse features first when learning rapidly at a high level. However, you can also attend to detailed features and learn these rapidly at a high level of awareness. For example, with the hippocampal complex, you can walk into a room and quickly see all the pieces of furniture or large objects, but you can also attend to something very detailed, like letters on a page or the arrangement of objects on a diagram. Because of the speed at which the brain picks that up, that's clearly happening at a very high level as well. The key factor is that it's still not that many locations, so there's a difference between the number of locations and the scale at which it's happening. If you're learning a diagram with a lot of detail, that's still going to take a lot of time. If you're learning a whole room with many different objects, that's also going to take a lot of time and require a lot of capacity. It doesn't really matter whether it's at the scale of an entire football field or a piece of paper in front of you. What we tend to notice first are these coarse features that stand out.

If I say anything that anyone disagrees with, let me know; otherwise, I'll keep going. Location space at the top could be detailed, but we may not be storing a lot of points there. We can interpolate between features, and if we pay attention to details, we can store more features at granular locations. This is similar to the earlier point, just also mentioning interpolation.

Learning coarse models first and interpolating until we fill in the details should also work at lower levels, but will require more observations, as we can't rely on informative, compositional inputs.

I'm not entirely clear what's meant here. If anyone remembers writing this, please comment. This was about the general strategy working at any level in the hierarchy: we first learn a coarse model of the object, which allows us to make rough predictions by interpolating between the few points we've stored.

That can happen anywhere in the hierarchy. At the low level, you're just getting raw features as input, so each point you store isn't as informative as at a high level. For example, input might be "chair at location X," and you already have a model of a chair, so you can use that to make predictions about all the locations on the chair. At a higher level, you're already getting more informative inputs for each location, like entire descriptions of models you know about, so your points help you more.

Attentional masking to only use information from parts that are moving can help here.

We then thought more specifically about object behaviors and how to be more efficient when learning object behaviors quickly. This can help with learning object behaviors efficiently. We later had a more in-depth discussion on attention.

For learning behaviors and morphology, we don't need to share knowledge laterally or hierarchically. Learning happens at all levels of the hierarchy in parallel, with learning happening fastest at the highest level. This is separate from using hierarchy to support multimodal generalization.

We discussed how maybe there's some way to share knowledge through lateral connections or hierarchically, but what we described was a way for learning to happen really fast at the top of the hierarchy, which enables us to do useful things while spending more time in the world. This gets you into expert mode by learning more models at the lowest level, but there's no transfer of models between columns. We discussed how that was problematic if we're constrained to CMP signals, and it's not clear how we could do that. Jeff also brought up neuroscience evidence showing that knowledge is not transferred from the hippocampus down the hierarchy, but instead is relearned at every level over time, which matches biology. Does anyone know what papers that might refer to? That's an interesting point. The classic finding is that someone could never learn a new skill, but I'm assuming Jeff is referring to a study where, with sufficient exposure, a patient with hippocampal lesions did learn new things, just much more slowly. I seem to remember there was evidence for learning motor skills, but that could be more subcortical, like trial and error in the basal ganglia.

Just to make sure I understand the problem and the solution: the problem was that we were trying to figure out a way to observe different parts of the behavior at the same time on an object. We assumed there would probably be some shared learning so we could observe different kinds of behaviors simultaneously. The solution is that because the higher regions have a larger spatial receptive field, we should be able to build a coarse model of the behavior at the higher levels. We don't necessarily need to transfer it down to the lower levels, but we would still have this coarse model of the behavior at the higher levels. This assumes that the lower-level columns don't need to have a complete model of the behavior. I don't think it was necessarily about the size of the receptive field or not being able to see all of the behavior at once. The assumption is still that we'll have to observe the behavior multiple times and look at different locations on the behavior to learn it. Even the lower-level model can learn that behavior; it just has to see it more times and look at all the locations more often because it learns more slowly. To me, the big question was how it is practical to learn a behavior. When we think of our models that have 2000 points and the optic changes after a second and it's in a different state, how is that realistic? The answer is that we just need two or three points to start with, and we can start making some predictions quickly. The next time we observe the behavior, we add another two or three points, and our predictions get better over time.

So it doesn't really solve the problem of learning a behavior quickly in one column because we still need to do the same repetitions. We can never avoid having to move over the behavior to learn it, because even at the highest level of the hierarchy, the input is still just features at a location. We don't suddenly get a bunch of locations at once as input. We also discussed the effect of voting, which helps with some of that. If all the columns are voting on both the object and the state it's in, that information could be passed up and inform a behavioral model that can generalize, but that's only for inference, not for learning. For inference and learning, you would learn, for example, that the stapler top is moving. Stapler top is a broad feature, so if you know where that is at a point in time because of your behavioral model, that can enable you to generalize to other parts of the stapler top. You don't need to learn every single point of the stapler top that was moving. That's more like using compositionally versus using voting. You can use voting to prefer the stapler top pose at the lower level, but at the higher level where we're learning the model, it's more about having this compositional object already. We just need to store a few points to make predictions about it.

During the brainstorming, I had the feeling that the idea of the horizontal spread of learning—sharing knowledge across columns in the same region—might be promising to solve the need for repetitions if the knowledge is being spread horizontally across the columns, since they all see different parts of the behavior at the same time.

Maybe we can discuss that later outside of the summary. The stuff we already discussed helps make that tractable, or at least seems like it would be tractable to a reasonable amount of observations. The observation in humans is that we do need to observe behaviors many times. If it's a totally novel behavior for a child, they can't just zero-shot or one-shot learn that in the same way they seem to be able to learn morphologies. Like the behavior you showed with the logo moving around on the cup—they watch it a bunch of times. It wasn't like all the columns just saw it and then transferred the knowledge compositionally. For behaviors like the inflating of a balloon, it does feel like you might be able to aggregate knowledge from neighboring columns because they all feed into one behavior, and there's no positionality there.

It might be a mechanism to explore more if we run into limitations of what we have so far. What we have right now seems pretty powerful already, so maybe we just have to practically test it and see if it's sufficient. It would be nice if we don't need to rely on the lateral spread of information, because we also don't necessarily need to learn every object in every column.

I have a question about the predictions. We're talking about learning quickly and being able to start generating predictions quickly. Are those predictions generated in a higher area and do they show up in the lower area? Is there some model sharing going on? If a higher area makes a prediction about what might show up in a particular location in a lower area, is that the case? When I said predictions, I was referring to what every learning module does all the time. Whenever you get a movement input to the learning module, it will activate a new location in the model's reference frame. At that location, we have storage of certain features, so it will predict to sense that feature. By that definition, it would be happening at every level in every learning module that has a reasonably confident hypothesis. Predictions basically stay within that level, and then they narrow down hypotheses or have prediction errors to attempt to learn new things.

All within, constrained within the learning module. Got it.

When we say learning is slower at a lower level versus a higher level, is it slower in terms of adding observations, like an adjustable learning rate, or is it just because the number of observations is small over time? No, it's more the learning rate. There are probably many factors, but at least two we could discuss. In biology, it's expensive to learn quickly; you need almost specialized neural hardware to make rapid connections. The hippocampus seems specifically evolved for that and is a large structure compared to an individual column. With representational drift, you might not want the lowest level representations to change as quickly as the highest ones, since the highest ones use what's lower down. There may be a benefit to less rapid plasticity at the lowest level of the hierarchy.

Those are at least two factors that come up. In Monty, we might not have the biological constraints, so maybe we want more rapid learning at multiple levels. That could be a way Monty is superhuman, but maybe there's a reason the hippocampus is at the top of the hierarchy and generally doesn't deal with very low-level sensory input. I wonder if a slower learning rate might be advantageous for generalization. If learning rates are too fast, you might overfit on a behavior, but maintaining some coarseness makes it easier to overlay on novel objects. That's a good point. The hippocampus is good for rapidly learning a particular instance, but you want diversity in the models that are learned. Having different learning rates allows some to specialize in learning exact instances and others to be more generalists.

Any other thoughts?

Ramy, you brought up a fair point that it wasn't clear how some of what we discussed mapped onto object behaviors. All the stuff we agreed on turned into black. I added that we learn coarse models and interpolate between them, which we can do better at higher levels. The above also relates to behaviors, either core sensory inputs—flow over a large region—or compositional inputs. For example, EEG or a stapler top moving enables a high-level learning module to quickly learn a behavior model with a few points that already enable some basic predictions.

That sounds reasonable to me. Maybe use a different color than black, like blue, to distinguish questions from answers.

So the summary is we rely on a system that will learn a few points and interpolate between them later. Adding more detail helps to end the coarse model at a higher level because we can use compositionally. Maybe just write—oh, that's driving me nuts.

Do you try refreshing your browser window? Maybe I should. I wonder how quickly your brain can learn that special offsite. I think it is consistent. Okay, thank you. Turn it on and off again. Always works. By the way, maybe I'll go down to here, and to keep it interesting, we can take turns reading so you don't have to just listen to me. Scott, feel free to bow out from that one.

For inference, this is where the multimodal part comes in. When it came to the hierarchy, this was where Jeff first brought it up. How do we do multimodal generalization? For example, learn with vision and infer with touch. If a high-level learning module has previously learned the association between two low-level objects or sensory features from different modalities—for example, the touch and sight of something sharp or the touch and sight of a cube—then if we encounter a new setting where we observe one and learn it as part of our high-level model, we can immediately predict what we'll sense in the other modality at that location.

Hierarchy is necessary to recognize a novel multi-feature object that has been learned in one modality and inferred in another. For example, if we saw a complex object and studied it with our eyes, we would need to use a high-level multimodal model to attend to each part when touching it blindly in order to recognize it as the same object.

That still sounds good to me. That was a big one, since the problem came up many times over the past year: how can you learn an object with your finger on your right hand and then infer it with your finger on the left hand? Maybe that's another good example to include. Since the brain always has hierarchy, even though most things are solved within a column or start there, this is a neat way hierarchy can be used.

This should also work when generalized across specific sensory inputs within a modality. For example, you can learn an object with one finger and recognize it with another.

Sometimes you cannot generalize with this mechanism. For example, a logo exploding in visual space—that behavior cannot or shouldn't be inferred by a touch column.

Maybe say a logo moving, since "exploding" doesn't sound quite right.

Not everyone is intimately familiar with the exploding logo yet. We can bring it to the world, put it up in Times Square, make it famous.

How can columns collaborate to infer behaviors? To recognize states before they change again, we agreed that columns should share the point in the sequence with other columns, though it's unclear if this should be done through voting or broadcast by the matrix cells.

In biology, voting could be a reasonable approach to identify where we are in the sequence or behavior. There shouldn't be too many elements in a sequence at any given level of the hierarchy, so it could be realistic to vote even on the state in the behavior. We discussed how many points there are in a song, words in a sentence, or a paragraph, and at what point to break it up hierarchically, like breaking up a song into verses or four-by-four notes.

Any questions or challenges to that?

The last topic is related to the governance: how does voting work for behaviors? Do we vote on behavior ID, pose, and point in sequence? These answers moved back and forth since they all touch on the same thing.

There was discussion that it might be too much to ask the thalamus to encode timing in the matrix cell output, specific to a given sequence. Jeff argued we shouldn't discard this idea yet. It's something to keep in mind, as we haven't really decided.

Moving on to object segmentation. Does anyone want to take this one?

I can do it. Do you want to share your screen or read out here? I'll be doing it on the other screen and not logged into the Teams meeting. Please scroll up and down while I type or read, and then I'll highlight it blue. 

Object segmentation: we're talking about a hierarchy where we have composition objects. For example, the stapler—we learned the morphology model of the stapler, and then the top part starts to move up and down. We thought attentional masking would allow us to define an object in the lower region column, like only the top of the stapler has moved, so we want to attend to that part and define it as a mask.

We brought up evidence that the TRN allows for attentional masking through the spotlight hypothesis, where it defines attention on part of the retina, since the TRN is also retinotopically organized.

As an overview of the neuroanatomy: the TRN is a thin sheet of inhibition that applies inhibitory effects on the LGN or the whole thalamus. The TRN is divided into sections based on modality. There's a part of the TRN called the PGN, the perigeniculate nucleus, which is matched one-to-one with the LGN. These are involved in vision inhibition. The PGN receives input from two places: the LGN, forming a loop where the LGN excites the TRN and the TRN inhibits the LGN back, and from layer six in the cortex. When it receives input from the cortex, that's model-based inhibition; when it receives input from the LGN, that's more model-free inhibition, since it doesn't have models of the world.

We have a bunch of notes at the bottom after all the questions, so we might need to sort them in. You're better at note-taking. While we were talking, I'll just add this: is the behavioral model able to attend to regions or templates? It seems reasonable that this would consist of model-free and model-based attention, and I'll add this up here.

One thing we didn't address is whether this attentional mask leads to a permanent model in the lower-level columns. Are we using the attentional mask so that, over time, the top of the stapler becomes a separate model from the bottom, or is it just a temporary mask for predictions? I think that's covered here. How do we communicate outside the column? We don't communicate entire models, so it's unclear. We need to communicate partial models, but this may be sufficient in the long term, as we will learn a new sub-child object morphology. In the short term, we can attend to the relevant part.

We might learn a model in the long term, but it doesn't specify how. Once we invoke a mask, does it turn into a totally different reference frame, or is it still related to the object reference frame? There are still open questions. If we consistently get this inhibitory signal—only getting the mask from the thalamus—the model through heavy learning might start to forget about different parts of the object that aren't reinforced.

This means one column wouldn't have a model of both the stapler and the stapler top, because it would forget about the whole stapler if it keeps paying attention only to the stapler top. The model of the whole stapler would be in the higher region, and the parts would be in the lower region.

That could be. I guess it would still have to be fairly consistent, because once the stapler stops moving, we'd be paying attention to the whole thing again. So we would still be able to learn or retain the morphology of the whole stapler.

That's a good point.

One thing I don't feel like we had in these notes, which I'm adding now, is: what are the key elements of attention? There is what draws our attention to something, and there is what narrows our potential window around, like, subselecting the input. These aren't always the same thing. I think there are some notes about that.

To me, this is about top-down decisions regarding where to attend.

I was looking at the bullet point below. It says there's top-down and bottom-up attention, both of which limit which columns are processing input based on where in space they're sensing.

Did we put that somewhere already? Yes.

I'll just delete it down here.

Did we get that first sentence, though? Maybe we didn't. So, there are also top-down and bottom-up factors determining the attentional window.

I'm not sure I understand the distinction between drawing our attention and narrowing the attention. For example, if you hear a sound, that's a bottom-up signal that draws your attention to an area. But when you're actually looking at something, that's different from what's determining what's coming into your retina.

It's more about informing your organs how to move in the world, versus masking what's coming in and saying this is irrelevant. Is that basically top-down versus bottom-up? No, I feel like top-down and bottom-up are in both.

Maybe I'm not understanding the narrowing down part.

To me, narrowing down is when you're looking at something and you just mask part of it without moving. It's not like you feel some stimulus in your visual field and start looking towards it. The narrowing down would just be masking part of the input without movement. The other kind of attention is when you feel some stimulus and move towards it, fixate on it, and then start masking to that part. If we start with the last bullet point, which is that top-down and bottom-up attention both limit which columns are processing input based on where in space they're sensing, that includes both narrowing down and drawing attention. It's about which parts of space we want to process and which we don't.

But I feel like it's helpful to break them apart, because they're driven by different mechanisms. Drawing attention is like using action commands to move somewhere—overt attention. Narrowing is more like covert attention, deciding which columns should process input. The only confusing thing about using the term "covert" is that, behaviorally, it usually refers to keeping all your sensory organs frozen and attending to a particular region. In reality, these tend to overlap: you move your sensory organ somewhere and then use attentional windowing at the same spot.

So, there's what draws our attention to something—attention that requires moving sensory organs to focus—and attention that narrows the sensory inputs received, given their positions.

The former is overt attention. The latter is covert. Usually, both happen together: we move our sensory organs to something and then focus them to the window.

Either top-down or bottom-up mechanisms can drive both of these. They're both part of the same mechanism. You get some stimulus, want to attend to some part in the field of view, and if it's not in the focal point, you go to it, then narrow your attention and mask it there. If you're already looking at it, you just mask it. These are two steps of attending to something.

I'm not suggesting they're totally unrelated. Sometimes our language refers to moving sensory organs, and other times it's about narrowing the potential window. As far as the LM is concerned, in terms of sensory flow, they're different: one is a movement causing a different sensory input, and one is a way of processing sensory input.

But I agree they happen together. I think we had a similar note here, but I'll change it to say "processing input in a certain region independent of moving the sensors." It's about which area in space you're processing, regardless of how or where you're moving the sensors.

With vision, moving your sensory organs is often a response to a sudden flash or movement, so you move your eye there. The fact that there's a big, coherent blob of movement tells you it might be one object, so you narrow your sensory input to that.

It starts model-free and then becomes more model-based. In that case, both are model-free.

You're just using some heuristic about the boundary.

Okay, cool. Is that clear?

Let me just check what other stuff is down here.

I'll use this as an example.

This may relate to what Scott is starting on.

Maybe I'll just say for the Al window, maybe something like this?

You have that up there.

I think the other things we can get to later. Finally, we can just read through the questions and then the answers. This is what you were just saying earlier.

With the thalamus being involved in attentional masking, it seems reasonable given the neuroanatomy. The TRN seems to be able to support both model-free and model-based approaches. You mean given the layer 6 inputs?

Basically, it's just layer 6 to G.

Maybe one other interesting thing you talked about that's worth mentioning is the colocalization of the receptive fields, as in the layout is both retinotopic and organized.

For clarity, the PGN is the nucleus in the TRN that corresponds to the LGN, or the part of the RN. This is the vision sector.

There was also information about how the receptive fields of the PGN nucleus, or neurons, are complex. They represent complex shapes that are more reminiscent of receptive fields and features in the cortex.

This would be very useful if you want to have an attentional mask over an object or some boundaries, because they're detecting more than just simple features.

That was PGN in irregular with complex features. Are they dynamic as well?

Presumably, they would have to change. I don't know if it's observed that they change given what is presented. I would think that because they get input from the layer 6 neurons, they change based on the input, but I don't recall seeing that. That's what we'd want, or it would be interesting if they had that.

I would also think they could have combining effects if they're applied together.

That might be the alternative: maybe a single cell's receptive field is fixed, but you can combine them to create arbitrary masks.

What can enable attentional masking—agreement or movement-based masking?

How does a column neuron represent this attentional mask?

Now, this is only in the cortex.

I guess the movement-based masking could be the model-free type masking.

We discussed ideas around how a column could use sensorimotor displacement associated with votes to predict when it'll move outside of an island of agreement. This is the island of agreement idea.

We already require sensorimotor displacement to process votes, so at least in Monty, that kind of information is local to each learning module. You could use this to look at your votes and see if you're about to move—was one of those votes from somewhere you're about to go? Based on whether that vote was from a consistent object or not, you decide whether you're going to be seeing the same object you think you're seeing now or something else. That could inform prediction.

It's a form of model-based attention, so it could be complementary to model-free signals. It's computationally feasible given the information that's local to learning modules and Monty, but it's unclear if that's biologically plausible. We've always been a bit uncomfortable with this kind of center displacement for voting. It's also unclear how important it is that the column can make this prediction accurately rather than just incorrectly believing the object will continue. It gets to the question of how important this temporary mask is in the first place. It feels intuitive that we have the sense that the object stops. We discussed some examples of that with static objects, which relates to this question, but maybe it's not actually necessary.

If I understand this idea, you're talking about a prediction error between the sensors. If you're trying to predict some feature in the other sensorimotor area and you're not able to, you're saying this is a different object. No, I think it's simpler than that. Let me see if I can find the slides I had.

It's basically the idea that a column getting sensory information from location A is voting with other columns at B, C, and D. The votes from columns at B and C are consistent with what column A is observing, and the vote from column D is inconsistent.

If column A is about to move, it will look for a vote where the sensorimotor displacement that vote is based on is similar to the inverse of the movement that's about to happen.

It could say, "I'm about to move where column B is, and I got a vote from column B. Did it agree with me?" If it did, then it's part of the same island of agreement—we're seeing the same object. I can use my own internal reference frame to predict what I'll see at B. It wouldn't try to get the sensory information from B directly. It would just ask, "Am I likely to still be in the same object?" Then I'll use my own internal most likely hypothesis and reference frame to predict what I'll see at B. If it was moving to location D and did that comparison, it would see that it's different, so it needs to look at the vote from D rather than B or C. It's different, so I'm going to predict that I'm off my reference frame. I don't know what I can predict, but I know I'm not going to see what my current reference frame would predict. It's dynamically determining whether we are moving beyond the island of agreement, but only for that one movement. It doesn't try to calculate a boundary everywhere all at once.

Okay. So it relies more on sensorimotor displacement than on actual features. Implicitly, sensorimotor features come in with whether these learning modules agree in the first place, but it's not doing a direct comparison with those.

It also relies on having pretty accurate, unnoisy votes to use for this. If you're getting lots of votes, you can maybe pull multiple of them. Have we solved how voting works in general in this scenario? We could just say it's not a stapler anymore because our votes are not agreeing. When the object changes, I think it works fine in that there's always a sufficiently large subpopulation that, even though some will disagree, others will agree. If voting is happening in different sections, it might be that we're definitely seeing a stapler, but we can't all agree on where it is.

Note that half of A's incoming votes would say one pose and half would say another. Votes can't be as important as what A itself is sensing; pose is as important as object ID, or more, as in what it's sensing is only consistent with the votes coming from here. Even if it got 50 votes from each, as long as its own sense of where it is remains significant, then it's an easy competition.

Basically, the votes are just biasing it, but it's relying mostly on what it itself thinks.

We're using the incorrect votes to modify the evidence, which may confuse the learning module because it's getting a lot of wrong votes.

It might think, "I have the stapler, but 50 of my votes say it's in this pose and another 50 say it's in that pose."

We would have to modify our current voting algorithm. I'm not saying it's impossible, but we need to explore this more. Our current learning modules would get confused, as Rami says. At the moment, a vote has the same amount of influence as sensory movements within a learning module—all the votes combined, not each vote.

We can figure out that this is a behavior because we're getting a lot of votes from the bottom of the state without saying it's this pose. Then we can detect a behavior and figure out a heuristic to exclude all of these votes because we're now in this behavior model rather than still trying to detect one pose. We'll just say these are all consistent with a different pose, which means this part is moving, and we can exclude all of these votes from modifying the evidence.

I can imagine having a heuristic where I'm getting two general themes in the votes, picking the favorite one, and ignoring the other.

Using that to model a behavior is maybe a bit complex. Would this problem go away with compositional objects? Then you'd be ignoring votes for different sub-objects as opposed to different poses of the same object.

Once we split the stapler into two parts, that wouldn't be an issue anymore. In this setting, we were hoping to get it working so that you see a stapler, and then suddenly half of it splits off and starts moving. You can instantly segment that and treat it as its own object temporarily, because you haven't had time to learn it as its own model.

Once we've had the chance to learn it as a child object, it's not as much of an issue.

The reason we want to apply this mask and keep using the model is because once it starts moving for the first time, you don't forget everything you've already learned about the stapler or the phone. You still expect the colors on the stapler to remain the same on the stapler top and just move. You're still using the model of the stapler you learned, but only the features on the part that is moving. Even in your head, you're thinking, "This is a stapler or a phone," but it's just part of the phone moving for some reason. It's part of an object you know, which is normally bigger, that's moving.

Maybe we leave this in gray and add another open question about how voting works with object behaviors and what we might be able to use voting information for.

Can it help us inform learning behaviors and masks?

We discussed that voting might be problematic more generally, but maybe that's too general. Using voting to inform recognition of behavior models was discussed above, and masking is discussed here. My bias would be to leave it just at learning.

I was thinking to put the gray bullet above, underneath this point, but we can also just remove it. It's worth having another meeting to talk about voting and all this stuff. Maybe we—how did this start? Object segmentation.

When we revisit this at some point, when we're not confused, I'll leave that gray. Sorry, what did you say? I wonder about what model freeness might give us beyond just attentional masking. If we had movement signals that were also available, then two points nearby on the top of the stapler should have the same or very similar movement vectors from time point to time point. Beyond attentional masking, that should provide information that these two points are likely viewing the same object. When they vote on what the object ID is, it seems that should help narrow down what the object ID is. There are priors now: whatever we're seeing in terms of the object ID, if our movement vectors are the same between neighboring LMs, then you should weight higher whatever that vote is for the object ID.

I guess that would happen at the level of the learning module's output. A particular learning module might think, "I'm seeing the stapler moving," because they wouldn't vote on sensory input. To your point, there's movement happening, so they would infer that the stapler is moving, and they would agree about the direction and speed or whatever the stapler is doing. They're much more likely to think, "We're seeing the same stapler," than LMs that might see the stapler not move at all. Maybe the model-free sensory input already contains enough information—it's already informative enough to create these potential masks. Having those potential masks would help solve the voting problem by saying anything in this model-free defined region can vote with each other. It's almost like a prescreening of agreement islands. It's not totally clear in my head how they interact, but it feels like a lot could be leveraged with the movement signal, maybe at various stages.

I think it's a good idea to look for coherent optic flow or something like that, since that's a simple feature, but I can't think of an example where it wouldn't come from an object that moves.

Maybe under "more generally," how can we work on subject-ordinary—the model-free approach could help limit payment by ensuring only relevant elements are processing one another.

Should we add coherent optic flow somewhere as a potential bottom-up signal? We have regions that are moving, but maybe also moving together as an additional factor.

Maybe, Rami, do you want to—

Could, can, or should this information be communicated outside the column? I assume we're talking about the mask. Would we want to communicate that outside the column? Not really sure. Maybe I'll say a model-based mask, irrespective of how it's derived. We don't communicate entire models, so it's unclear if we need to communicate half models. This isn't about an object ID; it's about the actual model—all the associations between features and locations. Do we want to—

It may be sufficient in the long term to learn a new sub-child object morphology, while in the short term we can attend to a particular region.

I would agree. Probably don't need to—I'm not sure. Should we make the language stronger? I would just remove the last part of the sentence and say, "We don't communicate whole models, so we don't communicate half models either."

Everything up to the dash could be taken out, since the second bullet covers how we learn the new child. At least the way I read it, it's clear. In the last part of that sentence, we should make sure that "while in the short term, we can attend to a particular region" refers to this region being defined inside the column and not shared.

So, while in the short term, we can use masks—local attentional masks or model-free.

Maybe I'll make it clear here: we don't communicate intentional masks outside of the column.

But if we have a model-free mask that gets broadly distributed by telling which columns should be processing the input and which shouldn't, that mask gets broadly applied already. This question is more about whether a top-down mask should be communicated outside the column. I feel like it would be through the hierarchy. Maybe what this is specifically getting at is: the subcomponent becomes part of a parent model. For example, we know it's a stapler top in this column. Is it telling the higher-level learning module, "By the way, I'm just a stapler top," or "I'm just part of a stapler"? That depends—are we changing the object ID, or are we sending the same object ID? That's what I was trying to imply: over time, you would learn a slightly different or totally different object ID for that child object, but you wouldn't develop that immediately. The last part doesn't make sense to me. In the short term, you just don't have that information at the higher region if we can't communicate the mask.

I think that was referring to the particular learning module that has it, but maybe it's not necessary to specify.

How would we prevent the higher model from thinking there are actually two staplers? With the way we have compositionally, it doesn't really matter. That's what happens with the mento logo: the high-level learning module thinks there are a bunch of new mento logos. All it knows is there's a new mento logo at a particular location. Remember, the hierarchically arranged columns have co-located receptive fields. The higher region doesn't get inputs from all locations on the stapler; it just gets input from the top of the stapler where the lower region is sending its input.

It raises an interesting question: how do we count child objects?

How would a high-level learning module know, as you said, Scott, how many child objects there are? It's interesting to think about because we can count objects.

Why do we need to count the child objects? This moves beyond what we've discussed recently, but as an ability of intelligent systems—at least humans—we can count things. In our compositional models, we generally keep laying down points to capture structure, but we can't just count how many points are associated with a particular object at a high level, as that would lead to overcounting.

When you have a point, you're indicating a different instance of the same object from another learned point. Especially if you have, for example, a logo that's bent halfway and you're storing two different poses, the high-level learning module might interpret these as two different child objects.

We can revisit that later, but it's an interesting question you brought up, Scott.

Another point discussed was whether learning modules need to store an attentional mask. If they're already getting sensorimotor information, maybe the attentional mask doesn't need to be represented in the column at all. My thinking was more related to sensorimotor modules and the learning module.

I'm not sure if that makes sense, but I remember thinking that maybe this isn't strictly an object behavior issue, but more generally, whether we're trying to recognize a static object or a behavior, we're already attending in both cases.

My question is: can we assume the learning module is already processing something because we're already attending to it? Do we have attention "for free" in some sense, because the act of doing something about it means we're already attending to it? Maybe I should just write that down as a question. My understanding is: is model-free attention sufficient?

For it to be model-based, it has to involve the cortical column somehow. If I'm understanding correctly, that's one way to phrase it. There's also the question of whether it's important that the column can make this prediction accurately, or if it's enough to increase the belief that the object will continue. This gets at whether model-based attention is necessary.

At least in the sense that we can use models to guide our attention to a new location, to move our attention—attentional windows, model-based masking.

We're assuming any sensory information going into a learning module has to be processed, which is why attention is handled outside the learning module, in the thalamus. But if we already have the signal of what we want to process, why can't we do it in the learning module directly? What you said earlier is what I was trying to say, but better.

Can we do attention directly? Can we ignore some of the input from the thalamus if we already know the attention mask and what we want to process? Or is that what we're already doing? The signal for that could be model-free or model-based. It could be based on simple heuristics, like things moving together or a large flat area with edges, or it could be model-based, like recognizing a stapler and focusing on the area it occupies based on hypotheses.

Does this relate to what Scott brought up about whether the model-free attention mask is powerful enough to solve some of the later processing, like voting disagreement, if we rely mostly on model-free signals for masking?

I'm glad we added this question. We can move on now. I just want to remember: how do we learn a new child model? Does it have an entirely new reference frame? I think we covered that already. I'll just turn it into a question, though we don't have to discuss it now. I don't think we have any good answers—it's a controversial topic. The bias would be to create a new reference frame because, as Viviane said, sometimes we need to recover the whole model and sometimes we don't. If we're applying a temporary mask, we don't need to create a new one. I see why this is controversial. I agree with you about the model. I think it's the SDR overlap issue that's maybe the sticking point. For masks, it means we're sending the same object ID, and now the parent object wouldn't know that this is just a part of the object, not the full one.

That would be my bias as well. Maybe we can write that having serial overlap would provide the benefit of commonality in the child and parent. If we use the term "child," it could get confusing.

"Break off" makes sense—it would be a child object. At least in this case, a single learning module might have a model for both the whole stapler and the break-off part, so there's no hierarchy within that learning module necessarily.

There's also the view of having a stapler and then at some point taking the stapler apart, like unscrewing the hinge and pulling off the top. It's not like I have to learn a brand new model of the top of the stapler after I completely separate it from the rest of the stapler. It seems like we transfer some of the knowledge. Perhaps I would make this gray because we are not certain enough about this answer.

Scott, I think it's a good point.

I don't know if this is actionable, and hopefully this isn't backtracking too much, but I was thinking about the islands of disagreement, specifically in the restricted case of the stapler motion. If there was more than just disagreement, but disagreement was specific in some way—whatever that angular distance was—that would be enough to encode where you are in the behavior sequence.

All of these are green on a sequence identifier. Maybe this already fits into a model we have, but I'm thinking about the particular case: these agree and say this orientation, step two, these agree and say a particular orientation relative to the previous one. Knowing the relative orientations of disagreement, in this small example, defines the location within the entire behavioral sequence. Maybe that's already something we get out of the parent-child relationship. That is probably something that already comes from the parent-child relationship, now that I think about it. Maybe it's something Rodney was suggesting earlier about learning based on disagreements and votes. It feels like voting isn't a great place to represent that. Voting will be used to get the two poses and child object IDs, but to represent it, it's better to do that in the parent column: at this location, we have stapler ID at pose X, and at this location, stapler ID at pose Y, versus having to learn that from all the messy votes coming into the child column.

In that sense, it's tying back to voting on the location within the sequence. Maybe that is better done at a higher level. It might be too much at the lower level. They could vote on where they are in the sequence, but they wouldn't try to store it. How would you know? Maybe if it's consistent enough, but voting works best when they're all consistently the same. I don't think it would work with voting because we can't do coordinate transforms. It wouldn't generalize to new relative orientations and things like that. That's why we need to do it with the parent-child relationship, because there we route things through the thalamus and store relative orientations and locations in the parent's object reference frame.

We do coordinate transforms well, but we can probably get rid of that question about learning between the agreements. You would have to learn that; you can't just do hypothesis testing between vote agreements, like stapler top pose A and stapler bottom pose B. The votes are very specific rotations, not a relative location to each other. If you want to learn that association, you have to learn it for all possible poses the stapler could be in. If you send both poses to the parent object, we store the relative orientation to the parent object.

We would have to store, for the vote, the relative offset and then transform it, similar to how we ensure they're all agreeing on the rotation. What would be the point of doing that? I think we can move on.

Can I ask my question? This section is called objects orientation, but most questions are about potential masking. Does anybody remember why we were trying to model the break-off object in the first place?

What was the benefit for learning compositional objects, so that we have a stapler top and also a stapler, but we already have a mechanism for learning compositional objects? I guess this can speed things up. If the stapler top truly broke apart, we don't need to explore the entire stapler top to create that model; it will exist because we have observed some kind of behavior. It seems helpful, but not necessary.

With the stapler, a lot of the times we've discussed behaviors, we have the stapler model, and that's the morphology we know. Then suddenly part of the stapler moves. We talked about how it would make sense to mask that out and say it's only part of the stapler that's moving. That's the connection to behavior: how do we use a fixed morphology model we've learned in the past to adapt it to learn a behavior once it starts moving?

When we have learning modules that are sparse and not looking at the entire stapler, we want to know that only the top is moving and not the whole stapler rotating together. But when we have a new example where learning modules are covering the entire morphology, like in your PowerPoint, we automatically know that only this part is moving because we're not getting any behaviors from the bottom part—there's no change in locations.

Just to clarify, any learning module in this diagram is only seeing part of the stapler, right? Yes, any learning module. That's right.

If we were able to gather the locations of these learning modules, I think we could know that by which sensorimotor it is attached to. I'm assuming there's a sensorimotor for every learning module, and a sensorimotor knows its location. We could consolidate which sensors were activated or attending, and all those points together would form an attentional mask. That can then be applied to the morphology model to learn to break off the object.

If I'm following you, it sounds like you're describing a way we might do attentional masking. My question is whether we still need to morph into something else, or if it could be beneficial if we're trying to use a fixed model. If we go with a solution that's more general to any kind of object deformations—not just the case where a big chunk of the object moves together—then the idea of the attentional mask is that we can apply it to that chunk on the stapler and make the same stapler predictions, just rotating the entire stapler model. But if we have total object deformations, like if the stapler is made out of wax and you can bend it, then the attentional mask solution doesn't help much anymore, or you'd have to make very tiny attentional masks.

Maybe if we go with a different solution, we wouldn't need them anymore, or at least they might still be useful in the sense that we could use the model-free attention mask to tell us which parts are moving and use that to inform what sub-component of the object we want to learn a separate model for. Basically, I'm only going to pay attention to this part, so only those learning modules on those parts will get input and naturally learn a new model for this sub-component. But we wouldn't use the attentional masks anymore for making predictions about morphology.

Unless it's more efficient—if the distortion stuff takes more time to learn and model, maybe if you can match existing distortion models to a new morphology, it would be very quick. But if you have to relearn it, it's not quick, like with the new logo behavior. So I guess attentional mask may not always be the criterion for creating a child object. Otherwise, with deforming stuff, you might end up creating infinitely many child objects. It's a good criterion—if something is moving together, that's a good candidate—but maybe it shouldn't be the only requirement.

I have another question. If we had a mug with a logo, and that was the only mug that ever existed, would that be a compositional object or just one object? If all the mugs in the world are just TP mugs, like white TP, would we still make a child object for the logo?

Let's say the logo appears in other places. Maybe not the logo, since it can appear elsewhere, but a completely unique design. This gets into general questions about unsupervised learning. One example is handles—handles on mugs are almost always associated with mugs, but we also have a sense that they're their own thing. Maybe we learn that through affordances. There are complex questions about how to decompose the world. Sometimes you can rely on statistical dissociation—things that appear consistently on their own, separate from other things. Your example was breaking that, but even in cases where that's broken, like handles always appearing on mugs or noses always appearing on faces, we still have a way of thinking of them as objects. It's weird. Some mysteries remain.

We've got seven minutes left. Should I quickly go through the rest of the segmentation stuff so we can say that's done? Sure.

Is there a more general attention mechanism? Could the same mechanisms be used for compositional objects?

The voting ends of agreement mechanism would, in theory, work for static objects, but there are more general concerns around the information required. Model-free signals for no masking would work in many situations, I think. Maybe I'll keep this one gray. Sounds good.

How can object behaviors be used to turn an attentional mask into its own model? I might delete this question; I feel like we already covered it.

We added a question that already existed.

How do we define child objects for continuous substances, like rubber, glue, cloth, or liquid? Do we do so at all? If not, how do we apply our solutions to behavioral modeling?

Maybe later. This might be your proposal. You can just say, "see object distortion models." If we go with a more general object distortion mechanism, we might not need attentional masks to make predictions about morphology.

Do you want me to write that down? Sure, go ahead.

The only thing is, if a behavior is totally novel, it might still be helpful.

You mean behaviors like the exploding logo?

If it's a new behavior-morphology combination, or you don't have a model for a new behavior at all. Because that's a different scenario where we first have to learn the behavior model. But it's one we've been discussing.

In terms of applying behavior to morphology, we already have a model of the behavior and a model of the morphology; we've just never applied them to each other. We've never seen this particular object. That's one question, but it's also a question of how we learn the concept of a stapler opening and closing, and similar behaviors.

I thought we already had the solution for that part before we learned it.

It just takes some repetition, which is why the logo was difficult to learn—we needed to observe it many times to build this new behavior model. We couldn't just take an existing behavior model and apply it, even though we tried for some of the components.

I'm just wondering whether attention is playing a role when that's happening.

It feels like there was definitely some, but maybe it was more model-free or bottom-up. I would say attention plays a role there, but I'm not sure where or if we would use attentional masking.

I'm rereading what you wrote. We wouldn't need attentional masking for making predictions about morphology. I agree with that. It wasn't that we don't need attention.

As I added in brackets at the end, we would still want attention for other reasons.

Then we have these two other things in a new scene. This was something Jeff said that I paraphrased, which could be classified as a feature of attention: in a new scene, attention may be broad at first and then narrowed down. This doesn't necessarily mean a simple circle of attention becoming narrower—EGFP threshold attention regions by movement or spatial frequency changes. These regions can be dynamically made smaller or larger as required, still remaining regular.

It was an interesting point in terms of developing attention in Monty—something to bear in mind.

There was also a discussion about priming. When you have a specific task, like finding object X, you would use top-down attention to bias which models to update and use the input for. We discussed how attention may not be the best term for this; it's more about priming a column for which object to observe. If the primed object doesn't match, it won't try to match other objects. Using Monty terminology, if that primed object isn't recognized, it won't try to consider other hypotheses; it would just conclude the object isn't here.

Maybe say if it doesn't recognize that object, it won't try to recognize other objects, or it will only try to recognize the specific object—essentially being blind to other objects.

I feel like that was actually a lot to cover, even though it was only two of those sections. There's quite a lot of blue.

I found that helpful. I would do that again.