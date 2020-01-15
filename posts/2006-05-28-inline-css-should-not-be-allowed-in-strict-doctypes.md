---
author: Emil Stenström
categories:
- CSS
- HTML
date: 2006-05-28 22:48:10
guid: http://friendlybit.com/css/inline-css-should-not-be-allowed-in-strict-doctypes/
id: 65
permalink: /css/inline-css-should-not-be-allowed-in-strict-doctypes/
title: Inline CSS should not be allowed in strict doctypes
---

<p class="first">
  As many of my readers already know all pages should include a doctype. The doctype tells the browser (or other user agent) what kind of document it can expect and what standards it follows.
</p>

You can divide doctypes into two categories. The first category consist of the _transitional_ ones, the ones that allow old syntax and still validate, and the other one consist of the strict ones. I have repeatedly [recommended the strict versions](/css/cross-browser-strategies-for-css/#mode) for a simple reason: it's the best ones for separating design from content.

Just to show an example, transitional allows the following:

```html {.incorrect}
<body bgcolor="blue">
<center>
```

Strict, by its very nature, requires the use of CSS instead.

What I find strange is that _inline CSS_ is valid in strict. Inline CSS is when you use the `style` attribute to set design information inside of the HTML. As an example the two deprecated pieces of code above can be done with:

```html {.incorrect}
<body style="background: blue">
<div style="text-align: center">
```

How is that any better than the transitional versions? Inline CSS goes against all the logic involved in the idea of two distinct doctypes. Why should you want to include design information inside of a document that you just explicitly stated would separate the two?

I hear the obvious reply: "What if I load design info from a database? I need to use inline CSS then!". To me, that sounds like a perfect case where you need to go _transitional_, if you can't manage to separate the two - don't.

Strict doctypes are for documents where the webmaster has taken the time to clearly separate the content from the design, not other hybrids.
