Niels Leadholm: and Yeah, firstly, apologies for anyone who tried looking at the document last night, and thanks, Rami, for supporting that. I, Because I thought just before bed, oh, I should share the document, and so just quickly opened my laptop, and then copy-paste it, but I... I was clearly using a high-level learning module, or quote-unquote column, because when I saw the page, I was like, yeah, this is the document. But then, it was... it was a different document I had open.

JHawkins: It was not. Anyways... Is it fun to read the different one?

Niels Leadholm: Yeah, it's also an interesting one. It's one Vivian put together on 2D sensor modules, but.

JHawkins: Okay, forget it, alright.

Niels Leadholm: Yeah.

Cool, and this will look familiar to those of you who saw the presentation just before the retreat, and I think, Jeff, you caught that as a recording after. So I wasn't going to go through it in as much detail. I was going to jump around a bit and kind of focus on either some of the kind of more open question type things, or, Yeah, and particularly, some of the things around metrics and stuff like that, which, come up... yeah, down here, things with prediction error.

But maybe just to orient you, like Scott was saying, the idea was with this... putting this together was just the exercise of, thinking through a bit more, how do we want to evaluate, compositional learning? What would the data set look like? What would the metrics for that look like? And how... how would we, without Monty needing to be perfect and have all these great things, how could we, for example, use some amount of supervision to just get a basic version of Monty working and able to do this?

And

JHawkins: I got a little bit lost at the beginning of this. Isn't this what we... one of the projects at the, offsite was?

Niels Leadholm: Yeah, and so this is to try and bookend that work, is just

JHawkins: looking at...

Niels Leadholm: Yeah, I guess we can discuss a bit what we actually did implement, and then what is outstanding, and.

JHawkins: This is just continuing on from what was done there.

Niels Leadholm: Exactly, yeah.

JHawkins: Okay, alright.

Niels Leadholm: Yeah, and like you say, Jeff, yeah, Scott had already implemented a dataset, which looked a bit like this, and At the retreat, we set up a benchmark that could pass objects like this, and we could look at performance at the two different levels. And then, since the retreat, Vivian's been wrapping up that codebase, and it's very close to being merged into The, kind of main repository.

But, yeah, so some of the kind of things that came up During the retreat, in which... It's worth, thinking a bit more about. Maybe it's just, What we actually want at the different levels of the learning modules.

it's intuitive that if we have two columns or two learning modules that are observing something like the TPP mug at the lowest level, it's going to develop a TPP logo, and then, sorry, at the highest level. we want, mug with logo, that's the whole idea of having a compositional, object. And, Yeah, one way we could... we did... ensure that this was possible, At the retreat was by... Enforcing that this learning module first learns about these child objects. And then we clamp it in an inference phase.

and then ensure that this one's doing inference while this one continues to do learning. And that gives us the kind of basic setup that, This one can learn, a compositional model, But one thing we didn't address at the retreat is how... there's a couple things, but one thing we didn't address is how do we learn mug with logo, like a compositional object, without relearning all of the mug features, all over again? And so this relates to a conversation we had the other day. Which was, how we might deal with this, and this is... where I think, and maybe, Jeff, I'm curious if you disagree, but I think the consensus at the moment is that some way of having state might be important for this, so that we have some part of the learning module is telling us, okay, yeah, you are still on the mug, but it's a different type of mug And I'm gonna help you learn to predict Observations at certain locations without you needing to relearn the whole thing.

JHawkins: Something like that seems essential, right?

Niels Leadholm: Yeah.

JHawkins: you're gonna have... You can have multiple flavors of the mug. That all share a lot of features, and yet you want to have, variations on them. of different types. And so they're just... and we can't relearn everything, Some kind of state seems essential.

Niels Leadholm: Yeah. Yeah, and then I guess one other thing which we The way we set this up assumes is... is... Always a simplification. is we've... is what I was saying about how we clamp this, learning module To do inference, once it's learned the child objects. And we don't enable it to do further learning. And one reason we did that was, because in order for it to pass an ID up. to this learning module, it has to recognize what it's seeing, so that... that just makes that process a bit quicker. Or as in, guarantees that it's just going to try and recognize something But. No, there's.

Viviane Clay: We don't necessarily need to... not have it learn. I think, right now, we have to do it, because it doesn't switch hypotheses quick enough. it would... if it has learned a model of a logo, and then we show the logo on the mug, it would start adding parts of the mug into the model of the logo. But if it does switch quick enough between logo and mug. I don't see a reason why we couldn't have it keep updating its models. the main thing is just that we only provide the mug with logo label to the higher level one, because we want that one to learn the compositional object.

JHawkins: I think this is a case where, we often talk about a single sensor patch, like a tip of a finger, or, looking at the world through a straw. And, that doesn't work. We know now that's not going to be sufficient for, learning behaviors of objects, and it's probably not sufficient in a situation like this, too, because I think the point you're pointing out is if I'm looking at this object through a straw. I have to... it takes a long time for the straw module, the one on the left, to recognize that's the logo, right? You can't do it right away, so we're moving around a bunch. But it seems like when we're out in the real world, we do this almost instantly, right? We go bing, bing, we see these complex objects which require multiple columns and voting. I think that's what we're talking about here, right?

Niels Leadholm: Yeah, I guess it's a couple things. I think that's part of it, is... is, yeah, that happening. fast enough. And yeah, I agree, things like voting would help with that.

And then the other thing is, it's more just the kind of weirdness of how, with unsupervised learning, right now, we don't... I think this is yeah, what you're saying, Vivian, we don't have a clear way to prevent the low-level learning module from just starting to add observations to the logo model it has.

Viviane Clay: Yeah, I think...

JHawkins: Is that a problem? Is that a problem? Because as long as it's passing up the logo ID, To the second module, it doesn't matter if it's learning?

Viviane Clay: the problem is if it starts adding, features of the mug to its model of the logo.

JHawkins: Oh. Boom. Oh, I see, we don't want that.

Viviane Clay: Yeah.

JHawkins: Is that a general problem? Have we dealt with that?

Viviane Clay: I think it'll be getting better with the work that Rami is doing, where we can quickly switch between different hypotheses, and then, potentially, one thing we talked about as well is to have some kind of low-level masking from the sensor module that kind of prevents it from sending Features on the mug when it's trying to recognize the logo. Yeah. I think both up a lot.

JHawkins: I guess it's a general issue of, hey, if you recognize something. How do you prevent it from thinking there's more to it?

Niels Leadholm: Yeah, I think it's just a general unsupervised, learning issue. I'm curious, yeah, just while we're talking about this, yeah, Vivian, you mentioned about Rami Singh. Do you think that would already help? Because... right now... let's say Monty starts on the logo, it's moving around, if it If it reaches the matching state, And then it starts exploring. It's just gonna keep adding information. Wouldn't it? It never kind of rematches or questions whether it's on a different object.

Viviane Clay: Yeah, we could just set it so it doesn't reach... it doesn't switch into exploratory mode, but it still has enough evidence to send up things through the hierarchy.

Niels Leadholm: Isn't that the same as preventing it from learning?

Viviane Clay: No, it couldn't learn about... It can learn about things that it has seen during the matching phase.

Niels Leadholm: And learn about things that's....

Viviane Clay: But, yeah, I guess you mean if, during the episode it has seen several different objects, it wouldn't be able to disentangle them? it would... yeah, right now Monty wouldn't be able to say, at this point, I had this hypothesis, so I'm gonna add that to.

Niels Leadholm: Yeah, it would add all of it.

Viviane Clay: Yeah, it would add everything to whatever was the last most likely hypothesis. Yeah, so that's... that's something that wouldn't work right now.

Niels Leadholm: Yeah, but it...

JHawkins: Excuse me.

I'm sorry.

Niels Leadholm: Yeah, but I guess it's just, yeah, general... Improvements in.

JHawkins: It does, just think about this particular problem.

that if I imagine I'm just walking around looking at things, and I'm constantly building compositional models as I just look at things. this is here, this is there, this is, these are relatives... just building up this compositional structure in my scene.

that I don't really, I wouldn't add anything to any of those models, oh, there's a book on my... I can see a book sitting on the window seat next to me, and there's a pillow. I wouldn't add anything, unless there's something odd about them. it's if I recognize a book, I say it's a book, I'm done. But if there's something odd about the book, then my attention would be focused on it. And then I would... I would switch out of building compositional models of the... of my room, but I'd be focusing on that particular thing, the book, trying to figure out what's wrong with it. So it does feel like we have this sort of mode where we're... we're not really constantly learning. Until I see something unexpected, And that's, that's the general rule, would be, like, as long as things are as expected, I'm not going to add anything to them, I'm not learning anything, I don't try to... I don't try to add anything to them, but as soon as something I... and then I'd switch, I see something wrong. Then I switch, and then I'm no longer learning the larger compositional structure, I'm now trying to re-figure out what's wrong with the book. I'm just supporting the idea that There seems to be this sort of attentional shift to learning something about an object that we don't do all the time. That we only do when there's an error. Which would support the idea of, Not continually adding features to an object, obviously trying to... good enough, I know that, it's a book. Don't think about any.

Niels Leadholm: Yeah, and it would make things a lot easier, because I think this is something we've wrestled with, is, like, how much should we have a discrete Sort of shift between learning an inference.

But, I think, like you say, if we rely on sort of prediction error and things like that. And it...

JHawkins: So that way.

Niels Leadholm: It can happen at any point, but it is a shift.

JHawkins: It is a shift. I think... I think that's a reasonable assumption.

Niels Leadholm: And then the... the then other piece, which... we already have with the... the constrained object models that Vivian implemented is the, is A kind of... a sense of impermanence of representations, or the permanence threshold in the HTM synapses. But that, like, when we add information, right now it's, it's just, it's... Full strength, and it's permanent. But that we would rather increment information with observations. And that over time. That would mean that, even if you incremented a little bit, that, oh, there's a mug above a hand, above the logo. As long as you see other instances of the logo where there isn't a mug. That isn't gonna become, a powerful signal versus...

JHawkins: Just,

Niels Leadholm: Everything that is self-contained, like the logo.

JHawkins: But I think the former method seems also valid, and it's more clear, where you just disable learning less... less, as you're... as you're building... Yeah, we need both, I think.

Niels Leadholm: No, because it...

JHawkins: like I said...

Niels Leadholm: complementary, because otherwise, sometimes we might correctly switch to a learning mode. But then... or, switch to a learning mode, but then late... kind of add some information that... Turns out not.

JHawkins: Yeah, I just... but I think... I think... but still, it wouldn't... I wouldn't rely on the second mechanism. I think the first mechanism is... you can do both, but I don't think we should be trying to add things to my... if I look over and I see the book on the... on my window seat, I shouldn't be trying to add things to it because part of the book is obscured by a, by a... poster. it's... it seems it seems but when you are learning something, then yes, then your statistical... Issues could come into play. I guess I'm still... I'm still... I'm still voting for the switching off-learning and the... On the child object. Sorry, Ron.

Ramy Mounir: I was just gonna say, this seems like a fundamental, question for me, at least. are we building these models in Monty or in TBT? Just enough to be able to make predictions. Or are we building the models first, and then we're doing inference? right now, in Monty, we are... We're learning, we're building the models, we're just going through these points, and we're adding all of these observations into the model. And then later on, we're using them to do inference. But other theories, like predictive coding and other theories, are... basically, they're just built on the idea of you're only building models that enable you to make predictions, and you're only learning enough to make predictions.

So I guess...

JHawkins: I'm not sure I understand the difference, but I don't like the language of the second, We're building a model... prediction is a key component of how we determine if the model is correct or not, but it's not... the goal of the system isn't just to make predictions, like predictive coding. I don't think that's right at all.

Ramy Mounir: Okay, good.

JHawkins: That's an offshoot of what the system does.

Hojae Lee: Oh, I think. ads. for one example, that we're not just making it for prediction, is that, there was, like, a paper that I shared, a while ago on, can GPT-5 do spatial reasoning? And it basically gives you, some blocks and, a picture of blocks, and say, what would this block look like when you look at it from top-down? And, it does a horrible job... not horrible, but it doesn't get it right, basically, even though it will be, like, very trivial for humans, even babies, to, imagine what that top-down view might look like, but we're never going to, train blocks on top-down views. it would be true for Monty to, learn the model, 3D models of, blocks. we could probably even make it, now. But then in... I'm thinking about, more towards also, goals, okay, if given this random question, what would this look like from top down, or side, or bottom, whatever? if Monty, because it has this model. We should be able to answer, any, any question.

JHawkins: are you saying, Jose, I think... I think what you're saying, Jose, is that... The goal is to build a model. From the model, we can make predictions, novel predictions as well. The goal is to build a model, right?

Hojae Lee: So true.

JHawkins: I agree. It's a good example. It's a good example. Alright, so it... the goal is to build a model. Not just make predictions. So where were we? Yeah. What were we talking about? Yeah,

Niels Leadholm: Okay. No, that's... that's helpful. It's... yeah, it's a little bit of a tangent with the unsupervised learning, but I think that is a thorny one, so it's... And it does relate to... It's becoming more and more of an issue with compositional objects, basically, because We cannot keep hiding from the fact that Yeah, we'll want to learn objects that don't have clear, Borders and all this kind of stuff.

Viviane Clay: basically, we can't keep supervising at every level.

Niels Leadholm: Exactly, yeah, it's gonna keep... it's gonna get increasingly hard to have any sort of supervision.

JHawkins: So, what.

Niels Leadholm: Yeah, one...

JHawkins: I didn't follow A to B there.

Niels Leadholm: that implies...

JHawkins: So that said, we won't be learning all the time. Is that... is that what you're saying? Or something else.

Niels Leadholm: that implies that, we need to have good ways of dealing we need to have good ways of learning without knowing exactly when learning is meant to take place or not meant to take place, and without always being able to provide labels.

the labels is a separate thing, but knowing when to provide supervision, or when learning should happen, that's the issue that sparked this discussion, because, We want to...

JHawkins: once...

Niels Leadholm: Constrain when the low-level learning module switches into Or, Right now, we're constraining it because we don't have an intelligent way of saying, okay, now you should be learning because you're making prediction errors, or whatever.

JHawkins: I have a sort of a general idea... feel about how this works, as if I can articulate it. it's in some sense, let's say we're always learning, and what... essentially, all learning is compositional in some sense, right? There's features or something at some location, and that can be a complete object, or complex something, or simple things. So always learning compositional structure, but it seems to me we'd only be doing it at one level in the hierarchy at a time, or... or always at the top of the hierarchy, or something like that. Where... whereas, it's if I... if I have a problem, it's like I was saying earlier, okay, I'm in the room, I'm learning... I'm in the room, I'm learning the compositional structure of the room, assuming that I recognize all the objects in the room. And I don't try to relearn those objects, but if I see an unusual object, I focus on that, and now I'm learning that object, and I'm forgetting about the room. And if I see a component of the second object that's unusual, has unusual switch, then I'll focus on that. So it seems like there's this... however this is organized in the hierarchy, it seems like we're... we're doing compositional structure at one point, at any point in time. It could be at one point in this... this depth of compositions. And we're not doing it all the time, so that doesn't solve the problem we're talking about, but it does say it's only happening at one point, and if I can't do it there, I have to drill down and focus on something else. I keep... I keep going down until I recognize something and say, okay, now I can build a composition of the things that I recognize. Does that make sense?

Niels Leadholm: Yeah, definitely.

Viviane Clay: You have to... you can shift your attention through the different levels in the hierarchy, and only one of them can be learning at a time. And if it's a higher level one that's learning, then the one that gives input to it is just doing inference to provide input.

JHawkins: What I don't understand yet still is... what if I find there's something wrong? I'm looking at the room, and then I see the book, and the book doesn't look right, and I go focus on the book, and then I see, oh, there's some weird thing on the surface, I focus on that. where is that happening in the hierarchy? Is that... is that somehow all shifted to the... now the book at the top of the hierarchy, like in the antherinal cortex? Or is this learning in... in, V1?

It feels once your attention shifts, that all this learning first occurs in a fast learning module, with, the hippocampus. So how that's distributed over the hierarchy is not clear to me. It's just not clear, but I think the sentiment other than that is correct, right? I think you expressed it well, Vivian.

Niels Leadholm: Yeah, okay. Yeah, that was actually something else I was gonna bring up, which was, like, yeah, this kind of slow learning in lower-level learning modules And how that could... contribute to some of this sort of stability as well, that, like you say, when you're learning something totally new for the first time, and you're learning it quickly. That's probably happening at the top of the hierarchy.

JHawkins: I've said this before, we have a problem with the Thousand Brains Theory in that we don't really understand how learning occurs across multiple learning modules. It works great for one learning module, but, we've come up with numerous instances where we don't have enough... in the behavioral system, we don't have enough... you can't... We don't understand how you can... how we can learn these things quickly over multiple learning modules, somehow the learning is distributed in a way we don't understand.

it's an open problem we have to address, which relates to this, so I'm just pointing out, it's part of that problem. You just put aside for today. If you want to focus on doing a compositional object testing, I think it's a reasonable assumption to assume that the child objects are fixed. At this point.

Niels Leadholm: It's a reasonable assumption to assume that the child object.

JHawkins: The child object is not... the child object is not learning. It's just...

Niels Leadholm: Or you have the child learning module?

JHawkins: Yeah, and also it would be assumed that... that... that it knows what it's... somehow voting would have occurred, so that It doesn't have to do a lot... we don't have to move the sensor We don't have to move the sensor to infer the child object. We want to be... we want to be moving our attentional focus from child object to child object, not within the child object to infer it. So if I, again, if I'm touching an object with my finger. I may not be able... I'd have to move the finger to infer the child object before I could assign it to the parent object. I think... I think we can assume that inference is occurring through voting, it's instantaneous. And up, in the child object, Which we can't do with one learning module, but we can... we can... Just fix it at this point.

Niels Leadholm: Yeah.

Can I start? Brings up another kind of interesting one. Which was, yeah, under evaluations. one thing I was just thinking is that, We talk often about how low-level and high-level learning modules can also converge on the same object, and vote with one another. And I know our focus is on compositionality here. But I was thinking something for us to maybe revisit at some point is... Having some metrics that capture this kind of condition. Which isn't necessarily wrong. Which is Yeah, basically that the child and the... learning module converged on the same object.

JHawkins: What kind of metric are you thinking about there?

Niels Leadholm: it doesn't need to be anything complex. It's more just needs to be, basically, we capture that information. Or look for it. Don't we get.

Viviane Clay: that right now with the parent-to-child mapping? consistent child object?

we would get correct, consistent child object if the parent learning module Recognize the mug instead of the mug with logo.

Niels Leadholm: yeah, basically we would... we would look for consistent child object in both learning modules, and also the same Because they could both have consistent child objects and not be converged to the same object.

JHawkins: Of course, in the brain, no one would know that they're consistent. They're just two different SDRs, Loading Module 1 and.

Niels Leadholm: Maybe I'll define... I'll define that, because the way we're using consistent here is a specific thing. in terms of, evaluating performance, one of the ones that we introduced During the hackathon is, this concept of a consistent child object.

if you imagine you have an object like this, we define, as the human experimenters, a list of potential chat objects that could be there. for example, mug and TPP logo. And potentially, we could also define particular poses, The logo either at the kind of neutral pose or the logo at this pose.

And then... A consistent child object is when the output of a learning module Is in the set of these Potential child objects. But, importantly, we don't know When the learning module has this output, we don't know exactly where the sensor module is. And therefore, we can't know for sure that this is correct. maybe it was on the handle for some reason when it converged on TBP logo. But we can at least say. It's consistent with what it could be looking at. Whereas, obviously if it output, an entirely different object, or an object in an incorrect pose, then we would still call this confused.

Viviane Clay: But yeah, this is really just for the experimental loop, and a bit constrained by what information we have in habitat. And not anything we would say is happening in the brain or something like that. For that, we're looking at the prediction error.

JHawkins: so let's throw ourselves into some more theory here, so here's a thought to think about. I asked myself, what happens when Region 1 and Region 2 are both recognizing the mug? And, what if I assume the same compositional mechanism was in play? The mug would essentially learn that, the object... let's say, so region 2, R2 and R1, we'll use those terms. R2 is saying, hey. There's a... there's some feature at this location, and R2's... R2's feature is mug. R1's feature is a mug. R1 is saying, I have a mug, I'm recognizing the mug, and R2 is saying, hey, there's this feature at this location, and I can learn it. In some sense, what I'm saying is that a mug recognized in R2 could be considered in some sense, a feature of the mug in... a mug in R1 could be a feature of the mug in R2. It... it... the mechanism seems like it would work. It's basically saying, I recognize something and help that I, R1, recognize something that's going to help you, R2, recognize what you're... what, what you're looking at. And if I see a mug, that's gonna help you know that you should be seeing a mug, too. in some sense, I didn't see any reason why that wouldn't happen, and what the problems with it would be.

it's really. this issue of consistency. It's I don't know if we need to have some sort of special mode that says, oh, now we're looking at a child object, now we're not. it could be whatever R1's recognizing, that gets assigned to the locations.

Viviane Clay: location-by-location basis is what R2's looking at.

JHawkins: And if R1's looking at a mug, that's what's being assigned to the mug. R1's mug is, in some sense, the same as R2's mug. It's a child, of course.

Viviane Clay: That's a good point, that, even if the object itself is, per our definition, not a compositional one. Region 2 doesn't know that, and would still get input from Region 1. yeah, Niels, I was just thinking, in our configs, maybe we should set them up so that when we learn the individual objects, we're just... We're first just training the lower-level learning module on the individual parts, and then... After that, we train the higher level one, Oh, no.

Niels Leadholm: Yeah, right?

Viviane Clay: and compositional objects, and during both of those, it can get input from the lower level one that does.

Niels Leadholm: Yeah.

Viviane Clay: Instead of learning the individual parts in both of them. As individual parts without hierarchical input, and then the compositional one and the higher level one.

JHawkins: I didn't... I didn't follow that, I don't know if I need to. Yeah, it's maybe more of a...

Niels Leadholm: But it's what you just described,

Viviane Clay: Yeah, basically allowing it to also get input from the lower level one when it sees the individual component.

JHawkins: Another thing that's nice about this is that we've talked in the past, V1 and V2 both might have models of the same objects, but they're at different scales. And, it's a question that's... never really addressed was like, how does it switch between those two? How does... when does it get too big for one and too small for the other, and there's some overlap where both are recognizing it? It feels like this mechanism where they act like child parents all the time. Helps... helps... makes that transition, in some sense.

I don't know how to describe it other than it feels like it's more fluid about where the representation of the object is between V1 and V2 and V4, because... As this... as the scale changes.

it just, merges these together. The mug becomes merged together across these different levels, because a small mug can be a child... the mug and be wanting to be a mug. I'm not expressing this well, but I think it... it just unifies the whole sort of scale issue. There's not, Maybe I should just take that comment back, it's a little bit weird. But anyway, I still... I still think the idea has merit. A mug could be a child of a mug.

Niels Leadholm: Yeah, and it... Yeah, I think, like you're saying, Vivian, we could already set up the config to have this, You can imagine that happening in this case, where, If these features are all disk, and the high-level object is just disk. That it's going to be, disk that's learned Sensor... sensory inputs, and disk that's learned. Kind of disk features at all of its locations.

Yeah, and so... I've added that here, cause I feel like, yeah. This kind of gets into, yeah, this sort of strangeness of heterarchy. And, so yeah, that we can have, Kind of low-level learning module, learn individual objects first, then train the high-level learning module on those same individual objects. But it'll develop these as compositional ones. And then for the voting across levels of hierarchy. I think it's just a case of... Having somewhere where we, In general, we don't really have much for, measuring voting except for post hoc. Maybe that's something to do more of. But, in this case, it would be just checking that they both get consistent child objects. That metric I was explaining earlier, Jeff, and that these match, that they have the same consistent child object.

It could just be interesting, for example, to see, like, how often The different levels of hierarchy are recognizing the same object.

Okay, Yeah, and while we're talking about, evaluations, I was just gonna revisit the prediction error thing, because that's probably one of the main things that came out of the Retreat was actually implementing that.

So the idea with that was to come up with a kind of unsupervised, Way of measuring how well our compositional models are doing. And the prediction error is basically the, inverse of the evidence that's incremented on any given step by these evidence learning modules for the most likely hypothesis. So the most likely hypothesis is we're assuming what the learning module, what the column thinks it's seeing. And if that isn't... if that... Either doesn't have much evidence, or the evidence actually drops on the current step, as in the change, then that's indicative of a high prediction error.

And then these were just some kind of, Toy diagrams to show different conditions that we might expect. where... In the kind of, baseline example, where we're capable of recognizing the mug and capable of recognizing the logo with the learning module. What you see here is the prediction error following, because basically, the hypothesis The most likely hypo- or, the hypothesis that is correct slowly climbs up until it becomes the most likely hypothesis, let's say around here. And because that hypothesis is correct, it knows where it is on the object, it's making low prediction errors. But then as soon as it moves to the logo. It's now surprised by that. It wasn't expecting that, and so it starts getting high air.

You could have a failure case where it never... the kind of most likely hypothesis that's correct, or the hypothesis that's correct, never becomes the most likely hypothesis, in which case you'd have a consistently high prediction error.

That's not that interesting an example. And then getting into more, compositionality, You can imagine... So first, so again, this is on the y-axis, we have the stepwise prediction error, the step on the x-axis, I should have said.

And We start on the mug. And there's some rotational symmetry, we we know we're on the mug, and we have some sense of where we are, but there's many possibilities. We have enough of a sense that The most likely hypothesis is basically getting no prediction error. But let's say because of rotational symmetry of the mug, it thinks it's somewhere on the... On the kind of, on it, but it's actually somewhere else, and then suddenly it goes onto the logo. It's still going to get a high prediction error because, it didn't... the high-level learning module didn't predict, the move onto the logo at that exact kind of step.

But then, the hypothesis that addresses this kind of symmetry, or that Isn't symmetric, that is unique to, a location on the logo It's eventually going to win, and then we get low prediction error. And then at that point, we know accurately where we are on the mug, and we can move on the mug with logo, and then at that point, we can move back onto the mug, back onto the logo. And maintain a low dictionary.

JHawkins: I'm confused, but maybe, these are unfamiliar terms for me, Yeah, but... so if I understand this. Why did... why when I'm... so the learning modules... this is... I'm not sure if this is one learning module we're talking about right now? This is the second one. Yeah, so I... yeah, so I would say, you can imagine that this is the high-level learning module that recognizes compositional... Okay, so it's... now that it knows it's on... the... the picture falls because it knows it's on the mug. Yeah, I know where I am. But if it's already learned. the mug with the logo, why is there a prediction error in the next section? Why does it jump back up again?

Niels Leadholm: That's the rotational symmetry. Okay, maybe this example is easier.

JHawkins: Oh, my gosh.

Niels Leadholm: Started with it.

JHawkins: Alright, that's what I was expecting, that one.

Niels Leadholm: Yeah, okay. if it sends the handle first. then it will know exactly where it is, and then you're right. Then if it knows the Mugwood logo, then it'll... It'll never get the big jump.

JHawkins: in the first example. In the first example, it didn't actually know where it was on the mug. It was... it was... it was incorrect.

Niels Leadholm: Yeah, it was correct... it was correct within the domain of the mug.

JHawkins: but if I know exactly where I am, then I should be able to predict the logo, but...

Niels Leadholm: Yeah, so I'm not saying... yeah, it wasn't... it didn't know exactly where it was.

JHawkins: It was making corrections because of the symmetry of the monk.

And so it's happy,

Viviane Clay: Yeah, the same thing would happen in a normal Mac without logo, if you moved to the handle for the first time.

And then resolve the symmetry. But, I think in the second example. We could still get a higher prediction error when we move to a logo, because the higher-level module knows mugs with and without logos. And before it moves to the logo, it doesn't know yet which one it is, so it might think we're just on the featureless mug, and predict to see white, and then when it moves on to the logo, that's when it first gets a high prediction error, but then pretty much on the next step, it knows, okay, I'm actually on the mug with logo, and I'm gonna keep.

Niels Leadholm: At that point, yeah.

JHawkins: I have a cabinet of mugs, and most of them don't have a logo, and the mugs are all facing, so I can't see a logo. Yeah, But one of them has a log... one of them has a logo on it. I didn't anticipate that, so I take it off the shelf, and then I... and I... and I turn it, and I go, oh, this is the one with the logo on it. It's it catches my attention, right? Because most of the buckets don't have the logo, that kind of thing.

Viviane Clay: Yeah. But yeah, the nice thing about this prediction error metric is that it's really simple, but it's really powerful, we don't need any log... any labels, we don't need any supervision, and we can just basically judge Monty's performance based on how well it can predict the next sensory input.

Niels Leadholm: What were you gonna say, Ron?

Ramy Mounir: I was gonna say, in the scenario where we have enough symmetry evidence, should the prediction error metric be calculated as an average over all of those symmetric poses? Or it would be only still the MLH, because there's nothing really special about the MLH, we're saying... Monty assumes they're all equal in terms of validity, Should we just average.

Niels Leadholm: Yeah.

Ramy Mounir: Or.

Niels Leadholm: I don't know, my temptation would... be that it's... there's still just one hypothesis, but it's... The sort of averaging or the equivalence is more across the rotations rather than across Because it feels like... Yeah, I don't know. When... when you're on a symmetric object, it feels like you still think you're at a location. It's not that you feel like you are at multiple locations at once. But it's like, all of those locations Or rotations of the object are equivalent.

Ramy Mounir: Yeah, it probably wouldn't make that much of a difference, because only one of them is correct in those symmetric poses, so it would only bring down the prediction error just by a little bit, because let's say we have 10 of them, 10 symmetric poses or more, and only one is correct, so the average is not really going to make a difference.

Niels Leadholm: Yeah, cause if they're... And then, presumably, if we are detecting symmetry, then that's because they're all similar.

So yeah, there might not be much of a difference.

Viviane Clay: I guess the other question could be is if we have multiple possible hypotheses that are all, in the, above the X percent threshold in Monty terms. It's basically as if Monty would be making several predictions at once, like... like you said, I have a cabinet with mugs, and this mug could have a logo or not. Both of them are valid within my models. If we should... If there should even be a prediction error, if it's valid with one of my possible hypotheses.

Niels Leadholm: I guess that's what I'm wondering, is that what we actually do? Because I feel like that's why, bistable stimuli are the way they are, is we We seem to commit to one. Hypothesis.

Viviane Clay: I guess once we pass it up the hierarchy, at least that's how we thought of it, once we pass it up the hierarchy, it's... we commit to one, the most likely one, but internally, within layer 4, we can predict several things at once as possible next sensations.

JHawkins: that mechanism came about when... when we were thinking about how a learning module or a cortical column wouldn't... hasn't figured out... hasn't come up with a good hypothesis yet. It's still confused. I'm a little bit along with Niels on this one, since it feels like... we lock into the, into a... once we have a good interpretation, we kind of stick with it until we know better. We don't try to keep multiple hypotheses going along. I don't... I want to pick the... pick the mug off the shelf. There's 10 mugs up there, and I don't see a logo. I know one of them has a logo. Or maybe I know somewhere in my house there's a bunch of logo, I don't expect it up there, I don't keep the hypothesis going, oh, maybe this is... I wouldn't normally think about it. I don't know, I feel like... It feels like the bistables sort of example is closer, and yet the theory about, the union of SDRs makes a lot of sense when you're... when you haven't figured out what you've got yet. You haven't settled on anything. So as soon as you settle on something, the whole... the union goes away.

Viviane Clay: Yeah, I guess in this example, we wouldn't have fully settled yet. We would be like, oh, it could be the mug with logo, or it could be the mug without the logo, based on what I've seen so far. So I would put,

JHawkins: But you have a hypothesis, which is... Which is consistent with everything, so there's... I have two... I see your point.

Viviane Clay: come to this.

JHawkins: Yeah, I see your point.

I don't know, that's weird.

Niels Leadholm: I don't think we'd want to do the extreme of, The prediction error is the minimal prediction error across all hypotheses. But I think you were suggesting it's one above a certain threshold?

Viviane Clay: Yeah, or depending on, right now, it would be the ones that are above the X percent threshold, once we do, hypothes deletion. It'll be all.

JHawkins: You know what?

Viviane Clay: still exist, But, yeah, I'm... it was just something that I just thought of. I haven't thought through it much yet. Right now, we're not doing that. I just thought it might be worth considering if that...

Niels Leadholm: Yeah, I don't know, Yeah, right now we use the most likely hypothesis to measure prediction error, but we may want to consider, other hypotheses as valid as well, or...

Viviane Clay: Yeah.

JHawkins: Yeah, let me just... let me just go back to, the comments you were saying a second ago. When we have the mug, but we don't know if it's a mug with the logo or the mug. We... we've just, in the beginning of this meeting today, we said, oh, that's the difference in state. In some sense, we've locked onto the correct reference frame. And now we're dealing with the difference of state. in some sense, I've... even though I don't know if it's the log... the mug with or without the logo, I have the... I've determined the correct class of this object. And the only... the only, variation right now is this... is this... It would be this sort of state of whether the logo is there or not, which is... which is not the same as being confused about the object. Because the logo... the mug with the logo and the mug without the logo are not completely two separate objects. They are the same object with variation. Yeah, it's maybe a bit more like being confused about where on the mark we are, because we haven't sensed the handle yet. Something like that, but... But think of it this way, we blocked onto the correct reference frame. So that's done. That's certain. at least we think we're certain. Because when we see the logo, we don't switch to a new reference frame. We just switch to a different state of the... Public mission.

that... that said you could be... you could lock on.

And maintain uncertainty only in the state. I don't know if that helps, but...

Niels Leadholm: Yeah. Yeah, for what it's worth, just to give a, show with another example... yeah, I'm open-minded about this, but just, yeah, trying to explore, at least perceptually, how it feels. if I'm thinking about where I am on this, even... even if I'm a... I could be anywhere along the edge. But at any given time, I only feel like I'm at one location. Like, all of these locations are valid. But...

JHawkins: you're at one of those...

Niels Leadholm: Actually, it doesn't feel like I'm everywhere on it. It's more that... It's more that this is the kind of, thing that there's multiple superpositions, its rotation is the thing that's, there's multiple things that are consistent, not my location.

Viviane Clay: Yeah,

Niels Leadholm: Maybe in one place at any time.

Viviane Clay: Yeah, so what we're talking about right now is a metric. So what would be most useful for us to measure and look at? And, like, when you show these plots, we're saying, oh yeah, here we expect the prediction error to be high, because we haven't resolved the pose yet. So we're, like, excusing Monty, being like, it's reasonable to have a high prediction error. But then in that case, if we want to minimize that metric. I feel like we should take into account the places where we are saying, oh, yes, this is expected, that here the error is high.

Niels Leadholm: Yeah, so maybe one way of framing it is, we could have multiple prediction errors. There could be, like, prediction error of the MLH versus prediction error of top hypotheses. Or something. And then... Prediction error of all hypotheses is essentially the inverse of the, Or, is like the, theoretical limit metric that you made, Rami.

Actually, would that be interesting? Because the theoretical limit That doesn't account for location, does it?

Ramy Mounir: No, only rotation.

Niels Leadholm: or symmetry.

Ramy Mounir: Just a minimum pose error. But it...

Niels Leadholm: There you go.

Ramy Mounir: with them.

Niels Leadholm: But yeah, the prediction... formulating it as a prediction error might be a way of accommodating for that.

Because that would just naturally absorb any... causes of, Yeah, okay, I'm gonna expand this note, additional versions of prediction error. Yay. Hypothesis... Given threshold... Okay.

Yeah, and any more on this prediction error stuff, or should I move on?

Ramy Mounir: I was gonna just... just to note, I'm not sure, are we going to also factor in noise, when we're talking about prediction error? Or is it going to be... I think it makes sense that if we're looking at a noisy observation, that our prediction error is going to be high, but do we want to smooth it, or are we just going to keep it as, okay, this is just the prediction error of this step?

Niels Leadholm: You mean, to make the benchmarks comparable? like... Dealing with the fact that right now we would inevitably see a higher prediction error on a noisy benchmark, or...

Ramy Mounir: Yeah, not just, on a noisy step, a noisy observation. Basically, the prediction is going to shoot up, and then, it's basically gonna fluctuate a lot, and... Should we average over time steps, or is it just expected that if we see a noisy observation, the predictions are going to be high?

blood that you're showing, so it doesn't really show the effect of noise, but I think that... Yeah, sweet.

Viviane Clay: the metric we report is the average prediction error over the whole episode, so it's already averaged over all of the steps anyways. I don't think we can really do anything about, noisy observations coming into the learning module.

Niels Leadholm: Yeah, I think the only thing we could do is, You could imagine having a plot where normally it... it bots the, It had a kind of a detailed level, like the raw values, but then you have, a smoothing scale on your plot, that if you want to see the smooth result, then it, Then it does that.

Ramy Mounir: Yeah, makes sense.

Niels Leadholm: And then, yeah, and then... I'm not suggesting we need to do this right now, but I was just thinking, there are some high-level forms of, prediction error that we could also use, for example, chamfer distance. I think this could become more relevant What you call it, when we look at, unsupervised object segmentation. If we want it to recognize that there's a handle, and that the handle is its own object, and where the handle is and stuff.

JHawkins: You can imagine, Chance.

Niels Leadholm: Oh, sorry, this is the metric we used in the DMC paper. This is where you have, two point clouds, and you're looking at the distance between them. on the left here, there's a high chamfer distance, on the right, there's a low chamfer distance.

JHawkins: Got it, yeah, okay, thank you.

Niels Leadholm: Or would, the logos a Euclidean distance and image space, or... Just things like that. But, yeah. Just something to consider. I think this one we talked about before the retreat. Yeah, and that one we talked about... Yeah, and then... So in terms of, so there's metrics, and then there's, how do we, mediate compositional Learning to actually happen. the thing we've done so far is just have some supervision. This is what we were talking about, how we Make sure the low-level learning module has had a chance to learn the child objects, then we ensure it's an inference, and then we pass a label to the high-level learning module. Stuff like that. But then there's a bunch of things that would be improvements to Monty, so they go beyond the scope of just, a dataset.

Or benchmark, but I still thought it was interesting to maybe talk a bit about them. And these are the things we've talked about before, with the sensor modules. So the question is, like, how do we actually observe the effect we want, which is that, low-level learning module is recognizing child objects and passing that ID up, and the high-level learning module is recognizing compositional objects. Yeah, we talked about sensory modules, how you could have differences where, the high-level learning module has a large core sensory input, so it's less likely to be able to even recognize something like the logo. And it's going to have to rely on the low-level learning module to recognize the logo and pass that idea up.

Whereas on the other hand, if a low-level learning module has a narrow, kind of fine-grained sensory input, it's going to struggle to learn big objects, and so it's less likely to learn things like, the entire mug.

Viviane Clay: And we... we already have that in our configs, that the lower level one Gets higher resolution, more fine-grained input than the higher-level one. Plus, also, the settings of the models that we're learning are a bit different in, what information is considered redundant. But then, one other parameter I played around with, 2 years ago, I think, was restricting the size of the models that the low-level ones can learn, basically a low-level Only represents objects up to a certain size, and then if the object is larger than that, it'll just not be learned there. I don't think we set that up here.

Niels Leadholm: No, and it's interesting to think about what that would mean here, because, Right now, yeah, so this is what you're talking about, where... Yeah, we already had, the low-level one learns this kind of detailed model of the cube, the high-level learning module learns this kind of coarser one.

And I guess then when the... when the high-level learning module is learning the compositional object, it's then going to get the ID output from the low-level one, even when it's on the cube, or when it's on the mug. But if we constrain the size of the models of the low-level one, it might be that it can only recognize the logo, and it can't recognize the mug at all.

And then the question is, okay, is that an issue? I guess not, because the high-level one To our whole argument before about, state and whatever. It could just, learn okay, I'm... this is a variation of the mug, and it might not... so it basically just... it might not always be getting an ID From the low-level learning module.

Viviane Clay: Yeah.

JHawkins: I've been taking some notes here because I think there's a whole set of issues that are related here. And, I'll throw out the word attention as part of it.

how does... it's just how do the representations occur at different locations in the hierarchy, and how are they constrained? I just think, this question of, oh, are we gonna physically constrain what it can recognize, or are we, an intentional mechanism to constrain what it recognizes, and I feel this sort of an uber theory here that we just haven't dealt with yet. I don't think it's going to be hard. I just don't think we've really grasped all this yet. It keeps going back to, like, where it's happening where in the hierarchy, and what is... I just throw it out, because I don't want to stop what you guys are doing, but I just want you to know that there's some things that we're missing here we have to deal with. They feel like they should be easy to deal with. We haven't done it yet.

Niels Leadholm: Yeah, and I'm curious, because I remember, yeah, taking some notes when I thought you made some nice points about, yeah, attention and how that would play a role in this, so that, Yeah, so you can imagine, they're both recognizing, mug, the low-level one and the high-level one, and then you move to the logo, and then it's the low-level one that is going to, have this narrowing of attention To see,

JHawkins: Maybe there's.

Niels Leadholm: detailed thing. And that would work with voting, of course, to constrain where the voting is happening.

JHawkins: Another thing that came up just listening to the conversation here was, like, is it true that the lowest level learning modules are always inferring something? Maybe not. maybe, the inference's starting higher up, and there's nothing small to worry about at the moment. And... so that's just another flavor of this problem. Where are things... where are things being inferred, and where are they... where's the learning occurring?

again, I don't want anyone to get worried about it, because it feels like we have the basics down pretty well, that we understand how compositional structure is learned. And we just have to... now have to play that out over, these are all questions about, oh, exactly which modules are doing what, and how is voting coming into play, and... and, are we locking things down or not? Anyway, these are all related, it feels But hopefully... Yeah, I think that's...

Viviane Clay: Oh yeah, go ahead.

JHawkins: I was gonna say, hopefully, that these uncertainties don't slow you down in implementing this right at the moment.

Viviane Clay: Yeah, no, I was just gonna say, that's the idea right now, that we have a basic testbed, but now we can iterate on it, and we can make improvements, and we can find out all the kinks, and things we didn't think about, and all the issues that come up, and improve on how we're doing right now, but basically we have all the plumbing in place, one, to pass up the object ID and connect learning modules hierarchically, and two. to, evaluate how we're doing. And now, the next months will be iterate, improve, So I think, in that context, we can get away with two learning modules and do a bunch of,

JHawkins: Hacky, hard-coded things, knowing that we'll solve those hacky, hard-coded things later.

Viviane Clay: Yeah.

JHawkins: we don't have to, hey, this is, one learning module, how am I going to get to do this stuff? It's you can just do it now, and we'll get the voting working later, and figure out some of these other things later. I'm good, I'm glad that we feel that way. It makes me motivated right now to want to work on this right now, trying to take a note and going, I don't want to think about this. It's annoying. Okay, good. Yeah.

Niels Leadholm: No, I think it's... like you guys say, yeah, I think it's a good position we're in now. One thing I just thought was... Maybe a bit interesting to talk about was, in terms of policies. I think in my mind, there was a lot of overlap with attention, that... because, they're both potentially segmenting out the world, and using that to Guide information gathering, but kind of attention could be more, all at once.

JHawkins: You're talking about, action policies here?

Niels Leadholm: Yeah.

JHawkins: Okay.

Niels Leadholm: Attention is Would be all at once, constraining where voting is happening and things like that, which learning modules are actually involved. Whereas policies would be yeah, where we move. But you can imagine something similar, whereas as an attentional window narrows, the policy constrains us to move in a smaller location, so until we recognize the logo. And this is something we've talked about before. And that kind of narrowing could be based on both model-based and model-free signals. But, yeah, when I was thinking about it. Although that could help us to recognize what is, the logo, what is that small object. That wouldn't do anything to prevent the high-level learning module from also trying to recognize that small object.

So it feels yeah, other things are definitely going to be important.

the attention, or the difference in the central modules, and maybe this implies that which I think is consistent with what we've talked about before, that maybe the attention is different for different levels of the hierarchy. the higher level learning modules, they're attending to a larger region, whereas the lower level learning modules are attending to a narrower region.

JHawkins: once I think about this. is, I'll just throw out an idea. let's say we have a hierarchy of regions, 2, 10, I don't know. But let's say the top one. is always in the mode of learning compositional object. Always. Never stops, because it's, a fast memory, it's, like the hippocampus. It never, stops, so it's never gonna sit there and go, oh, I recognize the mug. It's always saying, I am always building a new object up here. And, it could be the room, it could be, anything, I don't know, but I never stop.

I don't know if that... it puts an end stop to the question you brought up, Niels, which is how do I... how do I prevent the top-level module from recognizing... I could... I could somehow think about, the top module never stops learning compositions. It never... it'll never be happy with something. It'll say, I don't even know what that means yet, but it just says... it's a... it's a way of constraining the problem a bit.

the system will never be happy. They'll never say, oh, we're all recognizing the mug, and we're done. It'll be like, I'm gonna recognize... if I recognize something, I have to... I don't know, I have to put it in a larger context. the top module's always trying to figure a bigger context. It's never gonna settle. It'll never... it'll never infer anything. But.

Niels Leadholm: Yeah, in some ways, it does feel like working memory or the hippocampus or whatever is doing. And that, Yeah, it's... it's always okay, what is the situation now? And I'm never going to assume that I've experienced that before, because the world is constantly changing.

So there's no point trying to infer it at the highest level.

JHawkins: That's I don't even... that's the basic idea. how does that... what's that mean, actually? But it does feel to me like that's the way we work in the world. We're just constantly... it took me a long to understand this, but we're just constantly building compositional structure At different levels, but never stops. Unless you're asleep or something, right? it just never stops. I'll look around a familiar room I'm in right now, and I'll notice that, oh, there's a new thing outside, or there's, the pillow's different on my bed, or I don't know what it is, I'm just... It's just if I'm constantly... and then if... and then that's assuming that underneath that high-level compositional learning, there's all these structured objects. And I just assume they're there, I see them, I recognize them, but if one of them was odd, like I mentioned in the book, then I would just zoom down and focus on the book, and that would be the new compositional structure I'm learning. I don't know. Anyway, so it's a thought to keep in mind.

Viviane Clay: Yeah, I think that kind of makes sense if, at the highest level, we always build this compositional model of the scene around us, and it's basically... there's no need to use it for inference, there's no need to recognize it, because it's just this specific arrangement of things on my table today, but it's still super useful to build this temporal model, because That helps me, if I look at the lamp, I know what I'll see when I look back at my laptop, because I just built a temporary model of how you are all arranged on my screen, so I can inform my lower-level modules what to expect next.

JHawkins: But if I... but again, I think it seems to me, even if I saw this book, and the book was odd. I would then be building a new compositional model of that book at the top level of the hierarchy. It'd be like, that would be my attention. It would be an episodic memory of, oh, I have a book that's in the shape of a trapezoid. I never saw that. I'll remember that. Oh, that was yesterday, I saw that. It was like, it's not something that's happening in V1, it's something that's happening at high level, It's You imagine the top level is always building these new compositional models until they become until it becomes so structured, then... then I can... they become... then that movement moves down in the hierarchy, and I can build new compositional models on top of it. Something like that. I don't know. It's even low-level objects, it seems somehow get learned in the highest level. small objects get learned at the highest level initially, and somehow they get transferred down. It's like almost everything is episodic in the beginning. I, I, don't... it's weird. I don't know how that happens. But it feels like that. Tristan's phone: Sounds a lot like chunking.

JHawkins: Chunking. Oh, I forgot what that is, just... Tristan's phone: Oh, it's like in learning, in chunking, you have to... you have to chunk.

JHawkins: Go right. Tristan's phone: And to learn high-level concepts, otherwise you're always stuck in the details.

JHawkins: I guess that, It's chunking, I don't know if it's a technical term or not, but sure.

Niels Leadholm: Okay, nice. Yeah, no, I think that's a... Interesting idea, though, just to emphasize.

JHawkins: But we can do it right here, we can do it. learning modules. We can assume that the second learning module is just constantly learning compositional structure, and we can assume that the first learning module is recognizing objects. And, that's your test structure, I think, right? And that's consistent with everything we just said. And we assume that the first learning module doesn't have to move to infer the object. I assume that there's... we'd assume there's some sort of voting going on there.

Viviane Clay: Oh, yeah, we don't have that in our setup, in our current test setup. The lower level one also has to move to recognize the object, because we only have one...

JHawkins: Wolves.

Viviane Clay: But there's no water.

JHawkins: Yeah, I know, my ad, yeah. I don't know, I don't know if that messes up the system, then. It's Again, the idea that I was just proposing is that Let's say compositional learning always occurs at, let's say, at one level, the top level of the hierarchy. And it assumes that, I don't need to... It assumes that every... every feature that I'm gonna put into that compositional high-level object is already... is recognized instantly. I don't have to tend to it, I don't have to drill down and down So moving... if I have to... imagine trying to learn computational objects with a finger. It'd be pretty damn hard, I think. I don't know, I'd... I'd have to recognize one object, and then... think about it with a straw, okay, it might be easier. as I'm looking around, oh, I have to recognize something. I'm doing with the straw, and I say, oh, that's the logo. And then... I don't... I don't know, would I... would I start by recognizing the mug? I'm not sure... I don't know how it works... I don't know if it works if I have to spend time moving to and fro the object. It almost feels like I just want to do, this one-shot learning. Here's an object at this... here... I'm building up this compositional structure, object location, as opposed to, oh, there's... I have to move around here to figure out what that object is. Now it's at that location. I have to move around and figure out what that object is. I'm not sure that works very well. I don't know, it does work.

Niels Leadholm: Yeah, that's an interesting point.

JHawkins: from a testbed point of view, we just don't want to get stuck on this issue of moving the sensor to infer the first child object.

Yeah,

Viviane Clay: If you will have a logo on a mug. you do move a couple of times to recognize the logo itself first, but maybe while you're trying to recognize the logo, would be what's represented in the higher level, and then the letters are at the lower level?

JHawkins: Yeah, I don't know. That's a good question.

I don't know. You're right, it's hard to... it's hard not to move your eyes.

okay, let's say I look... I look at a mug, and I look at the logo.

there's two situations. One is I don't recognize the logo with one fixation, and I have to move my eyes to recognize it. The other one is I do recognize it with one fixation, yet I'm still moving my eyes. the second one is... they're different, really, right? In the second one, you're constantly passing out a logo to the parent object. And the fact that the eyes are moving doesn't really matter.

But, the first one, where you don't recognize the logo until you Did you attend to it? Yeah, it feels...

Niels Leadholm: It was like a, rather than, a binary difference, it's a bit like with behaviors, how we said, a single learning module, it can learn a repeating behavior in theory, but it's just really hard unless it's moving really slowly and stuff. It feels similar, you can learn, probably, a compositional object through a straw. But it's hard, because somehow you need to recognize Both the low-level object and the high-level object. And have that context, and that's just... the situation where that arises is just harder.

JHawkins: That's a good parallel. The behavioral thing is interesting, because even though, in some sense, theory you could do it, I think practically it cannot be done.

I can't really learn behaviors looking through a straw.

It's just... it just doesn't seem possible, so it almost... it requires some sort of group action, multiple learning module. And so that may be true here too, right? Some sort of theoretical limit could work, but maybe practically couldn't work. Yeah.

Viviane Clay: I think... yeah, I feel like still there needs to be some kind of middle ground, because if we do assume there needs to be flash inference of the child object, it gets more complicated when we have, for example, the logo with the band in it. There is no. of the logo with the bend that we can just recognize. So we'd have to... we have to move to figure out, oh, here it's rotated differently.

JHawkins: it would almost be like, if I saw the logo with the bend, it was like me looking at the book, I'm like. And seeing it's an odd book. I would, in some sense, for a moment, I would forget about everything else, and I'd be focusing on that logo. I might learn, temporarily, learn a model of the logo with a bend in it, and I said, okay, that's a thing. Okay, now I'm gonna sign this other mug. I don't know, I don't have.

Viviane Clay: But then, yeah, if we rely on that mechanism, then we lose a lot of the benefits of learning location by location, and assigning different orientations, and having the kind of flexibility where the location. be better.

JHawkins: now you're right. Okay, alright.

Viviane Clay: But maybe it... maybe you have to learn the logo as a compositional object, and then...

JHawkins: I don't know.

Viviane Clay: All right, I... we've been bouncing around a few things here. I've taken some notes here.

JHawkins: things... things that we, I've talked about multiple columns may be needed for learning composition. They may... they seem to be needed for learning behaviors, that's what Neil just said.

We have a basic... this is base... it's a basic problem of how do we learn across multiple learning modules when only one is experiencing an input? That's the same problem. I've talked about... I know it's about attention in the hierarchy. How do we, where does... where does learning occur in the hierarchy? Maybe learning occurs only at the... the compositional learning only at the top. Anyways, these are all related. I'm just saying notes for myself to think about.

Niels Leadholm: Nice, yeah, so I had a couple more that I can just touch on.

One... so yeah, we were just talking about voting now, so this is, again, in a sense, under the kind of heading of, what are ways we can improve Monty, or kind of ways that will push it towards developing these Compositional representations we expect. And I was just thinking, Yeah, we often talk about voting, but what about competition? Because, obviously, voting is about reaching consensus, but sometimes We might also want to push different learning modules away, From observing the same thing. And for what it's worth, I feel like, anatomically, I think most of the lateral connections actually synapse on interneurons, so inhibitory neurons.

And.

JHawkins: Is that a blanket rule for all different types of neurons, or...

Niels Leadholm: I thought that was... True for most electrical... I can double-check that, but I...

JHawkins: I thought... I thought, in Layer 4, most of the lateral connections were,

Niels Leadholm: No, sorry, lateral connections across columns.

JHawkins: Oh, of course, Colm.

Niels Leadholm: the long-range lateral connections.

JHawkins: Oh.

Is that true?

Niels Leadholm: I think so.

JHawkins: I'd be surprised by that.

Niels Leadholm: I can... I can look that up real quick, but But anyways, yeah, I was just curious, in the history of voting and stuff like that, Yeah, is that something that's also been discussed in terms of, mug and logo. Some learning modules are seeing the mug, some are seeing the logo. Is there, Yeah, is there anything encouraging them to actually develop different representations rather than trying to have the exact same one?

JHawkins: Mountain did talk about intercolmar inhibition.

Last week, we talked about... remember, we talked about many columns activating, and they'd be like a Mexican hat distribution, and so you'd have local expectation and longer-distance inhibition, and therefore, they would force it would force... it forces, a distribution of representations, right? When around the bump of the many columns, you're going to not be active. And he talked about the same thing going on in columns. But he briefly mentioned it, but I don't know... I can't remember any... reading anything else about it. But the idea would be... If you follow the same idea with the mini columns, then you can imagine in larger columns, the cortical columns, you might have They inhibit each other locally, so you make sure the ones surrounding you are not representing the same thing. But then that enables the ones further away. And this... so we don't... we don't have a concept like that in Monty today. we assume that every learning module can learn everything, but in reality, maybe they don't. Maybe, we're forcing models to be distributed not across every learning module, but across some subset of the learning model, right? not every learning module would learn a mug. But every, every fifth learning module, every tenth learning module, the learning module. That's an appealing idea. One of the issues that, brings up is that we have to assume that... we assume that each learning module is... gets an input from a sensory patch, and the next learning module gets an input from an adjacent sensory patch. If... if you had enough... if you have... if your learning modules were couldn't... local ones couldn't be active at the same time they're distributed, then they might be... would they... would they, by chance, be looking at the right learning? would they have... do they have enough overlap in their... in their sensory patches to make that work? because then you might be blind to some part of the sensory space. It's another high-level concept that I think relates to this issue about distributed learning.

because if I wanted to... if I wanted to have learning in one learning module affect other learning modules, it would be... it would... it would not be to the... it wouldn't be the adjacent learning module, it would be some further one... further away.

that's a topic we've never... really, we never addressed... talked about this issue. I'm not even sure it's true, so I don't know. Okay, yeah.

Niels Leadholm: Yeah, no, we... we don't need to go down that. And yeah, in this case, I was almost thinking about it in... across the hierarchy, that, Sometimes we want to vote across the hierarchy, but maybe we also want.

JHawkins: A voting up and down.

Niels Leadholm: the hierarchy.

JHawkins: Okay.

Niels Leadholm: Yeah.

JHawkins: When do we vote up and down the RK?

Niels Leadholm: I thought that was, like, one of the main things in the.

JHawkins: I know, but you know what? It could be... Earlier, I mentioned the fact that two hierarchical regions could be observing the same object, and that one could be the parent and one could be the child. That could... that could be the way they vote.

That could be the way that they reach a consensus, is... as opposed to the mechanism of, like we've talked about, like Layer 3, the voting mechanism. There could be potentially voting.

Niels Leadholm: Better with the neuroanatomy, I think, because I seem to remember.

JHawkins: I'm right.

Niels Leadholm: They find it hard to... of the...

Viviane Clay: Yeah, there isn't a lot of, evidence about the... It's between her. patients.

JHawkins: now that we mention this, is a better... I proposed that idea because it seemed logical to me that When two regions are observing and inferring the same object, two hierarchical reasons, That they should, Have a way of collaborating to reach a consensus. in a sense, that's voting. But in this case, the voting could be a different mechanism. It could be the compositional hierarchical mechanism. And that would work, too.

Niels Leadholm: Yeah, and that would have the benefit of being more asymmetric.

JHawkins: It just... it fits the biology better, as you just point out. And it fits in our mechanism better. So you could call it voting, but not... not the way we voted, we talked about before. It's a way of two regions assisting each other, In reaching a consensus.

So Region 1 thinks, I think I might be on a mug, and Region 2 says, I think I might be on a mug, and Region 2 says, oh, but Region 1's telling me that my child object, quote, the mug, that helps me infer, right? Because my child is... my child object is telling me that... or my... the region below me is telling me it's... It's providing information that would help me infer mug.

Anyway, that's an interesting idea.

Ramy Mounir: Do we also need that for shifting the hierarchy up and down, or, shifting the two levels of hierarchy? for example. When, at the higher level is looking at, a table that has a mug on it. the higher level's looking at the table, then it needs to force the lower level to look at the mug, but as soon as the higher level Shifts focus to the mug, then it needs the lower level to look at the handle. it could be a way of... Poor St. Louis.

JHawkins: But we're saying... but we're saying it doesn't always do that, Rami, right? it could be... both of them could be looking at mug and mug. That was the scenario we just talked about.

Ramy Mounir: But would that be.

JHawkins: I'm not... I'm...

Ramy Mounir: official object?

JHawkins: I don't know, I'm not sure.

Niels Leadholm: Yeah, you're saying, Rami, this would... yeah, basically we'd be capturing both, That they can agree with each other when there's no specific information. They're both But when there is a specific thing, like a handle, then the high-level one can tell the low-level one to predict that.

Ramy Mounir: Yeah, I'm saying that the, we know that both models are in both higher level and lower-level objects, the cup is in both, but... when we're look... when we're dealing with compositional objects, we probably want... we don't want both to be representing the same thing, we want to prevent that, so we want the higher level to be forcing the lower level to look at the child object if it is looking.

JHawkins: sometimes you do, but I can come up with examples sometimes, too. Think about recognizing printed words as you're reading. And I can read very small fonts, I can read large or large fonts. And I... if I'm reading along. And I recognize words. I don't actually, it's pretty well documented. We don't recognize all the letters. We don't... in fact, you can switch the letters in the middle of a word, and often you just don't even see it. So there's an example of a hierarchical, a compositional structure. where the brain is not actually checking that the details of the composition are correct. It's saying, good enough, that's the word, it looks about the right shape, right size, and it's got the right curvatures, and so in some sense, we end up recognizing the word as its own object.

And, It's funny, as you get older, like me, you start forgetting exactly how to spell the letters in between. It's was that one L or two L's? I can't remember, Because you just... but I still can read, no problem. I just can't remember exactly how to spell some words that I used to know how to spell. interesting. Anyway, so I'm not disagreeing around, I'm just saying there seems to be some cases where we don't, we just accept that the overall word is... the overall structure is good enough, and we recognize it, and we don't... we don't require the... that any... any... any below seems to be paying attention to the details. Tell you, otherwise, if you switch the letters in the word, I would... I would... should notice that they're wrong.

It's a weak... it's a weak example, but just on the front.

It's a good question, too, Rob, so I don't know.

It seems like we wouldn't want to... force... The system to try to attend to all the hierarchical details that we know exist in the world.

Yeah, I guess maybe.

Niels Leadholm: Yeah, and in the case you were bringing up, Romi, yeah, I guess the focus is on, learning, I don't know if this is what you were suggesting, but One way might be even, okay, if the high-level learning module is struggling to predict something, if it can ask the low-level learning module to try and learn that better, basically just some sort of mechanism to push apart their representations.

Ramy Mounir: Yeah, I was assuming... I was assuming more that the compositional structure is already learned, and so as soon as one level starts inferring something at a different level, then it needs to force the other level to move also, to change, because we're shifting across levels. But yeah, it could be... it could have some, ideas also for learning. Come. forcing learning at different levels, I'm sure.

Niels Leadholm: Yeah.

JHawkins: it just goes back... this goes back to that comment I made earlier, this... this really confusing point for me. It's one time, sometimes I feel like learning has to always occur at the top of the hierarchy, and that's where it intense... And then, that doesn't explain, then. And so when you shift, instead of shifting things around in the middle of the hierarchy, you're basically shifting what's up at the top. Yet, at the same time, we have to... we have to learn in V1 and V2. Yeah, I don't know. I have to think about this one.

Niels Leadholm: Yeah. Isn't it we just dream, and then everything gets transferred to Cortex?

JHawkins: Maybe, yeah.

Niels Leadholm: deliberately.

JHawkins: again, it's... nothing gets transferred. You don't transfer... Yeah, I don't at least that's... I don't think so. But you... but you can... dream can replay things and cause things to be learned lower down. that's an interesting bringing that back into the picture, that's interesting. I usually pay no attention to that sleep stuff, but you're right. That could be a solution to this problem.

Niels Leadholm: I think that's at least one theory for dreaming, is that, yeah, it's like a random assortment of perception to... Yeah. enable.

JHawkins: they've shown that dreaming is essential for consolidating memory.

Niels Leadholm: But yeah, while we're on this topic, I like the idea of... All of the learning modules learning in parallel. But it just being, like, really slow at the lowest level. And in practice, it's Yeah, it's like you don't notice they're learning until months have gone by, and it's oh, actually, now they have this representation, whereas... Yeah, in, in an instant, the highest level can just learn a new... representation.

JHawkins: I was thinking about the and, his... He couldn't, basically, oh, he couldn't learn anything new, he couldn't learn anything new, he couldn't learn anything new. But he was able to learn a few things.

And I forget what they were, but they were... Things he had been exposed to over and over again, and he didn't think he knew these things.

they'd give him a task, and he says, I don't know how to do that task. I can't do that task. And then he would do it, and he'd go, oh, somehow I did it

Niels Leadholm: Yeah, so I remember looking this up, and one of the interesting examples was he developed a... he could draw, a topological map of his house. Even though it was many years after his injury, or the surgery, that, that he owned this house, that he purchased it. And, And basically, the argument... or, The argument was he just kept moving around the house, walking around, and so eventually he must have built, a model Of how it was arranged. But of course, some people would argue, oh, he had some preserved hippocampus, or something like that. But that was at least definitely one example of where he learned a structured representation Through many, instances of exposure.

JHawkins: repetition, right? Yeah. And, maybe normally it requires a hippocampus and sleep, and so maybe it took much longer for him to do that,

Niels Leadholm: Yeah.

JHawkins: That'd be...

Scott Knudstrup: Something also about his being able to learn some skills. having to draw, if you saw half an image, and you were trying to draw the reflection of it on the right side, I think that they were saying that was a skill that he was able to acquire.

weeks or months, but... which is distinct from episodic memory, but it still seems like some kind of spatial Base model or skill that, you know...

Niels Leadholm: Yeah, I think I had thought, oh, it's just, a motor skill, so that could be subcortical, but, it's a fair point that it does involve, the spatial element of, reflect... yeah, I don't know.

JHawkins: Obviously, neurons learn, and they learn through repetition and association, so we expect that to happen. The mechanisms by how different parts of the cortex, when they learn and when they don't learn, when the hippocampus is learning, how they interact, that's a bit of a mystery here. So it shouldn't be a surprise that is able to learn, because neural tissue will learn, right? If you give it enough exposures, it'll learn something.

But that doesn't... that's the normal way we rely on it. maybe most of the time we... maybe most of the time we do rely on... we need the hippocampus most of the time, and maybe most of the time we do need sleep with the hippocampus, or something like that.

I don't know. We're not gonna solve this today. we'll stick on topic and say, how are we doing on our task for today, which is...

Niels Leadholm: Yeah, so I just had one last, kind of small thing I thought would be interesting to bring up, which is about OmniGlot.

Just to rewind a bit, when we were selecting which dataset to, used for this task, for this benchmark. We discussed a few different ones. One was the object with logos, which we ended up going with. Another one's OmniGlot, which... Is this one where it's a bunch of alphabetical characters from many different alphabets, and it's... each... it's a small dataset, as machine learning goes, where they have multiple instances, multiple examples of each letter. drawn by a person, albeit not a native speaker, generally, of... or kind of person of that, language.

And it's... it's an interesting data set, because it's definitely compositional, you have all these strokes, and how they compose the letters. It's small, so it's really hard for traditional machine learning, deep learning methods to work with. And Vivian had already implemented a data loader for us to be able to work with it. The main reason we didn't go with it for this retreat was because, we realized we'd still have to implement a whole new part of the data loader in order to pass the individual strokes the way we wanted to. And learn on just those individual strokes.

JHawkins: Why is that... why is your assumption... why is that assumption? Why can't... why can't we use these as just visual objects?

Viviane Clay: Yeah, we already tested just learning the characters in general. But Marty did well on recognizing the same version of the character, but didn't do well on generalizing to different drawings of the same character.

JHawkins: Yeah.

Viviane Clay: Because it's... to... if you only look at the pixel level, there's too much variation between them. But if you can learn them on the stroke level, like the H is two vertical strokes and a horizontal one in relative arrangements, then the thought was Monty should be able to do it. So basically, this was... The first dataset, where we were like, yeah, we need compositionality for this, and hierarchy. And

JHawkins: Yeah.

Viviane Clay: Now, the idea was, okay, the dataset already includes stroke information, so we give it each.

JHawkins: Yeah.

Viviane Clay: individually, and then I can learn the arrangement of them.

JHawkins: I remember thinking about this when I first saw this in the write-up prior to the retreat. And I said to myself, oh yeah, how would I learn these letters? And I realized that I would... I would personally imagine how I would draw them, that I didn't recognize them as images, I recognized them. I personally, even though I didn't know my idea anything about these, and I didn't have to see this colored picture you showed me here, that... that I would... I would... that's how I would tease it apart. It's like when I tried to, spend some time looking at, Chinese, glyphs, and that's why I have to do that, too. I have to imagine, oh, there's these two strokes here, and there's a stroke here, and that's how I... that... that's how you would just... not only hanging about them, that's how I would try to recognize them. So I agree, it brings in the motor component of it.

Niels Leadholm: Yeah, and I don't know if you remember that from the present, or, like, when we last talked about it, but that's one of the other cool things about the data today, is they've... they've actually stored that, or recorded the motor sequence as well.

JHawkins: You can see that in the colored images here, right? yeah, so this...

Niels Leadholm: The order in which they do it, but it also is oh, the stroke starts here, and then goes there, and they have, Each pixel as a function of time, basically.

JHawkins: I know.

Niels Leadholm: So it's... there's a lot of really nice features about this dataset, and so I... I think we'll return to it, at some point. So I thought it was worth just talking a bit about some of the kind of thornier things about it, One of those is how we would deal with the low-level strokes.

And in particular, there's a few issues, One is, Yeah, because it's not native speakers, or of the languages, they don't draw them in a particularly normal way, I think the example Vivian often gives is, B is sometimes drawn, a straight line like this, and then, almost, halfway up is the sort of semicircle, as opposed to at the bottom. Or, there were some other weird examples where people would do, an English letter as, a single stroke and stuff. even just this K, and this G, you can see looked pretty weird. They may have also been trying to draw it with a trackpad, I don't know.

But, anyways, but concretely, that also manifests as, the... the order in which these, the strokes are laid down is different, and that affects, according to OmniGlot, what the sort of label is for each stroke. If we were going to naively use this. So as in, green would be the first stroke, but you can see... In different examples, different strokes are green.

Viviane Clay: Even if we use that as a label, it's problematic. if you think of the age, the two vertical bars are basically the same thing. We don't give them different labels.

Niels Leadholm: Exactly. So that's the other issue. And then, not only are the vertical bars the same, but what about a vertical bar that's rotated. Is that a different object?

yeah.

Viviane Clay: I don't know. I think we would basically have to do unsupervised learning at the lowest level and have Monty figure out, what unique strokes are.

Niels Leadholm: Yeah.

JHawkins: But you don't want to use that, temporal information. that seems to be... It's funny, I did a lot of this when I was working on the hands-up computing stuff, right? And that makes it so much easier if you know the order in which the things are drawn. But when you're reading it, you don't have that information. You do... you can, when I look at these things, even if I didn't know the order in which the strokes are drawn, I would... I would tease apart the different strokes. I can see that, in this case here, there's a cross, there's a down, Stroke that goes to the right, and then there's the cross, and then there's a loopy one. And, I would... I would break down into those components on my own. without any additional information. And it's interesting, how would I do that? I guess there's some sort of assumption on my part that lines are drawn in continuous flows, and so I can see where lines start and end. And so I would just break this into 3... that little character is into three components. And the order in which they're drawn, and the order in which... the order in which the strokes are drawn, and the order in which the bit... what end you started, it shouldn't really matter. That's cheating, if you know that information. But, visually, I could just piece apart this thing and say, oh yeah, this is a character that's drawn of three strokes. The strokes are roughly these shapes. And somehow I would... it seems like I would make that a compositional object of 3 child objects, which are crudely written, but there's still 3 child objects. To make this thing up.

Viviane Clay: Yeah, that's the general idea that we were... thinking of, but I guess, yeah, the kind of low-level question would be, like, when you see an age. Do you, at the lower level, say that's 3 straight lines at different orientations and locations? Or do you say.

JHawkins: I think...

Viviane Clay: This is stroke 2, this is stroke 3.

JHawkins: I would think it's two straight lines, 3 straight lines of different oriented. that's the way to do it.

Viviane Clay: Yeah. So then, in that case, it's, we either have to... Create a new labeled dataset of the basic stroke types, like curves and straight lines and stuff, and train the lowest level on that. Or we have to do unsupervised learning. Where Monty has to figure out that those are two straight lines at different orientations.

JHawkins: it's funny because, I come in with some prior knowledge about drawing lines. when I look at those things, and so I... there's a prior knowledge that the pens have to, they don't change direction too much.

Viviane Clay: Yeah, your lower level learning module is already trained.

JHawkins: But it's interesting, how did I... how did I learn that? I learned that through mode or behavior, not through just visual. I think I learned that, I looked at that, and I said, oh, where did the pen go? It went around like this, and around like this. I don't, look at it and go.

Niels Leadholm: It's at, When we talked about, like, how you recognize stuff based on affordance, you mentally imagine yourself sitting on something. It's almost like you mentally imagine yourself Writing in some of these things.

JHawkins: Yeah, No, isn't it? Let's go back to that one particular character you had there. now that I'm thinking about it, it's... I... there's 3 strokes, right? And 2 of them, I recognize immediately. I know those strokes. I... I don't have to train on them. This is the one that goes down to the... and then across. In fact, I might sometimes look at it and say, oh, that's just a T. I have, a T like that, so I can maximize just two strokes as one thing? Or I could recognize those as two, a horizontal stroke and a hooked stroke, which I... those are things I already know. The other one is unfamiliar to me. And I had to mentally trace it out. To see what it is.

Niels Leadholm: I'm guessing you started here? Every time?

JHawkins: no, I actually... I actually started on the other end. Surprisingly, I started at the end that was the most visible. I started the... and that first character. The most clearly endpoint is the one on the bottom

Niels Leadholm: Are you lefty?

JHawkins: Standard. No, I'm right-handed, but the point is, I didn't ask myself how... I didn't ask myself how would I draw it.

Niels Leadholm: Okay.

JHawkins: I asked... I had to trace it out mentally where it was, and so one end of that line is clearly marked. It's the one that's all by itself on this particular image of the upper left-hand corner. It's clearly the one... the free end is the one that's on the bottom The character below that is similar. The one in the first row, second from the left. That's not the case. In that case. if you took away the color, it almost looks like it's one stroke that goes... down, around, and up again, and so that almost... if I just saw that, I would assume it was two strokes in that character. So only after looking at several of these did I say, oh, it's three. But really, I'm trying to do is I'm trying to segment out the different strokes. And then I would imagine how I would draw it, or figure out some kind of description for it. That... it's an interesting one, because that... that loopy thing is... there's nothing like that in... in the printed English letters that I can think of. Yeah, excitement.

Hojae Lee: So rotating G. Yeah, sideways line, rotator G.

JHawkins: Yeah, but, okay, but I didn't see it that way. Because it's sideways.

And I don't draw G that way anyway, I draw G where I... a different way. I don't know, I'm just... I think what... I think, mentally, I had... if I take that first... I saw 3 strokes in this... looking at this data set. 2 were familiar to me. And a third one wasn't, and the third one was the one I had to trace. First one, I didn't really have to trace, because I already recognized them. And I have to spend time trying to learn that funny little pattern of the third stroke. I'm looking at it over and over again, saying, how would I... how would I work? Okay, oh, okay.

Niels Leadholm: Yeah.

JHawkins: These are observations. These are complications of using this dataset. Yeah.

Niels Leadholm: But I think it would be a nice long-term one to revisit, because, yeah, again, with all the action stuff, it would... it would fit nicely with temporal, adding in time, and it would also fit nicely with eventually having action outputs where, we could get Monty to draw new examples of these letters and things like that.

JHawkins: Yeah, I think that... but I don't think it's a good one right now if we're just trying to get accomplished or something.

Niels Leadholm: Yeah.

Hojae Lee: Actually, this just reminded me, I think, I'm not sure, but I think there are some Chinese characters where, a character is made up of other characters, that one can stand on its own. But then, it's written smaller, in, a particular square area, there's other stuff, and that it changes, it's a different... Lord, or something like that? Yeah.

Niels Leadholm: Sounds right, I think, yeah.

JHawkins: Do you read Hongo?

Hojae Lee: I can read Korean, yeah, but...

JHawkins: Isn't that Hongo? Isn't what that Korean?

Hojae Lee: Yeah, that is Hangul, yeah.

JHawkins: But that's not true.

Hojae Lee: Chinese.

JHawkins: I know, so I was gonna ask you. Did they have the similar thing in the Korean language? Were those.

Hojae Lee: Yes, that... yeah, you can add in other characters to... In the same kind of... let's say you're writing, a a single character word in a box, you can add in multiple things, and that will be, like, a different word. But if you have, take one character out. Yeah, so the same components are there, but there might be...

Niels Leadholm: But yeah, you wouldn't have... you wouldn't have, a whole character within a character in Hongo, would you?

Hojae Lee: No. They're usually arranged side by side, but they take up the same kind of monospace.

JHawkins: I was just running it, some of the subsets, are they words themselves? Did they do the same thing? No,

Hojae Lee: no. they're more like vowels and, consonants. It's just that they're... yeah.

JHawkins: Arranged in a box.

Hojae Lee: Yeah, arranging the box, yes.

Niels Leadholm: Isn't that kind of, it con... or, has an effect on the language, because, you always need, 3 or 4 things in a box, which means that you pretty much always finish with a consonant, or... I think...

Hojae Lee: yeah.

Niels Leadholm: And, Yeah, whereas in English, you just have, a random... a word might just suddenly stop with a vowel. But. But I think there's some languages where you can't have that, because it's no, because then the box isn't complete.

JHawkins: Interesting. Tristan's phone: we don't... we don't have to go... too far out of our alphabet, so any accented language, right? with an A, with apostrophe atop of it. that contains an A, A within a posture.

Hojae Lee: contains an entire character of A. Tristan's phone: And in some languages, like in Polish, you have O, and if you put O with an accent on top of it, it's U. So it's a completely different sound, right? Or, even in English. I is like an L with a dot on top of it, right? So we don't have to go too far with seeing...

JHawkins: Cool. Tristan's phone: positional characters.

JHawkins: Yeah.

Niels Leadholm: Yeah, and I feel like, yeah, the letters with accents, those are maybe good examples of these, state ones, where it's you don't want to relearn the letter A, you don't want to relearn the mug when you're learning the TPB mug. But you... Yeah, it's it's related, but.

JHawkins: Different life. In many languages, you've got A's of different... there's half a dozen different accents you can put above it, and But they're all A's. And you type them that way, too, right? You basically type the A, and then you add the accent.

Ramy Mounir: In Arabic, they have dots, so basically, same letter, if it has two dots on top of it, or three dots, that's a completely different letter. But it's the same thing, it's just the number of dots on top of it, or below it.

JHawkins: Have you typed that on a keyboard? How do they do that? Do they type the letter and then add the dots, or is it...

Hojae Lee: I think if you...

Ramy Mounir: Oh, it's just a different theater.

Hojae Lee: Swish.

Ramy Mounir: That's it.

Hojae Lee: Okay.

Ramy Mounir: hate the devs.

JHawkins: I missed all that, but...

Hojae Lee: Oh, sorry, go ahead.

Ramy Mounir: That's just saying, So it's, a completely different letter.

JHawkins: Interesting. Because, if, in French, I think, I actually don't know. I have to take this back. When I've done it, you type the letter, and you add the accent. But then I wasn't using a French keyboard,

Viviane Clay: Yeah, in German, you have letters with dots on them, and in the German keyboard, you have extra keys for those letters. And then... but then... so in those cases, I think of them as different letters. But then, for example, in Greek, you use the accent to just say which part of the word just has the emphasis on it, like, how you pronounce it. And in that case, I just think of the accent as a modifier, and I don't think of the letters as being a different type of letter. it's still an A, it's just this A has the modifier on it for a different pronunciation. Versus the A with dots in German is a different letter to me.

Niels Leadholm: Yeah, I wonder how much it's to do with, familiarity, because I'm similar with, Danish, the O with the slash through it, I, again, think of as, a totally different letter. But French, which I don't speak very well, I would say, oh, it's... no, it's still an A, it's still an E, it just has an accent on it. But maybe someone who's native French would be like, no, that's... that's a different letter.

JHawkins: I was wondering about that with Vivian, because I think German was your native language, right? And I don't know how good your Greek is.

Viviane Clay: Yeah. I didn't know he spoke rich. Bro.

JHawkins: Debbie just...

Viviane Clay: Not sure you can say that, trying to learn, but yeah...

JHawkins: Okay, so then, Celeste, Niels was...

Viviane Clay: Yeah,

JHawkins: Is that...

Viviane Clay: Yeah, maybe it's familiarity, but it also seems like... The letters are pronounced the same way, it's just, pronounced stronger, that syllable is pronounced stronger, and it's the same effect on all of the letters, like... accent on an A or E or whatever, but then in German. Different letters with dots on them get different pronunciations.

Niels Leadholm: Yeah, and it's like a... if it's similar, then it's it's always the different pronunciation.

Viviane Clay: Yeah.

Hojae Lee: But does that change the meaning of the word? for example, I have I don't know, ABC, but then if you put an accident, you say, put an emphasis that's a... Somehow, the pronunciation of the word, actually.

Viviane Clay: Yeah, there are words that are, like, in Greek, they are exactly the same, two words are exactly the same, they have two A's in them, and depending which A has the emphasis on it, it means a different thing.

Hojae Lee: Okay.

Viviane Clay: Alright, we're getting far afield here.

Hojae Lee: Yeah.

Niels Leadholm: For what it's worth, that was... that was the last thing, I wanted...

JHawkins: I think the... it seems to me the Omnigot one is problematic still, I'm not sure.

Niels Leadholm: Yeah, maybe we have another discussion about it before we tackle it, if there comes a day when we...

Scott Knudstrup: Yeah.

JHawkins: Yeah. It seems something would be better once we have the whole system working with sensory motor and behaviors and stuff. Okay, now it treats the system the right stuff and the right. It seems there's implicit knowledge about how the strokes... I rely on knowledge about how strokes are drawn.

To tease apart those different strokes, to know that, oh, that's just one stroke, and that's another stroke. it's not just a bit pattern. if it was just a bit pattern, I'd be lost.

Viviane Clay: what I wrote down as takeaways for maybe the shorter term is for the benchmark test that we have right now, see about making a config where we Only train the lower-level learning module first, and then the high-level learning module, even when it learns the individual objects, like just the cup, still gets input from the lower-level module about the child object, so it just associates Merck on Merck. And then maybe looking into voting earlier than planned, seeing about how... if we can get it better, if we have, several lower-level learning modules that can infer the child object faster.

Niels Leadholm: Yeah.

JHawkins: Or just hardcore that for now.

Niels Leadholm: I'm sorry.

JHawkins: And you could just hard-code that, too, for starting.

Viviane Clay: Yeah, I guess that'll be a bit harder, because we don't really know what it's looking at. we don't... Have an easy way to tell whether it's looking at the logo or at the mug. Except... we can do, very hacky things, if it looks at those colors, it's the logo, and if it's looking at those colors, it's the mug, but...

JHawkins: Don't trust it.

Niels Leadholm: But yeah, I think, yeah, it could be interesting to add in the voting and yeah, see how it does. Yeah, also maybe the... adding the other forms of prediction error, like breaking down prediction error into, more granular ones could be interesting as well.

Viviane Clay: Yeah, on that, I was also thinking there might be some other, additional metrics, after a high prediction error, how fast does it go down, or weighing prediction error towards the end of the episode higher than at the beginning. Kind of things.

Niels Leadholm: Yeah.

Viviane Clay: Oh yeah, then one other thing that, that's not immediate, but maybe to keep in mind, some way to only learn when things are unexpected.

Yeah.

Niels Leadholm: Cool.