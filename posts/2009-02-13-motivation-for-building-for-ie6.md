---
author: Emil Stenström
categories:
- Browsers
date: 2009-02-13 15:29:37
guid: http://friendlybit.com/browsers/motivation-for-building-for-ie6/
id: 430
permalink: /browsers/motivation-for-building-for-ie6/
title: Who are you disappointing with IE6 support?
---

Internet Explorer 6 (IE6) is not getting any younger. With a initial release date of 27:th of August, **2001**, it's one of the oldest things touching the internet with its slimy fingers. Since then, surfing has taken great leaps forward. In all areas: Web standards, Security, Usability, Rendering speed, Debugging, and more. By working hard to maintain backwards compatibility all of us are missing all of that progress.

Now. You as a web developer have a **responsibility** here.

## Responsibility towards IE6 users

Over the years, IE6 has had [142 security issues uncovered](http://secunia.com/advisories/product/11/). Still 22 of those are not patched. Most IE6 users have no idea of this, but you do. You don't want these people do to their online banking with that kind of browser backing them. You should help these users by educating them, and **making it easy for them to upgrade**!

## Responsibility towards your employer

If people are paying you do build websites for them it's even worse. By not pushing for upgrade, you're holding their website back. You're downgrading features since "they won't work in IE6", you're over optimizing your javascript because "the site gets slow in IE6", you're hack around CSS issues with extra stylesheets because "IE6 just don't get your styling right". Each hour you work with IE6 backwards compatibility, is one hour less work on new features. Many developers agree that about half their time goes to planning, testing, and patching IE6 issues. That means you could be **twice as productive** to your employer it you did things differently.

## Responsibility towards Microsoft

Some people will call me and Microsoft-hater because of this article. You're right, I don't like most things Microsoft do. But that doesn't have anything to do with IE6. I'm fine with people upgrading to IE7. In fact, I prefer people upgrading to IE7 over them switching to Firefox. Why? Because IE7 replaces IE6, making it impossible (or too hard for beginners) to switch back to the IE6 junk.

So this has nothing to do with my Microsoft dislike. In fact the Microsoft developers [would be delighted](http://windowshelp.microsoft.com/Windows/en-US/Help/a426bb85-708c-4b75-87e2-874f9be3b4aa1033.mspx) if IE6 just stopped working today. Just consider, how much of the code you wrote 8 years ago are you still proud of? I mean, they just released IE8 RC1 for gods sake! Give them a break.

## Responsibility towards yourself

By subscribing to friendlybit I assume you care about web standards. You have lengthy arguments with table developers over why their way is outdated, you have already talked about Firefox with your friends, and your parents have switched long time ago. But what looks good when you open your mouth, **you throw away as soon as you start doing real work**. You hack, hack, hack, and patch for IE6. Despite you knowing that this is the wrong way of doing things, despite the pain you feel doing it, despite everything you've read.

What I'm asking of you are two simple things:

  1. Stop saying: "Well, you need to support IE6 at least, that's what everyone else is doing". Instead think like this: "**Can I find any reasons that warrants disappointing** IE6 users, my employer, Microsoft, and myself". Well, do you? (I'm sure comments will fill up reasons…)

  2. **Encourage IE6 users on your website to upgrade**. This is really a no-brainer. If IE6 development is so much of a pain, why don't we do more to stop it? Even if you disagree with everything else I've written, you must agree that promoting upgrade is a good thing. Right? This is the code you need:

```html
<!--[if lte IE 6]>

<div id="upgrade">Your browser is 8 years old! Please upgrade to the latest version by going to
<a href="http://windows.microsoft.com/en-us/internet-explorer/products/ie/home">Microsoft.com</a></div>

<![endif]-->
```

And then style the #upgrade div appropriately. It's easy, doesn't rely on javascript, and points users directly do the download page instead of the three intermediary pages on microsoft.com. Add this to your own site, to your employer's sites, to your sisters site. Or maybe buy one of the numerous [IE t-shirts](http://shop.cafepress.com/internet-explorer) out there. Hell, print it out and stick it on your dog! **Do something**!

Now. Before you get upset and tell me why your specific case is **so different** from everyone else. Don't. Remember point 1 above. I've just done point 2 above on this site. Now it's your turn!

(Thanks to [Robert](http://www.robertnyman.com/2009/02/09/stop-developing-for-internet-explorer-6/) for pushing me to write this)
