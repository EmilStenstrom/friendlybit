---
author: Emil Stenström
categories:
- CSS
date: 2008-08-07 16:29:24
guid: http://friendlybit.com/css/why-adding-variables-to-css-is-a-good-thing/
id: 171
permalink: /css/why-adding-variables-to-css-is-a-good-thing/
title: Why adding variables to CSS is a good thing
---

Via Simon Willison I find that Bert Bos, one of the creators of CSS, has written an article on why [variables shouldn't be included in CSS3](http://www.w3.org/People/Bos/CSS-variables). I thought I'd try to explain why I think **they should**.

## Professional perspective

Bert posts statistics of stylesheet usage from the W3C site, and means that most stylesheets are very small, and on those, variables are not really needed. I agree. You can get away with simple search-replace in those simple cases. But Bert also finds that there are bigger sheets: "largest hand-written style sheet: 1462 lines (bought from a Web design company)". I work at one of those companies, and almost all CSS files I write exceed 1000 lines.

In those cases, I think CSS variables would help me a lot. Especially for margins. Matching several margins together by copying the same value over and over again isn't maintainable. Search replace on a pixel value is a sure way to mess up your whole stylesheet: who says you only use 5px for those margins? So **there is** a use case for some kind of variables.

## So we need variables, but how?

Bert then suggests that those people should use a solution such as [PHP to generate CSS](http://interfacelab.com/variables-in-css-via-php/). So we should invent a new language for generating CSS with PHP? And another language for generating CSS from Ruby, from Java, from .NET, and so on. Why shouldn't we go this way? It's the path HTML has taken. And this is a hard nut to crack. How is CSS different from HTML? Why should CSS have variables when HTML doesn't?

I think the answer is that we should add variables to both languages. They are very similar in nature, so they should be treated the same. Because what has changed since when CSS was created is that we've started building bigger and more complex sites. And if CSS starts to be too cumbersome to use, people will start looking elsewhere, to Flash, Air, Silverlight and so on. CSS needs to adapt to the more complex sites people are building today.

**I'd rather see CSS follow the times and add variables, than seeing frustrated professionals move to proprietary technologies**.

## So what about beginners?

Bert's article deals a lot with beginners, and how it will be harder for them to understand another level of abstraction. Lets make it clear at first that CSS already is too hard for beginners. To make a very simple layout you need to understand floats (yes, almost everyone needs columns), and floating is really confusing (ever tried to explain float/clear to someone?). Even for someone like me, who has worked with CSS for years, floats still puzzle me regularly.

People will give up on CSS when they encounter floats (yes, I've seen this), not when they find CSS variables. They can just choose not to use variables, while they really need to know floats. Also, CSS variables are easier to understand than cascading values. I mean really, if I set font-size on body, why do my links get larger? That's a very similar concept that is central to CSS.

## Summary

CSS Variables make it easier for professionals to do their job. It doesn't require inventing new template languages. It doesn't make the language overall harder either. The people that can handle floats and cascading, can handle variables too. **We need variables**.
