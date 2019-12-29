---
id: 115
title: Accessibility as a platform to build upon
date: 2007-02-03T14:00:23
author: Emil Stenström
layout: post
guid: http://friendlybit.com/html/accessibility-as-a-platform-to-build-upon/
permalink: /html/accessibility-as-a-platform-to-build-upon/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205286889"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - Accessibility
  - HTML
---
Two things triggered this post. First a brave participant at the last [Geek Meet](http://www.robertnyman.com/geekmeet/) stood up and asked the question: "Why isn't it ok to require users have javascript enabled?". A few days afterwards I got a lot of good replies to my article about [AJAX vs. Flash](/js/flash-only-vs-ajax-sites/), claiming that users want multimedia, not plain HTML. To me, those are two different ways of asking one fundamental question: "Is it time we start requiring more from our users?".

## HTML: Our history

HTML has existed for (at least) 10 years now. The first browser, Mosaic, supported HTML and the same documents that where viewable then is still possible to look at in today's browsers. You know those polls that are still made to figure out the percentage of users that support javascript or flash? You don't need those for HTML, everyone supports it. Browsers, Mobile phones, Screen readers, Search engines… Everywhere you turn you have HTML support.

Now. HTML does not have everything you need to make a fully working website. So what you do is add another layer that figures out what the users what and generate HTML for them. It's an easy process and the point is that it does not put any pressure on the user at all, even today you can browse most sites with Mosaic. To me, that's fantastic! We truly have an global format for documents that works everywhere.

Semantic code and web standards did not change the basics, we still use the same header elements that where there from the beginning. What was added was a meaning to each element that had gotten lost in the table-era. Suddenly screen readers could just present a list of headers and know that they presented a balanced view of the site.

## But we want more than that!

In parallell to semantic HTML, Flash and AJAX apps have evolved. They do a good job when it comes to interacting with the user, and interfaces instantly feel more alive. Some developers love them for that.

My thesis is that even though we do want more multimedia there's good and bad ways of getting it. Throwing away 10 years of accessibility can't be the best way? What I want is a way to have both a structured and readable site that is accessible from anywhere, **and** a site that can give users more interactivity if their browsers support it. Some say it isn't possible, but as a programmer I know that's not true. Based on previous comments I know it is possible to add a flash layer on top of a HTML site; you simply parse the HTML from flash.

You have probably figured this out already but this is what many AJAX apps are doing. They are adding a more interactive layer, on top of HTML. Done right that has incredible consequences for how applications can be accessed by all sorts of devices.

**Don't believe those who say accessibility rules out everything else. Use accessibility as a platform to build other apps on top of. Only require more for extras, not the basics.**
