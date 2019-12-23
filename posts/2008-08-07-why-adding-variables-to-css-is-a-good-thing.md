---
id: 171
title: Why adding variables to CSS is a good thing
date: 2008-08-07T16:29:24
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=171
permalink: /css/why-adding-variables-to-css-is-a-good-thing/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205287628"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
Via Simon Willison I find that Bert Bos, one of the creators of CSS, has written an article on why [variables shouldn&#8217;t be included in CSS3](http://www.w3.org/People/Bos/CSS-variables). I thought I&#8217;d try to explain why I think **they should**.

## Professional perspective

Bert posts statistics of stylesheet usage from the W3C site, and means that most stylesheets are very small, and on those, variables are not really needed. I agree. You can get away with simple search-replace in those simple cases. But Bert also finds that there are bigger sheets: &#8220;largest hand-written style sheet: 1462 lines (bought from a Web design company)&#8221;. I work at one of those companies, and almost all CSS files I write exceed 1000 lines.

In those cases, I think CSS variables would help me a lot. Especially for margins. Matching several margins together by copying the same value over and over again isn&#8217;t maintainable. Search replace on a pixel value is a sure way to mess up your whole stylesheet: who says you only use 5px for those margins? So **there is** a use case for some kind of variables.

## So we need variables, but how?

Bert then suggests that those people should use a solution such as [PHP to generate CSS](http://interfacelab.com/variables-in-css-via-php/). So we should invent a new language for generating CSS with PHP? And another language for generating CSS from Ruby, from Java, from .NET, and so on. Why shouldn&#8217;t we go this way? It&#8217;s the path HTML has taken. And this is a hard nut to crack. How is CSS different from HTML? Why should CSS have variables when HTML doesn&#8217;t?

I think the answer is that we should add variables to both languages. They are very similar in nature, so they should be treated the same. Because what has changed since when CSS was created is that we&#8217;ve started building bigger and more complex sites. And if CSS starts to be too cumbersome to use, people will start looking elsewhere, to Flash, Air, Silverlight and so on. CSS needs to adapt to the more complex sites people are building today.

**I&#8217;d rather see CSS follow the times and add variables, than seeing frustrated professionals move to proprietary technologies**.

## So what about beginners?

Bert&#8217;s article deals a lot with beginners, and how it will be harder for them to understand another level of abstraction. Lets make it clear at first that CSS already is too hard for beginners. To make a very simple layout you need to understand floats (yes, almost everyone needs columns), and floating is really confusing (ever tried to explain float/clear to someone?). Even for someone like me, who has worked with CSS for years, floats still puzzle me regularly.

People will give up on CSS when they encounter floats (yes, I&#8217;ve seen this), not when they find CSS variables. They can just choose not to use variables, while they really need to know floats. Also, CSS variables are easier to understand than cascading values. I mean really, if I set font-size on body, why do my links get larger? That&#8217;s a very similar concept that is central to CSS.

## Summary

CSS Variables make it easier for professionals to do their job. It doesn&#8217;t require inventing new template languages. It doesn&#8217;t make the language overall harder either. The people that can handle floats and cascading, can handle variables too. **We need variables**.
