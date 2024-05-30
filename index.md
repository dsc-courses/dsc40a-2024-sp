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

[Jump to the current week](#week-9-conditional-independence-na%C3%AFve-bayes-br-small-there-will-not-be-live-lecture-on-tuesday-instead-a-pre-recorded-video-and-annotated-slides-have-already-been-posted-below-along-with-tuesday-s-lecture-read-this-note-on-a-href-conditional-independence-conditional-independence-a-small){: .btn } [Assignment Solutions](https://edstem.org/us/courses/57667/discussion/4730099){: .btn .btn-purple }

{: .green }
> **Note that you can use 2 slip days on Homework 7!**<br>**Also, check out the new [🫂 Advice](advice) page, which contains tips on how to succeed in DSC 40A from current tutors, based on their experiences in the course.**

{% for module in site.modules %}
{{ module }}
{% endfor %}
