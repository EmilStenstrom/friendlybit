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
We've all heard about how bad it is to use "left" and "yellow" as class names and ids. If you name an element "left", and then decide to move that element to the right, you have to go through all your pages and change that name. Too much work.

If you instead had called it "licenseAgreement", you would have been better off. Right? Perhaps not. Because we're forgetting about CMS:es. Those often have some kind of templates, where you as an interface developer define how the HTML should look. But as a interface developer, you have no idea of what kind of content editors will put into your templates. A couple of clicks later your "semantic id" is wrong.

**I think this is one of the reasons semantics hasn't gotten a hold of the CMS world**. CMS:es have no idea of what kind of content people will store in them. Their main business goal is to make something generic, that doesn't assume semantics.

This is why "wrapper" is such a common class name.
