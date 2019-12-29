---
id: 73
title: 'Reminder: Cross browser font sizes'
date: 2006-06-30T18:15:09
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/reminder-cross-browser-font-sizes/
permalink: /css/reminder-cross-browser-font-sizes/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205766436"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - Fonts
---
I'm sure most of you have already read the [excellent experiment](http://www.thenoodleincident.com/tutorials/box_lesson/font/index.html "Noodleincidents guide on font sizes") on font sizes but it's important enough to summarice here.

The problem is how to make as many browsers as possible display fonts in the same size, without using pixels or other absolute units. Why shouldn't you use fixed font sizes? Because they make Internet Explorer unable to zoom the text with text-zoom, something that's bad for accessibility.

When you start experimenting with this problem you quickly get into problems. I tested in Firefox 1.5, Internet Explorer 6 and Opera 9 and it was incredibly hard (Want a challange? Don't read on, try it by yourself) even with just those few browsers. Opera has problems with units it seems. If you use em:s you can't use more than two decimals, Opera will round it them differently than the others.

Anyway, Owen Briggs solved this for us in a very simple way:

```css
/* Set the size in percent on the body */
body { font-size: 76%; }
/* All other sizes should be in em units with maximum of one decimal */
p { font-size: 1em; }
h1 { font-size: 2em; }
h2 { font-size: 1.8em; }
```

From my simple tests it seems to work fine. Did you know?
