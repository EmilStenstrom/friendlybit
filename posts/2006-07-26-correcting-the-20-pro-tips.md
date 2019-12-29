---
id: 84
title: Correcting the 20 pro tips (.NET magazine)
date: 2006-07-26T05:01:06
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/correcting-the-20-pro-tips/
permalink: /css/correcting-the-20-pro-tips/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205286168"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - HTML
  - Tutorial
---
.NET magazine is a fairly big web development magazine. I've recently been referenced to its articles from many separate places, and often found the articles to be of good quality. The last one, called [20 pro tips](http://www.netmag.co.uk/zine/design-tutorials/20-pro-tips), was not too good though, so I'm going to go through and correct it. I'm not trying to attack the magazine here (remember "friendly" in the URL), I just want people to know these things.

The article consists of 20 points that a pro should know. Here are the points I found errors in:

## Stylesheets: importing vs linking (point 3)

The point is that importing is better than linking since many older browsers will not apply the CSS then. This is correct but they also go as far as suggesting developers to add a separate stylesheet for Netscape 4 (NS4). As someone that has experimented with NS4 I can say that its CSS support is bad. Really bad. Considering the near zero percent of NS4 users I would strongly advise against fixing your site for it. That is of course, unless your site logs suggests you have a lot of users with that (old) browser.

There's also a code error here, simple.css is included twice, and the second @import reference should probably be advanced.css. Not a big error but might confuse someone.

## Smarter gradient backgrounds (point 4)

Again a good point. CSS can be used to repeat background images on any element, not just body. This means you can save on file size by replacing big images with smaller ones. The article then suggests using 1 pixel wide images which is something old versions of IE has problems with. A lot of repetitions can easily get the browser very slow so my best bet would be to make them at least 5 pixels wide.

In the code you would be better off using shorthand notation (I know, this is not a big deal). To add an extra pedagogic twist something else than body could have been used:

```css
form { background: white url(background.png) repeat-x; }
```

## IE Box Model Hack (point 8)

A lot of confusion here. Internet Explorer 5 (IE5) uses another box model than the modern browsers. The padding and border are not added to the outside of a specified width, but instead included in it. This means that if you specify a 500 pixel wide box and add a 10 pixel border to it, it will still be 500 pixels wide. Some say that this is a better way of calculating widths but that's missing the point. The point is that according to the W3C box model the padding should be added _outside_ of the width.

This problem does not appear in Internet Explorer 6 (IE6) if you [include a proper Doctype](/css/cross-browser-strategies-for-css/#mode).

So IE5 is broken, should you care? Again, check your logs if people still use the ancient IE5. My guess is that they don't which saves you a lot of work. There's probably _no need for this hack_.

Also, the [Box model hack](http://tantek.com/CSS/Examples/boxmodelhack.html) is Tantek's hack using the voice-family property to add a "}" to your CSS. It's really ugly. The article uses the same name for another solution to the problem: wrapping the offending element in another element and moving the padding to that box. That's a much cleaner way of fixing the problem.

## Space saver (point 9)

Don't use inline styles for styling. Try to keep all your styles in the external CSS file. Two more general ways of saving space across browsers are outlined in my [cross-browser CSS article](/css/cross-browser-strategies-for-css/#default) (the star-selector and using a premade CSS file that resets browser defaults.

## Format fundamentals (point 11)

Good points about image formats. Use 8-bit PNGs instead of GIF, it makes you smaller files.

An addition: JPEGs are generally smaller than 32-bit PNGs but that's because JPEG removes information in your image to improve compression. Remember that, if you use JPEG.

If you use PNG you need to know that IE has problems showing them in the exact correct color ([technical explanation of the PNG color problem](http://hsivonen.iki.fi/png-gamma/)). If that matters a lot to you, use another format (remember that all PNGs change color in IE, so images still match each other). Friendly Bit uses PNGs only.

## The ‘title’ and ‘alt’ attributes (point 12)

Don't use the title attribute unless it's needed to convey what you mean. In the example it does not make sense at all, why repeat the alt text? The main point is still true though, always use the alt attribute and make good use of the title attribute.

## Wrapping text around images (point 17)

Come on! Using the align attribute is going against what was just recommended, use of semantic markup (point 14). Alignment is style and should be added through CSS, nothing else. Adding a strict Doctype and validating will generate an error on this kind of ugliness. Use `img.typeOfImage { float: left }` instead.

&nbsp;

<p class="first">
  That's it for now, hope you learned something. I just wanted to make sure my readers know more than the .NET readers :)
</p>
