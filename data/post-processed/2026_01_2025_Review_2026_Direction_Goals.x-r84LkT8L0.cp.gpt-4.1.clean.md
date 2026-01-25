2025. I didn't get as much time as I wanted for this review, so I put together a few slides highlighting the main accomplishments of 2025. There were many significant events this past year, and it's easy to lose track of them. This presentation doesn't cover everything we did, but it's a reminder of all we accomplished and how much can happen in a year. For those who joined recently, like Rami and Jeremy, we started operating as a separate non-profit entity at the beginning of last year.

We did a lot of organizational work, including setting up new accounts, subscriptions, paperwork, repositories, a board of directors, press releases, and announcements. We received our 501c status after submitting the application and heard back later in the year, around October or November. Now, donations to the project are tax deductible, and we can get discounts on subscriptions.

We have a new website since splitting from Nuenta, and it's been evolving over the past year. There were many communications with people in various industries and universities. We collaborated with professors and students at places like Loughborough University and Penn State, gave talks at the Chen Institute, and attended conferences like the Alberta Reinforcement Learning Conference and Coxai. We also engaged with companies in the ultrasound space, such as Butterfly, Sonastar, Bloom Standard, GH Labs, and IPRD Solutions, for hackathon preparation and proof-of-concept work with Monty. Through the Caddy collaboration, we worked with Priya Panda. We now have a spreadsheet to track all these interactions and collaborations.

We presented the project at various venues, including podcasts, university groups, and the RL debate series. Tristan presented at several places, like the Austin Robotics and AI Meetup, and Scott presented at the Chen Institute. We hope to continue this outreach next year. We released 162 videos on YouTube, processed and published them, and now have 1,600 subscribers, 6,000 hours of watch time, and 56,000 views in 2025. Engagement increased after the preprints were released in July and after we started posting YouTube Shorts.

The website views also increased and became more global, with spikes after the paper release and new posts. On Discourse, we've seen more users, including anonymous ones and crawlers. Everyone has been active on the forum, posting replies and engaging in discussions, which takes a significant amount of time. We've started to receive more substantial external contributions, including blog posts, feature proposals for Monty, and testing improvements. Artem Kisarnoff made a video about the Thousand Brains Theory. There are now so many blogs that we created a documentation section to collect them. We also publish meetings and community working group sessions on YouTube, and people contribute to future work items on our roadmap. Several contributors are taking on larger tasks, helping us achieve our goals. The project has been starred and forked by many—270 forks and 21 code contributors. Some people are applying Monty to MNIST, Robot, Audiobot on the phone, or other projects.

Will added an interactive future work widget to our documentation, allowing people to filter roadmap items and learn how to contribute. More data and text have been added to these items.

Everyone has been helping to improve our documentation, which now includes images, embedded videos, and many up-to-date tutorials. We've added documentation on reference frame transformations with animations. Most pages have been updated, restructured, or cross-linked. Tristan and Jeremy added style guides for code and typing to help contributors follow our standards. Nils added language about large language model use. Our project showcase now features more items.

The interactive Future Work Roadmap has more descriptions, and there's a new page on theory for object behaviors with various figures.

Lots of documentation updates were completed. The heterarchy paper preprint was published and submitted to a journal, with significant effort going into writing, creating figures, reviewing, and adding references. The DMC paper was also published as a preprint and accepted into a journal, which was a major achievement this year. Resources were published around the preprints, including explainer videos, blog posts, and shorts. We held two retreats, one in California and one in Brighton, and organized two virtual brainstorming weeks with extensive whiteboarding. The Robot Hackathon took place in two locations, where we built several Monty demos. This was the first time Monty moved its sensors in the real world, learning and recognizing by moving real motors and sensors, which was a significant milestone.

I explored Monty for ultrasound further, created several write-ups, held many meetings with various people, and developed a new dataset.

Tutorials were published on using Monty in custom applications, and the Monty for robotics projects were documented as examples for real-world applications, including animations, figures, and guidance on reproducing the projects.

There was substantial conceptual progress, literature reviews, and brainstorming, resulting in numerous write-ups, presentations, and intense discussions. We made significant progress on modeling object behaviors, disclosed the initial idea earlier in the year, shared videos of the development process, and refined the concept to the point of having a concrete outline for implementing this capability in Monty.

Rami added the ability for Monty to resample hypotheses quickly, allowing Monty to switch hypotheses efficiently when moving between objects. Previously, Monty couldn't do this, but now it performs this task well. Rami also introduced more sophisticated methods for adding and deleting hypotheses, keeping the hypothesis space small when Monty is certain of its location and only expanding it when uncertainty arises, such as when encountering a new object. This work is currently being integrated into Monty by Rami and Jeremy.

The compositional object dataset and metrics were created, providing a way to evaluate Monty's ability to model compositional objects. A saliency-based decoy policy was prototyped, with Scott focusing on detecting saliency, moving to salient points, and implementing inhibition of return to avoid repeatedly switching between the most salient points. Extensive testing was conducted, including during the hackathon with Jose. Scott and Tristan worked on integrating much of this into Monty, resulting in a major integration project where sensor modules can now emit goal states, which are selected and sent to the motor system.

A prototype was developed for extracting 2D features, enabling detection of texture features such as printed elements on a cup, in addition to shape, curvature, and surface normal. A sensor module can now detect these printed features.

Monty progressed to version 0.17. Tristan worked extensively on disentangling the motor system and enabling policy swapping, with numerous PRs contributing to this effort. Jeremy focused on Mujoku integration, Python updates, and habitat dependency removal, all of which were complex and interconnected issues. Tristan and Jeremy switched configuration management to Hydra during the November Focus Week and finalized the process in the following weeks, resulting in Hydra being used for configuration management. Many other improvements were made to Monty and related projects, with 425 merged PRs and 677 opened PRs for tbp.monty alone. There are 29 repositories overall, many of which saw significant activity, including feature branches for new research ideas, internal infrastructure, plotting tools, and video processing tooling.

Tpp Plot was developed by Rami, providing a robust library of visualization tools.

Tristan did a lot of platform planning. You've all seen the detailed breakdowns of the items needed to build the platform. We started a new prototyping process where we build prototypes on a fork and then integrate them into Monty once they are proven. The community event was organized. This slide was made in February last year, outlining the direction we were considering—figuring out object behaviors, which we didn't know how to model yet. We were looking into removing the one episode per object assumption to enable better unsupervised learning, which was a prerequisite for compositional modeling. We added a testbed for that, policies, and LM updates. On the implementation side, there were various code refactors, such as the data loader and dataset refactor, making motor policies more modular, improving documentation, and fostering the community.

Looking back, we accomplished a lot. We added documentation, published videos, fostered the community, and refactored the data loader and dataset. Other refactors, like the policy refactors, are ongoing. Rami's changes removed the one episode per object assumption, and it works well. We have a compositional modeling testbed and are working on improving performance on that testbed. We developed a theory for object behaviors and have ideas around other topics, or at least spent time discussing them. Light green items are still in progress. Overall, we made good progress on all these areas and others mentioned previously. Great job, everyone. It's been an exciting year.

Thanks for all the work you've put in. Any questions before I move on to 2026?

Jeff: It's interesting to see it again. For my old brain, I realized all the things we accomplished. It was a good first year, and I've really adjusted my perspective. It turned out pretty well.

Viviane Clay: I agree. It always feels like more than you remember, especially when looking at the numbers—how many pull requests we made to Monty, all the posts on Discord, the interactions, research prototypes, ideas we tested, and features we added.

Niels Leadholm: I feel like a lot of things are building momentum. From a technical perspective, it's about being familiar with the code and how Monty works, and then all the organizational aspects you mentioned, Viviane. Many of those are one-off tasks. It's cool that we've made all that progress, and it feels like we could do even more next year.

Jeff: Niels and Viviane worked on this beforehand, but really, starting a year ago, we had a running start. Still, there was a huge amount accomplished, and at the beginning, you don't know how it's going to turn out. There are so many issues—organization, funding, uncertainty. It all turned out pretty well so far. This is an amazing accomplishment for the first year of an organization like this. Pretty impressive. Now we can focus on next year.

Viviane Clay: Definitely makes me excited for the next year.

Jeff: I'm always worried about the future. We did well last year, but next year is another challenge. I'm a worrier.

Viviane Clay: I think, as Niels said, we've already put a lot of work into things, and we'll be able to reap the benefits this year.

Jeff: I think that's right.

Viviane Clay: I'm pretty hopeful for the next year.

Jeff: I'm always worried about what big things we might have missed. What haven't we thought about? It's just my normal way of operating to always be concerned about the future. That keeps you on your toes; you never get complacent. You never think you have it all figured out. It's always, what are we missing? But so far, it looks great.

We had no real setbacks this year. We could have, but we didn't.

Viviane Clay: There are always unexpected things and issues we didn't plan for, especially with research. We don't know if things will work out, especially when developing the theory, but it felt like we made great progress with object behaviors and gained much more clarity on other topics.

Jeff: The further you get, the more pieces you fill in, and the less likely you are to find a big gap you hadn't considered. It feels like we're filling in the remaining pieces.

I've expressed my optimism before. I said we might wrap up the big theory things this year. If not, then next year, but I'm hoping for this year.

It feels doable. But you're going to tell us what we're doing next year.

Viviane Clay: Yes, we need to do just that—wrap everything up.

Jeff: On the theory side, the other work will take a long time.

Tristan Slominski: I have one question. Jeff, you said no major setbacks. What would you have considered a setback?

Jeff: You don't know—it's just one of those things you worry about. Maybe there's some deep theoretical mistake we've made, like it doesn't work with reference frames, it works with something else. We have a whole set of fundamental assumptions about Monty and the Thousand Brains Theory. There are proposed theoretical ideas, and in science, nothing is ever proven; you can always discover later that you made a fundamental error. Newton didn't get gravity right, Einstein got it better, but maybe Einstein is wrong—there's always something you could get wrong, and you don't know what it is at the time. You always have to be thinking about that. You don't want to get so far down the path and realize you made a big mistake. Andy Grove, the CEO of Intel, used to say, "Only the paranoid survive." I interpret that to mean you always have to be worried about what you might be getting wrong. I think about that all the time, and yet I don't see anything, but I don't stop thinking about it. That's the way to be successful—always thinking, "Don't get complacent. Is there something I'm missing? What's the big idea?" I watch all the developments in deep learning, trying to figure out if I'm misunderstanding something, if there's something more fundamental going on that I don't understand. I haven't seen that yet, but I worry about it. I still feel very confident that our approach is the right way to go for AI and machine intelligence, but you worry about it.

Niels Leadholm: That's actually another interesting point. Over the last year, there's been greater acceptance in the broader community that deep learning, at least in its current form, isn't going to deliver a sudden, fast takeoff to AGI or whatever. There has been a lot of hype around that. In some ways, that's another encouraging sign. At the same time as we've seen a lot of promise in what we're doing, more people have looked at these approaches, and also predictive coding from a neuroscience perspective, and there's been more skepticism. One of the leading alternative theories in neuroscience and one of the leading alternative approaches in AI have both had a growing chorus of skeptics, which doesn't prove that what we're doing is correct, but it is an indirect signal suggesting we could be on the right track.

Jeff: I feel like our work is successful, not just because, as you point out, Niels, it's good that if we're right, these other approaches will eventually be set aside, but mostly I feel like this has to be right. You put all these pieces together, and so many fit together so nicely that it's hard to imagine them being wrong. But you never know 100%. As much as you're almost certain, there are always skeptics. One of the strengths of entrepreneurs is having conviction in your future vision—being certain of it, not just wishful. You have to plow through, even if 99% of the world doesn't believe it and believes in something else. If you're right, you're right. I always say time is on our side. If we're right, time is on our side. The world will come around to our way of thinking. So I'm always asking, are we right? Is there anything we're getting wrong? What's the big thing we're missing? I can't see it yet, so maybe it doesn't exist.

Viviane Clay: The only real judge of things is time.

Jeff: If we're right, the world will come around to our thinking. You just hope it's not 50 years from now—you hope it's one year from now.

We have to promote our ideas, and we also have to let these other approaches, whether predictive coding or deep learning techniques, run their course until people realize their limitations. Many people don't have a clear vision about the future and just follow whatever is currently popular. But over and over in the history of science and technology, you see that isn't the right way. Things that were thought to be hot just fall apart after a time. You have to stick with your convictions. It's not just wishful thinking—we're not just hoping this is right. Everything seems like it has to be this way. I'm very confident. At the same time, you can be paranoid, always asking, "What could go wrong?" I don't know yet; we haven't seen anything wrong. It doesn't seem like anything's wrong, but I'm constantly worried about it.

Tristan Slominski: What makes me paranoid is what you said about current things having to run their course, because there's been an enormous amount of resources poured into them, which might really extend the time it takes for those things to run their course.

Jeff: Maybe, I think...

Tristan Slominski: That's what I'm paranoid about.

Jeff: Maybe, or my observation is a different sort of course would run out. What might happen is everybody sours on all this. It's not that deep learning will go away, but people might think it's overhyped and only does a few things. That could impact us, because then nobody's interested in machine intelligence at all. That happened to me with mobile computing—there were early failures like the Apple Newton, and then everyone said it was a stupid idea. No one put money into it; it all dried up overnight just because of some notable failures. That's something I worry more about: people just giving up on this altogether, as opposed to it taking forever. The nice thing about deep learning right now is that so much money is being put into it, there's almost certainly going to be some big fallout, so I don't think it's going to disappear.

Niels Leadholm: Right, it kind of feels accelerated, actually.

Jeff: Gift of this.

Niels Leadholm: Without all that money in it, they can just keep saying scaling is all you need. But if you actually finish the plot and put all human resources into this, and the payout's still not that great, then it's like, okay.

Jeff: Yeah, right.

Niels Leadholm: Need to revisit.

Jeff: I...

Niels Leadholm: Is that a thumbnail?

Jeff: I remember the earlier wave of AI in the 80s and early 90s, when they were doing expert systems. At the time, a lot of money was put into it, and people were reporting all the successes in the press. You could easily believe it was going to be huge, but it all fell apart. Even though they said it was working, the current wave is a little bit like that. There are a lot of projects with deep learning that aren't really panning out. Some are, but a lot aren't. We'll have to see. But I think we can be confident that our approach is right. There are a lot of things we can do that no one else can do. It's going to be ultimately successful; we just have to keep going, improve our work, and let the others run their course.

That's life.

But it's great. I feel like we're on the right team. We're going to win.

Viviane Clay: Yeah, it definitely feels pretty exciting.

Jeff: Yeah.

Viviane Clay: With that, let's talk about next year.

This is borrowed from the diagrams that Tristan made that I showed earlier, so I don't want to take all the credit for this, but I thought it was a really nice way to visualize things. It's a bit simplified. Feel free to interrupt if you disagree with something or have a question.

Our basic process right now, developed over the past year or years, is that we develop some theory. The ideas from the theory turn into prototypes—research projects that the researchers develop on separate forks of Monty. Once a prototype is proven to work, it turns into an integration project, and a researcher pairs with an engineer to integrate it as a Monty feature into the main TBP Monty repository.

The more features Monty has, the better demos people can build. If Monty has new features, new kinds of demos can be built. After building demos, those could be turned into actual applications and real-world use cases. We're not there yet; there isn't any real-world deployment of Monty at the moment. We dabbled a bit in demos during the hackathon, for example. There are also cases where more Monty features enable new prototypes, and prototypes can build on top of each other.

As we prototype ideas, that can also feed back into the theory and reveal issues we didn't anticipate.

Jeff: Or some...

Viviane Clay: Things that actually don't work as we thought they would.

We also have platform quality, which helps in many ways. If the platform quality is better, it's easier and faster to build prototypes, add features to Monty, do integration projects, build demos, and build applications with Monty.

Does that make sense so far?

Okay. Our researchers are working on developing theory, building prototypes, and integrating the prototypes with the engineers. We've spent a small amount of time building demos, like during the hackathon and some wrap-up work afterwards. The engineering team is not working on theory or prototypes, but focuses on platform quality improvements, integration projects, and building demos.

Generally, this is how we want it to be. We don't want to spend our internal resources on building applications or even spend a lot of time building demos ourselves.

I've simplified the picture a bit, removing some of the back arrows so it doesn't get too complex. There's another part of this equation: the community. Community members can contribute to almost anything. It's a bit hard for the community to contribute to theory, or at least it hasn't happened yet. It would require someone to do deep dives and watch all our research meetings. Maybe people could test the theory and experiments, like experimentalists, but for now, I didn't include that in the community box. But they can build prototypes, add Monty features, build demos, build applications, and improve platform quality.

And also promote the project and help us grow the community. What really makes the community grow is seeing demos and applications. Some people are intrigued by the theory and ideas, but what's really going to make Monty take off is once people start using it and seeing its benefits. Right now, we don't have any applications and few demos, so most people in the community think this is a cool idea, a cool project, but I think once people actually start using Monty in demos and seeing its benefits, that will kick off this community growth much more.

Just like with LLMs, they were interesting in the research community, but once people saw ChatGPT and could play around with it, it really started taking off. A simple, easy demo led to a lot of growth. As the community grows, this whole green box has more and more resources and can contribute to other things, creating a positive cycle. What we want to do is kick off the cycle of the community growing and contributing back to the project, because if they're actually using Monty, they want to improve it.

How could this tie into our goals for the next year? Some things we want to do to encourage this are, when making platform quality improvements, focus on improving the ease of building demos and applications. Initially, Monty was developed as a research codebase for building prototypes and Monty features, which used to be the same thing because we didn't have this prototype-feature workflow. It was built as a research code base, and now we want to turn it into a platform that you can use to easily build demos and applications. We don't want prototyping to get worse or harder, but we want to focus improvements on ease of use, especially for building demos.

Similarly, with prototypes and Monty features, we should consider whether a feature will unlock new capabilities useful for building demos with Monty. Focus on developing features that unlock new applications. Once we can model compositional objects and a compositional world, that unlocks many new application areas. Once we can model object behaviors and things that move, that unlocks more application areas. Once we can use Monty's models to manipulate and interact with the world, that unlocks a huge range of new applications. As we prototype and think about these things, consider what we can actually do with this and what it unlocks in the real world. Lastly, this is a cool idea that Tristan had.

We call it the Solutions Incubator. It's the idea to encourage community members to build solutions with Monty. The basic premise, and we have to figure out the logistics, would be to offer grants or stipends to people who come to us with an idea of something they want to build with Monty. It's not like internships, where they come and say they want to do an internship and we have to come up with what they should do. Instead, they come to us with an idea, pitch it, and if we think it's realistic to build with Monty, we provide a grant, some money, and guidance, like meetings at a certain frequency. They spend a couple of months actually building that demo and presenting it to us, writing it up somewhere publicly. That way, we have idea generation from the community, with people coming up with ideas we would never think of ourselves.

We want to try to kickstart the cycle of having actual demos built, people spending time building useful things with Monty, and that leading to community growth. That's the idea: having more demos and use cases of Monty leads to community growth, which leads to more community members, which has a positive effect on everything.

Does that make sense? The basic premise is to focus both platform quality improvements and prototypes and Monty features on increasing the number of demos that exist with Monty and community growth.

Ramy Mounir: Is this only going to be for demos, or is it also for prototypes? Are they building research prototypes as well?

Viviane Clay: Community members can build research prototypes, but that wouldn't be the Solutions Incubator's focus. It would be more about actually building something where Monty is used in an application.

Any other questions?

Jeff: I have just an observation.

Viviane Clay: Definitely don't mind.

Jeff: The right side of the diagram is a complete unknown to us. We don't know what the first applications will be, and that's typical with new technologies. Usually, the first big use comes from someone outside the core team, often from the community. With ChatGPT, as you pointed out, there was something anyone could use without technical expertise. I don't know if that's going to happen for us. In one of our first board meetings, colleagues asked, "What's your ChatGPT moment? What's going to be the similar thing for us?" I'm not sure we'll have one. It's unusual because our technology requires interfacing with sensors and the physical world—it's not something you can just use in a browser. But maybe there is a possibility. There's a big question mark on the right-hand side: what will the big applications be? What kinds of applications and sensors will emerge? We haven't focused on that yet, so the idea of an incubator is useful—not something needed long-term, but valuable in the short term to generate ideas and let people explore. We need that. We can build the greatest platform, but someone has to see how to apply it. That takes domain expertise we may not have. In general, I like the idea. We need to gently seed things on the right-hand side to see what catches. Maybe many incubators won't achieve anything, but it's still a good idea.

Eventually, something will catch. We can all think about what would be a really cool way to get people excited and using it in a fruitful way, but that's not our main goal. Our main goal is to build the platform first.

Viviane Clay: The nice thing about the Solutions Incubator is that it should require minimal effort from our side to actually build the demo. It would require some meetings and communication, but someone external would be building it—likely someone with more domain knowledge of the specific application. That's a nice aspect.

Jeff: Right. If we made two or twenty, and one or two were successful, that would be fine. Who knows? It's really hard to predict what will happen on the right-hand side.

Viviane Clay: Yeah.

Okay, so what does this mean for the next year? What do we really want? We want Monty to be used in sensorimotor applications to solve real-world problems. There are many challenges in the world, and unless we innovate, we won't solve them. I don't think we'll solve them with deep learning alone. Maybe some can be solved by throwing a lot of data and compute at them, but many can't, and even when they can, it's usually not the most optimal solution if it requires burning a lot of energy and money. Monty is our bet on an elegant solution to these problems. It has immense promise and potential for making a positive impact on these applications and more.

We likely won't get there this year. It's not realistic to expect Monty to be used in a real-world application that requires interacting with the world this year. What we can aim for is to pave the path for building sensorimotor applications with Monty. Concretely, we need to figure out the open theoretical questions, especially around using models to manipulate the world. The big open question is how to actually interact with the world, not just move sensors to recognize things. Hopefully, we'll make some progress on that this year—maybe even figure it all out. We want to add capabilities to Monty that unlock more interesting applications. That's the focus of the prototypes and integration projects: picking which ones to do based on what applications they unlock and how much more useful they make Monty. Making it easier to build applications with Monty is the platform quality side—what can we do to improve platform quality and make it easier for people to build? Lastly, we want to get people interested in building applications with Monty. Part of that is the Solutions Incubator offering some funding to build something, but also promoting the project, presenting at various venues, publishing, interacting with people on Discourse, and so on. The community-building aspect is about figuring out how to get people interested in this approach before we have a lot of cool demos or our own "ChatGPT moment"—or a different kind of moment.

Going back to this diagram, here are some concrete goals for the next year that I think are doable and would hope to see by the end of next year when we do year reviews. We want to figure out the theory around causal interaction with the world—learning causality, learning how to produce actions that cause effects, and manipulating the world. In terms of prototypes, we plan to prototype our theory developed last year around object behaviors and test if it all works out.

For Monty features, we aim to model compositional models. We have several prototypes in the pipeline to integrate and develop further, along with more theory ideas that need to be prototyped and integrated. One sub-point is planning a publication around modeling compositional models in Monty and the benefits of that. We'll scope this in the next month or two to decide if we want to do a paper or a simpler form of publication, but we want to demonstrate the benefits.

Regarding platform quality, there's a lot to unpack, and Tristan has detailed diagrams, but to summarize: we want to separate platform, experiment, and environment. The idea is that Monty's class structure has the platform as the Monty class and its internal classes—learning modules, sensor modules, motor system. Separate from the platform is the environment, which could be a physical robot or a simulator like Habitat or Mujoco, but it's distinct from the platform. The experiment wraps around both and controls the simulator or task setup, measuring performance, and so on. It's not necessarily part of the platform, since you might use Monty in a robot in a factory without running experiments with episodes and epochs. By separating these three components, Monty becomes a platform you can plug into any environment or experimental or application setup. This involves many sub-bullets and complicated subtasks. If you're curious, there are Excalidraw boards from Tristan and some simplified versions from me, which I can link later on Slack if you want to take a closer look.

On the community growth side, we have continued documentation of the project, so when people join, they find documentation on how to build with Monty, as well as publications, community interactions, and collaborations, as we did in the past year. For demos, the solutions incubator will take a large chunk of time for the external person who receives the grant, but we'll still need to vet people, start the program, and interact with them throughout. That's the high-level view—top-level goals for the next year. If there are questions, let me know. Does that sound reasonable to everyone?

Jeff: I think it's a nice summary. It's a nice way of looking at all of it.

Viviane Clay: Cool. Thanks to Tristan for coming up with a lot of this framing and the solutions incubator idea.

Jeff: Yeah.

Tristan Slominski: I agree, Tristan. We could never come up with the diagram, so thank you for simplifying all of that.

Jeff: I'm going to say—

Tristan Slominski: It's more insane.

Jeff: We need our own process with Tristan moving from his ideas and theory into practicality. How do we make this easier for everyone to see? Thinking about this, and going back to the other question about what will bring our technology into the world—sometimes you have to wait for new things to occur outside of our world, like new sensors or new robotic things. One thing that occurred to me was drones. Drones weren't a big thing ten years ago. When did they start becoming a big thing? I don't know. But that's a whole new sensorimotor platform that lots of people have. Suddenly, the appearance of something like that is maybe what these killer applications for our technology require—a new thing that hasn't happened yet. We can't necessarily predict that now. This goes back to the incubator idea. There are probably new technologies and things like drones, maybe drones themselves, that are coming about where our technology will really take off. We have to keep our ears to the ground or let others think of those things, because that may be what's required to have our big moment—something that millions of people have, and suddenly they can use it, and it's a new thing. We can make it better.

Viviane Clay: Yeah.

Jeff: Anyway, it's a great summary.

Viviane Clay: Cool. And then, yeah, there's also...