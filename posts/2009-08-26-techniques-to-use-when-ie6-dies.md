---
id: 496
title: Techniques to use when IE6 dies
date: 2009-08-26T23:54:51
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=496
permalink: /css/techniques-to-use-when-ie6-dies/
btc_comment_counts:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205288422"
btcnew_comment_summary:
  - 'a:1:{i:0;a:3:{s:11:"comment_src";s:4:"blog";s:3:"cnt";s:2:"25";s:7:"enabled";s:1:"0";}}'
categories:
  - Browsers
  - CSS
---
Everyone [except Microsoft themselves](http://www.eweek.com/c/a/Windows/Microsoft-Internet-Explorer-6-Support-Continues-Despite-Calls-for-PhaseOut-307122/) are talking about the death of IE6. I&#8217;ve tried [motivating people to drop support](/browsers/motivation-for-building-for-ie6/), arguing that you at least can show IE6 users a message. Many have replied with &#8220;but our IT department doesn&#8217;t let us&#8230;&#8221;, and I can say nothing more than that the IT department is filled with humans. Which means they are lazy, and upgrade when people whine enough about it. It&#8217;s a shame it has to be that way, that we have to [punish people for their IT departments](http://www.ie6nomore.com/corporate-users.html), but that&#8217;s how it has to be.

As **web developers**, we should be the ones complaining the loudest. We have so much to win on IE6:s death it&#8217;s silly. Just look at the below list of things IE6 can&#8217;t do, but IE7 can (the next worst browser):

  * Native PNG alpha transparency without silly hacks.
  * Several selectors: Child selector (&#8220;&gt;&#8221;), Adjacent sibling selector (&#8220;+&#8221;), Attribute selectors ([attr=value]), and [General sibling selector](http://www.w3.org/TR/css3-selectors/#general-sibling-combinators) (&#8220;~&#8221;, CSS3)
  * Min-height, Max-height, Min-width, Max-width
  * Multiple class/id selectors in the same ruleset (ie. .class1.class2 { &#8230; })
  * :hover on all elements, not just links
  * position: fixed
  * Native XMLHTTP (Without ActiveX)
  * International Domain Names (IDN), the ability to use UTF-8 chars in domains
  * Page zoom that zooms the whole page (don&#8217;t worry about zoom)

This is a huge step forward for us web developers. Huge! Bigger then when CSS3 comes out, because we won&#8217;t be able to use that one for years. Someone is pushing the front of what&#8217;s possible, I&#8217;m pushing for the front of what&#8217;s **usable**.

What can you do to help me get everything in the above list? And, did I forget something?

Sources:

  * [CSS Compatibility charts](http://www.quirksmode.org/css/contents.html)
  * [IE6 vs IE7 &#8211; New features in Internet Explorer 7](http://blogulate.com/content/new-features-of-internet-explorer-7/)
