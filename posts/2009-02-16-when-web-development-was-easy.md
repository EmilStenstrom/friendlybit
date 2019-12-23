---
id: 438
title: 'When web development was easy…'
date: 2009-02-16T17:02:33
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=438
permalink: /browsers/when-web-development-was-easy/
btc_comment_counts:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205288112"
btcnew_comment_summary:
  - 'a:1:{i:0;a:3:{s:11:"comment_src";s:4:"blog";s:3:"cnt";s:2:"20";s:7:"enabled";s:1:"0";}}'
categories:
  - Browsers
---
Do you remember the time when web development was easy? Right where it all started, when there was just one browser, and [only one website](http://www.w3.org/People/Berners-Lee/FAQ.html#Examples) existed?

Things changed. And now you can&#8217;t trust anything any longer. Trust me, if you think you know how your site will be shown, you&#8217;re wrong. Just consider the 10 major steps of &#8220;progress&#8221; we&#8217;ve made since then:

  1. **Browser widths** stopped being predictable as soon as people stopped using maximized windows, and monitor sizes stopped being the same everywhere. People cling to their fixed 760px or 960px grids feverishly (yes, me too), dreaming that they are what people use.
  2. **Browser heights** started giving us the same problems as widths, but toolbars also started showing up, making height prediction plain impossible to predict. &#8220;The fold&#8221; is now the top 10 pixels of a page, unless you got a browser warning, then &#8220;the fold&#8221; is pixels 10 to 20.
  3. **Aspect ratio**, the relation between width and height, went strange when first wide-screen monitors, then TV-screens and mobile phones, entered the market. I wouldn&#8217;t be surprised if I&#8217;m soon able to set my own ratio, or if someone launches a stretchable screen that I can drag to my own preference. I hope your site is well prepared for that one.
  4. **Colors** differ not only depending on the lightning in the room (which was a problem as soon as there where two computers), but also depending on monitor (including brightness and contrast), gamma correction differences between operating systems, gamma correction bugs in PNG files and browser implementations, color profiles (now supported in Firefox 3.1!). Add to this accessibility tools that invert colors, increase or decrease saturation. Pantone color codes on the web anyone?
  5. **Font selection** is another interesting mess. The browser has a default font, different (of course), depending on what operating system/device you&#8217;re on. The website author can try to override that font, specifying one or more fonts, which the user might, or might not, have. Oh, and lets not forget the editors, copying and pasting text from Outlook or Word, getting font tags inserted into your throughly crafted site.
  6. **Font rendering** complicates things even further by letting either the operating system or the browser render the fonts as they wish. Things like ClearType, subpixel font rendering, and font smoothing.
  7. **Character encoding** is far beyond repair, and this is easily conveyed by looking at what steps a browser has to go through to render a single letter. To [quote Mark Pilgrim](http://blog.whatwg.org/the-road-to-html-5-character-encoding): &#8220;It&#8217;s a 7-step algorithm; step 4 has 2 sub-steps, the first of which has 7 branches, one of which has 8 sub-steps, one of which actually links to a separate algorithm that itself has 7 steps&#8230;&#8221;.
  8. **Unstyled HTML** looks different because of default stylesheets in some (but not all) browsers. Developers are left guessing what styles to set to override all defaults.
  9. **CSS styling** is of course fully unpredicable, depending on not only browser, but on what underlying rendering engine, and version of that engine, and with what patches applied, and on what settings the user has made. On top of this we have piles of bugs, which tips most developers from scientists, trying to use logic to solve problems, to &#8220;empirates&#8221;, trusting only trial-and-error as a tool to &#8220;just get it to work&#8221;.
 10. **HTML versions** can also be selected in several ways, not always according to reason. First you can specify no doctype, and watch everyone try to render your site like IE5 once did, long time ago when someone used that browser. Then you can pick a doctype, and watch how some browsers render your page differently, depending on whether your doctype is in their &#8220;white-list&#8221; or not. And then there&#8217;s standards mode, quirks mode, and almost standards mode, there&#8217;s XML prologues and MIME-types, and what-not.

## But that&#8217;s not all, enter IE8

The newest entry in the &#8220;making web development hard&#8221; toplist, is (soon to be released) IE8. They have recently decided that your page will be [**rendered based on popular vote**](http://www.isolani.co.uk/blog/standards/Ie8BlacklistForcingStandardsRenderingOptIn). So better not make your designs &#8220;arty&#8221; in any way. People might think it&#8217;s broken and vote you to IE7 rendering (very broken). **Don&#8217;t laugh**, it&#8217;s not a joke, the proof is on IEblog, linked in the paragraph above. I dare you.

&#8220;Are you fully out of your fucking mind?&#8221;, you might be tempted to ask the IE8 developers. The reply is simply, no no, don&#8217;t worry, just settings this HTTP header you can opt-out of the rendering that popular vote has selected for you, even though you already opted-in by setting a doctype once.

And so we slowly stop caring, and give up. Dreaming ourselves back to the time when there where one computer, and one website&#8230;
