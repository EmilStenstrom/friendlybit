---
id: 140
title: 'Sharepoint 2007 from an interface developer’s view'
date: 2008-01-20T12:10:42
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/sharepoint-2007-from-an-interface-developers-view/
permalink: /css/sharepoint-2007-from-an-interface-developers-view/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205287262"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - HTML
  - JS
---
Like Cameron Moll ([Skinning Sharepoint](http://cameronmoll.com/archives/2007/05/skinning_ms_sharepoint_with_st/) and [Pointedly unskinnable](http://cameronmoll.com/archives/2007/10/sharepoint_2007_pointedly_unskinnable/)), I've been working with Sharepoint 2007 (aka MOSS) recently, and I hope you don't mind me posting a few articles about my work here. I've found far too few blog posts that really go to the depth in explaining how things really work. I'll try to do that here, but I hope you can respect my wish that this does not turn into a helpdesk.

## "Customization"

Let's start. **Sharepoint 2007 very, very hard to customize**. If your job is to customize the interface in any major way, you have a lot of work ahead of you. You might think you're a much better interface developer than me, but you still have a lot of work ahead of you. You need to accept that.

When you read about Sharepoint 2007 on other sites you will find that people are really ecstatic about it. Just check the comments on how to [customize the calendar](http://planetwilson.blogspot.com/2007/09/sharepoint-2007-colour-color-calendar.html). Reading carefully you will find that he's comparing it with Sharepoint 2003, not with other products, or even a standard ASP.NET site. That's a big difference. Sharepoint 2003 was much worse, but that does not mean things are good now. This is a common pattern, people that like Sharepoint compare it to the previous version, not with better ways of doing things.

As most CMS:es, Sharepoint gets sold to customers that don't know programming. They see a product that can handle all the features they want: blogs, wikis, forums, calendars, document libraries, workflows, and so on. All features you could ever want is included, from what is called "out of the box". The problem is that the system is built so that all of those "out of the box" features are hard to customize. Things like changing how the wiki renders, is really hard. Often it's easier to rebuild that feature from scratch, than customizing what Sharepoint ships.

This is the main reason, from my point of view, that you should pick another CMS.

## Specifics

I don't believe you trust me on my words, so I thought I'd be more specific now, and talk about the issues that make Sharepoint 2007 hard to work with (customize). Let me stress that these are not all the issues, just the major ones that an interface developer has to tackle.

### Development

From what I've read from larger projects, the recommended development environment for a Sharepoint site is a virtual machine. For us, we needed a 36 Gb image, a size that required me to get a new external hard drive, just to store it. Also, running in a virtual machine means that you only can use about half of your RAM, which means everything gets slow. As if that wasn't enough, a new virtual machine means you have to reinstall all your programs, browsers, plugins again. Web development shouldn't have to be like that.

### Accessibility

Sharepoint has gotten a lot of bashing for not being accessible, so they've added some features to account for that. Some of those are really good individually, but looking at the general mess that is the HTML that Sharepoint spits out, the pretty page above fades in importance. One major problem is that you still need **javascript enabled** for many of the accessibility features. Enabling "Accessibility mode", among other things, makes dropdown menus appear as new windows (popups) instead of dynamically writing HTML to the page. And this is after they "fixed" it.

### Page size

A standard Sharepoint site uses lots of default Javascript and CSS in two files called core.js and core.css. All in all they add up to over 250 kb. Yes, that's not a misspelling or extra zero, a default page in sharepoint takes at least 250 kb. This is not counting the HTML, a huge, table-ridden, inline-javascripted, mess of things.

If you go through lots of trouble, you can strip those files out, but that means you can't use any default components. Since much of Sharepoint depend on those, you don't really want to go that way. It's a mess, and Microsoft themselves recommend you try to [remove some of it](http://msdn2.microsoft.com/en-us/library/bb727371.aspx#MOSS2007OptPerfWCM_PagePayloadSmallisGood) to boost performance. Preferably by using AJAX to load the js file later. Seriously.

### Javascript and Browser dependencies

Except from core.js, the javascript is spread out all over the place. As usual in many CMS:es, javascript is not treated as a real programming language, so there's no structuring whatsoever. Sometimes it's script tags, sometimes inline, sometimes external mini files, and most often automatically generated code. It's a real mess, and is a big reason for the HTML size being so large. Many of the scripts do not work in browsers other than IE, which means you really need IE to properly use the admin interface.

From the browser compatability info you can read that there are level 1 and level 2 browsers:

> "Level 2 web browsers support all of our basic functionality so that users can both read and write in our content sites, perform site administration, etc. Some functionality may not be available, some functionality may be available in a more limited form, and some visual rendering may not be as optimized as our Level 1 browsers. We also will not support Level 2 web browsers on the Central Administration site."

These are the Level 2 browsers: Firefox, Netscape, Safari. Opera isn't even in the list. Is this the new, modern way, of handling cross browser compatibility?

### Changing the CSS

I previously said that most CSS is included in a file called core.css. The file in itself if huge, with thousands of class names, and no structuring whatsoever. Heather Solomon has made an attempt to make things workable by [making images of what each class specifies](http://www.heathersolomon.com/content/sp07cssreference.htm). It's not even nearly a complete reference, and helps some, but using [Firebug](http://getfirebug.com/) is a faster way. Another thing the CSS sheet above does, is show how completely unorganized the CSS is. Have a look at it.

As with core.js you can't really remove core.css, since lots of built-in functionality depends on it. So what you need to do is start deciding which of those rules you need to overwrite and which not. Have fun!

To add to the insult, if you just add your own CSS as an external file and try to link to that on your own pages, core.css is appended as the last stylesheet in the source code. This of course means that all your changes get overwritten, and you need to hack around things by using the <link> tag directly (instead of sharepoint's own csslink-control), or add your custom files via the admin interface. Since core.css is just a list of simple class names, you can also use [CSS Specificity](http://www.htmldog.com/guides/cssadvanced/specificity/) to make your rules count, but that isn't mentioned in any of the troubleshooting blog posts. None the less, it's tedious do work around.

### Share point and Master pages

Most of Sharepoint is upgraded to use .NET 2.0, and its concept of Master pages and aspx pages. For those of you that don't develop in .NET the two can be explained as a templating mechanism, where each Master page has general placeholders where you can insert aspx pages. In each aspx page you specify one master page, and all of the placeholders you want to fill with content. It's a pretty good system.

Sharepoint taps into this system by making up two strings "~masterurl/custom.master", and "~masterurl/default.master", that you use instead of specifying your own masterpages. Users then specify masterpages in the admin interface, potentially breaking the entire site. Also, Sharepoint assumes there's just one masterpage per site, so if you thought you could use one masterpage for twocolumn layouts, and another for threecolumn layouts, you're wrong. The solution here is to break out of the Sharepoint way and hardcode real urls instead of doing things the Sharepoint way.

There's also things you can't change. The admin interface has a masterpage called application.master, which controls pretty much everything that has to do with built-in Sharepoint things. You don't ever change this file, since it's quite easy to seriously break things then. The problem is that this file also specify the look and feel of the admin interface, and if you're building a site where people are expected to add stuff, they will spend time in the admin interface. There isn't a good way around this, and you probably end up just changing some colors via CSS and let it be.

### Default .NET controls

The default master pages that ship with Sharepoint is horrendous and I'll post more details about them in a later post. But even if you roll your own master pages from scratch you still have the standard .NET-problem with controls. Using controls in .NET is a way to package functionality that you can easily add to your pages. A developer just needs to copy a DLL file, and call the control, optionally sending in some parameters. Easy.

The problem with this approach is that a control consists both of logic and HTML. So if you want some built-in logic that renders, say, the breadcrumb trail, you also get the HTML the author of the control deemed appropriate. In Sharepoint, a breadcrumb trail can be a doubly nested table, with display: none; controls to enable accessibility, and a doubly span nested link. It's just a terrible mess, but there's no other way to get to the breadcrumb logic, except from building a new control from scratch. Be prepared to work with terrible HTML.

## In summary

If you want to examine the points above by yourself, there's a MOSS example site up at [wssdemo.com](http://www.wssdemo.com/default.aspx).

This article is a interface developer view at Sharepoint 2007. If you look at the system from other viewpoints, I'm sure there are good things there. That's not my point. What I'm trying to say is that **Sharepoint 2007, is beyond repair when it comes to interface customization**, and you should do everything in your power to avoid working with it. If I can give one interface developer the arguments to convince a customer to pick another system, this article was worth it. Thanks for reading.
