Today I'm going to talk about the paper "Sorting Out Lipschitz Function Approximation." The paper has a couple of motivations. I wanted to start with a big picture overview, and I have some slides in this presentation that try to condense a semester's worth of statistical learning theory into a few slides. I did this not necessarily to convey all that knowledge to my audience, but as an exercise for myself to go back to the basics and make sure I understood them.

At a high level, the idea is to reduce generalization error and increase adversarial robustness. This is the main problem they're trying to tackle. They also discuss topics I'm less familiar with, like Wasserstein distance. I came across this paper because I've been interested in the intersection of symbolic reasoning, deep learning, and solving discrete optimization problems. Until now, I had the impression that deep learning had glaring weaknesses, such as being unable to do something straightforward like sorting a list, despite its impressive capabilities in other areas. I didn't think it could do that, but a friend told me it actually can and suggested I check out this paper. That's how I got here.

All right, time for a quick overview of statistical machine learning to get some notation on the board.

Generally, we assume there's some input domain X and an output domain Y. Frequently, to derive theorems, we assume the labels Y are binary, zero or one. Not all points in X are equally likely; there's a data-generating distribution D that samples points from X, and a labeling function F that takes points in X and labels them with something in Y, which for now is zero or one. There's a loss function, and in early basic theorems, we just assume it's zero-one loss for simplicity. You have a training set XS, which consists of a series of tuples: point X and then F of X, its label. Models, such as neural networks, are just functions. The set of all possible models is called the hypothesis class. For example, if I'm using ResNet-50, the hypothesis class would be the set of all parameter configurations for ResNet-50. A single model is what you try to obtain through optimization—it's a single lowercase h in that hypothesis class. Training is basically trying to approximate F, the labeling function, with some h. So I'm searching through this big stack of hypotheses to find lowercase h. Generalization error is the overall error—the expected error, the expectation of the loss over D, the whole data-generating distribution, minus the loss on the training set. Most of this is probably obvious, but it was an exercise to make sure I understood some things.

Going one step deeper, there are a couple of important notions to keep in mind. There's sample complexity, which is a function from (0,1) × (0,1) to the natural numbers. Sample complexity asks: how many samples do I need to be within epsilon of the truth with probability at least one minus delta? Going back to generalization error, if I want my true LDH—the expectation of the error—to be within epsilon with high probability, how many samples do I need to guarantee that? Then there's the notion of VC dimension. This is the largest size of a dataset C, a subset of X, such that my hypothesis class shatters it. Shattering means I can label it every possible way.

To make that concrete, the size of the restriction of H to C is all the ways H can label C. I can shatter this set if the size of the restriction of H to C is two to the C, or you can replace two with the size of the output space Y. Generally, the more parameters you have in your model or hypothesis space, the larger the VC dimension will be. Neural networks with many parameters may have a very high VC dimension, but it doesn't always correlate with the number of parameters. In "Understanding Machine Learning" by Shai Shalev-Shwartz and Shai Ben-David, which is my reference for statistical machine learning, they give a counterexample: even something simple like a sinusoid function with a ceiling non-linearity applied to it can have an infinite VC dimension, because you can crank up the frequency to hit the training points with perfect labeling.

I know I'm talking a lot about statistical learning theory, but we're almost done. I wanted to do this to contextualize the actual problem they're trying to solve in this paper. Two more ideas: there's the growth function tau with respect to a hypothesis class, which asks how many ways I can label a small dataset C with my hypothesis space. As I change the size of C, from one point to two points to ten points, how many functions can my hypothesis space represent?

You can manipulate symbols for quite some time and prove the following textbook generalization error bound: the gap between the overall risk and the risk on the training set is bounded above by this quantity, where tau(H) is in the numerator and depends on the VC dimension, and the number of samples is in the denominator. If I want to decrease my generalization error and get a tighter bound, I can do two things: lower the VC dimension of my hypothesis space, perhaps by choosing a simpler model or reducing the number of parameters or layers, or get more samples. These are the two sides of this inequality, but generally, we want to make this as small as possible.

Could I ask a question, Ben, about your first paragraph up there?

Epsilon and delta—are we supposed to have some kind of intuitive feel for what the shape of epsilon-delta space is?

An intuitive feel for what that space looks like? You have epsilon within the truth, and then with probability one minus delta. I'm trying to understand the relationship between those. There's a functional relationship, and I'm trying to figure out whether, if I plotted M of h as a function of epsilon and delta, it's just a smooth thing or if there are all sorts of gotchas.

The way I would think about it is that there's a trade-off between epsilon and delta. If I just need my risk to be barely above chance, epsilon is my error term. If the error can be really high, I can guarantee that with probability almost one—delta can be very small. On the other hand, if I want the error to be very small, I may have to sacrifice probability. If I want to get 100% accuracy, it may be possible, but with very low probability—I'm going to find that needle in the haystack. Conversely, if I relax the probability bound, I can have perfect accuracy, as long as I'm allowed to do it a low percentage of the time.

I might be anticipating the Lipschitz condition, but my question is about visualizing that trade-off. I'm presuming it's a nonlinear trade-off of some sort, so I'm wondering if there's anything interesting in the shape of that trade-off.

It's a good question. I've never tried to plot a sample complexity bound, so I don't know that I can say much more. When I see the Lipschitz condition, there's usually some context where the surface is continuous, locally differentiable, and has other interesting properties. I was trying to map that philosophy to what you were showing, but the Lipschitz property is with respect to the function you're learning—the neural network you learn. We're going to look for a function that has the Lipschitz property, which is a little different from the sample complexity function and its smoothness.

The way I like to make this concrete is by thinking about how many functions I have to search through, or how many samples I need. If I take some dataset C with, say, 10 points, and the labels are binary, there are 2^10 possible functions. This is just a general formula to keep in mind. How many functions can my hypothesis class represent from this dataset C to {0,1}? It depends on the VC dimension of your hypothesis space. For a neural network with a large number of parameters, the VC dimension can be high. The question is, doesn't this mean the generalization error bound increases? It does. There's also the question: neural networks overfit, but shouldn't they actually do even worse than we see in practice? It's just something to keep in mind.

I made this slide to tie together two notions. As I add more parameters to my model, the function space I have to search through gets larger, which hurts generalization error. On the other hand, the curse of dimensionality relates to the dimensionality of X. As I increase the number of dimensions, I need more samples to cover the space. How are these ideas related? If I discretize my space X into bins—imagine X is the interval [0,1] on the real numbers, and I chop it into 10 bins: 0 to 0.1, 0.1 to 0.2, and so on—how many samples do I need to construct my dataset C? If it's one-dimensional, I need 10 samples. If I turn that interval into a square, [0,1] x [0,1], I have the product of those two sets of bins, so 10 squared, which is 100. If I turn that into a cube, it's 10 cubed, and so on. Generally, with K bins and dimensionality D, the size of this dataset C, which samples one point in each bin, scales exponentially. If I want to construct a dataset like this, the size of C is exponential in D. Tying this back to the number of functions, for such a dataset, the number of functions is exponential in the dimensionality of the inputs. The takeaway is that the number of functions I have to search through grows in two ways: with the input dimension and the number of parameters. Both tend to hurt the generalization error bound. The main problem tackled in this paper is lowering the generalization error, which is affected by the number of parameters and the dimensionality of the inputs. I wanted to tie them together as part of the same issue with generalization error.

That's all I have on learning theory. Does anyone want to respond or have questions before I get into the actual paper? The space is exponential in two fashions.

Is the total space reduced by priors, or is that a question for another day? I'm going to touch on it right here and tie it back.

You're right. Generally, this is just two to the size of C functions. How do I restrict this? Instead of having to learn every possible function, I don't have to search through every function. Here are some strategies. One idea is to assume that the labeling function or the target f has certain properties. One would be to assume that it's invariant to certain changes in the input. For example, if I'm trying to detect whether there is a dog in my image, and we want translation invariance, it shouldn't matter where the dog is in the image—it can appear anywhere. The labeling function should be invariant to those types of changes. Another idea is that the labeling function has a small Lipschitz constant. The labeling function is really from the input domain to zero or one. If we assume there's a continuous Lipschitz function and then threshold it to get the labels, we can think about the underlying f as having a small Lipschitz constant. That also restricts us from having to learn all possible functions to a smaller set of functions. Another approach is to assume that the labeling function only uses a subset of the features in X, and then we can try to learn functions that respect these properties.

Remember, this will help us decrease the size of the function space we have to search through.

To put a finer point on that, if we go back to the growth function tau, this grows exponentially as long as my hypothesis class shatters C. If I want to slow down the growth function, a couple of things can happen: I can either increase m or decrease the size of my hypothesis class. There's a theorem that shows as soon as you exceed the VC dimension of h, the growth function goes from exponential to polynomial. If you have enough samples, the growth function slows down. Or, if I make the VC dimension smaller, the growth function slows down. This gets back to your point, Kevin—now I don't have to search through exponentially many functions, just polynomially many functions. I want to make one comment. The reason I was going there is that there was a problem in computer graphics, in ray tracing, where you're trying to launch rays and there are a lot of variables: how many samples do you fire for anti-aliasing, for detecting shadows, for depth of field, and there are n dimensions to go across. The critical thing that made ray tracing work so well was the realization that they didn't have to increase the sample size with dimensionality. They simply scattered the samples across all dimensions independently, and that was sufficient to sample the space. This gives a bound, more detail from that finding, that you're able to do something like that and still sample the space. That's what intrigued me—it's something that came up in the 1980s, and the math was too complex for me to understand at the time, but you've presented a nice background for that.

It's a very nice tie-in. As I'm digesting it, I'm thinking: how many samples do I need? Is the question or the problem, how many samples do I need to learn a function that shades properly and represents these different aspects of computer graphics properly? That's essentially it. You have to launch enough samples to simultaneously minimize aliasing and all these other aspects, including distributing samples in time to get motion blur. The worry was that you'd have to use an exponential number of samples because you want to sample each of those dimensions equally. It turned out, after a certain number of samples—maybe it's that cut point where it goes from exponential to polynomial—you just have to launch a sufficient number of samples, and the rest of the error converts into a form of noise that's acceptable. It solved this huge dimensionality problem and made ray tracing practical.

It's a very nice tie-in. I'm trying to relate that to the properties of the target function. There are two ways I could unpack what you're saying, or two guesses I have. One would be that, of all those dimensions—motion blur, shading, and so on—some of these dimensions matter a lot more than others. I can sample some of them heavily, and for others, I don't need that many samples and it doesn't hurt me. Another possibility is that, if they're independent, I don't have to sample all pairs or triples of points in a grid or cube. I just have to sample each dimension n times, and the complexity would be linear in the number of dimensions instead of exponential.

That would make it polynomial, right? But they found it was more or less linear.

It's a good tie-in. I'm glad you brought it up. It's nice when the ideas here feel tangible and relate to a real-world problem.

The other thing discussed in this paper is adversarial examples. I'm not an expert—I'm not even really a beginner in adversarial machine learning. This seems to be a deep field, and the person who notified me of this paper studies adversarial learning. I'm tempted to say this is through the extremely blurry, probably largely wrong lens of generalization error. The rough definition of an adversarial example is that I can apply a small perturbation—for example, the norm of the noise I add has to be small. I perturb the inputs X by a small amount, and it changes the decision rule. Basically, the label that the model outputs changes—from, in binary classification, zero to one, or in multi-class cases, it flips to the wrong answer.

So naively, not knowing anything about adversarial ML, it's part of the generalization error. All of those examples you get wrong—some are due to adversarial examples, cases that look adversarial. Others are not, but you still get them wrong. All other things equal, if I make my model more adversarially robust, theoretically I should decrease my risk.

Another thing to note is that, from what I can tell, adversarial vulnerability is generally observed in really large models with a high VC dimension, and not so much in small models like an SVM. I'm not an expert in this domain, but my naive read is that adversarial vulnerability is a symptom of having a really high VC dimension, so the generalization error has the potential to be pretty high. Hey Ben, I worked in adversarial AI and machine learning, and you characterized it well. That's all correct. Regarding the difference between vulnerability and other kinds of generalization errors, misclassification errors are sometimes not directly eliminated by making the model more robust to adversarial attacks, because those attacks tend to be more obscure. You change pixels in a way that's not noticeable, with a very small epsilon on the pixel value, or you change just a few pixels. There have been examples where a single pixel can change the output.

Those are different in nature than just mistaking a banana for a cap. You don't necessarily get better performance by making it more robust. In practice, with various techniques to make it more robust, you typically lose some classification performance, so there's a trade-off: making it robust, but losing some performance.

Not to derail into adversarial ML, which is mostly speculation for me, but I've heard both takes: that there's a trade-off between performance and adversarial robustness, but in some cases, making it more robust actually increases overall accuracy. It depends on the kinds of errors you make.

Basically, my read is that, relying on theory, the number of functions your hypothesis class contains is extremely large, which means the number of functions that fit the training data well but not the test data is also extremely large. The naive interpretation is that I'm selecting a hypothesis from this space that fits the data, but it's a type of overfitting. I don't know if that rings true, but that would be my naive model of what's going on. There's certainly some amount of overfitting.

Now, let's actually talk about the paper and Lipschitz functions.

Here's the definition of a Lipschitz function. My X and Y both need to be metric spaces. DY is a metric in the Y world, and DX is a metric in the X world. A function is Lipschitz continuous if there's some constant K so that, over the whole domain X, the distance between F of X1 and F of X2 is always bounded by K times the difference in the inputs. Intuitively, the slope is less than or equal to this constant at all times.

They're trying to learn a neural network that has this Lipschitz property because it narrows down the space of functions to choose from. It makes your hypothesis class a lot smaller, which has benefits including possibly reducing generalization error, providing guarantees about adversarial robustness, and maybe making it more interpretable.

A little bit of math. Can I ask one quick question about that slide?

Do we know of problems where we can't guarantee that continuity, or is it always possible to construct solutions that satisfy that property?

No, I think it's the opposite. Generally speaking, this is not satisfied. When you learn a neural network, there are generally no guarantees about Lipschitz continuity, and trying to make it satisfied is a somewhat new line of research. That's my take. Thanks.

By the way, Ben, what do you think makes it discontinuous? Since generally, we're not talking about small K—K could be very large, so if it's not Lipschitz continuous, there's some discontinuity, some gap, some chunk.

How do we get the jump in Y? Why do you think? My intuition is that adversarial examples suggest that functions normally learned are not Lipschitz continuous, because a small change in the inputs flips the label. It could be that it's not actually a big change in the logits of the network, but because it's a one-hot vector and we just choose the best. Do you agree with that? That's right. On the output, since we only choose one correct sample, one correct class, a small change can flip the class. Actually, now that I remember, there are plenty of examples where an adversarial perturbation also causes the logits to change a lot. Instead of being very confident that I'm looking at a dog, the logits can flip to being very confident that I'm looking at a cat. That's a clear example of not being Lipschitz continuous, or it means that K is just really large. In that case, it would be continuous, but K is large. But at some point, if I do the threshold—this is this class—that's where I get the discontinuity. I'm sorry, you were asking why I think it's discontinuous, and I don't necessarily think that for the logits; I'm more thinking that K is large. Okay, good. Thanks.

They just casually mention in this paper that 1-Lipschitz functions are closed under composition. This paper took a long time because I had to stop and convince myself of a bunch of things. That also means I ran out of time and didn't get through every theory in this paper. I've never taken a class on functional analysis, so I wanted to take this opportunity to think through what they mean by this.

This was just my naive reasoning. Here I have two functions, F1 and F2, with Lipschitz constants C1 and C2. This is just the definition of Lipschitz continuity: the left one has constant C1, the right one has constant C2. If we assume the distance metric has the property that, in the limit as X1 minus X2 goes to zero, dividing both sides of the inequality by the distance in the Xs and taking the limit as X1 minus X2 goes to zero, we recover the derivative of the function. I think this would be true for a distance metric like absolute value.

If that's the case, then DDX for this function is less than or equal to C1, and it's less than or equal to C2 for the other function. If I compose the functions, by the chain rule, I get the derivative with respect to X of F2 times the derivative with respect to X of F1, and these are both bounded by C1 and C2. So the composition of Lipschitz functions has a Lipschitz constant equal to the product of the two functions' constants. If anyone is familiar with this, you could check me on this and see if this reasoning is accurate. If this bullet point is correct, then if C1 and C2 are both one, the composition of 1-Lipschitz functions is automatically 1-Lipschitz.

They just mention that in the paper. I didn't get it initially, so I tried to go through and actually get it. The 1-Lipschitz means that's the K. Is it K equal to one? Yes, that's the notation. I used C here; I probably should have used K. In the first line, it says C1. Okay.

When you mention this function that includes whatever non-linearities in the layer, everything above this last bullet point isn't necessarily about a neural network—just functions in general.

It's the bolded one where you're basically saying you're equating an MLP layer to being a function with the same properties you're trying to apply. In the preamble, is that the case—that you consider whatever the non-linearity is, you consider an MLP layer to be a function? Yes, that's exactly right. You nailed it. It's to make the whole function, the whole network, start to finish, 1-Lipschitz. It means the weights in each layer need to be 1-Lipschitz, and the nonlinear activation also has to be 1-Lipschitz, and they tackle both aspects in this paper.

That's exactly it. Now, making the whole network Lipschitz boils down to needing the weights to be Lipschitz and the activations to be Lipschitz.

I'll skip that slide for now and come back to it if necessary. Here's what I understood from the next section in the paper: if the weights W—not the activations, just the weights—are norm-constrained, then I have a Lipschitz function.

The reason is that having the norm constrained is a stronger condition than being Lipschitz. If I have a function that's 1-Lipschitz, that doesn't necessarily mean the slope equals one everywhere; it just means it's less than or equal to one everywhere. The ReLU activation, for example, is definitely Lipschitz almost everywhere. It's not at the single point where you cross zero, but that point has measure zero. Almost everywhere, ReLU is 1-Lipschitz, but on the left side of zero, there's no change, so the derivative is actually zero, and you're less than 1-Lipschitz there—you're zero-Lipschitz on the left side of the real numbers.

If I constrain the norm so that when I multiply by X, the norm of the output Y is constrained to be one, now I'm saying I have to be exactly 1-Lipschitz everywhere. I can never even be less than one. Does that make sense?

Question regarding the definition of Lipschitz: does it mean it has to be one? It says K is one, right? Isn't it the upper limit? Yes, exactly, K is the upper limit. It took me a while to parse this, but I think that's what's going on. That's why ReLU is 1-Lipschitz. If you just look at the left side of the function, between minus infinity and zero, it's zero-Lipschitz on that side, but the whole thing is still 1-Lipschitz, right? Exactly. But if I make the norm so that I multiply X by W and the norm of Y is always fixed to be one, now the slope has to be exactly one everywhere, not just less than one. I'm not quite sure about the definition for ReLU around zero. If I take any delta, if I think about function Y or X, for any delta Y divided by delta X, it's always bounded. It doesn't have a derivative at zero, but it's still Lipschitz because it's always bounded, though the slope is discontinuous. It is, but the question is how exactly it's defined. If the definition is where we're trying to approximate a partial derivative with the finite difference and it's ambiguous at a point, then it's a singularity in that sense. If the function is the derivative itself, but the criteria they were defining there—if you approach from the right-hand side, you have Lipschitz one; from the left-hand side, you're Lipschitz zero. So at that point itself, you have a conundrum.

It's continuous in some sense, but the derivative is not, so what impact that has on Lipschitz continuity is the question.

I think you raised a good point, Haiko. I was thinking it wasn't Lipschitz at that one point, but after looking at the definition, the changes in this and this—if I move this around—it seems like it might still satisfy the upper bound. So it's Lipschitz continuous even though it's not actually differentiable at that point. Differentiability is a stronger condition than Lipschitz continuity.

Back to the idea of making the weights and activations: one stronger condition is that they're norm preserving, gradient norm preserving. But if they're norm preserving, that means the slope is just one all the time, which would make it a linear function. They have a couple theorems about this. If I have a neural network from ℝⁿ to ℝ, and the weights are always 2-norm constrained to be less than or equal to one, then the norm of the gradient is one almost everywhere. Then the whole function F is linear.

It's a bit to unpack, but the general idea is that as I add these constraints—like the norm and the gradient norm—they have to be not just Lipschitz, but actually exactly so. For the gradient, they say it has to be exactly one.

This isn't obvious; they prove a theorem about it. The high-level intuitive view is that these constraints basically take your network and cause the nonlinearity to disappear.

Next, they prove another theorem. We have this network from ℝⁿ to ℝ, built with matrix 2-norm constrained weights, and the gradient is always equal to one. Without changing the actual computation of the neural network, I can replace all of my Ws with some W tilde whose singular values are all equal to one. If the singular values are all equal to one, that means it's stretching and squishing space equally in all directions that W is warping space. In the proof, they show that depending on the dimensions M and K, you either get orthonormal rows or columns, and when they're the same, W is orthogonal.

So the rows are all warping the space in different directions.

I'm not sure I really get what's going on here, but if you blur your eyes a little, it seems like it makes sense.

Now on to activations. The point of these theorems is that instead of searching over W, I can search over W with singular values all equal to one. This helps with searching over Ws. For activation functions, they note that most activation functions like tanh and ReLU are already one-Lipschitz, or if they're not, you can do some scaling to make them one-Lipschitz.

ReLU is Lipschitz, but it's not norm preserving because on the left side of zero, the gradient goes to zero, so it doesn't preserve the gradient norm. The whole function no longer satisfies the gradient norm preservation property. Maybe a question is why they care about norm preservation as opposed to just one-Lipschitz.

My guess is that norm preserving is a stronger condition than one-Lipschitz. But why do we care about it? Because if I'm trying to learn a Lipschitz function, restricting my Ws to norm preserving Ws gives me a smaller space of Ws to search over.

Is that the motivation? Maybe it's just hard to guarantee that the whole function is one-Lipschitz, so you might consider several strategies. The strategy here is to focus on norm preserving Ws. Maybe the concern is that in a deep net, it could collapse to almost zero W, and at another layer, you'd need to blow it up. They probably want to avoid that. This way, if you go deeper, the norm stays the same.

They talk about that later: because the norm is preserved, the gradient norm is preserved. If the gradient norm is preserved, you can stack as many layers as you like and you won't have vanishing or exploding gradients.

This seemed like a conundrum: you're looking for a non-linear activation function that's norm preserving, so the slope is one everywhere, but then it's just linear. Isn't that just a linear function? So what's going on here?

Here's how I interpreted this. This is a nonlinear activation function introduced in the paper. Each cell is a neuron, and they're grouped into clusters of, say, five. In each window, they sort the neurons based on their pre-activations. This isn't intuitive because it seems like you're just sorting, and sorting can be done with a permutation matrix, making the whole thing linear again.

That's where the "almost everywhere" aspect seems to matter. They show they're able to learn functions like absolute value or chopping it up into Ws. The network has one linear function over here and doesn't have to worry about this one point; it can have another linear function over there. Maybe now it's a good time to look at the actual paper.

Let me make my participant a little smaller.

Okay. Running short on time.

They try to provide some intuition for why this is a non-linearity in the appendix. It's interesting, but I'm not sure I fully understand it yet. They show that min max min, when the window size is two, involves looking at two neurons and sorting them. They demonstrate that this is equivalent to applying relu versus minus relu, minus x—a mix of non-linear activation functions. Flipping the x's around can recover relu functions and different variations on relu. They also show it can replicate the absolute value function.

I've looked at this for a while and didn't quite get it. It seems correct, though—they can learn the absolute value, and it can act as an absolute value non-linear activation. Another way to gain intuition is by training the network to learn one-dimensional functions. Instead of a vector, the input is a single number, which helps diagnose what's happening. With a network of just two hidden units, sorting them shows that the two units flip on the left-hand side. With one hidden layer of two units and a one-dimensional input, the output resembles the absolute value function.

A quick observation: because it's zero in one half-space of the inputs, they've split the problem into two half-spaces—one for negative inputs and one for positive inputs.

That minus relu of negative x: if x is negative, it becomes positive, but then you give it a negative value, so it's displaced. Have they basically made a bilateral relu? Is that what's happening here?

Honestly, I wish I knew, Kevin.

You're talking about this equation right here? Yes.

That will admit both positive and negative values of x, right? Yes. Let's walk through it. If x is positive, then x is greater than zero, so x is here and zero is here. X is positive, so this is just x minus x is negative now. This part goes to zero, so that makes sense. If x is negative, relu of a negative number is zero. Now zero is on top and relu of minus. Now I get x here and then apply the minus sign, so I get a negative value. But x was negative in the first place, so it becomes positive. You apply relu to it, and you could say it's x again, right? Yes, exactly.

I don't know if it's the function of the sorting or what, but in this toy example, they've split the problem into two pieces and seem to be dealing with them independently.

I don't think they implemented it this way. I think they're trying to show that swapping and sorting a couple of elements is similar to other non-linear activations.

If you start with x, you go to a space where you have two x, doubling the dimensionality. In the upper one, you're dealing with one half-space of x, and in the other, the other half-space. You've gone from a scalar to a two-vector. In this case, I'm not sure I follow that. You've gone from a two-vector to a two-vector. If you just had x and did ue, you'd get a single value, not a column vector. But here, you're getting two outputs for every one input. I think I see what you're saying. They're trying to show that applying this function to the vector x and zero is the same as applying two non-linear activations to just x. I misunderstood. Sorry. No, that's fine. It's good to pick this apart because it's honestly pretty confusing. I'm still not totally reconciled with the idea that you're applying a permutation matrix as an activation function. The permutation matrix seems interesting. Assume the sort order is constant, but if you're doing a real sort, the permutation matrix will vary depending on the input to get things sorted. So it's not a constant function. Is the idea that it's non-linear because it's a different permutation matrix at every time step? Yes, it's almost like K winners. You're sorting, breaking it into groups, and sorting each one, giving them a canonical order based on rank. If you had a static permutation matrix, you'd be correct, but because it's a sort function, that's not the case. You're using rank statistics on those pieces.

Thanks, Kevin. You could document it as such, but it changes each time you change your input.

I don't think I quite got that until now. I'll have to go back and make sure it really makes sense, but initially, that seems right. Does that seem right to you, Ko? I don't have a good intuition yet about how this sorting works.

We're already over time, so let me try to summarize some results and ideas.

Pretty much every machine learning paper that gets accepted somewhere includes experiments demonstrating that their method works well in some cases. They conduct various experiments on Wasserstein distance, examining the distance between samples generated by GANs and a real dataset, and their method performs well. They're able to learn non-linear functions like absolute value or "W," so they can learn zigzags and similar patterns with this approach. This is interesting, especially regarding the potential for deep learning to address discrete optimization problems, since the non-linear activation is sorting. It seems like you could sort a list using this technique. As you mentioned, Kevin, this relates to ReLU and K-winners, because K-winners involves sorting and adjusting the threshold so that exactly K units are active at any time. The relationship between group sort and K-winners is interesting.

I had never heard of the dynamical isometry property before. Had you? No.

I think dynamical isometry refers to having the weights of the network be norm-preserving, which means the gradients are also norm-preserving. As you take optimization steps, the network continues to preserve norms. Apparently, one paper showed that initializing the network with norm-preserving weights can radically speed up convergence and training. I hadn't heard that until reading the discussion in this paper, and it seems like an interesting thread to explore. As you said, Heco, if the gradient norm is one, you can stack as many layers as you like without vanishing gradients.

They also prove something interesting about being able to approximate arbitrary 1-Lipschitz functions using this method. The math is a bit involved, getting into function spaces and the Weierstrass approximation theorem, which I hadn't looked at until this paper. These are some of the intriguing threads this paper brought up.

Did they show it on more complicated functions, like non-linear functions? They can learn it—let's pull up the paper and look through it.

No, this is just estimating the Wasserstein distance between real data and GAN-generated data. They did MNIST, ImageNet, and CIFAR. I thought so, but I think they buried it in the appendix.

So I have a quick question. We have this conundrum where the slope is one everywhere. In two dimensions, that would be somewhat constraining, but how do you define the slope in multiple dimensions? Do you look at projections? I'm wondering if, by requiring things to be orthonormal, they're sitting on some kind of hypersphere where the local slope is one everywhere. Does it mean that in every dimension it projects to being one? Is that the degree of freedom they're allowing?

Do you have a good intuition for that, Ko? No. That's a good point, Karen.

I don't know at this point. If you look at their condition for initializing the weight to be orthogonal, you've collapsed the dimensionality down, so now you're on a manifold that's orthonormal as opposed to all the other combinations. Maybe it has good properties because you're ensuring each column of your matrix points in a different direction and captures some independent aspect of the input.

For the matrix, if it's square and all values are one, it's like the identity matrix. If they're all one, then it's degenerate.

It's just a rotation.

So you've clearly reduced the dimensionality if that's the case.

But it's not just a rotation if the matrix isn't square, because then the singular values are different from the eigenvalues. The definition of singular in that case requires the pseudo-inverse to make sense of it. I think that's right. Then you get projection and rotation. Something like that.

It's an interesting space to explore if they've found a more principled way of assigning the weights.

What if your weights are sparse? What's the implication then?

You're projecting into a different subspace, maybe. The matrix itself might be singular, depending, but that's not always true. It would be interesting to see if you can add zeros and still preserve the desirable properties. Is there a way to assign zeros and maintain these properties? If you think in terms of square matrices, you have rotations, and to get zeros, you have only certain rotations—like 90-degree rotations. It's almost like projecting into subspaces when you add zeros. Could it also be permutation matrices? Those have eigenvalues of one and can be square.

Did you understand at the end what the Wasserstein distance is about?

No. That's optimal transport. Typically, it's the Wasserstein distance between two probability distributions, and it measures, instead of something like the Kullback-Leibler divergence, the distance between the distributions.

For the Wasserstein distance, it's the amount of transport required to make two distributions overlap as much as possible. Another name for it is the earth mover distance. If you imagine a bulldozer pushing values from one bin to another, it represents how much energy it takes to make one distribution match the other. The nice thing is, compared to Kullback-Leibler divergence, you have a very good distance measure even if the distributions are far apart. You get a nice gradient for the distance measure, whereas for other functions, if they're far apart and the overlap is almost zero, you get very bad gradients. For cases where you need the distance between distributions, the Wasserstein distance is useful for numerical reasons.

Ben, regarding the results, what were the results on the CCI, on the faces? What did they report compared to other methods? I actually didn't look at it. Table five at the very end of the appendix? Yes, on table five.

This is MDE.

Which one is theirs?

It's going to be C. I didn't even talk about this technique in the paper, but the technique they use to make the weights, not the activations, norm-preserving is called the Björck algorithm, which uses an iterative procedure to find the closest orthogonal matrix to a given matrix. They use this to try to find weights, so the last column would be theirs. Everything with Min Max is theirs. That's the comparison. Both of these columns are theirs, and this is the one where they used orthogonal weights as well as Max Min.

These are the test errors. They're comparable with ReLU, slightly worse.

They compare against ResNet. Did they actually use it within a ResNet architecture?

I don't think so. They said they just focused on multilayer perceptrons in this paper. They mention that you can extend it to more complicated architectures. Table six discusses wide ResNets. I'm looking at six, but I'm not sure. What I was wondering is, with avoiding weight decay, do you need the residual layers, or can you just use standard linear layers instead of residual connections?

I'm not sure. Let me check where they mentioned this.

They turn the convolution into the typical form, turning it into a matrix.

I honestly didn't read the results section of this paper that carefully.

It would probably take a few minutes to figure out what the results were, and we're already 20 minutes over. 

Thanks, Ben. Thanks, everyone. I learned a few things from your comments today, so I appreciate the input. Wish you both a nice weekend. See you. Thank you. You too. Likewise.