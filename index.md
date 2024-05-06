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

{: .red }
> **Due to the campus closure for Monday, May 6th, discussion section is cancelled, and all office hours are being held remotely at the following link:**
>
> [Zoom link](https://ucsd.zoom.us/j/96170150611){: .btn .btn-blue }
>
> **A decision has not yet been made about tomorrow's exam – stay tuned.**

{: .green }
> **The Midterm Exam is on Tuesday, May 7th during lecture! Read the [logistics post on Ed ASAP](https://edstem.org/us/courses/57667/discussion/4898894), and prepare by:**
> - Attempting past exam problems at [**practice.dsc40a.com**](https://practice.dsc40a.com).
> - Creating your own index card to bring to the exam, using [**our example index card**](https://dsc40a.com/resources/index-card.pdf) as inspiration (if you want).
> - Reviewing the podcast of the review session, linked in Week 5 below.
> - Reviewing [**assignment solutions**](https://edstem.org/us/courses/57667/discussion/4730099).
> - Double-checking your seat assignment in the [**logistics post above**](https://edstem.org/us/courses/57667/discussion/4898894).

{% for module in site.modules %}
{{ module }}
{% endfor %}
