---
author: Emil Stenström
categories:
- HTML
date: 2007-05-28 21:42:01
guid: http://friendlybit.com/html/dont-attach-html-files-in-outlook/
id: 127
permalink: /html/dont-attach-html-files-in-outlook/
title: Don’t attach HTML-files in Outlook
---

Just a short word of warning. I thought I'd mail the [min-/max-width template](/files/min-max-template/) to a colleague at work. So I fired up Outlook, attached the file and sent it. I thought that was it, Outlook couldn't get something simple like that wrong, could it? **Yes it could!** Opening the file I found some pretty nasty changes…

  1. A meta-tag with encoding gets added as the first line of the file (before the doctype). This naturally sends browsers into quirks-mode, effectively destroying most layouts.
  2. Comments are removed from the file, including Internet Explorers own conditional comments. This makes sure any fixes you have applied gets removed, additionally destroying the layout in IE.
  3. External stylsheets are instantly removed. You didn't think you could get away with that, did you?
  4. Links get `onClick="return (false);"` added, making them not work.

Have a look at the [mangled Outlook file](/files/min-max-template/index_mangled.html) (and the [original file](/files/min-max-template/)).

I'm sure there's more Outlook does, but those are the things that I noticed on this file. I've tried sending files and opening it with Thunderbird, and that seems to work, so the problem appears when you open the file from within Outlook, both when run as a native application and from the webmail version.

When sending off examples to your clients, do you know what e-mail client they use? Didn't think so. We better start zipping the files first…
