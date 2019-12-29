---
id: 37
title: Line Breaking With Javascript
date: 2006-01-22T00:00:00
author: Emil Stenström
layout: post
guid: http://friendlybit.com/js/line-breaking-with-javascript/
permalink: /js/line-breaking-with-javascript/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205285611"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - JS
  - CSS
  - HTML
---
Over the years there have been numerous suggestions of different ways of doing line breaks on the web. Browser incompatibilities, lack of support for standardized features, and the creation of browser specific features all helps in making it incredibly difficult. Searching and reading for a while quickly brought me to think the best current solution is [quirksmode's wbr](http://www.quirksmode.org/blog/archives/2005/06/quirks_mode_and_1.html). It seems quite well supported but has two major flaws:

  1. `<wbr>` is not valid HTML
  2. The suggested solution does not work in Safari

So off I went to find a better one. I started trying some different combinations of spaces marked up with `<span>` tags and I tried some nifty CSS tricks before it hit me - this should be done with javascript. Javascript has wide browser support and after some research (and help from the people in EFNet #javascript) I actually got a [working example](/files/js-linebreak/) up. I have been able to test it in FF 1.5/Win, IE 5.5/Win, IE 6/Win, Opera 8.51/Win+Mac, and Safari 2.0.3/Mac and everything seems to work fine in all of them.

## How it works

The idea here is to add ordinary `<br>`s and using javascript to measure the length of the text. The user gives a piece of text and a width in pixels and the script returns the text with breaks inserted.

The hard part is to find at which letter we should break. My first idea was to just loop over the text and keep track of the width in pixels. When we get over the given width, back one step and add a break at that position. But this will be slow for small font-sizes and wide columns so let's do something faster. Instead of looping through all letters we can use [Binary Search](http://en.wikipedia.org/wiki/Binary_search) (check the link if you're not familiar with it, it's good to know). This makes for a lot less calls.

We need a small change to the algorithm since we won't be able to find the exact width we're looking for (a letter is wider than 1px). Instead we break when we're down to knowing that it's between two letters. We then return the first letter's position. Here is code:

```js
function binSearch(text, searchLen) {
   var left = 0, right = text.length;
   var breakPos = left, lastBreakPos = right;
   while (Math.abs(lastBreakPos - breakPos) > 1) {
      lastBreakPos = breakPos;
      breakPos = Math.floor((left+right)/2);
      if (searchLen  getTextWidth(text.substring(0, breakPos)))
         right = breakPos - 1;
      else
         left = breakPos + 1;
   }
   return Math.min(breakPos, lastBreakPos);
}
```

The code above uses `getTextWidth()` to get the width of a piece of text. `getTextWidth()` makes use of the `offsetWidth` property to get the width of a piece of text. Problem is that only elements that are rendered have the property set. This means we need to add it to the page, measure it, and then remove it. This code does just that:

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

Good. We now have two nice helper functions to handle all the hard work. Now we only need some code to actually split the text and add the breaks. We do this by using `binSearch()` to fetch where the next break should be. `binSearch()` returns an index and we split the line and add the first part (including a break) to a buffer. We then repeat the same procedure on the last part of the string. We keep splitting until `getTextWidth()` tells us we're done.

```js
function linebreak(text, maxLen) {
   var breakPos = 0;
   var out = "";
   var part1 = text, part2 = "";
   if (getTextWidth(part1) > maxLen) {
      while (getTextWidth(part1) > maxLen) {
         var breakPos = binSearch(part1, maxLen);
         part2 = part1.substring(breakPos, part1.length);
         part1 = part1.substring(0, breakPos);
         out += part1 + "";
         part1 = part2;
      }
      return out + part2;
   }
   else
      return text;
}
```

It's now time to use the function we have. The first line selects what elements we want to wrap. You can replace this with a loop if you want if you need to go over all the paragraphs in your document. The second line just fetches everything inside the paragraph and sends it to `linebreak()` for wrapping. The two lines are then made to trigger when the document is ready loading.

```js
window.onload = function () {
   var e = document.getElementsByTagName("p")[0];
   e.innerHTML = linebreak(e.innerHTML, 200);
}
```

A [working example](/files/js-linebreak/) is available that shows what it can do. So, what do you think? Could this be the best solution so far to handling line breaks?
