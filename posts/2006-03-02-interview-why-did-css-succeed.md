---
id: 48
title: 'Interview: Why did CSS succeed?'
date: 2006-03-02T12:14:22
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/interview-why-did-css-succeed/
permalink: /css/interview-why-did-css-succeed/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205285745"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
When you are looking to reach the upper skill levels of a technique it's always a good idea to start with looking back. The history often says much about the fundamental building blocks and why they work like they do. What were the basic driving forces behind it? What need did it fill? When examining those kinds of questions you can get a far deeper knowledge of what you are working with.

In an attempt to gain some of that knowledge I contacted the authors of [Cascading Style Sheets, level 1](http://www.w3.org/TR/REC-CSS1-961217) (CSS1, notice the nice background image) and asked a few questions about the development on the first CSS specification.

[Håkon Wium Lie](http://people.opera.com/howcome/) promptly answered my questions. He's currently the CTO of Opera, making one of the better browsers out there. This was done by email so don't be surprised if earlier answers reference later ones :) Here's the interview:

**Emil Stenström:**

First I'd like to extend a big thank you from the web development community for coming up with the fantastic idea that is CSS. The language has become a huge success and thousands of people daily exchange ideas of how to best use its power CSS. New people also learn the language each day and big corporations rebuild their sites because of it.

**Håkon Wium Lie:**

Thank you for your kind words. As we'll get back to later in the interview, CSS is the result of many people's ideas and efforts. Without a strong community around CSS, the specification would not have succeeded.

**Emil Stenström:**

1994 when CSS where first proposed there were many different languages available that also made it possible to style web pages. What arguments where there that made people choose CSS instead of any of the others?

**Håkon Wium Lie:**

There were, indeed, a bunch of proposals on the table. First, there were the style sheet languages that had been developed before the web. FOSI, DSSSL, and "P" should be mentioned. Second, there were around ten different style sheet proposals for the web. Several of them were based on earlier languages, but most of them brought new ideas to the table. There was also a healthy interchange of ideas and CSS picked up its shares.

In the end, I think CSS succeeded because it took the web — as opposed to a paper-centric publishing model — seriously. The web introduced some new requirements for style sheet languages, including progressive rendering, screen-based formatting (e.g., pixel units), media-specific style sheets, link styling, and a certain robustness in case one resource (e.g., the style sheet itself) is missing.

It so happens that I'm about to defend my PhD thesis on this subject. So, if you're interested in the history of style sheet languages in the context of the web, I can offer you a few hundred pages to read.

  * <http://people.opera.com/howcome/2006/phd>

**Emil Stenström:**

I can imagine that getting the language from the idea stage to it being accepted by the W3C as a recommendation was anything but a walk in the park. There where surely other authors that wanted their language to succeed instead. How much did work did you put in to promoting the language? Did the features it contain work in promoting the language in itself?

**Håkon Wium Lie:**

Most of the ten proposals I mentioned above were not serious contenders. The one proposal that had the most backing, beside CSS, was DSSSL-Lite. Many people in the SGML camp were upset when W3C (on March 5, 1996) announced that <q>The style sheet efforts will be based on Håkon Lie's Cascading Style Sheets (CSS) initiative, to be further refined by a group of experts within the W3C.</q>

  * <http://www.w3.org/Style/960305_News.html>

One important reason for W3C promoting CSS was support from implementors. Microsoft, amongst others, had committed to implementing CSS at a Style Sheet workshop held in 1995. Compared to DSSSL-Lite, CSS was easier to support since it wasn't Turing-complete and didn't require a transformation step. So, in a way, it was the simplicity — the **lack** of features — that won people over.

The fact that Microsoft haven’t followed up on their promises of supporting CSS and other web standards is very sad. I proposed the Acid2 test to support them along the way:

  * [The Acid2 challenge to Microsoft](http://news.com.com/The+Acid2+challenge+to+Microsoft/2010-1032_3-5618723.html?tag=nefd.ac)
  * <http://www.webstandards.org/acid2>

**Emil Stenström:**

CSS got accepted as a recommendation and browsers started to implement the language. This was the real test to see if the specifications where clear enough. Are there sections or parts of the first specification that you wish that you had written differently or emphasized more?

**Håkon Wium Lie:**

All in all, I'm very happy with how CSS1 has stood the test of time. Compared to many other standards, there are few ugly compromises and not much feature creep. Looking back, I probably would have argued to drop a few features that havn't seen much use (first-letter and first-line), and I would have split a few overloaded properties ('display' and 'white-space' come to mind).
>
I CSS2, I think we should have seen the rise of JavaScript as an opportunity rather than a threat. A 'style sheet object model' should have been built into the thing rather than being an afterthought.

**Emil Stenström:**

Many people shift between thinking about CSS as something written by a few people, perhaps even only the two of you, and it being written by an organization of thousands of people. Which of those are closest to the truth? How many are approximately involved in the writing of a specification (ie. CSS 2)?

**Håkon Wium Lie:**

Lots of people have to be involved. Otherwise, a specification is likely to die a lonely death. In the beginning, however, it's better to be only a few people in order to establish a foundation quickly. For CSS, that happened in the summer of 1995 when Bert Bos and I worked intensely around a white board for a few weeks. He came up with many key ideas, including the forward-compatible parsing.

After that, CSS became a work item of the W3C's HTML working group before getting a working group of its own in 1997. CSS2 came out of that working group. I would estimate that around 10-15 people were actively involved in working out the design of CSS2, while four people are listed as "editors". CSS1 didn't have "editors", it had "authors".

Also, there was a strong community of users on the www-style mailing list that helped us shape the specification, write test suites, and complain in all the right places and do all the other things that are necessary to make a web standard succeed. The real work starts when the specification is finished…

**Emil Stenström:**

Attribute selectors and generated text where available in one of the early browsers, Argo, over 10 years ago. Those features were not included in the first spec but instead moved to CSS 2. Why were they moved and do you have any ideas of why they are still not implemented by some browsers? Do you have any ideas of things we could do to get implementations available faster in the different browsers?

**Håkon Wium Lie:**

Generated content is very cool and it's sad to see that Microsoft's IE7 — coming out 8 years after CSS2 became a Recommendation — will not support it. This is remarkable since Dean Edwards has added support for generated content in his "IE7" project; by adding a link to a JavaScript on our page, IE will happily display CSS2 generated content. So, I believe the decision not to fully support CSS in IE is political rather than technical. Thankfully, there are some other browsers around. May I mention Opera, here?

  * <http://www.opera.com/>

**Emil Stenström:**

Talking more about the future of CSS, there is much work going on with the CSS 3 spec. We will see text shadows, gradients, and multi column layouts, just to name a few. Which new features are to most exciting to you? Is there anything that isn't in the spec yet but will soon be that you want to tell us about?

**Håkon Wium Lie:**

Personally, I'm very exited about the print-related features. Being able to write our book in HTML and style it with CSS was great fun and confirmed our belief in CSS beyond screen use. It required a few features not present in CSS2 and they will be described in CSS3.

  * <http://www.alistapart.com/articles/boom>

Just like I got involved with Opera to ensure that someone implemented CSS correctly, I’m now also involved with Prince to ensure that someone gets CSS printing right.

  * <http://www.princexml.com>

**Emil Stenström:**

Thanks again for taking the time to answer these questions. Perhaps some of my readers will be the ones coming up with the next big thing™.

**Håkon Wium Lie:**

Cheers
