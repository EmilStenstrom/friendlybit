---
author: Emil Stenström
categories:
- Django
- HTML
date: 2008-11-29 15:18:49
guid: http://friendlybit.com/?p=320
id: 320
permalink: /html/html-includes/
title: HTML includes
---

One of the first questions beginners ask when starting to learn HTML is [how to do includes](http://www.google.com/search?q=include+html). They seldom know that includes is what they are asking about, but instead feels bad when having to copy and paste that same menu HTML each time they want a new page. "Do I have to type the same thing over and over?".

After asking friends how to solve the problem they get the answer that they now have to learn PHP. Or ASP. Or JSP. Or some other strange language they don't need. And install this thing here, and that thing there. What does your server host support? Oh, no, you need to configure stuff better. No, that setting is insecure… You know the drill, I'm sure you've walked someone through it sometime.

So, a way to include a piece of HTML into a random page would clearly benefit beginners learning HTML. But that's not all:

  * **Browsers would be able to cache** components of a page, and therefor load new pages using common components faster.
  * **Less work learning new template languages** just to find that language X does not have a way to include things.
  * Possible to learn componentization by **looking at existing sites** and learn from them. This is an area we need to be better in.
  * **Easy to make fallbacks** by linking directly to the corresponding HTML snippet.

So, how would this be implemented? We need a tag that acts as a kind of include, so what about `<object>`? Just point to the HTML file you want and voilá, it gets included. Since this is HTML it would work exactly the same across all server-side languages.

Luckily, this is already in the HTML5 spec. At the [bottom of the object specification](http://www.whatwg.org/specs/web-apps/current-work/#the-object-element). Interestingly, I found it **after** writing this article… Great minds think alike :)

> In this example, an HTML page is embedded in another using the [object](http://www.whatwg.org/specs/web-apps/current-work/#the-object-element) element.

```html
<figure>
    <object data="clock.html"></object>
    <figcaption>My HTML Clock</figcaption>
</figure>
```

Good! And it even seems to work in current browsers ([Thanks Siegfried](#comment-31225)). I've tested it in Firefox, Opera, and Safari, and it works the same in all of them. Internet Explorer 6, 7, 8 (beta 2) just ignores it altogether.

The problem is, the current implementation is to handle them just like iframes. And there's of course lots of problems with that approach:

  * Currently, an object element without a height and width gets rendered as a **300 x 150 pixel block**. There is no reason whatsoever to do this when including HTML. This must change for this to be usable.
  * The included HTML needs to be **stylable** with the CSS rules on the page it's included from. Currently, this does not work, included HTML is treated as an iframe. Must be changed if this is to be usable.
  * Are HTML components full HTML pages? Do they include a doctype and a `<head>`, and do those get included? I assume only HTML **inside `<body>` gets included** in the new page. No CSS. No JS linked to in `<head>`.
  * Clicking links inside included HTML should be handled as if the HTML was on the current page. This follows the same concept as if the HTML was included in the server side, and is needed if this is ever going to be used for a menu.

So, what do you think, is this a good idea? Personally, I'm hoping more concepts from template languages start to move into HTML.

> **Update**: Thanks to the comments (thanks zcorpan) I now have found exactly the above in HTML5. It's called `<iframe seamless>`. It meets all the points in my list, and I'm now really looking forward to the first implementation.
