---
id: 108
title: Forgotten HTML elements?
date: 2006-12-04T19:59:26
author: Emil Stenström
layout: post
guid: http://friendlybit.com/html/forgotten-html-elements/
permalink: /html/forgotten-html-elements/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "207160331"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - HTML
---
HTML has existed for a long time now with five released versions ([[1]](http://www.w3.org/MarkUp/draft-ietf-iiir-html-01.txt "HTML 1 draft"), [[2]](http://www.w3.org/MarkUp/html-spec/html-spec_toc.html "HTML 2 Specification"), [[3.0]](http://www.w3.org/MarkUp/html3/Contents.html "HTML 3.0 Specification"), [[3.2]](http://www.w3.org/TR/REC-html32 "HTML 3.2 Specification"), [[4.01]](http://www.w3.org/TR/html401/ "HTML 4.01 Specification")). Some very interesting elements have existed in previous versions and I went on a little journey back in time to find and document them. Off we go.

Robert Nyman had a little contest a couple of weeks ago where he gave away an iPod to the person that [best motivated why he/she liked a certain HTML element](http://www.robertnyman.com/2006/10/01/win-a-1-gb-ipod-shuffle-name-your-favorite-html-element/). People gave a lot of good explanations and pretty much the whole HTML 4 specification was covered (even blink!). Knowing that all of HTML 4 was taken, and that he didn't specify what version of HTML to choose, I started searching through the older specs. I was soon stuck in HTML 3.0, and continued reading long after I had found my favorite…

`<note>` was (and is) my favorite. [Specified in HTML 3.0](http://www.w3.org/MarkUp/html3/notes.html "Specification of notes in HTML 3.0") as an element that's there for all kinds of little notes; a sidetrack to something you are currently speaking about, or perhaps some "operation failed" message. They even go as far as to recommend a few default class names: warning, notice, and error. Nice! Wouldn't this be nice in the current AJAX/Web 2.0 world where everything acts like an application? Why not use note for all those little messages? I could certainly see the use for something like that. Unlike me, the HTML 4 spec writers didn't see any use of such an element, and note was not included in HTML 4.

`<fn>`, also [from HTML 3.0](http://www.w3.org/MarkUp/html3/footnotes.html "Specification of footnotes in HTML 3.0"), is up next. Most of the "new" HTML 3.0 elements are aimed at different things that fit into the document metaphor, like research papers and books. So is the next one: fn is short for footnote, a name that clearly defines its purpose. It’s similar to the note element but meant for smaller notes. If you are trying to mimic a book, with references to somewhat disconnected information about something, this one is perfect. But why not use it for things like fancy tooltips while we're at it? Sadly, this element got kicked out of HTML 4.

`<isindex>` is a bit different from the previous elements. It's defined as far back as [in HTML 1](http://www.w3.org/MarkUp/draft-ietf-iiir-html-01.txt "Specification of isindex in HTML 1"), and was [included](http://www.w3.org/MarkUp/html3/dochead.html "Specification of isindex in HTML 3.2") all the way to HTML 3.2. It was meant to represent that a certain page could be searched, but gave the user agent the option of how to get the query from the user. If put in the head of the document the user agent should prompt the user on load. If put in the body it should behave like one of those "search this page" form fields we are used to from Google.com. Needless to say, the exact same thing can be accomplished with a snippet of javascript or a HTML form. No need to let this one clutter the spec. Good removal.

`<banner>` is another half-breed, [specified in HTML 3.0](http://www.w3.org/MarkUp/html3/banners.html "Specification of banner in HTML 3.0"). It's meant for elements which should be set at a fixed position on the page, much like how position: fixed works in modern browsers. From the name you could think that this is an element you would want to block to get rid of ads, but the HTML 3.0 spec mentions that navigation inside the banner element is OK too. I believe the problem with this element is twofold: first, if it was meant for banners only, why should you want to put you advertisement inside it? That would just mean that it would be easier to block, and I'm sure most advertisers would dislike that. Second, if it's meant for "information that shouldn't be scrolled", then what's it doing in the HTML? That's certainly style, and should be in the CSS as well. Another good removal.

`<figure>` actually has some uses (Also [from HTML 3.0](http://www.w3.org/MarkUp/html3/figures.html "Specification of figure in HTMl 3.0")). It's meant for all types of media, and has built-in support for alternative content. It has ways to add image maps by using ordinary links and it has support for figure captions. Yes, this is a catch-all for any data that's not in text-format. Have a look at the [figure examples in the specification](http://www.w3.org/MarkUp/html3/figures.html), looks pretty nice doesn't it? Why was this removed? My guess is that the `<object>` element took its place (see [object in HTML 4.01](http://www.w3.org/TR/html4/struct/objects.html#edef-OBJECT)). Object lets you specify more information about the "figures" its meant for, but does not limit itself to images. Yeah, there were reasons to remove figure from the spec too.

Well, that's all from friendly bit. Feel free to read through the specs in search for other elements that I've missed and post your findings in the comments. Perhaps [HTML 5](http://www.whatwg.org/specs/web-apps/current-work/) will even revive some of the old elements?
