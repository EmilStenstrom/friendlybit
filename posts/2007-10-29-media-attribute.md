---
id: 136
title: 'Media attribute – what have you done for me lately?'
date: 2007-10-29T00:06:54
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/media-attribute/
permalink: /css/media-attribute/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205287208"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
I've been thinking for a while about the media attribute on link tags. Some people might find that thinking deep thoughts about HTML attributes is kind of strange, but I know you, my dear readers, know the feeling ;)

An example, just so I know we're on the same page:


```html
<link href="style.css" media="handheld"
   rel="stylesheet" type="text/css">
```

This makes sure devices that support the handheld media type (mobile phones?) should load that stylesheet, but no others. It seems simple doesn't it? By using a simple attribute you can style things differently for certain devices. But there's several things to keep in mind, that actually make this attribute a lot less useful.

## Problem number 1: Presentation and content are coupled

One of the big selling points of CSS is the separation of presentation from content. And while I believe that's still a good thing to have, not everyone agrees about it's usefulness. Some time ago Jeff Croft wrote an article about how unusual it is to only change the CSS and not the HTML of a site. While he's mostly making a point of why we should use a certain CSS framework, there's a good point hidden there: Right now it isn't possible to separate things completely.

Designers have of course known this for centuries. They will tell you: you need to adapt the design to the content you're designing. If you're building a site for a shampoo, you might use water and bubbles in your design. If you build a web development blog, you use an image of blueish sky… ehm… Well, you get the point. Good design adapts to the content. They are coupled.

You can't just switch out the content and expect the design to still work. Sure, you can make small adjustments, and make these available as alternate stylesheets, but larger changes just doesn't work. The problem with the media attribute is that it's made for big design changes (switching media), but with no changes in content. How often can you just restyle a word document to get a powerpoint slide? What about converting that slide to something nicely viewable on a mobile phone? That's what the media attribute is there for.

My point is: switching to another media needs much more than just a change in design. You need to change the content to fit that media too. And if you change the content, why not change what stylesheet you link to? This is why I rarely use the "handheld" or "projection" values.

## Problem number 2: Load time

You could think that the browser only loads the one stylesheet that matches the media it's currently showing. Not true. All stylesheets, [no matter what media](http://www.phpied.com/delay-loading-your-print-css/) they are tied to, are loaded at startup.

This means that the more media types you account for, the longer the load time for any of them will be. Very annoying.

## Problem number 3: User agent support

While being able to design for specific user agents might sound like a good idea, the media attribute still requires user agents to support it. If a large part of user agents refuse to apply your style using the media attribute, why not use another method directly? Just to get an idea of how messy support currently is, you can read the [css-discuss summary of the handheld problems](http://css-discuss.incutio.com/?page=HandheldStylesheets):

> "Some current phones apply "screen" styles as well as "handheld" styles, others ignore both, and in some cases the phone carrier runs pages through a proxy that strips styles out even if the phone could recognize them, so it's a crapshoot figuring out what will get applied"

As you see, the value of the media attribute isn't entirely obvious. Sure, you might be able to use it for print with good results, but that's not all it's there for. Right?
