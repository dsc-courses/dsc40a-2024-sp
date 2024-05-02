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

[Jump to the current week](#week-5-multiple-linear-regression-feature-engineering-br-small-read-a-href-resources-notes-notes-chapter-1-pdf-page-16-note-1-pages-16-17-a-small){: .btn } [Assignment Solutions](https://edstem.org/us/courses/57667/discussion/4730099){: .btn .btn-purple }


{: .green }
> **The Midterm Exam is on Tuesday, May 7th during lecture! Prepare by attempting past exam problems at [practice.dsc40a.com](https://practice.dsc40a.com).**

{% for module in site.modules %}
{{ module }}
{% endfor %}
