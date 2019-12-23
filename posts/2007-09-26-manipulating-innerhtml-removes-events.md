---
id: 137
title: Manipulating innerHTML removes events
date: 2007-09-26T23:24:04
author: Emil Stenström
layout: post
guid: http://friendlybit.com/js/manipulating-innerhtml-removes-events/
permalink: /js/manipulating-innerhtml-removes-events/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205287231"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - JS
---
Others have written about this before, but I thought I&#8217;d mention it again, just so you don&#8217;t miss it. Aleksandar Vaci? found it while playing with tables and their cells. I found it when [Robert](http://www.robertnyman.com/) and I played with nested lists. It works the same across browers. Let me show a quick example:

You have a paragraph tag that contains a span that you want to make clickable.

```html
<p id="para">
   <span id="clickspan">This is clickable.</span>
   But this is not.
</p>
```

To make it clickable you don&#8217;t do any fancy stuff, you just add it with onclick:

```javascript
var span = document.getElementsById("clickspan");
span.onclick = function() {
   alert("You clicked the span!");
}
```

All fine. You click the span and it just works. But then you remember something. You want to add some text to the end of the paragraph, and you decide to do this with javascript. You add the following line to the end of the script:

```javascript
var p = document.getElementById("para");
p.innerHTML += " Some extra text";
```

You try clicking the span again, and it doesn work. You scratch your hair, you bite your nails, you scream of desperation and anger. It still doesn&#8217;t work. It seems manipulating an element by using innerHTML removes all events from that element, and all children. Here&#8217;s a [live example](/files/innerHTMLevents/). I thought you should know.
