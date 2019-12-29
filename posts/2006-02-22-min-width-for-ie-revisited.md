---
id: 47
title: Min-width for IE revisited
date: 2006-02-22T21:41:56
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/min-width-for-ie-revisited/
permalink: /css/min-width-for-ie-revisited/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205285722"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
Much has been written over the years of how to get min-width to work in Internet Explorer (IE). Min-width works almost like width but it only sets a lower bound on the width ("You can't get any narrower than this!"). Very useful when building layouts that are supposed to work on many screen resolutions. This article is a remake of Stu Nicholls variant but removing most of the divs he uses. [An example is availiable](/files/minwidth_for_IE/).

## If all browsers supported standards

The question that triggered this article was someone that wanted the page to be 90% wide but no less than 500px. For those of you that know CSS2 you know that this can be done by simply setting:

```css
#element {
   width: 90%;
   min-width: 500px;
}
```

Since no versions of IE support the min-width property we will have to try something else.

## What has been done before?

To solve this problem there has been suggestions of all sorts of things: [Javascript](http://www.doxdesk.com/software/js/minmax.html), Proprietary CSS expressions, One that doesn't handle both width and min-width, and [One using four (!) extra divs](http://www.webreference.com/programming/min-width/). When looking at the different solutions I quickly came to the conclusion that I didn't want to use javascript. It would be better if it could be accomplished using CSS only. That rules out the two first versions. Dave Shea's does not handle both width and min-width. The last one uses a lot of divs, are really all of them needed?

Stu's solution is set to work in IE 5, an old outdated browser and by removing the code to make it work for that one we will be able to lose some of the code.

IE5 has a broken [box model](http://www.brainjar.com/css/positioning/), so you can't set both margin/border/padding and a width on the same container and get consistent behaviour across browsers. I know of two ways to sidestep that bug: The first one is using the ugly [box model hack](http://www.tantek.com/CSS/Examples/boxmodelhack.html) which incorporates a parsing bug in how IE 5 handles the voice-family property. The other way is to use two containers and set the width on one of them and the margin/border/padding on the other. Stu uses the latter variant and therefore has two unnecessary divs. Two down, and counting!

Next up we can use the `<body>` tag just like if it was a div, setting the width and min-width on that one. Another div bites the dust. If we can handle using a solid background color another one can be left out.

With everything summed up we can get [min-width for IE on any container using only one extra div](/files/minwidth_for_IE/). This works under the constraint that we don't support IE 5 and that we can handle a single color background. I hope that helps someone out there.
