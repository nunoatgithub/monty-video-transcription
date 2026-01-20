All right, so here's another video from our archives. It's from July, 2023, and it's the second part of the Legend of Monty. And although it's from 2023, it's actually not that far off from where we are today. Because shortly after that presentation, the whole Monty team was pulled into some other work at Numenta and we took about a year's break from work on Monty. So if you look at the in future roadmap towards the end of the presentation, this is still pretty much all future work. and some of our next goals have changed since then, and you can find a more up to date version of what we're working on in the near term future on our documentation website in the future work section. Unfortunately, we forgot to start the recording for this presentation, and only remembered it a little bit into the presentation. So I'm just gonna go through the first slides that are missing, in that presentation. All right, so legend of Monty chapter two.

As you may recall, a while ago, the Monty team washed up on the shores of NuPIC Island there. In the beginning, they had nothing besides a few principles they wanted to follow.

There was sensorimotor learning and inference, so there's always active interaction with the environment to learn and perceive the world. Another principle is using reference frames, so not just a bag of features, but that we actually have structured models with a 2 or 3D or 4D inductive bias.

another one is modular structure. So an easy plug and play extensible system, with learning modules and sensorimotor modules. And importantly also, no sensor perceives everything. There isn't just one input image. There are a bunch of little patches that move in the world. And fourth, the common communication protocol, which we now call the Cortical Messaging Protocol, which is the messaging format that learning modules use to communicate with each other through voting, but also in a hierarchical way, and that they expect as input and output with these principles, they made their way across the island and collected much knowledge on the way.

They set up the Monty framework. They set up a test environment. They introduce rotation, translation invariant recognition.

They got multi to the point where it could sample arbitrary displacement, added voting and speed.

They introduced sampling invariance. So now any, point on the object can be sampled in any order and objects are still being recognized correctly. They added robustness and basic generalization capabilities. And for a more detailed view, you can have a read or look at, the legend of multi chapter one.

We ended the last chapter in evidence learning module town with much of the island still to explore. We had explored and learned much about NuPIC island, but much of NuPIC island still stretched out far in front of us and we did not know what was waiting up ahead. So the Monty team ventured forth into the unknown and made their way to the next town.

The next town was a partner city of Evidence LM Town, Action town. Here, they worked with the local tradesmen on developing intelligent policies for Monty.

So for instance, we have policies that use model free signals to move along the principle curvature directions for more efficient coverage of objects. And we also have model-based policies that use internal models and hypotheses to figure out where to sense next to resolve ambiguity.

Together these new policies make Monty move much more efficiently through space and recognize objects faster.

After some regrouping and careful planning, the Monty team decided to split up and explore different areas around them. They kept in touch with each other through frequent messenger birds and runners. so I'll let you go over to the actual recording from back then and enjoy the rest of the legend of Monty. Have fun.

One part of the party started walking east towards the tower of multiple objects. Another part of the party took the northern road, passed the lake towards the castle of compositionality. Another part of the group split off North to scope out the small Fisher Village that specializes in robust sensors.

At the Fisher Village, they improved the design of their sensor modules.

They worked on smoothing depth values and improving the point normal and curvature estimates to get a higher accuracy when faced with raw sensorimotor noise.

In the Castle of Composition, they implemented the basic framework for hierarchy.

To be able to experiments with the hierarchical system, they implemented new information routing and processing. They also implemented constrained object models to force Monty to make use and composition models of objects in Tower of Multiple Objects, they set up the foundations for dealing with multiple, potentially touching or overlapping objects.

First, they set up an environment which they could, within which they could run multiple object experiments, as well as evaluate, these, experiments. These are objects that touch each other, or they called, they're very close to each other. Okay. Yeah. Yeah, definitely feel free to ask.

Yeah. Yeah. Like a Potted Meat Can. Yeah. Yeah. Ted's, it's a weird, ridiculously complex we can do, it's a, it's like a dinner table, a weird dinner table in and abyss, with a, yeah, variety of optics, but we intentionally make it adversarial so that the objects are very close to each other.

So first they set up this environment and then, yeah, then they implemented an approach to detect when an LM has moved onto new object based on a sudden shift of evidence.

this detected shift can then be used to move back onto the object, improving accuracy.

During the individual missions, they met up at the lake of reality for a little boat trip where they tested their system and acquired knowledge in the real world for the first time.

It took Monty for it's first test drive using an iPad camera, and a new data set of real world objects.

Most recently, during their journey, they have ventured into the grotto of dynamic environments and the surrounding forest.

They set up an environment that models dynamic objects where they will be able to test Monty on their venture into the forest towards the town of dynamic environments. They investigated potential ways to model and recognize object states and behaviors in Monty.

Over time, the cities they have reached have been thriving and there has been more and more trade between them. The team has steadily reinforced the infrastructure by refactoring and cleaning up, adding many speed improvements and optimizing their communication process. They've also put down a concrete definition of the common communication protocol, Recently, there has been much exchange, between action towns and the Castle of Compositionality. they have conceptualized and started a big construction project on hierarchical action policies.

Looking back at what they accomplished in the past half year, they wonder what path to take next.

We might do in the next half year.

So we had ventured far and learned much about NuPIC Island stretched, but NuPIC Island stretched out even further ahead of us and we did not know what was waiting up ahead. This was a rough thought of what was gonna happen in the next half year. That actually changed a bit in the past half year. Not too much. Most of the things we did plan on, we did get on this map.

By now we have a clear idea about where we are and where we may want to go next. So these yellow boxes that up here now are current tasks in progress about to be started. So as Niels already mentioned, we're starting to work on hierarchical action policies and generally making actions much more sophisticated where every learning module kind of proposes its own goal states. We can compose goals into sub goals and, yeah, generate hierarchical policies.

then we're also working on testing and improving hierarchy on new and sophisticated data sets with actual compositional objects.

We've started conceptually to investigate how we might model dynamic environments and how we want to test that, but something, and then also "multiple objects" currently still in progress, there's stuff done there already, but still a bit, that we need to get better to actually work in an environment with many objects.