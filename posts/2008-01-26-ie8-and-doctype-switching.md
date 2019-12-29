---
id: 150
title: IE8 and Doctype switching
date: 2008-01-26T17:44:50
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/ie8-and-doctype-switching/
permalink: /css/ie8-and-doctype-switching/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205287342"
btcnew_comment_counts:
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - HTML
---
The topic of this week has been IE8s new rendering mode, and the strange way to trigger it. As usual, I've decided not to comment right away, and instead first read what others are saying and try to form an opinion.

I believe the best articles that talks about the switch are these:

  1. [Legacy](http://www.b-list.org/weblog/2008/jan/23/legacy/), by <span class="person-name">James Bennet, puts this move in a bigger context. I believe his most important conclusion is that Microsoft are now clearly positioning themselves towards big old corporate intranets, reiterating "Don't break the web".<br /> </span>
  2. [Has Internet Explorer Just Shot Itself in the Foot?,](http://www.andybudd.com/archives/2008/01/has_internet_ex/) by Andy Budd, talks about how Microsoft marginalizes their own browser. Most people won't know about the switch, and end up in IE7 mode, so there's no real need for anyone to upgrade. IE7s rendering engine needs to be with us, forever.
  3. [Microsoft koan](http://diveintomark.org/archives/2008/01/23/microsoft-koan), by Mark Pilgrim, elegantly points out that strange code (unknown doctypes, including html5) will be rendered in standards mode, and ordinary code (proper doctype) will be rendered in IE7 mode. Seems twisted?

## The real strangeness

What I can't understand in all of this is how IE7-specific sites can be such big of a problem. Because that what all of this fuss is really about. That's why we need a new switching mode and they need to ship the IE7 rendering engine with IE8.

So, now there's a couple of different sites.

  * **IE6 specific sites.** My guess is that these are the majority of sites out there. These will break as much in IE8 as they did in IE7. "Don't break the web" does not apply to these sites.
  * **IE7 specific sites**. These are much fewer and got updated rather recently (badly, to work only in IE7). The new switch is there for these sites. With the switch these sites won't break.
  * **Sites built to the standards**. These were also updated rather recently, but unlike the above sites they were built to the standards. Fixes for IE6 and IE7 were properly only sent to just those browsers, and will _not_ be sent to IE8 (conditional comments anyone?). If you targeted IE7 with your conditional comment, IE8 will not get that fix, breaking these type of sites. Well, unless IE8 will execute IE7 conditional comments, when that engine does the rendering.

So let's look back at the previous articles, keeping in mind the IE team mantra: "_Don't break the web_", the very reason why this fix exists.

**First article** (1): My guess is that many corporate intranets belong in the first group of sites. They haven't been updated in a while, and won't be either. This group of sites will be just as unhappy with IE8 as they were with IE7. This can't be about those sites. IE team mantra: "_Keep breaking the web just as much as we broke it before_".

**Second article** (2): This switch will increase the number of sites in the IE7 specific group. This will be at the expense of the standards group. When a developer not knowing about the switch sees that his site works in IE7 and IE8 (which will be the same), he will stop working on it. IE team mantra: "_Freeze the web to IE7_".

**Third article** (3): Since unknown doctypes will send IE8 into standards mode, there will be even more breakage than before. What? Well, sites with broken doctypes, that previously sent IE6 and IE7 into quirks mode and relied on that, will break. IE Team mantra: "_Break the web_".

Additionally, modern developers that don't read the IE blog, and don't know about the new switch, will keep getting IE7s strange behaviour on their sites. And since the switch also can be made via a HTTP header, even copying the full HTML and CSS of a site might break it when looking at it locally. IE team mantra: "_Make people read our blog, or go insane trying to develop to the standards_".

## What it all comes down to

This is a terrible idea, both technically and in how it was presented. If the same idea had been presented in a more open manner, "_we're thinking about solving this problem like this… what do you think?_", people would have been much more willing to help, and had probably came up with a better solution.

WaSP really acted badly by not first talking to the community, or at least discussing things internally, and instead just presented how IE8 will be built. Also, since this won't help developing standards based websites, and instead help IE7 specific sites, I'm not sure what the WaSP has to do with this issue whatsoever.

On the constructive side of things, I think the **best way forward for IE8 is to change the switch to be opt-in, letting IE7 specific sites switch to IE7 rendering if they want to**. That's makes sure IE7 sites that break are easy to fix, and does not break havoc on the rest of the web. Don't set the default to worse rendering than you can produce.

With the above change, I'm looking forward to another modern web browser, IE8.
