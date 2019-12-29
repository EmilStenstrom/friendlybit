---
author: Emil Stenström
categories:
- CSS
date: 2006-11-27 22:04:42
guid: http://friendlybit.com/css/ie6-bug-ignored-selector-hover-bug/
id: 107
permalink: /css/ie6-bug-ignored-selector-hover-bug/
title: 'IE6 bug: Ignored selector hover bug'
---

IE6 bugs seem to pop up all over the place recently. This one is a very small one, but it might affect people that are building tabbed navigation or CSS-based tooltips. The problem is that IE6 ignores selectors in the form of `a:hover [selector]`.

## The problem

Say you want to build a tabbed navigation where tabs move slightly when you hover them (that was how I found the bug). Since you want to reuse the images for the tabs you divide them into two pieces (according to [sliding doors](http://alistapart.com/articles/slidingdoors/)). But to do that you need two elements that react on hover. One can be the link but you need one more. So you add a nested span and your code looks like this:

```html
<ul>
    <li><a href="url1"><span>Home</span></a></li>
    <li><a href="url2"><span>Contact</span></a></li>
    <li><a href="url3"><span>About</span></a></li>
</ul>
```

You cleverly position the span and the link, and add a couple of rules to your stylesheet. You also want the text to move slightly, just like the background, so you add some padding.

```css
a:hover {
   background: url(...) no-repeat left top;
}
a span {
   display: block;
}
a:hover span {
   background: url(...) no-repeat right top;
   padding-top: 10px;
}
```

You look at the site in Firefox, Opera, Safari, and IE7 and everything works just fine. But what's that? Why doesn't the text move in IE6? You start removing CSS and HTML to pinpoint the problem and end up with a [very small testcase with the bug intact](/files/ie6hoverpadding/ "testcase of the ignored selector hover bug").

## The solution

Looking at the testcase I was just confused. I was pretty sure I'd seen IE6 do selectors like that before, but why didn't it work now? [HasLayout](http://www.satzansatz.de/cssd/onhavinglayout.html) and the other usual IE6 fixes didn't work.

I loaded up my IM client and started asking people if they knew anything. [Simon](http://simon.html5.org) noted that everything started working when you changed the selector to `a:hover, a:hover span { ... }`. Ok, so setting and then resetting that rule seemed to work. Some further experimenting revealed that just setting **any** padding to a:hover (setting it to zero worked well) also solved the problem.

That was good enough, an extra `a:hover { padding-top: 0 }`. So here's the [testcase with the bug solved](/files/ie6hoverpadding/fixed.html). The bug is apparently fixed in IE7.
