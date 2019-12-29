---
author: Emil Stenström
categories:
- CSS
date: 2007-05-28 20:57:31
guid: http://friendlybit.com/css/min-width-and-max-width-template/
id: 126
permalink: /css/min-width-and-max-width-template/
title: Min-width and Max-width template
---

Some problems seem to appear again and again, and one of them is **page width**. How wide should a site be? Should you adapt to 800px resolution? 1024px? Fully fluid with percentages? Perhaps elastic using em-units? There are lots to choose from. What I've found is that there's one solution that almost always works. You most probably already know it, but I thought it might be helpful for some to have a template you just copy and use.

The idea is to use a fluid width but limit it by using `min-width` and `max-width`. As with almost all CSS tricks, we do a little bit of hacking for Internet Explorer 6 (IE6). Link to the working [min/max template](/files/min-max-template/) is available, and an explanation follows.

I'm picking 760px as the minimum width. It fits within a maximized browser window on 800×600 resolution, accounting for scrollbars. Next we need some kind of max-width, and for this I'm going to pick 960px. I could probably go a bit higher but 960 is nicely divisible with a lot of numbers, 3, 4, 5, 6, 8, 10, 12, 15, and 16, making for nice columns (see [Gridding the 960](http://cameronmoll.com/archives/2006/12/gridding_the_960/)). Lastly we need some way to tell the browser to follow the width of the browser window when resizing, and width: 100% does that.

```css
#wrapper {
   min-width: 760px;
   max-width: 960px;
   width: 100%;
}
```

This assumes that you have a div with id wrapper around all your content.

The above works perfectly in both Firefox, IE7, Opera, and Safari. But (as usual) there's one culprit: IE6. To solve this I'm going to use the fact that IE allows for javascript execution inside CSS files. Have a look at the code below:

```css
#wrapper {
   width: 960px;
   width: expression(
      (document.documentElement.clientWidth > 962)? "960px" :
         (document.documentElement.clientWidth  762)? "760px" :
            "auto"
   );
   height: 1%;
}
```

First, the element gets a width by means of a IE expression(). The expression looks at the window width and if it's too wide it sets it to 960. It also limits it downwards to 760 pixels. At last we need to set trigger hasLayout on the element, and I usually use height: 1% for that (zoom: 1 works aswell).

> **Update**: Martin suggests we add a default width when IE have javascript turned off. Excellent, added it to the example. The default width will be applied in IE if javascript is turned off.

> **Update**: Matthjis notes that there is a [bug in IE6](http://www.cameronmoll.com/archives/000892.html) that causes it to freeze sometimes when using the same number for the conditional as for the max or min-value. Updated the code to reflect this.

(The expression is built up with two tertiary operators, so `(condition)? "true value": "false value";`, with a couple of numbers in it. Check it, it makes sense.)

The IE6-stuff above will of course not validate (and doesn't work in other browsers), so what we do is enclose it inside a conditional comment. The final [min-/max-width example](/files/min-max-template/) has all the code you need (I've added centering too), but you should of course move the code to an external file.

Happy hacking!
