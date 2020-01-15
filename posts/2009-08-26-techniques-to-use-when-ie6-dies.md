---
author: Emil Stenström
categories:
- Browsers
- CSS
date: 2009-08-26 23:54:51
guid: http://friendlybit.com/css/techniques-to-use-when-ie6-dies/
id: 496
permalink: /css/techniques-to-use-when-ie6-dies/
title: Techniques to use when IE6 dies
---

Everyone [except Microsoft themselves](http://www.eweek.com/c/a/Windows/Microsoft-Internet-Explorer-6-Support-Continues-Despite-Calls-for-PhaseOut-307122/) are talking about the death of IE6. I've tried [motivating people to drop support](/browsers/motivation-for-building-for-ie6/), arguing that you at least can show IE6 users a message. Many have replied with "but our IT department doesn't let us…", and I can say nothing more than that the IT department is filled with humans. Which means they are lazy, and upgrade when people whine enough about it. It's a shame it has to be that way, that we have to [punish people for their IT departments](http://www.ie6nomore.com/corporate-users.html), but that's how it has to be.

As **web developers**, we should be the ones complaining the loudest. We have so much to win on IE6:s death it's silly. Just look at the below list of things IE6 can't do, but IE7 can (the next worst browser):

  * Native PNG alpha transparency without silly hacks.
  * Several selectors: Child selector ("&gt;"), Adjacent sibling selector ("+"), Attribute selectors ([attr=value]), and [General sibling selector](http://www.w3.org/TR/css3-selectors/#general-sibling-combinators) ("~", CSS3)
  * Min-height, Max-height, Min-width, Max-width
  * Multiple class/id selectors in the same ruleset (ie. .class1.class2 { … })
  * :hover on all elements, not just links
  * position: fixed
  * Native XMLHTTP (Without ActiveX)
  * International Domain Names (IDN), the ability to use UTF-8 chars in domains
  * Page zoom that zooms the whole page (don't worry about zoom)

This is a huge step forward for us web developers. Huge! Bigger then when CSS3 comes out, because we won't be able to use that one for years. Someone is pushing the front of what's possible, I'm pushing for the front of what's **usable**.

What can you do to help me get everything in the above list? And, did I forget something?

Sources:

  * [CSS Compatibility charts](http://www.quirksmode.org/css/contents.html)
  * [IE6 vs IE7 - New features in Internet Explorer 7](http://blogulate.com/content/new-features-of-internet-explorer-7/)
