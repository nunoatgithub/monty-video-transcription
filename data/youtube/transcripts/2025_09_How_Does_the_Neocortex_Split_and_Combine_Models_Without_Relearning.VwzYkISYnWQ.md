Niels Leadholm: So yeah, the question, how do we represent, multiple objects When we start learning variations of familiar ones, or, as you mentioned in the document. Suddenly, you have a subpart of an object, like the stapler top.

JHawkins: Yeah.

Niels Leadholm: But yeah, I don't know, do you want to start?

JHawkins: I can just, yeah, I can just start walking through that, this is a topic that was, like, really confusing for me. Yeah, and I worked on it last week, I don't remember, we were exchanging some messages on Slack. And, just felt, lost thinking about it. then I said, I'll just sit down and hunker down and try to come up with some ideas, and so I worked on it the last couple days. And it ended up pretty... something pretty simple, so I'm not sure what I'm missing. But it's not a complete idea either. It's just, at least it's... it's a grounding in which to build upon. So I wrote that up, some of you may have seen that. I put it in Slack, I can share my screen and bring it up, just walk through it, if that's okay.

Niels Leadholm: Yeah, sounds great.

JHawkins: Okay, I'm now sharing, and I want to bring up Slack. And I don't know if it's been the document I posted in Slack. Let's open the research pane. This guy here.

Alright, did everyone see that?

Scott Knudstrup: Yep.

JHawkins: How do I... how do I get rid of this? There are shares of that crazy thing coming up. Okay.

I just started wandering the wilderness, thinking about all the things we've been doing, and trying to make some sense of it all, and we have all these variations on models that we've come up with. Since the original idea was like, hey, there's a reference frame, and there's a location, and you have a sense, and you put some information at some location in the reference frame. Hey, isn't that wonderful? And then it gets really complicated. we've talked about morphology versus features, and I don't think we've ever completely resolved all that. But the idea that there's... you can build models that are just... you can recognize things just on the orientation, or the edges of models. And then we've done a lot of work on compositional structure. We've done a lot of work on object behaviors, which we've now broken into sort of separate models. And then we've had this whole classification, this whole area of classes of objects, which I think, Niels, you might have been the first one to bring up, but we never really resolved all those either. And so those are... those are variations of objects that are similar.

And if I see a, a new class of an object, it inherits some properties from previous objects in that class.

so there was a common theme over this, is that, that we end up to splitting models. I use the word splitting, I don't know if that's the word you guys use up again, where we have a model, and then we have to create a new variation of it. We want to maintain a lot of the properties of the first model, but have a new model. And the more important thing is we can't relearn everything every time we form a new variation, whether, a new... any variation, And then we first got into this in a big way with the stapler. Which we have a lot of good figures, which I'm not showing here, but how do we learn that if we never saw the stapler open, then we see it open, then how do we model the different parts of the stapler when before they were the same? hopefully you all remember that. And then at that point was, we're running into similar problems with the, with... with composition. And there's two ways the composition problem works. There's, a feed-forward way and a feedback way. The stapler was a feedback way, in some sense, and it's I start with an object, I'm splitting it into components. Child objects. And the other way, the feed-forward way, you might think of it as I take two objects, and I'm going to create a new object that I didn't have before. So one, you're building new things, and one is you're putting something apart. I also wrote here, the problem I saw, we had this basic idea.

Let me just see what... I'm reading my text here.

So when we talked about the mug and the logo, right here.

we had this idea, oh, how do I know I have a mug and I have a mug with a logo? And we said, we might have some state variable, which says, oh, this is a regular mug. Oh, no, this is the one with the logo. And then, internal to the model, we could say, oh, if I know the state variable says there's a logo, I make one set of predictions, and if it's one without the logo, I make a different set of predictions, but other than that, they're the same. But this doesn't work if there's a lot of variations of the other things, just this one thing, like a logo, yes, but I came up with lots of variations where You could have multiple things. I could have mugs with logos and without logos. I could have mugs that are tall, and mugs are short. Some could have logos, some could have no logos, and so on. And so a single state variable wouldn't work, and we can't have lots of state variables in a column. There's just no... it's not possible.

and then we also.

Niels Leadholm: When you say we can't have single state variables in a column, as in...

JHawkins: I don't have many state variables in a column. We could have one. if I have... if I have... if I say, okay, mugs come in, tall, short, green and red. the blue lips, or no blue lips, with the mental logo, or with a Thousand Brains logo, and I can have any one of those flavors. then a single state variable does not suffice. I have to have a state variable for each of those particular variations. And, So I'd have to be able to say, oh, this mug is the red one and a logo, and I can make predictions about that. Or this one's the green one without the logo, and I can make predictions about that. the idea that there'd be a set of cells within a column, I'd have, I... if I have a size themselves to represent a particular variable. I can't mix them, I'd have to have separate sets of cells for those. otherwise you get back into this, mixing of SDRs anyway, so it just felt... Okay.

Niels Leadholm: Yeah.

JHawkins: And then I came up with another example. Bum... this one down here. Did I answer your question, Neil, sufficiently, or do you.

Niels Leadholm: yeah, I think we'll get to it later in terms of the top-down feedback stuff, but it feels to me like you could have a single population that represents multiple different

JHawkins: Good, but then...

Niels Leadholm: And then there's some limitation to how much superposition of those states you could have. But.

JHawkins: it's not a... it's not a general, solution either, because as we saw with the stapler. there was information that had to come from the R2 to tell the R1 how to divide the object into two parts. So in the case of the staper top and the bottom, we saw that there had to be a signal from another learning module. Tying, so that was an example where, internally, you wouldn't have enough information to know that the stapler should be broken into the two parts. Somebody has.

Niels Leadholm: Totally.

JHawkins: And then... then I gave up this example here, where I started thinking about time. And, where, you can have a temporary arrangement of features, that's the thing, imagine the mugs on a table. And you want to remember where it was last time you saw it on the tables. That's a temporary compositional object. Our mechanism should work for that. But then I realized, oh, but I might remember where it was this morning or yesterday. And so I have the same basic components in a different arrangement. And I have a model of that, too, so the only difference between those two is time. And I don't... I don't expect that time variable to be located within the column. And then I said, what if every day of the week the mug was on a different portion of the table? And so that day of the week would be the variable that, I would use to make the correct prediction about where the mug is. And that, too, is not something I would expect to be in the column representing mugs or tables. So there's... so there could be some variables in... within a column, within the learning module. But clearly, that's not the general case. The general case, I have to have signals coming from elsewhere. that these are... there's examples, many examples of signals coming from elsewhere that would tell me how to different, what... which model should I be invoking right now? Is it the model where the... where the cup's in the middle of the table? Is the model cups on the one corner? is this... is this the... that kind of thing. So I... I just went and assumed... I went all full on this. I said, how about I just assume that... that it's always an external state variable. That could be wrong. But if I have extra... if I assume there's external state variables, then I can have as many as I want, because they can be coming from different places, thus broadcast broadly in the cortex. some could be broadcasting times, some could be broadcasting a day of the week, some of it could be... under any context, I might say, oh, when I'm in the living room, the mug is always on this corner of the table. When I'm in the In the dining room, it's on this other corner of the table, that kind of thing. So there could be almost an unlimited variety of contexts in which you'd make different predictions on the same objects, or similar objects. It just felt like that to me.

Viviane Clay: Yeah, and that would match with the... The way we talked before about how a state could be this broader Layer 1 input that gives context and basically conditions which features to expect at what locations, but while still using the same reference frame in Layer 6.

JHawkins: So maybe I came right back to where we were before, but it certainly wasn't obvious to me in the beginning, as I started going through this. I got clarity going through those examples. before I came to a simple conclusion, did you have something else you want to say?

Viviane Clay: I can bring it up later.

JHawkins: Then I also thought about classes of objects. This is something that... It bothers me every time I bring it up, because I really have no idea about it. And... and we never really resolved, what's a, what makes a class, and how would I differ, how do I know when a class, and how do I... and then I said to myself, if I have an if I have... let's say... let's just jump right into it and say, what if... what if my reference frame anchoring, that is, the reference frames are anchored That is the class. And I can have as many variations on that as I want. And as long as I've anchor the same way, then it's the class of objects. That class of object could consist of one object, so I could say, oh, I'm in this room, and that's, I've anchored to this room. Or I could say, oh, I'm in a room let's... I'm in a kitchen, and... or, that's a class of objects, and therefore I have some... I have a bunch of different kitchens I know, and... but they're all anchored the same way, that kind of thing, so I... it's not all rooms would be unique. It would be, like, if there's nothing common, I would say, yeah, this is the class of other... I had before. this idea that you essentially say, okay, the definition of a class is a particular anchoring of the reference frame. I may have one or many specific models in that class. Those models actually don't even have to have anything in common. I could still say they're in the same class. I always used to think it's funny how, when we start to think of what's a fruit. And then you tell the child thinks of all the things that they think are fruit, and then you tell them a tomato's a fruit, and they say, wow, that doesn't look like a fruit. And yeah, it is, technically it's a fruit, so you can... you can say a tomato's a fruit in the same class, maybe. But, That's a... that's a stretch example, but my point was, if you just take this idea, once you say an anchor of a reference frame is a class. than anything. You can have any kind of models in there that overlap or don't overlap a lot, or just have slight changes or not. It doesn't really matter. There could be lots of different variations of things that's in that class. I don't know if that works, but that's the way I was thinking about it.

Viviane Clay: Yeah, I like that general idea a lot, actually. But I was wondering... So when you create a new state of that particular object. can you still reuse the data that's stored from a different state? for example, I've learned the mug without the logo, and then I create a different state of mug, which is mug with logo. Can that model, if it basically doesn't store things for the locations where, I don't know, the handle is, go back to...

JHawkins: I think the way I look at it is at any particular location, there is something stored. And... and then sometimes you can, under different states, you can store different things at that location. I can have a very small change, and everything else is the same, right? I can say, oh, this is the... this is the mug that has the nick in the corner, the little crack in the corner. And okay, so everything else is the same, but when I get to that location on this one. I'll make a prediction that's different, and only in that location.

Viviane Clay: Yeah, so it's more there's a default, and then the state can change specific parts that are different in that stage. Oh, yeah.

JHawkins: The default assumptions, you, You keep everything until you start adding something else. I thought about this with the stapler. I mentioned it in here, so I don't have no good figures for this. You just have to listen to me rambling. When I thought it was a statement, we used to... we would draw the staple sometimes as it was just a big rectangular box. And featureless, and you couldn't even see the seam, and then it opens up, and voila Now you see that it's two parts.

I was imagining, like, when you open it up, then sometimes you see things you didn't see before. there's... there's new features you can see under the bottom of the top, and there's new features you can see under the top or the bottom, and so you'd want to add those features to, to those models. So you'd start out... absorbing all the things you had before, the staple top is still the staple... is still this... these features in this area of the model, and now I can add new features to the... only to the staple top, and I can add new features only to the staple bottom. That's actually...

Viviane Clay: Yeah, I was wondering if this... If it makes sense to apply the same mechanism to the stapler, because it seems like... it seems fundamentally different, I wouldn't say the top and the bottom are two different states of the stapler. I would say, like, where the top and the bottom are relative to each other are different states of the stapler.

JHawkins: I wouldn't say the treatment states. Imagine I say they're different, they're all in the class of stapler. the stapler could be a complete stapler, or it could be a stapler at top, or it could be a stapler at the bottom. But in my definition, I would say all... they're all... In the class of Stapler. Using the word state is a little misleading. That's a... right?

Viviane Clay: I guess? Yeah, the thing that feels weird about that to me is that... As you see the whole stapler, you perceive both parts, so you're basically perceiving both states at the same time, if the top and the bottom are two different states of the stapler.

JHawkins: but I wrote in here someplace. I don't know where I wrote it in here. Here we go, this paragraph here, I think. Whoops, is it getting rich talking?

Viviane Clay: And especially if they share the same reference frame, then that's odd if the bottom of the stapler is not rotating.

JHawkins: So I... here's... here's what I said, suggested this. I said, you might, No, this is not the paragraph. Where did I say this? Oh, right here.

I said, you might... you might have 3 models of the stapler in R1. You have the original one. And then you have the one that says, oh, we're paying attention to the top, and you have another one that says, oh, we're paying attention to the bottom. And I... I don't... I didn't see why the original complete model would go away.

Viviane Clay: Yeah, everyone.

JHawkins: Does that still bother you?

Viviane Clay: Yeah, that sentence I would agree with, I would think of it as R1 having three models of the stapler, but I wouldn't think of them as being... 3 states of the same model that share the same reference frame, because.

JHawkins: Oh, I like...

Viviane Clay: independently, and, one...

JHawkins: My pleasure.

Viviane Clay: rotating...

JHawkins: They're not the same model. There's 3 models, but they have a shared reference frame. So they're all in the class of stapler. In fact, if I asked you to identify one, you'd immediately identify any... any one of those three models. If I just saw the top or the bottom, you'd say it's just... it's part of a stapler, right? So you know it's... So what's the...

Viviane Clay: If they're sharing a reference frame, and you're perceiving them both at the same time, how can... The top part be rotating, while the bottom part is not moving.

JHawkins: But then you wouldn't, then you'd only be... then you'd only be perceiving the top or the bottom. That column would be?

Niels Leadholm: Yeah, it's interesting, I... Yeah.

JHawkins: Yeah, R1 would be... you'd be attending to the top, and R1 would... In some way, I don't know yet. The context would tell it that we're just dealing with the top model. And pay no attention to the bottom model right now.

Viviane Clay: Yeah, I guess I was thinking of, the kind of child object segmentation, as you see the move, as being maybe a different type of process, where you have originally learned the full stapler model, and then as you see them moving. some of the parts, the model isn't predictive of anymore. So let's say it has anchored to the stapler top. and so the reference frame is rotating with the stapler top. It stops being predictive of the bottom features, and so it slowly forgets about those. And then they might be.

JHawkins: wait, why do you say it slowly forgets about him? It's not gonna forget. It's just the context says we're not paying attention to that model right now. The context, by the way, one thing I didn't say here is that the Stapler example gave us that it wasn't... there was this idea also that the context would occlude some parts. We required that in the staple example. That the context was not just, oh, we're stapled atop, but the context says. There was a contact that says, only pay attention to this part of the model. Yeah.

Niels Leadholm: for what it's worth, I had a similar thought when I was reading this, that... specifically for the stapler subdivision part, that feels like a different mechanism, and I feel like part of it is just how fast it happens. That it's as soon as you see something moving, independent of other things, you can segment that out. And it feels like that happens almost to, the whole object, which kind of fits with I guess what we've talked about before, the kind of Type stuff.

JHawkins: Yeah, but I can't...

Niels Leadholm: It feels like when you're learning this new stuff. That's more you attend, then you learn a point of new information. with that context in the middle. Then you attend, you learn another new point of information, oh, okay. There's another logo here.

JHawkins: I'm missing this distinction that both of you see. I have the... I'm a R1, I have a model of the staple. And now, Stabletop's moving. Our assumption before. was that a signal from R2 Points out that, hey, there's a subset that's moving here. And it's a... that... and it's... it... there had to be some sort of, Signal that says, attend to this area of your model, and don't attend to the rest.

Viviane Clay: Yeah.

JHawkins: And that... that, to me, is... is... is either... it's part of the context that's being provided to R1, it may be the entire context that's being provided to R1. It's interesting to think that the context may be thought of as an occlusion area, or an area of attention, I don't know. But anyway... It's at least part of the context. in that case, As soon as we do that. we have the ability... we have to be able to add new features to the stapler top that we didn't see before, so I have... I have to have a new model that I'm building at that point.

Ramy Mounir: I have a question. Sometimes a child object needs to be, part of two different classes of objects, like a table leg, or a... it could be part of, a table, or a chair, or something like that. Does that mean, for that leg, we would, learn two objects? Because they have to anchor differently now?

JHawkins: That's a good question. Yeah.

That's interesting to think about.

Viviane Clay: Yeah, I think that's another good point. I don't know, to me, I'm still on board with the, temporary masking and all that, it just doesn't feel like it's a different state of the same object. It seems like maybe at first it is exactly the same object, and we're just applying a temporary mask, but it seems... it's a different problem to segment an object into child objects versus having an object and different variations of it,

JHawkins: it may feel that way, but let's just walk through it. on the one hand, we know that we have to keep the features in the same reference frame For the top of the stapler, because otherwise we wouldn't be able to make predictions about it. So even though I'm... I'm... I'm isolating the top of the stapler. I have to maintain the original model, right? that has to be there. And now... now I need to be able to add new features to that model that only attain to that subset.

And it seems to me I have to maintain the same reference frame, I have to be able to differentiate it from other instances of models in that reference frame. And, I've just stated some, what I consider. Points of fact, or at least statements of... making. And That feels to me the same. How's that feel different to you? I don't...

Niels Leadholm: Yo, or...

Hojae Lee: Can I give a different example instead of Stapler? Sapler...

JHawkins: Should I stop, excuse me, should I stop sharing my screen? I don't know if it's helpful to have me.

Niels Leadholm: Sure, yeah, we can always come back to the document.

Hojae Lee: Yeah, maybe, bicycle? if we, like... stabler top and stabler bottom feels like it belongs to the model stapler. But for a bicycle, if we segment out, for example, everything except for the wheel. I wouldn't say we all is... it all feels like a different model from.

JHawkins: I think it is, in fact.

Hojae Lee: Reference?

JHawkins: I do, I think you're right, because if I... if I see a bicycle the first time. I don't know why, but it feels like I would not think of this as, monolithic thing. I would look at the... I would look at each component and try to And try to understand what it is, or... and I probably have seen wheels before, and I might have seen pedals before, and things like that. That, to me, is... It's more like the mug and the coffee cup, where we're taking individual things we already recognize and building something new. But the thing with the stapler, Jose, we were able to imagine a stapler looking just like a rectilinear box with no delineation, and all of a sudden, magically, it separates, and now you see things. So there's no way in advance to know that there's two parts. With a bicycle, it doesn't feel that way to me. I would... I wouldn't learn the bicycle, one thing. It would always be multiple things to start with.

Viviane Clay: But I'm not... I'm not sure... you usually see the full bicycle before you see all of the parts of it. Individually.

JHawkins: Yeah, but the way... the way I I think normally what happens... is when I see something I don't recognize. I immediately try to... I keep narrowing down my attentional focus until there's a part I do recognize.

I always do that, if I never saw... I see something, I don't know what it is, a new kitchen gadget or something, I will then keep attending until there's a, oh, here's a blade, or here's a screw, or here's a handle, I always keep... and then I start building up a compositional structure. The staple example is different, because we can imagine the basic staple having no differentiating components. It was just a box. But that's not the case, usually. Usually, I think we would... if I see a new word, I don't learn the whole word. I go down and look at each individual letter, and if I don't recognize the letter, I'll look at the features of the letter or something. So you think a bicycles more like that. You wouldn't learn the whole thing. You keep attending until you find something you do recognize, something basic. And then... and then another, and another, and you build it up compositionally.

Viviane Clay: But it still seems, Generally, we would want child objects to be their own. objects, and then be composed into a parent object, instead of child objects being different states of the parent object.

JHawkins: No, I agree. That's what I'm saying, that's what would happen. In the bicycle example, all the components of the bicycle would have their own reference frame, and then we'd be building a compositional object from them. we're going in a forward... feed-forward direction. We're saying, oh, we have all these... these individual models, now we're going to build a compositional model, that... that it's basically positioning all these child objects, relative to each other. That's why I was trying to make this distinction between fee-forward and feedback, where the stapler, we had something we thought was un... we didn't realize could be divided at all, and then it got divided, and we had to figure out what was going on there. And... and that's a... it's, in some sense, a different... It's a different problem or a different solution. yeah, I agree, all parts of the bicycle would have their own independent reference frame, because they're all independent components that you would have learned separately.

Viviane Clay: And then maybe the stapler is more of an edge case that doesn't really use the mechanism we want to be using, or maybe it would require having to relearn individual models of the.

JHawkins: Maybe, I don't think.

Niels Leadholm: or is it a short versus long-term thing? yeah, initially you developed this child object representation.

Whether there's a contact signal or not, it's still, taking a... Full model, and just looking at parts of it.

JHawkins: that's interesting.

Niels Leadholm: I think that could happen with, anything, even a, you could have a new tropical fruit you've never seen before. you learn a model of that just by looking at it. Then someone slices it in half. Now you see the new insides of it, and also half of it has been taken away, and Suddenly, you have this half of an object. That you can instant... almost instantly perceive as this... You still think, oh, that's that fruit now cut in half.

JHawkins: it's or if I see the top or the bottom of the staple, I still say it's a stapler. If I see... a wheel, I don't say it's a bicycle. I said, it's real. And it could be on lots of different things. It could be on a little trailer, or the... It suggests it might be on a bicycle, but I don't say, oh, that's a part of a bicycle. That's real.

Viviane Clay: I wouldn't say that the bottom of the stapler is a stapler. I would also say it's the bottom of a stapler.

JHawkins: But... but... but it's... but it... it isn't anything else. It's... it's not part.

Niels Leadholm: That's maybe the intersection of the state variable or state representation with the reference frame. is okay, that's bottom of Stapler.

JHawkins: I didn't follow your comment.

Niels Leadholm: As in, yeah, I agree, it's something you can uniquely define, but it's... maybe that unique definition is the intersection of the state representation with the reference frame. That's what makes it the bottom of the stapler, or the top of the stapler. As opposed to, you're not saying, someone doesn't give you the bottom of the stapler, and you say, this is an entire stapler.

JHawkins: No, you don't.

Niels Leadholm: But it's still grounded in your representation of Stapler.

JHawkins: If all I could see was... maybe I was looking through a straw, and all I could see was some features, or on the bottom, I'd say, oh, that's a stapler, and then I see... and then I see a feature which is only exposed when the stapler is open. Then I say, oh, that's the bottom of the stapler, and the stapler is open. or the top of the... then I would switch to the context of, I'm only looking at the bottom part. I think it works out well. I don't see this as an important distinction. I can see... where it's coming from. Essentially, it's possible... I think you captured on different words that I would use. if I take something that I know is one object, and I divide it into multiple pieces, those multiple pieces are still classes or parts of that object. they're not something else. It's not like a stapler bottom doesn't appear on my bicycle. I could try to make that happen, but... It's still this part of Stapler. And so there's a... that's where you're going... that's the feedback one, where you're taking something that you know is one thing, and you realize that there's independent parts of it that you didn't realize, but that assumption there is that they're all still part of that... they're all still stapler parts. They're not, like, all of a sudden completely different objects. And you would immediately classify any one of them as part of a stapler. Whereas, if you go in the forward direction, I have a logo, and I have a mug. I now create a new, I now take the mug, and I say, oh, under certain contexts, there's a logo here, in certain contexts, there's not. They... the logo and the mug are not part of the same class. They don't share reference frames, and And it's just different. But I think the same mech... the feedback and the feedforward are different, but the same concepts apply. I guess I'm trying to set up both of these at once.

Viviane Clay: But the first.

Niels Leadholm: Yeah, and maybe with long-term... Huh. Okay. I was gonna say, yeah, and then maybe with long-term, you would learn, a totally separate reference frame, particularly if you see that child object in different contexts. So you see wheels in different contexts, and then that's when you start I wouldn't be surprised if, when a child first sees a wheel on a bicycle, they understand that it's moving, it's this separate child object, but it's also it doesn't... it's not a concept that exists beyond bicycles.

JHawkins: Have you ever seen it.

Niels Leadholm: If they've only ever seen it in that context.

JHawkins: maybe.

I don't know, in reality, they would have seen wheels elsewhere, almost certainly. And, It's possible what you say is true, Niels, but it's also possible that children, children struggle with things initially in their life, understanding what they are, and it's possible also that They just really can't conceive of of a bicycle very well until they understand the components. It's it's like a... it's harder to... this goes back to the theory about how to learn... child learns to read. Should they learn to read by looking at whole words, or should they learn to read by looking at letters? And there's these, two schools of thought on this. I was brought up in the era when you learned ladders first, then you composed them with the words. But... That's the way I think about it. More oh, I'm not gonna really learn words until I know letters. And if I saw some pattern... but I could, under a different context, I could learn a whole word as a thing, and then later try to... try to separate out the letters.

Niels Leadholm: Yeah, I noticed when I was trying to learn, some Sanskrit. that I was simul... I was doing both. I would obviously try and learn the letters, and focus on the strokes and those, and then if I was learning a new word, I would try and Focus on each stroke to recognize the letter, and then recognize a series of letters to be like, oh yeah, that is the word. but I also had, a coarse model of the whole word. And I could often just match that, because it had, almost a shape, quote-unquote, that sort of looked familiar, and I was like, oh, that is the kind of shape of the word for man, and that's a word for woman.

JHawkins: We do that.

Niels Leadholm: So it feels both was happening at the same time.

JHawkins: And we do that in English, or any Western language like that, where, when you read, of course, you don't even see the letters, you just see the words, pretty much for the whole part, unless you get to a complicated word, and you might have to... one you don't know very well. But we don't look at letters. This is why people can swap out letters in the middle of sentence words, and you don't even notice it while you're reading it. As long as it has the right basic shape, and the words, the right length and so on, you won't even notice it changed anything.

I think these are just... I don't know, to me, these all fit into... this is the right conversation to have, I think. It's okay, sometimes we have to take things and break them apart. I'm arguing that when we break them apart. which is not the most common way we learn, then we have to... we break them apart, and we have these components to share a reference frame. If we're... mostly what we do is building compositional objects, where we take things we already know and bring them together, But we can do both, right? We can... then we can learn, as she said, learn the words as an entity, as opposed to just a compositional structure. I don't know what else to say about that.

Viviane Clay: Yeah, to me, it still seems odd to talk about components as different states of the parent object. Because, like, how do you know that the stapler bottom is not gonna show up in different objects the first time.

JHawkins: let's... first of all, we know that we can deduce that, initially, the stapler top and stapler bottom have to have the same reference name. If not, you wouldn't be able to recognize them, you wouldn't be able to make any predictions about them.

Viviane Clay: Yeah, but then why... it could just stick to the part that you keep following, and it just learns more about.

JHawkins: then, but then... then I said, oh, but as they become separate, then I can add new features independently to them. That was the point of saying, oh, I can now see under the stapler top, there's some extra things that I couldn't see before, and they become now added to that variation. First of all, I wouldn't say these are just states of the stapler. I'd say there's three models in the class of stapler.

There's a subtle distinction, but I think it's an important one.

Viviane Clay: It's not oh, there's a base model, and then there's flavors of it.

JHawkins: It's no, there's 3 models, because they all share the same reference frame, and... and let's say there's a context for all of them, and on the one context, we have a whole bunch of features. In other contexts, you have... some of them are shared, and some are new. In another context, other ones are shared, and some are new. I even put this in my little write-up. I said, when I'm learning something new. a new object from the start, should I assume that there's context for that? That is, when I learned a stapler for the first time, it's not like the stapler... it's not the whole stapler is somehow superior to the components. It's just another class of object in the same reference frame anchoring.

Niels Leadholm: I guess it's more parsimonious if you do... Assume, because that's the... topic earlier, it's more parsimonious if you do assume some kind of superiority by that being the original learned model. I have a model of a mug. And I just learned that. And then... That's... maybe there's some default context, but it doesn't really need to help predict anything. Because the reference frame can predict everything. It's almost... the context is just needed when you deviate from that, and so now, if there's just, a bit of color here.

JHawkins: That was my assumption, too.

Niels Leadholm: That would be, like, the one association, but then it's... it's weird if, the original context needs to learn for every point. adding information that the reference frame already has.

JHawkins: So I've taken this one step further in my mind. And I said, just assume there isn't some sort of master object. The only thing that matters is anchoring the reference frame. And now, just... just imagine... I'm just gonna state this. After we've done the stapler, I have an anchoring of a reference frame, and in that, there are 3 objects. And, you and I might say, oh, one's the complete stapler, and one's the stapler top, and one's the stapler at the bottom, but the system doesn't know that. It just says those three objects that... and any of those objects could share any number of features and have any number of unique features.

Viviane Clay: It just turns out...

JHawkins: Yeah.

Viviane Clay: Didn't we just earlier talk... said... say that there is a default object, and then in the different states, we only store the deviations from that? Because otherwise...

JHawkins: no.

Viviane Clay: Every state has to relearn everything again.

JHawkins: No, it doesn't.

Viviane Clay: I wouldn't know where to look up the.

Niels Leadholm: That's my feeling.

Viviane Clay: That are not stored in that different state. Wouldn't it need to look up in the default state?

JHawkins: Okay, I'm trying to make it work.

So let's just... let's just think very generically about models. You got this reference frame. And you get to some location in the reference frame.

What we're suggesting, under a different context, you would predict different things.

And... and then we said, and you're arguing, without any context, It would be a default. And I'm trying to get it to the work where... I'm trying to get it to work where And I think this is a more powerful solution, is if I could get rid of the idea that there's a default. That they're just 3 models.

And... How would that work? I can see the problems of it.

I still like the idea.

Niels Leadholm: I agree that... Jerry, what'd you say?

Viviane Clay: What would be the advantage of there not being a default?

Niels Leadholm: yeah, because I agree that it's nice that you don't... we don't magically assume the complete stapler is the prime model or whatever, but I feel like that's not an insurmountable issue in that, it's either, a mixture of, what was learned first, plus what is most common, and that just becomes the most represented model. It's not that it has some.

JHawkins: Okay, let's...

Niels Leadholm: Special significance.

JHawkins: Let's say I have a mug. And now I learn another mug, which is exactly the same as the first mug, except it's an inch taller. Everything else is the same. I don't want, I see that new mug, I'm gonna... it's gonna... it's gonna inherit a lot of properties from the old one. Some of those properties are location-specific, some are not. it'll inherit properties of, what its affordances are. How it will behave physically, its temperature, and so on. its fragility, how it might break. It might also... I might also say, oh yeah, this is just a mug in the same series, so if I go on the bottom, I'll see the mark of the... of this... of the person who made the mug, so I expect to see that. So those two mugs, in some sense, are very similar. And even though I learned one first, and then I learned the other one second.

I'm not sure I feel like one is a primary and one is a variation. It's oh, these are just two flavors of mugs.

and yes, I learned one first, but does that really matter?

after I've used it for a bit.

Viviane Clay: You don't have to feel a difference introspectively. It wouldn't look any different in the output representation. It would just be that when you see a new mug, like, when you see a mug with a logo, you don't have to relearn the handle, to look up the predicted features from The model...

JHawkins: But let's... but let's say... let's say I've learned these two mugs, one's taller and one's shorter, and now I see the bottom of... and I have both of these, I use them all the time. And now I see the bottom of a mug. And I can't tell how tall it is. Do I assume it's... do I say, oh, until I know better, I'm gonna assume it's a short one? And now if I see it's tall, I'll change my opinion, or do I just say. I don't know yet. I don't have the right... I don't have enough context, It's is there a default in this case? That it's the shorter mug, because that's the one I learned first? Or... or is there not?

Viviane Clay: Yeah, I wasn't thinking of it being, like, an inference default, saying. I assume I'm gonna see the default. I would say inference still doesn't say, oh, I assume to be in state 0, and only if I see something that contradicts with it, I'll look at the other ones. I would still do inference over all of the states, testing them all, but for learning that we have a place where, The generic features are stored, so we don't have to relearn them for every variation, and then the variations just express what's different from the generic version.

JHawkins: But that... but that sort of goes counter to what you just said a second ago, which is, if... if... if... wouldn't inference make the assumption it's the default scenario? until I have... until I have any kind of contrary evidence. I would assume it's the base model.

Viviane Clay: It would just be that if you're at a specific location in that shared reference frame, and your current state doesn't store any feature at that location, it would look up what the generic model stores for that location.

JHawkins: this could be right. I liked... It feels more powerful and more orthogonal and more, elegant. And I can't put my finger... I'm trying to come up with examples to prove that it's important. I am... I think came up with examples of the two mugs, because I don't think one necessarily has a priority over the other. Why would one require a context variable and one doesn't?

You know what I'm saying? it doesn't feel right to me. I'm trying to make it work where it's... to me, it's much more... it's more elegant if I can just assume that All the models end up being equal. And... It may not start that way, you might learn one first, but... It just... And these models can grow and become independent... they can grow in any way we want them to grow, the different variations of the same reference frame.

Niels Leadholm: I also, with the example, I almost wonder whether, when you see that mug that's a little taller. Your brain, you'd potentially... infer, oh, this is similar to the column... to the mug I've had before. So you activate that, reference frame. But then, with some context that, okay, this is different, you learn that it's... there's some variation. So in some sense, it is This is a... a child, or whatever of... not child, but a variant of a familiar object, whereas if it was a totally different mug, you wouldn't... you wouldn't, Recover that model in the first place, and you would just learn it as an entirely new model.

JHawkins: I thought... I'm sorry.

Niels Leadholm: Yeah, that's okay.

JHawkins: I had a.

Niels Leadholm: Yeah, it just... okay.

JHawkins: Imagine...

Niels Leadholm: It feels to me like you could... yeah, it could be. It could be which way.

JHawkins: Are you going for the primary? You guys both like this idea of a primary home. Imagine I had.

Niels Leadholm: I agree there's weird things about it, but anyways.

JHawkins: let's imagine I have 3 state variables that are coming from elsewhere, A, B, and C. And, I learned... imagine that you start off by learning a new model, and I'm going to pick state variable A. not only am I learning all the features of the object, but I'm learning them in the context of A. now I, And now I learn a variation of A, the new mug. and I'm gonna have it state variable B, That's why... as I move over the new mug, the taller mug, I will be... I could be associating state variable B and A with the common features, but only state variable A with some features, and only state variable B with other features.

Niels Leadholm: But then don't you have to relearn the things? Because...

JHawkins: no.

Niels Leadholm: if you...

JHawkins: I don't have to relearn anything, because there's already something there. I go to this location, there's something there.

and now I can associate that something with B.

it would... alright, I guess I'd have to think this through more carefully here. All right, maybe we can...

Niels Leadholm: Unless, A is always active, and then the question is, what is the purpose of A?

JHawkins: that's what I'm thinking. A could always be active, and A and B can be active simultaneously. Alright, I... I think it... this is a tricky one here. I'm running at my limits of being able to think on the fly. about this. I'll just state that it is more elegant, in my mind, if we do not consider this a primary model and submodels. It's... they could start out with one you learn first, and then you learn subsequent ones, but in my mind. It would be a nicer solution, and probably less likely to cause problems in the future if we could... if we didn't have to assume there was the default, mama-pop object, parent, Default one. It just feels like the world is too... the world is always changing and morphing, it would be much easier if we just made no assumptions about... there was original, and now there's variations. You could just have... you can just have all variations from the start. and the only thing that's common between them The thing that's common between them all is the anchoring of the reference frame. That seems to be a more... a less problematic and more elegant solution to this... to the problem.

Niels Leadholm: I understand you're... just a quick... or, yeah, feeling of disquiet, but I guess if there's one thing that might help, is just whether this sort of default model Rather than being, like, State A with capital A, and that... there, it's... therefore it's special. all it is the representation that exists without states. it's the L4, L6.

JHawkins: Yeah.

Niels Leadholm: and all that.

JHawkins: I got it. But imagine, now, okay, imagine that's the case. Now, imagine I'm learning state B. so I'm going around, there's some changes now under state B. And I go visit the location, so I have the state variable coming in from someplace that says B, and I go to the default model, and I'm looking at those. the state variable's still there, why wouldn't I associate the state variable with that? That previously learned feature.

Niels Leadholm: isn't it optional context on the apical dendrites?

JHawkins: but it would be there. it's context, and the context doesn't know when it's supposed to be applied, when it's not supposed to be applied. It just says, there's context

Viviane Clay: You would only apply it if there's a prediction error from the default model. If you can already make perfect prediction about your sensory input using what's already stored there, you don't have to learn a conditional, different feature.

JHawkins: I'm not sure that's true. You don't have to learn it, but you could.

Viviane Clay: But you've already learned it.

JHawkins: I know, but I don't associate it with B. I'm only... This is a way that... What if I just... I just... if it was context, I always associate it with whatever I'm learning. Whatever I'm experiencing. And imagine... no ones are always learning all the time. Imagine they're not learning only when there's an error. Imagine they're always associating context with the current observation. that way... The context would predict... would eventually learn to predict the entire object, independent of, Yeah, I'll just sit with that. It's I could constantly... associate whatever I'm observing with the current context. And if I've already learned it, no problem, but if I haven't learned it, I'll learn it. And... Therefore, the context is not just predicting variations on the base model. Over time, the context would predict the entire thing.

Again, I'm just trying to get away from the idea there's a base model.

I guess I'm just...

Viviane Clay: Not understanding what the issue with the base model is. I thought it was a really, nice and elegant idea that way, because then we don't have to relearn any of the common features.

JHawkins: No, nothing, has to be relearned. I'm not suggesting anything has to be relearned.

There's no relearning going on here.

Viviane Clay: To associate the new state with all of the different.

JHawkins: but that's not... that's not loading new features at locations. That's just associating a feature at a location, which is already learned, with associating with the contact.

Niels Leadholm: if context A is learned for all. Locations in the original, example.

Then, presumably, it needs to always be active when we're recognizing that object. Including variations. Otherwise... Otherwise, we need to relearn things.

JHawkins: I can see where you're going here.

Niels Leadholm: And then it's whoa... and then I... But it's...

JHawkins: I...

Niels Leadholm: It's always active, and then it's...

JHawkins: Okay, I agree that we don't want to relearn anything, so I'm not suggesting we're relearning anything.

Niels Leadholm: I don't mind...

JHawkins: learning associations, that's not relearning. That's just, adding on additional information. And so the question is, can I get this idea that I have, which is there isn't a parent or base object. Can I get that to work? I also like the idea that there might always be contact. That is, there might always be something from someplace else giving me contact.

That's nice, too. But then I have to decide when to provide context and when not to provide context. If somehow the mechanism of providing context was always there, it's always available. time might always be available, and I can use it or not, depending on if it correlates.

I like those ideas. So the question is, can you get it to work?

Niels Leadholm: I wonder if it's a language thing, because would you agree that there's a base reference frame?

JHawkins: for all of these, the same reference frame.

Niels Leadholm: Yeah, so I feel like that's maybe what is... the base model. And...

JHawkins: no, my point is.

Niels Leadholm: Or at least.

JHawkins: My point is... no, my point is the base reference frame can represent multiple objects all within the same class. That's my argument, right? There are multiple objects under that base reference frame. So the reference frame itself does not... It can look like it's anchoring to an object, because maybe there's only one object. But I gave the examples, like, when a rat goes between rooms, the grid cells re-anchor, right? my point would be, like, what if I went between two kitchens or, two similar rooms? Would I... would I re-anchor, or would I say, oh, this is a variation of what I already know? I would assume all the knowledge I have about kitchens would apply to this one. So I may not re-anchor, but I could... End up learning different features at different locations.

Niels Leadholm: Okay, yeah, and so I guess something like a base model could be what is learned in the reference frame when you don't have any specific context.

JHawkins: and I'm trying to get away... the whole... the reason I got to... the reason I actually brought up this idea, initially I said, why wouldn't I have context? wouldn't there always be... it'd be easy to say there's always some context. Imagine there's always some context, and if I... that seemed okay, that's... that's an idea I liked, or at least it was an idea that was intriguing. It's then I have to worry about when there's a context and when isn't a context. It's there's always a context, and... and the... how I learn these objects, the order I learn them isn't really that important.

I could go and... it doesn't really matter. In the end, I just end up with a bunch of models, all under the same reference frame anchoring, and... It doesn't matter which order I learned them in, they're all gonna... you're gonna end up with the same thing. That's... that's... there's a... there's advantages to that.

Viviane Clay: what if there's always context? But there's still a kind of base model that is... all the features that are generally predictive for all of the models. So you might not ever see that generic object itself, but it's like an... maybe an average model of the other, so that whenever you don't store a specific feature in a model, you can go to that base model and use that feature to make a prediction.

JHawkins: that's what you're arguing. Isn't that the same thing you've been... you've been arguing.

Viviane Clay: Yeah, basically you're saying you need some place to look up what to predict when you don't... haven't stored something at that location in this specific state. for example, trees. There are tons trees. But it feels like we have some kind of generic idea of how a tree looks like. There's a tree trunk and branches and stuff like that. And we might have never seen that generic tree, ever. But we still have that to make a general prediction about where the trunk should be, and where to predict the greenery.

JHawkins: Okay, so how does that relate to our conversation? Sounds good, but...

Viviane Clay: Yeah, I guess just... That there should be some way to look up features at.

JHawkins: But that's the case, you just said yourself, there's an example where I may have never learned the base model.

Viviane Clay: Yeah, I'm saying there should still exist a.

Niels Leadholm: Yeah, and it... And it could be averaged....

JHawkins: I would rather that. I would... that argues in my direction. That's saying, I learned specifics.

Viviane Clay: And.

JHawkins: specific models, and then, they're all in the same class, and somehow, from that, I can derive a generic sort of tree. It's not that the generic tree is the first one I learned.

Viviane Clay: Yeah, that'd agree.

Niels Leadholm: That's what I was trying to say as well, that it's not that it's the first one. It's just, it's the accumulation of experience that that, yeah, like Vivian says, when you don't have a specific prediction, this is Tells you what you're likely to see.

And it can be reused.

Most of the features at locations in that model are reused. By the different state examples.

And in practice, it would look like the first object you learned when you first learned it, but over time, it would change and become more a general nonspecific model.

Ramy Mounir: And is this, an average... is this, the mean or the mode of what you're seeing? Is this, an average, or is it, something that you've seen multiple times?

Hojae Lee: I think... it's more... so I feel like... what... Jeff, you might have written this in the, Honda talk, but, We're always learning compositional objects, that never stops. everything that we learn is probably something specific. we say generic mug, but, what is exactly, a generic mug? We have never... we might have never seen that, but then somehow we have all these, different models of mugs, mugs with logo, mugs with chip. And the reference frame itself is, representing that class. And so I feel like that generic mug is like that... Reference frame that's representing the class that We're able to deduce from the subject that we have seen.

JHawkins: Getting close, but the reference frame itself can't represent the generic mug. It's gotta be a mod... it's gotta be a model within the reference frame. It's gotta be features associated. I think the tree... this is a gamble's a good example. in some sense, I think it's arguing in favor of what I'm suggesting. We learn specific things. And there's no preferred... I'm trying to make it work, so there's no preferred specific things. There's the first one you learn, you may learn one more than another. But the order in which you learn them in this class should... in the end, shouldn't matter. and then this... so the idea that there's a generic class of tree that comes out of this, which is still fuzzy in my mind. which says, hey, there isn't... there wasn't a preferred tree.

there's lots of models of trees and, under different contexts, but somehow we're able to come up with this, average, or mode, or mean, whatever, for... for the whole class. That's an interesting idea. Yeah, it's an interesting idea.

if I could get... if I could get the idea that... that there is no... if I could say, hey, we learn a... we learn a first object, but it's not... it really has no... I can get it to work... imagine if I could get it to work that... that after I've learned 3 variations of something. There is no master object anymore. There's no default object. And it all works. Would anyone have an objection to that? It's are you objecting to the sun?

Viviane Clay: Yeah, I'm not arguing against that point at all, and actually it's easier to think about a solution now that I know what your problem with it is. I'm just trying to find, a practical way of achieving that without having to relearn all the points in the new.

JHawkins: assuming we're not going to relearn all the points. my... if I approach a problem like this, I'm saying, oh, in my mind, there's definite advantages to not having, the default object. And those... I should say, there are advantages. It's hard for me to put my finger on them right away, but I smell that there's really big advantages there. This is somehow in the back of my brain going, yeah, you want to go this direction, this seems to be the right direction to go, that there is not a default model. There is the first model. And then we make... we change after that, but it shouldn't matter the order in which you learn things, and there shouldn't be some sort of preferential model. If I can get that to work without relearning, anything. That feels better to me than... Taking the simple... what seems like a simple example, oh, we learn a model, and now we're learning a... a... And that... the first thing I learned is always the parent, and now, now it's all derivatives and that.

Niels Leadholm: Yeah, no, I agree with that.

Viviane Clay: I think the average approach could actually be a good way to achieve that. I don't know if that language works for you, Jeff, but maybe for Niels. If you think about the constrained object models that we have in Monty, where We're basically taking the K statistically most frequently observed locations, and we kind of average features that were Observed at those locations to, to learn to learn models. The way I would think of...

JHawkins: Is that to get around noise? Is that to get around the issue of noise, or sampling size, or what's the purpose of that?

Viviane Clay: Yeah, it... not... it was mostly so that, there's actually a point to learning hierarchical models, and we don't just learn, a super high-resolution model of a house, basically.

JHawkins: yeah.

Viviane Clay: We have some constraints on the models, we can't just store millions of points for an object.

Niels Leadholm: Yeah, it's a form of sparsity. It's basically, we have a certain amount of representational capacity. What is the best way to distill down what we've learned?

JHawkins: okay, It does feel like, yeah, if you showed...

Niels Leadholm: That's a bunch of trees, it would develop an average tree model.

Viviane Clay: Yeah, so basically, there would be, like, the base model that always gets all of the observations, even if there are different states of the object. It always incorporates all these observations, and it learns over time an average of those. And then there's the state conditioning, which only learns the specific features on that specific object, and it would only store those features if they deviate from what's stored in the average model.

JHawkins: Okay, so I... that all sounds good, except I still think... I don't mind... I like the average model idea. I just don't like that there's a default model. I think... Maybe I just called it...

Viviane Clay: the wrong word, it would be... It would be the place to look up which feature to expect at a location if there's nothing stored in the specific state model.

JHawkins: Yeah, I guess I'm saying... I'm...

Niels Leadholm: And it's not necessarily a model you would ever see, or, an object you would ever see.

JHawkins: Okay, it was the first one I learned, I'm still trying... I'm still trying to get it to the point where, imagine.

Niels Leadholm: Wait, say that again? It's the first one you... it's not necessarily the first one you learned. When you've only ever learned one object, then the default model... the average model has nothing else to be informed by, so that.

JHawkins: no, not the average model, but this... I don't the average model I like. It's the default model I don't like.

Niels Leadholm: Those are the same thing. Or I'm not sure what default means in this context.

JHawkins: And it's... the default means, without... without a contact signal, what do I assume is stored?

Viviane Clay: So we moved... I moved away from that, basically saying there's always a context signal, but we have the average model To use to make predictions when we didn't store specific.

JHawkins: Oh, okay, alright, that may... alright, so that may be... That may be... meet my criteria?

personally.

Niels Leadholm: Personally, it still feels like you could have an example without context, in which case... Use the average model, but...

JHawkins: Maybe, but imagine this context, we haven't really defined what the context is, and where it's coming from, and how to interpret it, and when, to my mind, it's when would there be context, and when would it? If I assume that there's always some kind of context signal, because the state of the brain, in some sense, is context.

Then... then that's a nice idea. There's always context. There's something floating on Layer 1 always. Something's going on someplace in the brain, And let's assume that's flowing by my Layer 1. If I can... if I can associate if... If I just assume there's always some sort of contact, that seems like a safer assumption. And then, I just work with that. I take that as a given. There's always context, and maybe it's useful, maybe it's not useful, maybe there's associations, maybe there's no associations statistically, but there's always context. And, And, I don't like the idea of, oh, we have the bug, and now, under the right context, we predict a logo.

I'd rather have...

Viviane Clay: we have the average mug for all the points that are not the logo, to predict, the handle and stuff.

JHawkins: Okay, I think that's a good, Compromise that might work, right? And initially, the average isn't very interesting, because I don't have enough to average. So initially, the average will look like the first thing you learned, right?

And that can fool us, thinking, oh, that's the default model. average, it really... it's just an average model that hasn't averaged anything. So it's just...

Viviane Clay: Yeah, as soon as you've seen two instances of that object, the average is something that you've never seen before.

It'll be

JHawkins: Assuming there's a difference, assuming there's a difference at that point. I don't know what it means to average, an average, there's a logo here, there's not a logo here. It doesn't seem like you can average that.

You could average morphology, perhaps.

Ramy Mounir: Maybe show something. Oh.

I remember presenting this before, where I talked a little bit about, a generic morphology in the columns and the variations in the... the variations in the actual SDR.

JHawkins: I don't remember this, but I remember the picture, but I don't remember the context of what it was. You just walk us through it.

Ramy Mounir: Yeah, it was mostly, that I was thinking of... coming up with an average of, these, more different instances of the cup as a generic model, and that generic model would be in the columns themselves. So it'd be, we would have a location, and the variation of that location, that is an instance of that location, basically. a unique and generic representation, the generic being what defines the class of the objects, and it would be something like an average, and then the unique representation would be in the SDR, and it would define the actual representation. This is like the state. Basically, that tells you where that actual location is based on the state, but it's the full SDR now.

JHawkins: this thing, this helps me realize that The different models that could be under the same class. may not look at all like each other. these mugs all have... they're not too far in variations from each other. But the way I've been thinking about it, the different... you can have a reference frame, and the different models under that reference frame could be... Really unique, that you wouldn't want to average them.

That would take, That would mess things up. Here, you could average...

Niels Leadholm: It depends on, yeah, how we're approaching class. I've always felt that there's class that's more morphology-based, and then there's class that's based on other things, like affordance, or language, and stuff like that, and A banana and an apple both being fruit. is... I think, represented in the brain in a very different way from yeah, these mugs being similar.

JHawkins: Thank you. I agree, but I still think even simple morphology could be quite different. we've seen a hint of that with the stapler parts.

And... if the top of the staple and the bottom of the staple are both In the same class of stapler. then you don't want to... they're really unique, and you don't want to average them, but they could be very unique. You don't want to average them. I think the averaging works really well. Not a particular class. Oh, sounds a little confusing.

Scott Knudstrup: it reminds me of the shape skeleton stuff, going back to that, which is that there's... The shape skeleton being this, particular computer vision type thing, but if you just imagine that the brain is doing something. similar, where it's saying, okay, here's some underlying structure that's more fundamental to the thing, and yes, the variations, like surface-level variations exist, but somehow there's some column or some part of the column that's representing some, Something fundamental about the overall shape of that thing, and it's running concurrently.

JHawkins: Currently.

Scott Knudstrup: With the part of the brain that does the more surface level variation.

JHawkins: but I don't know how the... what's... just some part of the brain, it's it's I'd like to understand all this in the sense of a cortical column, and oh, these guys over here are doing shaped skeletons, and these guys over here are doing specific models.

Scott Knudstrup: We couldn't.

JHawkins: I feel like that. It doesn't seem like that to me. I'd rather not go there. Another thing... the more I think about it, it seems This idea under the... under class, that... There's lots of things that we might be able to observe, the similarities between two objects and put them in the same class, but they can be quite different, and so averaging them Isn't always gonna work very well. It would make a mess of things at times.

Hojae Lee: at least mathematically, there's ways to, besides average, we could try to factor out, let's say we have specific instances of objects. if we... so again, this is just really mathematically, if we have some matrix of all the points and, some features, there will be some way amongst different matrices to find some commonality, so that... it's like a...

JHawkins: it's a clustering problem, right?

Hojae Lee: yeah.

JHawkins: There's a lot of...

Hojae Lee: Yeah, so it might...

JHawkins: the average,

Hojae Lee: be some other linear combination.

JHawkins: clustering is... clustering is... averaging over N... N clusters. Something like... I don't know what you call it, right? Clustering says, oh, I got 5 clusters, therefore I have N averages.

Which could be happening,

Viviane Clay: In what examples are you thinking that very different models would be Under the same object ID.

same object, you mean same reference frame? Yeah.

JHawkins: I didn't say same IG. I'm going to talk about anchoring a reference range. What are you saying? What are examples where you have different objects under the same reference frame that look quite different?

Viviane Clay: Yeah.

JHawkins: even something simple like mug morphology, there's a... there's a lot of things that I might say are mugs that... that if I averaged them, imagine I had tall, skinny ones and short, wide ones.

if you average... At points, you'll end up with not, something in between. imagine I have tall ones and short ones, and there's a lot of points that That are average points, but they don't exist on any mug.

Viviane Clay: But if they are two different, maybe they are just learned as different objects with different reference frames. if you have, a tea mug and a big coffee mug, they might just be different reference frames.

JHawkins: so we... but then, right today, we're exploring the idea that The common reference frame is a way of grouping objects together under some... under some class, or some... yeah, some class. That could be wrong, But if I go with that idea that... that the reference frame anchoring represents a class, then that class should be able to accommodate lots of different things that don't... aren't morphologically... that are morphologically different. it's... it's just say, I can say this isn't the same class of objects, because maybe it works the same, or maybe it has the same color or something, and yet.

Viviane Clay: But yeah, the object being in that class, the class needs to have some predictive power for that specific instance. for it to be useful to be in that class. So it needs to share at least a good amount of features at locations. With the other objects in the class. And maybe there are different models in different areas, there might be the morphology models that share morphology, and then there might be more, semantic or action-based classes, that... That don't learn as much about...

JHawkins: I can see that objects could become quite different morphology, Even though they're in the same class. imagine, the stapler top coming up, and as it comes up, it goes through some sort of weird gyrations, and so it has... ends up with a morphology, it's completely different than it started with, and... And yet, I still know it's the same object. I still know it's part of the stapler.

there might... this idea that the common reference frame represents a class may not work out. I don't know. It seemed really good. blanked it.

Scott Knudstrup: I think there's another nice thing about it, which is... in the unsupervised learning stage, if most of the time I see mugs upright, they're mostly in the same basic orientation, and that probably helps me merge them into a class. So the fact that there is something about their... Reference frames are already aligned. Helps me merge them into a class,

JHawkins: I think that's true.

Scott Knudstrup: On the learning side, too.

JHawkins: If I see a new object and I want to put it in an existing class, then you definitely want to have similar features and similar orientations. Then they have to have a commonality.

If I say, here's a new thing, I don't know what it is, it has... then if it has some similarities.

Viviane Clay: There seem to be two different signals, or two different ways to... put things into the same category with different states. One is similarity, like morphological similarity, like the different mugs. The other one is time, which is all the object behaviors, where we know it's still the same object, because we've seen it transition from one state into the other. And it seems like with time, because we see the transition happening, there can be a lot more change in the morphology, and we still keep it in the... as the same object, or in the same reference frame, but with different states. But if we don't see that transition happening, and there are actually different instances of objects. It seems much harder to say, oh, this should be In this reference frame, even though.

JHawkins: Yeah,

Viviane Clay: French?

JHawkins: I was trying to imagine someone saying to you, you give, Link something, you say, Link, I know this looks like a teddy bear, but it's actually a mug. See? It's a mug, right? What would you say?

Hojae Lee: Sliding your child.

JHawkins: maybe it's a, maybe it's a.

Scott Knudstrup: Hyper science.

JHawkins: I'm bug in the safe in the shape of a teddy bear, I don't know. But then you'd have to... then he'd have to pay... you're right, you'd probably have to see, oh, there's an opening, and there's liquid in it, or something like that.

Ramy Mounir: There's also affordances. we put things in a specific category based on the affordances, and that's... they could be completely different morphologies or features.

Niels Leadholm: Yeah, that feels more like a model, so it's

JHawkins: But...

Niels Leadholm: a, a chair or something, it's, something that you can...

JHawkins: Can you have affordance? Can you have affordances about some similar morphology? It seems like you have to have some...

Niels Leadholm: I think they could be linked, you could learn that, chairs have the behavior that you can sit on them, but they also tend to look like chairs. But you could also independently be like, oh, that is going to be sufficiently chair-like for my purposes right now.

Ramy Mounir: Or just basically things like, things that could be eaten, or like fruits, and they have complete different morphologies, like a banana and an apple. I know it might not be affordances or... but it's, they appear in the same context together, they're in the same fruit basket, so you basically label them together as the same category.

JHawkins: Yeah, hearing this conversation made me think of something that was worth throwing out. I think about the chair example, or... There are... there are things that we definitely... there are objects I have And... and I know what they are, and then under certain contexts, I want to use them for something else, like a tool. Or, it's something that's not a chair, but I want to use it as a chair. I know it's not a chair, and so I have a model of this thing, it's... it's not chair model, it's something else. And, But I want to use it as a chair, and so it seems to be somebody, it seems like you have to take two models. You have to have something like a chair model. and... and you're trying to apply the chair model to this other model. It's like you're saying, hey, here's some predictions from Model A, which are... which is a chair, and here's some affordances or some behaviors of Model A. Let's see if I can make it work for this model of B, which is not a chair. And... So I don't think B is a chair. I might use it as a chair, but I don't think B is a chair. I'm not going to relearn B as a chair. I want to be able to make predictions about it, oh, can I sit here? Will I be able to lean back on this? Is there a cup holder? I don't know. Whatever it is, I might want to say. I might want to take knowledge about the chair and try to force it onto this other object to see if I can get it to... to work, which... which... which is a... I just think that's an interesting observation. We do that all the time, I think, when we...

Niels Leadholm: Rude.

JHawkins: New tools and stuff.

Hojae Lee: Yeah.

JHawkins: And it'd be like saying, okay, I don't want to relearn object... the non-chair object, I don't want to relearn it. but I want to be able to use it as a chair, Or use it as something. And I'm not going to relearn it, so I basically didn't have to be... I have to be, Taking one model, enforcing behaviors and, And morphology predictions onto another one.

Viviane Clay: Or...

JHawkins: I don't know how...

Viviane Clay: We can take the model of our body and run a quick simulation of Sitting down on the thing, without going directly from chair to chair model. feels more like what I do. I think about...

Hojae Lee: do it.

Viviane Clay: If I sat down on it, though, I don't know. would it be comfortable, I don't know, it feels like I'm.

JHawkins: Alright, that may be true of Chair, but I'm... I also think, sometimes I'm doing some work on something, and I need a tool. I don't have the right tool. So then I just start rummaging around, looking for something that might work as this tool, This could hold this,

Ramy Mounir: It's like we're computing similarity along a specific dimension, because similarity is a very high-dimensional thing, and it's like we're singling out or attending to only one dimension in the similarity space, and we're just computing similarity between objects.

Niels Leadholm: But yeah, I guess in a way that can generalize to, a totally novel... situation. I think use... through using that kind of structured representation, yeah, simulation, because it's You can see... yeah, some, I don't know, like a penguin-shaped statue or something, and it's you will have never computed the similarity of that to, to a chair. But if you can just mentally imagine Sitting on it, or... I don't know.

JHawkins: it's almost imagine, it's somehow I take a chair object model, and they say, alright, There should be a flat surface, horizontal surface, about here. In my chair model, and... Can I... project it onto the reference frame for the penguin, and say, is there some flat surface like that there, or where is the flat surface? God, it's amazing what the brain does. It's so damn complicated, it seems. But we do this, and we know it has to happen.

That's... I think this issue of... the chair examples is... that's actually really core to what we're just... we've been talking about here. It's... it's a way of... of... of taking a model And using it in a way that... without relearning what the model is. It's, in some sense, a way of... Sharing knowledge to a new model without relearning the model.

Niels Leadholm: yeah, Misha, I saw you posted some interesting, questions and stuff. Feel free to definitely, jump on the call if you want to voice those, or we can discuss.

JHawkins: Did you just post those now?

Niels Leadholm: It was in the chat.

JHawkins: Oh, in the chat.

Niels Leadholm: But anyway...

JHawkins: Yep.

Niels Leadholm: It was in the midst of heated discussion.

JHawkins: Oh, there we go.

Misha Savchenko: I just, I'm driving, so I never...

Niels Leadholm: Oh, okay. Yeah, no worries. I can also read it out for you if you want.

Misha Savchenko: Sure, yeah, thanks.

Niels Leadholm: Cool, yeah, no worries. Yeah, yeah, Misha, I guess first we're just making the point that, we were using this term averaging, but generalizing is maybe a better, conceptual

JHawkins: Why is that? I don't have an objection to that, but I don't know why.

Niels Leadholm: I can see, the argument that, or I'm assuming what you meant, Misha, is, what we're describing is a model that generalizes across specific instances.

Misha Savchenko: Yeah, averaging just has this mathematical or morphological connotation. Where you're... which, Jeff, you pointed out that you don't really want to average completely different morphologies of things that still belong to the same class, but I think it's appropriate to think of it as a general, the idea of many trees and what a general concept of a tree is.

JHawkins: so maybe... so the nice thing about... the nice thing about averaging is it is a specific mathematical thing, and that's... but generalizing isn't, I think. So I think maybe what... can I say what you're saying is that it's probably not averaging, but we still have to come up with some sort of general... generalizing mechanism, which we don't know what it is yet.

Misha Savchenko: Yeah, exactly.

JHawkins: I see. Yeah.

Niels Leadholm: Yeah. And then I guess, like you... like you said, Hoji,

JHawkins: It's a vote against averaging.

Niels Leadholm: I think what you were getting at, Jose, was things like, I don't know, PCA or whatever is an... generalizing of kind of a distribution of points, and I think already the grid... constrained models that, you implemented, Vivian, it feels like that already does a pretty interesting one that goes beyond just averaging, because. there are points in the code that averages are taken, but that isn't the key... that isn't the key part. Most of it is about... It's only local averages. most of it is about, storing points and... Yeah, it would almost be interesting to throw a bunch of tree images at it and see what it learns.

Viviane Clay: Yeah, I guess at the global scale, it's really, K winners of, the most consistently observed locations.

Niels Leadholm: Yeah, so it's a morphology.

Viviane Clay: Yeah, it would never... if you've never... if you've only seen point A and C, it wouldn't average it to B, it would pick A or C, depending on which one was observed more often.

Niels Leadholm: but then if you had, I don't know, a crescent shape. You had lots of observations along that, and then a few that kind of went off the crescent. because most of them fell along that crescent, that would be what comes out. And so that's where, yeah, it feels like it would have most... a lot of trees are bent and all this stuff, but most of them have a roughly upward trend. And yeah, you would get that kind of.

JHawkins: the more I think about this, the more I feel like. this averaging tree thing isn't really right, because, in fact, what kids draw, they draw, a little lollipop, right? they stick another thing on top. There's actually very few trees that look like that. Even anything that looked remotely like that. They're like... they're really different than that. So there are... yeah, there's some trees that are lollipops, but... so I'm wondering if maybe what kids draw is not some average, it's just somebody show them a tree, here, draw a tree like this, make a circle on a stick, and that's what they learned.

Niels Leadholm: Yeah, it's also difficult, because when we talk about what people draw and what children draw and stuff, it's entangled with what your internal representation is and what you're able to produce, which aren't the same thing. And, we've talked many times about how people are terrible at drawing and all the different. Reasons Thousand Brains Theory might explain that. Don't know, I think this.

JHawkins: I'm not sure I'd buy the average thing, or even the generalizing thing. I feel

Viviane Clay: Yeah,

JHawkins: Jordan.

Viviane Clay: Yeah, I think the statistical frequency thing is probably better than averaging, but another thing we could look at is, like, how predictive it is for the different instances of the model. we would only store points in the general model if they are consistent with most of the other states. Because, there's no point in storing a point in the general one if all of the specific instances overwrite that point. culture.

JHawkins: Yeah, between us, I'm not gonna think about this averaging thing. I think that's a... might be a bit of a red herring today. And, I keep it in the back of my mind, But I do think...

Viviane Clay: But not at all, because I feel like it was the only solution to not having to relearn everything. taking out of the equation how it's generated, I agree it might not be an average, but that there should be some kind of generic representation that we can look up the feature if we don't have it in a specific model.

JHawkins: I don't know.

I'm thinking of the tree example. I think kids learn that's how you draw a tree. Not that they observe trees, and then generally.

Viviane Clay: I agree with that. I'm not talking about drawing, I'm just talking about, like, how would you learn them without having to relearn all of the points in the different states?

JHawkins: But how to learn what? The.

Viviane Clay: Like, how do you learn a new state? Without having to relearn all of the points.

JHawkins: I thought we.

Viviane Clay: We have a generic model to look at... look at.

JHawkins: we, I think that was the key that I'm gonna walk away trying to solve, which is imagine I don't have a generic model. I have a bunch of models, each have its own context. And these models overlap. many of the models have the same features at certain locations.

And the assumptions will never have to be learned. The knowledge is there, and the question is, how do I make sure I use the knowledge that's already been learned?

fruitfully. I'm just taking that as the working assumption and the task to solve.

Ramy Mounir: I think it can be... I can be... think it can be done without a generic or default model.

Viviane Clay: Do you just look up in a random other state?

JHawkins: no, I... you... you have... there are... imagine every location, you might have something stored, you may not have anything stored. If you have something stored, there could be one thing, or there could be multiple things, depending on the context.

And we just take that as a starting assumption.

if something was learned at some location, it'll be there, and it might be... it might be consistent with one or more contacts. And if I'm on some context. and my... and there's a feature there, and my context is not associated with that feature, then I would associate that feature with my content.

Viviane Clay: What if you're in a context and you haven't stored a feature for that location?

JHawkins: And there's still a feature stored there, just, my contact doesn't predict it. But there is a feature there. I like that the feature will be... imagine I can recognize a feature with... the context is an optional override, right? it's imagine it's coming on Layer 1 or something like that, and, there's... there's things learned there, but I can now... I guess it would default to one of the other states, I guess whatever one is. I don't have to make it work.

Viviane Clay: That's what I... that's, I feel like, the core problem I was trying to solve today, at least, which... what state does it default to?

JHawkins: Okay, I have a... now that I have a clearer definition of a particular problem. I'd like to think about that. Nope, that's it.

Misha Savchenko: If there's no... if there's no general model, then how do you... what do you do when you're asked what... What is above the tree trunk in a tree? How do you answer that question if you don't have a general model of a tree?

JHawkins: You have models of trees. So there's no... there's no question, you have knowledge about that. It's just... you're asking me... you're assuming there's a general knowledge as opposed to a specific knowledge. I could learn one tree. There's only one tree in my life. I have a very impoverished place, I live, there's only one tree, and I could learn that tree, and you can say, what's about the tree trunk? And I can tell you, I don't have to have a general model for that. Yeah, and then there's a lot of... there's a lot of trees where you can't even answer that question, because tree trunk isn't visible, it's hidden behind,

Viviane Clay: you're looking at a new tree, and you recognize it's a new tree, because the trunk at the bottom looks different. So you have a different context now than from what you learned before in the tree class. Now you look up, you can still make a rough prediction that you're gonna see some leaps there.

JHawkins: just be... just because I have a new context, doesn't mean... I'm trying to get to the point where I have a new context, but if my context doesn't say something about a particular point, I'll default to something else. I'll default to whatever else is there.

Viviane Clay: Okay, so then, yeah, I... I'm not sure.

JHawkins: Christians, you want to default it to the default model? I'm trying to avoid having a default model.

Niels Leadholm: Maybe one thing is...

Viviane Clay: too.

Niels Leadholm: Maybe the one thing...

JHawkins: No, I have to figure it out. You gotta let me work on it.

Niels Leadholm: Cause, came up at the end of your document, Jeff, and also, I think it was what your other question was referring to, Misha. We can also have columns with different models. And you can have a column that has learned a kind of more coarse model of trees, and so it just... it's closer to the lollipop representation, even if it's not necessarily that. And that might be through, sparsity constraints about trying to learn, a complex object, but without that much, representational capacity, or it could be through having large receptive fields that are blurry input features and things like that. Maybe, but with specific.

JHawkins: example of the tree have argued that we don't really see trees that look like melod pops. Very rare.

but you might have a column that only looks for.

Niels Leadholm: green blob... not green blob, but it just...

JHawkins: I'm just saying... yeah, I'm saying I don't think that... I don't even see that really in nature. I... again, I'm going to go back to the tree example. Maybe your point's still valid, Niels, but my... the tree-specific tree example, I think kids draw the lollipop, because that's what they're told how to draw.

Niels Leadholm: Sure.

JHawkins: It does.

Niels Leadholm: But yeah.

JHawkins: That's not what they... they don't see that anywhere.

Niels Leadholm: But then, circling back to the motivating problem for this was Okay, we know a model of a mug. Now it's got a chip in it, or something like that. How do we represent that, be able to predict that, without having to relearn the model of the mug? And one... one valid approach, which you discussed in the document, Jeff, is Maybe you have different columns that have different models, and one of those columns, or some of those columns, do update their model, but then other ones keep them the same.

JHawkins: that would... that would be true, certainly, if different modalities, for example, one has a colored spot on it, you wouldn't feel that. You would just hear, but I don't think that's a general solution. I just missed that in my write-up.

Niels Leadholm: Yeah, I'm just saying it's...

JHawkins: problems.

Niels Leadholm: It's an... it's... yeah, I'm not saying it's the solution, I'm just saying it is, another one to, consider. But, yeah, I think...

JHawkins: Here's another way to think about it. And maybe I'll try to solve this problem the way I want to solve it, and I won't succeed, so that's fine, but I'm going to try. One of the things I realized is that in terms of providing context. we really don't have any good... we're just throwing it out like it's something, but we don't really have a good example, or a good understanding of it. like in the staple example, the context... there was masking that along... went along with it, or something like that.

that, maybe the solution to this, what I'm trying to achieve, is having a better understanding of what context is.

Viviane Clay: Yeah, I feel like maybe we have two examples of that, what it could be already. One is the feedback connection to Layer 1, That could give a context signal. The second one could be the time signal in an object behavior. Those won't really work for, object categories, which type of mug instance is it, but....

JHawkins: I guess what?

Viviane Clay: Still help to think through some of the examples.

JHawkins: and we also... there's examples of contexts which are really out of left field. often we have surprising predictions based on some sort of context, oh, the context of something you... Neil said earlier today. about... his house. And in that context, I make different predictions about something, I don't know, we're talking about right now. it's there can be very... or something I saw this morning on, in my yard, makes the... changes what I think about something else later. context can be really all over the map. It can be very specific, but it can be really strange, and time is just, one of those, right? It's one of those... Things.

Niels Leadholm: circling...

JHawkins: Boom. Yeah.

Niels Leadholm: like what you were saying, Vivian, Is there a reason it couldn't be the first, the L1 feedback, that couldn't impact class? Because if L2, L3 neurons have apal dendrites going up to L1, It feels like that would be a good, location to Influence the sort of object-level description.

Viviane Clay: yeah. Yeah, I think it would be part of that solution. I guess it just, in my head, seemed a bit of a chicken and egg problem, that... The lower level is trying to tell it that it's the... logo... the mug of the logo by recognizing the logo, and then the higher level one is trying to give it the context. But, yeah,

Niels Leadholm: I agree, though,

Viviane Clay: Nothing.

Niels Leadholm: Yeah, because I was thinking about this before, that, if the state or context or whatever is represented in the apical dendrites, how is that communicated up? So it feels there might be different places it's represented, or different representations of it. One might be what is active in L2, L3, And that could be passed forward. And one is, what is the feedback? And that would be. More like the L6 to L1.

JHawkins: Maybe. But anyway, I'll point in general, there's a whole ton of stuff in the brain that projects to Layer 1. we've talked about time, the matrix cells, other regions, weird stuff all over the place. you want to... and emotional saliency issues, that's where... neuromodulators are released, often in Layer 1,

Viviane Clay: Perfect.

JHawkins: It's done.

Viviane Clay: We're looking for the context signal, something where we can get a bunch of different types of signals.

JHawkins: so you imagine Layer 1 is this bath of, noise going past all the time about different things that might mean different things. Of course, the columns don't really know what most of that stuff is. it's just activity up there, but the general idea is they can pick and choose anything that's helpful associatively from up that point. So that's... that's the... I'm just pointing it out that Layer 1 is... is... has very specific projections, like we did in our paper, and O'Neil's just talking about in Vivint, but there's also all these Crazy stuff, everything goes up there, it seems which is good, right? We want... we want broad context, and, part of being smart sometimes is to recognize an unusual context as a predictive mechanism. something that someone else didn't pick up. Damn.

all good.

is there... let me ask, before I go on... we end today. if I'm wrong, and there is... and let's say there is a default model, not even an average one, just like the default, we learned this, and now we're learning variations of it. Was there any problems with that we identified? Were there any specific problems?

Viviane Clay: I don't...

Niels Leadholm: I don't think so. I think the main one is... is, yeah, how we derive it, because... And I think that's maybe what came up when you were presenting that, Rami, is that we were discussing how would you average the morphology points, or something like that? And we were concerned, like you were saying, Jeff, today. that, Depending on, what system you're using, you might end up just with, a total mess. But.

JHawkins: I'm not...

Niels Leadholm: It feels like that there are many different approaches and as.

JHawkins: I'm not interested.

Niels Leadholm: The one we have is already fairly sophisticated.

JHawkins: I'm not... I'm not... I'm not excited about the advertising video. Do we need that? Essentially.

Niels Leadholm: I think averaging is really a term worth avoiding.

Viviane Clay: Yeah, basically, just a generic... a generic model.

Niels Leadholm: Or kind of distillation?

JHawkins: But is a generic model learned, or is a generic model.

Viviane Clay: Distilled, or...

Niels Leadholm: computed?

Yeah, computed. No, it's definitely learned... And it's... I feel like it has the attributes you wanted, which was, like, the first model you ever learn it's gonna be like that, but then, as Vivian says, as soon as you learn a second model. It's gonna be unlike any model you've ever seen, any object you've ever seen.

Ramy Mounir: It feels more like we're extracting the variability, so it's like we're subtracting the variability from the model that we learned, and then we're building associations with that as a state. So it's it's exactly like what Tristan is doing with extracting a functionality from a class, and he's just assigning a default class there, and then he's just building another few ones, and then just assigning different, connections to those extracted functionalities. It feels exactly the same to me. It's just, we're... we're removing the variability, and then we're assigning it back, but as an association, and then we're building associations with different other variabilities, or with different variations of that class.

Niels Leadholm: Which, yeah, fits with maybe the language that you were using Hojab, Maximum variance that kind of, There's some parts that kind of... There's some way of representing most of these things. And accounting for most of the things we observe, and then there's slight deviations from that. And it's... the slight deviations are the states, and then... the sort of... Generic description is the... yeah.

Scott Knudstrup: I think... Oops, sorry.

JHawkins: That's alright.

Scott Knudstrup: I was gonna say, one nice aspect of that description is... That when there are areas with a large degree of variance, that's a good signal that the prediction is not necessarily strong. It's not a strong prediction, necessarily. But areas where, there's a great deal of consistency, we ought to... Have high confidence in our predictions to locations like that.

JHawkins: Unless... unless the variances are associated with very specific instances, right? If the variance is associated with very specific instances, then they're... it's very... those are significant.

That's part of the problem. sure. When do you assume things are unique? I have one last thought before we're done for the day, if we're gonna almost be done. I'm working on another idea, which is really confusing. You'd think today is confusing?

But I throw it out, because maybe it'll spark something. in our models, if we think about, layer 4, the feature layer, it's... I'm going to talk about the neuroscience now, right? You have... we have a representation of... the mini column represents, the point normal of the... or the edge orientation, and then the cells in the column are uniquely represent Specific instances of that edge. so it's a generic edge, and then a very specific location on a specific object.

I was wondering if the same thing is happening in the location signal. There's many columns down there. They have similar properties. when the... in the idea that you'd have two representations of location. One is a very generic one, which is almost this, pure grid cells. It's only... there's only maybe 10 or 12 different Grid cell locations that a grid cell can represent, something like that. And then there's specific, then in a minicom, you pick particular cells that would represent specific locations. So you have, generic feature, which is really just an orientation, and then specific features, and then on the bottom, you'd have generic locations, which are not really unique, but Still something. And then specific ones. And so when we were talking about, when we were talking about things like, oh. averaging, or fuzziness, or whatever. it's just the idea that could the brain be taking advantage of the same sort of mechanism we see in Layer 4? Could the same similar kind of mechanism going on in Layer 6, where we have the generic, a very low resolution location and the high resolution location? I just...

Niels Leadholm: Yeah, like what Rami was showing before.

JHawkins: Thank you.

Niels Leadholm: remember that... When he presented that, but...

JHawkins: The one with the pictures of the mugs we saw earlier today?

Niels Leadholm: Yeah, the...

JHawkins: Dimensional change card slot, I don't remember seeing this.

This is to me.

Ramy Mounir: The wrong ones.

JHawkins: I would... I would remember rowboats, if I've seen rowboats before, so I don't seen a rowboat.

Ramy Mounir: Hold on just a sec.

JHawkins: Are you guys hearing that? There's a noise outside my window, are you guys hearing that?

Ramy Mounir: Okay,

JHawkins: Oh, this thing here, oh, the generic and specific. Oh, really?

Ramy Mounir: So I was... I was thinking...

JHawkins: Put it...

Ramy Mounir: What did you conclude from that? we were thinking that we would have, just like we were having in the Layer 4 features representation... And then this, and then, we also suggested... That would have the same thing in the... in the Layer 6, also. okay.

JHawkins: And what... and what is... and how did they proceed? What did you learn? What did you gain from that?

Ramy Mounir: I don't know, I felt it was a... It was a good idea. I didn't really.

JHawkins: all right, so we have... I've thought of this idea before, and I've forgotten about it, and then, so I just brought it up again this week in my thinking, so maybe you were thinking about it too, or maybe this is... I don't know where this came from, but... but yes, this is the idea. But I'm not sure where the arrows go. yes, you have these two representations, But where do the arrows go? I don't know. How do they interplay with each other? When, when do we use a very coarse coating of space? Versus, encoding space. Yeah, we have some ideas of when you'd use a course coding and features versus... fine features, right? We can see the advantages of that.

Tristan Slominski: Also, I'm not entirely convinced that the generic location is actually Cartesian at all. It could be, like, a... toroidal... toroid... toroidal thing, like Jose mentioned before. Where those generic locations are not Cartesian 3D at all.

JHawkins: they're right. They are, they would be terrorial, because... just think about pure grid cells. imagine, I'm thinking, grid cells. grid cell modules are... if you just take one grid cell module. it has maybe, I don't know, 10, 20 different locations it can represent, and they repeat over and over again. And so it's often described as a toroidal space. But it still would say, What it does is says that particular That particular representation could appear many different places in the world. It's not unique. it doesn't occur everywhere, just, 1 out of 20, or whatever it is. So it repeats over and over again.

just an interesting tidbit. When, the, when Grit Schwabs was discovered, What's his name? The guy who discovered.

Niels Leadholm: Closer?

JHawkins: no, Mozard...

Hojae Lee: O'Keefe.

JHawkins: O'Keefe, O'Keefe.

Niels Leadholm: O'Keefe was play sales, Right,

JHawkins: he's just got a place.

Niels Leadholm: No, sir.

JHawkins: And then the Moses discovered grid cells, and O'Keefe, they're very competitive people, and as far as I know, and Keith was at one point expressed Disappointment that he didn't discover grid cells, too. And... and the reason he didn't is that where he was looking, the grid cells The spacing was so large that they didn't actually repeat within the environment. that they... they were representing the space and the environment, but they didn't actually wrap around the Torah, they didn't repeat again, or he didn't... it was far apart that they didn't see that. with these interesting observations, it means that, many times, you might just have a coarse coating of space, and you don't have this torridal aspect yet, you don't have the... which is normal, repeating a lot, or not repeating a lot, and having coarse coating?

it just throws that out that it's still... if I don't have that... if I have a large enough receptive field for the grid cells. It's... it's just a fuzzy representation space. It's not a, it's... it's not repeating. So each grid cell would only... would represent a fairly large area. something else to think about in that picture you made.

Ronnie.

Niels Leadholm: Cool, yeah, that seems like a good... good stopping point.

JHawkins: More stuff to get confused about. Alright, we'll get to the bottom of it, I'm sure.