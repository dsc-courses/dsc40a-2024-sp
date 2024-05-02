---
layout: page
title: 🧮 Lecture 10 Animations
description: Animations for Lecture 10.
nav_exclude: true
---

# 🧮 Lecture 10 Animations

To start an animation, first click the "⏯️ Stop animation" button and then click the "▶️ Start animation" button.

---

### Derivatives and Tangent Lines

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

**Key ideas**:

- $$\frac{df}{dt}(t)$$ is the <span style="color:red">slope of the tangent line</span> to $$f$$ at the point $$(t, f(t))$$.
- When the <span style="color:red">slope of the tangent line</span> is negative, increasing $$t$$ brings you closer to a minimum.
- When the <span style="color:red">slope of the tangent line</span> is positive, increasing $$t$$ brings you further away from a minimum.
- The closer $$t$$ is to a minimum, the shallower the <span style="color:red">slope of the tangent line</span> is – at a minimum, the <span style="color:red">slope of the tangent line</span> is 0!

<center>

<iframe src="slopes_changing.html" frameBorder=0 width=800 height=700></iframe>

</center>

---

### Gradient Descent

**Key idea**: Depending on (1) the nature of $$f$$, (2) the initial guess, and (3) the learning rate, gradient descent may or may not converge to a global minimum!

<center>

<iframe src="grad_desc_0_001.html" frameBorder=0 width=800 height=700></iframe>

</center>

<center>

<iframe src="grad_desc_11_001.html" frameBorder=0 width=800 height=700></iframe>

</center>

<center>

<iframe src="grad_desc_0_01.html" frameBorder=0 width=800 height=700></iframe>

</center>