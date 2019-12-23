---
id: 61
title: Open letter to the IE Team
date: 2006-05-03T13:37:07
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/open-letter-to-the-ie-team/
permalink: /css/open-letter-to-the-ie-team/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205285837"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - Other
---
<p class="first">
  Dear IE Team,
</p>

<p class="first">
  I have carefully followed the development of Internet Explorer 7 (IE7) and really liked what I&#8217;ve seen. Especially the CSS bugfixes are wonderful, the tabs are really needed, and the team talking about the development on your blog is really nice too. You are doing a great job and you should receive credit for it.
</p>

One thing keeps bugging me though. Soon you will release the browser on Windows Update and people will automatically start upgrading, replacing their old browser (IE6) with the new version. I use Windows Update so my version will be upgraded too, and there&#8217;s the problem: I&#8217;m a web developer and I need to test my sites in more than one version of each browser. IE7&#8217;s ability to _replace_ IE6 instead of working standalone will for me be a pain. As I see it I have the following options:

  * **Get another computer**. On that other computer I could have the old version of IE installed, with security bugs and all, and then move from computer to computer while testing.
  * **Install a virtual machine** on my current computer. This means I could have the old IE6 on the virtual machine and test there. While this sounds pretty good it still means I have a reserve a large part of my computer for IE6 testing, something that feels very strange to me. I looked up what Microsoft Virtual PC costs and found $129, an expence that a student can&#8217;t take just like that
  * **Drop support for IE6**. If you really could get all your current users to upgrade this would be a viable option. The problem is that you will not, at least for the comming five years. You will have the non-XP Windows users that won&#8217;t get the oppurtunity to upgrade, you will have the modem users that will not have the bandwidth to upgrade and you will have the clueless people that will have no idea that there is an upgrade available. This is not a problem for you, because you are just working with the new version, but it is a problem for me as a web developer, because I have to deal with the old version for a long time still.
  * **Hack IE7 to work standalone**. I have found some tutorials on how to make IE7 standalone but the problem with that is that it&#8217;s a mess. Look at it, copying of registry entries, DLL files, and EXE files around. If this is what you want us to do, why not ship a nice and thoroughly tested version of this script yourselves?

So, this is my dilemma. Which of the options do you want me to use?
