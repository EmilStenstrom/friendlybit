---
id: 44
title: Extra fluid layouts with javascript
date: 2006-02-13T01:00:31
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/extra-fluid-layouts-with-javascript/
permalink: /css/extra-fluid-layouts-with-javascript/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205423582"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - JS
---
I'm a big fan of vector graphics. Because of that I love Macromedia Fireworks and the way it handles all elements like vectors. The good thing about that is that they can be resized and zoomed without them losing their sharpness.

This got me thinking about how to add some vectorization to CSS layouts. My idea was that you should let the width of the screen decide the font-size of, for example, your headers. This could make for nice fluid layouts and might even add to usability in some cases. There are probably other uses for this but I leave that to you, please use the comments if you come up with something.

Start by having a look at the [dynamic font-size example](/files/window_fontsize/) just so we're talking about the same thing. Try resizing the window and reloading and see that the headers really do adapt to the width of the browser window.

## How it's done

First we need a way to meassure the width of the text in the default font. For this I use my own little getTextWidth() that were constructed in my [line-break script](/css/line-breaking-with-javascript/). It simply takes a piece of text, attaches it to the page, meassures it's width and removes it again.

```js
function getTextWidth(text) {
   var ea = document.createElement("span");
   ea.innerHTML = text;
   document.body.appendChild(ea);
   var len = ea.offsetWidth;
   document.body.removeChild(ea);
   return len;
}
```

Ok, now we know the width of some text in it's non formated state. Next up is to scale it as much as needed.

```js
function scaleUp(elem, targetWidth) {
   var blockWidth = getTextWidth(elem.innerHTML);
   var defaultSize = parseInt(elem.style.fontSize || '100%')
   var newSize = Math.floor(0.9*targetWidth/(blockWidth/defaultSize))
   elem.style.fontSize = newSize + "%";
}
```

As you see scaleUp() determines a percentage by looking at three things: it's unformated width, it's current width and the target width. Font-size and text width does not seem to follow eachother perfectly so an additional multiplication by 0.9 is needed.

This handy little function is then called with the element you want to scale and the width in pixels of how wide you want it. The calls look something like this:

```js
var element = document.getElementsByTagName("h1")[0];
var width = document.body.offsetWidth;
scaleUp(element, width);
```

That's it, hope you find some fun use for it.

**Update:** After doing some research I see that Eric Meyer is already using something like this in his [slideshow system S5](http://www.meyerweb.com/eric/tools/s5/). Well well, it was a funny exercise none the less.
