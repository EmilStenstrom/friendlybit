---
author: Emil Stenström
categories:
- CSS
- Tutorial
date: 2006-01-13 00:21:39
guid: http://friendlybit.com/css/cross-browser-strategies-for-css/
id: 35
permalink: /css/cross-browser-strategies-for-css/
title: Cross browser CSS for your site
---

This article will go through some useful cross-browser CSS techniques I use to get my sites to look the same in several modern browsers. It's fairly easy to send out different versions of your site to different browsers. This should be avoided though since it will end up with you having to maintain the site as if it was in fact several. That defeats the whole purpose with standards, why are they even needed if you are adapting to the browsers instead? My opinion is that good cross-browser coding is to find the set of standards that _are_ supported and then use them.

## Validate your site {#validate}

Validation is a much debated area and many [Level 2 bosses](/css/levels-of-css-knowledge/) doubt that this procedure really helps. It does help though. It ensures that you didn't do any simple spelling errors, things that could be incredibly hard to find manually. A validator also checks for nesting errors (did you put a `<div>` inside of an anchor?) and other strange things like your character encoding. Information about each of the errors is available as links when they appear, just click on one and you're on your way to learn something new.

Validation is the simplest of my tricks to check. There are validators available for both [(X)HTML](http://validator.w3.org/) and [CSS](http://jigsaw.w3.org/css-validator/). Use them! Any errors that show up on those lists could be a potential cross-browser breaker so if you decide to ignore any of them you should be really sure about what you are doing. There are reasons why each one of all of the errors on the validation page show up, so validate, fix, validate, fix, validate.

## Stay in standards mode {#mode}

The next trick is not as obvious. Modern browsers have two rendering modes they use to display websites with: _Standards mode_ and _Quirks mode_. Standards mode is a rendering mode that is made to work according to the W3C specifications as closely as possible and Quirks mode is a bug ridden mode made for older sites. Why have a mode with bugs you ask? It's a way for browser makers to keep their users happy. When you do big changes to your rendering engine a lot of old sites relying on browser bugs will break. Some might think that this is a good thing, why should sites still work when they are poorly coded? If you think like that you have forgot about who the web is for. It's not a place for experts only, it's made for regular users, that is, _anyone_ with a browser. Those people need to see a working site if that's possible.

So a new browser is released with a more standards compliant rendering mode and pages start to break. This is a bad thing for users so browser makers decided to first identify pages that tried to follow the standards, and if they did, switch to the new and improved rendering mode. You will probably see why I recommend standards mode now. All browsers are trying to render things as similar to the specs as possible when in standards mode, while in quirks mode they keep all their old bugs just to help regular users.

So how do the browsers identify who's trying to follow standards and who's not? They use the _doctype_. If you're not familiar with doctypes, don't worry, they are easy to learn. A doctype is a tag on first line of your site file telling the browser what markup language you will be using. There are basically two doctypes you should select among:

**HTML 4.01 Strict (what I recommend)**

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```

**XHTML 1.0 Strict (without `<?xml ...>` on the line before)**

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```

Using any of these make sure the browser switches to standards mode and your design not fail because of that. Using a _strict_ doctype means that you will do your best to separate structure from design and the validator will give you errors in those areas. It's very useful. (Worth a small note is that the XHTML Transitional doctype also triggers standards mode, but while using transitional you don't get as many good validation checks so don't use that one anyways.)

There is one last catch one needs to talk about when dealing with doctypes and standards mode - **the doctype needs to be the first tag in the document**. If you put any HTML comments or strange characters before it <acronym title="Internet Explorer">IE</acronym> will go crazy and switch to quirks mode. This has cause many developers countless hours of trying to fix things. Just don't do it!

## Remove default styling of elements {#default}

Another cause of many web developers screaming in the night is the default CSS that is applied to elements. If you don't use any CSS at all on your page elements will still have a certain look. Headers will be larger than text paragraphs and blockquotes will have padding. Sizes of text is something that is pretty similar across browsers but something that's not is padding and margins. Let me give you an example: With no styling an `<ul>` gets a padding in Firefox but a margin in IE. Solution? Set either the margin or padding to zero and set the other one to the indentation you want. You need to somehow remove the default browset styles.

These kinds of problems take up a lot of development time if not handled nicely. "Do definition lists in Opera have padding or margin?". "What about second level headers in IE 6?". Two schools of thought have evolved to handling this. The first one tells you to start by resetting _all_ margins to their defaults at the top of you CSS file. This can easily be done by typing in `* { margin: 0; padding: 0; }`, * being a [universal selector](http://css.maxdesign.com.au/selectutorial/selectors_universal.htm) that applies the same rules to _all_ elements.

Problem solved right? That's where the second school of thought comes in. They argue that too many default margins are reset. Why should we mess with users form fields, rendering them hard to use unless they are set to good values again? Instead you could just reset those elements that have differences, and leave the rest untouched. This is quite a lot of work to get right so Faruk Ate? built a "starting css" template that you can easily include in your head. Personally I prefer the *-method, but try both and decide for yourself.

## Browser bugs {#bugs}

This is the area where CSS gets hard. Even though browser makers work their asses off to follow standards they sometimes don't reach their goals. This leaves us webmasters with bugs that when fixed triggers new bugs, either in the same or another browser. It can easily get real dirty.

One of the worst browsers (that is widely in use) is Microsoft's Internet Explorer, version 6. Some claim they have about 80% of the browser market so it's not a browser you can just ignore. IE was a good browser when it was first released but by today's standards it's certainly not. No other browser caused me more pain while building the design of this page. Its shortcomings get painfully clear when it comes to rendering complex CSS layouts.

How do you handle these bugs then? The easiest (and fastest) way is not solving it yourself but reading up on someone else's solution. "Holly 'n John" have gathered the most frequent bugs on their page [Explorer Exposed!](http://positioniseverything.net/explorer.html). They give you examples of how to detect the bug, how it works and why (sometimes) and most importantly how to solve it. Sometimes the solution is just setting `position: relative;` or `display: inline;` on some element and sometimes you have to resort to strange code. The point here is that if your bug is on that page; don't waste time trying to figure it out yourself. Learn that list by heart.

So what do you do if your bug isn't on the list? You start by googling for a solution of course. Googling takes a few minutes compared to the hour you probably need to hunt it down. Don't underestimate this step.

If you don't find it somewhere you need to hunt it down yourself. Do this by making a copy of your page and then removing as much code as you can while keeping the bug. Then find out exactly what line (or lines) of code that causes it and finally try to find another way of doing what triggers it. This is much better than just throwing in hacks, you keep your code maintainable and you learn a lot more useful stuff than if you were throwing in nonsense code from the beginning.

If you for some reason do not manage to solve the bug with the above technique you either rethink what you are doing (not likely) or you go get your arsenal of hacks. Make sure the hacks are valid code. The one I use for IE when nothing else works is the "* html" hack. You use it but writing like this: `* html #element { code; }`. That selector selects all tags that have the child html that have the child #element. But "html" is the topmost element in the hierarchy so nothing is selected, unless IE can choose of course. The code gets applied in IE only. Note that it is perfectly valid CSS, it just doesn't select anything. Remember: hacks are your _last resort_ when nothing else works.

**Update 18 Jan:** [Richard](#comment-51) in the comments point out that you can also use [conditional comments](http://www.quirksmode.org/css/condcom.html) to serve a certain `<style> or <link>` to different versions of IE. The "* html"-hack will not work in the comming IE7. Thanks Richard.

&nbsp;

I hope you found something useful in this article that you can use when you get cross-browser CSS problems. I have now told you what steps I use, did I miss something? Do you do something differently?
