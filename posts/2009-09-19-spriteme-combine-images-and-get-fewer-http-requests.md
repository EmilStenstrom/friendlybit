---
author: Emil Stenström
categories:
- CSS
date: 2009-09-19 17:09:02
guid: http://friendlybit.com/?p=557
id: 557
permalink: /css/spriteme-combine-images-and-get-fewer-http-requests/
title: SpriteMe – Combine images and get fewer HTTP requests
---

Those of you that care about website performance have probably read about combining images, something that's called "CSS sprites". The idea is that by using the same (somewhat larger) image several times, you get fewer HTTP requests to your site, and therefore speed it up. Problem is, most of your images are CSS background images, that are positioned using clever background-positions and repeats.

Now, this makes to tricky to combine images. Something that repeats horizontally can't be combined with something that repeats vertically (unless there's transparency involved), and wide images can't be combined with narrow ones. So combining is usually tedious, manual work, both to combine the images and then calculate the new background-positions required.

Lucky for us then, that there is a tool called [SpriteMe](http://spriteme.org/), available as a bookmarklet (a bookmark containing javascript), and as an excellent [online demo](http://spriteme.org/demo.php) that walks you through how it works. SpriteMe does all the hard work for you, you just have to copy and paste both the combined images, and the new background rules, to your site.

Decreasing the number of HTTP requests have never been simpler. Well done [Steve Souders](http://www.stevesouders.com/)!
