---
id: 470
title: 'Projectors: a great accessibility argument'
date: 2009-04-03T17:31:32
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=470
permalink: /accessibility/projectors-a-great-accessibility-argument/
btc_comment_counts:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205288263"
btcnew_comment_summary:
  - 'a:1:{i:0;a:3:{s:11:"comment_src";s:4:"blog";s:3:"cnt";s:1:"8";s:7:"enabled";s:1:"0";}}'
categories:
  - Accessibility
---
So there I sat, at the demonstration of a new website I've been part of building. About 10 people in the room, some of which had never seen the site before. There had been preparations, and we had gone through which parts of the site we were going to present. Only the simple part left…

So the presenter fires up the projector, connects it to his Mac, and looks at the projection. Half the site is outside of the screen. Turns out the maximum resolution is 800×600, and we've designed the site for 1024! People started looking at each other.

> "We have to be able to show the site with a projector!", one from the audience proclaimed.

Awkward silence.

<img class="secondary" src="http://farm1.static.flickr.com/34/110679756_98fdd45346.jpg?v=0" alt="" width="180" height="175" />

I've rarely heard people working with accessibility mention projectors as arguments for accessibility, but it turns out they are great for that purpose. Just look at it like this:

  * **Resolution** is often at the very low end, and they get upgraded much slower than regular computers.
  * **Brightness** is much lower than on a computer screen, especially at daytime, in a room with bad curtains.
  * Many presenters **move their mouse** by looking at the projection, which makes clicking things harder.

Interesting isn't it? Those three just happens to be exactly the same things that we try to optimize when working with accessibility:

  * We try to avoid having people to **scroll sideways**, because unexperienced users find that hard to do. A flexible design, that can adapt to different screen widths (within reason), is a great way to accomplish that.
  * We work hard to make sure that the contrast between page elements is big enough. That way, the large part of the population with low vision (don't forget those that left their glasses at home…), can use the page without problems.
  * We expand clickable areas of links and buttons, to make sure people with motor disabilities can still use our site.

So, we could just as well have been optimizing the "projector experience" all along.

How did the presentation go? Well, we simply zoomed the site out one step, and continued as usual. You are making sure your site zooms properly are you?
