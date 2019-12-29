---
author: Emil Stenström
categories:
- CSS
date: 2006-09-04 22:08:49
guid: http://friendlybit.com/css/ie6-resize-bug/
id: 91
permalink: /css/ie6-resize-bug/
title: 'IE6 resize bug (position: relative becomes fixed)'
---

One bug kept popping up on the sites I built, and I was almost going insane. The bug I'm talking about is specific to Internet Explorer 6 (IE6) and has to do with what happens when you resize the page. Here's an [example page showing the bug](/files/ie6resizebug/). Open it in IE6 and try resizing the window. Let me explain:

> **Update**: [Paula comments](/css/ie6-resize-bug/#comment-4551) that IE7 beta 2 has the same problem. Thanks Paula.

## Setting up the IE6 resize bug

To see the bug in action you need two things: You need to center your page using the body element and you need to be using a fixed width (not percent) on the element. If you use this you will quickly notice that all elements you set `position: relative` on, will stay fixed on the page when you resize the window. They behave as if you just set position: fixed on them, but only until you reload. It's really a fun effect (if you know the fix).

Example code:

```css
body {
   margin: 0 auto;
   width: 760px; /* Any fixed or fluid width */
}
/* Affects all elements with position: relative; */
#example p {
   position: relative;
}
```

Here's a live example of the [IE6 resize bug](/files/ie6resizebug/) with borders added for clarity.

The bug is kinda rare you could say. But using body for centering is a great way of getting rid of one extra container div, so I have been using it more and more lately (IE5 can't handle that, but you don't support it do you?). Anyway, not being able to use `position: relative` is not ok.

## Making things behave as normal again

Fortunately the fix is very easy. You simply add **position: relative to the body element**. \*Blam\* All previous broken elements start behaving like expected again. Here's the same [example with the bug fixed](/files/ie6resizebug/fixed.html).

That's a couple of hours less IE6 adoption time on my next project. I hope it helps someone out there too.
