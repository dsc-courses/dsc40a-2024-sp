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

[Jump to the current week](#week-7-probability-br-small-read-a-href-resources-probability-roadmap-janine-s-probability-roadmap-a-and-a-href-http-stat88-org-textbook-content-intro-html-chapters-1-and-2-of-this-probability-textbook-a-small){: .btn } [Assignment Solutions](https://edstem.org/us/courses/57667/discussion/4730099){: .btn .btn-purple }

<!-- {: .green }
> **The Midterm Exam is on Tuesday, May 7th during lecture (yes, [campus is back in person tomorrow](https://edstem.org/us/courses/57667/discussion/4920907))! Read the [logistics post on Ed ASAP](https://edstem.org/us/courses/57667/discussion/4898894), and prepare by:**
> - Attempting past exam problems at [**practice.dsc40a.com**](https://practice.dsc40a.com).
> - Reviewing the recently-updated [**FAQs**](faqs) page.
> - Creating your own index card to bring to the exam, using [**our example index card**](https://dsc40a.com/resources/index-card.pdf) as inspiration (if you want).
> - Reviewing the podcast of the review session, linked in Week 5 below.
> - Reviewing [**assignment solutions**](https://edstem.org/us/courses/57667/discussion/4730099).
> - Double-checking your seat assignment in the [**logistics post above**](https://edstem.org/us/courses/57667/discussion/4898894). -->

{: .green }
**Homework 5 is released and is due on Thursday, May 16th. Midterm Exam scores are available on Gradescope; read [this Ed post](https://edstem.org/us/courses/57667/discussion/4928912) for advice on how to move forward.**

{% for module in site.modules %}
{{ module }}
{% endfor %}
