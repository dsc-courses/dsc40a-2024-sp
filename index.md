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
> - **The Final Exam is on Saturday from 8-11AM. There are several logistical details, which you should read about [here](https://edstem.org/us/courses/57667/discussion/5028163). You will be assigned a seat, either in Center Hall 212 or 214, which you can look up [here](https://docs.google.com/spreadsheets/d/1smu7prCuUpJcGDz1kQnfn7cQ90u9C6M1RgK6IiVHpfw/edit#gid=767657234).**
> - **If at least 90% of the class fills out both the [End-of-Quarter Survey](https://docs.google.com/forms/d/e/1FAIpQLSffswste_zytkO55njB5fLcJWdRbTj1cM7T87zUEhAhTi0-kQ/viewform) and [SETs](https://academicaffairs.ucsd.edu/Modules/Evals/) by 8AM on Saturday, then the entire class will have 2% of extra credit added to their overall grade. We're only around 80% as of now!**
> - **There's a study session on Friday from 4-9PM in HDSI 123.**
> - **We've released a few [review videos](https://edstem.org/us/courses/57667/discussion/5024313) on combinatorics and Naïve Bayes.**
> - **The recordings and solutions from this week's review sessions can be found at the bottom of this page.**

{% for module in site.modules %}
{{ module }}
{% endfor %}
