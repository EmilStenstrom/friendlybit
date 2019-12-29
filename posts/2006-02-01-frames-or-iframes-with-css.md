---
author: Emil Stenström
categories:
- CSS
- HTML
date: 2006-02-01 23:50:59
guid: http://friendlybit.com/css/frames-or-iframes-with-css/
id: 43
permalink: /css/frames-or-iframes-with-css/
title: Frames or Iframes with CSS
---

A frequent request from people new to CSS is trying to get a behaviour similar to frames while only using CSS. Many have read that frames have a lot of problems but do not know much more than that. This article will try to explain why frames are bad and what to do about it.

  * [Why are traditional frames such a bad thing?](#why)
  * [Getting a scrollbar on any element using CSS](#scrollbar)
  * [Mimicking traditional frames](#traditional)

> **Update**: I've updated this technique [using position: fixed in a new article](/css/position-fixed-css-templates/), have a look at those templates instead! (Although this article is still good for background information).

## Why are traditional frames such a bad thing? {#why}

Let me start by just listing a few bad things about frames.

  * **Prevents users from bookmarking** the exact page they're on. Instead the bookmark will lead to the frameset. This is clearly not a good choice for larger sites where finding a certain page might be a problem, but even users on smaller sites might find it annoying. I do.
  * **Poor support by some parsers** leads to problems. Many screen readers, mobile phones, and search engines have problems parsing frames. This means some of your users might miss out on your content.
  * **Content order** problems. Just like with tables, frames give screen readers problems when deciding which order to read the frames. If it reads a 2×2 frameset will not know whether to read the content like two rows or like two columns. The order might be important for understanding the content and frames has nothing built-in to help with that.
  * **Search engines** might split the ranking up on the different pages. I just discovered this by looking at one of my old pages (no, I won't show it, it's terrible :). There, the [PageRank](http://www.webworkshop.net/pagerank.html) has been split up on the framed pages and the frameset has no rank whatsoever.
  * **Invalid code**. If you're using separate frames for navigation and content your links will need the `target` attribute to make links from the navigation frame open in the content frame. That attribute is not supported when using a strict doctype so you will have to use transitional. The doctype won't matter if you want to get rid of borders cross-browser though, to do that you need invalid markup.
  * **Printing is a problem**. How should the different frames be handled while printing? There's no good solution to this.

People that are good with javascript sometimes say they like frames because they make it possible to save information about the user even though the user clicks links. A variable can be saved in a frame and be accessible to the other frames even after they are reloaded. Another pro-frames reason frequently heard is that it saves overhead since not the entire page gets reloaded.

Personally I think that the first is a bad reason to use frames. Using server side scripting to save session info is much more robust since that will mean the applications still work if the user reloads the page. The other reason of only reloading a part of the page is nowadays done by using javascript together with XMLHttp (some like to call it AJAX). To me, the bad parts of frames greatly weigh over, even for applications.

## Getting a scrollbar on any element using CSS {#scrollbar}

Aside from all of the above frames are not structure. Think about it. When working with frames you define that you want a couple of rows and columns, which should scroll and which shouldn't, and which should have borders. These are things that many of us would never dream of doing with tables but some still use frames like that.

Instead we should define that kind of design in our CSS files. How? By using a few lines of code you can easily limit any element to a certain width/height and let it scroll if the content overflows that size.

```html
<p>Here's some sample content that I would like to scroll</p>
```

```css
p {
   width: 200px;
   height: 80px;
   overflow: auto;
}
```

It's easy, you're saying: "limit the paragraph to this size and give the box a scrollbar if the content gets too big" (Other valid values for overflow are "hidden" and "scroll". The former just cuts everything that sticks out, that latter adds the scrollbars even if they're not needed).

The above method works when you want something that's similar to iframes but it doesn't work right away for traditional frames. Those usually span the whole width or height of the page and leave the rest of the page scrolling. But what stops us from taking any element and stretching and placing it like a frame? Nothing. Let's do it.

## Mimicking traditional frames {#traditional}

  * [Two columns with left fixed](/files/frames/columns.html)
  * [Two columns with right fixed](/files/frames/columns_navright.html)
  * [Two rows with a fixed top](/files/frames/rows.html)

The idea here is to use divisions to group our content. Then position those divisions as if they where frames and limit their site and set `overflow: auto` like we did above. Frames use the syntax `cols="200,*"` to say that the first column should be 200px wide and the second one "cover what's left". The second part is a bit harder to do with CSS.

There's no way to say 100%-200px but there's a trick we can use: floats push the content away. So if we set a width on the left block to 200px and float it left, the other block will be as wide as possible (default for block level elements) but it's content will be pushed 200px to the right. Here's an example of [two columns with a fixed left](/files/frames/columns.html) in action. By just changing float: left; on navigation to float: right; we get the other example: [Two columns with the right one fixed](/files/frames/columns_navright.html).

(Technical note: we don't need to add any margin-left since [overflow: auto; clears](http://www.mezzoblue.com/archives/2005/03/03/clearance/) too).

The above works well for columns but what if we need rows instead? When using frames we specify `rows="100,*"` and as I said this is not possible directly with CSS. We can't use the above trick either since we're dealing with height here. Setting `height: 100%` will just make it as high as the window, leaving no space for the other row. The solution here is to cheat a bit. If we make the first column 100px high and the lower one 100% high but then remove the first one from the flow we will be pretty close. The first row will be on top of the other one but that can easily be solved by adding a padding-top the same height as the first row.

We're almost there now, one last thing: the latter row scrolls on top of the first one because of the order in the source (latter elements stack on top of earlier ones). So what we do is force the first one on top with position: relative. This solves the problem except that it also covers the scrollbar now. An easy (and ugly fix) is to add a margin-left of 16px to the top column making the scrollbar visible again. Browsers seem to use the same scrollbar width so that's it, an [example of frame rows](/files/frames/rows.html) using CSS.

I've tested this in IE 6, FF 1.5 and Opera 8.5 on WinXP and it seems to work fine. Broken in any other browsers? Let me know through the comments.

When looking at this I see that this is also a good way to mimick blocks that are `position: fixed`, something that doesn't work in IE. This method might be good in a situation where you need that one.
