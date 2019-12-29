---
author: Emil Stenström
categories:
- CSS
date: 2007-04-28 20:44:31
guid: http://friendlybit.com/css/transparent-pngs-and-ie6-standalone/
id: 122
permalink: /css/transparent-pngs-and-ie6-standalone/
title: Transparent PNGs and IE6 standalone
---

I'm one of many that have installed [IE6 standalone](http://tredosoft.com/Multiple_IE) and it really is a great solution to running both IE6 and IE7 on the same computer. Frequently people claim that IE6 standalone and the real IE6 render things differently but I've never seen that happen. Until now.

## Why an alpha transparent image?

I'm working on a site with several alpha-transparent areas, where authors should be able to switch images and an semi-transparent box should cover half of that image. The users are not skilled enough with image programs to be able to add the transparent part to the image, and adding it to the image would prevent it from expanding when the containing text was zoomed. So I decided to use CSS together with alpha transparent PNGs to solve it. Let’s get to business.

## Alpha transparency on modern browsers

Fireworks, my favourite image editor, allowed me to set the opacity to 60%. It smoothly exported my image to PNG and I positioned everything where it should be. Two background images later, one that the author could specify (added with a style tag in the head, [not with inline styles](/css/inline-css-should-not-be-allowed-in-strict-doctypes/)), and one with the transparency. Everything worked flawlessly in Firefox, Opera, and IE7, as expected. Easy!

## IE6 and AlphaImageLoader

IE6 does not support PNG images like that, so I decided to use what I always use to fix that, the [AlphaImageLoader Filter](http://support.microsoft.com/kb/294714). Note that the fix doesn't make the background specified with CSS work, it _adds a new_ element to the page, on top of the element you apply it to. It's also proprietary, meaning it won't validate, so make sure add it to the page by using [conditional comments](http://www.quirksmode.org/css/condcom.html).

One thing you need to know to use the filter is how the [sizingMethod property](http://msdn2.microsoft.com/en-us/library/ms532920.aspx) works:

> **crop** - Clips the image to fit the dimensions of the object.

> **image** - Default. Enlarges or reduces the border of the object to fit the dimensions of the image.

> **scale** - Stretches or shrinks the image to fill the borders of the object.

So there is no way to repeat an image as we're used to from CSS. Luckily, since I wanted a solid semi-transparent background repeating and scaling is the same, so I just did:

```css
#breadcrumbs {
  filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(
    src="semi_transparent.png", sizingMethod="scale");
}
```

## Making links work in IE6

You could think that we've hacked enough to get things up to speed with IE6, but no. Links on top of images loaded with filter does not work. The text of them are selectable, but you can't click them. Fortunately Ingo Chao fixed this in 2005 (some people are WAY ahead) by simply [adding an inner wrapper](http://www.satzansatz.de/cssd/tmp/alphatransparency.html) with hasLayout enabled. Thanks Ingo!

Everything set, and tested in Firefox, Opera, IE7 and IE6 standalone. Phew!

## Differences between IE6 standalone and IE6

After deploying the design on the client's server I quickly got a bug report back: "The breadcrumbs have a grey background, not a transparent one". I double checked the client's browser version to be IE6, and tested again locally on my own computer: it worked for me but not for the client. Confused I started looking for another computer with IE6 on (something that was surprisingly hard) I found one at the reception. Gotcha, the PNG was broken there too. I confirmed that IE7 was not installed and downgraded my own to IE6 again. Let's get to work!

After much fiddling with CSS I moved over to Fireworks again. It has three different versions of PNGs you can export as: PNG-8, PNG-24, and PNG32. I tried **switching from PNG-24 to PNG-8** and \*blam\* it worked!

I'm not sure why this works, but after reading the comments on the [Multiple IE](http://tredosoft.com/Multiple_IE) page, I have a guess. To get filters to work in IE6 standalone two files are added to the IE6 folder. The authors picked them from an updated version of IE6; could it be that Microsoft updated the filters somewhere between my downgraded version and the latest IE6? After Googling I found an update to IE6 called SP1 which changes the behaviour of alphaimageloader. Quite likely, and very tricky to find.

Anyway, I hope this long story taught you something, I sure did it for me: Next time I'll use [Iepngfix.htc](http://www.twinhelix.com/css/iepngfix/) instead :)
