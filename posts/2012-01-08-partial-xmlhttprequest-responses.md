---
id: 839
title: Partial XMLHttpRequest responses?
date: 2012-01-08T15:28:49
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=839
permalink: /js/partial-xmlhttprequest-responses/
btcnew_comment_counts:
  - 'a:0:{}'
categories:
  - JS
  - Modern web
---
We all know how to make an AJAX request, and fetch some data. But as soon as you need to fetch data incrementally, have the server push data to you, you have to resort to all sorts of complicated stuff. Websockets; with all their different versions and shady support, different kinds of polling, hidden iframes, ActiveX for IE?

The simplest way, that almost workds is partial XMLHttpRequest responses. I first read about them as [progressive xmlhttprequests on Kyle Schulz blog](http://www.kylescholz.com/blog/2010/01/progressive_xmlhttprequest_1.html), but really think that method should get more recognition.

Note: I&#8217;ve only tested this with Webkit, against Twitter&#8217;s Streaming API, with a XMLHttpRequest that allows cross-domain requests. I think it works with Firefox too, but it will definitely not work in IE. Sorry.

```js
var xhr = new XMLHttpRequest();
var url = "<streaming-url-on-you-own-domain-or-CORS>";
xhr.open("GET", url, true);
xhr.send();
// Define a method to parse the partial response chunk by chunk
var last_index = 0;
function parse() {
    var curr_index = xhr.responseText.length;
    if (last_index == curr_index) return; // No new data
    var s = xhr.responseText.substring(last_index, curr_index);
    last_index = curr_index;
    console.log(s);
}
// Check for new content every 5 seconds
var interval = setInterval(parse, 5000);
// Abort after 25 seconds
setTimeout(function() {
    clearInterval(interval);
    parse();
    xhr.abort();
}, 25000);
```

The biggest problem with this method is that the responseText property keeps filling up with data. The longer you receive data, the bigger the data in memory will be. The only way I can see this fixed (today) is to simply kill the connection after a certain amount of data has been received, and open it up again.

**I would love to see a better way to do this**, from native javascript, without all the numerous hacks that are out there. If you know of a way that fills these requirements, please let me know:

  1. Easy to implement on the **client side**. Ideally I would like to use XMLHttpRequest, and just get a callback each time the client sends data, with the NEW data specified as a callback parameter.
  2. Easy to implement on the **server-side**. I can set some headers if you make me, but ideally I would like to use this against existing Streaming APIs (like Twitter&#8217;s), without adding custom stuff.
  3. As cross-browser, cross-platform as possible.

Is there a way to get this working? It&#8217;s so annoying to see something that&#8217;s a curl one-liner, be 100s of lines of code with web technologies&#8230;

```bash
curl https://stream.twitter.com/1/statuses/filter.json?track=<your-keyword> -u <your-twitter-nick>
```

**Is the web really that far behind?**
