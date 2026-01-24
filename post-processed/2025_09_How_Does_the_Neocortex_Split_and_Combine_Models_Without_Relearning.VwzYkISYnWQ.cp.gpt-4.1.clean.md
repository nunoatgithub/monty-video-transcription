Niels Leadholm: The question is, how do we represent multiple objects when we start learning variations of familiar ones, or, as you mentioned in the document, when you suddenly have a subpart of an object, like the stapler top.

JHawkins: I can start walking through that. This topic was really confusing for me. I worked on it last week, and we exchanged some messages on Slack. I felt lost thinking about it, so I decided to sit down and try to come up with some ideas. I worked on it the last couple of days, and it ended up being something pretty simple, so I'm not sure what I'm missing. It's not a complete idea, but at least it's a grounding to build upon. I wrote that up, and some of you may have seen it. I put it in Slack. I can share my screen and bring it up, just walk through it, if that's okay.

Niels Leadholm: Sounds great.

JHawkins: I'm now sharing, and I want to bring up Slack. I'm not sure if it's the document I posted in Slack. Let's open the research pane. This one here.

Alright, did everyone see that?

Scott Knudstrup: Yep.

JHawkins: How do I get rid of this? There are shares of that thing coming up. Okay.

I started thinking about all the things we've been doing and trying to make sense of it all. We have all these variations on models that we've come up with. The original idea was that there's a reference frame and a location, and you put some information at some location in the reference frame. Then it gets really complicated. We've talked about morphology versus features, and I don't think we've ever completely resolved that. The idea is that you can build models that can recognize things just on the orientation or the edges of models. We've done a lot of work on compositional structure and object behaviors, which we've now broken into separate models. We've also discussed classes of objects, which I think, Niels, you might have been the first to bring up, but we never really resolved those either. Those are variations of objects that are similar.

If I see a new class of an object, it inherits some properties from previous objects in that class.

A common theme is that we end up splitting models. I use the word splitting, though I'm not sure if that's the word you use, where we have a model and then create a new variation of it. We want to maintain a lot of the properties of the first model but have a new model. The important thing is we can't relearn everything every time we form a new variation. We first got into this in a big way with the stapler. We have a lot of good figures, which I'm not showing here, but how do we learn that if we never saw the stapler open, then we see it open, how do we model the different parts of the stapler when before they were the same? Hopefully you all remember that. At that point, we were running into similar problems with composition. There are two ways the composition problem works: a feed-forward way and a feedback way. The stapler was a feedback way, in some sense. I start with an object and split it into components, child objects. The other way, the feed-forward way, is when I take two objects and create a new object that I didn't have before. In one, you're building new things, and in the other, you're taking something apart. I also wrote here the problem I saw: we had this basic idea.

Let me see what... I'm reading my text here.

When we talked about the mug and the logo, we had this idea: how do I know I have a mug and a mug with a logo? We said we might have some state variable that says this is a regular mug, or this is the one with the logo. Internal to the model, if the state variable says there's a logo, I make one set of predictions; if it's one without the logo, I make a different set of predictions, but otherwise they're the same. This doesn't work if there are a lot of variations. With just one thing, like a logo, yes, but I came up with lots of variations where you could have multiple things. I could have mugs with logos and without logos, mugs that are tall, mugs that are short. Some could have logos, some could have no logos, and so on. A single state variable wouldn't work, and we can't have lots of state variables in a column. It's just not possible.

Niels Leadholm: When you say we can't have single state variables in a column, as in...

JHawkins: I don't have many state variables in a column. We could have one. If I say mugs come in tall, short, green, and red, with blue lips or no blue lips, with the mental logo or with a Thousand Brains logo, and I can have any one of those variations, then a single state variable does not suffice. I have to have a state variable for each of those particular variations. I'd have to be able to say, this mug is the red one with a logo, and I can make predictions about that, or this one's the green one without the logo, and I can make predictions about that. The idea is that there would be a set of cells within a column. If I have a size of cells to represent a particular variable, I can't mix them; I'd have to have separate sets of cells for those. Otherwise, you get back into this mixing of SDRs, so it just felt... okay.

Niels Leadholm: Yeah.

JHawkins: Then I came up with another example. Did I answer your question, Niels, sufficiently, or...

Niels Leadholm: I think we'll get to it later in terms of the top-down feedback stuff, but it feels to me like you could have a single population that represents multiple different...

JHawkins: Good, but then...

Niels Leadholm: And then there's some limitation to how much superposition of those states you could have. But...

JHawkins: It's not a general solution either, because as we saw with the stapler, there was information that had to come from the R2 to tell the R1 how to divide the object into two parts. In the case of the stapler top and bottom, there had to be a signal from another learning module. That was an example where, internally, you wouldn't have enough information to know that the stapler should be broken into two parts. Somebody has to provide that.

Niels Leadholm: Totally.

JHawkins: Then I gave this example where I started thinking about time. You can have a temporary arrangement of features—imagine mugs on a table, and you want to remember where it was last time you saw it. That's a temporary compositional object. Our mechanism should work for that. But then I realized, I might remember where it was this morning or yesterday, so I have the same basic components in a different arrangement, and I have a model of that too. The only difference between those two is time, and I don't expect that time variable to be located within the column. What if every day of the week the mug was on a different portion of the table? That day of the week would be the variable I'd use to make the correct prediction about where the mug is. That, too, is not something I would expect to be in the column representing mugs or tables. There could be some variables within a column, within the learning module, but clearly that's not the general case. The general case is that I have to have signals coming from elsewhere. There are many examples of signals coming from elsewhere that would tell me which model I should be invoking right now. Is it the model where the cup's in the middle of the table? Is it the model where the cup's on the corner? That kind of thing. I just assumed it's always an external state variable. That could be wrong, but if I assume there are external state variables, then I can have as many as I want, because they can be coming from different places, broadcast broadly in the cortex. Some could be broadcasting times, some could be broadcasting day of the week, and under any context, I might say, when I'm in the living room, the mug is always on this corner of the table; when I'm in the dining room, it's on another corner. There could be almost an unlimited variety of contexts in which you'd make different predictions on the same objects or similar objects. It just felt like that to me.

Viviane Clay: Yeah, and that would match with the way we talked before about how a state could be this broader Layer 1 input that gives context and basically conditions which features to expect at what locations, but while still using the same reference frame in Layer 6.

JHawkins: So maybe I came right back to where we were before, but it certainly wasn't obvious to me in the beginning as I started going through this. I got clarity going through those examples before I came to a simple conclusion. Did you have something else you wanted to say?

Viviane Clay: I can bring it up later.

JHawkins: Then I also thought about classes of objects. This is something that bothers me every time I bring it up, because I really have no idea about it. We never really resolved what makes a class, how would I know when something is a class, and how do I differentiate. Then I said to myself, let's just jump right into it and say, what if my reference frame anchoring is the class? I can have as many variations on that as I want, and as long as I've anchored the same way, then it's the class of objects. That class of object could consist of one object, so I could say, I'm in this room, and I've anchored to this room. Or I could say, I'm in a kitchen, and that's a class of objects, and I have a bunch of different kitchens I know, but they're all anchored the same way. Not all rooms would be unique. If there's nothing common, I would say, this is the class of other things I had before. The idea is that the definition of a class is a particular anchoring of the reference frame. I may have one or many specific models in that class. Those models don't even have to have anything in common. I could still say they're in the same class. I always thought it's funny how, when we start to think of what's a fruit, and then you tell a child all the things that are fruit, and then you tell them a tomato's a fruit, and they say, that doesn't look like a fruit. But technically, it's a fruit, so you can say a tomato's a fruit in the same class, maybe. That's a stretch example, but my point is, once you say an anchor of a reference frame is a class, you can have any kind of models in there that overlap or don't overlap, or just have slight changes or not. It doesn't really matter. There could be lots of different variations of things in that class. I don't know if that works, but that's the way I was thinking about it.

Viviane Clay: Yeah, I like that general idea a lot, actually. But I was wondering, when you create a new state of that particular object, can you still reuse the data that's stored from a different state? For example, I've learned the mug without the logo, and then I create a different state of mug, which is mug with logo. Can that model, if it doesn't store things for the locations where the handle is, go back to...

JHawkins: I think the way I look at it is at any particular location, there is something stored. Sometimes, under different states, you can store different things at that location. I can have a very small change, and everything else is the same. I can say, this is the mug that has the nick in the corner, the little crack in the corner. Everything else is the same, but when I get to that location on this one, I'll make a prediction that's different, and only in that location.

Viviane Clay: Yeah, so there's a default, and then the state can change specific parts that are different in that stage. Oh, yeah.

JHawkins: The default assumption is you keep everything until you start adding something else. I thought about this with the stapler. I mentioned it here, but I don't have good figures for this, so you'll have to listen to me. When I thought it was a stapler, we would sometimes draw the staple as just a big rectangular box, featureless, and you couldn't even see the seam. Then it opens up, and now you see it's two parts.

When you open it up, sometimes you see things you didn't see before—new features under the bottom of the top, and new features under the top or the bottom. You'd want to add those features to those models. You start out absorbing all the things you had before; the staple top is still the staple, still these features in this area of the model. Now I can add new features only to the staple top, and I can add new features only to the staple bottom.

Viviane Clay: I was wondering if it makes sense to apply the same mechanism to the stapler, because it seems fundamentally different. I wouldn't say the top and the bottom are two different states of the stapler. I would say where the top and the bottom are relative to each other are different states of the stapler.

JHawkins: I wouldn't say they're treatment states. They're all in the class of stapler. The stapler could be a complete stapler, or it could be a stapler top, or it could be a stapler bottom. In my definition, they're all in the class of stapler. Using the word "state" is a little misleading.

Viviane Clay: The thing that feels weird about that to me is that as you see the whole stapler, you perceive both parts, so you're basically perceiving both states at the same time, if the top and the bottom are two different states of the stapler.

JHawkins: I wrote in here someplace—here we go, this paragraph, I think. Is it getting rich talking?

Viviane Clay: Especially if they share the same reference frame, then that's odd if the bottom of the stapler is not rotating.

JHawkins: Here's what I suggested. You might have three models of the stapler in R1: the original one, one that says we're paying attention to the top, and another that says we're paying attention to the bottom. I don't see why the original complete model would go away.

Viviane Clay: I would think of it as R1 having three models of the stapler, but I wouldn't think of them as being three states of the same model that share the same reference frame.

JHawkins: They're not the same model. There are three models, but they have a shared reference frame. They're all in the class of stapler. If I asked you to identify one, you'd immediately identify any of those three models. If I just saw the top or the bottom, you'd say it's part of a stapler.

Viviane Clay: If they're sharing a reference frame and you're perceiving them both at the same time, how can the top part be rotating while the bottom part is not moving?

JHawkins: Then you'd only be perceiving the top or the bottom. That column would be—

Niels Leadholm: It's interesting.

JHawkins: R1 would be attending to the top, and R1 would—in some way, I don't know yet—the context would tell it that we're just dealing with the top model and to pay no attention to the bottom model right now.

Viviane Clay: I was thinking of the kind of child object segmentation, as you see the move, as being maybe a different type of process. You originally learned the full stapler model, and then as you see them moving, some of the parts the model isn't predictive of anymore. Let's say it has anchored to the stapler top, and the reference frame is rotating with the stapler top. It stops being predictive of the bottom features, so it slowly forgets about those.

JHawkins: Why do you say it slowly forgets about them? It's not going to forget. The context just says we're not paying attention to that model right now. One thing I didn't say here is that the stapler example gave us the idea that the context would occlude some parts. We required that in the staple example. The context was not just "we're stapled atop," but the context says only pay attention to this part of the model.

Niels Leadholm: For what it's worth, I had a similar thought when I was reading this. Specifically for the stapler subdivision part, that feels like a different mechanism, and part of it is just how fast it happens. As soon as you see something moving independently, you can segment that out. It feels like that happens almost to the whole object, which fits with what we've talked about before, the type stuff.

JHawkins: But I can't—

Niels Leadholm: It feels like when you're learning this new stuff, you attend, then you learn a point of new information with that context in the middle. Then you attend, you learn another new point of information—oh, there's another logo here.

JHawkins: I'm missing this distinction that both of you see. I'm R1, I have a model of the staple, and now the staple top's moving. Our assumption before was that a signal from R2 points out that there's a subset that's moving here. There had to be some sort of signal that says attend to this area of your model and don't attend to the rest.

Viviane Clay: Yeah.

JHawkins: That, to me, is either part of the context being provided to R1, or it may be the entire context. It's interesting to think that the context may be thought of as an occlusion area or an area of attention. But it's at least part of the context. In that case, as soon as we do that, we have to be able to add new features to the stapler top that we didn't see before, so I have to have a new model that I'm building at that point.

Ramy Mounir: I have a question. Sometimes a child object needs to be part of two different classes of objects, like a table leg—it could be part of a table or a chair. Does that mean, for that leg, we would learn two objects? Because they have to anchor differently now?

JHawkins: That's a good question. Yeah, that's interesting to think about.

Viviane Clay: I think that's another good point. To me, I'm still on board with the temporary masking and all that, but it doesn't feel like it's a different state of the same object. It seems like maybe at first it is exactly the same object, and we're just applying a temporary mask, but it's a different problem to segment an object into child objects versus having an object and different variations of it.

JHawkins: It may feel that way, but let's walk through it. On the one hand, we know that we have to keep the features in the same reference frame for the top of the stapler, because otherwise we wouldn't be able to make predictions about it. So even though I'm isolating the top of the stapler, I have to maintain the original model, right? That has to be there. Now I need to be able to add new features to that model that only pertain to that subset.

It seems to me I have to maintain the same reference frame, and I have to be able to differentiate it from other instances of models in that reference frame. I've just stated some points of fact, or at least statements of making. That feels to me the same. How does that feel different to you?

Niels Leadholm: Or...

Hojae Lee: Can I give a different example instead of stapler?

JHawkins: Should I stop sharing my screen? I don't know if it's helpful to have me.

Niels Leadholm: Sure, we can always come back to the document.

Hojae Lee: Maybe, bicycle? Stabler top and bottom feel like they belong to the model stapler. But for a bicycle, if we segment out everything except for the wheel, I wouldn't say it all feels like a different model.

JHawkins: I think it is, in fact.

Hojae Lee: Reference?

JHawkins: I do, I think you're right, because if I see a bicycle the first time, I would not think of this as a monolithic thing. I would look at each component and try to understand what it is. I probably have seen wheels before, and I might have seen pedals before, and things like that. That, to me, is more like the mug and the coffee cup, where we're taking individual things we already recognize and building something new. But with the stapler, we were able to imagine a stapler looking just like a rectilinear box with no delineation, and all of a sudden, magically, it separates, and now you see things. There's no way in advance to know that there are two parts. With a bicycle, it doesn't feel that way to me. I wouldn't learn the bicycle as one thing. It would always be multiple things to start with.

Viviane Clay: But you usually see the full bicycle before you see all of the parts of it individually.

JHawkins: Normally, when I see something I don't recognize, I immediately try to narrow down my attentional focus until there's a part I do recognize.

If I see something I don't know what it is, like a new kitchen gadget, I will keep attending until there's a blade, or a screw, or a handle—something I recognize. Then I start building up a compositional structure. The staple example is different, because we can imagine the basic staple having no differentiating components—it was just a box. But that's not usually the case. Usually, if I see a new word, I don't learn the whole word. I look at each individual letter, and if I don't recognize the letter, I'll look at the features of the letter. So with a bicycle, you wouldn't learn the whole thing; you keep attending until you find something you recognize, something basic, and then another, and another, and you build it up compositionally.

Viviane Clay: Generally, we would want child objects to be their own objects, and then be composed into a parent object, instead of child objects being different states of the parent object.

JHawkins: I agree. That's what would happen. In the bicycle example, all the components of the bicycle would have their own reference frame, and then we'd be building a compositional object from them. We're going in a feed-forward direction. We have all these individual models, and now we're going to build a compositional model that positions all these child objects relative to each other. That's why I was trying to make this distinction between feed-forward and feedback, where with the stapler, we had something we thought was undivided, and then it got divided, and we had to figure out what was going on. It's a different problem or a different solution. I agree, all parts of the bicycle would have their own independent reference frame, because they're all independent components that you would have learned separately.

Viviane Clay: Maybe the stapler is more of an edge case that doesn't really use the mechanism we want to be using, or maybe it would require having to relearn individual models.

JHawkins: Maybe, I don't think so.

Niels Leadholm: Or is it a short versus long-term thing? Initially you developed this child object representation. Whether there's a contact signal or not, it's still taking a full model and just looking at parts of it.

JHawkins: That's interesting.

Niels Leadholm: I think that could happen with anything. You could have a new tropical fruit you've never seen before, and you learn a model of it just by looking at it. Then someone slices it in half. Now you see the new insides, and half of it has been taken away. Suddenly, you have this half of an object that you can almost instantly perceive as the same fruit, just cut in half.

JHawkins: Or if I see the top or the bottom of the stapler, I still say it's a stapler. If I see a wheel, I don't say it's a bicycle. I say it's a wheel, and it could be on lots of different things. It could be on a little trailer. It suggests it might be on a bicycle, but I don't say, oh, that's a part of a bicycle. That's a wheel.

Viviane Clay: I wouldn't say that the bottom of the stapler is a stapler. I would say it's the bottom of a stapler.

JHawkins: But it isn't anything else. It's not part.

Niels Leadholm: That's maybe the intersection of the state variable or state representation with the reference frame. It's the bottom of the stapler.

JHawkins: I didn't follow your comment.

Niels Leadholm: I agree, it's something you can uniquely define, but maybe that unique definition is the intersection of the state representation with the reference frame. That's what makes it the bottom or top of the stapler. You're not saying, someone gives you the bottom of the stapler and you say, this is an entire stapler.

JHawkins: No, you don't.

Niels Leadholm: But it's still grounded in your representation of stapler.

JHawkins: If all I could see was—maybe I was looking through a straw and all I could see was some features on the bottom—I'd say, oh, that's a stapler. Then I see a feature that's only exposed when the stapler is open. Then I say, oh, that's the bottom of the stapler, and the stapler is open. Or the top of the stapler. Then I would switch to the context of only looking at the bottom part. I think it works out well. I don't see this as an important distinction. I can see where it's coming from. It's possible you captured it with different words than I would use. If I take something I know is one object and divide it into multiple pieces, those pieces are still classes or parts of that object. They're not something else. It's not like a stapler bottom appears on my bicycle. I could try to make that happen, but it's still part of the stapler. That's where you're going—that's the feedback one, where you realize there are independent parts you didn't realize, but the assumption is they're all still stapler parts. They're not suddenly completely different objects. You would immediately classify any one of them as part of a stapler. 

Whereas, if you go in the forward direction, I have a logo and a mug. I take the mug and say, under certain contexts there's a logo here, in others there's not. The logo and the mug are not part of the same class. They don't share reference frames. It's just different. The feedback and the feedforward are different, but the same concepts apply. I'm trying to set up both of these at once.

Viviane Clay: But the first—

Niels Leadholm: Yeah, and maybe with long-term—you would learn a totally separate reference frame, particularly if you see that child object in different contexts. You see wheels in different contexts, and that's when you start— I wouldn't be surprised if, when a child first sees a wheel on a bicycle, they understand it's moving, it's a separate child object, but it's not a concept that exists beyond bicycles.

JHawkins: Have you ever seen it—

Niels Leadholm: If they've only ever seen it in that context.

JHawkins: Maybe. I don't know, in reality, they would have seen wheels elsewhere, almost certainly. It's possible what you say is true, Niels, but it's also possible that children struggle with things initially, understanding what they are. It's possible they just can't conceive of a bicycle very well until they understand the components. This goes back to the theory about how a child learns to read. Should they learn to read by looking at whole words, or by looking at letters? There are two schools of thought on this. I was brought up in the era when you learned letters first, then composed them into words. That's the way I think about it. I'm not going to really learn words until I know letters. If I saw some pattern—under a different context, I could learn a whole word as a thing, and then later try to separate out the letters.

Niels Leadholm: I noticed when I was trying to learn some Sanskrit, I was doing both. I would try to learn the letters and focus on the strokes, and then if I was learning a new word, I would focus on each stroke to recognize the letter, and then recognize a series of letters to identify the word. But I also had a coarse model of the whole word. I could often just match that, because it had almost a shape that looked familiar, and I was like, oh, that's the shape of the word for man, and that's the word for woman.

JHawkins: We do that.

Niels Leadholm: So it feels like both were happening at the same time.

JHawkins: And we do that in English, or any Western language, where when you read, you don't even see the letters, you just see the words, unless you get to a complicated word you don't know very well. But we don't look at letters. This is why people can swap out letters in the middle of words, and you don't even notice it while reading. As long as it has the right basic shape and the words are the right length, you won't even notice anything changed.

I think these all fit into the right conversation. Sometimes we have to break things apart, and when we do, we have components that share a reference frame. Most of what we do is build compositional objects, taking things we already know and bringing them together. But we can do both—we can learn words as entities, not just as compositional structures. I don't have much more to add to that.

Viviane Clay: To me, it still seems odd to talk about components as different states of the parent object. How do you know the stapler bottom won't show up in different objects the first time?

JHawkins: First, we know that the stapler top and stapler bottom must have the same reference name. Otherwise, you couldn't recognize them or make predictions about them.

Viviane Clay: But then, it could just stick to the part you keep following and learn more about it.

JHawkins: As they become separate, I can add new features independently. For example, I can now see under the stapler top, and there are extra things that become added to that variation. I wouldn't say these are just states of the stapler. I'd say there are three models in the class of stapler. There's a subtle but important distinction.

Viviane Clay: It's not that there's a base model and then flavors of it.

JHawkins: No, there are three models because they all share the same reference frame. Let's say there's a context for all of them. In one context, we have a bunch of features; in other contexts, some are shared and some are new. When learning a new object from the start, should I assume there's context for that? When I learned a stapler for the first time, it's not that the whole stapler is superior to the components. It's just another class of object in the same reference frame anchoring.

Niels Leadholm: It's more parsimonious if you assume some kind of superiority by the original learned model. I have a model of a mug, and I just learned that. Maybe there's some default context, but it doesn't really need to help predict anything. The reference frame can predict everything. The context is just needed when you deviate from that, like a bit of color.

JHawkins: That was my assumption too.

Niels Leadholm: That would be the one association, but it's odd if the original context needs to learn for every point, adding information the reference frame already has.

JHawkins: I've taken this one step further. Just assume there isn't a master object. The only thing that matters is anchoring the reference frame. After we've done the stapler, I have an anchoring of a reference frame, and in that, there are three objects. You and I might say one's the complete stapler, one's the stapler top, and one's the stapler bottom, but the system doesn't know that. It just sees three objects, and any of those could share or have unique features.

Viviane Clay: It just turns out...

JHawkins: Yeah.

Viviane Clay: Didn't we earlier say there's a default object, and in different states, we only store the deviations from that? Because otherwise...

JHawkins: No.

Viviane Clay: Every state has to relearn everything again.

JHawkins: No, it doesn't.

Viviane Clay: I wouldn't know where to look up the...

Niels Leadholm: That's my feeling.

Viviane Clay: ...that are not stored in that different state. Wouldn't it need to look up in the default state?

JHawkins: Okay, I'm trying to make it work.

Let's just think generically about models. You have this reference frame, and you get to some location in it. Under a different context, you would predict different things. Without any context, it would be a default. I'm trying to get it to work where I can get rid of the idea of a default, so there are just three models. How would that work? I see the problems, but I still like the idea.

Niels Leadholm: I agree. Jerry, what did you say?

Viviane Clay: What would be the advantage of not having a default?

Niels Leadholm: I agree it's nice not to assume the complete stapler is the prime model, but that's not an insurmountable issue. It's a mixture of what was learned first and what is most common, and that becomes the most represented model. It's not that it has special significance.

JHawkins: Let's...

Niels Leadholm: ...special significance.

JHawkins: Let's say I have a mug. Now I learn another mug, exactly the same as the first but an inch taller. Everything else is the same. When I see that new mug, it will inherit many properties from the old one. Some properties are location-specific, some are not. It will inherit properties like affordances, physical behavior, temperature, fragility, and how it might break. I might also expect to see the mark of the person who made the mug on the bottom. Those two mugs are very similar, and even though I learned one first and then the other, I'm not sure one is primary and the other a variation. They're just two flavors of mugs. Yes, I learned one first, but does that really matter after I've used it for a bit?

Viviane Clay: You don't have to feel a difference introspectively. It wouldn't look any different in the output representation. When you see a new mug, like a mug with a logo, you don't have to relearn the handle or look up the predicted features from the model.

JHawkins: Let's say I've learned these two mugs, one's taller and one's shorter, and I use them all the time. Now I see the bottom of a mug and can't tell how tall it is. Do I assume it's the short one until I know better, and then change my opinion if I see it's tall? Or do I just say I don't know yet, I don't have enough context? Is there a default in this case, that it's the shorter mug because that's the one I learned first, or is there not?

Viviane Clay: I wasn't thinking of it as an inference default. I wouldn't say inference assumes the default and only looks at the others if something contradicts it. I would still do inference over all the states, testing them all. For learning, we have a place where the generic features are stored, so we don't have to relearn them for every variation, and the variations just express what's different from the generic version.

JHawkins: But that goes counter to what you just said a second ago. Wouldn't inference make the assumption it's the default scenario until there's contrary evidence? I would assume it's the base model.

Viviane Clay: If you're at a specific location in that shared reference frame, and your current state doesn't store any feature at that location, it would look up what the generic model stores for that location.

JHawkins: This could be right. It feels more powerful, more orthogonal, and more elegant. I'm trying to come up with examples to prove that it's important. I thought of the two mugs because I don't think one necessarily has priority over the other. Why would one require a context variable and one doesn't? It doesn't feel right to me. I'm trying to make it work where all the models end up being equal. It may not start that way—you might learn one first—but these models can grow and become independent, and they can grow in any way we want, the different variations of the same reference frame.

Niels Leadholm: With the example, I wonder whether, when you see that mug that's a little taller, your brain might infer this is similar to the mug you've had before, so you activate that reference frame. Then, with some context that it's different, you learn there's some variation. In some sense, it's a variant of a familiar object, whereas if it was a totally different mug, you wouldn't recover that model and would just learn it as an entirely new model.

JHawkins: I'm sorry.

Niels Leadholm: That's okay.

JHawkins: I had a—

Niels Leadholm: Yeah, it just—

JHawkins: Imagine—

Niels Leadholm: It feels to me like it could go either way.

JHawkins: Are you going for the primary? You both like this idea of a primary home. Imagine I had—

Niels Leadholm: I agree there's weird things about it, but anyway.

JHawkins: Let's imagine I have three state variables coming from elsewhere: A, B, and C. Imagine you start off by learning a new model, and you pick state variable A. Not only are you learning all the features of the object, but you're learning them in the context of A. Now you learn a variation of A, the new mug, and assign it state variable B. As I move over the new, taller mug, I could be associating state variables B and A with the common features, but only A with some features, and only B with other features.

Niels Leadholm: But then don't you have to relearn the things?

JHawkins: No.

Niels Leadholm: If you—

JHawkins: I don't have to relearn anything, because there's already something there. I go to this location, there's something there, and now I can associate that something with B. I guess I'd have to think this through more carefully. Maybe we can—

Niels Leadholm: Unless A is always active, and then the question is, what is the purpose of A?

JHawkins: That's what I'm thinking. A could always be active, and A and B can be active simultaneously. This is a tricky one. I'm running at my limits of being able to think on the fly about this. I'll just state that it is more elegant, in my mind, if we do not consider this a primary model and submodels. They could start out with one you learn first, and then you learn subsequent ones, but it would be a nicer solution, and probably less likely to cause problems in the future, if we didn't have to assume there was a default, parent object. The world is always changing and morphing; it would be much easier if we made no assumptions about an original and its variations. You can have all variations from the start, and the only thing that's common between them is the anchoring of the reference frame. That seems to be a less problematic and more elegant solution to the problem.

Niels Leadholm: I understand your feeling of disquiet, but if there's one thing that might help, it's that the default model, rather than being State A with a capital A and therefore special, is just the representation that exists without states—it's the L4, L6.

JHawkins: Yeah.

Niels Leadholm: And all that.

JHawkins: I got it. But imagine that's the case. Now, imagine I'm learning state B. There are some changes now under state B. I go visit the location, so I have the state variable coming in from someplace that says B, and I go to the default model and look at those. The state variable's still there—why wouldn't I associate the state variable with that previously learned feature?

Niels Leadholm: Isn't it optional context on the apical dendrites?

JHawkins: But it would be there. It's context, and the context doesn't know when it's supposed to be applied or not. It just says, there's context.

Viviane Clay: You would only apply it if there's a prediction error from the default model. If you can already make a perfect prediction about your sensory input using what's already stored, you don't have to learn a conditional, different feature.

JHawkins: I'm not sure that's true. You don't have to learn it, but you could.

Viviane Clay: But you've already learned it.

JHawkins: I know, but I don't associate it with B. If it was context, I always associate it with whatever I'm learning, whatever I'm experiencing. Imagine they're always associating context with the current observation. The context would eventually learn to predict the entire object, independent of variations. I could constantly associate whatever I'm observing with the current context. If I've already learned it, no problem, but if I haven't, I'll learn it. Therefore, the context is not just predicting variations on the base model. Over time, the context would predict the entire thing.

I'm just trying to get away from the idea there's a base model.

Viviane Clay: Not understanding what the issue with the base model is. I thought it was a really nice and elegant idea that way, because then we don't have to relearn any of the common features.

JHawkins: No, nothing has to be relearned. I'm not suggesting anything has to be relearned. There's no relearning going on here.

Viviane Clay: To associate the new state with all of the different—

JHawkins: That's not loading new features at locations. That's just associating a feature at a location, which is already learned, with the contact.

Niels Leadholm: If context A is learned for all locations in the original example, then presumably it needs to always be active when we're recognizing that object, including variations. Otherwise, we need to relearn things.

JHawkins: I can see where you're going here.

Niels Leadholm: And then it's always active, and then it's—

JHawkins: Okay, I agree that we don't want to relearn anything, so I'm not suggesting we're relearning anything.

Niels Leadholm: I don't mind—

JHawkins: Learning associations, that's not relearning. That's just adding on additional information. The question is, can I get this idea that I have, which is there isn't a parent or base object, to work? I also like the idea that there might always be contact, that there might always be something from someplace else giving me contact. That's nice, too. But then I have to decide when to provide context and when not to provide context. If the mechanism of providing context was always there, it's always available. Time might always be available, and I can use it or not, depending on if it correlates.

I like those ideas. So the question is, can you get it to work?

Niels Leadholm: I wonder if it's a language thing, because would you agree that there's a base reference frame?

JHawkins: For all of these, the same reference frame.

Niels Leadholm: Yeah, so I feel like that's maybe what is the base model.

JHawkins: No, my point is the base reference frame can represent multiple objects all within the same class. That's my argument. There are multiple objects under that base reference frame. The reference frame itself does not necessarily anchor to an object, because maybe there's only one object. But I gave the examples, like when a rat goes between rooms, the grid cells re-anchor. My point would be, what if I went between two kitchens or two similar rooms? Would I re-anchor, or would I say, oh, this is a variation of what I already know? I would assume all the knowledge I have about kitchens would apply to this one. So I may not re-anchor, but I could end up learning different features at different locations.

Niels Leadholm: Okay, yeah, and so I guess something like a base model could be what is learned in the reference frame when you don't have any specific context.

JHawkins: The reason I brought up this idea is, why wouldn't I have context? Wouldn't there always be some context? It seemed like an idea I liked, or at least it was intriguing. Then I have to worry about when there's a context and when there isn't. There's always a context, and how I learn these objects, the order I learn them, isn't really that important.

It doesn't really matter. In the end, I just end up with a bunch of models, all under the same reference frame anchoring. It doesn't matter which order I learned them in; they're all going to end up with the same thing. There are advantages to that.

Viviane Clay: What if there's always context, but there's still a kind of base model that is all the features that are generally predictive for all of the models? You might not ever see that generic object itself, but it's maybe an average model of the others, so that whenever you don't store a specific feature in a model, you can go to that base model and use that feature to make a prediction.

JHawkins: That's what you're arguing. Isn't that the same thing you've been arguing?

Viviane Clay: Yeah, basically you're saying you need some place to look up what to predict when you haven't stored something at that location in this specific state. For example, trees. There are tons of trees. But it feels like we have some kind of generic idea of how a tree looks. There's a tree trunk and branches and things like that. We might have never seen that generic tree, ever, but we still have that to make a general prediction about where the trunk should be and where to predict the greenery.

JHawkins: Okay, so how does that relate to our conversation? Sounds good, but—

Viviane Clay: Yeah, I guess just that there should be some way to look up features at—

JHawkins: But that's the case. You just said yourself, there's an example where I may have never learned the base model.

Viviane Clay: I'm saying there should still exist a—

Niels Leadholm: And it could be averaged.

JHawkins: I would rather that. That argues in my direction. That's saying I learned specifics.

Viviane Clay: And—

JHawkins: Specific models, and then they're all in the same class, and somehow from that I can derive a generic sort of tree. It's not that the generic tree is the first one I learned.

Viviane Clay: Yeah, I'd agree.

Niels Leadholm: That's what I was trying to say as well, that it's not the first one. It's the accumulation of experience. Like Vivian says, when you don't have a specific prediction, this tells you what you're likely to see.

And it can be reused.

Most of the features at locations in that model are reused by the different state examples.

In practice, it would look like the first object you learned when you first learned it, but over time, it would change and become a more general, nonspecific model.

Ramy Mounir: Is this an average, the mean or the mode of what you're seeing? Is it something you've seen multiple times?

Hojae Lee: I think it's more—Jeff, you might have written this in the Honda talk—but we're always learning compositional objects, that never stops. Everything we learn is probably something specific. We say "generic mug," but what exactly is a generic mug? We might have never seen that, but somehow we have all these different models of mugs: mugs with logos, mugs with chips. The reference frame itself is representing that class. I feel like that generic mug is like that reference frame that's representing the class we're able to deduce from the subjects we've seen.

JHawkins: Getting close, but the reference frame itself can't represent the generic mug. It's got to be a model within the reference frame. It's got to be features associated. I think the tree example is a good one. In some sense, I think it's arguing in favor of what I'm suggesting. We learn specific things. There's no preferred—I'm trying to make it work so there's no preferred specific thing. The first one you learn, you may learn one more than another, but the order in which you learn them in this class shouldn't matter. The idea that there's a generic class of tree that comes out of this is still fuzzy in my mind, which says there wasn't a preferred tree.

There are lots of models of trees under different contexts, but somehow we're able to come up with this average, or mode, or mean, for the whole class. That's an interesting idea.

If I could get the idea that there is no—if I could say, we learn a first object, but it really has no—imagine if I could get it to work that after I've learned three variations of something, there is no master object anymore. There's no default object, and it all works. Would anyone have an objection to that? Are you objecting to the sun?

Viviane Clay: I'm not arguing against that point at all, and actually it's easier to think about a solution now that I know what your problem with it is. I'm just trying to find a practical way of achieving that without having to relearn all the points in the new model.

JHawkins: Assuming we're not going to relearn all the points. If I approach a problem like this, I'm saying in my mind, there are definite advantages to not having the default object. It's hard for me to put my finger on them right away, but I sense there are really big advantages. This is somehow in the back of my brain going, you want to go this direction, this seems to be the right direction, that there is not a default model. There is the first model, and then we change after that, but it shouldn't matter the order in which you learn things, and there shouldn't be some sort of preferential model. If I can get that to work without relearning anything, that feels better to me than taking what seems like a simple example: we learn a model, and now we're learning a— the first thing I learned is always the parent, and now it's all derivatives.

Niels Leadholm: I agree with that.

Viviane Clay: I think the average approach could actually be a good way to achieve that. I don't know if that language works for you, Jeff, but maybe for Niels. If you think about the constrained object models we have in Monty, where we're basically taking the K statistically most frequently observed locations, and we average features observed at those locations to learn models. The way I would think of—

JHawkins: Is that to get around noise? Is that to get around the issue of noise, or sampling size, or what's the purpose of that?

Viviane Clay: It was mostly so that there's actually a point to learning hierarchical models, and we don't just learn a super high-resolution model of a house.

JHawkins: Yeah.

Viviane Clay: We have some constraints on the models; we can't just store millions of points for an object.

Niels Leadholm: It's a form of sparsity. We have a certain amount of representational capacity. What is the best way to distill down what we've learned?

JHawkins: It does feel like, yeah, if you showed—

Niels Leadholm: If you showed a bunch of trees, it would develop an average tree model.

Viviane Clay: There would be the base model that always gets all of the observations, even if there are different states of the object. It always incorporates all these observations and learns over time an average of those. Then there's the state conditioning, which only learns the specific features on that specific object, and it would only store those features if they deviate from what's stored in the average model.

JHawkins: That all sounds good, except I still think—I don't mind, I like the average model idea. I just don't like that there's a default model. Maybe I just called it—

Viviane Clay: The wrong word. It would be the place to look up which feature to expect at a location if there's nothing stored in the specific state model.

JHawkins: Yeah, I guess I'm saying—

Niels Leadholm: And it's not necessarily a model you would ever see, or an object you would ever see.

JHawkins: Okay, it was the first one I learned. I'm still trying to get it to the point where, imagine—

Niels Leadholm: Wait, say that again? It's not necessarily the first one you learned. When you've only ever learned one object, the default model—the average model—has nothing else to be informed by.

JHawkins: No, not the average model. I don't like the default model.

Niels Leadholm: Those are the same thing. Or I'm not sure what default means in this context.

JHawkins: The default means, without a context signal, what do I assume is stored?

Viviane Clay: I moved away from that, basically saying there's always a context signal, but we have the average model to use to make predictions when we didn't store specifics.

JHawkins: Okay, so that may meet my criteria, personally.

Niels Leadholm: Personally, it still feels like you could have an example without context, in which case you use the average model.

JHawkins: Maybe, but imagine this context—we haven't really defined what the context is, where it's coming from, or how to interpret it. To my mind, it's about when there would be context and when there wouldn't. If I assume there's always some kind of context signal, because the state of the brain, in some sense, is context, then that's a nice idea. There's always context. There's something floating on Layer 1 always. Something's going on someplace in the brain, and let's assume that's flowing by my Layer 1. If I just assume there's always some sort of context, that seems like a safer assumption. I take that as a given. There's always context, and maybe it's useful, maybe it's not, maybe there are associations, maybe there aren't statistically, but there's always context. I don't like the idea of, "Oh, we have the mug, and now, under the right context, we predict a logo." 

I'd rather have—

Viviane Clay: We have the average mug for all the points that are not the logo, to predict the handle and such.

JHawkins: Okay, I think that's a good compromise that might work. Initially, the average isn't very interesting, because I don't have enough to average. So initially, the average will look like the first thing you learned. That can fool us into thinking that's the default model. It's just an average model that hasn't averaged anything.

Viviane Clay: As soon as you've seen two instances of that object, the average is something you've never seen before.

JHawkins: Assuming there's a difference at that point. I don't know what it means to average—a logo here, not a logo there. It doesn't seem like you can average that. You could average morphology, perhaps.

Ramy Mounir: Maybe show something. I remember presenting this before, where I talked about a generic morphology in the columns and the variations in the actual SDR.

JHawkins: I remember the picture, but I don't remember the context. Walk us through it.

Ramy Mounir: I was thinking of coming up with an average of different instances of the cup as a generic model, and that generic model would be in the columns themselves. We would have a location, and the variation of that location is an instance of that location—a unique and generic representation. The generic defines the class of the objects, and it would be something like an average. The unique representation would be in the SDR, defining the actual representation. This is like the state that tells you where that actual location is based on the state, but it's the full SDR now.

JHawkins: This helps me realize that the different models under the same class may not look at all like each other. These mugs aren't too far in variation from each other, but the way I've been thinking about it, you can have a reference frame, and the different models under that reference frame could be really unique—you wouldn't want to average them. That would mess things up. Here, you could average—

Niels Leadholm: It depends on how we're approaching class. I've always felt that there's class that's more morphology-based, and then there's class based on other things, like affordance or language. A banana and an apple both being fruit is, I think, represented in the brain very differently from these mugs being similar.

JHawkins: I agree, but I still think even simple morphology could be quite different. We've seen a hint of that with the stapler parts. If the top and bottom of the stapler are both in the same class, you don't want to average them—they could be very unique. I think the averaging works really well for some classes, but not all. It sounds a little confusing.

Scott Knudstrup: It reminds me of the shape skeleton stuff, which is a particular computer vision concept. If you imagine the brain is doing something similar, where it's identifying some underlying structure that's more fundamental to the thing, the surface-level variations exist, but somehow there's some column or part of the column representing something fundamental about the overall shape, and it's running concurrently.

JHawkins: Currently.

Scott Knudstrup: With the part of the brain that does the more surface-level variation.

JHawkins: I don't know how that works. I'd like to understand all this in the sense of a cortical column—some columns doing shape skeletons, others doing specific models.

Scott Knudstrup: We couldn't.

JHawkins: It doesn't seem like that to me. I'd rather not go there. The more I think about it, under class, there are lots of things where we might observe similarities between two objects and put them in the same class, but they can be quite different, so averaging them isn't always going to work well. It would make a mess of things at times.

Hojae Lee: Mathematically, besides averaging, we could try to factor out specific instances of objects. If we have a matrix of all the points and features, there should be a way among different matrices to find some commonality.

JHawkins: It's a clustering problem, right?

Hojae Lee: Yeah.

JHawkins: The average—

Hojae Lee: Or some other linear combination.

JHawkins: Clustering is averaging over N clusters. Clustering says, "I have five clusters, therefore I have N averages," which could be happening.

Viviane Clay: In what examples are you thinking that very different models would be under the same object ID? Same object, you mean same reference frame?

JHawkins: I didn't say same ID. I'm talking about anchoring a reference range. What are examples where you have different objects under the same reference frame that look quite different?

Viviane Clay: Yeah.

JHawkins: Even something simple like mug morphology—there are a lot of things I might call mugs, but if I averaged them, like tall, skinny ones and short, wide ones, at points you'll end up with something in between. There are a lot of average points that don't exist on any mug.

Viviane Clay: But if they are different, maybe they're just learned as different objects with different reference frames. If you have a tea mug and a big coffee mug, they might just be different reference frames.

JHawkins: Today we're exploring the idea that the common reference frame is a way of grouping objects together under some class. That could be wrong, but if I go with the idea that the reference frame anchoring represents a class, then that class should be able to accommodate lots of different things that are morphologically different. I can say these are in the same class of objects because maybe they work the same or have the same color, and yet—

Viviane Clay: But the object being in that class—the class needs to have some predictive power for that specific instance for it to be useful. It needs to share at least a good amount of features at locations with the other objects in the class. Maybe there are different models in different areas: morphology models that share morphology, and then more semantic or action-based classes that don't learn as much about—

JHawkins: I can see that objects could become quite different morphologically, even though they're in the same class. Imagine the stapler top coming up and going through some sort of weird gyrations, ending up with a completely different morphology than it started with, and yet I still know it's the same object, still part of the stapler. The idea that the common reference frame represents a class may not work out. I don't know. It seemed really good, then I blanked.

Scott Knudstrup: There's another nice thing about it. In the unsupervised learning stage, if most of the time I see mugs upright, they're mostly in the same basic orientation, and that probably helps me merge them into a class. The fact that their reference frames are already aligned helps me merge them into a class.

JHawkins: I think that's true.

Scott Knudstrup: On the learning side, too.

JHawkins: If I see a new object and want to put it in an existing class, you definitely want similar features and similar orientations. They have to have a commonality. If I say, "Here's a new thing, I don't know what it is," then if it has some similarities—

Viviane Clay: There seem to be two different signals, or two different ways to put things into the same category with different states. One is similarity, like morphological similarity, such as different mugs. The other is time—all the object behaviors, where we know it's still the same object because we've seen it transition from one state into another. With time, because we see the transition happening, there can be a lot more change in morphology, and we still keep it as the same object or in the same reference frame but with different states. But if we don't see that transition and there are actually different instances of objects, it seems much harder to say, "Oh, this should be in this reference frame," even though—

JHawkins: Yeah.

Viviane Clay: French?

JHawkins: I was trying to imagine someone saying, "Link, I know this looks like a teddy bear, but it's actually a mug. See? It's a mug." What would you say?

Hojae Lee: Sliding your child.

JHawkins: Maybe it's a—

Scott Knudstrup: Hyper science.

JHawkins: A mug in the shape of a teddy bear. But then you'd have to see there's an opening, there's liquid in it, or something like that.

Ramy Mounir: There's also affordances. We put things in a specific category based on the affordances, and they could have completely different morphologies or features.

Niels Leadholm: That feels more like a model.

JHawkins: But—

Niels Leadholm: A chair or something—it's something you can—

JHawkins: Can you have affordances about similar morphology? It seems like you have to have some—

Niels Leadholm: I think they could be linked. You could learn that chairs have the behavior that you can sit on them, but they also tend to look like chairs. But you could also independently decide, "That is sufficiently chair-like for my purposes right now."

Ramy Mounir: Or just things that could be eaten, like fruits, which have completely different morphologies, like a banana and an apple. They might not be affordances, but they appear in the same context together, like in a fruit basket, so you label them together as the same category.

JHawkins: Hearing this conversation made me think of something worth mentioning. I think about the chair example—there are objects I have, and I know what they are, but under certain contexts, I want to use them for something else, like a tool. Sometimes it's something that's not a chair, but I want to use it as a chair. I know it's not a chair, so I have a model of this thing—it's not a chair model, it's something else. But I want to use it as a chair, so it seems like you have to take two models. You need a chair model, and you're trying to apply the chair model to this other object. It's like saying, here are some predictions from Model A, which is a chair, and here are some affordances or behaviors of Model A. Let's see if I can make it work for this model of B, which is not a chair. I don't think B is a chair. I might use it as a chair, but I don't think B is a chair. I'm not going to relearn B as a chair. I want to be able to make predictions about it—can I sit here? Will I be able to lean back on this? Is there a cup holder? I might want to take knowledge about the chair and try to force it onto this other object to see if I can get it to work. I think that's an interesting observation. We do that all the time.

Niels Leadholm: Rude.

JHawkins: New tools and stuff.

Hojae Lee: Yeah.

JHawkins: It's like saying, I don't want to relearn the non-chair object, but I want to be able to use it as a chair, or use it as something. I'm not going to relearn it, so I have to take one model and enforce behaviors and morphology predictions onto another one.

Viviane Clay: Or...

JHawkins: I don't know how...

Viviane Clay: We can take the model of our body and run a quick simulation of sitting down on the thing, without going directly from chair to chair model. That feels more like what I do. I think about...

Hojae Lee: Do it.

Viviane Clay: If I sat down on it, would it be comfortable? I don't know, it feels like I'm—

JHawkins: That may be true of chairs, but sometimes I'm doing some work and I need a tool. I don't have the right tool, so I start rummaging around, looking for something that might work as this tool. This could hold this—

Ramy Mounir: It's like we're computing similarity along a specific dimension, because similarity is a very high-dimensional thing, and we're singling out or attending to only one dimension in the similarity space, just computing similarity between objects.

Niels Leadholm: I guess in a way that can generalize to a totally novel situation. Through using that kind of structured representation, you can see something like a penguin-shaped statue, and you will have never computed the similarity of that to a chair. But if you can just mentally imagine sitting on it, or—

JHawkins: It's almost like I take a chair object model and say, there should be a flat, horizontal surface about here in my chair model. Can I project it onto the reference frame for the penguin and see if there's some flat surface like that there, or where is the flat surface? It's amazing what the brain does. It's so complicated, but we do this, and we know it has to happen.

That's the core of what we've been talking about here. It's a way of taking a model and using it in a way that doesn't require relearning what the model is. In some sense, it's a way of sharing knowledge to a new model without relearning the model.

Niels Leadholm: Misha, I saw you posted some interesting questions. Feel free to jump on the call if you want to voice those, or we can discuss.

JHawkins: Did you just post those now?

Niels Leadholm: It was in the chat.

JHawkins: Oh, in the chat.

Niels Leadholm: But anyway...

JHawkins: Yep.

Niels Leadholm: It was in the midst of heated discussion.

JHawkins: Oh, there we go.

Misha Savchenko: I'm driving, so I never—

Niels Leadholm: Oh, okay. No worries. I can also read it out for you if you want.

Misha Savchenko: Sure, thanks.

Niels Leadholm: Cool, no worries. Misha, I guess first we're just making the point that we were using the term "averaging," but "generalizing" is maybe a better conceptual—

JHawkins: Why is that? I don't have an objection, but I don't know why.

Niels Leadholm: I'm assuming what you meant, Misha, is that what we're describing is a model that generalizes across specific instances.

Misha Savchenko: Yeah, "averaging" just has this mathematical or morphological connotation. Jeff, you pointed out that you don't really want to average completely different morphologies of things that still belong to the same class, but I think it's appropriate to think of it as a general idea—the idea of many trees and what a general concept of a tree is.

JHawkins: The nice thing about averaging is that it's a specific mathematical thing, but generalizing isn't. So maybe what you're saying is that it's probably not averaging, but we still have to come up with some sort of generalizing mechanism, which we don't know what it is yet.

Misha Savchenko: Yeah, exactly.

JHawkins: I see.

Niels Leadholm: And then, like you said, Hoji—

JHawkins: It's a vote against averaging.

Niels Leadholm: I think what you were getting at, Jose, was things like PCA or whatever—generalizing a distribution of points. The grid-constrained models that you implemented, Vivian, already do something interesting that goes beyond just averaging. There are points in the code where averages are taken, but that isn't the key part. Most of it is about local averages. Most of it is about storing points. It would be interesting to throw a bunch of tree images at it and see what it learns.

Viviane Clay: At the global scale, it's really K winners of the most consistently observed locations.

Niels Leadholm: So it's a morphology.

Viviane Clay: If you've only seen point A and C, it wouldn't average to B; it would pick A or C, depending on which was observed more often.

Niels Leadholm: If you had a crescent shape with many observations along it and a few that went off the crescent, most would fall along that crescent, and that's what would come out. Many trees are bent, but most have a roughly upward trend, so you would get that kind of result.

JHawkins: The more I think about this, the more I feel like this averaging tree idea isn't right. What kids draw is a little lollipop—they stick another thing on top. Very few trees actually look like that. They're really different. There are some trees that are lollipops, but maybe what kids draw isn't an average; it's just that someone showed them a tree and said, "Draw a tree like this, make a circle on a stick," and that's what they learned.

Niels Leadholm: It's difficult because when we talk about what people or children draw, it's entangled with your internal representation and what you're able to produce, which aren't the same. We've discussed how people are terrible at drawing and the different reasons Thousand Brains Theory might explain that.

JHawkins: I'm not sure I buy the average or even the generalizing idea.

Viviane Clay: I think the statistical frequency is probably better than averaging, but another thing we could look at is how predictive it is for different instances of the model. We would only store points in the general model if they're consistent with most other states. There's no point in storing a point in the general model if all the specific instances overwrite it.

JHawkins: I'm not going to think about the averaging idea; it might be a red herring today. I'll keep it in mind, but I do think...

Viviane Clay: Not at all, because it was the only solution to not having to relearn everything. Taking out how it's generated, I agree it might not be an average, but there should be some kind of generic representation to look up a feature if we don't have it in a specific model.

JHawkins: I don't know. I'm thinking of the tree example. I think kids learn that's how you draw a tree, not that they observe trees and then generalize.

Viviane Clay: I agree. I'm not talking about drawing, just about how you would learn them without having to relearn all the points in different states.

JHawkins: But how to learn what?

Viviane Clay: How do you learn a new state without having to relearn all the points?

JHawkins: I thought we...

Viviane Clay: We have a generic model to look at.

JHawkins: I think that's the key I'm going to try to solve: imagine I don't have a generic model. I have a bunch of models, each with its own context, and these models overlap. Many have the same features at certain locations. The assumptions never have to be relearned; the knowledge is there. The question is, how do I make sure I use the knowledge that's already been learned fruitfully? That's the working assumption and the task to solve.

Ramy Mounir: I think it can be done without a generic or default model.

Viviane Clay: Do you just look up in a random other state?

JHawkins: No. Imagine every location—you might have something stored, or you might not. If you have something stored, there could be one thing or multiple things, depending on the context. We take that as a starting assumption. If something was learned at a location, it'll be there, and it might be consistent with one or more contexts. If I'm in some context and there's a feature there, and my context isn't associated with that feature, then I would associate that feature with my context.

Viviane Clay: What if you're in a context and haven't stored a feature for that location?

JHawkins: There's still a feature stored there; my context just doesn't predict it. But there is a feature. The feature could be recognized, and the context is an optional override. It's like it's coming on Layer 1, and there are things learned there, but now I can—maybe it would default to one of the other states, whatever one is available. I don't have to make it work.

Viviane Clay: That's the core problem I was trying to solve today: what state does it default to?

JHawkins: Now that I have a clearer definition of the problem, I'd like to think about that. That's it.

Misha Savchenko: If there's no general model, then what do you do when you're asked, "What is above the tree trunk in a tree?" How do you answer that if you don't have a general model of a tree?

JHawkins: You have models of trees. There's no question; you have knowledge about that. You're assuming there's general knowledge as opposed to specific knowledge. I could learn one tree—if there's only one tree in my life, I could learn that tree, and if you ask, "What's above the tree trunk?" I can tell you. I don't have to have a general model for that. There are also many trees where you can't answer that question because the trunk isn't visible; it's hidden.

Viviane Clay: You're looking at a new tree and recognize it's new because the trunk at the bottom looks different. You have a different context now than before in the tree class. Now you look up, and you can still make a rough prediction that you'll see some leaves there.

JHawkins: Just because I have a new context doesn't mean—I'm trying to get to the point where if my context doesn't say something about a particular point, I'll default to something else, whatever else is there.

Viviane Clay: Okay, so then, I'm not sure.

JHawkins: Christians, do you want to default to the default model? I'm trying to avoid having a default model.

Niels Leadholm: Maybe one thing is...

Viviane Clay: Too.

Niels Leadholm: Maybe the one thing...

JHawkins: No, I have to figure it out. You have to let me work on it.

Niels Leadholm: This came up at the end of your document, Jeff, and I think it was what your other question was referring to, Misha. We can also have columns with different models. You can have a column that has learned a more coarse model of trees, so it's closer to the lollipop representation, even if it's not exactly that. That might be due to sparsity constraints when trying to learn a complex object without much representational capacity, or it could be from having large receptive fields with blurry input features. Maybe, but with specifics.

JHawkins: In the tree example, I've argued that we don't really see trees that look like lollipops. It's very rare, but you might have a column that only looks for—

Niels Leadholm: Green blob... not green blob, but it just...

JHawkins: I'm just saying, I don't think that— I don't even see that in nature. Again, going back to the tree example, maybe your point is still valid, Niels, but in the tree-specific example, I think kids draw the lollipop because that's what they're told to draw.

Niels Leadholm: Sure.

JHawkins: It does.

Niels Leadholm: But yeah.

JHawkins: That's not what they see anywhere.

Niels Leadholm: Circling back to the motivating problem, we know a model of a mug. Now it's got a chip in it, or something like that. How do we represent that and predict it without having to relearn the model of the mug? One valid approach, which you discussed in the document, Jeff, is maybe you have different columns with different models, and some of those columns update their model, but others keep them the same.

JHawkins: That would be true, certainly, for different modalities. For example, if one has a colored spot on it, you wouldn't feel that, you would just see it, but I don't think that's a general solution. I missed that in my write-up.

Niels Leadholm: Yeah, I'm just saying it's...

JHawkins: Problems.

Niels Leadholm: It's not the solution, but it's another one to consider.

JHawkins: Here's another way to think about it. Maybe I'll try to solve this problem the way I want to solve it, and I won't succeed, but I'm going to try. One thing I realized is that in terms of providing context, we really don't have any good— we're just throwing it out like it's something, but we don't really have a good example or understanding of it. In the staple example, the context had masking that went along with it, or something like that. Maybe the solution to what I'm trying to achieve is having a better understanding of what context is.

Viviane Clay: I feel like we have two examples of what it could be already. One is the feedback connection to Layer 1, which could give a context signal. The second could be the time signal in an object behavior. Those won't really work for object categories, like which type of mug instance it is, but...

JHawkins: I guess what?

Viviane Clay: Still, it helps to think through some examples.

JHawkins: There are also examples of contexts that are really out of left field. Often we have surprising predictions based on some sort of context, like something Neil said earlier today about his house. In that context, I make different predictions about something we're talking about now. Something I saw this morning in my yard changes what I think about something else later. Context can be all over the map. It can be very specific, but also really strange, and time is just one of those things.

Niels Leadholm: Circling...

JHawkins: Boom. Yeah.

Niels Leadholm: Like what you were saying, Vivian, is there a reason it couldn't be the first, the L1 feedback, that couldn't impact class? If L2, L3 neurons have apical dendrites going up to L1, it feels like that would be a good location to influence the object-level description.

Viviane Clay: Yeah, I think it would be part of that solution. In my head, it seemed a bit of a chicken and egg problem. The lower level is trying to say it's the mug with the logo by recognizing the logo, and the higher level is trying to give it the context. But, yeah.

Niels Leadholm: I agree.

Viviane Clay: Nothing.

Niels Leadholm: I was thinking about this before—if the state or context is represented in the apical dendrites, how is that communicated up? It feels like there might be different places it's represented, or different representations of it. One might be what is active in L2, L3, and that could be passed forward. Another is the feedback, more like L6 to L1.

JHawkins: Maybe. In general, there's a lot in the brain that projects to Layer 1. We've talked about time, matrix cells, other regions, and unusual things all over the place. Emotional saliency issues—neuromodulators are often released in Layer 1.

Viviane Clay: Perfect.

JHawkins: It's done.

Viviane Clay: We're looking for the context signal, something where we can get a bunch of different types of signals.

JHawkins: Imagine Layer 1 as a bath of noise going past all the time about different things that might mean different things. The columns don't really know what most of that is; it's just activity up there. The general idea is they can pick and choose anything that's helpful associatively from that point. Layer 1 has very specific projections, like we did in our paper and as O'Neil was just talking about, but there's also all this crazy stuff—everything goes up there, it seems, which is good. We want broad context, and part of being smart is recognizing an unusual context as a predictive mechanism, something someone else didn't pick up. Damn.

All good.

Is there—let me ask before we end today—if I'm wrong, and there is a default model, not even an average one, just the default: we learned this, and now we're learning variations of it. Were there any problems with that we identified? Were there any specific problems?

Viviane Clay: I don't...

Niels Leadholm: I don't think so. I think the main one is how we derive it, because—and I think that's maybe what came up when you were presenting that, Rami—we were discussing how you would average the morphology points or something like that. We were concerned, like you were saying, Jeff, that depending on what system you're using, you might end up with a total mess.

JHawkins: I'm not...

Niels Leadholm: It feels like there are many different approaches.

JHawkins: I'm not interested.

Niels Leadholm: The one we have is already fairly sophisticated.

JHawkins: I'm not excited about the advertising video. Do we need that, essentially?

Niels Leadholm: I think averaging is really a term worth avoiding.

Viviane Clay: Yeah, basically, just a generic model.

Niels Leadholm: Or kind of distillation?

JHawkins: But is a generic model learned, or is a generic model...

Viviane Clay: Distilled, or...

Niels Leadholm: Computed?

Yeah, computed. No, it's definitely learned. I feel like it has the attributes you wanted, which was, like, the first model you ever learn is going to be like that, but then, as Vivian says, as soon as you learn a second model, it's going to be unlike any model you've ever seen, any object you've ever seen.

Ramy Mounir: It feels more like we're extracting the variability, so it's like we're subtracting the variability from the model that we learned, and then we're building associations with that as a state. It's exactly like what Tristan is doing with extracting a functionality from a class, assigning a default class, then building others and assigning different connections to those extracted functionalities. We're removing the variability and then assigning it back as an association, building associations with different other variabilities or with different variations of that class.

Niels Leadholm: Which fits with maybe the language you were using, Hojab—maximum variance. There's some way of representing most of these things and accounting for most of the things we observe, and then there are slight deviations from that. The slight deviations are the states, and the generic description is the...

Scott Knudstrup: I think...

JHawkins: That's alright.

Scott Knudstrup: One nice aspect of that description is that when there are areas with a large degree of variance, that's a good signal that the prediction is not necessarily strong. But areas where there's a great deal of consistency, we ought to have high confidence in our predictions to locations like that.

JHawkins: Unless the variances are associated with very specific instances, right? If the variance is associated with very specific instances, then those are significant.

That's part of the problem. When do you assume things are unique? I have one last thought before we're done for the day. I'm working on another idea, which is really confusing. You'd think today is confusing?

But I'll throw it out, because maybe it'll spark something. In our models, if we think about layer 4, the feature layer—I'm going to talk about the neuroscience now—we have a representation where the mini column represents the point normal or the edge orientation, and then the cells in the column uniquely represent specific instances of that edge. So it's a generic edge, and then a very specific location on a specific object.

I was wondering if the same thing is happening in the location signal. There are many columns down there with similar properties. In the idea that you'd have two representations of location: one is a very generic one, almost pure grid cells—maybe only 10 or 12 different grid cell locations that a grid cell can represent, something like that. Then, in a minicolumn, you pick particular cells that would represent specific locations. So you have a generic feature, which is really just an orientation, and then specific features; and on the bottom, you'd have generic locations, which are not really unique, but still something, and then specific ones. When we were talking about things like averaging or fuzziness, it's just the idea that the brain could be taking advantage of the same sort of mechanism we see in Layer 4. Could a similar kind of mechanism be going on in Layer 6, where we have a very low-resolution location and a high-resolution location?

Niels Leadholm: Yeah, like what Rami was showing before.

JHawkins: Thank you.

Niels Leadholm: Remember that when he presented that...

JHawkins: The one with the pictures of the mugs we saw earlier today?

Niels Leadholm: Yeah, the...

JHawkins: Dimensional change card slot, I don't remember seeing this.

Ramy Mounir: The wrong ones.

JHawkins: I would remember rowboats if I'd seen rowboats before, so I don't think I've seen a rowboat.

Ramy Mounir: Hold on just a sec.

JHawkins: Are you guys hearing that? There's a noise outside my window, are you guys hearing that?

Ramy Mounir: Okay.

JHawkins: Oh, this thing here, the generic and specific. Oh, really?

Ramy Mounir: So I was thinking...

JHawkins: Put it...

Ramy Mounir: What did you conclude from that? We were thinking that we would have, just like we were having in the Layer 4 features representation, and then we also suggested that we would have the same thing in Layer 6 also.

JHawkins: And how did they proceed? What did you learn? What did you gain from that?

Ramy Mounir: I don't know, I felt it was a good idea. I didn't really.

JHawkins: All right, so I've thought of this idea before, forgotten about it, and brought it up again this week in my thinking. Maybe you were thinking about it too, or maybe this is from somewhere else, but yes, this is the idea. I'm not sure where the arrows go. You have these two representations, but where do the arrows go? How do they interplay with each other? When do we use a very coarse coding of space versus encoding space? We have some ideas of when you'd use a coarse coding and features versus fine features. We can see the advantages of that.

Tristan Slominski: Also, I'm not entirely convinced that the generic location is actually Cartesian at all. It could be a toroidal thing, like Jose mentioned before, where those generic locations are not Cartesian 3D at all.

JHawkins: They're right. They would be toroidal, because if you think about pure grid cells—imagine grid cells—if you just take one grid cell module, it has maybe 10 or 20 different locations it can represent, and they repeat over and over again. It's often described as a toroidal space. What it does is say that particular representation could appear in many different places in the world. It's not unique; it doesn't occur everywhere, just one out of 20, or whatever it is. So it repeats over and over again.

Just an interesting tidbit: when grid cells were discovered—what's his name, the guy who discovered—

Niels Leadholm: Closer?

JHawkins: No, Mozard—

Hojae Lee: O'Keefe.

JHawkins: O'Keefe, O'Keefe.

Niels Leadholm: O'Keefe was place cells, right?

JHawkins: He's just got a place.

Niels Leadholm: No, sir.

JHawkins: And then the Mosers discovered grid cells, and O'Keefe—they're very competitive people, as far as I know—and O'Keefe at one point expressed disappointment that he didn't discover grid cells too. The reason he didn't is that where he was looking, the grid cell spacing was so large that they didn't actually repeat within the environment. They were representing the space and the environment, but they didn't actually wrap around the torus; they didn't repeat again, or it was so far apart that they didn't see that. With these interesting observations, it means that many times you might just have a coarse coding of space, and you don't have this toroidal aspect yet, not repeating a lot, and having coarse coding.

If I have a large enough receptive field for the grid cells, it's just a fuzzy representation of space. It's not repeating. Each grid cell would represent a fairly large area. Something else to think about in that picture you made.

Ronnie.

Niels Leadholm: Cool, yeah, that seems like a good stopping point.

JHawkins: More stuff to get confused about. All right, we'll get to the bottom of it, I'm sure.