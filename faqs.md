---
layout: page
title: 🙋 FAQs
description: Answers to frequently asked questions each week.
nav_order: 7
---

# 🙋FAQs

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

Moving forward, we're going to **try** and update this page each week to provide answers to questions asked (1) live in lecture, (2) at [q.dsc40a.com](https://docs.google.com/forms/d/e/1FAIpQLSfEaSAGovXZCk_51_CVI587CcGW1GZH1w4Y50dKDzoLEX3D4w/viewform) during lecture, (3) on Ed, and (4) in the relevant Reflection and Feedback Form. If you have other related questions, feel free to post them on Ed.

Jump to:

- [Weeks 3-5: Regression and Linear Algebra](#weeks3-5-regression-and-linear-algebra)
- [Week 2: Loss Functions, Center and Spread, and Simple Linear Regression](#week-2-loss-functions-center-and-spread-and-simple-linear-regression)

---

## Weeks 3-5: Regression and Linear Algebra

Coming soon...

### Can you recap the proof of the formula for $$w_1^*$$ that includes $$r$$?

Sure!

Given a set of data points $$(x_i, y_i)_{i=1}^n$$, the slope $$w_1^*$$ of the best-fit line in a simple linear regression is given by:

$$
w_1^* = \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2},
$$

where $$\bar{x}$$ and $$\bar{y}$$ are the means of the $x$ and $y$ values, respectively.

Additionally, the Pearson correlation coefficient \(r\) is defined as:

$$
r = \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2 \sum_{i=1}^n (y_i - \bar{y})^2}}.
$$

We want to express $$w_1^*$$ in terms of $$r$$. Rearranging the formula for $$r$$, we have:

$$
r \cdot \sqrt{\sum_{i=1}^n (x_i - \bar{x})^2 \sum_{i=1}^n (y_i - \bar{y})^2} = \sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y}).
$$

To match the original formula for $$w_1^*$$, we need to divide both sides by $$\sum_{i=1}^n (x_i - \bar{x})^2$$:

$$
w_1 = \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = r \cdot \frac{\sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2}}.
$$

Finally, recognizing that the standard deviations of $$x$$ and $$y$$ are:

$$
\text{std}_x = \sqrt{\sum_{i=1}^n (x_i - \bar{x})^2 / (n - 1)}
$$

and

$$
\text{std}_y = \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2 / (n - 1)},
$$

we can conclude that:

$$
w_1^* = r \cdot \frac{\text{std}_y}{\text{std}_x}.
$$

### What do you mean by "the inner dimensions need to match in order to perform matrix multiplication"?

### What's the relationship between spans, projections, and multiple linear regression?

### Why does the design matrix have a column of all 1s?

### What is the projection of $$\vec{y}$$ onto $$\text{span}(\vec{x})$$ – is it $$w^*$$ or $$w^* \vec{x}$$?

### Do the normal equations work even when there is only one column in the matrix $$X$$?

### When do two vectors in $$\mathbb{R}^2$$ span all of $$\mathbb{R}^2$$? When do $$n$$ vectors in $$\mathbb{R}^n$$ span all of $$\mathbb{R}^n$$?

### When $$X^TX$$ isn't invertible, how do we solve the normal equations?

### What does it mean for a matrix to be full rank?

### In multiple linear regression, is $$\vec{h}^*$$ orthogonal to $$\vec{y}$$?

### Why does the multiple linear regression model with two features look like a plane?

### Is there a more detailed version of the MSE proof shown in Lecture 5?

Yes. Here's a proof of the fact that $$R_\text{sq}(w_0^*, w_1^*) = \sigma_y^2 (1 - r^2)$$.

First, note that since $$\sigma_x^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2$$, we have that $$\sum_{i = 1}^n (x_i - \bar{x})^2 = n \sigma_x^2$$. Then:

$$R_{\text{sq}}( w_0^*, w_1^* )$$ = $$\frac{1}{n} \sum_{i=1}^{n} (y_i - \bar{y} - w_1^*(x_i - \bar{x}))^2 $$ \\
= $$ \frac{1}{n} \sum_{i=1}^{n} \left[ (y_i - \bar{y})^2 - 2 w_1^*(x_i - \bar{x})(y_i - \bar{y}) + w_1^{*2} (x_i - \bar{x})^2 \right] $$ \\
= $$ \frac{1}{n} \sum_{i=1}^{n} (y_i - \bar{y})^2 - \frac{2w_1^*}{n} \sum_{i=1}^{n} ((x_i - \bar{x})(y_i - \bar{y})) + \frac{w_1^{*2}}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2 $$ \\
 = $$\sigma_y^2 - \frac{2w_1^*}{n} \sum_{i=1}^{n} ((x_i - \bar{x})(y_i - \bar{y})) + w_1^{*2} \sigma_x^2 $$\\
 = $$\sigma_y^2 - \frac{2w_1^*}{n} \frac{\sum_{i=1}^{n} ((x_i - \bar{x})(y_i - \bar{y}))}{\sum_{i=1}^{n} (x_i - \bar{x})^2} (\sum_{i=1}^{n} (x_i - \bar{x})^2) + r^2 \sigma_y^2 $$\\
 = $$\sigma_y^2 - 2w_1^* \frac{\sum_{i=1}^{n} ((x_i - \bar{x})(y_i - \bar{y}))}{\sum_{i=1}^{n} (x_i - \bar{x})^2} \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n} + r^2 \sigma_y^2$$ \\
= $$\sigma_y^2 - 2w_1^{*2} \sigma_x^2 + r^2 \sigma_y^2 $$ \\
= $$\sigma_y^2 - 2(r^2\frac{\sigma_y^2}{\sigma_x^2}) \sigma_x^2 + r^2 \sigma_y^2 $$\\
= $$\sigma_y^2 - 2r^2\sigma_y^2 + r^2 \sigma_y^2 $$\\
= $$\sigma_y^2 - r^2 \sigma_y^2$$ \\
= $$\sigma_y^2 (1 - r^2)$$


---

## Week 2: Loss Functions, Center and Spread, and Simple Linear Regression

### Isn't the mean affected by outliers? How is it the best prediction?

A prediction is only the "best" relative to some loss function. When using the constant model, $$H(x) = h$$, the mean is the best prediction only if we choose to use the squared loss function, $$L_\text{sq}(y_i, h) = (y_i - h)^2$$. If we choose another loss function, like absolute loss $$L_\text{abs}(y_i, h) = \lvert y_i - h \rvert$$, the mean is no longer the best prediction.

The key idea is that different loss functions lead to different "best" parameters.

### Does empirical risk = mean squared error?

"Empirical risk" is another term for "average loss for whatever loss function you're using." Any loss function $$L(y_i, h)$$ can be used to create an empirical risk function $$R(h)$$. We've seen two common loss function choices:

- When using absolute loss, $$L_\text{abs}(y_i, h) = \lvert y_i - h\rvert$$, the empirical risk, $$R_\text{abs}(y_i, h) = \frac{1}{n} \sum_{i = 1}^n \lvert y_i - h\rvert$$, has a special name: "mean absolute error."
- When using squared loss, $$L_\text{sq}(y_i, h) = (y_i - h)^2$$, the empirical risk, $$R_\text{sq}(y_i, h) = \frac{1}{n} \sum_{i = 1}^n (y_i - h)^2$$, has a special name: "mean squared error."

### What does it mean for a minimizer to be unique?

Let's suppose we're working with the constant model, $$H(x) = h$$.

The minimizer of mean squared error is unique, because the minimizer of mean squared error for the constant model is the mean, and the mean of a collection of numbers $$y_1, y_2, ..., y_n$$ is always just a single number. Specifically, it's the number $$\frac{y_1 + y_2 + ... + y_n}{n}$$.

The minimizer of mean absolute error is not necessarily unique. It's unique when there's an odd number of data points – specifically, if the data points are sorted in order, with $$y_1$$ being the smallest and $$y_n$$ being the largest, then the minimizer of mean absolute error is the median, $$y_{\frac{n+1}{2}}$$. But if there are an even number of data points, then any of the infinitely many numbers on the number line between $$y_{\frac{n}{2}}$$ and $$y_{\frac{n}{2} + 1}$$ minimize mean absolute error, so the minimizer of mean absolute error is not necessarily unique.

For example, in the dataset 72, 90, 61, 85, 92, 75, there are an infinite number of possible predictions that minimize mean absolute error. 75 is one of them, but so is 75.001, 76, 79.913, etc – anything between 75 and 85, inclusive, minimizes mean absolute error.

<center>

<img src="../assets/images/faq2-unique.png">

</center>

### What was the point of plugging in $$h^*$$ into $$R(h)$$?

We spent the first week of class minimizing empirical risk, $$R(h)$$. We found that, depending on our choice of loss function, $$h^*$$ ended up being a different measure of the center of our dataset. The point was to show that the values of $$R(h)$$ actually have some meaning as well, and in particular, the smallest possible value of $$R(h)$$ (which is $$R(h^*)$$) happens to describe the spread of our dataset.

<center>

<img src="../assets/images/faq2-mad.png">

</center>

In the image above, $$h^*$$ is the $$x$$-coordinate of the vertex (80 and 85). We know what 80 and 85 mean – they're the mean and median of the dataset 72, 90, 61, 85, 92, respectively. What we were trying to give context to is what 150 and 9.9 mean – they're the variance and the mean absolute deviation from the median of our dataset. Both the variance and mean absolute deviation from the median are measurements of spread.

### Are there more loss functions outside of what we learned in class?

There are plenty! For example, there's Huber loss, which is like a smoothed version of absolute loss (it's absolute loss, with the corner at the bottom replaced with the bottom of a parabola). There's also cross-entropy loss, also known as "log loss", which is designed for models that predict probabilities (like logistic regression). These, and many more, will come up in future ML classes, like DSC 140A and CSE 158/DSC 148.

### How do I know which loss function to choose in practice?

As we've seen, different loss functions have different properties. At least with regards to the constant model:

<center>

<img src="../assets/images/faq2-pros-cons.png" width="70%">

</center>

In practice, various models have a "default" choice of loss function. Regression usually uses squared loss, not just because squared loss is easily differentiable, but also because squared loss comes with lots of nice theoretical properties (which you'll learn about in DSC 140A, like the fact that implicitly assumes that the distribution of errors is normal/Gaussian). But depending on your model, you can just try different loss functions and see which ends up creating the model with the best performance!

### What was the point of the midrange and infinity loss? Will I actually use that in practice?

I've never heard of anyone using $$\lvert y_i - h\rvert^p$$ with $$p \rightarrow \infty$$ as a loss function in practice, so no. But the point of us studying that was for us to get a better understanding of how different loss functions penalize different kinds of errors, and in particular, how the optimal constant prediction is influenced by outliers.

Again, for the constant model $$H(x) = h$$:

- Absolute loss, $$\lvert y_i - h\rvert$$, isn't sensitive to outliers, it's very robust. Remember, the minimizer (the median) was found by finding the $$h$$ where (# points to the left of $$h$$ = # points to the right of $$h$$).
- Squared loss, $$(y_i - h)^2$$, is more sensitive to outliers. Remember, the minimizer (the mean) was found by finding the $$h$$ where $$-\frac{2}{n} \sum_{i = 1}^n (y_i - h)= 0$$, because $$-\frac{2}{n} \sum_{i = 1}^n (y_i - h)$$ is the derivative of $$R_\text{sq}(h) = \frac{1}{n} \sum_{i = 1}^n (y_i - h)^2$$. Since this is the case, the mean is "pulled" in the direction of the outliers, since it needs to balance the deviations.
- Following the pattern, $$\lvert y_i - h\rvert^3$$ would be even more sensitive to outliers.

As we keep increasing the exponent, $$\lvert y_i - h\rvert^p$$ creates a prediction that's extremely sensitive to outliers, to the point where its goal is to balance the worst case (maximum distance) from any one point. That's where the midrange comes in – it's in the middle of the data, so it's not too far from any one point.

So while no, you won't really use the idea of "infinity loss" in practice, I hope that by deeply understanding how it works, you'll better understand how loss functions (including those we haven't seen in class, but do exist in the real world) work and impact your predictions.

### In Lecture 4, is the $$x_i$$ not part of the summation since it is out of the parentheses?

The question was referring to a summation like this one:

$$\sum_{i = 1}^n (y_i - w_0 - w_1 x_i) x_i$$

Here, $$x_i$$ is indeed a part of the summation. The sum is of $$n$$ terms, each of which are the form $$(y_i - w_0 - w_1 x_i) \cdot x_i$$. That is, the summation above is equivalent to:

$$\sum_{i = 1}^n \left( (y_i - w_0 - w_1 x_i) x_i \right)$$

On the other hand, the following expression is invalid, since $$x_i$$ doesn't have any meaning when not part of a summation over $$i$$:

$$\left( \sum_{i = 1}^n (y_i - w_0 - w_1 x_i) \right) x_i$$

### What was the 3D graph in Lecture 4 about?

<center>

<img src="../assets/images/faq2-surface.png">

</center>

On the left, we have the graph of the mean squared error of a constant prediction, $$h$$, on the dataset 72, 90, 61, 85, 92. It shows us that there is some best $$h$$, which we've been calling $$h^*$$, that makes the mean squared error as small as possible. We showed, using calculus, that the value of $$h^*$$ for any dataset is $$\text{Mean}(y_1, y_2, ..., y_n)$$.

On the right, we have the graph of mean squared error of the line $$H(x) = w_0 + w_1 x$$. The dataset is the dataset of departure times and commute times we've been using as our running example. Specifically:

The two axes on the "ground" of the plot represent different intercepts, $$w_0$$, and slopes, $$w_1$$, that we could be using for making predictions.

The height of the graph above any $$(w_0, w_1)$$ pair is $$\frac{1}{n} \sum_{i = 1}^n (y_i - (w_0 + w_1 x_i))^2$$. $$x_i$$ represents the $$i$$th departure time (e.g. 8.5, corresponding to 8:30AM) and $$y_i$$ represents the $$i$$th actual commute time (e.g. 75 minutes).

The point was to show what the function $$R_\text{sq}(w_0, w_1) = \frac{1}{n} \sum_{i = 1}^n (y_i - (w_0 + w_1 x_i))^2$$ actually looks like, before we went to use calculus to minimize it. It kind of looks like a bowl, and has a clearly defined minimum. Calculus helped us find that minimum, which occurs at $$w_0^* = \bar{y} - w_1^* \bar{x}$$ and $$w_1^* = \frac{\sum_{i = 1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i = 1}^n (x_i - \bar{x})^2}$$.

### Can we minimize the mean absolute error of the simple linear regression model?

Yes, we can! The issue is just that there doesn't exist a closed-form solution, i.e. a formula, for the optimal $$w_0^*$$ and $$w_1^*$$ in:

$$R_\text{abs}(w_0, w_1) = \frac{1}{n} \sum_{i = 1}^n \lvert y_i - (w_0 + w_1 x_i) \rvert$$

So, we have to use the computer to approximate the answer. Regression with squared loss is called "least squares regression," but regression with absolute los is called "least absolute deviations regression." You can learn more here.

### Can you post the slides earlier than 20 minutes before lecture?

I'll try, but I'm making lots of changes to the lectures this quarter, and that usually takes me until right before lecture 😅
