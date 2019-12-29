---
id: 70
title: 'Beyond the web with CSS: PrinceXML and S5'
date: 2006-06-25T00:37:34
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/beyond-the-web-with-css-princexml-and-s5/
permalink: /css/beyond-the-web-with-css-princexml-and-s5/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205362459"
btcnew_comment_counts:
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - HTML
---
Right now, depending on what kind of presentation you will be doing, you use different techniques. I'm not talking about "presentation" as in design here, I'm talking about web sites, printed paper, slide shows and so on, different types of media. How many of you use the print feature in browsers for your reports? Didn't think so.

Wouldn't it be nice if there was only one set of standards you needed to learn? One set that worked for all kinds of documents. One where encoding problems of differences in alphabets had been solved. One with a huge community of developers that gave of their time to help you with problems. Wouldn't that be nice? Good thing that set of standards exist: HTML and CSS.

## Printing like it once was: Word and LaTeX

The ordinary Windows user uses [Mircosoft Word](http://office.microsoft.com/word) for editing text. Word is popular for its ease of use and hides all the code from the user, instead showing the document like it will be printed. This of course pushes the filesizes up because of inefficient code, just like with any <acronym title="What you see is what you get">WYSIWYG</acronym> editor. Word supports the separation of structure and design by it's templates but hides this feature behind menu selections instead of promoting it as the preferred method. It also uses a proprietary format for storing the documents, something that makes sharing documents harder. Word costs a lot, but if you're lucky it's included when you buy your Windows machine.

For scientific work, [LaTeX](http://www.latex-project.org/) is very popular. LaTeX takes a very different approach from Word at editing text by requiring the user to mark up structure with its own markup format. It comes with a few predefined designs that you pick among by writing some markup in the beginning of the document. The document is then compiled by a command line program into an intermediary format that can be sent to a printer. If you know what you're doing, this makes it easy to get those default designs out fast. The problem with LaTeX is when you _do_ want to change the design. This requires you to dig deep into TeX syntax, a language not known for its ease of use.

Example of some LaTeX code:

```latex
\\documentclass{article}
\\title{Cartesian closed categories and the price of eggs}
\\author{Jane Doe}
\\date{September 1994}
\\begin{document}
   \\maketitle
   Hello world!
\\end{document}
```

## Printing with web standards: PrinceXML

The runner up in the print category is [PrinceXML](http://princexml.com/). It's based on ordinary (X)HTML/XML together with CSS and outputs PDF documents ready for printing. The CSS support is quite remarkable, managing to render the [Acid2 test](http://webstandards.org/action/acid2/) according to standard and supporting new CSS3 features like cross-references without problem. The handling of page sizes, page footers and headers comes from the [CSS3 Paged Media](http://www.w3.org/TR/css3-page/) module and too works well from my testing.

Below you can see an example of what can be done in PrinceXML. First we add a counter that keeps track of what number each block with the classname figure as. Then we add that number before the figure's caption. Lastly we add a parantesis with the figure number too all links that link to a certain figure.

```css
.figure {
	counter-increment: fig;
}
.figure .caption::before {
	content: "Figure #" counter(fig) ": "
}
a[href^="#fig_"]::after {
	content: " (see figure " target-counter(attr(href), fig) ")";
}
```

I am currently using the program for my degree thesis, a 34 page giant that has quite strict rules it needs to follow for styling. PrinceXML handles things just like it should. It costs a bit, but if you write a lot of documents it's probably worth it. If you can handle a promotional first page a [free trial version](http://princexml.com/download/) is available on the web site.

## Slide shows like they once were: PowerPoint

Microsoft is in the lead in the slide show area too with its well known [Microsoft PowerPoint](http://office.microsoft.com/powerpoint). Interestingly PowerPoint goes a long way towards separation with it's easy to use layout modes. You pick a layout from a easy to overview list of options and then just click and type to fill it with your content. What isn't included is design. Much like LaTeX, PowerPoint lets you pick from a number of premade templates but makes it hard to make your own. Given that ease of use is more important for PowerPoint than customization you could say that the product is successful. For someone like me though, that wants to make my own designs, learning how to make PowerPoint templates isn't easy enough to be interesting. PowerPoint also uses a proprietary format and costs _mucho dinero_, but if you are lucky it was included when you bought your computer.

## Slide shows with web standards: S5

Eric Meyer is the author of a web standards based [slide show system called S5](http://meyerweb.com/eric/tools/s5/). It's rather easy to use for someone used to HTML and CSS. Pick your favourite properly marked up HTML file, add `<div class="slide">` around a block of content you want on its own slide, link some javascript and CSS and you're ready to go. The slide show is then run in a web browser in fullscreen mode. It supports incremental display and resizes with the browser window, just like PowerPoint. It's also completly free.

## Summary

It _is_ possible to use HTML and CSS for both web, print and slide shows. In fact you can combine all of them and by using the media attribute on your link elements. That way the same document can be shown on the web, be rendered as a PDF in PrinceXML and displayed in a slideshow with S5.

Isn't this standards stuff quite fantastic?
