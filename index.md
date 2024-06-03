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
> Here's what you need to know:
> - **The Final Exam is on Saturday from 8-11AM. You will be assigned a seat, either in Center Hall 212 or 214.**
> - **If at least 90% of the class fills out both the [End-of-Quarter Survey](https://docs.google.com/forms/d/e/1FAIpQLSffswste_zytkO55njB5fLcJWdRbTj1cM7T87zUEhAhTi0-kQ/viewform) and [SETs](https://academicaffairs.ucsd.edu/Modules/Evals/) by 8AM on Saturday, then the entire class will have 2% of extra credit added to their overall grade**.
> - **Homework 8 is due on Thursday, and you can't use slip days on it** (read more [here](https://edstem.org/us/courses/57667/discussion/5011177)).
> - **Homework 4 and 5 scores are released, along with a Grade Report that summarizes your score in the course so far** (read more [here](https://edstem.org/us/courses/57667/discussion/5011263)).
> - **There are two review sessions, on Tuesday and Thursday from 5-7PM in Center Hall 216. The first half of each review session will be a mock exam, where you come and work on problems on paper.**

{% for module in site.modules %}
{{ module }}
{% endfor %}
