---
author: Emil Stenström
categories:
- JS
date: 2010-05-08 00:15:06
guid: http://friendlybit.com/js/lazy-loading-asyncronous-javascript/
id: 613
permalink: /js/lazy-loading-asyncronous-javascript/
title: Lazy Loading Asyncronous Javascript
---

**Update:** This is no longer the best way to load scripts. Use a [script tag with async and defer set](https://www.igvita.com/2014/05/20/script-injected-async-scripts-considered-harmful/) instead.

Like many of you might know, I'm working on a site called [Kundo](http://kundo.se) with a couple of friends. It's kinda like a Swedish version of [Getsatisfaction](http://getsatisfaction.com/), which means we have a javascript snippet that people add to their site to get feedback functionality. Cut-and-paste instead of writing the code yourself. Simple.

The problem is, how do you load an external javascript with minimal impact on your customer's sites? Here are my requirements:

  1. **Small**. I don't want a big mess for them to include on their sites. 10-15 lines, tops.
  2. **Stand-alone**. The environment is unknown, so we can't rely on any external dependencies, like javascript libraries.
  3. **Cross-browser**. I have no idea what browsers my customer's customers have, so I can't do anything modern or fancy that isn't backwards compatible. I assume at least IE6 and up though.
  4. **Asynchronous download**. The download of my script should not block the download of any script on their sites.
  5. **Lazy Loading**. If my site is temporarily slow, I don't want to block the onload event from triggering until after our site responds.
  6. **Preserve events**. Any events used should not override any events on the customer's site. Minimal impact, like I said.
  7. **Don't pollute namespace**. Global variables should be avoided, since they could conflict with existing javascript.

Note: I did not make all of this up myself. Lots of people did, I'm just writing it down for you. Thanks: Jonatan, [Steven](http://stevenbenner.com/), [Peter](http://fleecelabs.se/), and [Linus](http://hanssonlarsson.se/).

## Script tag

```html
<script src="http://yourdomain.com/script.js"></script>
```

While being the stand-alone, cross-browser, and the shortest piece of code possible; it doesn't download asynchronously and doesn't lazy load. **Fail**.

<div style="overflow: auto;">
  <img class="alignnone size-full wp-image-619" title="Firebug screenshoot with script tag" src="/files/post-media/script11.png" alt="" width="725" height="70" />
</div>

_**Screenshot from Firebug's net console:** The script (set to load in 2 seconds) blocks the download of the big image (added after the above script tag, and used throughout this article as a test). Onload event (the red line) triggers after 2.46 seconds._

## Async pattern (A script tag written with javascript)

[Steve Souders](http://stevesouders.com), the web performance guru, has compiled a decision tree over [different ways to achieve non-blocking downloads](http://stevesouders.com/efws/images/0405-load-scripts-decision-tree-04.gif). Have a look at that graph.

Since we're on a different domain, and only have one script (order doesn't matter), the solution is given: We should create a script tag with inline javascript, and append it to the document. Voila! Non-blocking download!

```js
(function() {
    var s = document.createElement('script');
    s.type = 'text/javascript';
    s.async = true;
    s.src = 'http://yourdomain.com/script.js';
    var x = document.getElementsByTagName('script')[0];
    x.parentNode.insertBefore(s, x);
})();
```

**Note**: `async` is a [HTML5 attribute](http://www.whatwg.org/specs/web-apps/current-work/#attr-script-async), doing exactly what we're trying to simulate with our hack, so it's added for good measure. Also, wrapping the code in an anonymous function prevents any variables to leak out to the rest of the document.

This is a pattern that is getting more and more popular nowadays, especially since [Google Analytics uses it](http://code.google.com/apis/analytics/docs/tracking/asyncTracking.html). But there's an important distinction here: The above snipped **blocks onload from triggering** until the referenced script is fully loaded. **Fail**.

**Update 2010-09-01**: [Steve Souders](#comment-34047) adds that the above is only true for Firefox, Chrome, and Safari, but not IE and Opera. So for a IE-only site, this might be the best method.

<div style="overflow: auto;">
  <img class="alignnone size-full wp-image-617" title="Firefox screenshoot with the async pattern" src="/files/post-media/asyncload11.png" alt="" width="726" height="69" />
</div>

_**Screenshot from Firebug's net console:** The script (set to load in 2 seconds) downloads in parallell with the big image. Onload event (the red line) triggers after 2.02 seconds._

## Lazy load pattern (Async pattern triggered onload)

So, how to you make sure you don't block onload? Well, you wrap your code inside a function that's called on load. When the onload event triggers, you know you haven't blocked it.

```js
window.onload = function() {
    var s = document.createElement('script');
    s.type = 'text/javascript';
    s.async = true;
    s.src = 'http://yourdomain.com/script.js';
    var x = document.getElementsByTagName('script')[0];
    x.parentNode.insertBefore(s, x);
}
```

This works, but it overrides the onload event of the site that uses the script. This could be OK in some cases, where you have control over the site referencing the script, but I need to cater for that. **Fail**.

## Unobtrusive lazy load pattern

The logical solution to the above problem is to use an incarnation of addEvent. addEvent is simply a common name for an cross browser way to take the current function tied to onload, add it to a queue, add your function to the queue, and tie the queue to the onload event. So which version of addEvent should we use?

There's been competitions for writing a [short and compact version of addEvent](http://www.quirksmode.org/blog/archives/2005/10/_and_the_winner_1.html), and the winner of that competition was John Resig, with this little beauty:

```js
function addEvent(obj, type, fn)  {
  if (obj.attachEvent) {
    obj['e'+type+fn] = fn;
    obj[type+fn] = function(){obj['e'+type+fn](window.event);}
    obj.attachEvent('on'+type, obj[type+fn]);
  } else
    obj.addEventListener(type, fn, false);
}
```

**Note**: This is unsafe code, since it relies on serializing a function to a string, something that [Opera mobile browsers have disabled](http://my.opera.com/hallvors/blog/2007/03/28/a-problem-with-john-resigs-addevent).

Thing is, we don't need all that generic event stuff, we're only dealing with onload here. So if we first replace the type attribute with hardcoded 'load', replace obj with 'window', and remove the fix for making 'this' work in IE, we've got four lines of code left. Let's combine this with the above lazy load pattern:

```js
(function() {
    function async_load(){
        var s = document.createElement('script');
        s.type = 'text/javascript';
        s.async = true;
        s.src = 'http://yourdomain.com/script.js';
        var x = document.getElementsByTagName('script')[0];
        x.parentNode.insertBefore(s, x);
    }
    if (window.attachEvent)
        window.attachEvent('onload', async_load);
    else
        window.addEventListener('load', async_load, false);
})();
```

This is exactly what we're looking for here. **Finally!**

<div style="overflow: auto;">
  <img class="alignnone size-full wp-image-618" title="Firebug screenshoot with the lazy load pattern" src="/files/post-media/lazyload11.png" alt="" width="726" height="71" />
</div>

_**Screenshot from Firebug's net console:** The script (set to load in 2 seconds) downloads after the onload event has triggered. Onload event (the red line) triggers after 0.41 seconds._

And that wraps up this article: Different tactics works for different scenarios, and only understanding them all makes you capable of picking the right one for your problem. As always, I'm waiting for your feedback in the comments. Thanks for reading!
