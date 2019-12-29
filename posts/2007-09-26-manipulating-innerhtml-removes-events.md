---
author: Emil Stenström
categories:
- JS
date: 2007-09-26 23:24:04
guid: http://friendlybit.com/js/manipulating-innerhtml-removes-events/
id: 137
permalink: /js/manipulating-innerhtml-removes-events/
title: Manipulating innerHTML removes events
---

Others have written about this before, but I thought I'd mention it again, just so you don't miss it. Aleksandar Vaci? found it while playing with tables and their cells. I found it when [Robert](http://www.robertnyman.com/) and I played with nested lists. It works the same across browers. Let me show a quick example:

You have a paragraph tag that contains a span that you want to make clickable.

```html
<p id="para">
   <span id="clickspan">This is clickable.</span>
   But this is not.
</p>
```

To make it clickable you don't do any fancy stuff, you just add it with onclick:

```js
var span = document.getElementsById("clickspan");
span.onclick = function() {
   alert("You clicked the span!");
}
```

All fine. You click the span and it just works. But then you remember something. You want to add some text to the end of the paragraph, and you decide to do this with javascript. You add the following line to the end of the script:

```js
var p = document.getElementById("para");
p.innerHTML += " Some extra text";
```

You try clicking the span again, and it doesn work. You scratch your hair, you bite your nails, you scream of desperation and anger. It still doesn't work. It seems manipulating an element by using innerHTML removes all events from that element, and all children. Here's a [live example](/files/innerHTMLevents/). I thought you should know.
