---
id: 161
title: Use formats instead of microformats
date: 2008-05-17T12:29:26
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=161
permalink: /html/use-formats-instead-of-microformats/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205287477"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - HTML
---
The [Semantic Web](http://www.w3.org/2001/sw/) continues to break new ground, and [Web 3.0](http://en.wikipedia.org/wiki/Web_3) seems to be a term that people associate with it. In the backwaters of semantics, microformats aims to develop standards to embed semantic information into XHTML. I can&#8217;t help to think that&#8217;s strange.

One of the [principles of microformats](http://microformats.org/about/) is to &#8220;design for humans first, machines second&#8221;. Still, almost all formats are about adding span tags and class or rel attributes to existing XHTML. Humans will never see those, or benefit from them, unless there&#8217;s some kind of machine parsing done on top. Microformats were first built by people working with the blog search engine [technorati](http://technorati.com/), one of the reasons being to make it easier for technorati to aggregate data from those blogs. So machines it is.

Thing is, if you&#8217;re going to give information to machines, why not use [vCard](http://en.wikipedia.org/wiki/VCard) instead of the equivalent microformat [hCard](http://microformats.org/wiki/hcard)? hCard is just a translation of vCard into XHTML. vCards open in your e-mail program, allowing you to save the contact information there, hCards don&#8217;t open anywhere. vCards are also just as easy (probably easier) to crawl and parse as microformats.

So what I&#8217;m saying is, **could we please use real formats instead of microformats**?

**Update:** This article was too fuzzy, so let me clarify: This discussion is about embedded formats vs. formats. The &#8220;vs.&#8221; come from the fact that lots of sites that implement microformats choose not to implement the corresponding format, which in some cases lead to people not being able to use the extra information.