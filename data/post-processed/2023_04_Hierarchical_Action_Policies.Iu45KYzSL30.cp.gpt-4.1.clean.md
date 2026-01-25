Okay, nice. This is my effort to distill some thoughts around hierarchical action policies. It's not fully clear in my head yet, so this will be an amalgamation of ideas, but that's the point—to talk through it. These aren't really new ideas; it's more about structuring how we think about this, and it relates to Rajesh Rao's presentation, which has many similarities.

The aim of hierarchical action policies is to enable flexible and efficient agent behavior that can impact the world and handle arbitrary, novel situations. We all have an intuition about how hierarchy helps with efficiency and flexibility, and we can work through it together.

At the same time, we've discussed the need to better understand how to represent object behaviors to develop meaningful hierarchical action policies. That's a lot of what I'll talk about today.

First, some basic definitions to make sure we're on the same page. An action policy is a basic set of actions to achieve a goal, typically conditioned on the state of the agent and the world. Reinforcement learning is a method to learn an action policy given reward signals. There are two main flavors: model-free, where you learn an action policy directly from rewards without learning a model of the world, and model-based, where you explicitly learn a model (often called a transition model or transition function) and a reward model that tells you how valuable certain states are. With these, you can develop policies on the fly and adapt as needed. If a blockage appears, you can refer to the model and find a way around it.

The holy grail is to learn these models in an unsupervised fashion, then leverage reinforcement learning as needed when certain states are important. The hope is to learn the transition model first, so you can use it later.

I've always been uncomfortable with reward-based reinforcement learning because much of what we do is not reward-based—it's model-based. I'm trying to get to a state using the model, not by learning an action policy through rewards. The idea of a reward model, even in model-based reinforcement learning, is a bit of a red herring. We should focus on the models and how to achieve results given a desired outcome, without needing rewards. I don't know if you agree, but I wanted to make that clear.

I definitely agree. From my reading, you rarely see studies that focus solely on learning the transition model; reinforcement learning is almost always baked in. That's why I mentioned rewards, because it's how it's defined, but you can learn a transition model without rewards, using prediction errors, for example, and then learn a policy using reinforcement learning or another planning algorithm. You don't have to use reinforcement learning at all if you have a sufficient model of the world and are just trying to reach a state. We should really focus on the model-based transition model. I agree.

A classic example from neuroscience is Tolman's work with rodents, where they explored maze-like structures without a reward. After exploring, if given a single reward, the rodents could quickly navigate the maze to reach it, compared to those learning from scratch. This suggested they built a cognitive map or world model, which they leveraged. Much of reinforcement learning and sensorimotor action-based learning focuses on agents interacting with environments, but what makes Numenta unique is trying to capture this concept at every level of representation, not just agent-environment interaction, but understanding everything, including objects.

We want a cognitive map for all relevant models. Drawing a parallel to Monty, learning the maze is like learning object models, and reinforcement learning is about achieving a goal state, not about learning the model itself. You don't need a reward to learn the model; you just need to know you've accomplished the goal.

We do lay down memories of how we solve problems, but not always. In a maze, you might remember the solution for next time, but manipulating a stapler might be different each time. It doesn't always require a reward signal, and sometimes the solution is a one-off.

Typically, this is called a transition model or transition function: a set of states of an environment or object, and the transitions between those states, often conditioned on actions. The simplest case is a deterministic mapping between states, but more often it's probabilistic or conditioned on actions, forming an arbitrary function.

Transition models can be hierarchical. For example, Matthew Botnovich's 2014 paper discusses hierarchical reinforcement learning and hierarchical transition models. The literature often describes actions as those of the agent, but it's useful to generalize action as any influence on state—gravity, another object's behavior, or even internal factors like elasticity. Not everything changes only by agent action; many influences can cause state transitions.

This approach naturally connects object behavior with representations that support planned actions. Once we learn a transition function or model and represent it usefully, it can support powerful action policies.

Hierarchical reinforcement learning is standard reinforcement learning—model-based or model-free—where action policies can abstract over time or states.

If you imagine this diagram, you have to take a series of actions down a tree to reach a particular goal state. You might learn to group these actions, such as "opening the door" or "getting out my car keys," rather than focusing on the minutiae of motor movements required for each subgoal. This makes planning more efficient and credit assignment easier. If you're just trying to achieve a state and know the structure of the world, reward learning may not be necessary. The diagram suggests there's only one path to any end state, but in reality, there are many paths. The diagram doesn't capture that complexity. The chunking or hierarchical nature of actions is well illustrated, but it doesn't fully represent the problem.

Another diagram shows abstraction, where you can have temporal abstractions over actions or state abstractions, such as the agent having the key. State abstraction seems more relevant; it's the first thing you do. We don't want models only at the highest level of detail—we want relatively abstract models of the world, which we're already doing with heterarchy.

Much of the literature focuses on model-free reinforcement learning, especially hierarchical reinforcement learning, because learning hierarchical world or object models is not easy. There are unsupervised signals, like predicting the next image, that can inform these models, but hierarchical models tend to be shallow or simple. In future brainstorming, we could discuss learning how particles interact with a world model.

Of course, it can be model-based, which is where we may contribute.

The last definition to mention is "options," which refers to chunking actions into more temporally abstract units. An option could be "open door," which initiates its own subpolicy until completion. In the literature, "options" are higher-level actions, not just choices between alternatives. Once you select an option, a different policy executes it.

That's all the definitions, so we're on the same page.

Stepping back, the challenge is to learn the transition model of objects across multiple hierarchies—object behaviors—and also how motor systems interact with the transition model to achieve a goal state. This is the intersection of object behaviors and action policies, which are related but not equivalent.

As a first step, I'll walk through how I'm conceptualizing transition models and how this may tie in with cortical anatomy as we've been discussing.

This will focus on object behavior, not hierarchy yet. Imagine we have a learning module that has learned a model of a stapler, with different layers. If a layer is shown as one color, it's because I don't have a reason to subdivide it, but that could change with discussion. The term "transition model" refers to how the state of the object changes with the environment over time. The state might include the stapler moving up and down or icons changing on a screen. The transition model is about the object's state and how states transition, which could also include our location on the object. For example, grid cells and path integration are part of the transition model because they update our location as we move through space.

There's a distinction between the model of how a sensor moves through space and the model of the stapler itself. The transition model is about how actions move you through the state space, with actions specified relative to the object, not how your fingers move. The model of the stapler includes its behaviors, separate from how you interact with it, but they are also entangled. The state is a set of variables: location on the object, sensed feature, object ID, object pose, and possibly an object state type, such as open versus closed.

A learned behavior might default to using the index finger to push down the stapler, but the stapler's model is about how it behaves, independent of how the body interacts with it. These models may be separate but are also entangled, as the transition model captures how everything changes given the current state and an action.

The variables shown previously would not all be in layer five; they would be represented in other layers, and layer five tells us how to move through them given actions. For example, XT is in L6, FT in L4, OT and PT in L2/L3. None are in L5; L5 is about routing between them.

The transition model itself is also subject to change and isn't fixed. For example, a simple action like movement through space affects XT+1, possibly via a direct or predicted connection, or through actual sensor movement, changing FT+1. These changes can influence the object model, such as recognizing a mug instead of a stapler. Here, the transition model is simple, like path integration.

A more complex action, like persistent downward pressure on the stapler head, could change the object's state to "stapler depressed," requiring a more complex transition model. Later, I'll discuss how we might represent a transition model capable of capturing such changes.

And then lastly, the object state—for example, if the stapler is opened or if the ID changes—can influence the transition model. We would expect the transition model to differ between objects, but also for the state of the object to influence it. For instance, when the stapler is open, moving from one location to another might yield a different result than if it were closed.

With more complex objects, interaction can make new affordances available. Closing the stapler allows you to use it; opening it allows you to load it. The transition model becomes more complex, and the notion of space and state becomes more flexible.

All these factors are part of the system's possible actions and state changes. Different parts of the state may be affected and can influence each other. It's not as simple as moving through an environment and taking actions; everything feeds back.

Jeff, regarding your point, it sounds like you were saying actions affect the state of the object ID or its representation. I like this diagram; it's thought-provoking, though I may interpret it differently. It's a good starting point.

If you want to brainstorm, I can do that, or I can continue with the presentation. I'll just finish the last bit for clarity.

Before I forget, when labeling, I wrote "feature detectives" and "feature location binding cells." What was the name of those cells with specific tuning responses that fire consistently? They're a flavor of bipolar cells, but sometimes called something else. Not stellate cells. I have a mental image—skinny, with limited dendrites and axons. Some papers just call them bipolar cells. If you remember the term, send me a link. The name isn't universally agreed upon.

The point is to bring in hierarchy. For example, to use a stapler, you move to it, then depress the stapler head, changing its state. A more complex example is making coffee, where hierarchy lets you skip or select options. Once the machine has water, you can turn it on, changing its state, and then press the start button, changing the button state.

Much of hierarchical action policy literature discusses sending down actions that produce sub-actions, but I wonder if we also want top-down feedback that passes a goal state. This would mean the transition model is conditioned not just on the current state and action, but also on the goal state, continuing until the system achieves the goal state. The transition model is not the same as the policy.

The output would not be the next state, but the next action, independent of the transition model, though the transition model is one of its conditioning elements.

The idea is to pass a goal state to a learning module, which then transitions through states by initiating whatever policy it has until it reaches the goal state.

That final state, depending on how it's specified, likely involves the representation at the L2/L3 layer—the object-level representation—but achieving it might require an interim location, XT. For example, if the goal is to depress the stapler, the learning module knows it must reach the stapler head, then either finish the task or pass responsibility to a lower-level module. The black line represents the desired goal state, which is top-down feedback from a higher-level learning module.

Because of its transition model, the module knows it needs to get to the stapler head, then perhaps pass a goal to the stapler head model, such as applying downward force. The stapler head model then takes over. If the module is making progress toward its target state, it sends motor outputs from L5 for execution. If it needs something else to be achieved, it sends a target state to another learning module. For example, in making coffee, after filling the machine with coffee, the next step is to ensure the machine has water, so a goal state is passed to another module.

I like the idea of sending goal states instead of actions. Currently, our goal state only captures the sensor's location, but we could expand it to include the state and pose of the object and the hand. For example, to make coffee, you specify the desired state of the coffee pot and hand, and those goal states are translated into action sequences elsewhere. The main question is where the goal state turns into actions and where the policy resides—whether in the column or elsewhere.

L5 can send top-down connections, so it could send goal states, but it also has a policy that generates actions. The policy would exist here, but I need to check if L5 has hierarchical projections down, as it might be L6. There's a lot of literature, so I'll double-check.

A single learning module must be able to implement an action policy and put the model into a desired state. If this happens in the cortex, it happens in every learning module, and hierarchy can be added on top. If a top-down request is made to depress the stapler, the module determines the current state and location, then generates the behavior needed to achieve the goal. L6 represents the current position of the sensor or body, and the combination of this and the model state generates an action in L5 to move the model to the goal state.

If you have ten fingers on the stapler, each with its own learning module, all modeling the stapler and knowing its state, a top-down request goes to all modules. Each calculates how to move its finger to achieve the goal, but only one will actually do it. There are many ways to push the stapler down, and each module can calculate its own behavior, but only one will implement the required action.

I'm just interpreting what you're saying. As Viviane pointed out, we do need to execute the action at some point, and there's a balance between passing the task onward and doing it yourself, similar to middle management in a company. You can only subdivide a task so many times before someone actually has to do the work. Pressing a stapler may not be the best example, since once you reach the target location, you can just generate the action. One important aspect not shown here, but worth exploring next time, is that we also have models for complex motor systems, like the hand, which are involved in executing the action.

Why not just send actions? Why send goal states? It's easier for the higher-level learning module to know nothing about the lower-level module; it just needs to specify the desired outcome. This separates knowledge of necessary states—like the coffee machine button being pressed—from the actions that achieve it. For example, pressing with an elbow is independent of the required state.

It's also easier to represent when the top-down directive is satisfied, since the current state will equal the target state. If that representation is in L2/L3, it's sent forward, so we immediately know if we were successful. If you send an action, it's less clear whether the desired outcome was achieved. My assumption is that no actions are sent down, only desired states.

But what about the motor output from L5? Imagine a two-level hierarchy: the top says "depress the stapler," and the lower level decides who will do it and generates the behaviors. The motor outputs of the higher-level region are expressed as projections from layer 5 cells subcortically. The motor system outside the cortex is already hierarchically arranged, with nerve centers in the spinal cord, brainstem, and cerebellum. Many ingrained behaviors are already hierarchical or complex. A level two region may issue a higher-level command, and the lower-level motor system interprets it.

Layer 5 and higher and lower regions may project to complementary hierarchical motor systems in the old brain. If a higher-level region finds a correlation between its output and a system below, it will use it. A higher-level learning module's layer 5 may project to the basal ganglia, while a lower-level one projects to the spinal cord.

These are all subcortical projections. Some may go to the motor cortex, but motor cortex is itself cortical. I'm not aware of layer 5 cells projecting elsewhere, except as described by Sherman and Guillory: the large, intrinsically bursting layer 5 cells have axons that split, with one branch going out of the cortex to the old brain (related to behavior) and the other going up the hierarchy through the thalamus. Other layer 5 cells, which seem to be voting cells, do not project subcortically but to other layer 5a cells in the cortex. There appears to be a voting layer and a motor output layer that either exits the cortex or passes up the hierarchy. That's what Sherman and Guillory have written, though it may need refinement.

So, I argue there's no reason to pass down behaviors, and it doesn't appear to be happening. There's evidence that layer 5 cells project to different levels of hierarchy in the old brain. The cortex may be modeling existing body behaviors—like walking and reflexes—that are old brain behaviors, mapping its hierarchy onto the old brain's. A high-level cortical region can give a high-level state or behavior goal to a part of the old brain, while a lower cortical region projects to a lower behavioral section. 

We can express all hierarchical behavior in the cortex as target states. At the lowest level, something in the motor cortex might specify a target, such as the hand being in a grasping state, which is then sent subcortically and turned into motor commands. Layer 5 cells never directly innervate muscles; instead, they project to subcortical motor sections and learn to associate their representations with existing subcortical states. They never directly drive musculature, but influence the old motor system to act, pairing their representations with those that already exist elsewhere.

If you send a target state, it's easy to tell when it's been achieved, allowing a higher-level module to continue a complex sequence once the desired state is reached. A lower-level module can quickly signal if a target state is outside its possible state space, prompting a higher-level adjustment. This approach suggests a possible unification of sensory and motor representations: if motor outputs are target states, they're analogous to the sensory or object representations sent up the hierarchy (L2/L3). This means they're fundamentally linked, though it's still unclear how object states are represented. We're saying everything is in control, but we don't yet know how it's done.

Okay. I was just thinking about this—if we put it this way, the output states and the input target states will have the same format: objects at poses and sensors at poses. In the hierarchy, you get target states from the higher level and send back your current state, but the main question is, where do the highest-level targets come from? For example, why do I want to make a cup of coffee now? At a certain level, basic needs like hunger and sleep, possibly from the hypothalamus or amygdala, drive these goals.

My suggestion is to focus on how a single cortical column or learning module can build a true sensorimotor model of an object. We should solve how one module interacts with and changes the state of an object on its own, then introduce hierarchy to overcome limitations, as we did with the logo on the coffee cup. Our goal isn't to worry about where the top-level goal comes from; we can just specify a goal, like pushing down a stapler or opening it, and see if the system can achieve it.

We could make an artificial system where we specify the desired state and see if it can reach it. The breaking point for a single learning module is when hierarchy is needed, such as when multiple fingers are involved in manipulating an object. This isn't really hierarchical composition, but rather a necessity for coordination.

Some behaviors, like making coffee, require the "where" pathways, but for now, we should avoid tasks that require navigation. It's better to focus on tasks where the hand is already on the object, and the manipulation happens in the "what" space. The early evidence for "what" and "where" pathways shows that if the "what" pathway is damaged, a person can move their hand to an object but can't identify it until they touch it. We want to skip the navigation and start with the hand on the object, focusing on manipulation.

I'm still working through papers and developing a detailed model of the column and how it relates to these ideas. I'm excited to work on this problem, though progress is slow.