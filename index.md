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
> **The Midterm Exam is on Tuesday, May 7th during lecture! Read the [logistics post on Ed ASAP](https://edstem.org/us/courses/57667/discussion/4898894), and prepare by:**
> - Coming to the review session TODAY (Friday) in Center Hall 109 from 2-5PM. View the problems we'll take up [**here**](https://edstem.org/us/courses/57667/discussion/4898851). It'll be podcasted if you can't make it.
> - Attempting past exam problems at [**practice.dsc40a.com**](https://practice.dsc40a.com).
> - Creating your own index card to bring to the exam, using [**our example index card**](https://dsc40a.com/resources/index-card.pdf) as inspiration (if you want).

{% for module in site.modules %}
{{ module }}
{% endfor %}
