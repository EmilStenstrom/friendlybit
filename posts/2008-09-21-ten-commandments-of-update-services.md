---
id: 239
title: Ten commandments of update services
date: 2008-09-21T23:10:25
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=239
permalink: /other/ten-commandments-of-update-services/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205287710"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - Other
  - Tutorial
---
I'm getting increasingly annoyed with update services shipped with popular applications. It's looks like it's getting worse and worse, and I think someone should stand up and say **enough is enough**.

  * [Adobe Update](#adobe)
  * [Google Update](#google)
  * [Microsoft Update](#microsoft)
  * [Ten Commandments of Update Services](#ten)

Let me start by showing when updates go wrong:

## Adobe Update {#adobe}

<img class="secondary" src="/files/post-media/adobe_logo.jpg" alt="" />I start Adobe Fireworks because I want to resize an image I have. After it has started and the image has loaded the update service prompts me that there are new updates available. For what? It doesn't say, so I click more info and get a list of things. Strange: **None of them seem related to Fireworks**.

The update starts, and tells me I **have to close Fireworks** to complete it. Bah, I just started it! I'm trying to resize an image here, remember? But Ok, this time. Next it tells me to close Firefox. What?! All my precious tabs I've saved for later reading! Bitches.

The download begins, and the **progress window takes focus** over the other stuff I'm doing while not looking at the progress bar. \*Repeated clicking to hide the window\*. Then when it's done it takes focus again, and asks me to click the only button available. GAH?!

Ok, done. Why was I starting Fireworks again? And hey, what's those **new PDF icons** doing in my Links toolbar in Internet Explorer?

## Google Update {#google}

<img class="secondary" src="/files/post-media/google-logo.jpg" alt="" />Oh, a new web browser: Google Chrome, I surely want to try it out. \*Couple of hours of fiddling\*. Nah, I still like Firefox more, I'll go back to using that one. **Wait, what's that GoogleUpdate.exe process doing there**? I'll try closing Chrome. Nope, still there. Ok, I'll force it to close. Hmm, it restarts after a while. Ok, must be some kind of process that starts with Windows. Ah, registry setting, lets remove that one. \*Reboot\*. Still there?! Ah, they also installed it as a service. Lets remove that too. Finally!

What's that? A new version of Google Gears! \*Installing\*. Hmm… What's that GoogleUpdate.exe process doing there? GAH! What were you thinking Google?!

## Microsoft update {#microsoft}

<img class="secondary" src="/files/post-media/logo_microsoft_small.gif" alt="" />I really should make sure my OS is up to date. Lets go to the windowsupdate website. What? I need to run IE5 or later? Ah, no Firefox support, damn it. Lets switch browser. Ok. Install validation thingie? Ehm… I guess I have no choice. \*Waiting\*. Ok, now let's see if there's some updates, Express or Custom? Custom, of course. \*Waiting quite a long time\*. Why are you making me look at a progress bar? Ok, no OS upgrades, but there's some update to Windows Media player. Yeye, I guess it couldn't do any harm (not that I use that one). Trust ActiveX thingie? Yeye, I know what I'm doing. \*Waiting some more, with focus stealing\*. "Please restart your computer to complete the installation". Sigh.

So why don't I just use Windows Update program instead? Well, there's a window that pops up every 5 minutes that remind you that you have to restart the computer. Do you know how annoying that one is? No, it's MORE annoying than that.

## Ten Commandments of Update Services {#ten}

So I hope that's enough evidence that big companies have no idea how do conduct a decent update of their own program. So let me offer some (free of charge) advise:

  1. If your update is web based, **let me use any modern browser I want**. Don't start by getting me annoyed.
  2. Check for updates **right before the program starts**. I know that you want me to close the app while it's being updated, but why on earth do you let me start it then? Lets keep it simple, update before the program starts, and resume starting the app when you're done.
  3. **Don't leave processes running in the background** when I close the program. When I close your program, I don't care about you, or any updates to your program.
  4. **Only update the current program**, not bundled ones. I know you want me to have the latest versions of all your programs, but odds are I don't even use them. Update those programs when I start them, not now.
  5. **Show me what gets updated**, and if possible link to a change log. If you want me to download 70 Mb you need to first talk me into why I need it. You may want to hide detailed info for inexperienced users, but could you please then remember that I'm not one of those?
  6. If it's a tiny update (less than 1 Mb), you can just **go ahead and install right away**. You don't even have to prompt me.
  7. **Download and install in the background**, without stealing my focus. If you're shipping a big pile of fixes (ie. the version I bought was not done), you have to let me do other stuff while you update. Like surfing the web. It's not Ok it require that I close unrelated programs, sorry.
  8. **Never ever touch my browser bookmarks**. Never add things to the quicklaunch bar. Never make things start automatically unless I've told you that's what I want (why do most people have a Quicktime icon in their systray?). The only way of getting into my bookmarks or my quicklaunch bar is writing a really good application. You can't force me to like you. The opposite works well though.
  9. **Never require me to restart the computer**. There's only one exception for when you may: when I'm updating the operating system. No excuses.
 10. **When you're done**, just start the program. I don't want to confirm anything, I want to get to work using your app.

(Bonus point from [James Socol](#comment-31047) in the comments: 11. **Use incremental downloads**, so I don't have to download stuff I already have installed.)

If you are a software company, and can't manage the above, just do it the old fashion way: let me manually download a file from your website. That will annoy me much less than a bad automatic process. Or if you want things to be really convenient: **write a web application instead**.

Now get to work. I've had it.
