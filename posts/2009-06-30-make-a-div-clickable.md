---
author: Emil Stenström
categories:
- JS
date: 2009-06-30 22:53:25
guid: http://friendlybit.com/?p=498
id: 498
permalink: /js/make-a-div-clickable/
title: Make a div clickable
---

We all dislike that links are so small, and hard to click. So of course we want to make the clickable areas bigger. Some would think that doing this with some CSS on the a-tag would be a good way, but then you can't have block level elements inside it (you'll get a validation error if you try to put headings or paragraph tags inside of links). So what's a more general solution?

My take is to use a div instead, and use javascript, of course together with a good fallback. When clicking the div, find the first link inside it, and go to that URL. It's simple, and with a few additional quirks, it gets really useful.

Javascript code (requires jQuery):

```js
$(document).ready(function(){
   var block = $(".teaser");
   block.click(function(){
      window.location = $(this).find("a:first").attr("href")
   });
   block.addClass("clickable");
   block.hover(function(){
      window.status = $(this).find("a:first").attr("href")
   }, function(){
      window.status = ""
   })
});
```

CSS for showing that the div actually is clickable:

```css
.clickable {
   cursor: pointer;
}
.clickable:hover {
   background: #efefef;
}
```

A [clickable div demo](/files/clickable_block/) is of course available.

## How it works

  * When the div (or other tag, you choose) is clicked, find the **first anchor tag**, get it's href attribute, and go there. Relying on an actual link means you always have a fallback, so no cheating.
  * When **javascript is disabled**, it just falls back to a regular block, where only the links are clickable.
  * A class called "clickable" is set on the block to allow for **javascript-specific styling**, such as changing the cursor with cursor: pointer, something you don't want to happen when the block isn't clickable.
  * The changing background color on **hover is done with CSS**, which I think is fair, considering the small percentage of users using IE6. Changing background color isn't a must feature.
  * Lastly, since we're simulating a link here, it should show where the link is going. I've done this by setting the statusbar to the link location on hover, something that's useful when it works (users can disable this in some browsers).

Hope that little snippet is useful for someone out there, I think it's a good example of good use of javascript.
