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

<!-- {: .green }
> **The Midterm Exam is on Tuesday, May 7th during lecture (yes, [campus is back in person tomorrow](https://edstem.org/us/courses/57667/discussion/4920907))! Read the [logistics post on Ed ASAP](https://edstem.org/us/courses/57667/discussion/4898894), and prepare by:**
> - Attempting past exam problems at [**practice.dsc40a.com**](https://practice.dsc40a.com).
> - Reviewing the recently-updated [**FAQs**](faqs) page.
> - Creating your own index card to bring to the exam, using [**our example index card**](https://dsc40a.com/resources/index-card.pdf) as inspiration (if you want).
> - Reviewing the podcast of the review session, linked in Week 5 below.
> - Reviewing [**assignment solutions**](https://edstem.org/us/courses/57667/discussion/4730099).
> - Double-checking your seat assignment in the [**logistics post above**](https://edstem.org/us/courses/57667/discussion/4898894). -->

{: .green }
**Congrats on finishing the Midterm Exam! Homework 5 will be released later this week and will be due on Thursday, May 16th. Most office hours on Wednesday (the day after the Midterm Exam) are cancelled.**

{% for module in site.modules %}
{{ module }}
{% endfor %}
