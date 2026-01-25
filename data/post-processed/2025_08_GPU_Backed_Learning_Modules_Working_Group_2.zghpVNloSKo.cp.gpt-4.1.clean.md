All right.

Last time, we were discussing how to parallelize across object graphs. The main issue is that hypothesis updates are called per object graph. To clarify, this is the evidence graph limb, which has a hypothesis and an update evidence call. Inside this call, it invokes the hypothesis updater and Update Hypothesis, both operating per graph ID. The context is that the logic is already split by graph ID.

Does that sound like a reasonable place to resume? Yes. Regarding the grouping LMS discussion, I haven't made progress on that yet. Let me switch to sharing my desktop.

That's still a to-do on the refactor list. I realized that as I was reviewing this before the meeting. We can trace where this comes from: Update evidence takes in a graph, and wherever that gets called is here. This is how it gets split by graph ID. There is already some threading—C threading looks promising. We need to fit the parallelization, whether it's CPU multi-threading or GPU batched operations, into the backend. The logic currently in the graph will need to be shifted to the backend. Is there an issue with placing the code there? Conceptually, is there anything the backend shouldn't be aware of?

It doesn't seem so. We either scatter here and gather here.

We haven't defined it yet. If we use multithreading scatter-gather, and with LM groups, ideally, every LM would do the scatter before the gather, allowing us to use different CUDA streams to parallelize across LMs. Within an LM, doing it across object graphs is similar to the current implementation.

It's a bigger code overhaul to have the scatter come before the gather for all LMs at once.

We can explore that. This is update possible matches. I don't see any references in this file, so I think it's called in graph_lm.compute_possible_matches.

I wrote a spec earlier—this one.

This is per learning module. So, complete possible matches, and above that is the matching step function, also in graph.

Up here.

It's still per learning module. We just need to adjust the interface. Right now, we're telling the learning module to do these steps; instead, we'll do these steps with the learning modules. That's the refactor.

Monty for graph matching step learning modules iterates over the learning modules. We want to switch to a non-blocking scatter for every LM, then a gather for every LM in Monty for graph matching, unless something has changed in the code recently.

So, instead of forwarding this, it feels like there should be a difference.

The logic is still at this level. Whether we do it here or elsewhere, the abstraction is the same. We either use a for loop to call specific methods or call the methods and pass in the set—it should be equivalent. Passing the set means if we had a collection of all LMs to do the steps and pass that into the backend object, Monty for graph matching would reference that hypothesis update, operating on all LMs at once. Currently, for graph matching has a list of LMs but isn't aware of the hypothesis update.

I don't want to go directly to hypothesis update since that's internal to the learning module. I'm trying to figure out how to represent it so it's accessible but still encapsulated. If we don't want to expose the internals of the learning module, backend, or hypothesis updater to the graph matching class, we could still leave it inside the learning modules. We'd iterate over every LM, dispatch the work, and then outside that loop, collect the results—scatter and gather in two different loops.

What information do we need?

I'm trying to determine what info we need to expose from a learning module to enable parallel compute here with a GPU backend. If we want to avoid the for loop, we need a function that operates on all LMs. For sensorimotor input, this is a per learning module function. We should be able to do this for all LMs, avoiding the for loop.

We'd need something like this, then a step method called per learning module—self.step_learning_modules against self.learning_modules.

That's the next step. This should be replaced with that.

ought to be able to. So this should be able to be replaced with something like that, right? Still sensory inputs for all LMs—this starts to seem like the same function, since it has the same signature. It's not easy to break it down, because what is the difference between set stepwise targets and calling the step method? Let's find out: set the stepwise targets for each class label of the object actually receiving sensory input. This is some baked, experimental framework.

This is an issue with the coupled experiment and the actual Monty framework. Let's design it without decoupling first. Going back, set_stepwise_targets is an experiment method, while the other is the actual runtime method. I'll say "runtime" for the Monty system and "experiment" for experiment-specific operations. So this would be an experiment method, and this is a runtime method. This processing is basically step_learning_modules.

Technically, we could do it as a step type—self.step_type_learning_modules—since it could be a matching step or evaluation step, but that doesn't matter for what we're thinking about here. That's parallelized. Over here, it just skips; if the sensorimotor input is not present, there's nothing to do. This could be a no-op. If we had a part of the function that doesn't need to be handled here, I'm just marking it as a no-op, in case we don't want this branch. Maybe something like that. Does that make sense?

Now that I said this is per LM, the whole thing is actually just this function. In my mind, there is an experiment method that sets stepwise targets for everything, and a runtime method that executes the step side, which is what step_learning_modules should do. Note that step might be a no-op if sensory input is not present. This is parallelizable.

How did we get here? We were seeing that this calls—how did we get up here? You brought this up, but we were somewhere in the second part. This was just to get to the level where we're iterating over LMs, so everything else was a per-LM call. Okay, cool. Let's look at the matching steps and learning steps. These will be methods on the learning modules. In step_learning_modules, we're now switching to, instead of doing the for loop in that call, calling directly into set_stepwise_targets or the actual matching step or exploratory step. We still have to either do the for loop in that step or in that function, which would still be part of Monty for graph matching, or switch to dispatching all LM data to some backend, which we didn't really want to do.

Right now, we're shifting the for loop iteration to this other method. Is that what you would like to see? I think we still have to do some level of this. Maybe it doesn't have to be explicitly a for loop in the code, but we still have to dispatch all the work across LMs, wait for that to be done, and then collect all the data from the LMs. That needs to happen at this level before we get to the per-LM level.

One thing I want to get to is how we talk about update_possible_matches here, and we use multithreading, right? But because this method is on the single learning module, the maximum parallelization we can get is per graph ID in a learning module. What we're trying to get to is parallelization across a bunch of graph IDs and learning modules—we want to parallelize across all learning modules. Right here is a constraint. I'm trying to imagine what the API looks like.

The problem in my head is, if there's a for loop, anytime we have a for loop like this, we can parallelize it by passing a set at a certain point, as long as the API allows. If we look at the current implementation and see a for loop that iterates through a list, that restricts how much can be parallelized. Because now, since this method is called for every learning module, I have to have a for loop somewhere for every learning module to call this method. I can't call this one in parallel for every learning module.

This for loop can be parallelized across graph IDs, but this method is not yet parallelizable across learning modules. I'm trying to make this method parallelizable across all learning modules and align the interfaces so that the parallel interface is maintained. The mechanism of how they're being parallelized still matters. If you want to call it on a set of learning modules instead of a for loop, currently, for graph matching, you can directly interface with every learning module separately. But if we want to run those learning modules as a set, how do we represent that? We would need one runtime to handle the logic of setting up all the data for the inputs to the learning modules and running them in a batch. That would change the dispatch structure to have some representation of multiple learning module dispatches, whether that's a hypothesis update or a new class that runs them all in parallel. I don't see a way to run these steps for all learning modules in parallel and have the graph matching only reference those learning modules, unless we have some collection parallelization object that tracks that.

Alternatively, we could still use a for loop approach but in a non-blocking way, where each iteration doesn't wait for the work to finish—it just dispatches the work. The for loop would end before any of the work is complete, having dispatched it across all learning modules, and then you have another step to collect the results. This is different from multi-threading on the CPU, where we can split the process, versus launching all the work on one GPU.

The for loop approach could work if we shift it so that instead of doing all the work in one call to the learning module, we have a dispatch call, a waiting call, and a collection call—like scatter, block, gather.

Does that make sense? Do you have something in mind?

I'm still thinking through what you're saying. If you have something to type, let me know and I'll give you the screen. I'll just update the possible matches there.

We would want to go back to the higher level, like the step learning modules. That for loop of learning modules should dispatch the work for each learning module in that loop. I already had some of this written down in that function.

We would have the dispatch step. Are you sharing a screen? No, I'm just looking over my notes.

We'd still have Monty for graph matching reference the backend so it can call it. We'd have a single backend shared between all learning modules, something like self.backend, with a wait-until-complete call. What's the API of the backend you have in mind? Is it join, join all of them if we use multithreading, or is there a GPU term? We need a call to wait for the work to complete. Then we can process all the results as needed, depending on the downstream handling of the learning module update steps. At that point, we're done with the hypothesis update or parallelization. If we want to loop through the learning modules and call downstream effects, or just have this function return, that's up to us.

What's the high-level algorithm here? What comes before the join? If we're getting rid of the for loop, it would just be dispatch, join, process results—three steps. Learning modules, sensory inputs for all, then join all of them.

At that point, the backend should track whether it's done with all the work. Then, I guess, dispatch something—there's a method or function to run. The backends would have different implementations for CPU and GPU, so they would need to know what functions to call. We couldn't just pass in a function; they would have to be aware of the operations and we'd call into them.

There are still several points in the current stack chain through the learning module, so I'm not sure exactly how to refactor that. But it sounds like we have a backend abstraction that steps all the learning modules, with a default backend and a GPU backend that does something else. What would the GPU backend do?

It depends on how we define the learning module groupings. If each learning module is its own group, the GPU backend would use a different CUDA stream for every learning module and dispatch the work. If we wanted to do grouping, we'd iterate over those groups and have the backend run a different CUDA stream for each group. In the join step, it would wait for all CUDA streams to finish before processing and returning the results.

So, for group in groups, we dispatch the work, and the CUDA backend join happens after the for loop, outside of it.

All right. Does that make sense? I think so.

So, do we need anything else to collect for the CUDA backend dispatch? What we're talking about here is actually running this step, right? This needs to be a matching step. Let's see. Graph learning—don't care about tests.

We have the graph alarm. I traced this earlier, trying to send in the chat just the list of function calls that contribute to sending messages. That's the traits here.

In the matching step, it's an observation, so this needs to be rewritten because it's a learning module thing. There's going to be a CUDA backend matching step, a learning module matching step that's going to take learning modules and whatever else. That's how the translation would likely go. In that batch, it just means CUDA backend. This is matching step four.

We essentially have to expose all the algorithms.

This is compute possible matches; it's going to do a bunch of stuff.

It's on the same file. Got it.

So, we have the DA matching step, and there is a compute possible matches per group.

I lost my sensory data somewhere already.

Wait, this is inside matching step. Observations. There we go. Group sensory inputs, and then, like you said, we're going to do even more compute possible matches and then update. At this point, it just needs to be—at a high level, let me see if I'm tracking what you're saying. Whether it is grouping or not, the point is there's a backend. The backend, instead of doing a for loop, is going to get all the learning modules and all the sensory inputs. If it's a default backend, it's just going to do a for loop and do whatever it's doing today. If it's a CUDA backend, it's going to implement these other methods.

This is straightforward, but how does this code get organized? What this means is that any method we flip inside out means the learning module has two implementations. They're different: one is a method on the learning module, the other is the learning module as data passed into the thing. In the proof of concept code I have, the backend is just implementing the hypothesis updater operations and isn't trying to handle as much of the logic around the LM itself. There are two directions: either the CUDA backend handles more of the LM logic if we're calling directly into it at this stage, or we maintain that it's still per LM, and they handle their own logic. We just make sure that none of those calls into the LM through matching step, compute possible matches, update possible matches, update hypotheses—none of those wait for the work to be done. They all just dispatch the work and return, so from this high-level step, the learning modules method can call into every LM and have it dispatch its own work, but all those calls return. Then we can wait for all that work to be done in parallel. Each LM will still reference that single backend and can do the work in parallel, but the dispatching control logic comes from the LMs themselves.

Or we switch to a more involved backend that keeps track of different settings per LM. I think I finally understand what you've been trying to say. With a CUDA backend, we could retain all this logic, and as long as by the time we get here, it's not actually doing a compute but just queues it up for later, it can still execute the same for loop. We just need to find the right place to come back and join, then resume the other steps. In my code from before our last meeting, I kept that same for loop and just changed it so it's a dispatch instead of a compute call. Once the for loop completes, we call to wait on the backend to finish and then process results. It would still require changing each of these functions to make sure they're just dispatching and not waiting for results, but it wouldn't require as much code rewriting of what the backend is doing versus what the LMs are doing. We would have to audit this to see where previous results are being used, because you cannot proceed past the join or gather in this for loop.

Or can you set up the computation even with a follow-on computation? Let's say I have two calls in sequence, and one uses the results from the other. Could the CUDA backend set that up?

I think what we would do is have a clear sense of what the sequence of operations could be. The LM could be set up so the backend objects LM interaction is aware of the pipeline of operations. We can dispatch that full pipeline, so we don't have to control each step of the pipeline at this level. We can just dispatch the whole pipeline of operations in parallel for each LM. Let's find an example of an LM that does this. I'm slowly catching up, so thank you. It's a weird programming paradigm, but I get it now.

Now, the specific question: update evidence. Update evidence. The query has been select features to use, get current display. Is this expensive? Did you replace one of these?

No, I only replaced the hypothesis updater. Update evidence. There we go. And then hypothesis update. Got it.

And so, basically this would switch to something like—we wouldn't have this equals yet. We would just have hypothesis; it would basically be the interfaces. We just have to change to something like this, where it's just—wow, thanks cursor. Let me—it's like overriding tab is a useful thing. So it'd be something like this. Essentially, this is the dispatch. Then we have to stop here, and then later on there's an entire different call, update evidence. It's like process evidence or something, right? So we wouldn't have it stop; we would just have it return, because we want that higher-level for loop to finish each of these dispatches. We need to find these break points where we split a method into before the dispatch and after the join—before the scatter, after the gather. 

What terminology are you using? CUDA? I keep making it up—scatter, gather, map, reduce for chart. I think you can do a lot of things. It's helpful to think of dispatch operations and then block or wait for those to complete. So, non-blocking route, blocking. We need to evaluate the functions and see which portions are dispatch, and then everywhere we need to block, we essentially create a new function. We need to split up functions at the block points.

Yes. Am I saying the same thing? Unless it depends on what we want to include in the pipeline of operations the backend is completing. Got it. Because we could still just have that one dispatch and have that queue off for that LM all of the hypothesis updating steps, and not have to keep track of that at the evidence graph LM level.

Ideally, whatever step this is running in the experiment, we just have one dispatch call, one blocking wake call. Then we take the results and continue with the next steps, like doing LM voting, ting, and goal states. All of the evidence update operations occur from this one dispatch to the backend pipeline. Got it.

It smells a lot like, at first approximation, a visitor pattern. I want to pass it a visitor—each one of these things, pass a visitor, and then here be visitor, dispatch, or whatnot.

Let me say it differently. If we split it up, how does my CPU stuff work? It's almost like—I guess I'm just trying to figure out what is the common interface between that paradigm and this and the current paradigm. Visitor smells like maybe that's adjacent to the right interface, because if each one of these calls a specific method on a visitor, and if it's the CUDA visitor, it's going to just queue and dispatch the stuff. But if it's a CPU visitor, I guess it needs to immediately return. I don't know how to design that. Maybe visitor's not the right one, but that's what I reached for immediately here. I haven't thought through the CPU side as much. Kind of do both. A simple, naive CPU backend—certainly for conceptualizing one step, this would work. I'm trying to extend that to doing these sort of pipeline steps. You could have it do multithreading, or you could just have it do the full for loop and actually wait for each step to complete. But that already changes the interface, because you wouldn't have this dispatch, wait, process results call—the CPU doesn't, if it's operating sequentially.

I guess the CPU backend would calculate it immediately, but I would just have to do a level of indirection. Everything would have to be designed to support the CUDA kind of dispatch and block. I think I'm now catching up to how the CPU one would work. A CPU visitor, when I dispatch it, or since everything is the same API, maybe we don't need a visitor anymore—it's just the API. When a CPU does it, it just stores the results in the variables in its backend, and then when you call the things at the block, it just reads it from where it stored, from its internal state, versus on CUDA. For a CPU backend, when you dispatch to it, it would actually do the computations right there and then, and store the results in its internal variables. For a CUDA dispatch, it would start queuing things up to send off to the GPU. Then, when the CPU backend blocks, all the results are already there. For CUDA blocks, we actually wait for the GPU to finish, then resume everything and the results are there either way. In the CPU, we block, the results are already there, so we proceed, and the slope was the dispatch code. The CUDA part block actually calculates the results, gets them back, and we proceed as well. Does that sound—yeah, actually, I think that makes sense.

We could probably even switch the blocking call to be a part of the very beginning of the GPU's process results. We don't even have to have the blocking be made available at this level. It could just be dispatch work, process work, or process results. The CPU just does that sequentially and then has them already, and the GPU does a dispatch of them all in parallel. Whenever you want the results, it first waits for the results to be done and then provides them back to you. That's actually more in line with how GPU programming typically works. You have a CPU thread, and whenever you want to run something on a GPU, you dispatch the work. It'll automatically handle the blocking stuff. As soon as you want to process some of those results, that's when it will wait. As long as you do other things in the meantime before you process the results, it'll handle all of that running in the background. As soon as you want the results, that's when the CPU thread will stop and wait for the GPU to finish.

Got it. So we just want to do the same thing. Let me write up the GPU version: backend, block or results to come back from GPU, process results. GPU backend is dispatch work to GPU.

Yes, and then return immediately.

And then the CPU version would be: do the work, then return after the work is done.

And then store results in turn. I think this is where we need to decide what should be handled by the LMS themselves and what by the backend. If the LMS have their own functions to set up and dispatch work, we can still store the results in those LMS, with results not being stored or handled by the backend. So, somewhere for later retrieval—could be backend intermediate variables, could be learning modules, etc.

After the work is done, for the CPU backend, results are available and we process results right away.

This is promising. Let me put this in chat so it doesn't disappear, so you can also see this as we come close on time.

We have four minutes.

Perfect. Done? Yes, that's great. I can write up my understanding and post this in our discourse. I'll summarize the high-level idea and think through what needs to be updated. We made progress. I think we still need to get the details, but we have the level one, right? Does that sound right? I'll report here that we have a high-level plan. I'll try to describe it—please correct me if I get it wrong. Next time, we'll see if we can push the details further. This has been super helpful, and thanks for repeating this until I got it. I'll also try to describe it in my words for anyone who comes after. I'll make sure this high-level plan would work with the conceptualization of the GPU backend and see if there are any problems I haven't thought through.

We just want to make sure we're considering it now, and I think it would work both for an individual LM or for an LM group if we wanted to shift to that architecture in the future. Will this work for both individual LMS and groups of LMS? Perfect. The other thing I want to do is find the process results points that might block. Does that make sense?

That's the one, and I'm just writing the notes here, but I'll summarize it again in the discourse.

This is a detail we don't have to think about right now, but I want to mention it because it could impact how we think through the high-level architecture. Traditionally, one of the most common bottlenecks for any heterogeneous programming where you're doing CPU and GPU is transferring data between the CPU and GPU. That's often much more of a bottleneck than the actual compute running on the GPU. The best way around that is to keep as much data resident on the GPU as possible, and I think it's conceptually very feasible because the Monty experiments care about those intermediate data steps—the intermediate formats and the output of one GPU kernel into the next.

It would mean that anytime the LM needs to access its own internal data, like looking at an object graph, it might have to read that from the GPU instead of having it already in CPU memory, which is easy to do. Conceptually, we want to make sure this architecture works so we can keep as much data on the GPU as possible and avoid big data transfers, just reading back and forth the new inputs, whatever changes happen, and the outputs at the end.

Good to know.

Alright, I'll write up the notes summary. Let's stop here. We'll catch up in a few weeks when you get back and go from there. Sounds good. Awesome. Thanks. Appreciate it. Good to see you again. Progress for sure. Alright. Cheers.