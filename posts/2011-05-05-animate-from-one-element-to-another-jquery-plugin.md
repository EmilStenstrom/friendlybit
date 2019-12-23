---
id: 700
title: Animate from one element to another (jQuery plugin)
date: 2011-05-05T22:52:14
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=700
permalink: /js/animate-from-one-element-to-another-jquery-plugin/
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
image:
  - /files/post-media/Stencil_shopping_cart-1024x768.jpg
embed:
  - This is the default text
seo_follow:
  - 'false'
seo_noindex:
  - 'false'
categories:
  - JS
tags:
  - JavaScript
  - JQuery
---
<div class="zemanta-img">
  <figure style="width: 215px" class="wp-caption alignright"><a href="http://commons.wikipedia.org/wiki/File:Stencil_shopping_cart.jpg"><img title="Stencil of a shopping cart with the head of th..." src="/files/post-media/300px-Stencil_shopping_cart31.jpg" alt="Stencil of a shopping cart with the head of th..." width="215" height="162" /></a><figcaption class="wp-caption-text">Image via Wikipedia</figcaption></figure>
</div>

Have you even tried clicking an &#8220;Add to cart&#8221;-button and not understood what happened? I have. An although I understand the idea of adding a product to the cart, and then letting the user continue browsing from where he is, I still get stumped when &#8220;nothing happens&#8221; when I click the button. So what to do?

Simple: Add a **animation from the add button to the cart**. That way you communicate what just happened. &#8220;The product moved in there, and by clicking the cart you&#8217;ll find it again. Now continue buying stuff!&#8221;.

Somebody must have done this before, so I started looking for a <a class="zem_slink" title="JQuery" rel="homepage" href="http://jquery.com/">jQuery</a> plugin to do this (jQuery was already on the page, so why not?). I found add2cart &#8211; A plugin that looks good, but that misses a few features I wanted:

  * The **animation duration** is set in seconds, meaning products further down the page will move faster than those further up. I wanted constant speed.
  * It didn&#8217;t allow me to **customize the look** of the animated element.
  * The code rely on concatenating strings of CSS and generally could use **lots of improvement**.

So I did what anyone would do: rewrote the code from scratch, and posted it on GitHub.

**Get the code: [Animate From To 1.0](https://github.com/EmilStenstrom/jQuery-animate_from_to)**

It&#8217;s my first jQuery plugin ever, and my first public GitHub project, so let me know if I&#8217;ve done something wrong. Is this something that could be useful in one of your projects?
