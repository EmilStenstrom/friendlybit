---
id: 159
title: 'Why the class name "wrapper" is so common'
date: 2008-04-30T15:06:27
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=159
permalink: /html/why-the-class-name-wrapper-is-so-common/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205287454"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - HTML
---
We&#8217;ve all heard about how bad it is to use &#8220;left&#8221; and &#8220;yellow&#8221; as class names and ids. If you name an element &#8220;left&#8221;, and then decide to move that element to the right, you have to go through all your pages and change that name. Too much work.

If you instead had called it &#8220;licenseAgreement&#8221;, you would have been better off. Right? Perhaps not. Because we&#8217;re forgetting about CMS:es. Those often have some kind of templates, where you as an interface developer define how the HTML should look. But as a interface developer, you have no idea of what kind of content editors will put into your templates. A couple of clicks later your &#8220;semantic id&#8221; is wrong.

**I think this is one of the reasons semantics hasn&#8217;t gotten a hold of the CMS world**. CMS:es have no idea of what kind of content people will store in them. Their main business goal is to make something generic, that doesn&#8217;t assume semantics.

This is why &#8220;wrapper&#8221; is such a common class name.
