Niels Leadholm: Firstly, apologies to anyone who tried looking at the document last night, and thanks, Rami, for supporting that. I thought just before bed that I should share the document, so I quickly opened my laptop and copy-pasted it, but I was clearly using a high-level learning module, or "column," because when I saw the page, I thought it was the document. But it was a different document I had open.

JHawkins: It was not. Anyway, was it fun to read the different one?

Niels Leadholm: Yes, it's also an interesting one. It's one Vivian put together on 2D sensor modules.

JHawkins: Okay, forget it.

Niels Leadholm: This will look familiar to those of you who saw the presentation just before the retreat. Jeff, I think you caught that as a recording after. I wasn't going to go through it in as much detail, but jump around and focus on some of the more open questions, particularly around metrics, like prediction error.

To orient you, as Scott was saying, the idea with putting this together was to think through how we want to evaluate compositional learning. What would the dataset look like? What would the metrics be? How could we, without Monty needing to be perfect, use some supervision to get a basic version of Monty working and able to do this?

JHawkins: I got a little lost at the beginning. Isn't this one of the projects from the offsite?

Niels Leadholm: Yes, this is to try and bookend that work.

JHawkins: Looking at...

Niels Leadholm: We can discuss what we actually implemented and what is outstanding.

JHawkins: This is just continuing from what was done there.

Niels Leadholm: Exactly.

JHawkins: Okay.

Niels Leadholm: Scott had already implemented a dataset like this. At the retreat, we set up a benchmark that could pass objects like this, and we could look at performance at two different levels. Since the retreat, Vivian has been wrapping up that codebase, and it's very close to being merged into the main repository.

Some things that came up during the retreat are worth thinking more about. Maybe it's about what we actually want at the different levels of the learning modules.

It's intuitive that if we have two columns or learning modules observing something like the TPP mug at the lowest level, it's going to develop a TPP logo, and at the highest level, we want "mug with logo." That's the idea of having a compositional object. One way we ensured this was possible at the retreat was by enforcing that the learning module first learns about the child objects, then we clamp it in an inference phase.

We ensure that one is doing inference while the other continues learning. That gives us the basic setup where one can learn a compositional model. One thing we didn't address at the retreat is how to learn "mug with logo" as a compositional object without relearning all the mug features again. This relates to a conversation we had the other day about how we might deal with this. I think the consensus is that some way of having state might be important, so that part of the learning module tells us, "You are still on the mug, but it's a different type of mug," and helps you predict observations at certain locations without relearning everything.

JHawkins: Something like that seems essential, right?

Niels Leadholm: Yes.

JHawkins: You can have multiple flavors of the mug that share a lot of features, but you want variations of different types. We can't relearn everything. Some kind of state seems essential.

Niels Leadholm: Yes. Another thing is that the way we set this up assumes a simplification. We clamp the learning module to do inference once it's learned the child objects and don't enable further learning. One reason is that for it to pass an ID up to the higher module, it has to recognize what it's seeing, which makes the process quicker and guarantees it's going to try to recognize something.

Viviane Clay: We don't necessarily need to prevent it from learning. Right now, we have to do it because it doesn't switch hypotheses quickly enough. If it has learned a model of a logo and then we show the logo on the mug, it would start adding parts of the mug into the model of the logo. But if it switches quickly enough between logo and mug, I don't see a reason why it couldn't keep updating its models. The main thing is that we only provide the "mug with logo" label to the higher-level one, because we want that one to learn the compositional object.

JHawkins: This is a case where we often talk about a single sensor patch, like a fingertip or looking at the world through a straw. That doesn't work. We know now that's not sufficient for learning behaviors of objects, and it's probably not sufficient here either. If I'm looking at this object through a straw, it takes a long time for the straw module to recognize the logo. You can't do it right away, so we're moving around a lot. But in the real world, we do this almost instantly. We see complex objects that require multiple columns and voting. I think that's what we're talking about here.

Niels Leadholm: Yes, I think that's part of it—having that happen fast enough. I agree, things like voting would help with that.

And then the other thing is the oddity of how, with unsupervised learning, we currently don't have a clear way to prevent the low-level learning module from adding observations to the logo model it has.

Viviane Clay: The problem is if it starts adding features of the mug to its model of the logo.

JHawkins: Oh, I see, we don't want that.

Viviane Clay: The work Rami is doing may help, allowing us to quickly switch between different hypotheses. One idea is to have low-level masking from the sensor module to prevent it from sending features of the mug when it's trying to recognize the logo.

JHawkins: If you recognize something, how do you prevent it from thinking there's more to it?

Niels Leadholm: It's a general unsupervised learning issue. Vivian, you mentioned Rami Singh—do you think that would help? If Monty starts on the logo and moves around, once it reaches the matching state and starts exploring, it will keep adding information. It never rematches or questions whether it's on a different object.

Viviane Clay: We could set it so it doesn't switch into exploratory mode, but it still has enough evidence to send things up the hierarchy.

Niels Leadholm: Isn't that the same as preventing it from learning?

Viviane Clay: No, it can learn about things it has seen during the matching phase.

Niels Leadholm: But if, during the episode, it has seen several different objects, it wouldn't be able to disentangle them. Right now, Monty wouldn't be able to say, "At this point, I had this hypothesis, so I'll add that."

Niels Leadholm: It would add everything to whatever was the last most likely hypothesis. That's something that wouldn't work right now.

JHawkins: Excuse me. I'm sorry.

Niels Leadholm: It's just general improvements.

JHawkins: Think about this particular problem: if I'm walking around looking at things, I'm constantly building compositional models. This is here, that is there, these are relatives—just building up the compositional structure in my scene. I wouldn't add anything to those models unless there's something odd about them. If I recognize a book, I say it's a book, and I'm done. But if there's something odd about the book, my attention would focus on it. Then I'd switch out of building compositional models of my room and focus on that particular thing, trying to figure out what's wrong with it. We have this mode where we're not constantly learning. Until I see something unexpected, as long as things are as expected, I'm not going to add anything to them. But as soon as I see something wrong, I switch and try to figure out what's wrong with the object. There seems to be an attentional shift to learning about an object only when there's an error, which supports the idea of not continually adding features to an object. If I know it's a book, I don't think about it further.

Niels Leadholm: That would make things easier. We've wrestled with how much we should have a discrete shift between learning and inference. If we rely on prediction error and similar mechanisms, it can happen at any point, but it is a shift.

JHawkins: It is a shift. I think that's a reasonable assumption.

Niels Leadholm: The other piece, which we already have with the constrained object models that Vivian implemented, is a sense of impermanence of representations, or the permanence threshold in the HTM synapses. When we add information, right now it's full strength and permanent, but we would rather increment information with observations. Over time, even if you increment a little, for example, there's a mug above a hand above the logo, as long as you see other instances of the logo without a mug, that won't become a strong signal.

JHawkins: Everything that is self-contained, like the logo.

JHawkins: The former method also seems valid and is clearer, where you just disable learning as you're building. We need both, I think.

Niels Leadholm: Otherwise, sometimes we might correctly switch to a learning mode but then add information that turns out not to be correct.

JHawkins: I wouldn't rely on the second mechanism. You can do both, but I don't think we should try to add things to an object just because part of it is obscured. When you are learning something, statistical issues could come into play. I'm still in favor of switching off learning on the child object.

Ramy Mounir: This seems like a fundamental question for me. Are we building these models in Monty or in TBT just enough to make predictions, or are we building the models first and then doing inference? Right now, in Monty, we're learning, building the models, going through these points, and adding all these observations into the model. Later, we use them to do inference. Other theories, like predictive coding, are built on the idea that you only build models that enable you to make predictions, and you only learn enough to make predictions.

JHawkins: I'm not sure I understand the difference, but I don't like the language of the second. We're building a model—prediction is a key component of how we determine if the model is correct, but the goal of the system isn't just to make predictions, like predictive coding. I don't think that's right at all.

Ramy Mounir: Okay, good.

JHawkins: That's an offshoot of what the system does.

Hojae Lee: For one example that we're not just making it for prediction, there was a paper I shared a while ago on whether GPT-5 can do spatial reasoning. It gives you some blocks and a picture of blocks and asks what a block would look like from a top-down view. It doesn't get it right, even though it would be trivial for humans, even babies, to imagine what that top-down view might look like. We're never going to train blocks on top-down views. It would be true for Monty to learn the 3D models of blocks—we could probably even make it now. But I'm thinking more toward goals: if given a random question, like what would this look like from the top, side, or bottom, if Monty has this model, we should be able to answer any question.

JHawkins: Are you saying, Jose, that the goal is to build a model? From the model, we can make predictions, including novel predictions. The goal is to build a model, right?

Hojae Lee: So true.

JHawkins: I agree. It's a good example. The goal is to build a model, not just make predictions. So where were we? What were we talking about?

Niels Leadholm: Okay. That's helpful. It's a bit of a tangent with unsupervised learning, but I think that is a thorny one. It relates to compositional objects, because we cannot keep hiding from the fact that we'll want to learn objects that don't have clear borders and all this kind of stuff.

Viviane Clay: Basically, we can't keep supervising at every level.

Niels Leadholm: Exactly. It's going to get increasingly hard to have any sort of supervision.

JHawkins: So, what—

Niels Leadholm: Yeah, one—

JHawkins: I didn't follow A to B there.

Niels Leadholm: That implies—

JHawkins: So that said, we won't be learning all the time. Is that what you're saying, or something else?

Niels Leadholm: That implies we need to have good ways of learning without knowing exactly when learning is meant to take place, and without always being able to provide labels. Labels are a separate thing, but knowing when to provide supervision or when learning should happen is the issue that sparked this discussion. We want to—

JHawkins: Once—

Niels Leadholm: Constrain when the low-level learning module switches. Right now, we're constraining it because we don't have an intelligent way of saying, "Now you should be learning because you're making prediction errors," or whatever.

JHawkins: I have a general idea of how this works, if I can articulate it. In some sense, let's say we're always learning, and essentially all learning is compositional in some sense. There are features at some location, and that can be a complete object, something complex, or simple things. We're always learning compositional structure, but it seems we'd only be doing it at one level in the hierarchy at a time, or always at the top of the hierarchy, or something like that. If I have a problem, like I was saying earlier—I'm in the room, learning the compositional structure of the room, assuming I recognize all the objects in the room. I don't try to relearn those objects, but if I see an unusual object, I focus on that and learn that object, forgetting about the room. If I see a component of the second object that's unusual, I focus on that. However this is organized in the hierarchy, it seems we're doing compositional structure at one point at any time. It could be at one point in this depth of compositions. We're not doing it all the time, so that doesn't solve the problem we're talking about, but it does say it's only happening at one point, and if I can't do it there, I have to drill down and focus on something else. I keep going down until I recognize something and say, "Now I can build a composition of the things I recognize." Does that make sense?

Niels Leadholm: Yeah, definitely.

Viviane Clay: You can shift your attention through the different levels in the hierarchy, and only one of them can be learning at a time. If it's a higher-level one that's learning, then the one that gives input to it is just doing inference to provide input.

JHawkins: What I don't understand yet is, what if I find something wrong? I'm looking at the room, then I see the book, and the book doesn't look right, so I focus on the book. Then I see something weird on the surface and focus on that. Where is that happening in the hierarchy? Is that all shifted to the book at the top of the hierarchy, like in the entorhinal cortex, or is this learning in V1?

It feels like once your attention shifts, all this learning first occurs in a fast learning module, like the hippocampus. How that's distributed over the hierarchy is not clear to me, but I think the sentiment is correct. I think you expressed it well, Vivian.

Niels Leadholm: That was actually something else I wanted to bring up, which is this kind of slow learning in lower-level learning modules and how that could contribute to stability. When you're learning something totally new for the first time and learning it quickly, that's probably happening at the top of the hierarchy.

JHawkins: I've said before, we have a problem with the Thousand Brains Theory in that we don't really understand how learning occurs across multiple learning modules. It works well for one learning module, but we've encountered numerous instances where, in the behavioral system, we don't have enough understanding of how we can learn things quickly over multiple learning modules. Somehow, the learning is distributed in a way we don't understand.

It's an open problem we have to address, which relates to this. If you want to focus on compositional object testing, I think it's reasonable to assume that the child objects are fixed at this point.

Niels Leadholm: It's a reasonable assumption to assume that the child object—

JHawkins: The child object is not learning. It's just—

Niels Leadholm: Or you have the child learning module?

JHawkins: Yeah, and it would be assumed that voting would have occurred, so we don't have to move the sensor to infer the child object. We want to move our attentional focus from child object to child object, not within the child object to infer it. For example, if I'm touching an object with my finger, I'd have to move the finger to infer the child object before I could assign it to the parent object. I think we can assume that inference is occurring through voting, and it's instantaneous in the child object, which we can't do with one learning module, but we can just fix it at this point.

Niels Leadholm: Yeah.

Can I start? This brings up another interesting point. Under evaluations, one thing I was thinking is that we often talk about how low-level and high-level learning modules can converge on the same object and vote with one another. Our focus is on compositionality, but maybe we should revisit having some metrics that capture this condition, where the child and the learning module converge on the same object.

JHawkins: What kind of metric are you thinking about?

Niels Leadholm: It doesn't need to be complex. We just need to capture that information or look for it.

Viviane Clay: Do we get that right now with the parent-to-child mapping? Consistent child object?

We would get a correct, consistent child object if the parent learning module recognized the mug instead of the mug with logo.

Niels Leadholm: Basically, we would look for a consistent child object in both learning modules, and also the same one, because they could both have consistent child objects and not be converged to the same object.

JHawkins: In the brain, no one would know that they're consistent. They're just two different SDRs, Loading Module 1 and—

Niels Leadholm: Maybe I'll define that, because the way we're using "consistent" here is specific. In terms of evaluating performance, one of the metrics we introduced during the hackathon is the concept of a consistent child object.

If you imagine you have an object, we define, as the human experimenters, a list of potential child objects that could be there—for example, mug and TPP logo. We could also define particular poses, like the logo at a neutral pose or at a specific pose.

A consistent child object is when the output of a learning module is in the set of these potential child objects. Importantly, when the learning module has this output, we don't know exactly where the sensor module is, so we can't know for sure that this is correct. Maybe it was on the handle when it converged on TBP logo, but we can at least say it's consistent with what it could be looking at. If it outputs an entirely different object or an object in an incorrect pose, we would call this confused.

Viviane Clay: This is really just for the experimental loop and is constrained by what information we have in habitat. It's not something we would say is happening in the brain. For that, we're looking at the prediction error.

JHawkins: Let's get into some more theory. What happens when Region 1 and Region 2 are both recognizing the mug? If I assume the same compositional mechanism is in play, the mug would essentially learn that the object—let's say, so Region 2, R2, and R1. R2 is saying there's some feature at this location, and R2's feature is mug. R1's feature is mug. R1 is saying, I have a mug, I'm recognizing the mug, and R2 is saying, there's this feature at this location, and I can learn it. In some sense, a mug recognized in R2 could be considered a feature of the mug in R1. The mechanism seems like it would work. It's basically saying, I recognize something, and I, R1, recognize something that's going to help you, R2, recognize what you're looking at. If I see a mug, that's going to help you know that you should be seeing a mug, too. I don't see any reason why that wouldn't happen or what the problems with it would be.

It's really an issue of consistency. I don't know if we need a special mode that says, now we're looking at a child object, now we're not. It could be whatever R1's recognizing that gets assigned to the locations.

Viviane Clay: Location-by-location basis is what R2's looking at.

JHawkins: And if R1's looking at a mug, that's what's being assigned to the mug. R1's mug is, in some sense, the same as R2's mug. It's a child, of course.

Viviane Clay: That's a good point. Even if the object itself is, by our definition, not a compositional one, Region 2 doesn't know that and would still get input from Region 1. Niels, I was just thinking, in our configs, maybe we should set them up so that when we learn the individual objects, we first train the lower-level learning module on the individual parts, and then after that, we train the higher-level one.

Niels Leadholm: Yeah, right?

Viviane Clay: And compositional objects—during both of those, it can get input from the lower-level one.

Niels Leadholm: Yeah.

Viviane Clay: Instead of learning the individual parts in both modules as individual parts without hierarchical input, and then the compositional one and the higher-level one.

JHawkins: I didn't follow that. I don't know if I need to. It's maybe more of a...

Niels Leadholm: But it's what you just described.

Viviane Clay: Basically, allowing it to also get input from the lower-level one when it sees the individual component.

JHawkins: Another thing that's nice about this is that we've talked in the past—V1 and V2 both might have models of the same objects, but they're at different scales. A question that's never really been addressed is how it switches between those two. When does it get too big for one and too small for the other? There's some overlap where both are recognizing it. It feels like this mechanism, where they act like child and parent all the time, helps make that transition. In some sense, it's more fluid about where the representation of the object is between V1, V2, and V4 as the scale changes.

It just merges these together. The mug becomes merged across these different levels, because a small mug can be a child of the mug. I'm not expressing this well, but I think it unifies the whole scale issue. Maybe I should take that comment back; it's a little bit weird. But I still think the idea has merit. A mug could be a child of a mug.

Niels Leadholm: Yeah, and I think, like you're saying, Vivian, we could already set up the config to have this. You can imagine that happening in this case, where if these features are all disk, and the high-level object is just disk, it's going to be disk that's learned sensory inputs and disk that's learned disk features at all of its locations.

I've added that here because this gets into the strangeness of heterarchy. We can have the low-level learning module learn individual objects first, then train the high-level learning module on those same individual objects. But it'll develop these as compositional ones. For voting across levels of hierarchy, I think it's just a case of having somewhere where, in general, we don't really have much for measuring voting except for post hoc. Maybe that's something to do more of. In this case, it would be just checking that they both get consistent child objects. That metric I was explaining earlier, Jeff, is that these match and have the same consistent child object.

It could be interesting, for example, to see how often the different levels of hierarchy are recognizing the same object.

While we're talking about evaluations, I wanted to revisit the prediction error, because that's probably one of the main things that came out of the retreat—actually implementing that.

The idea was to come up with an unsupervised way of measuring how well our compositional models are doing. The prediction error is basically the inverse of the evidence that's incremented on any given step by these evidence learning modules for the most likely hypothesis. The most likely hypothesis is what the learning module, what the column, thinks it's seeing. If that doesn't have much evidence, or the evidence actually drops on the current step, then that's indicative of a high prediction error.

These are some toy diagrams to show different conditions we might expect. In the baseline example, where we're capable of recognizing the mug and the logo with the learning module, the prediction error follows because the hypothesis—the most likely or correct hypothesis—slowly climbs up until it becomes the most likely hypothesis, let's say around here. Because that hypothesis is correct, it knows where it is on the object and makes low prediction errors. But as soon as it moves to the logo, it's now surprised by that. It wasn't expecting that, so it starts getting high error.

You could have a failure case where the most likely hypothesis that's correct never becomes the most likely hypothesis, resulting in a consistently high prediction error.

That's not that interesting an example. Getting into more compositionality, you can imagine—on the y-axis, we have the stepwise prediction error; the step is on the x-axis.

We start on the mug. There's some rotational symmetry; we know we're on the mug and have some sense of where we are, but there are many possibilities. We have enough of a sense that the most likely hypothesis is basically getting no prediction error. But let's say, because of rotational symmetry of the mug, it thinks it's somewhere on it, but it's actually somewhere else. Then suddenly it goes onto the logo. It's still going to get a high prediction error because the high-level learning module didn't predict the move onto the logo at that exact step.

But then, the hypothesis that addresses this kind of symmetry, or that isn't symmetric and is unique to a location on the logo, eventually wins, and we get low prediction error. At that point, we know accurately where we are on the mug, and we can move on the mug with the logo, and then move back onto the mug, back onto the logo, and maintain a low dictionary.

JHawkins: I'm confused; these are unfamiliar terms for me. If I understand this, why, when I'm—so the learning modules—I'm not sure if this is one learning module we're talking about right now. This is the second one. I would say you can imagine this is the high-level learning module that recognizes compositional structure. Now that it knows it's on the mug, the picture falls because it knows it's on the mug. I know where I am. But if it's already learned the mug with the logo, why is there a prediction error in the next section? Why does it jump back up again?

Niels Leadholm: That's the rotational symmetry. Maybe this example is easier.

JHawkins: Oh, my gosh.

Niels Leadholm: Started with it.

JHawkins: That's what I was expecting.

Niels Leadholm: If it senses the handle first, then it will know exactly where it is, and you're right. Then if it knows the mug with the logo, it'll never get the big jump.

JHawkins: In the first example, it didn't actually know where it was on the mug. It was incorrect.

Niels Leadholm: It was correct within the domain of the mug.

JHawkins: But if I know exactly where I am, then I should be able to predict the logo.

Niels Leadholm: It didn't know exactly where it was.

JHawkins: It was making corrections because of the symmetry of the mug. And so it's happy.

Viviane Clay: The same thing would happen in a normal mug without a logo if you moved to the handle for the first time and then resolved the symmetry. In the second example, we could still get a higher prediction error when we move to a logo, because the higher-level module knows mugs with and without logos. Before it moves to the logo, it doesn't know yet which one it is, so it might think we're just on the featureless mug and predict to see white. When it moves onto the logo, that's when it first gets a high prediction error, but then on the next step, it knows it's actually on the mug with the logo.

Niels Leadholm: At that point, yeah.

JHawkins: I have a cabinet of mugs, and most of them don't have a logo, and the mugs are all facing so I can't see a logo. But one of them has a logo on it. I didn't anticipate that, so I take it off the shelf, turn it, and realize this is the one with the logo. It catches my attention because most of the mugs don't have the logo.

Viviane Clay: The nice thing about this prediction error metric is that it's really simple but powerful. We don't need any labels or supervision, and we can judge Monty's performance based on how well it can predict the next sensory input.

Niels Leadholm: What were you going to say, Ron?

Ramy Mounir: In the scenario where we have enough symmetry evidence, should the prediction error metric be calculated as an average over all of those symmetric poses, or would it still be the MLH? There's nothing really special about the MLH; Monty assumes they're all equal in terms of validity. Should we just average?

Niels Leadholm: Yeah.

Ramy Mounir: Or—

Niels Leadholm: I don't know, my temptation would be that there's still just one hypothesis. The averaging or equivalence is more across the rotations rather than across locations. When you're on a symmetric object, it feels like you still think you're at a location. It's not that you feel like you are at multiple locations at once, but all of those locations or rotations of the object are equivalent.

Ramy Mounir: It probably wouldn't make much of a difference, because only one of them is correct in those symmetric poses, so it would only bring down the prediction error a little bit. If we have 10 symmetric poses or more and only one is correct, the average is not really going to make a difference.

Niels Leadholm: If they're similar, and if we are detecting symmetry, then that's because they're all similar. There might not be much of a difference.

Viviane Clay: The other question could be if we have multiple possible hypotheses that are all above the X percent threshold in Monty terms. It's as if Monty would be making several predictions at once. Like you said, I have a cabinet with mugs, and this mug could have a logo or not. Both are valid within my models. Should there even be a prediction error if it's valid with one of my possible hypotheses?

Niels Leadholm: I guess that's what I'm wondering—is that what we actually do? That's why bistable stimuli are the way they are. We seem to commit to one hypothesis.

Viviane Clay: Once we pass it up the hierarchy, at least that's how we thought of it, we commit to the most likely one, but internally, within layer 4, we can predict several things at once as possible next sensations.

JHawkins: That mechanism came about when we were thinking about how a learning module or a cortical column hasn't figured out a good hypothesis yet. It's still confused. I'm a little bit along with Niels on this one, since it feels like we lock into a good interpretation and stick with it until we know better. We don't try to keep multiple hypotheses going. I want to pick the mug off the shelf. There are 10 mugs up there, and I don't see a logo. I know one of them has a logo, or maybe somewhere in my house there's a bunch with logos. I don't expect it up there, and I don't keep the hypothesis going. I wouldn't normally think about it. The bistable example is closer, and yet the theory about the union of SDRs makes sense when you haven't figured out what you've got yet. You haven't settled on anything. As soon as you settle on something, the union goes away.

Viviane Clay: In this example, we wouldn't have fully settled yet. We would be like, it could be the mug with a logo, or it could be the mug without the logo, based on what I've seen so far. So I would put—

JHawkins: But you have a hypothesis which is consistent with everything, so I see your point.

Viviane Clay: Come to this.

JHawkins: I see your point. I don't know, that's odd.

Niels Leadholm: I don't think we'd want to do the extreme where the prediction error is the minimal prediction error across all hypotheses. I think you were suggesting it's one above a certain threshold?

Viviane Clay: Yeah, or depending on the threshold, it would be the ones above the X percent threshold once we do hypothesis deletion. It'll be all.

JHawkins: Still exist, but I just thought of it. I haven't thought it through much yet. Right now, we're not doing that. I just thought it might be worth considering.

Niels Leadholm: Right now we use the most likely hypothesis to measure prediction error, but we may want to consider other hypotheses as valid as well.

Viviane Clay: Yeah.

JHawkins: Let me go back to the comments you were making a second ago. When we have the mug, but we don't know if it's the mug with the logo or not, at the beginning of this meeting we said that's the difference in state. In some sense, we've locked onto the correct reference frame, and now we're dealing with the difference of state. Even though I don't know if it's the mug with or without the logo, I've determined the correct class of this object. The only variation right now is the state of whether the logo is there or not, which is not the same as being confused about the object. The mug with the logo and the mug without the logo are not two separate objects; they are the same object with variation. It's more like being confused about where on the mark we are, because we haven't sensed the handle yet. But we've locked onto the correct reference frame, so that's done, at least we think we're certain. When we see the logo, we don't switch to a new reference frame, we just switch to a different state of the object.

That said, you could lock on and maintain uncertainty only in the state. I don't know if that helps.

Niels Leadholm: Just to give another example, I'm open-minded about this, but trying to explore perceptually how it feels. If I'm thinking about where I am on this, even if I could be anywhere along the edge, at any given time I only feel like I'm at one location. All of these locations are valid.

JHawkins: You're at one of those.

Niels Leadholm: It doesn't feel like I'm everywhere on it. It's more that this is the kind of thing where there's multiple superpositions; its rotation is the thing where there are multiple consistent possibilities, not my location.

Viviane Clay: Yeah.

Niels Leadholm: Maybe in one place at any time.

Viviane Clay: So what we're talking about right now is a metric. What would be most useful for us to measure and look at? When you show these plots, we're saying, here we expect the prediction error to be high because we haven't resolved the pose yet. We're excusing Monty, saying it's reasonable to have a high prediction error. But if we want to minimize that metric, we should take into account the places where we expect the error to be high.

Niels Leadholm: Maybe one way of framing it is, we could have multiple prediction errors: prediction error of the MLH versus prediction error of top hypotheses, or something. Prediction error of all hypotheses is essentially the inverse, or is like the theoretical limit metric that you made, Rami. Would that be interesting? The theoretical limit doesn't account for location, does it?

Ramy Mounir: No, only rotation.

Niels Leadholm: Or symmetry.

Ramy Mounir: Just a minimum pose error.

Niels Leadholm: There you go.

Ramy Mounir: With them.

Niels Leadholm: Formulating it as a prediction error might be a way of accommodating for that, because that would naturally absorb any causes. I'm going to expand this note: additional versions of prediction error, hypothesis, given threshold.

Yeah, any more on this prediction error stuff, or should I move on?

Ramy Mounir: I was just going to note, are we going to also factor in noise when we're talking about prediction error? If we're looking at a noisy observation, our prediction error is going to be high, but do we want to smooth it, or just keep it as the prediction error of this step?

Niels Leadholm: You mean to make the benchmarks comparable? Dealing with the fact that right now we would inevitably see a higher prediction error on a noisy benchmark?

Ramy Mounir: Not just on a noisy step, but a noisy observation. The prediction is going to shoot up and fluctuate a lot. Should we average over time steps, or is it just expected that if we see a noisy observation, the predictions are going to be high?

Viviane Clay: The metric we report is the average prediction error over the whole episode, so it's already averaged over all of the steps. I don't think we can do anything about noisy observations coming into the learning module.

Niels Leadholm: The only thing we could do is imagine having a plot where it shows the raw values at a detailed level, but then you have a smoothing scale on your plot. If you want to see the smooth result, then it does that.

Ramy Mounir: Makes sense.

Niels Leadholm: I'm not suggesting we need to do this right now, but there are some high-level forms of prediction error we could also use, for example, chamfer distance. This could become more relevant when we look at unsupervised object segmentation. If we want it to recognize that there's a handle, and that the handle is its own object, and where the handle is.

JHawkins: You can imagine, Chance.

Niels Leadholm: This is the metric we used in the DMC paper. You have two point clouds and measure the distance between them. On the left, there's a high Chamfer distance; on the right, a low Chamfer distance.

JHawkins: Got it, thank you.

Niels Leadholm: Or you could use Euclidean distance in image space, or similar metrics. Just something to consider. We talked about this before the retreat. In terms of metrics and how we mediate compositional learning, what we've done so far is add some supervision. We make sure the low-level learning module has learned the child objects, ensure it's in inference mode, and then pass a label to the high-level learning module. There are also improvements to Monty that go beyond just a dataset or benchmark, but I thought it was interesting to discuss them. These include the sensor modules. The question is how we observe the effect we want: the low-level learning module recognizes child objects and passes the ID up, and the high-level learning module recognizes compositional objects. We discussed sensory modules and how the high-level learning module might have a large core sensory input, making it less likely to recognize something like the logo, so it relies on the low-level module to recognize the logo and pass the ID up.

On the other hand, if a low-level learning module has a narrow, fine-grained sensory input, it will struggle to learn big objects and is less likely to learn things like the entire mug.

Viviane Clay: We already have that in our configs—the lower-level module gets higher resolution, more fine-grained input than the higher-level one. Also, the model settings differ in what information is considered redundant. Another parameter I tried a couple of years ago was restricting the size of the models that the low-level modules can learn. A low-level module only represents objects up to a certain size; if the object is larger, it won't be learned there. I don't think we set that up here.

Niels Leadholm: No, and it's interesting to consider what that would mean here. Right now, the low-level module learns a detailed model of the cube, and the high-level module learns a coarser one. When the high-level module is learning the compositional object, it gets the ID output from the low-level one, even when it's on the cube or the mug. If we constrain the size of the low-level models, it might only recognize the logo and not the mug at all.

Then the question is, is that an issue? I guess not, because the high-level module could just learn that this is a variation of the mug, and it might not always get an ID from the low-level module.

Viviane Clay: Yeah.

JHawkins: I've been taking notes because I think there's a whole set of related issues. I'll mention attention as part of it. How do representations occur at different locations in the hierarchy, and how are they constrained? Are we going to physically constrain what it can recognize, or use an intentional mechanism? I feel there's an overarching theory here that we haven't addressed yet. I don't think it's going to be hard, but we haven't fully grasped it. It keeps coming back to where in the hierarchy things are happening. I just want to point out that there are things we're missing that we have to deal with. They seem easy to address, but we haven't done it yet.

Niels Leadholm: I'm curious, because I remember taking notes when you made good points about attention and its role here. You can imagine both modules recognizing the mug, then moving to the logo, and the low-level module narrows its attention to see the detailed feature.

JHawkins: Maybe there's—

Niels Leadholm: —a detailed thing. That would work with voting to constrain where voting happens.

JHawkins: Another point from this conversation is whether the lowest-level learning modules are always inferring something. Maybe not. Maybe inference starts higher up, and there's nothing small to worry about at the moment. That's another aspect of the problem: where inference and learning are occurring.

Again, I don't want anyone to worry, because it feels like we have the basics down and understand how compositional structure is learned. Now we just have to play it out—these are questions about which modules are doing what, how voting comes into play, and whether we're locking things down. These are all related, but hopefully—

Viviane Clay: Oh yeah, go ahead.

JHawkins: I hope these uncertainties don't slow you down in implementing this right now.

Viviane Clay: That's the idea—we have a basic testbed, and now we can iterate, make improvements, find issues, and improve how we're doing things. We have the plumbing in place to pass up the object ID and connect learning modules hierarchically, and to evaluate our progress. In the next months, we'll iterate and improve. In that context, we can use two learning modules and do a bunch of—

JHawkins: Hacky, hard-coded things, knowing we'll solve those later.

Viviane Clay: 

JHawkins: We don't have to worry about how one learning module will do everything. You can just do it now, and we'll get the voting working later and figure out the other things as we go. I'm glad we feel that way. It makes me motivated to work on this right now. Sometimes I take a note and think, I don't want to deal with this, it's annoying. Okay, good.

Niels Leadholm: I think it's a good position we're in now. One thing I thought might be interesting to discuss is policies. In my mind, there's a lot of overlap with attention, since both can segment the world and guide information gathering, but attention could be more all at once.

JHawkins: You're talking about action policies here?

Niels Leadholm: Yes.

JHawkins: Okay.

Niels Leadholm: Attention would be all at once, constraining where voting happens and which learning modules are involved. Policies would determine where we move. You can imagine something similar: as an attentional window narrows, the policy constrains us to move in a smaller location, until we recognize the logo. This is something we've discussed before. That narrowing could be based on both model-based and model-free signals. Although that could help us recognize what the logo or small object is, it wouldn't prevent the high-level learning module from also trying to recognize that small object.

So, other things are definitely going to be important.

The difference in the central modules may imply, as we've discussed before, that attention is different for different levels of the hierarchy. Higher-level learning modules attend to a larger region, while lower-level modules attend to a narrower region.

JHawkins: Once I think about this, I'll throw out an idea. Let's say we have a hierarchy of regions—two, ten, whatever. The top one is always in the mode of learning compositional objects. It never stops, because it's like a fast memory, like the hippocampus. It never stops, so it's never going to sit there and say, "Oh, I recognize the mug." It's always building a new object at the top. It could be the room, it could be anything, but it never stops.

I don't know if that answers your question, Niels, about how to prevent the top-level module from recognizing and stopping. Maybe the top module never stops learning compositions. It'll never be satisfied. It will always say, "I don't even know what that means yet," but it's a way of constraining the problem.

The system will never be satisfied. It will never say, "We're all recognizing the mug, and we're done." If I recognize something, I have to put it in a larger context. The top module is always trying to figure out a bigger context. It never settles. It never infers anything.

Niels Leadholm: In some ways, it feels like working memory or the hippocampus. It's always asking, "What is the situation now?" and never assumes it's experienced it before, because the world is constantly changing.

So there's no point trying to infer it at the highest level.

JHawkins: That's the basic idea. What does that actually mean? It feels like that's how we work in the world. We're constantly building compositional structure at different levels, and it never stops—unless you're asleep or something. I'll look around a familiar room and notice something new, like a different pillow on my bed. If I'm constantly doing that, and assuming that underneath that high-level compositional learning, there are all these structured objects, I just assume they're there. I see them, I recognize them, but if one of them is odd, like I mentioned in the book, I would zoom in and focus on that, and that would become the new compositional structure I'm learning. It's a thought to keep in mind.

Viviane Clay: That makes sense. At the highest level, we're always building a compositional model of the scene around us. There's no need to use it for inference or recognition, because it's just the specific arrangement of things on my table today, but it's still useful to build this temporal model. If I look at the lamp, I know what I'll see when I look back at my laptop, because I've built a temporary model of how everything is arranged on my screen, so I can inform my lower-level modules what to expect next.

JHawkins: If I saw a book and it was odd, I would build a new compositional model of that book at the top level of the hierarchy. That would be my attention. It would be an episodic memory: "I have a book that's in the shape of a trapezoid. I never saw that before. I'll remember that. That was yesterday." It's not something happening in V1; it's happening at a high level. The top level is always building new compositional models until they become so structured that the process moves down in the hierarchy, and I can build new compositional models on top of that. Even low-level objects seem to get learned at the highest level initially and then get transferred down. Almost everything is episodic in the beginning. It's weird. I don't know how that happens, but it feels like that.

Tristan's phone: Sounds a lot like chunking.

JHawkins: Chunking. I forgot what that is.

Tristan's phone: In learning, chunking is when you have to group things together.

JHawkins: Go on.

Tristan's phone: To learn high-level concepts, otherwise you're always stuck in the details.

JHawkins: I guess that's chunking. I don't know if it's a technical term or not, but sure.

Niels Leadholm: Okay, nice. I think that's an interesting idea, just to emphasize.

JHawkins: But we can do it right here. We can do it—learning modules. We can assume that the second learning module is constantly learning compositional structure, and the first learning module is recognizing objects. That's your test structure, I think, and that's consistent with everything we just said. We assume that the first learning module doesn't have to move to infer the object. I assume there's some sort of voting going on there.

Viviane Clay: We don't have that in our current test setup. The lower level one also has to move to recognize the object, because we only have one...

JHawkins: Wolves.

Viviane Clay: But there's no water.

JHawkins: Yeah, I know, my ad. I don't know if that messes up the system. The idea I was proposing is that compositional learning always occurs at one level, the top level of the hierarchy. It assumes that every feature I'm going to put into that compositional high-level object is already recognized instantly. I don't have to tend to it or drill down. If I have to imagine trying to learn computational objects with a finger, it'd be pretty hard. I'd have to recognize one object, and then—think about it with a straw, maybe it's easier. As I'm looking around, I have to recognize something. I'm doing it with the straw, and I say, that's the logo. Would I start by recognizing the mug? I'm not sure how it works. I don't know if it works if I have to spend time moving to and fro the object. It almost feels like I want to do one-shot learning. Here's an object—I'm building up this compositional structure, object location, as opposed to having to move around to figure out what that object is. Now it's at that location. I have to move around and figure out what that object is. I'm not sure that works very well. I don't know, it does work.

Niels Leadholm: That's an interesting point.

JHawkins: From a testbed point of view, we just don't want to get stuck on this issue of moving the sensor to infer the first child object.

Viviane Clay: If you have a logo on a mug, you do move a couple of times to recognize the logo itself first, but maybe while you're trying to recognize the logo, that's what's represented in the higher level, and then the letters are at the lower level?

JHawkins: I don't know. That's a good question. You're right, it's hard not to move your eyes. Let's say I look at a mug, and I look at the logo. There are two situations. One is I don't recognize the logo with one fixation and have to move my eyes to recognize it. The other is I do recognize it with one fixation, yet I'm still moving my eyes. The second one is different. In the second one, you're constantly passing out a logo to the parent object, and the fact that the eyes are moving doesn't really matter. But in the first one, where you don't recognize the logo until you attend to it, it feels...

Niels Leadholm: Rather than a binary difference, it's a bit like with behaviors. A single learning module can learn a repeating behavior in theory, but it's really hard unless it's moving very slowly. It feels similar; you can probably learn a compositional object through a straw, but it's hard because you need to recognize both the low-level object and the high-level object and have that context. The situation where that arises is just harder.

JHawkins: That's a good parallel. The behavioral thing is interesting, because even though in theory you could do it, I think practically it cannot be done. I can't really learn behaviors looking through a straw. It just doesn't seem possible. It requires some sort of group action, multiple learning modules. That may be true here too. Some sort of theoretical limit could work, but maybe practically it couldn't. Yeah.

Viviane Clay: I feel like there needs to be some kind of middle ground, because if we assume there needs to be flash inference of the child object, it gets more complicated when we have, for example, the logo with the band in it. There is no version of the logo with the bend that we can just recognize. We'd have to move to figure out, here it's rotated differently.

JHawkins: If I saw the logo with the bend, it would be like looking at the book and seeing it's an odd book. For a moment, I would forget about everything else and focus on that logo. I might temporarily learn a model of the logo with a bend in it and say, that's a thing. Now I'm going to assign this to another mug. I don't know.

Viviane Clay: If we rely on that mechanism, we lose a lot of the benefits of learning location by location, assigning different orientations, and having the flexibility where the location would be better.

JHawkins: You're right. Okay.

Viviane Clay: Maybe you have to learn the logo as a compositional object, and then...

JHawkins: I don't know.

Viviane Clay: We've been bouncing around a few things. I've taken some notes.

JHawkins: Things that we've talked about: multiple columns may be needed for learning composition. They seem to be needed for learning behaviors, as Neil just said. This is a basic problem of how we learn across multiple learning modules when only one is experiencing an input. That's the same problem. It's about attention in the hierarchy. Where does learning occur in the hierarchy? Maybe compositional learning occurs only at the top. These are all related. I'm just making notes for myself to think about.

Niels Leadholm: Nice, I had a couple more I can touch on.

We were just talking about voting, which is under the heading of ways to improve Monty or push it toward developing the compositional representations we expect. We often discuss voting, but what about competition? Voting is about reaching consensus, but sometimes we might want to push different learning modules away from observing the same thing. Anatomically, most lateral connections actually synapse on interneurons, so inhibitory neurons.

JHawkins: Is that a blanket rule for all different types of neurons?

Niels Leadholm: I thought that was true for most electrical connections. I can double-check that.

JHawkins: I thought in Layer 4, most of the lateral connections were—

Niels Leadholm: No, sorry, lateral connections across columns.

JHawkins: Oh, columns.

Niels Leadholm: The long-range lateral connections.

JHawkins: Oh. Is that true?

Niels Leadholm: I think so.

JHawkins: I'd be surprised by that.

Niels Leadholm: I can look that up real quick. Anyway, I was curious, in the history of voting and similar mechanisms, has it been discussed in terms of mug and logo? Some learning modules see the mug, some see the logo. Is there anything encouraging them to develop different representations rather than trying to have the exact same one?

JHawkins: Mountain did talk about intercolumnar inhibition. Last week, we discussed many columns activating, forming a Mexican hat distribution, so you'd have local excitation and longer-distance inhibition, forcing a distribution of representations. Around the bump of the mini columns, you won't be active. He mentioned the same thing happening in columns. He briefly mentioned it, but I can't remember reading anything else about it. The idea is, if you follow the same idea with mini columns, then in larger cortical columns, they might inhibit each other locally, ensuring the surrounding ones aren't representing the same thing, which enables the ones further away. We don't have a concept like that in Monty today. We assume every learning module can learn everything, but maybe they don't. Maybe we're forcing models to be distributed not across every learning module, but across some subset. Not every learning module would learn a mug, but every fifth or tenth learning module might. That's an appealing idea. One issue is that we assume each learning module gets input from a sensory patch, and the next module gets input from an adjacent patch. If local modules couldn't be active at the same time and are distributed, would they, by chance, be looking at the right learning? Do they have enough overlap in their sensory patches to make that work? Otherwise, you might be blind to some part of the sensory space. It's another high-level concept related to distributed learning.

If I wanted learning in one module to affect others, it wouldn't be the adjacent module, but one further away. We've never really addressed this issue. I'm not even sure it's true.

Niels Leadholm: We don't need to go down that path. In this case, I was thinking about it across the hierarchy. Sometimes we want to vote across the hierarchy, but maybe we also want—

JHawkins: Voting up and down.

Niels Leadholm: The hierarchy.

JHawkins: Okay.

Niels Leadholm: Yeah.

JHawkins: When do we vote up and down the hierarchy?

Niels Leadholm: I thought that was one of the main things.

JHawkins: It could be. Earlier, I mentioned that two hierarchical regions could be observing the same object, with one as the parent and one as the child. That could be the way they vote, the way they reach consensus, as opposed to the Layer 3 voting mechanism we've discussed. There could be voting in another way.

Niels Leadholm: That fits better with the neuroanatomy, I think.

JHawkins: I'm right.

Niels Leadholm: They find it hard to—

Viviane Clay: There isn't a lot of evidence about that. It's between her patients.

JHawkins: Now that we mention this, I proposed the idea because it seemed logical that when two regions are observing and inferring the same object, they should have a way of collaborating to reach a consensus. In a sense, that's voting, but the mechanism could be compositional and hierarchical. That would work, too.

Niels Leadholm: That would have the benefit of being more asymmetric.

JHawkins: It fits the biology better, as you pointed out, and fits our mechanism better. You could call it voting, but not the way we've talked about before. It's a way of two regions assisting each other in reaching a consensus.

So Region 1 thinks, "I might be on a mug," and Region 2 says, "I might be on a mug," and Region 2 says, "Region 1 is telling me that my child object, the mug, helps me infer." The region below is providing information that helps infer "mug."

That's an interesting idea.

Ramy Mounir: Do we also need that for shifting the hierarchy up and down, or shifting two levels of hierarchy? For example, when the higher level is looking at a table with a mug on it, the higher level is looking at the table, then it needs to force the lower level to look at the mug. As soon as the higher level shifts focus to the mug, it needs the lower level to look at the handle.

JHawkins: But we're saying it doesn't always do that, Rami, right? Both of them could be looking at mug and mug. That was the scenario we just talked about.

Ramy Mounir: But would that be—

JHawkins: I'm not sure.

Ramy Mounir: Official object?

JHawkins: I don't know.

Niels Leadholm: Yeah, you're saying, Rami, basically we'd be capturing both. They can agree with each other when there's no specific information. But when there is a specific thing, like a handle, then the high-level one can tell the low-level one to predict that.

Ramy Mounir: Yeah, I'm saying that we know both models are in both higher-level and lower-level objects—the cup is in both—but when we're dealing with compositional objects, we probably don't want both to be representing the same thing. We want to prevent that, so we want the higher level to force the lower level to look at the child object if it is looking.

JHawkins: Sometimes you do, but I can come up with examples where you don't. Think about recognizing printed words as you're reading. I can read very small fonts, I can read large fonts. If I'm reading along and I recognize words, it's pretty well documented that we don't recognize all the letters. In fact, you can switch the letters in the middle of a word, and often you just don't even see it. That's an example of a hierarchical, compositional structure where the brain is not actually checking that the details of the composition are correct. It's saying, good enough, that's the word, it looks about the right shape, right size, and it's got the right curvatures, so in some sense, we end up recognizing the word as its own object.

As you get older, like me, you start forgetting exactly how to spell the letters in between. Was that one L or two L's? I can't remember. But I still can read, no problem. I just can't remember exactly how to spell some words that I used to know how to spell. So I'm not disagreeing, I'm just saying there seem to be some cases where we just accept that the overall word is good enough, and we recognize it, and we don't require that any lower level is paying attention to the details. Otherwise, if you switch the letters in the word, I should notice that they're wrong.

It's a weak example, but just on the front.

It's a good question, Rob, so I don't know.

It seems like we wouldn't want to force the system to try to attend to all the hierarchical details that we know exist in the world.

Yeah, I guess maybe.

Niels Leadholm: Yeah, and in the case you were bringing up, Romi, I guess the focus is on learning. I don't know if this is what you were suggesting, but one way might be if the high-level learning module is struggling to predict something, it can ask the low-level learning module to try and learn that better—basically just some sort of mechanism to push apart their representations.

Ramy Mounir: I was assuming more that the compositional structure is already learned, and as soon as one level starts inferring something at a different level, it needs to force the other level to change, because we're shifting across levels. But it could have some ideas also for learning, forcing learning at different levels.

Niels Leadholm: Yeah.

JHawkins: This goes back to that comment I made earlier, this really confusing point for me. Sometimes I feel like learning has to always occur at the top of the hierarchy, and that's where it intensifies. That doesn't explain, then, when you shift things around in the middle of the hierarchy—you're basically shifting what's up at the top. Yet, at the same time, we have to learn in V1 and V2. I don't know. I have to think about this one.

Niels Leadholm: Isn't it we just dream, and then everything gets transferred to cortex?

JHawkins: Maybe.

Niels Leadholm: Deliberately.

JHawkins: Again, nothing gets transferred. You don't transfer—at least I don't think so. But dream can replay things and cause things to be learned lower down. That's interesting, bringing that back into the picture. I usually pay no attention to that sleep stuff, but you're right. That could be a solution to this problem.

Niels Leadholm: I think that's at least one theory for dreaming, that it's a random assortment of perception to enable learning.

JHawkins: They've shown that dreaming is essential for consolidating memory.

Niels Leadholm: While we're on this topic, I like the idea of all of the learning modules learning in parallel, but it just being really slow at the lowest level. In practice, you don't notice they're learning until months have gone by, and now they have this representation, whereas in an instant, the highest level can just learn a new representation.

JHawkins: I was thinking about the case where he couldn't learn anything new, but he was able to learn a few things.

I forget what they were, but they were things he had been exposed to over and over again, and he didn't think he knew these things.

They'd give him a task, and he would say, I don't know how to do that task, I can't do that task. Then he would do it and realize, somehow I did it.

Niels Leadholm: I remember looking this up, and one of the interesting examples was he could draw a topological map of his house. Even though it was many years after his injury or the surgery, after he purchased the house, he just kept moving around the house, walking around, and eventually he must have built a model of how it was arranged. Some people would argue he had some preserved hippocampus, or something like that, but that was at least one example of where he learned a structured representation through many instances of exposure.

JHawkins: Repetition, right? Maybe normally it requires a hippocampus and sleep, and so maybe it took much longer for him to do that.

Niels Leadholm: Yeah.

JHawkins: That'd be—

Scott Knudstrup: There was something about his ability to learn certain skills, like drawing the reflection of half an image on the right side. I think they said he was able to acquire that skill.

Weeks or months, which is distinct from episodic memory, but it still seems like some kind of spatial base model or skill.

Niels Leadholm: I thought it was just a motor skill, so that could be subcortical, but it's a fair point that it involves a spatial element of reflection. I don't know.

JHawkins: Obviously, neurons learn through repetition and association, so we expect that to happen. The mechanisms by which different parts of the cortex learn, when they learn, when the hippocampus is learning, and how they interact, that's still a bit of a mystery. It shouldn't be a surprise that learning happens, because neural tissue will learn if you give it enough exposures.

But that's the normal way we rely on it. Maybe most of the time we need the hippocampus, and maybe we need sleep with the hippocampus, or something like that.

I don't know. We're not going to solve this today. Let's stick to the topic and see how we're doing on our task for today, which is...

Niels Leadholm: I just had one last small thing I thought would be interesting to bring up, which is about OmniGlot.

Just to rewind a bit, when we were selecting which dataset to use for this task, for this benchmark, we discussed a few different ones. One was the object with logos, which we ended up going with. Another was OmniGlot, which is a dataset of alphabetical characters from many different alphabets. It's a small dataset, as machine learning goes, with multiple examples of each letter drawn by a person, usually not a native speaker of that language.

It's an interesting dataset because it's definitely compositional—you have all these strokes and how they compose the letters. It's small, so it's really hard for traditional machine learning and deep learning methods to work with. Vivian had already implemented a data loader for us to work with it. The main reason we didn't use it for this retreat was because we realized we'd still have to implement a new part of the data loader to pass the individual strokes the way we wanted to, and learn on just those individual strokes.

JHawkins: Why is that the assumption? Why can't we use these as just visual objects?

Viviane Clay: We already tested just learning the characters in general. Marty did well on recognizing the same version of the character, but didn't do well on generalizing to different drawings of the same character.

JHawkins: Yeah.

Viviane Clay: If you only look at the pixel level, there's too much variation between them. But if you can learn them on the stroke level, like the H is two vertical strokes and a horizontal one in relative arrangements, then the thought was Monty should be able to do it. This was the first dataset where we realized we needed compositionality and hierarchy.

JHawkins: Yeah.

Viviane Clay: The dataset already includes stroke information, so we give it each stroke individually, and then it can learn the arrangement.

JHawkins: I remember thinking about this when I first saw it in the write-up before the retreat. I realized that I would personally imagine how I would draw the letters, not just recognize them as images. Even though I didn't know anything about these, I would tease them apart by imagining the strokes. When I tried looking at Chinese glyphs, I had to imagine the strokes to recognize them. That's how I would try to recognize them, so I agree it brings in the motor component.

Niels Leadholm: I don't know if you remember that from the last time we talked about it, but one of the cool things about the data is they've actually recorded the motor sequence as well.

JHawkins: You can see that in the colored images here, right?

Niels Leadholm: The order in which they do it, and also where the stroke starts and ends. They have each pixel as a function of time.

JHawkins: I know.

Niels Leadholm: There are a lot of nice features about this dataset, and I think we'll return to it at some point. I thought it was worth talking about some of the thornier aspects, like how we would deal with the low-level strokes.

In particular, there are a few issues. One is that, because the people drawing aren't native speakers of the languages, they don't draw them in a particularly normal way. For example, B is sometimes drawn as a straight line with a semicircle halfway up instead of at the bottom. There are other odd examples, like drawing an English letter as a single stroke. Even just this K and this G look pretty weird. They may have been using a trackpad.

Concretely, the order in which the strokes are laid down is different, and that affects, according to OmniGlot, what the label is for each stroke. For example, green would be the first stroke, but in different examples, different strokes are green.

Viviane Clay: Even if we use that as a label, it's problematic. For example, the H—the two vertical bars are basically the same thing. We don't give them different labels.

Niels Leadholm: Exactly. That's another issue. Not only are the vertical bars the same, but what about a vertical bar that's rotated? Is that a different object?

Viviane Clay: I don't know. I think we would have to do unsupervised learning at the lowest level and have Monty figure out what unique strokes are.

Niels Leadholm: Yeah.

JHawkins: But you don't want to use that temporal information. It's funny, I did a lot of this when I was working on the hands-up computing stuff, and it makes it so much easier if you know the order in which things are drawn. But when you're reading it, you don't have that information. When I look at these things, even if I didn't know the order in which the strokes are drawn, I would tease apart the different strokes. In this case, there's a cross, a down stroke that goes to the right, then the cross, and then a loopy one. I would break it down into those components on my own, without any additional information. It's interesting—how would I do that? I guess there's some assumption that lines are drawn in continuous flows, so I can see where lines start and end. I would just break this character into three components. The order in which they're drawn, or the end you started, shouldn't really matter. That's cheating if you know that information. Visually, I could just piece apart this thing and say, this is a character made of three strokes. The strokes are roughly these shapes. It seems like I would make that a compositional object of three child objects, which are crudely written, but still three child objects that make up this thing.

Viviane Clay: That's the general idea we were thinking of, but the low-level question would be, when you see an "H," do you, at the lower level, say that's three straight lines at different orientations and locations? Or do you say—

JHawkins: I think—

Viviane Clay: This is stroke two, this is stroke three.

JHawkins: I would think it's three straight lines of different orientations. That's the way to do it.

Viviane Clay: So in that case, we either have to create a new labeled dataset of the basic stroke types, like curves and straight lines, and train the lowest level on that, or we have to do unsupervised learning where Monty has to figure out that those are two straight lines at different orientations.

JHawkins: It's funny because I come in with some prior knowledge about drawing lines. When I look at those things, there's a prior knowledge that the pens don't change direction too much.

Viviane Clay: Yeah, your lower-level learning module is already trained.

JHawkins: But it's interesting, how did I learn that? I learned that through mode or behavior, not just visually. I looked at that and said, where did the pen go? It went around like this, and around like this. I don't look at it and go—

Niels Leadholm: When we talked about how you recognize stuff based on affordance, you mentally imagine yourself sitting on something. It's almost like you mentally imagine yourself writing in some of these things.

JHawkins: Yeah, isn't it? Let's go back to that one particular character you had there. Now that I'm thinking about it, there are three strokes, right? Two of them I recognize immediately. I know those strokes. I don't have to train on them. This is the one that goes down and then across. In fact, I might sometimes look at it and say, that's just a T. I have a T like that, so can I maximize just two strokes as one thing? Or I could recognize those as two—a horizontal stroke and a hooked stroke—which I already know. The other one is unfamiliar to me, and I had to mentally trace it out to see what it is.

Niels Leadholm: I'm guessing you started here every time?

JHawkins: No, I actually started on the other end. Surprisingly, I started at the end that was the most visible. That first character, the most clearly marked endpoint is the one on the bottom.

Niels Leadholm: Are you lefty?

JHawkins: Standard. No, I'm right-handed, but the point is, I didn't ask myself how I would draw it.

Niels Leadholm: Okay.

JHawkins: I had to trace it out mentally, and one end of that line is clearly marked. It's the one that's all by itself on this particular image, the upper left-hand corner. The free end is the one that's on the bottom. The character below that is similar. The one in the first row, second from the left, that's not the case. If you took away the color, it almost looks like it's one stroke that goes down, around, and up again. If I just saw that, I would assume it was two strokes in that character. Only after looking at several of these did I say, oh, it's three. What I'm trying to do is segment out the different strokes. Then I would imagine how I would draw it, or figure out some kind of description for it. It's an interesting one, because that loopy thing—there's nothing like that in printed English letters that I can think of.

Hojae Lee: So rotating G. Yeah, sideways line, rotator G.

JHawkins: Yeah, but I didn't see it that way, because it's sideways. And I don't draw G that way anyway. I draw G a different way. I don't know, I'm just—mentally, if I take that first, I saw three strokes in this dataset. Two were familiar to me, and a third one wasn't. The third one was the one I had to trace. The first one, I didn't really have to trace, because I already recognized them. I have to spend time trying to learn that funny little pattern of the third stroke. I'm looking at it over and over again, asking how I would work it out.

Niels Leadholm: Yeah.

JHawkins: These are observations. These are complications of using this dataset.

Niels Leadholm: But I think it would be a nice long-term one to revisit, because with all the action stuff, it would fit nicely with temporal aspects, adding in time, and it would also fit nicely with eventually having action outputs where we could get Monty to draw new examples of these letters and things like that.

JHawkins: Yeah, but I don't think it's a good one right now if we're just trying to get accomplished or something.

Niels Leadholm: Yeah.

Hojae Lee: This reminds me, I think there are some Chinese characters where a character is made up of other characters that can stand on their own, but when written smaller in a particular square area with other elements, it changes meaning—it's a different character or word.

Niels Leadholm: That sounds right.

JHawkins: Do you read Hongo?

Hojae Lee: I can read Korean.

JHawkins: Isn't that Hongo? Isn't that Korean?

Hojae Lee: Yes, that's Hangul.

JHawkins: But that's not true.

Hojae Lee: Chinese.

JHawkins: I was going to ask, do they have a similar thing in Korean?

Hojae Lee: Yes, you can add other characters in the same kind of way. If you're writing a single character word in a box, you can add multiple elements, and that becomes a different word. If you take one character out, the same components are there, but there might be differences.

Niels Leadholm: But you wouldn't have a whole character within a character in Hongo, would you?

Hojae Lee: No. They're usually arranged side by side, but they take up the same kind of monospace.

JHawkins: I was just wondering, are some of the subsets words themselves? Do they do the same thing?

Hojae Lee: No, they're more like vowels and consonants.

JHawkins: Arranged in a box.

Hojae Lee: Yes, arranged in a box.

Niels Leadholm: Doesn't that affect the language? You always need three or four things in a box, which means you almost always finish with a consonant. In English, a word might just end with a vowel, but in some languages, you can't have that because the box isn't complete.

JHawkins: Interesting. Tristan's phone: We don't have to go too far out of our alphabet. Any accented language, right? An A with an apostrophe on top contains an A.

Hojae Lee: Contains an entire character of A.

Tristan's phone: In some languages, like Polish, you have O, and if you put an accent on top, it's U—a completely different sound. Even in English, I is like an L with a dot on top. We don't have to go too far to see this.

JHawkins: Cool.

Tristan's phone: Positional characters.

JHawkins: Yeah.

Niels Leadholm: Letters with accents are good examples of these state changes. You don't want to relearn the letter A or the mug when you're learning the TPB mug. It's related, but different.

JHawkins: In many languages, you have A's with different accents, but they're all A's. You type the A and then add the accent.

Ramy Mounir: In Arabic, they have dots. The same letter with two or three dots on top or below becomes a completely different letter.

JHawkins: Have you typed that on a keyboard? Do you type the letter and then add the dots?

Hojae Lee: I think if you...

Ramy Mounir: It's just a different character.

Hojae Lee: Swish.

Ramy Mounir: That's it.

Hojae Lee: Okay.

Ramy Mounir: Hate the devs.

JHawkins: I missed all that.

Hojae Lee: Oh, sorry, go ahead.

Ramy Mounir: It's just a completely different letter.

JHawkins: Interesting. In French, I think you type the letter and then add the accent, but I wasn't using a French keyboard.

Viviane Clay: In German, you have letters with dots, and the German keyboard has extra keys for those letters. In those cases, I think of them as different letters. In Greek, the accent just indicates which part of the word has the emphasis, affecting pronunciation. I think of the accent as a modifier, not a different letter. It's still an A, just with a modifier for pronunciation. In German, the A with dots is a different letter.

Niels Leadholm: I wonder how much is due to familiarity. In Danish, the O with the slash is a totally different letter to me. In French, which I don't speak well, I see it as still an A or E with an accent. Maybe a native French speaker would see it as a different letter.

JHawkins: I was wondering about that with Vivian, since German is your native language. I don't know how good your Greek is.

Viviane Clay: Not sure you can say that, trying to learn, but yes.

JHawkins: So, Celeste, Niels was...

Viviane Clay: Maybe it's familiarity, but it also seems like the letters are pronounced the same way, just with stronger emphasis on that syllable. The accent on an A or E has the same effect on all the letters. In German, letters with dots get different pronunciations.

Niels Leadholm: If it's similar, it's always a different pronunciation.

Viviane Clay: Yes.

Hojae Lee: Does that change the meaning of the word? For example, if you have ABC, and you put an accent to emphasize a syllable, does the pronunciation change the meaning?

Viviane Clay: In Greek, there are words that are exactly the same, with two A's, and depending on which A has the emphasis, it means something different.

Hojae Lee: Okay.

Viviane Clay: We're getting far afield here.

Hojae Lee: Yeah.

Niels Leadholm: That was the last thing I wanted to mention.

JHawkins: I think the Omniglot one is still problematic.

Niels Leadholm: Maybe we should have another discussion about it before tackling it.

Scott Knudstrup: Yeah.

JHawkins: It seems things would improve once we have the whole system working with sensorimotor behaviors. Now, it treats the system the right way, but there's implicit knowledge about how the strokes are drawn. I rely on knowledge about how strokes are drawn.

To tease apart those different strokes, to know that's just one stroke and that's another, it's not just a bit pattern. If it were just a bit pattern, I'd be lost.

Viviane Clay: What I wrote down as takeaways for the shorter term is, for the benchmark test we have now, see about making a config where we only train the lower-level learning module first. Then, the high-level learning module, even when it learns individual objects like just the cup, still gets input from the lower-level module about the child object, so it just associates Merck on Merck. Maybe look into voting earlier than planned, seeing if we can improve things by having several lower-level learning modules that can infer the child object faster.

Niels Leadholm: Yeah.

JHawkins: Or just hard-code that for now.

Niels Leadholm: I'm sorry.

JHawkins: You could just hard-code that to start.

Viviane Clay: That might be harder, because we don't really know what it's looking at. We don't have an easy way to tell whether it's looking at the logo or the mug. We can do some hacky things—if it looks at certain colors, it's the logo, and if it's looking at other colors, it's the mug.

JHawkins: Don't trust it.

Niels Leadholm: It could be interesting to add in the voting and see how it does. Also, maybe adding other forms of prediction error, like breaking down prediction error into more granular ones, could be interesting as well.

Viviane Clay: I was also thinking there might be some additional metrics, like after a high prediction error, how fast does it go down, or weighing prediction error towards the end of the episode higher than at the beginning.

Niels Leadholm: Yeah.

Viviane Clay: One other thing, not immediate but maybe to keep in mind, is some way to only learn when things are unexpected.

Niels Leadholm: Cool.