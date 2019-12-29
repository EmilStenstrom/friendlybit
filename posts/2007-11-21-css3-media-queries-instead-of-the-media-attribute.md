---
id: 141
title: CSS3 Media queries instead of the media attribute
date: 2007-11-21T18:21:50
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/css3-media-queries-instead-of-the-media-attribute/
permalink: /css/css3-media-queries-instead-of-the-media-attribute/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205287300"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
In my previous post about the media attribute I talked about [how strange the media attribute is](/css/media-attribute/), and that its usefulness isn't that obvious.

As a followup I want to point you to an article that Russell Beattie wrote about [CSS3 media queries](http://www.russellbeattie.com/blog/css3-and-the-death-of-handheld-stylesheets). Media queries are a way to **check the capabilities** of a user-agent instead of checking what kind of media type it claims to be. This makes a lot of sense to me. Does it really matter if someone is using a small computer screen or a big mobile phone? What about if they use a [big ass table](http://www.youtube.com/watch?v=CZrr7AZ9nCY)? (aside from the pun, I really think [Microsoft surface](http://www.youtube.com/watch?v=rP5y7yp06n0) is cool)

Checking for capabilities of a certain user-agent makes much more sense: "if available width larger than 200px, show two columns instead of one". If they are dynamically evaluated (I don't know if they are), they allow you to build truly dynamic layouts, that work virtually everywhere. That's what I call accessible layouts.

An interesting parallel is comparing checking user-agent strings and [object detection in javascript](http://developer.apple.com/internet/webcontent/objectdetection.html), and the media attribute and media queries. I believe media queries is the natural next step. Today, the different types of media have started to mix; just look at TV:s and computers, or handheld computers and mobile phones. **The type of media is not as important, capabilities are**.

Although queries do not solve all of the questions I put forward in the previous post, they do pose an interesting alternative. Agreed?

([CSS3 Media queries](http://www.w3.org/TR/css3-mediaqueries/) are as a standard currently a candidate recommendation (which means it's safe to implement), and is currently [supported by Opera 9 and Safari 3](http://www.css3.info/preview/media-queries/).

> **Update**: Opera 9.5 evaluates the queries dynamically, Safari does not, thanks [zcorpan](http://simon.html5.org/))
