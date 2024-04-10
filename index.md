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

[Jump to the current week](#week-2-simple-linear-regression-br-small-read-a-href-resources-notes-spread-pdf-the-spread-notes-a-and-a-href-resources-notes-notes-chapter-2-pdf-page-1-note-2-pages-1-7-a-small){: .btn } [Assignment Solutions](https://edstem.org/us/courses/57667/discussion/4730099){: .btn .btn-purple }

<!-- Click the 🎥 button to view the recording of a lecture/discussion.<br>Click the 📝 button to view lecture notebooks after they've been filled in during lecture. -->

{: .green }
> **Welcome to DSC 40A! 👋 Make sure to read the [Syllabus](syllabus), that you can access [Gradescope](https://www.gradescope.com/courses/759109) and [Ed](https://edstem.org/us/join/tFGYBG), and to fill out the [Welcome Survey](https://docs.google.com/forms/d/e/1FAIpQLSftyR__u1hEA39AufRcOZVf5Xu49wDJFokH212XJGhum88wqA/viewform). See you in class!**

{% for module in site.modules %}
{{ module }}
{% endfor %}