---
author: Emil Stenström
categories:
- JS
date: 2011-05-05 22:52:14
guid: http://friendlybit.com/?p=700
id: 700
permalink: /js/animate-from-one-element-to-another-jquery-plugin/
title: Animate from one element to another (jQuery plugin)
---

<div class="zemanta-img">
  <figure style="width: 215px" class="wp-caption alignright"><a href="http://commons.wikipedia.org/wiki/File:Stencil_shopping_cart.jpg"><img title="Stencil of a shopping cart with the head of th..." src="/files/post-media/300px-Stencil_shopping_cart31.jpg" alt="Stencil of a shopping cart with the head of th..." width="215" height="162" /></a><figcaption class="wp-caption-text">Image via Wikipedia</figcaption></figure>
</div>

Have you even tried clicking an "Add to cart"-button and not understood what happened? I have. An although I understand the idea of adding a product to the cart, and then letting the user continue browsing from where he is, I still get stumped when "nothing happens" when I click the button. So what to do?

Simple: Add a **animation from the add button to the cart**. That way you communicate what just happened. "The product moved in there, and by clicking the cart you'll find it again. Now continue buying stuff!".

Somebody must have done this before, so I started looking for a <a class="zem_slink" title="JQuery" rel="homepage" href="http://jquery.com/">jQuery</a> plugin to do this (jQuery was already on the page, so why not?). I found add2cart - A plugin that looks good, but that misses a few features I wanted:

  * The **animation duration** is set in seconds, meaning products further down the page will move faster than those further up. I wanted constant speed.
  * It didn't allow me to **customize the look** of the animated element.
  * The code rely on concatenating strings of CSS and generally could use **lots of improvement**.

So I did what anyone would do: rewrote the code from scratch, and posted it on GitHub.

**Get the code: [Animate From To 1.0](https://github.com/EmilStenstrom/jQuery-animate_from_to)**

It's my first jQuery plugin ever, and my first public GitHub project, so let me know if I've done something wrong. Is this something that could be useful in one of your projects?
