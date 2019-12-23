---
id: 398
title: Interface developers and security
date: 2009-01-24T00:30:44
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=398
permalink: /css/interface-developers-and-security/
btc_comment_counts:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205556777"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - HTML
  - JS
---
You live in a **new era**, when demanding that people register on your site is no longer enough. There&#8217;s far too many other sites out that that you&#8217;re already a member of, you don&#8217;t need another one. You need to trust people.

You also want people to contribute to your sites with content somehow. Text is not enough, you want all kinds of &#8220;rich&#8221; content, and you want people to be able to place them how they want on your page. I mean, we live in a **new era** after all.

Problem is, this **new era thingie talk** makes people forget the basics. Even though this is the future, and we&#8217;re all bored with &#8220;just&#8221; hypertext, we can&#8217;t allow random people to add HTML to our sites. Why? Ask myspace about the [Samy worm](http://namb.la/popular/tech.html) from 2005, a little piece of clever front-end code that took their servers flying. What did they do wrong? They tried to let untrusted people embed HTML on their profile pages.

But they even had this clever filter, which cleaned the code first! Well, long story short, using a div with the style attribute set to a background image that points to a javascript url actually execute the javascript in IE6. Didn&#8217;t think of that did you? So what about the fact that both IE6 and IE7 execute vbscripts in urls prefixed with &#8220;vbscript:&#8221;, just like with javascript. Didn&#8217;t know that? Ohhh. Perhaps then you shouldn&#8217;t be trying to let unknown people embed HTML on your site?

Many of these security issues stem from the fact that ordinary well-educated computer scientists **don&#8217;t know enough about interface development**, HTML, CSS and javascript, and discount them as being something that &#8220;anyone&#8221; could do. &#8220;Even my aunt made this puppy site in like 3 days, how hard can it be?!&#8221;.

I&#8217;ve always thought that interface development have an undeserved reputation of being easier than &#8220;real programming&#8221;; something that you can let rookies work with, something that no &#8220;real&#8221; programmer would ever want. &#8220;No, I want to work with hard stuff, not that webby stuff&#8221;.

If you are in a position where people actually think that, perhaps security could be the way to lift interface development to its proper status. So why not read up on [Cross Site Scripting (XSS)](http://en.wikipedia.org/wiki/Cross-site_scripting), look at examples of vulnerabilities, and pick a couple of examples of [big sites that are vulnerable](http://www.xssed.com/). While you&#8217;re at it, why not read up on [Cross-site request forgery (CSRF)](http://en.wikipedia.org/wiki/Cross-site_request_forgery) too?

These are real issues that **someone** needs to take into account when building websites. My guess is that the fancy computer scientists will have a very long way to go before grasping this stuff. &#8220;Why does IE6 parse &#8216;java   script:&#8217; as if there where no space in the middle?&#8221;. You know who&#8217;s not surprised? Every damn interface developer out there.

So. Go out there, and teach them silly math people how it&#8217;s done, and what your HTML, CSS and javscript-knowledge is worth. Show them that logic isn&#8217;t the way we do things around here, that anything can happen when IE6 boots. And&#8230; whatever you do&#8230; think very hard before letting people embed HTML on your site.
