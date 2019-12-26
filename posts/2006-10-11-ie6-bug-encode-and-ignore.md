---
id: 97
title: 'IE6 bug: Encode and ignore'
date: 2006-10-11T21:12:01
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/ie6-bug-encode-and-ignore/
permalink: /css/ie6-bug-encode-and-ignore/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205286503"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
I&#8217;ve previously talked about [encodings](/other/character-encoding-basics) and tried to explain how they work. This time I&#8217;ll show you a bug in IE6 that is based on encoding problems. Because if you don&#8217;t watch out, IE6 might ignore whole rules in your stylesheet. If you want you can see the example right away: [Ignore encoding example](/files/encode-ignore/). Open in in IE6 and compare with the rendering in a modern browser.

I&#8217;ve never seen this bug mentioned before so I took the liberty of naming it the **&#8220;Encode and Ignore bug&#8221;**. If you find it somewhere else, please tell, and I&#8217;ll use that name instead.

Now. Stylesheets unfortunately have no way of specifying encoding. So you type away in your favourite text editor set to some obfuscate Greek charset and of course expect everything to work. It often does. CSS works with very few characters; mostly you just use the letters A-Z, some brackets, and colons. Since most charsets have those positioned similarly there&#8217;s no problem. But there are exceptions where you want to use other letters too: inside comments and in the future: in generated content.

> **Update**: [Niels Leenheer](http://rakaz.nl/) points out that there are two ways to specify encoding on stylesheets. Either using the method in the [encodings article](/other/character-encoding-basics) to send a proper HTTP header, or using the @charset &#8220;utf-8&#8221;; rule. The latter is just a rule you put on the first line of the CSS. Even seems to have decent browser support. Thanks Niels!

So this Swedish friend of mine is learning CSS and I&#8217;m helping him out when he notices a strange error. When setting his html document to be encoded in utf-8 IE6 starts to display the page differently. I had never seen anything like it and start digging through the code. After like half an hour I find the culprit: an &#8220;å&#8221;-letter in a comment!

What he had done was add a comment after one of the colors he used, /\* ljusblå \*/ (&#8220;light blue&#8221; in Swedish). When IE switches the HTML to UTF-8 the CSS seems to be switched with it. In UTF-8 mode the incorrectly encoded &#8220;å&#8221;-letter means something else, and IE not only ignores the comment or the line, but everything following it (still inside the current rule). So about half of a rule was ignored. I researched further and found that it was only triggered when the strange character was at the end of a comment.

Interesting, and easy to miss. The solution is of course to encode your CSS in the same charset as your HTML, or if you&#8217;re lazy put some characters after the culprit. A very simple (and kinda rare) problem, but I thought it might save you an hour of debugging sometime.
