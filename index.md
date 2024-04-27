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

[Jump to the current week](#week-4-multiple-linear-regression-br-small-read-a-href-resources-notes-notes-chapter-2-pdf-page-10-note-2-pages-10-19-a-small){: .btn } [Assignment Solutions](https://edstem.org/us/courses/57667/discussion/4730099){: .btn .btn-purple }


{: .green }
> **Take a look at the new [Lecture FAQs](faqs) page on the course website!**

{% for module in site.modules %}
{{ module }}
{% endfor %}
