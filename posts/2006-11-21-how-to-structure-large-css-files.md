---
author: Emil Stenström
categories:
- CSS
date: 2006-11-21 21:55:47
guid: http://friendlybit.com/css/how-to-structure-large-css-files/
id: 106
permalink: /css/how-to-structure-large-css-files/
title: How to structure large CSS files
---

Many methods exist to structure your CSS. This article tries to describe the method I use. I call it the "Tree method", since it structures the CSS like… that's right, a tree structure. I want to stress that it isn’t my invention; I just describe and give reasons for its rules.

Everyone that has built a bigger site has had to deal with the mess CSS so easily become. There are ids and classes all over the place, and to find where a certain class is defined you usually need to use some search feature in your editor. Matching the other way, from the CSS to the HTML is even harder; you don't even know _what file_ a certain class is defined in. It’s a mess.

The Tree method tries to structure the CSS into logical blocks; blocks taken from the HTML. It also aims to be easy to understand for anyone. No secret codes or difficult ordering schemes.

  * [Order your selectors like the HTML](#order)
  * [Always use the "full path" to elements](#full)
  * [Indent your code cleverly](#indent)
  * [Each declaration on its own line](#own)
  * [… in alphabetic order](#alpha)

## Order your selectors like the HTML {#order}

One of the problems of mapping between the HTML and the CSS is that they usually differ in structure. The HTML is (if you’re lucky) structured like a convenient semantical tree while the CSS often is ordered by something random like fonts, colors, and positioning.

To make moving between the two worlds easier we want to make them as similar as possible. Is the HTML divided into header, content, and footer? Then make sure that's the three major parts of your CSS as well. Have you put the navigation above your header in the HTML? Then order it like that in the CSS as well! Any other structure makes moving from the HTML to the CSS much harder. You might be able to find all font manipulations in one part of the CSS, but only if you know that this particular developer uses that exact scheme. No, let’s keep it simple.

Here's a simple example where we just order the selectors:

```css
#header { ... }
h1 { ... }
h2 { ... }
#content { ... }
p { ... }
em { ... }
strong { ... }
```

When grouping several styles into one definition I just put the group above both of their specific styles. `#header, #content` comes before both #header and #content.

## Always use the "full path" to elements {#full}

The above is very easy to get an overview of, but the experienced developer knows that very few sites are that easy. Something you often want is a way to define different styles to different parts of a page. Let’s say you want green links in the navigation, but want to keep them blue everywhere else.

For this we use sub selectors. The selector `#navigation a` lets you give all links inside your navigation another look. But let’s take that further. Why not always write the _full path_ to your elements? Why not use `#navigation ul li a` instead? Doing this gives a developer looking at your code a lot of information about how the HTML and CSS belongs together.

Lets add that to the previous example:

```css
#header { ... }
#header h1 { ... }
#header h2 { ... }
#content { ... }
#content p { ... }
#content p em { ... }
#content p strong { ... }
```

This does change the meaning from before. Before we selected all the level two headers; now we only select headers inside of the header division. Extending each selector with a "path" has made our CSS rules more specific, and specific means more control for you.

This also makes for fewer new ids and classes; just specify the path to an element instead of adding a class for it. Don't add a new class or id unless you really need to.

We still have the issue of "common styles"; styles that we want to apply to elements in different parts of the tree. Since they should be applied to all elements they don’t fit in the tree structure we've built. Instead we make a section in the beginning of the file (or a separate) with just "general styles". Don't add rules to this section if you only use them once in the document, you want as much of your code to be in "the tree" as possible.

## Indent your code cleverly {#indent}

To make the code even easier to understand I always add indentation (for those that don't know that word: it means spacing in front of blocks of text). Indenting makes the tree structure we're trying to build even clearer, you can easily find the major sections and dig down from there.

Lets add indention to you our example too:

```css
#header { ... }
   #header h1 { ... }
   #header h2 { ... }
#content { ... }
   #content p { ... }
      #content p em { ... }
      #content p strong { ... }
```

Don't take indentation too far. If you're styling tables and using thead in the markup, but don't change the style of it, you can skip that indentation level. Double indention just for the sake of it is just a waste of space.

## Special case: Templating

We also need to deal with rules that only appear on some of our pages. Perhaps we want the home page to look somewhat different than the sub pages? We solve this by giving an id or class to the body element. Doing this lets me specify styles for just one specific page, and setting the id or class on body makes me able to change anything in the document based on that.

These page specific styles need a place in the tree too. Here I tend to break from the above scheme and put them together with the style they change. So `body#page_home #header h1` is one step below `#header h1` in the tree. That makes it easier to see all styles for a certain element, instead of scrolling back and fourth (like you need to do if you don't remember your general styles). Keep your templates together with the style they change instead of completely separate.

If you want bigger changes, perhaps a totally different look on some pages, there's no reason to group things according to the scheme above. Move them to a separate file instead.

## Each declaration on its own line {#own}

Indentation combined with full paths makes some lines rather long. This means that putting all declarations on one line will force you to scroll horizontally, something we already avoid on our sites. The simplest way to prevent horizontal scrolling is to use one declaration per line, so that's what the tree method uses.

## … in alphabetic order {#alpha}

Grouping of properties is another issue. I've seen grouping schemes based on all sorts of things; from splitting things into "positioning", colors, and fonts, to people adding their properties completely randomly. I've chosen to just order them alphabetically. It's one of the few methods that bring some order while still being simple enough. I've seen total beginners do this by themselves; something I believe is a good argument for it. It's intuitive.

A simple example to illustrate:

```css
#content {
  color: Blue;
  font: 3.4em Arial, sans-serif;
  margin: 0.5em;
}
```

One complaint I've heard on this method is that it splits up things that belong together. People tend to keep `position: absolute` and `left: 0` together, just to name one such pairing. It annoyed me at first too, but declaration blocks rarely contain more than 10 declarations, and the alphabetic order still makes them easy to find. Also, why handle position different than float and margin?

&nbsp;

That's it! By following a few simple rules you can get a CSS-file that's easier to overview, a file that you proudly can give away to the next developer. I can praise its existence all day, but you're the judge of whether it works or not. Why not give it a try in your next project?

> **Update**: Maurice van Creij writes in and says that he's using the same method. A good way to get started is to generate a CSS file from the HTML. He has written a javascript that does just that. Nice! Try generating a CSS file.

> **Update**: Another part structuring your CSS is making sure you don't load too much. I wrote an article previously about [combining static and dynamic CSS](/css/static-and-dynamic-css-combined/).

> **Update**: This article got digged to the frontpage. There's a lot of good comments there (but as usual pretty harsh language).
