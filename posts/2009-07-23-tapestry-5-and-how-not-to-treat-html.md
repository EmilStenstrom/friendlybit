---
id: 528
title: Tapestry 5, and how not to treat HTML
date: 2009-07-23T21:39:10
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=528
permalink: /html/tapestry-5-and-how-not-to-treat-html/
btc_comment_counts:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205288575"
btcnew_comment_summary:
  - 'a:1:{i:0;a:3:{s:11:"comment_src";s:4:"blog";s:3:"cnt";s:2:"25";s:7:"enabled";s:1:"0";}}'
categories:
  - HTML
---
I&#8217;ve previously written about how [Microsoft Sharepoint](/html/default-html-in-sharepoint-2007/) mistreats HTML, and makes it look a whole other language. But truth to be told, Sharepoint (and .NET for that matter) isn&#8217;t the only framework that can&#8217;t handle HTML. I&#8217;ve recently worked with a Java framework called [Tapestry 5](http://tapestry.apache.org/), and it&#8217;s really bad in some respects too (though not quite as bad as Sharepoint). Note that this is a review based on **only** how it handles HTML, not any other of its merits. Let&#8217;s get started.

Many of Tapestry&#8217;s problems comes from their design decision to parse the HTML you&#8217;re trying to output. Yes, Tapestry parses your HTML, and adds stuff to it dynamically. This is nothing new, anyone that has played with ASP.NET knows how hidden form elements get stuffed in here and there. This is a nightmare for an interface developer, we need exact control over HTML to do our jobs well.

Tapestry does horrible things to HTML:

  * **Several extra javascripts and CSS files** are referenced in the head tag. There is no simple way to get rid of these.
  * **A meta tag** which states that the tapestry did generate this page, is added.
  * The two above are added to the head, and if a **head tag doesn&#8217;t exist, it gets added**. Never mind that your current little HTML snippet was just a little part of a page, that was being fetched with AJAX, Tapestry will add a head tag for you.
  * **More javascript, and a hidden div** with a firebug-like console, is appended to the end of the body element.
  * **Self-closing tags are expanded** to a start tag and an end tag (`<input />` gets transformed to `<input></input>`), which means you can&#8217;t use XHTML together with Tapestry.
  * **All whitespace is removed** by default, and you have to disable the &#8220;feature&#8221; on a tag-by-tag basis (&#8220;Please don&#8217;t strip whitespace inside this list, IE6 goes crazy then&#8221;). This is a mess for interface developers, who know that whitespace matters for rendering. It was even [pointed out to Tapestry developers](https://issues.apache.org/jira/browse/TAPESTRY-2028) early on, but was ignored.
  * There are ways to do loops, if:s, reference variables and generate URL:s, but all of these are based on the HTML parsing. And as a good parser, **it skips all comments**. This means using tapestry template code inside a HTML comment will not work. When do you need that? Conditional comments! So what if you want an URL generated to your IE6 stylesheet? No go. You&#8217;ll have to write a custom component that does that for you.
  * Changes the **id of all your forms to &#8220;form&#8221; and adds name=&#8221;form&#8221;** (which is invalid HTML).
  * Adds a **hidden &#8220;t:formdata&#8221; field to forms**, much like the dreaded ASP.NET viewstate.
  * One of the javascript files added is [prototype](http://www.prototypejs.org/), a javascript framework which isn&#8217;t compatible with jQuery. So you have to rewrite your javascript code to work in &#8220;No conflicts mode&#8221; if you want it to work with Tapestry.

No. Tapestry was clearly not built with an interface developer in mind. Why is it so hard for many web framework developers to just talk with people that work with HTML, CSS, and Javascript? Please ask us **before** implementing stuff like the above. We&#8217;ll gladly give you our viewpoint.
