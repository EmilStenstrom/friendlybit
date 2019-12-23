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
When you are looking to reach the upper skill levels of a technique it&#8217;s always a good idea to start with looking back. The history often says much about the fundamental building blocks and why they work like they do. What were the basic driving forces behind it? What need did it fill? When examining those kinds of questions you can get a far deeper knowledge of what you are working with.

In an attempt to gain some of that knowledge I contacted the authors of [Cascading Style Sheets, level 1](http://www.w3.org/TR/REC-CSS1-961217) (CSS1, notice the nice background image) and asked a few questions about the development on the first CSS specification.

[Håkon Wium Lie](http://people.opera.com/howcome/) promptly answered my questions. He&#8217;s currently the CTO of Opera, making one of the better browsers out there. This was done by email so don&#8217;t be surprised if earlier answers reference later ones :) Here&#8217;s the interview:

<blockquote class="alternate">

    <strong>Emil Stenström:</strong><br /> First I&#8217;d like to extend a big thank you from the web development community for coming up with the fantastic idea that is CSS. The language has become a huge success and thousands of people daily exchange ideas of how to best use its power CSS. New people also learn the language each day and big corporations rebuild their sites because of it.

</blockquote>

> **Håkon Wium Lie:**

> Thank you for your kind words. As we&#8217;ll get back to later in the interview, CSS is the result of many people&#8217;s ideas and efforts. Without a strong community around CSS, the specification would not have succeeded.

<blockquote class="alternate">

    <strong>Emil Stenström:</strong><br /> 1994 when CSS where first proposed there were many different languages available that also made it possible to style web pages. What arguments where there that made people choose CSS instead of any of the others?

</blockquote>

> **Håkon Wium Lie:**

> There were, indeed, a bunch of proposals on the table. First, there were the style sheet languages that had been developed before the web. FOSI, DSSSL, and &#8220;P&#8221; should be mentioned. Second, there were around ten different style sheet proposals for the web. Several of them were based on earlier languages, but most of them brought new ideas to the table. There was also a healthy interchange of ideas and CSS picked up its shares.
>
> In the end, I think CSS succeeded because it took the web &#8212; as opposed to a paper-centric publishing model &#8212; seriously. The web introduced some new requirements for style sheet languages, including progressive rendering, screen-based formatting (e.g., pixel units), media-specific style sheets, link styling, and a certain robustness in case one resource (e.g., the style sheet itself) is missing.
>
> It so happens that I&#8217;m about to defend my PhD thesis on this subject. So, if you&#8217;re interested in the history of style sheet languages in the context of the web, I can offer you a few hundred pages to read.
>
>   * <http://people.opera.com/howcome/2006/phd>

<blockquote class="alternate">

    <strong>Emil Stenström:</strong><br /> I can imagine that getting the language from the idea stage to it being accepted by the W3C as a recommendation was anything but a walk in the park. There where surely other authors that wanted their language to succeed instead. How much did work did you put in to promoting the language? Did the features it contain work in promoting the language in itself?

</blockquote>

> **Håkon Wium Lie:**

> Most of the ten proposals I mentioned above were not serious contenders. The one proposal that had the most backing, beside CSS, was DSSSL-Lite. Many people in the SGML camp were upset when W3C (on March 5, 1996) announced that <q>The style sheet efforts will be based on Håkon Lie&#8217;s Cascading Style Sheets (CSS) initiative, to be further refined by a group of experts within the W3C.</q>
>
>   * <http://www.w3.org/Style/960305_News.html>
>
> One important reason for W3C promoting CSS was support from implementors. Microsoft, amongst others, had committed to implementing CSS at a Style Sheet workshop held in 1995. Compared to DSSSL-Lite, CSS was easier to support since it wasn&#8217;t Turing-complete and didn&#8217;t require a transformation step. So, in a way, it was the simplicity &#8212; the **lack** of features &#8212; that won people over.
>
> The fact that Microsoft haven’t followed up on their promises of supporting CSS and other web standards is very sad. I proposed the Acid2 test to support them along the way:
>
>   * [The Acid2 challenge to Microsoft](http://news.com.com/The+Acid2+challenge+to+Microsoft/2010-1032_3-5618723.html?tag=nefd.ac)
>   * <http://www.webstandards.org/acid2>

<blockquote class="alternate">

    <strong>Emil Stenström:</strong><br /> CSS got accepted as a recommendation and browsers started to implement the language. This was the real test to see if the specifications where clear enough. Are there sections or parts of the first specification that you wish that you had written differently or emphasized more?

</blockquote>

> **Håkon Wium Lie:**

> All in all, I&#8217;m very happy with how CSS1 has stood the test of time. Compared to many other standards, there are few ugly compromises and not much feature creep. Looking back, I probably would have argued to drop a few features that havn&#8217;t seen much use (first-letter and first-line), and I would have split a few overloaded properties (&#8216;display&#8217; and &#8216;white-space&#8217; come to mind).
>
> I CSS2, I think we should have seen the rise of JavaScript as an opportunity rather than a threat. A &#8216;style sheet object model&#8217; should have been built into the thing rather than being an afterthought.

<blockquote class="alternate">

    <strong>Emil Stenström:</strong><br /> Many people shift between thinking about CSS as something written by a few people, perhaps even only the two of you, and it being written by an organization of thousands of people. Which of those are closest to the truth? How many are approximately involved in the writing of a specification (ie. CSS 2)?

</blockquote>

> **Håkon Wium Lie:**

> Lots of people have to be involved. Otherwise, a specification is likely to die a lonely death. In the beginning, however, it&#8217;s better to be only a few people in order to establish a foundation quickly. For CSS, that happened in the summer of 1995 when Bert Bos and I worked intensely around a white board for a few weeks. He came up with many key ideas, including the forward-compatible parsing.
>
> After that, CSS became a work item of the W3C&#8217;s HTML working group before getting a working group of its own in 1997. CSS2 came out of that working group. I would estimate that around 10-15 people were actively involved in working out the design of CSS2, while four people are listed as &#8220;editors&#8221;. CSS1 didn&#8217;t have &#8220;editors&#8221;, it had &#8220;authors&#8221;.
>
> Also, there was a strong community of users on the www-style mailing list that helped us shape the specification, write test suites, and complain in all the right places and do all the other things that are necessary to make a web standard succeed. The real work starts when the specification is finished&#8230;

<blockquote class="alternate">

    <strong>Emil Stenström:</strong><br /> Attribute selectors and generated text where available in one of the early browsers, Argo, over 10 years ago. Those features were not included in the first spec but instead moved to CSS 2. Why were they moved and do you have any ideas of why they are still not implemented by some browsers? Do you have any ideas of things we could do to get implementations available faster in the different browsers?

</blockquote>

> **Håkon Wium Lie:**

> Generated content is very cool and it&#8217;s sad to see that Microsoft&#8217;s IE7 &#8212; coming out 8 years after CSS2 became a Recommendation &#8212; will not support it. This is remarkable since Dean Edwards has added support for generated content in his &#8220;IE7&#8221; project; by adding a link to a JavaScript on our page, IE will happily display CSS2 generated content. So, I believe the decision not to fully support CSS in IE is political rather than technical. Thankfully, there are some other browsers around. May I mention Opera, here?
>
>   * <http://www.opera.com/>

<blockquote class="alternate">

    <strong>Emil Stenström:</strong><br /> Talking more about the future of CSS, there is much work going on with the CSS 3 spec. We will see text shadows, gradients, and multi column layouts, just to name a few. Which new features are to most exciting to you? Is there anything that isn&#8217;t in the spec yet but will soon be that you want to tell us about?

</blockquote>

> **Håkon Wium Lie:**

> Personally, I&#8217;m very exited about the print-related features. Being able to write our book in HTML and style it with CSS was great fun and confirmed our belief in CSS beyond screen use. It required a few features not present in CSS2 and they will be described in CSS3.
>
>   * <http://www.alistapart.com/articles/boom>
>
> Just like I got involved with Opera to ensure that someone implemented CSS correctly, I’m now also involved with Prince to ensure that someone gets CSS printing right.
>
>   * <http://www.princexml.com>

<blockquote class="alternate">

    <strong>Emil Stenström:</strong><br /> Thanks again for taking the time to answer these questions. Perhaps some of my readers will be the ones coming up with the next big thing &#8482;.

</blockquote>

> **Håkon Wium Lie:**

> Cheers
