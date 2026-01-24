All right, here's another video from our archives. It's from July 2023 and is the second part of the Legend of Monty. Although it's from 2023, it's not far off from where we are today. Shortly after that presentation, the Monty team was pulled into other work at Numenta, and we took about a year's break from Monty. If you look at the future roadmap towards the end of the presentation, this is still mostly future work. Some of our next goals have changed since then, and you can find a more up-to-date version of what we're working on in the near-term future on our documentation website in the future work section. Unfortunately, we forgot to start the recording for this presentation and only remembered a little bit into it. I'll go through the first slides that are missing from the presentation. All right, Legend of Monty Chapter Two.

As you may recall, a while ago, the Monty team washed up on the shores of NuPIC Island. In the beginning, they had nothing besides a few principles they wanted to follow.

There was sensorimotor learning and inference, so there is always active interaction with the environment to learn and perceive the world. Another principle is using reference frames—not just a bag of features, but structured models with a 2D, 3D, or 4D inductive bias.

Another principle is modular structure: an easy, plug-and-play extensible system with learning modules and sensorimotor modules. Importantly, no sensor perceives everything. There isn't just one input image; there are many small patches that move in the world. The fourth principle is the common communication protocol, now called the Cortical Messaging Protocol. This is the messaging format that learning modules use to communicate with each other through voting, but also hierarchically, and that they expect as input and output. With these principles, they made their way across the island and collected much knowledge along the way.

They set up the Monty framework and a test environment. They introduced rotation and translation-invariant recognition.

They got Monty to the point where it could sample arbitrary displacement, added voting and speed.

They introduced sampling invariance, so any point on the object can be sampled in any order and objects are still recognized correctly. They added robustness and basic generalization capabilities. For a more detailed view, you can look at the Legend of Monty Chapter One.

We ended the last chapter in Evidence Learning Module Town with much of the island still to explore. We had explored and learned much about NuPIC Island, but much of it still stretched out far in front of us, and we did not know what was waiting up ahead. So the Monty team ventured forth into the unknown and made their way to the next town.

The next town was a partner city of Evidence LM Town: Action Town. Here, they worked with the local tradesmen on developing intelligent policies for Monty.

For instance, we have policies that use model-free signals to move along the principal curvature directions for more efficient coverage of objects. We also have model-based policies that use internal models and hypotheses to figure out where to sense next to resolve ambiguity.

Together, these new policies make Monty move much more efficiently through space and recognize objects faster.

After regrouping and careful planning, the Monty team decided to split up and explore different areas around them. They kept in touch with each other through frequent messenger birds and runners. I'll let you go over to the actual recording from back then and enjoy the rest of the Legend of Monty. Have fun.

One part of the party started walking east towards the Tower of Multiple Objects. Another part took the northern road, past the lake towards the Castle of Compositionality. Another group split off north to scope out the small Fisher Village that specializes in robust sensors.

At the Fisher Village, they improved the design of their sensor modules.

They worked on smoothing depth values and improving the point normal and curvature estimates to get higher accuracy when faced with raw sensorimotor noise.

In the Castle of Composition, they implemented the basic framework for hierarchy.

To experiment with the hierarchical system, they implemented new information routing and processing. They also implemented constrained object models to force Monty to use composition models of objects. In the Tower of Multiple Objects, they set up the foundations for dealing with multiple, potentially touching or overlapping objects.

First, they set up an environment within which they could run multiple object experiments and evaluate these experiments. These are objects that touch each other or are very close to each other.

They intentionally made it adversarial so that the objects are very close to each other.

First, they set up this environment and then implemented an approach to detect when an LM has moved onto a new object based on a sudden shift of evidence.

This detected shift can then be used to move back onto the object, improving accuracy.

During the individual missions, they met up at the Lake of Reality for a boat trip where they tested their system and acquired knowledge in the real world for the first time.

They took Monty for its first test drive using an iPad camera and a new dataset of real-world objects.

Most recently, during their journey, they ventured into the Grotto of Dynamic Environments and the surrounding forest.

They set up an environment that models dynamic objects where they will be able to test Monty on their venture into the forest towards the town of dynamic environments. They investigated potential ways to model and recognize object states and behaviors in Monty.

Over time, the cities they reached have been thriving, and there has been more and more trade between them. The team has steadily reinforced the infrastructure by refactoring and cleaning up, adding many speed improvements, and optimizing their communication process. They've also defined the common communication protocol. Recently, there has been much exchange between Action Town and the Castle of Compositionality. They have conceptualized and started a major construction project on hierarchical action policies.

Looking back at what they accomplished in the past half year, they wonder what path to take next.

We might do in the next half year.

We had ventured far and learned much about NuPIC Island, but NuPIC Island stretched out even further ahead of us, and we did not know what was waiting up ahead. This was a rough idea of what would happen in the next half year. That actually changed a bit in the past half year, but not too much. Most of the things we planned, we did get on this map.

By now, we have a clear idea about where we are and where we may want to go next. These yellow boxes that appear now are current tasks in progress or about to be started. As Niels already mentioned, we're starting to work on hierarchical action policies and generally making actions much more sophisticated, where every learning module proposes its own goal states. We can compose goals into subgoals and generate hierarchical policies.

We're also working on testing and improving hierarchy on new and sophisticated data sets with actual compositional objects.

We've started conceptually to investigate how we might model dynamic environments and how we want to test that. "Multiple objects" is currently still in progress; there's work done there already, but we still need to improve to actually work in an environment with many objects.