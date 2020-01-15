---
author: Emil Stenström
categories:
- HTML
date: 2009-07-23 21:39:10
guid: http://friendlybit.com/html/tapestry-5-and-how-not-to-treat-html/
id: 528
permalink: /html/tapestry-5-and-how-not-to-treat-html/
title: Tapestry 5, and how not to treat HTML
---

I've previously written about how [Microsoft Sharepoint](/html/default-html-in-sharepoint-2007/) mistreats HTML, and makes it look a whole other language. But truth to be told, Sharepoint (and .NET for that matter) isn't the only framework that can't handle HTML. I've recently worked with a Java framework called [Tapestry 5](http://tapestry.apache.org/), and it's really bad in some respects too (though not quite as bad as Sharepoint). Note that this is a review based on **only** how it handles HTML, not any other of its merits. Let's get started.

Many of Tapestry's problems comes from their design decision to parse the HTML you're trying to output. Yes, Tapestry parses your HTML, and adds stuff to it dynamically. This is nothing new, anyone that has played with ASP.NET knows how hidden form elements get stuffed in here and there. This is a nightmare for an interface developer, we need exact control over HTML to do our jobs well.

Tapestry does horrible things to HTML:

  * **Several extra javascripts and CSS files** are referenced in the head tag. There is no simple way to get rid of these.
  * **A meta tag** which states that the tapestry did generate this page, is added.
  * The two above are added to the head, and if a **head tag doesn't exist, it gets added**. Never mind that your current little HTML snippet was just a little part of a page, that was being fetched with AJAX, Tapestry will add a head tag for you.
  * **More javascript, and a hidden div** with a firebug-like console, is appended to the end of the body element.
  * **Self-closing tags are expanded** to a start tag and an end tag (`<input />` gets transformed to `<input></input>`), which means you can't use XHTML together with Tapestry.
  * **All whitespace is removed** by default, and you have to disable the "feature" on a tag-by-tag basis ("Please don't strip whitespace inside this list, IE6 goes crazy then"). This is a mess for interface developers, who know that whitespace matters for rendering. It was even [pointed out to Tapestry developers](https://issues.apache.org/jira/browse/TAPESTRY-2028) early on, but was ignored.
  * There are ways to do loops, if:s, reference variables and generate URL:s, but all of these are based on the HTML parsing. And as a good parser, **it skips all comments**. This means using tapestry template code inside a HTML comment will not work. When do you need that? Conditional comments! So what if you want an URL generated to your IE6 stylesheet? No go. You'll have to write a custom component that does that for you.
  * Changes the **id of all your forms to "form" and adds name="form"** (which is invalid HTML).
  * Adds a **hidden "t:formdata" field to forms**, much like the dreaded ASP.NET viewstate.
  * One of the javascript files added is [prototype](http://www.prototypejs.org/), a javascript framework which isn't compatible with jQuery. So you have to rewrite your javascript code to work in "No conflicts mode" if you want it to work with Tapestry.

No. Tapestry was clearly not built with an interface developer in mind. Why is it so hard for many web framework developers to just talk with people that work with HTML, CSS, and Javascript? Please ask us **before** implementing stuff like the above. We'll gladly give you our viewpoint.
