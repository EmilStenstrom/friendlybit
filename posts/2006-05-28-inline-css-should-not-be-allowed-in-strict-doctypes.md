---
id: 65
title: Inline CSS should not be allowed in strict doctypes
date: 2006-05-28T22:48:10
author: Emil Stenström
layout: post
guid: http://friendlybit.com/html/inline-css-should-not-be-allowed-in-strict-doctypes/
permalink: /css/inline-css-should-not-be-allowed-in-strict-doctypes/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205285912"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - HTML
---
<p class="first">
  As many of my readers already know all pages should include a doctype. The doctype tells the browser (or other user agent) what kind of document it can expect and what standards it follows.
</p>

You can divide doctypes into two categories. The first category consist of the _transitional_ ones, the ones that allow old syntax and still validate, and the other one consist of the strict ones. I have repeatedly [recommended the strict versions](http://friendlybit.com/css/cross-browser-strategies-for-css/#mode) for a simple reason: it&#8217;s the best ones for separating design from content.

Just to show an example, transitional allows the following:

<div class="incorrect">
{% highlight html %}
<body bgcolor="blue">
<center>
{% endhighlight %}
</div>

Strict, by its very nature, requires the use of CSS instead.

What I find strange is that _inline CSS_ is valid in strict. Inline CSS is when you use the `style` attribute to set design information inside of the HTML. As an example the two deprecated pieces of code above can be done with:

<div class="incorrect">
{% highlight html %}
<body style="background: blue">
<div style="text-align: center">
{% endhighlight %}
</div>

How is that any better than the transitional versions? Inline CSS goes against all the logic involved in the idea of two distinct doctypes. Why should you want to include design information inside of a document that you just explicitly stated would separate the two?

I hear the obvious reply: &#8220;What if I load design info from a database? I need to use inline CSS then!&#8221;. To me, that sounds like a perfect case where you need to go _transitional_, if you can&#8217;t manage to separate the two &#8211; don&#8217;t.

Strict doctypes are for documents where the webmaster has taken the time to clearly separate the content from the design, not other hybrids.
