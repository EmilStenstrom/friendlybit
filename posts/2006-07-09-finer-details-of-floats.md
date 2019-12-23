---
id: 76
title: Finer details of floats
date: 2006-07-09T15:40:06
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/finer-details-of-floats/
permalink: /css/finer-details-of-floats/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205286100"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
The other day I was working on one of those two column layouts. I quickly got into trouble by something I thought was a bug. It was a bug, but not in the browser(s) I thought. Let&#8217;s go.

A two column layout I said, but this one was a bit different. Each column consisted of a number of boxes, much like a newspaper kind of layout. I wanted the boxes ordered a bit different though: Content editors on the site ordered articles by importance in a single list and when that was transferred to a two column layout I wanted the second most important article to the right of the first article rather than below it. In the HTML source the boxes were ordered like the editors wanted and my job was to make them display in two columns.

![Number 1 to the left, number 2 to the right, number 3 below number 1 to the left, number 4 below number 2 to the right and so on...](/files/textcolumns/textcolumns.png)

&#8220;This can&#8217;t be that difficult&#8221; I thought and floated all odd numbered divs to the left and all even numbered divs to the right. Behold the [huge gap](/files/textcolumns/textcolumns.html) on the left side. I was stumbled. IE displayed it like I thought it worked, Firefox and Opera both displayed the gap (note to self: it&#8217;s seldom a bug if both Fx and Op display it the same).

So, where does the gap come from? I went looking in the [CSS specification on float positioning](http://www.w3.org/TR/CSS21/visuren.html#float-position) and found an interesting list of the rules that govern floats. As with almost all specifications they are not meant to be easy to read, so made a version of them where I use some sample code to explain each of the rules.

This is the sample code you need to have in mind:

```html
HTML:
<div id="parent">
  <div id="child">...</div>
  <div id="child2">...</div>
</div>
```

```css
CSS:
#child { float: left; }
#child2 { float: left; }
```

  1. #child and #child2 must stay to the right of #parent&#8217;s left border.
  2. #child2 must be to the right of #child since #child is earlier in the source. If there is not enough space to the right of #child, #child2 must be moved below #child instead.
  3. If #child2 was floated right and #child and #child2 could not be fitted on the same line, they still must not overlap.
  4. #child and #child2 must stay below #parent&#8217;s top border.
  5. #child2&#8217;s top border may not be higher than #child&#8217;s top.
  6. If #child was display: inline; #child2 must still not be above it.
  7. With #child and #child2 both floated left on the same line, #child2 may not stick out outside of #parent&#8217;s right edge, unless it is already as far to the left as possible.
  8. #child and #child2 must be placed as high as possible
  9. #child and #child2 must be placed as far to the left as possible.

The tricky one here is rule 5. It means that if #child was moved down for some reason, #child2 will have to move down too. Check [the example again](/files/textcolumns/textcolumns.html). See the space above box5 and compare it to the top of box4. Box5 can&#8217;t be above box4 according to rule 5 above. This is clearly what&#8217;s going on here. If we made box2 smaller than box1 there would be a space above it by the same reason.

Note that the list of rules is a prioritized list; rules earlier in the list are more important than the latter ones. To Internet Explorer, rule 8 seems to be more important than rule 5. Strange move by IE.

I hope this gave you an &#8220;Aha!&#8221; feeling, it certainly gave me.
