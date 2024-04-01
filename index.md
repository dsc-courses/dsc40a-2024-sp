---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}

{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

[Jump to the current week](#week-1-modeling-and-loss-functions){: .btn }

<!-- Click the 🎥 button to view the recording of a lecture/discussion.<br>Click the 📝 button to view lecture notebooks after they've been filled in during lecture. -->

{: .red }
> **Welcome to DSC 40A! 👋 This site is still under construction, and everything here is subject to change. But, for now:**
> - There is no discussion this Monday 4/1; the first class meeting will be lecture on Tuesday 4/2. You can attend either section.
> - Make sure that you can access [**Gradescope**](https://www.gradescope.com/courses/759109/) and [**Ed**](https://edstem.org/us/courses/57667/discussion/4667406). [**Here**](https://edstem.org/us/join/tFGYBG) is the Ed join link if you weren't already added.
> - Please fill out the [**Welcome Survey**](https://docs.google.com/forms/d/e/1FAIpQLSftyR__u1hEA39AufRcOZVf5Xu49wDJFokH212XJGhum88wqA/viewform).
> 
> See you on Tuesday in Center Hall 212!

{% for module in site.modules %}
{{ module }}
{% endfor %}