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

{: .green }
> **Welcome to DSC 40A! 👋 Make sure to read the [Syllabus](syllabus), that you can access [Gradescope](https://www.gradescope.com/courses/759109) and [Ed](https://edstem.org/us/join/tFGYBG), and to fill out the [Welcome Survey](https://docs.google.com/forms/d/e/1FAIpQLSftyR__u1hEA39AufRcOZVf5Xu49wDJFokH212XJGhum88wqA/viewform). See you in class!**

{% for module in site.modules %}
{{ module }}
{% endfor %}