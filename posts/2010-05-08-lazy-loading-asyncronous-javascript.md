---
id: 613
title: Lazy Loading Asyncronous Javascript
date: 2010-05-08T00:15:06
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=613
permalink: /js/lazy-loading-asyncronous-javascript/
btc_comment_counts:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205288890"
btcnew_comment_summary:
  - 'a:4:{i:0;a:3:{s:11:"comment_src";s:4:"blog";s:3:"cnt";s:2:"35";s:7:"enabled";s:1:"0";}i:1;a:3:{s:11:"comment_src";s:10:"friendfeed";s:3:"cnt";s:1:"3";s:7:"enabled";s:1:"1";}i:2;a:3:{s:11:"comment_src";s:7:"twitter";s:3:"cnt";s:1:"1";s:7:"enabled";s:1:"0";}i:3;a:3:{s:11:"comment_src";s:2:"yc";s:3:"cnt";s:1:"3";s:7:"enabled";s:1:"1";}}'
image:
  - ""
embed:
  - This is the default text
seo_follow:
  - 'false'
seo_noindex:
  - 'false'
dsq_needs_sync:
  - "1"
categories:
  - JS
---
**Update:** This is no longer the best way to load scripts. Use a [script tag with async and defer set](https://www.igvita.com/2014/05/20/script-injected-async-scripts-considered-harmful/) instead.

Like many of you might know, I&#8217;m working on a site called [Kundo](http://kundo.se) with a couple of friends. It&#8217;s kinda like a Swedish version of [Getsatisfaction](http://getsatisfaction.com/), which means we have a javascript snippet that people add to their site to get feedback functionality. Cut-and-paste instead of writing the code yourself. Simple.

The problem is, how do you load an external javascript with minimal impact on your customer&#8217;s sites? Here are my requirements:

  1. **Small**. I don&#8217;t want a big mess for them to include on their sites. 10-15 lines, tops.
  2. **Stand-alone**. The environment is unknown, so we can&#8217;t rely on any external dependencies, like javascript libraries.
  3. **Cross-browser**. I have no idea what browsers my customer&#8217;s customers have, so I can&#8217;t do anything modern or fancy that isn&#8217;t backwards compatible. I assume at least IE6 and up though.
  4. **Asynchronous download**. The download of my script should not block the download of any script on their sites.
  5. **Lazy Loading**. If my site is temporarily slow, I don&#8217;t want to block the onload event from triggering until after our site responds.
  6. **Preserve events**. Any events used should not override any events on the customer&#8217;s site. Minimal impact, like I said.
  7. **Don&#8217;t pollute namespace**. Global variables should be avoided, since they could conflict with existing javascript.

Note: I did not make all of this up myself. Lots of people did, I&#8217;m just writing it down for you. Thanks: Jonatan, [Steven](http://stevenbenner.com/), [Peter](http://fleecelabs.se/), and [Linus](http://hanssonlarsson.se/).

## Script tag

```html
<script src="http://yourdomain.com/script.js"></script>
```

While being the stand-alone, cross-browser, and the shortest piece of code possible; it doesn&#8217;t download asynchronously and doesn&#8217;t lazy load. **Fail**.

<div style="overflow: auto;">
  <img class="alignnone size-full wp-image-619" title="Firebug screenshoot with script tag" src="/files/post-media/script11.png" alt="" width="725" height="70" />
</div>

_**Screenshot from Firebug&#8217;s net console:** The script (set to load in 2 seconds) blocks the download of the big image (added after the above script tag, and used throughout this article as a test). Onload event (the red line) triggers after 2.46 seconds._

## Async pattern (A script tag written with javascript)

[Steve Souders](http://stevesouders.com), the web performance guru, has compiled a decision tree over [different ways to achieve non-blocking downloads](http://stevesouders.com/efws/images/0405-load-scripts-decision-tree-04.gif). Have a look at that graph.

Since we&#8217;re on a different domain, and only have one script (order doesn&#8217;t matter), the solution is given: We should create a script tag with inline javascript, and append it to the document. Voila! Non-blocking download!

```javascript
(function() {
    var s = document.createElement('script');
    s.type = 'text/javascript';
    s.async = true;
    s.src = 'http://yourdomain.com/script.js';
    var x = document.getElementsByTagName('script')[0];
    x.parentNode.insertBefore(s, x);
})();
```

**Note**: `async` is a [HTML5 attribute](http://www.whatwg.org/specs/web-apps/current-work/#attr-script-async), doing exactly what we&#8217;re trying to simulate with our hack, so it&#8217;s added for good measure. Also, wrapping the code in an anonymous function prevents any variables to leak out to the rest of the document.

This is a pattern that is getting more and more popular nowadays, especially since [Google Analytics uses it](http://code.google.com/apis/analytics/docs/tracking/asyncTracking.html). But there&#8217;s an important distinction here: The above snipped **blocks onload from triggering** until the referenced script is fully loaded. **Fail**.

**Update 2010-09-01**: [Steve Souders](#comment-34047) adds that the above is only true for Firefox, Chrome, and Safari, but not IE and Opera. So for a IE-only site, this might be the best method.

<div style="overflow: auto;">
  <img class="alignnone size-full wp-image-617" title="Firefox screenshoot with the async pattern" src="/files/post-media/asyncload11.png" alt="" width="726" height="69" />
</div>

_**Screenshot from Firebug&#8217;s net console:** The script (set to load in 2 seconds) downloads in parallell with the big image. Onload event (the red line) triggers after 2.02 seconds._

## Lazy load pattern (Async pattern triggered onload)

So, how to you make sure you don&#8217;t block onload? Well, you wrap your code inside a function that&#8217;s called on load. When the onload event triggers, you know you haven&#8217;t blocked it.

```javascript
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

There&#8217;s been competitions for writing a [short and compact version of addEvent](http://www.quirksmode.org/blog/archives/2005/10/_and_the_winner_1.html), and the winner of that competition was John Resig, with this little beauty:

```javascript
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

Thing is, we don&#8217;t need all that generic event stuff, we&#8217;re only dealing with onload here. So if we first replace the type attribute with hardcoded &#8216;load&#8217;, replace obj with &#8216;window&#8217;, and remove the fix for making &#8216;this&#8217; work in IE, we&#8217;ve got four lines of code left. Let&#8217;s combine this with the above lazy load pattern:

```javascript
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

This is exactly what we&#8217;re looking for here. **Finally!**

<div style="overflow: auto;">
  <img class="alignnone size-full wp-image-618" title="Firebug screenshoot with the lazy load pattern" src="/files/post-media/lazyload11.png" alt="" width="726" height="71" />
</div>

_**Screenshot from Firebug&#8217;s net console:** The script (set to load in 2 seconds) downloads after the onload event has triggered. Onload event (the red line) triggers after 0.41 seconds._

And that wraps up this article: Different tactics works for different scenarios, and only understanding them all makes you capable of picking the right one for your problem. As always, I&#8217;m waiting for your feedback in the comments. Thanks for reading!
