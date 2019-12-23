---
id: 95
title: Judging the technical quality of a site
date: 2006-10-01T00:28:08
author: Emil Stenström
layout: post
guid: http://friendlybit.com/tutorial/judging-the-technical-quality-of-a-site/
permalink: /tutorial/judging-the-technical-quality-of-a-site/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205286466"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - Accessibility
  - Tutorial
---
When you look at a website to determine its quality on the code level, you need a different set of metrics than you did some years ago. This article is my attempt at specifying what metrics I use. Have a look at them, do they match yours?

First I look at the **validation**. Does the front page validate? Do all sub pages of the site validate? If they don’t, what kind of errors are there? While validation isn’t the most important metric, it’s a very quick way to get a feeling of if the coder is “web standards aware” or not. I use the [Firefox validation plugin](http://users.skynet.be/mgueury/mozilla/) that checks all the pages I visit and puts a little green check in the statusbar if the current page validates. For doing sitewide validation I use [htmlhelp’s validation spider](http://www.htmlhelp.com/tools/validator/) and let it loose on the site (check &#8220;Validate entire site&#8221;). Validation is slowly catching on as a standard tool in the webdev toolbox. Someone who is not using the validator probably doesn&#8217;t know much about web standards.

While on the subject of validation: don’t forget **validating the CSS**. There’s a lot of basic errors that the validator finds that only leads to errors in some browsers. The W3C CSS validator might help you fix some of those right away. Before you complain: the CSS validator has a few issues. If you use line-height, you need pass it a decimal number; 1 becomes 1.0, 0 becomes 0.0. Secondly, if you use CSS 2.1 or CSS 3 properties you need to inform the validator you do. Add the [URL parameter “profile”](http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Ffriendlybit.com&usermedium=all&profile=css21) with the value set to “css21” or “css3”, and revalidate. CSS errors and whether or not the style sheet is **well organized** clearly propagates what [CSS level](http://friendlybit.com/css/levels-of-css-knowledge/) the developer is on.

Next I look at the **doctype**. That single line of information at the first line of the HTML that defines what language the coder is using. Use of [Strict or Transitional](http://accessites.org/gbcms_xml/news_page.php?id=23) is what matters most. Most pages that validate as transitional can with very small changes be upgraded to strict. And why not? Strict signals that an effort has been made to ensure that the document separates structure from design. If you know how, there’s no reason not to. At this stage I also check that the doctype is properly set, there’s an IE bug that makes IE render things badly (quirks mode) if the doctype isn’t the first element of the page. Incorrect use of doctype is also a common way to recognize a beginner.

Sites that pass the above code tests get another batch of checks. Is the code **semantic**? (ie. does the HTML describe the content?) I look at elements, classes, and ids in use. Do they describe the content they contain? Bad sites use class names tied to design. Mediocre sites use general names like “wrapper” or “column2”. Great sites use “copyright”, “invitation”, and “footnote”. Many CMS:es generate design-oriented classes and ids, and only a few reach mediocre. This is one way to see that a site was robot-made.

Another code issue is the **content over HTML quotient**. For just a few lines of content you shouldn’t have to need huge amounts of HTML. You shouldn’t need 10 divisions just for one header. A high content over HTML quotient signals that the developer knows what he’s doing. An “overmarked” site means that the developer is on the right track but suddenly forgot that content is more important than the code behind it.

One last angle is the **accessibility** one. How will a screen reader read this site? Is all the content of the site available as readable text? Does the site require javascript when it isn’t needed? A good place to see if someone knows about accessibility (on the web) or not is checking the forms. Fieldsets, legends, and labels: they all tell their story about the developer and his knowledge about accessibility.

A quality site ranks high in all of the above.
