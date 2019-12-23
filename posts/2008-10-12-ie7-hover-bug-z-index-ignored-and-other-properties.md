---
id: 285
title: 'IE7 hover bug: z-index ignored (and other properties)'
date: 2008-10-12T20:17:04
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=285
permalink: /css/ie7-hover-bug-z-index-ignored-and-other-properties/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205287797"
btcnew_comment_counts:
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
I&#8217;m implementing a rather different design right now for an intranet, and have found a bug I thought you&#8217;d like to know about. If you restyle things with :hover, you might have to add an extra property for the rule to be applied in IE7.

How is this design different? Well, it built on columns that are overlapping each other. When you hover one of the columns, that column get placed on top (temporarily). You think you need javascript for this? You don&#8217;t (if you can live with not supporting IE6).

```css
#menu, #content, #sidebar {
   z-index: 1;
}
#menu:hover, #content:hover, #sidebar:hover {
   z-index: 2;
}
```

Simple isn&#8217;t it? Now you just have to absolutely position the three columns. By the way, working with absolute positioning is ok as long as you don&#8217;t need a cleared footer below the three columns. Strange that not more people use this.

Anyway, the above doesn&#8217;t work in IE7. It should, because IE7 supports :hover on all elements, including my &#8220;div columns&#8221;. Some googling led me to an old IE6 bug where some elements are ignored on links. The bug talks about IE6 and the color property being ignored, but the same seems to apply to IE7 and z-index.

So, long story short, just add `display: block` to the hover rule and everything works fine. As the link above dictates, many different rules work, the important thing is that it must be a new rule, which you **haven&#8217;t used before** on that element. But you don&#8217;t set display: block; on divs, do you? So it should work fine.

Hope it helps some frustrated soul out there :) And long live funky designs.
