Howdy. This is Tristan. And what I will go over is a brief overview of how we put together hydro configurations to get a multi experiment running. let me orient you to our workspace here and what's gonna happen, over here on the right, this will be just reference materials so I can put together the configuration. We're gonna do configuration the hard way. It will just be one big flat configuration so you can see how everything comes together in Hydra.

and then the main workspace here will be here on the left. let's get started as a first place. We have Monty set up in a configuration. I'm gonna go to experiments folder, here, an experiments folder. We can see a bunch of experiments already. I'm going to add a new file code. My experiment yamo. And this will be, my experiment. Straightforward. Alright, let's get started. the experiment that I'm going to run is going to be the multi supervised object p training experiments. So we set that as a target and then everything else will go inside the config for this experiment to get started.

the first we're going to, let's see, do train, do eval, So we are going to say that we want to do train to be true. And we want do evolve to be false. So we will train, we will not evaluate this, by the way, will mirror the configuration from the tutorial for running your first experiment. So it'll be just a very straightforward, short pre-training run.

So the eval, the train, next step will be show sensorimotor output.

will be false. We don't need to visualize anything. we are going to have max train steps. One, again, we, this is just a quick demo, so we wanted to finish quickly.

we can leave max eval steps can really be anything because, we will not be doing eval. next step will be max total steps. also we'll be short circuited, but we're not going to run into this limit because we have tiny amount of max train steps and then, we have train epochs. We want to have one train epoch again, we're just doing short training eval. We can take the defaults. They don't matter because we are not doing. Evals and model name or path that we will use.

we are not loading anything 'cause we are training, we are not loading any pre-trained models, so there will be no model name or path Men LMS match we believe as the default.

We will leave the standard seed in place, and then the supervised LM IDs. We are going to supervise all of the learning modules. Again, this is a pre-training setting, so that is the main bit of the configuration for the experiment. Now let's configure everything that goes inside there. So next step will be logging. So logging configuration is nested.

let's provide it just before so we don't forget. Let's provide it a run name. The run name will be my experiment. And next, for logging, we are going to say that we want the multi log level. To be detailed, we will, specify three monthly handlers that we wanted to add. we want a, these are logging, multi logging handlers, so we want the basic CSV stats that will generate CSV stats, generate j and then reproduce episode handler. I'm pretty sure we don't need this one. So let's just do these two, one DB handlers in case you want to send data to one db. We don't want to do that, so we will set them as being empty. And then we want the Python log level to be info. Python log to file. We do wanna log to the file. We also wanna log to standard error and the output directory. We will go with the default, which is based on, user expanded path for multi logs projects, multi runs.

we are not resuming in the one DB run, so that is false. We will say we want to use these, but one db ID we can generate it, but we're not gonna be needing it. This is a debugging group, but if we're to run one DB and we are not logging, we're not gonna. Log in parallel again. one DB settings will not take place because we don't have one DB handlers activated. Okay, and that is it for logging. Next, let us configure Monty itself. So Monty itself, which Monty class are we going to use? We are going to use.

Monty for graph matching, which is our state of the Art Monty class. Let's configure the, let's do Monty Arguments next. Monty ARGs, which will be passed to this monthly class.

So number of exploratory steps will be a thousand. Minimum eval steps will be three. Minimum train steps will be three max. Total steps will be 2,500.

So these are the Monty arcs that are the defaults that we passed through that class. Next up, I think that's it for Monty Arcs. Lemme just double check. Yeah.

All right, next up. so notice these are here for the experiment, and these here are for Monty itself. All right? So that's multi class and multi arcs. next up, let's configure, let's configure the motor system.

so Monty, So the motor sy, so it's motor, excuse me, motor system config, and the motor system config will have a motor system class and that's the motor system and it will have water system arcs.

And in water system arcs, we want the policy. We're going to use the informed policy in this case, and we want to pass in some policy arguments, policy arcs. the action sampler that we will use is a constant action sampler, and that action sampler takes a rotation degrees as an argument. So we're gonna give it five degrees. And, the policy arcs also need to know what agent ID the policy is for. And so we using, agent ID agent IZ zero. This, this will turn in, code, will instantiate an agent id, agent ID zero, identifier, for the policy. Okay.

the other policy arcs, that we will include is, there is no file name that we are reading from. If there are any pre-trained actions type of things, good view percentage, we want 0.5 desired object distance 0.3. This is again for the informed policy parameters. If we do not wanna use ghosted der actions, which frequency will be one mid percent on object zero to five.

And then, the other thing, and then one more thing we need to specify. So that's for the, that's enough for the policy arguments. One more thing we need to specify for the action sampler class. Here is the action space. And the act, and so these are the actions that it chooses from, so actions. So the policy sampler, excuse me, this constant sampler of actions, if we tell it to sample for random action, it'll choose from this list of actions. So give it the monthly, give it the classes. We give it a lookup action. Look down, turn left, turn right at agent post. At end, sensorimotor of rotations. Okay, so with this we have our action sampler class and with, with its arguments, we have our policy class with its. Policy arguments. And then we have motor system, we have motor system arguments. Let me just make sure that there's nothing else that I need to do for the motor system.

no. That configures the motor. That completes the motor system configuration. Alright, so next over that's configure our learning modules, learning module, configs, and for learning modules, we are just going to have a single learning module.

we're going to use the displacement graph learning module and the arguments that we're gonna give it is match attribute displacement and K is equal to five. Next step, we're gonna configure sensorimotor, module configs, and we're gonna have two sensorimotor modules. One that will be hooked up to displacement graph, feeding it information, and the other one will be. Experimental probe so that we can look at what's going on in case we want to. So sensorimotor module zero will be, will use, will be the standard habitat sensorimotor module because we're using habitat for our experiments here, sensorimotor module arguments. We're going to, give this the ID of patch. And then the features we want the sensorimotor module to, we're configuring again the Habitat Sensorimotor module and the features we want the Habitat sensorimotor module to include are, this list of features.

This is, these are the morphological features that we wanted to send through the learning module, and these are the non morphological features that we wanted to send it through the learning module. And we do not want to save raw observations. sorry. We do want to save raw observations.

Okay. And so that's the sensorimotor, that's the first sensorimotor module, the zero sensorimotor module. Next up, we'll do Sensorimotor module one.

And for this one, we're going to use the probe sensorimotor module. Again, this is our experimental probe, so we can visualize things if we need to. we're going to pass in sensorimotor module arguments. And the only arguments it takes is the identifier, which is the viewfinder, which is our kind of the name for, we will not look at an object that a sensorimotor module is seeing. And then we have, and we also have s observations, the truth. And this concludes the sensorimotor module configuration.

Okay.

the other bits of Monty that are, if you remember, we're still up here, we're still inside Monty. We config Monty. We did the, we configured Monty arguments. We configured motor system config learning, module config, sensorimotor, module config.

There's a, there are a few more, things we need to configure Monty with. And so this is, how to set up the network between, the sensorimotor module. How did these sensorimotor modules, learning modules connected? So SM to Agent Dictionary, and we have the, patch sensorimotor module. It's the one that we created here. Sensorimotor module Patch as a sensorimotor module. Patch co. corresponds to agent id. The data from that corresponds to agent ID zero, and then the viewfinder. Also agent ID zero and then SM to LM Matrix, sensorimotor module to learning module matrix.

and then LM to LM Matrix doesn't have one. We only have one learning module, and then there is no voting happening in this. Okay. And so this completes, our monthly configuration. So let, actually, let's minimize these guys, so they're outta the way. So that's Monty what we need to configure next is, let me just review my reference material here. so we have, we've done. We've configured the experiment, we've configured logging, we've configured Monty Logging as part of the experiment, Monty, inside of the experiment. Next we need to do is configure the environment and so the environment will be, one second environment.

Okay, there we go.

So environment will be configured and environment interface config. All right. And so the environment initialization it function will, be instantiating the habitat environment and then, environment in it, ARGs.

So the arguments to this habitat environment are, let me see. It's going to the agents that it's gonna get.

it's gonna be agent type, will be multisensor agent. That's what we're gonna give it. And then, the objects that we will put in our environment. In this case, we're just going to do a.

pre, these are predefined objects, so there's inhabit that there's a C solid object. We're gonna place it at disposition. we're gonna tell this, scene ID is null, seat 42. And then the data path is to retrieve objects from habitat objects, YCB from the YCB or Habitat object dataset.

Okay. and then the other thing is we need to, we have agents, but we also need to provide, we have agent type, but we need agent ARGs that we need to provide here to instantiate the agent and, agent patch and view finder. Okay. Cool. And so the agent id, It is gonna be agent ID, zero sensorimotor IDs. That will be patch and viewfinder. And then the height of this agent will be at zero zero. We're, essentially possessing this agent inside the habitat simulator now, and then resolutions, correspond to the two sensors. So there'll be a, so they both have 64 by 64 resolution positions.

And then rotations. This is where we essentially set up these sensorimotor, like this agent has these sensors and the agent is at this height. This is the agent positions, but these are the resolutions of the sensors. The positions of the sensors relative to the agent, rotations of the sensors relative to the agent. So semantics, false, and then zooms. And then these are the zoom levels, for the sensors. Okay. This is very, all this is all very habitat specific. So again, we are starting habitat environment from simulator habitat. And so this configurations is for habitat agents and those have a specific configuration. lemme make sure that, okay, cool. It was just a suggestion. Cool. So you have agents, you have agent type, agent arcs. Excellent. And And that's it. So we have a habitat environment and it's gonna be configured with these agents which are connected to these sensors. This environment has these objects. The scene, this entire scene is just, I'm gonna give you the id. We have a seed and we have where the data for any objects that we define here comes from. Excellent. I believe that will, let me just double check. Oh, okay. And then the one more thing we need to specify about in our environment is the transform. So what trans, what transforms. So once we receive observations from the environment, what transforms are we going to run before we hand them over to Monty? one first transform that we're gonna run will be missing to max depth. this thing has gonna have agent id.

And notice this agent ID is the same as the agent ID from the agent, and then the max depth will be one. So Max, if depth is missing, we're gonna set it to one. the other thing we're going to do is we're going to convert, basically screen pixel data with depth data on top of it. So it's RGBD, red, blue, green depth, and we're going to convert it into 3D locations.

that's what this transform does. Again, the same agent, it works on, and observations coming from the same agent id. it works on the sensors, from that agent.

And then, we need to, this transform needs to know what resolutions is working with. So we're just feeding it. We're just telling it that these are the resolutions that we set for the agent. we'll do this in World Court and it's, again, we have to pass in the zoom information, same one from above. And we wanted to get all points and we want to use semantic, sensorimotor false. All righty. And then we also need to, we're not gonna give it any specific RNG.

this is an artifact. I wouldn't worry about it. so environment interface config. This should complete, our environment interface configuration. Let me just double check my references.

So we have, Let me just see patch and view habitat. Okay. So Envi, we have our environment in IT function. We have our environment ARGs, and we have our transform and we have our RNG for the environment. Okay, excellent.

the reason this is RNG Noll is 'cause we need to instantiate habitat with an RNG and a current code will first instantiate habitat environment and then later on pass it an RNG. so this is just how we have things currently. This will be changed in the future. Okay. That should configure the environment interface configuration. Let me just make sure I put everything in the right place. Environment and function. Environment and at ARGs, and then Transform and RG are at this top level. Okay. Excellent. So now environment is configured. We are almost there. the remaining bit we have to configure is our, we said we're not doing eval, so we don't have to configure eval any farther, but we do have to configure, our, how are we going to interface with the, environment doing training. So train environment interface class, and this will be environment interface per object.

And then train environment interface, ARGs. And what are we gonna pass to that?

Okay. so one second, let me once again consult.

so the per object. So parent, we are not going to provide any parent to child mapping in this instance.

And then, okay. And then the other thing we need to give it is what object names, what objects we wanna populate the environment with. We're gonna do a mug object in. Its simpler, and we want to use the predefined object initializer. Okay.

And that should be a working configuration. So we have, let me just reduce it so it's easier to see.

Okay. So we have our, want to supervise machine experiment. We have a configuration. High level configuration for the experiment here. Then we have logging Monty, our environment set up, and then how, is our training going to interface with the environment? So for logging, we specified our run name and then. What log, multi log level, what multi handlers we wanna do. These are like data telemetry level and handlers. And then this is your kind of standard logging. it's gonna be info and we're gonna log to a file into a standard error. That's where we're gonna do it at. one DB is ignored. Settings are ignored because we didn't specify any one DB handlers. Then we configure Monty. A multi configurations confi consists of, this. And so we have a multi class, which we're gonna give it some arguments. We also need to configure our motor system, our learning module configuration, our sensorimotor module configurations, and then we need to define how the network of agents to sensorimotor modules to learning modules looks like. So for Monty Arcs, here's the arguments that we passed in for modern configuration. We need to specify motor system class and motor system arcs, which takes a policy and policy arguments. And then policies also take action sampler as an action arguments like And then, we have learning module configurations. In this case we specified learning module class, learning module arcs. I think I'm missing something here. Let me just double check that this is set up. This learning module configuration is set up correctly.

Okay. Yeah, I am, I, made a mistake here. this is this, yeah. Learning module. Configure is a dictionary. so this is our learning module zero, and this is class and arguments. Okay. This is the correction here, and then the sensorimotor module configuration. Similarly, we have Sensorimotor Module Zero on Sensorimotor module one, and. For this one, we have actual sensorimotor module, it's ID and what features we wanna pass to the learning module. And then we have our probe that we use for like visualizations and other things. So that's sensorimotor module configs mapping between sensorimotor modules and agents, sensorimotor modules and learning modules, and then learning modules and voting. not applicable in this case. Then we have our environment configuration where we have, our. what we're environment we are gonna stand up, which is habitat, and then what arguments we're gonna pass to that, and then the transforms that we wanted to do before we pass the observations from the environment to Monty. And then, this is just an artifact of how a Q it currently is. Just put RNG all here. but don't worry about it for now. Any farther. And then inside, this is habitat specific. Now we need to specify what agents we have with objects, CID, and the data path where habitat should be getting it's, objects from. And then these is the, list of transfers that we want to apply to those observations. And then lastly, how the training, the how the training is going to interact with the environment. So environment, interface per object. And we're just gonna present a mug and we use the predefined object initializer. And with that we have our, my Experiment, multi configuration, the hard way. And over here, we will, should be able to now, from top level do run parallel experiment equals actually just may just run, not run parallel. Experiment equals, my experiment. the reason this works, my experiment equals my experiment is because inside the Conf Experiment folder, we created a file called My Experiment. And so that's how that mapping goes.

if we were to create it, and if my experiment was inside tutorial, then I would have to do experiment equals tutorial my experiment. But I just, because I put it at top level, it should be here. All right. He goes, nothing.

Oh no. What did I do? Key error Monty. Config, let's see.

Oh, I called it Monty. It's Monty config.

I think that should fix it. Let's run it again.

And there we go. There is our training happening. It doesn't do anything interesting because we just wanted to demonstrate the configuration and things running, but it's done running and it, the thing, this concludes the demonstration.