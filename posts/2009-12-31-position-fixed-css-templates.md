---
id: 573
title: 'Position: fixed CSS templates'
date: 2009-12-31T15:14:26
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=573
permalink: /css/position-fixed-css-templates/
btc_comment_counts:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205288844"
btcnew_comment_summary:
  - 'a:1:{i:0;a:3:{s:11:"comment_src";s:4:"blog";s:3:"cnt";s:2:"24";s:7:"enabled";s:1:"0";}}'
categories:
  - CSS
---
In 2006 I wrote an article about [simulating Frames and Iframes](/css/frames-or-iframes-with-css/) and from time to time, I get questions of how to make modifications to the templates presented. But one big thing has changed since 2006: **Perfect support for IE6 is no longer mandatory**.

So yesterday, when Brandon Cobb of [Super Fighter Team](http://superfighter.com/) asked about a design with a fixed header, fixed left column, and scrolling right column, I thought I&#8217;d renew my take on [simulating frames](/css/frames-or-iframes-with-css/) with CSS (The original article is still good for background information, so I still recommend reading it).

## Position: fixed CSS templates

The idea is this: Instead of specifying what parts of the page should scroll, we can **specify what parts should stay fixed when scrolling**. This makes it easier to deal with several fixed parts of the same layout, but also allows us do to things frames cannot do.

So what&#8217;s the trick? Well, `position: fixed` does exactly what we want. It works just like `position: absolute`, but it stays still when the page is scrolled. So it&#8217;s really just a matter of making sure things don&#8217;t overlap.

  * [Demo: Fixed top, fixed left, scrolling right](/files/fixed/fixedtopandleft.html)
  * [Demo: Fixed top, scrolling bottom](/files/fixed/fixedtop.html)
  * [Demo: Fixed left, scrolling right](/files/fixed/fixedleft.html)

**Try resizing the page, and see how the scrolling works**. The templates have been tested in: Fx 3.5, IE8, IE7, IE6 (see note below), Opera 10, Safari 4; all on Windows. Let me know if you can test it on more browsers, or find bugs.

You&#8217;re of course free to use this templates as you see fit, with or without a link back, commercially or not. Consider it public domain.

## Fixes for IE6

As I&#8217;ve said, these designs don&#8217;t act the same in IE6. Instead of some parts being fixed, the whole page scrolls in IE6. The good thing about this is that  **IE6 users won&#8217;t see that your site is &#8220;broken&#8221;**, they will just get another design. And as the number of IE6 users goes towards zero, your design will be more and more consistent :). The fallback is very simple, IE6 gets `position: absolute` instead of fixed, using the [!important hack](http://www.webdevout.net/css-hacks#in_css-important) (you should probably use [conditional comments](http://www.quirksmode.org/css/condcom.html) instead).

Hope these templates are useful for some of you!
