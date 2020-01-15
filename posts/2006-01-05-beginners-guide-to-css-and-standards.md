---
author: Emil Stenström
categories:
- CSS
- HTML
- Tutorial
date: 2006-01-05 18:11:00
guid: http://friendlybit.com/css/beginners-guide-to-css-and-standards/
id: 27
permalink: /css/beginners-guide-to-css-and-standards/
title: Beginner’s guide to CSS
---

In the chat channel I'm in, I get to talk to people on a daily basis that have never used <acronym title="Cascading StyleSheets">CSS</acronym> before, or are at the very beginning of learning it.. This article teaches all the basics you need to make your first CSS powered website. It is aimed at people that know a little <acronym title="HyperText Markup Language">HTML</acronym>, and maybe have made a few websites themselves. Let's get started.

## What is CSS? {#what}

CSS is a language that adds style (colors, images, borders, margins…) to your site. It's really that simple. CSS is not used to put any content on your site, it's just there to take the content you have and make it pretty. First thing you do is link a CSS-file to your HTML document. Do this by adding this line:


```html
<link rel="stylesheet" href="style.css" type="text/css">
```

The line should be placed in between your `<head>` tags. If you have several pages you could add the exact same line to all of them and they will all use the same stylesheet, but more about that later. Let's look inside the file "style.css" we just linked to.

```css
h1 {
   font-size: 40px;
   height: 200px;
}
.warning {
   color: red;
   font-weight: bold;
}
#footer {
   background-color: gray;
}
```

You have three <dfn>selectors</dfn> up there, `h1`, `.warning` and `#footer`. A selector simply points to somewhere in your HTML document. It can be built in many ways and can be a combination of the following building blocks:

  * Element
  * Class
  * Id

I'm going to go through all three of them and explain what they do.

An <dfn>element</dfn> points at a HTML-tag somewhere on your page. In the example above we want to style the `<h1>`-tag. Note that using an element like that affects all tags with that name, so using `p { margin-left: 100px; }` gives _all_ `p`-tags a left-margin.

Using a <dfn>class</dfn> is just as simple. When writing `.your_class` you style all tags with a class with the name "your_class". In the example above we have `.warning` which will style e.g. `<div class="warning">` and `<em class="warning">`, that is, any element with the class warning. Classes are used when you want to style just a few of your tags in a way, perhaps you want some of your links red? Add a class to all those links.

You need one more building block: the <dfn>id</dfn>. This time you style an element with the attribute "id" set to the id you have chosen. Ids work exactly like classes except for one thing; you can only have one id with a certain name in each of your HTML documents. In the example above we style `<div id="footer">`. If you look at the example it does make sense: a HTML document may contain several warnings but only one footer. Ids should be used when you want to style just one specific tag.

Using those three building blocks will take you far but when you get to more advanced layouts you might want to combine the building blocks into more advanced selectors. Just to give you two examples of what you can do: `em.warning` to style only those `<em>`-tags with the class `.warning` set. You can also use `#footer a` to style only the links that are nested inside the tag with id "footer". Pretty nice, isn't it?

I could go on forever about the advanced uses of selectors but this is a beginner tutorial so I won't. If you want all the finer details, go have a look at the excellent [Maxdesigns Selectutorial](http://css.maxdesign.com.au/selectutorial/).

Let's go on explaining the code above. Each of the selectors has a set of <dfn>declarations</dfn> tied to them. Each declaration has a <dfn>property</dfn>, describing what we want to change and a <dfn>value</dfn>, what we should change it to. Too many terms there? Are you still with me? Let me explain with an example: `a { color: Blue; font-size: 3em; }`. You have the <dfn>selector</dfn> `a` there, so all links in your document will be styled. We have two <dfn>declarations</dfn>: `color: Blue` and `font-size: 3em;`. Lastly each declaration consists of two parts: the <dfn>property</dfn> `color` and the <dfn>value</dfn> `Blue`. Phew! Well done for making it this far. The terms above are good to know since it gives you a way to talk about your CSS. If you join a CSS-channel asking for help with your code and they tell you "You have an error in your a-selector in the second declaration" you know exactly where! Right? :)

Now you will probably ask what properties there are. You have seen `font-size` and `color` but what else is there? The answer is that there are a _LOT_ of things you can style and play with. Additionally (close to) all tags are equal in CSS, so you can set e.g. borders and colors of _any_ element just like you could with a table if you used only HTML. Starting to see the possibilities?

I won't go through all the properties here, it would just bore you to death. Instead I'll point you to another great resource: [w3schools section about CSS](http://www.w3schools.com/css/). Just select one of the menu options to the left to start exploring what CSS can do.

But don't you leave me all alone here, there is more to learn! Next we will talk about good and bad coding and there will be a lot of colorful examples for you. Sounds good?

## CSS is all about separation {#separation}

One of the least followed parts of CSS is the very idea behind it, the idea of separation of content and design. The idea here is that all sites contain two major parts, the content: all your articles, text and photos and the design: rounded corners, colors and effects. Usually those two are made in different parts of a webpage's lifetime. The design is determined at the beginning and then you start filling it with content and keep the design fixed. So if you just want to add content to your site you don't want to be forced to mess around with the design, do you? The same thing is true the other way around, if you decide on a redesign, why should you have to mess around with the content, making sure it fits in the new layout?

In CSS you just add the nifty `<link>`-tag I've told you about to the head of your HTML document and you have created a link to your design. In the HTML document you put content only, and that link of yours makes sure it looks right. You can also use the exact same link on many of your pages, giving them all of them the same design. You want to add content? Just write a plain HTML document and think about marking things up like "header" instead of "big blue header" and use CSS to make _all_ headers look the way you want!

This is a different way of thinking about webpages, and it's something that took a while for me to understand. To help you I have written some examples of good and bad coding. What's wrong with this?

```html {.incorrect}
<font size="3">Welcome to my page</font>
```

Comment: The font-tag is design and design shouldn't be in the HTML document. All design should be in the CSS-file! Instead do this:

In the HTML:
```html {.correct}
<h1>Welcome to my page</h1>
```

In the CSS:

```css {.correct}
h1 { font-size: 2em; }
```

One more example:

```html {.incorrect}
<b>An error occurred</b>
```

Comment: This looks right doesn't it? But if you look up what `<b>` stands for you quickly find *bold*. But bold is certainly design, so it still doesn't belong in the HTML document. A better choice is `<em>` that stands for *emphasis* or simply "this piece of text is important". So instead of saying "this text looks like this" you are saying "this text is important" and you let the looks be decided by the CSS. Seems like a minor change, but it illustrates how to select your tags. Use this instead:

In the HTML:

```html {.correct}
<em>An error occured</em>
```

In the CSS:

```css {.correct}
em {
   font-weight: bold;
   color: Red;
}
```

One last example:

```html {.incorrect}
<table>
  <tr>
    <td><a href="">first link</a></td>
  </tr>
  <tr>
    <td><a href="">second link</a></td>
  </tr>
  ...
</table>
```

Comment: Lots of people format their navigation menu like the above example. But is a navigation menu really a table? If you look up the definition of a table you see that it's made for tabular data, the same kind of data you would put in an Excel sheet. The example has only one column of data, and no headers… Some people state that they use tables because that means that they can get borders and a background color on their navigation, but that's exactly what your CSS file is for (not the HTML document). So what should we do? Look deep in the list of [HTML elements at w3schools](http://www.w3schools.com/html/) and you'll find something called an unordered list, `<ul>`. Have a look at this:

In the HTML:

```html {.correct}
<ul>
  <li><a href="">first link</a></li>
  <li><a href="">second link</a></li>
  ...
</ul>
```

In the CSS:

```css {.correct}
li {
   border: 1px solid;
}
```

This is probably a different way of thinking about HTML than you're used to but trust me, when you've worked with it for a while you'll see the power of it. Not only does this way of coding give you a more logical structure, there is also proof that this improves your ranking in search engines and makes it easier for accessibility devices to read your site. This way of designing is great.

Next we will build a simple HTML template to use as a start when building a new page. Like to see it?

## Building a standards based HTML template

We have talked a lot about the theory behind CSS and HTML working together to form a site with good structure that is separated from the design. But the first parts of building pages are always the same, you type

```html
<!doctype html>
<html>
  <body>
    <div id="header">
       <!-- Header here! -->
    </div>
    <div id="navigation">
      <!-- Navigaiton here! -->
    </div>
    <div id="content">
      <!-- Content here -->
    </div>
  </body>
</html>
```

Ok, there might be some new stuff there so let's go through the lines one by one. First we state this document's doctype: what language we use. You might have heard of XHTML, another similar web language, but for a first page we don't need the features that gives us access to, keep it simple, just go with HTML. Also, the `<!doctype html>` above sets the document to use _Strict_ HTML. To understand that you need to know that there are two kinds of rendering in a browser. One that follows the standards set up by the [W3C](http://www.w3c.org), <dfn>"standards mode"</dfn>, and one for older pages, called <dfn>"quirks mode"</dfn>. Standards mode is what we want to use. It makes the pages render (almost) the same in modern browsers and it frees us from being dependent on a specific browser, we'll just follow the standard. Quirks mode is something of a bug mode. It's there to keep old pages looking the same as they did before browsers started trying to follow the standards and is therefore intentionally filled with strange bugs. A browser determines which rendering mode to use based on what doctype we use, so make sure you use the right one!

Ok. That's a lot of explaining for a single line of code, I'll be swifter now, next line. You have probably written `<html>` before in the beginning of your documents. My line is almost like that except that I have added `lang="en"` there. That line tells the browser which language we will use. Why does it matter what language we use? you ask… Well, there is assistive technology that read webpages to people out loud called screen readers. Those _have to_ know what language it is to be able to pronounce the words. It's so easy for you to add those few characters so why not do it? If you don't plan on making an English page you can find your own language code by visiting [WAIs Language Codes](http://www.w3.org/WAI/ER/IG/ert/iso639.htm#2letter) and check out the two-letter names there (_Note:_ language codes are in lowercase).

Next we have the _head_ of the document. The head contains a some of meta-information about the page, like character encoding, title and what stylesheet (CSS file) to use. The charset there is the trickiest one so let's take that first. There are a lot of different letters in a language. When computers where first constructed the engineers only thought about the American/English language, they didn't even think about the swedish letters å, ä, ö or the deutsch umlaut ü or what about the &-sign? There are a lot of characters and at first there was no general consensus on how to handle them. Then someone came up with the smart idea of grouping them into _sets_, groups of characters that are used in certain parts of the world. So, what the meta-tag does is simply to state: "This person wants to input western characters (latin-1 characters)", and this tells the browser what character set to use. A more genaral approach is to use the utf-8 character set but that quickly gets tricky. Finally we have a text/html there that simply tells the server to send the document as a HTML, not like an image or something like that. The `<title>` and `<link>` you should be familiar with, if not, google it :)

That was a lot of info on just a few lines of code, I hope I didn't give the impression that this stuff is hard, because it's not. To use the stuff above you just copy and paste it and start filling it with content.

The body of the document consists of a bunch of divisions, let's add some content to them:

<div id="semantics"></div>

```html
...
<div id="header">
  <h1>The name of this page</h1>
</div>
<div id="navigation">
  <h2>Navigation</h2>
  <ul>
  <li><a href="first.html">First</a></li>
  <li><a href="second.html">Second</a></li>
  <li><a href="third.html">Third</a></li>
  </ul>
</div>
<div id="content">
  <h2>Content</h2>
  Some sample content, add your own here
</div>
<div id="footer">
  This page is written by [Your name] and builds on a <a href="http://friendlybit.com">Friendlybit template</a>.
</div>
...
```

What have we done here? First you should note that a quick overview of the document tells you quite much about the content. You can easily see that some stuff are headers (h1, h2) and some are just a list of links (ul, li, a). Let's go through the code quickly:

First we have a header. A header is something that's most often a big image and some text. Some pages don't have the header in the HTML at all, they just link to an image and have the text in that image. Problem with that is that neither search engines nor screen readers can get the title text. With the title text being the most important piece of description a visitor has to what page they have come to, you do have a problem. So trust me, keep that text there.

Next up we have the navigation. Navigation should almost always be marked up as an unordered list of links. I've seen the strangest variants of this with tables, nested tables, ``-tags after each line and so on but the only content there is a list of links, why make it something it isn't? Using a list doesn't mean it will have to look a certain way, remember that all design is handled in the CSS later on, this is just HTML we are dealing with here. Note: you can easily remove the bullet marks with `list-style: none;`, that's not a reason to use some other HTML.

The most important part of your HTML document is the content. This is the reason people will visit your page and this is where you should put most of your effort. Mark your headers with appropriate header-tags and make sure they look different from the ordinary text, this makes it easier quickly get a grip of what you're are trying to say. Use paragraph tags around your paragraphs to make is easier to style your text. The CSS `text-indent: 2em;` adds some space before only the first word in each paragraph, just to name one simple thing you can do with CSS when you've used good markup.

Lastly, it could be a good idea to add a footer to your page. Make sure you have some kind of contact information here or somewhere else on your site, who knows what people will want to ask you? If you want to help me you could add a link to this site somewhere on your site too. If you do, thanks alot!

On the next (and last) page of this short beginners guide we will wrap everything up and add some sample CSS to the mix. All is free for you to copy and use on your page. Ready?

## Full HTML template and sample CSS

Let's start by putting the two pieces of HTML I showed you together and combine it with some sample CSS: [Sample HTML + CSS](/files/example1/). You can find all code that makes that page below. Feel free to copy the code below and experiment on your own.

```html
<!doctype html>
<html lang="en">
  <body>
    <div id="header">
      <h1>The name of this page</h1>
    </div>
    <div id="navigation">
      <h2>Navigation</h2>
      <ul>
        <li><a href="first.html">First</a></li>
        <li><a href="second.html">Second</a></li>
        <li><a href="third.html">Third</a></li>
      </ul>
    </div>
    <div id="content">
      <h2>Content</h2>
      Some sample content, add your own here
    </div>
    <div id="footer">
      This page is written by [Your name] and builds on a <a href="http://friendlybit.com">Friendlybit template</a>.
    </div>
  </body>
</html>
```

You should be able to tell what each part of the HTML does by now. Let's instead have a look at some sample CSS for the structure we have above. If you want to experiment with this code you can copy it to a file named style.css (or any other filename you reference in the `<link>`-tag in the HTML) and place it in the same directory as the HTML document.

```css
body {
	background-color: Green;
}
div {
	border: 3px solid Black;
	padding: 7px;
	width: 600px;
}
h1, h2, h3, h4, h5, h6 {
	margin: 0;
}
#navigation {
	float: left;
	width: 150px;
}
#content {
	float: left;
	width: 430px;
}
#footer {
	clear: both;
}
```

Let's go through the six rules above. First we set the background-color of body, and body is the background of everything, so this will do the same as bgcolor did in HTML.

Next we set some styles on all divisions on the page. We have four of them and with this single rule we affect them all. First we set a black border to be 3 pixels wide (note that there is no space between number and unit in CSS). We then set a padding (the space between the border and content) to be 7 pixels and lastly we set the width of all divs to 600 pixels (note that margins, borders and padding are not included in the width).

The third rule selects all headers on the page and removes the margins (the space between the border and other nearby elements) from them. The commas are used between the elements to apply the same CSS to all of them.

Next we have some specific rules for three of the divisions. We position the navigation to the left of the content. This is done by using <dfn>floats</dfn>, a way to put things side by side. If you have used the align-attribute on images in HTML you will know how floats work, they move the element as far to the left as possible and then let the next element follow right next to it. If you want to put something below a float you need to <dfn>clear</dfn> it. Clearing moves the element down until it's below any floats, exactly where we want the footer. So both navigation and content are floated and given a width to match the 600 pixels wide header, and the footer is cleared.

**Update:** I have added some [simple layouts](/css/simple-css-templates/) for you to look at, and a list of [tools I use when developing](/css/web-development-pack/). Hope they help all of you out there that learn by examples.

Now it's your turn, you will learn CSS by using it and trying out how things work. So go ahead and play with the sample above. Thanks for reading, and good luck!

Any ideas of how this guide could be improved? Just leave a comment to the right.
