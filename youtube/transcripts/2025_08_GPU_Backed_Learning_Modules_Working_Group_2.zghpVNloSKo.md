All right.

so last we, left off, from what I recall is we were talking about, let me share for context.

we are talking about.

the issue where it's unclear how to parallelize across object graphs.

I think what we can spend today on, or at least start, is to think through and define how to paralyze object graphs. basically hypothesis because hypothesis update, calls are per object graph. And to that point.

make this bigger so it's visible. Okay. So to that point, this is, evidence graph limb. And we have a hypothesis and it has an update evidence call and we, and inside this evidence call, it has calls hypothesis updater and it calls Update Hypothesis. And we notice it's per graph id, so it's getting per graph id. And the issue was. So that's the context for it. So one, does that sound like a reasonable place to try to resume and figure out what we remember? Yeah. No. Sounds good. Alright. we also, do you recall any of our, grouping LMS discussion? Yeah. so I haven't made any progress on that. that's still there. actually let me switch my sharing mode so I can share the desktop instead.

There we go.

so yeah, so that's, still a to do over here on the refactor stuff. I have, not made progress, but, yeah, so I realized that. So one thing, one, one thing about, I've noticed as I was peeking at this, like in the few minutes before the meeting, Was, it's, I guess we can trace up of where all this comes from, so Update evidence takes in a graph, and so wherever that gets called is gonna be, here. So this is interesting, right? So this is how it gets split up by graph id. But there is already, there is a, there is, yeah. Yeah. So C threading looks promising. Yeah. Yeah, so I think we would definitely need to fit however the paralyzation is happening, whether it's the CPU backend doing multi-threading there, or the GP doing it and batched operations into the backend. So certainly it seems like this logic here that's going on in the. Graph right now will need to be shifted to the backend, but Got it. Is there an issue with anything about the current, placing the code there? I don't know, mean conceptually to separate into the, backend. Are there parts of this that it shouldn't, the backend shouldn't be aware of?

I don.

Doesn't seem to be, no, that's, I don't see anything because it's like we either, spread, we either scatter here And then gather here.

Oh, no. This is where, oh, we don't, haven't even defined it. yeah. So if we use Multithreading Scatter Gather. Okay. the thing if. We were talking about kinda with like LM groups. Yeah. Ideally we would want every LM to do the scatter Yeah. Before doing a gather so that we could use different CUDA streams to parallelize even across lms. I think within an LM doing it across the object graphs similar to the implementation I have right now.

Figuring out, I, I think it's a bigger code rehaul to have the scatter come before they gather for all LMS at one time.

we can, explore that, right? Like we can see We can do a. Kind. Don't chase that down. So this is update possible matches. I'm not seeing any references in this file, so think it's called in graph lm dot compute, possible matches.

I have a little right spec I just did earlier. Yeah. This one, right?

So that's, this is per learning module. Ah, okay. There we go. Yeah, I was like, okay. So it's per learning module, so complete possible matches, and then I think above that it's the matching step, the function also in graph.

Yeah. Up here.

Okay. It's still our learning module. Yeah. We just have to just turn this interface and set out, basically. Yeah. Right now we're telling the learning module, do these steps and instead we're gonna do these steps with the learning modules. That's the entire refactor.

Okay. Yeah, and so it's, yeah. Monty for graph matching step learning modules. Where it actually iterates over the learning modules. So I think that's where we would want to switch to a non-blocking scatter for every lm and then a gather for every lm hit Monte for graph matching. Oh, unless something's changed is, from the code a few weeks ago.

There we go.

Okay.

Yeah. Yeah. So this is what's gonna get, yeah, so instead of forward this, oh, It seems, it feels like it should a difference because.

The logic is still at this level. So whether we do it for here or whether I'm just thinking at the logic is at this level of abstraction. Either way, we either do in a four loop and call specific methods, or we can call the specific methods and pass in the set. Like it should be the same thing. Okay. And passing the set. Yes. So You're saying if we had a collection of all LMS to do the steps Yeah. And pass that into the backend Yeah. Object basically. So it would be like this Monte for graph matching references that like hypothesis update that can operate on all LMS at once because like right now it, it's, I, for graph matching has a. Isn't aware of the hypothesis update or it just has a list of lms. I don't think Yeah, I hear you. I'm thinking, I don't wanna go directly to hypothesis update because that's like in, in like internal guts of learning module.

I'm just trying to figure out how to represent it. So, it's accessible, but it's still, yeah. And so if we didn't want to expose the internals of the learning module, backend or hypothesis updater to this, 1D for graph matching class, I think we could still leave it inside the learning modules, but that's, yeah. Where we would have to yeah, iterate over every LM and dispatch the work and then out and then outside of that loop in the next step. I need to collect. So do the scattering gather in two different loops?

what the, what, what information do we need?

I, guess what I'm trying to figure is like, what info do we need to expose from a learning module to get to, to be able to do parallel compute here? With a GPU backend, right? oh, wow. This doesn't, this is not gonna wrap for me. Okay. I need to wrap it. Okay. So I guess what I'm trying to think is okay, there is, if instead of we wanna do four, instead of do this, we wanna have some function right? That will, so what are we doing at four if sensorimotor, there's input. So we're gonna, so like he, like this is. This is a weird way, this is a calling it per learning module function, right? And so what, I'm saying is we should be able to do, instead of doing that, we should totally be able to just do this, right?

Something like that, right? Although this would be like, for Allems or something like that, there. Like, how, do we avoid the for loop, right? So, the first thing I'm seeing is we would need something like this, and then I want a step method. Okay. And this is called per learning module. So there's some so this is like self step learning modules and it's against self-learning modules.

That's the next, that's the next step is does. So here, let's do this.

this should, this ought to be replaced with that.

ought to be able to. so this should be able to be replaced with something like that, right? Because Oh, and, still sensory inputs. So still sensory inputs for all lms, this starts to smell like the same function really? 'cause it's got the same signature. There's not, easy to break it down, right? Because this, what is the difference between set? Stepwise targets and then calling the step method. Let's fine out set the stepwise targets for each the class label of the object that is actually receiving sensory input from, oh, this is an experi, this is baked. This is some baked, baked, an experimental framework.

We could just, yeah, I don't know if how important Yeah. This, is one, this is an issue with. The coupled experiment and the actual multi framework thing. So let's design it without de coupling first. sure. So going back would be, so this is an, so this so says step, set, step ways, targets is a experimental experiment, method versus this is the actual Runtime method. I'm gonna say runtime for the Monte system and experiment for experiment specific operations that are doing stuff. so this would be like an experiment method. This is a runtime method. And so we can see that. this processing, yeah. So this, this is basically this right step learning modules.

I'll just call, technically we can maybe do it like it's a step type there, just to be clear, self step type learning modules.

'cause it have matching step or evaluation step. but doesn't matter for the purpose of what, we're thinking about here. So that's paralyzed. over here it just skips. Yeah. So if the sensorimotor input is not, there's nothing to do. Yeah. So this could be like a no up. Yeah. And if we had a part of the, function that we're calling there, if it doesn't have to be handled in this function. Yeah. I'm, just marking no up. It's like in case that we don't wanna have this branch then, maybe something. Does that make sense? Yeah.

So now that I said that this is, per lm, so that means the whole thing is actually just this. so this function? so in my mind there is an experiment method that sets step by target for everything, and there is a runtime method.

That executes the step side, which is true. that's what step learning modules should do. and there is a, with a note that, note step might be no up if sensory input is not okay there, So this is Paralyzable.

and then we, so how did we get here? Because we were seeing, so this calls, we weren't here. How did we get up here? Because you, brought this up, but we were somewhere in the second. This was to get, yeah. And this was just to get to the level where, oh, okay. Iterating over lm. So everything else was per LM call. Okay, cool. so let's look at the matching steps and learning steps. So these will be methods on the learning modules that's matching. So yeah, so in that, step learning modules, we're now switching to instead of doing the four loop in that call, we want to call directly into the set stepwise targets or the actual, like matching step or exploratory step. We still have to either do the for loop there in that step or sorry, in that function, which would still be a part of this Monty for graph matching. Or we'd have to switch to find a way to dispatch all LM data to some sort of backend, which Gotcha. We didn't really want to do.

So right now we're shifting the for loop iteration to this other method. Is that okay with, is that kinda what you would like to see? Because I think we still have to do some level of this. Maybe it doesn't have to be explicitly a for loop in the code. But we still have to have, you dispatch all the work across LMS and then wait for that to be done and then collect all the data from the lms. And that needs to happen at this level before we get to the per LM level.

So one of the things I wanna get to is, so you how we talk about update possible matches here and, and, and we do, use multi multithreading here, right? And so it's but because this method is on the single learning module, then. The maximum parallelization we can get is per graph ID in a learning module. But what we're trying to get to is how can we paralyze across a bunch of graph IDs and learning modules Like, like we wanna paralyze across all learning modules, right? and so right here is a constraint that what, I guess what I'm trying to imagine what the API looks like.

And so yeah, the joy of life design.

I, guess I, I think the, problem in my head is I'm looking at is here is a for loop. Anytime we have a for loop like this, we can paralyze it by passing a set. At certain point and as long as the API I, I guess what I'm saying is if we look at the current implementation and we see a for loop that iterates through a list, then we have restricted that is a restriction of how much can be paralyzed. Because I can't, because now I just said.

I can't, because this method is called for every learning module, then I for sure have to have a for loop somewhere for every learning module to call this method. I can't say call this one in parallel for every learning module. So it's because.

This parallel, this can, like this for loop can be parallelized across graph IDs, but this method is not yet parallelizable across lms. Yeah. So I'm trying to look it up with here where it's like this method is parallelizable across all lambs and I'm trying to get them to meet so that the interface of the these so I don't wanna go up from here. Down from here and see if I can meet them while maintaining the parallel interface. I think it, it's still like the mechanism of how they're being paralleled still matters because if, when you want to call it on a set of learning modules instead of a before loop How, like right now you like this. For graph matching just can directly interface with every learning module separately. But if we want to run those learning modules as a set, how do we represent that? Because that's where we would need one runtime to handle that logic of setting up all the data for the, inputs to the lms running them in a batch. So that would change the dispatch structure to now be. Having some representation of multiple LM dispatch, whether that's a hypothesis update or some new class that runs 'em all in parallel. 'cause I just don't see a way that we can just run these steps for all learning modules in parallel and just have this Ponty for graph matching only reference those learning modules. And I have some other sort of collection. Paralyzation object that tracks that. Unless we still do a for loop approach, but we do the non-blocking case that we were kinda talking about last time, where you can still iterate over each learning module, but you just need to make sure that each iteration of that loop doesn't wait for the work to finish. It just dispatches the work. And so then that for Loop will end before any of the work's complete. It's just dispatched it across all LMS and then you have another for Loop that, or you don't plan, not for Loop, but, this thing. You're just gonna literally do this and they abstract. Yeah, but that's because you're actually multi-threading would be different than GPU dispatch here because we can split the CPU process to do multi-threading. No, Or we still want one CPU process launching all of this work on one GPU.

So I think the four Loop approach would be fine. We would just need to shift it so that instead of doing all the work in one call to the lm, we switch it to, do you have a dispatch call and then you have a sort of like waiting call and like a collection call. So like scatter block gathered.

Does that make any sense? I think so. Do you have something in mind?

I don't have anything to type. I'm still thinking through what you're saying. If you have something to type, let me know. I'll give you the screen or take the screen. I'll just so we're looking Yeah. Update the possible matches there.

I think we would want to, we would want to go back to the higher level, like the step learning modules, right? So there, so like that four. Of learning modules. I think we want that to do dispatch the work for each learning module in that loop.

I actually already had some of this written down in that function.

so yeah, we would have the dispatch step. Are you sharing a screen or something? no. I'm just looking over my notes. Oh, okay.

and then we'd have to have some, what I have was, still having the, Monty for graph matching, have a reference to the backend so that it can Yeah. Call we'll still we'd have a single backend that's shared between all learning modules. Yeah. so we have something like, self backend. It should have a wait until complete call. Something to let the, yeah, so what's the, so what's the API of the backend that you have in mind? So it's join, would it be the, join, join all of them if we just use the multithreading or, is there a GPU term? I think, yeah, this just needs, we, we need to have some call to just wait for the work to complete. Yeah. John, okay. And then how do you, and then we can process all the results however we want. it just kinda depends on the downstream, how we'd like to handle the results of the LM update steps. But at that point, we're done with the hypothesis update or paralyzation. Okay. So like at that point, if we wanna loop through the learning modules and call some downstream effects or, if we just want this function to return up. So what's the high level algorithm here? What comes before the join? yeah, we just, we have, okay. So yeah, so that, sorry. So yeah, the, if we're getting rid of that for loop Then. It would just be like, yeah, dispatch join process results, like three steps. So it'd be, its learning modules, sensory inputs for alls, and then we would just join all of these guys.

it's not even at that point, it doesn't mean, yeah, the backend should be able to track whether it's done with all of the work. Okay. and then I guess. Dispatch something, right? There's like a method here, like a function to do, to run, or is this the, so the backends, because it's gonna, it'd be this, it'll define, yeah. I don't know exactly it, because this is where we'd have two different, we'd have support for different rapids, like CPU and dpu, so like they would be aware of. they would actually have to have different implementations of the fundamental operations going on. So we couldn't just pass in a function and have them Yeah. Run that. It would've to be like they, they know what the functions are and we're just calling into them. Okay. But yeah, there's still several points in the, current, stack chain through the right, through the learning module. So I don't know exactly how we wanna refactor that. Okay, but does this sound, so then it sounds we have a backend that's the abstraction and then it's gonna step all the learning modules and then quote unquote, the default backend would be this. Yeah. And then Versus the GPU backend would do something else. So what would the GPU backend do?

So this kind of depends on how we. Define like the LM groupings and everything. If right now we're just saying HLM was its own group or kind ignoring that, that change, then it's gonna do a different kuda stream for every learning module and dispatch the work.

So consider grouping of alarm in the learning. Modules call below, right? Yeah. Yeah. So if we wanted to do a grouping, we would want to iterate over those groups here and do Yeah. But whatever that grouping is, we would have the back end would basically run a different cuda stream for each group.

And then in that join step, it has to wait for all of those kuda streams to finish before. Processing, giving you back the results, however you wanna do something. Okay. So it's so for group and groups, this is Theda, Budda backend. So for group pseudo coding here, so for group and groups, we just dispatch the work, some sort of, yeah, dispatch stuff.

And then the kuda backend join has to happen once that for loop's done. It has to be outside that for loop. Yeah. So this, this is just that. Yeah.

Okay.

All right. Does that making sense? I think so.

so we did that and then when there, okay.

Yeah. Gotcha.

Oh, Yeah, so then do we need anything else collect for the Cuda backend dispatch? So what we're talking about here is actually running this step, right? so we still, it's this needs to be. Like a matching step. let's see. Graph learning. Don't care about tests.

okay. so we have where the.

There. Graph alarm. Cool. Yeah, I can, because I traced this earlier, trying to send in the chat just like the list of, function calls. Okay.

That contributes to send messages. Yeah.

in the chat. Okay, cool. So that's the traits here.

Okay. So in matching step.

Okay. But it's, an observations. So this needs to get rewritten it then, because it's a learning module thing.

So it's, all, so there's gonna be a cuda backend matching step learning module, matching step that's gonna take learning modules and whatever, right? That's, how the translation would likely go. That's what I'm trying to think through. So this batch, but in there, that just means could have backend. So this is matching step four.

yeah, essentially have to expose all the algorithm.

there we go. Alright.

This is compute possible matches. It's gonna do a bunch of stuff.

it's gonna be, oh, it's on the same. Oh, okay. I was like, why am I getting, it's the same file. Got it.

I was like, confus myself there. There we go. All right. so we have, there we go over here. So we'll come back to it. All right. So we have, DA matching step. And there is a complete possible matches per group.

I lost my sensory data somewhere already or Right.

the wait, this is inside.

Matching step. Observations. Observations. There we go. Okay. okay, this is, oh no, there it is right there. so group sensory inputs and then like you said, and then we're gonna do even more compute possible matches.

And then update. Okay. But at this point it just, okay, I think I understand now. So it just, it needs to be the, it just needs to, so at a high level, okay. Let me just see if I'm Tracking what you're saying. So whether it is grouping or not, the point being is there's a backend. The backend, instead of doing a for loop, it needs to, it's gonna be just get all the learning modules and all the sensory inputs, and if it's a default backend, it's just gonna do a for loop and do whatever it's doing today. If it's a cuda backend, it's actually going to implement these other methods, which does that mean? Okay. But the, okay.

okay, this is straightforward, but now, like how does this code get organized because So what this means to me is that if we have, so any method that we flip inside out Means that the learning module, there's two implementations.

And they're, different, right? One of them is a method on the learning module. The other one, the learning module, is the data passed into the thing. And I think like in the, kinda proof of concept code that I have, the backend is really just implementing the. Hypothesis updater operations. And isn't trying to handle as much of the logic around the LM itself. And yeah, I think there's kind of two directions. We either have this Cuda backend, have to handle a lot more of the LM logic if we're calling directly into it at this stage, or we maintain that it's still. Kind of per LM that they handle their own sort of logic and, but it's just that we make sure that none of those calls into that LM through matching step compute possible matches, update possible matches, update hypotheses. None of those wait for the work to be done. They all just dispatch the work and then return so that from this high level step learning modules method, we can. Call into every LM and have it dispatch its own work, but all those calls return so that then we can wait for all that work to be done in parallel. So like each LM will still reference that single backend and it can still do the work in parallel, but the dispatching kind of control logic comes from the LMS themselves.

or we switch to trying to have this sort of more involved backend. Last second, keep track of some of the different settings per lm, or I think I finally understand what you've been trying to say. Okay, got it. yeah, so there is, so basically what you're saying is like with Acua backend, what we could do is we retain all this logic and as long as by the time we get to here. As long as it's not actually doing a compute, but just cues. A compute just Yeah. Just cue it. Yeah. Matches it, queues it up for later, whatever. It can still execute the exact same for loop, whatever, We just need to find the right place to come back and Yeah. And then be like, okay, join and now resume the other. Okay. Got it. Yeah, so like in my little code that I wrote before our last meeting, it was. It. I kept that same for loop that we have there in the code. And yeah, just change it to, instead it's just a dispatch instead of a compute call. And then once that for loop completes, then we have the call to wait on the back end to finish and then process results. But it would still require changing each of these functions along the way to make sure that it Yeah. Is just dispatching and not waiting for the results. But it wouldn't require as much code rewriting of what the backend is doing versus what the elements are doing. So, we would have to, but we would have to audit this thing to see where the previous results are being used, right? Because you cannot proceed past the, join past the gather in this for loop in.

Or can you or, can you set up the computation even with a follow on computation? if, I like, let's say, oh, this is made up, but I have two calls in a sequence. So let's say this call uses the results from this call. it could have backend have no problem setting that up.

Yeah. So I think what we would do. This is where, we need to have really good, clear sense of what the sequence operations could be. yep. But the lm, we could set it up such that the backend objects LM interaction, like it, it's aware of the pipeline of operations. So we can do one dispatch of that full pipeline. So we don't have to control each step of the pipeline dispatching and queuing and waiting in this level of code. We can just be like, dispatch this whole pipeline of operations parallel for each other. And so that, that's what, I'm saying. So yeah. So let's find an example of an that does this? I'm, slowly catching up, so thank you. Yeah, no, it's, kinda a weird program paradigm. Yeah. But I, think like, the flip the switch. I get it now. so now the specific question, what are we talking about? update evidence. Update evidence. Okay. So yeah. Yeah. Blah, blah, blah query. And the query has been, select features to use, get current display. Okay. is this expensive? Did you replace one of these?

No, I, only replace that hypothesis update or Ah, Update evidence. Oh, there we go. Right there. Okay, cool. Blah, blah, blah. And then hypothesis update. Okay, got it.

okay.

And so, basically this would switch, to become something like, we wouldn't have this equals yet. We would just have so hypothesis we, it would basically be.

the, the interfaces, we just have to change to something like this, right? Where it's just, wow. Thanks cursor. Okay, let me, it's like overriding tab is tab is a useful thing. Okay. so it'd be something, like this, essentially this is the dispatch. Yeah. And then it would be, then you get. Results. No. Then we have to stop. Then we have to stop here, and then later on there's an entire call, different call update evidence. And it's like process evidence or something, right? Like after the, yeah, so we wouldn't have it stop, we would just have it return. Because we want those, that higher level for loop to finish each of these dispatches. We gotta find these break points where it's like we need to split a method into the, before the dispatch and then after the join, right? Before the scatter, after the gather. What's, what terminology are you using? Cuda, because I keep on making it up. I've like scatter, gather, map, reduce for chart. Yeah. I think you can do a lot of things. I, think it's helpful. Just think of like, dispatch operations and then like block or wait for those to complete. Okay. Cool. So, non-blocking route blocking. So, we gotta do, so we gotta evaluate the functions and see which portions are dispatch and then where, and then everywhere we need to block, we need to essentially create a new function. Like we need to, split up functions at the block points.

Yes. Am I saying the same thing? unless it depends on what we want to include in the pipeline of operations, the backend's completing. Got it. Because we could still just, if you have that one dispatch and have that queue off, for that LM all of the hypothesis updating steps. Yep. and not have to mess with keeping track of that at the evidence graph LM level. Yep.

So I think, yeah, ideally whatever step this is running in the experiment, we just have one dispatch call, one blocking wake call. And then we take the results and continue with the next steps, right? Like doing LM voting and ting and goal states and all that. But all of the evidence update operations occur from this one dispatch to the backend pipeline. Got it.

Okay.

It smells a lot like initially at first approximation. it smells like a visitor pattern. Like I wanna pass it a visitor, like each one of these things, pass a visitor and then here be visitor, dispatch or whatnot.

let me, lemme say it differently. again, thinking out loud and raw, If we split it up, how do my CPU stuff works? How does my CPU stuff works? it's almost like I do yeah. I guess I'm just trying to figure out what is the common interface between that paradigm and this and the. Current paradigm, and I'm like, visitor smells like, maybe that's like adjacent to the right interface because if I, each one of these calls a specific method on a visitor, and if it's the Cuda visitor, it's gonna just cue the, dispatch the stuff. But if it's, I'm just trying to mention, but if it's a CPU visitor, it's then I guess it needs to immediately returns. Some yeah. I don't know how to design that. Yeah. and maybe visitor's not the right one, but that's what I reached for immediately here. yeah, I haven't, I haven't thought through the CPU side as much. Yeah. Kind do both. So like a simple kind of naive CPU backend, certainly for one, conceptualizing one step this would work. I'm trying to extend that to doing these sort of pipeline of steps. you could have it do multithreading or you could just have it. Do the full for loop and actually wait for each step to complete. But that kind of already changes the interface. 'cause you wouldn't have this dispatch wait process results call, like the CPU doesn't if it's operating sequentially.

okay. I guess the CPU backend, it's, just. It would calculate it immediately, but it, I would just have to just do a level of indirection. So if I, okay, so if I have a, so everything would have to be designed to support the cuda kind of dispatch and a block. And the way the, I think I'm now catching up how the CPU one would work is, and a CPU. Visitor when I dispatch it or, since everything is the same, API maybe don't need a visitor anymore. It's just the API. So when A CPU does it, it just stores the results in the variables in its backend and then when you call the things up the block, it just reads it from where it stored. It's just reads it from its internal state versus actually, versus like on a cuda. It's, yeah. Okay. Got it. So A CPU backend. When you would dispatch to it, it would actually do the computations right there and then, and it would store the results in its internal variables versus for a cuda dispatch, it would, start queuing things up to send off to the GPU. Then when the CPU back and blocks, there's no up, like all the results are already there. Versus Cuda blocks, we actually then wait for the GPU to finish and then we resume everything and the results are there either way. Like in the CPU Yeah, we block was the now up and the results were already there, so we proceed and the slope was the dispatch code and then the Cuda part block actually calculates the results and get some back and we proceed as well. Yeah. Does that sound yeah, actually I think that makes sense because. We could probably even switch the blocking call just to be a part of the, very beginning of the GPU's, process results. We don't even have to have, the blocking be made Oh, yeah. Available at this level. So it could just be dispatch work process work or process results. And the CPU just does that sequentially and then has 'em already. And the GPU does a dispatch them all in parallel. And then whenever you want the results, it first waits. For the results to be done and then provides them back to you. That's actually reasonably more in line with how GP programming typically works. Like you, just typical GPU programming, is it's like you have a CPU thread. Whenever you wanna run something on A GPU, you dispatch the work. And then it'll just automatically handle this sort of like blocking stuff. Just as soon as you actually want to process some of those results, that's when it will. It'll wait. So as long as you, do other things in the meantime before you process the results, it'll handle all of that running in the background. And then as soon as you want the results, that's when the CPU U Fed will then we stopped waiting for the GPU to finish. Got it. So we just wanna do the same thing and, okay, so lemme write up the GPU version. So backend, block or results to come back from GPU. Process results. And then GPU backend is, GPU backend is dispatch work to GPU?

Yes. And then return immediately.

And then it's and okay, and then CPU version, it would be, do the work. The work return after work is done.

And then I guess store, results in turn and, yeah. I think this is where we still kinda make a choice about where we want, what we want to be handled by the LMS themselves and what by the backend. Yep. Because if we still have it be that, like the LMS are have their own functions too. Set up and then dispatch this work, we can then still store the results in those lms. Okay. Yeah. Results without it being stored and handled by the backend. So somewhere, yeah. Or later retrieval. So it's could be backend intermediate VARs.

Could be learning modules. Et cetera. Okay. After the work is done, CPU backend, results are available. So process results right away.

Okay. This is promising. let me put this in chat so it doesn't disappear. so you can also see this Yeah. As we come in close on time.

okay.

I so we have four minutes.

perfect. Done? Yes. That's great. so, I guess, what, I, what we can, I can do is I, can write up my under, I guess I'll just post this in our discourse, Here. I can just pause this in a, discourse summary of this is the high level thing, and I'll think through what's the update about? actually, we got, we, we, made progress. I think we still need to get the details, but I think we have the level one, right? Does that sound right? Okay. So I think, so I'll report. Over here say that we do have a high level thing. I will try to describe it. Please correct me if I screw that up or whatever. And then, for the next time we'll be to see if we can, we should push that down, the details farther. but this has been super helpful, and thanks for, yeah. Repeating this time over and over again until I got it. no problem. It'll be, I'll try to also try to describe it. in my words as well, for anybody who comes after, lemme see to do. Yeah. And I could try to think through and make sure that this sort of high level plan I think would work with conceptualization of the GPU U backend and see if there's any problems I'm thought through.

and I guess, yeah, we just wanna make sure that. We're considering it now, and I think it, is, would work both for an individual LM or for a, an LM group if we wanted to shift to that architecture in the future. Will this work for both individual LMS groups of lms? Yeah. Perfect. And then the other thing I wanna do is just like find, yeah, I need to find the, process results points.

That might block or does that make sense?

that's the one that's, and I'm just writing the notes here, but I'll summarize It again, in the discourse.

okay. And this is, so this is a detail we don't have to, I think about right now, but I do wanna mention it just because it could impact how we think through the high level architecture. Okay. Traditionally, one of the most common bottlenecks for any heterogeneous programming where you're doing CPU and GPU, like this is gonna be, transferring data between the CPU and GPU. That's often much more of a bottleneck than actual compute running on the GPU. So the best way around that is we try to keep as much data resident on the GPU as possible, and I think it's conceptually very feasible because. The Monte experiments, like it is not like it, it really cares about a lot of the, those intermediate data steps. Like all the intermediate formats and the output of one GPU kernel into the next.

but it would basically just mean that anytime the LM does need to access its own internal data, right? look at an object graph It might have to read that from the GPU instead of just having that already in CP memory, which is like pretty easy to do. It's just like conceptually, we wanna make sure that this architecture works where we could keep as much of the data on A GPU as possible and prevent having to do these big data transfers and like just read back and forth, like the new inputs, whatever changes happen, and like the outputs at the end. Gotcha. Okay.

Good to know.

Alright, I'll, write up the notes summary. let's stop here. Cool. And, we'll catch up in a few weeks on yeah. when you get back and, go from there. Yeah. Sounds good. Okay. Awesome. Thanks. Appreciate it. Good to see you again. Interesting. It like progress for sure. Yeah. Alright. Cheers.