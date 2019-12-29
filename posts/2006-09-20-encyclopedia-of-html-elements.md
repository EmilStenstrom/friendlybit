---
author: Emil Stenström
categories:
- HTML
date: 2006-09-20 23:53:36
guid: http://friendlybit.com/html/encyclopedia-of-html-elements/
id: 94
permalink: /html/encyclopedia-of-html-elements/
title: Encyclopedia of HTML elements
---

HTML is a much richer language than what it's used for. There are 77 elements and each one has a certain purpose. It is possible to find that reason by reading the specification, but who does that? I wrote this list as a way to tell you what I think each of the HTML tags should be used for, common problems you might encounter, and general advise about each one.

I've included all the elements from HTML 4.01 *Strict*. It's a long one, but I'm sure you have more "tips and tricks" to add to it. Leave a comment and I'll add yours to the list too. Let's start off with a list of all the elements:

<p class="linkblock">
  <a href="#A">A</a>, <a href="#ABBR">ABBR</a>, <a href="#ACRONYM">ACRONYM</a>, <a href="#ADDRESS">ADDRESS</a>, <a href="#AREA">AREA</a>, <a href="#B">B</a>, <a href="#BASE">BASE</a>, <a href="#BDO">BDO</a>, <a href="#BIG">BIG</a>, <a href="#BLOCKQUOTE">BLOCKQUOTE</a>, <a href="#BODY">BODY</a>, <a href="#BR">BR</a>, <a href="#BUTTON">BUTTON</a>, <a href="#CAPTION">CAPTION</a>, <a href="#CITE">CITE</a>, <a href="#CODE">CODE</a>, <a href="#COL">COL</a>, <a href="#COLGROUP">COLGROUP</a>, <a href="#DD">DD</a>, <a href="#DEL">DEL</a>, <a href="#DFN">DFN</a>, <a href="#DIV">DIV</a>, <a href="#DL">DL</a>, <a href="#DT">DT</a>, <a href="#EM">EM</a>, <a href="#FIELDSET">FIELDSET</a>, <a href="#FORM">FORM</a>, <a href="#H1">H1</a>, <a href="#H1">H2</a>, <a href="#H1">H3</a>, <a href="#H1">H4</a>, <a href="#H1">H5</a>, <a href="#H1">H6</a>, <a href="#HEAD">HEAD</a>, <a href="#HR">HR</a>, <a href="#HTML">HTML</a>, <a href="#I"> I </a>, <a href="#IMG">IMG</a>, <a href="#INPUT">INPUT</a>, <a href="#INS">INS</a>, <a href="#KBD">KBD</a>, <a href="#LABEL">LABEL</a>, <a href="#LEGEND">LEGEND</a>, <a href="#LI">LI</a>, <a href="#LINK">LINK</a>, <a href="#MAP">MAP</a>, <a href="#META">META</a>, <a href="#NOSCRIPT">NOSCRIPT</a>, <a href="#OBJECT">OBJECT</a>, <a href="#OL">OL</a>, <a href="#OPTGROUP">OPTGROUP</a>, <a href="#OPTION">OPTION</a>, <a href="#P">P</a>, <a href="#PARAM">PARAM</a>, <a href="#PRE">PRE</a>, <a href="#QU">Q</a>, <a href="#SAMP">SAMP</a>, <a href="#SCRIPT">SCRIPT</a>, <a href="#SELECT">SELECT</a>, <a href="#SMALL">SMALL</a>, <a href="#SPAN">SPAN</a>, <a href="#STRONG">STRONG</a>, <a href="#STYLE">STYLE</a>, <a href="#SUB">SUB</a>, <a href="#SUB">SUP</a>, <a href="#TABLE">TABLE</a>, <a href="#TBODY">TBODY</a>, <a href="#TD">TD</a>, <a href="#TEXTAREA">TEXTAREA</a>, <a href="#TFOOT">TFOOT</a>, <a href="#TH">TH</a>, <a href="#THEAD">THEAD</a>, <a href="#TITLE">TITLE</a>, <a href="#TR">TR</a>, <a href="#TT">TT</a>, <a href="#UL">UL</a>, <a href="#VAR">VAR</a>


For people that view this site in a visual browser I added colored bars on all the elements. They represent if an element is recommended to use or not. Green bar means "Use this!", Yellow means "Consider if you really need it", and Red means "Don't use this unless you have a really good reason".

## **A** - Links, the very foundation of the web {#A.correct}

Should have the href attribute, but be sure to not include & in it. Write that as & instead.

Don't put blocks ([divisions](#DIV), [paragraphs](#P)) inside of links or you will get a validation error.

If you set `display: block` on a link, you can set its width and height with CSS.

## **ABBR** - Explain what your abbreviations mean {#ABBR.correct}

Abbreviations are words which are short forms of a longer word or phrase. Examples include HTML, int, and Amex

Should have a title attribute with the explaination of your term.

Make sure this explanation is humanly readable (unlike how it's used in [microformats](/html/current-issues-with-microformats/)). It's here to help *people* not machines.

## **ACRONYM** - Special case of the above where the word is formed from beginning parts of the words in a phrase {#ACRONYM.almost}

No need to use this one, abbr is enough. Do we really need to differ between acronyms and abbreviations? What about initialisms and the other types of words?

## **ADDRESS** - Contact information of some kind {#ADDRESS.correct}

Can be used for more than just street addresses, be creative! E-mail address and other contact info?

## **AREA** - Define links in any shape {#AREA.almost}

Useful if you need clickable links in odd shapes. A possible example of this is a map with clickable regions.

[CSS sprites](http://alistapart.com/articles/sprites#irregularshapes) is another way of doing something similar using CSS.

Don't forget to specify alt text for your area links.

Isn't the shape of links really design? Should be specified in the CSS then, not in the HTML.

## **B** - Make text look bold {#B.incorrect}

Don't use. Boldness is design and should be specified in the CSS using `font-weight: bold;`

If you intended to show that something was very important you can use `<strong></strong>` instead. It describes the meaning better and has the same default styling.

## **BASE** - Change your links to be relative to this address {#BASE.incorrect}

If you have to use this one, you're probably doing something wrong. I've seen terrible sites using this one.

There's a very strange [Internet Explorer bug with the base element](http://www.456bereastreet.com/archive/200608/base_elements_cause_text_selection_problems_in_ie/)

## **BDO** - For foreign languages (ie. Hebrew), mark text direction {#BDO.almost}

This is a tricky one. I wouldn't say text direction is structure (and belong to the HTML), but it isn't design either (and belong in the CSS). Perhaps it's content?

Text direction can be set in the CSS with the `dir` attribute

## **BIG** - set larger text relative to surrounding text {#BIG.incorrect}

Don't use. This is design and should be in the CSS. Use `font-size` instead.

## **BLOCKQUOTE** - Longer quotes {#BLOCKQUOTE.correct}

Include one or many paragraph(s) inside of this one.

Takes a cite attribute but this isn't rendered in browsers so use the cite *element* instead.

Don't ever use this one for indenting text, there's margin and padding in CSS for that.

## **BODY** - All your real content goes inside this one {#BODY.correct}

Always use (even though a page without it for strange reasons still validate).

Never use bgcolor, background or the a-/v-/link attributes on body. Those can be set by using CSS instead.

Set a class or id to the body on each of your different pages if you want to style them differently. By using `body#contact div`, you can easily style all the divs on only the contact page.

## **BR** - Line break {#BR.almost}

Instead of marking the line-breaks between your items, mark the items! For ordinary text use [paragraphs](#P) around each text block instead of breaks between them. Use a [lists](#UL) and add a [line item](#LI) around each of the items instead of separating them with line breaks.

A valid use-case is poems, where line breaks are part of poems themselves.

## **BUTTON** - Alternative to inputs with types submit and reset {#BUTTON.correct}

A much more general way to add buttons to your form elements (Thanks [Rowan Lewis](http://pixelcarnage.net/) for correcting my misstake.)

Allows you to add more than just text as the label, wrap the content you want inside of the button element.

## **CAPTION** - Description of a table {#CAPTION.correct}

As many other [table](#TABLE) elements, caption is sometimes hard to style with CSS in some browsers. If you start to get into trouble, use a header instead.

## **CITE** - Source where quoted text originated {#CITE.correct}

Use together with [blockquote](#BLOCKQUOTE) to connect the quotation and source.

Can be used to mark something as reference by wrapping cite around it. This could be useful if you are talking about a book but don't have a link to it.

## **CODE** - Computer code example {#CODE.correct}

Perfect for authors writing about computer code.

Don't fall into the trap of using the lang attribute on code to specify what computer language your code is written in. The [specification clearly states](http://www.w3.org/TR/html4/struct/dirlang.html#h-8.1.1) that's not allowed (I need to fix one of my plug-ins that does that on this blog). Thanks trovster.

## **COL** - Used to specify that some table cells belong together in columns {#COL.correct}

A very nice way of setting attributes of columns of cells in a table. Why not use this to set a class on that last column of cells you want to give that grey background?

Keep using [table headers](#TH), this is not a replacement for them

## **COLGROUP** - Shorter way of specifying table columns {#COLGROUP.correct}

Use colgroup instead of several col elements by setting the span attribute to the number of columns you want to affect.

## **DD** - Description of a term in a [definition list](#DL) {#DD.correct}

Several dd:s after each other means that there's many meanings to a certain term.

## **DEL** - Mark deleted text in documents {#DEL.almost}

Good for marking up document revisions, where one author makes changes and what to clearly mark where.

An interesting idea is to use this for version management (together with [ins](#ins)). Probably rare but an interesting idea. An example is how this is used at Wikipedia when comparing historical versions of an article (thanks Fredrico).

I have never seen an example where this element would be appropriate. Very rare.

Some screen readers are uncertain of what to do with the text inside of a del element. Should it be included in the page content or not? Be careful (Thanks [Peter Krantz](http://www.standards-schmandards.com/))

## **DFN** - Term that's being explained by you {#DFN.correct}

Useful when you explain a term in the middle of a sentence. Add dfn around the word you explain.

A [definition list](#DL) is more appropriate if you want to explain many terms at the same time.

## **DIV** - Divider into logical parts {#DIV.correct}

Divide the page into logical parts. Typical examples are "header", "content", "sidebar" and "footer".

Divisions should only be used when there's no other better fitted element available. Keep the number of divs down as much as you can.

A similar element for inline stuff is the [span element](#SPAN)

## **DL** - List of definitions {#DL.correct}

Very useful for glossaries where you provide a term and it's explanation.

I use it much wider than just the above, more like a structure for matching key and value. Say you have a list of people and their preferred colors. I would use a definition for that.

Use dt for the key and dd for the value

## **DT** - What you define in a definition list {#DT.correct}

If you put two dt elements after each other that means that the two terms means the same. The explaination that follows applies to them both.

## **EM** - Important phrase {#EM.correct}

Use this to mark some part of your text a bit more important. Try not the think of the default styling, think importance.

If you want something stronger, use [strong](#STRONG).

It's not always possible to just change a italic element to a em element, are you really using it to mark up importance?

## **FIELDSET** - Groups form elements that belong together {#FIELDSET.correct}

Perfect if you have a first and last name in two different text fields and want to show that they belong together.

A [legend element](#LEGEND) should be put inside of the fieldset to label it.

Fieldset borders are tricky with different browsers, I generally disable them with `border: none`.

Don't fall into the trap of using fieldsets for non-form elements. They are meant for grouping form elements, nothing else.

## **FORM** - Wrapper for all kinds of form fields {#FORM.correct}

Use the form element just like you would use a [div](#DIV), like a wrapper.

If possible make sure your forms work without javascript enabled. I'm not asking that your sliding-fadeout-gradients are working, just make sure the basic stuff gets through.

## **H1, H2, H3, H4, H5, H6** - Headings for your sections {#H1.correct}

One of the most important elements in HTML. If you don't have any headers on a certain page you're most certainly doing something wrong. Think about your structure!

Always start with the h1 element. If you don't like the size, change it with `font-size`.

Don't skip levels of headings. If you have a h5 on the page, all four previous levels should be there too.

Different browsers have different default sizes for headings. Make sure you set the size for every one of them to get rid of that problem.

## **HEAD** - Container for meta data in the document {#HEAD.correct}

For validation, you only need a [title](#TITLE) inside this element, but typical documents have a [link element](#LINK) for the stylesheet, a [script element](#SCRIPT) for the javascript, and some meta data inside [meta elements](#META).

## **HR** - Horizontal line {#HR.incorrect}

Don't use. This is design, the same effect can be accomplished through `border-bottom` in CSS.

Some people claim that hr is a section divider, but isn't that what we have [divisions](#DIV) for?

## **HTML** - Wrapper for everything except the doctype {#HTML.correct}

The HTML element can be used as a wrapper (an outer div around all content). Use this to get rid of one unnessesary wrapper.

Also takes the lang attribute that tells browsers what lanugage the site is written in (thanks [Ben Millard](http://sitesurgeon.co.uk/)). This is extra useful for screen readers that needs to change their pronunciations. [Language codes](http://www.loc.gov/standards/iso639-2/langcodes.html) are available through the US Library of congress. Use the two letter variants.

## **I** - Italic text {#I.incorrect}

Don't use. Purely presentational way of adding italic styling. Use the [em element](#EM) instead.

## **IMG** - Embedded image {#IMG.correct}

Used incorrectly very frequently. IMG should only be used for images that can be considered content on the page. An example of this is a thumbnail gallery or a helpful image somehow connected to the text. Things that shouldn't be img elements are decorations: rounded corners, bullet points in lists, and page dividers. Use `background-image` in CSS for that instead.

If the image contains information that you want to convey, use the alt attribute to give that information to user-agents that doesn't load images.

## **INPUT** - Radio button, check box, text field, button, or hidden data {#INPUT.correct}

Element used as a building block for form fields. The type is determined by the setting the type attribute to either radio, checkbox, text, image, submit, reset, or hidden.

Other elements normally used together with this one is [select](#SELECT) and [textarea](#TEXTAREA).

Make sure you add an id to each input field and tie an [label element](#LABEL) to it. No input should be without it.

Wrap your inputs and labels in a [fieldset](#FIELDSET), paragraph or div to stop the validator from complaining that elements are not allowed where they are.

## **INS** - Inserted text {#INS.almost}

Similar to [del](#DEL), this element can be used to mark deleted text.

Might be useful for tracking changes in your document but again, I have never seen a site where this element was needed.

## **KBD** - Text that should be entered on the keyboard {#KBD.correct}

One of the numerous elements that can be used to mark up documents about computers. Rarely used.

How do you know your user will use the keyboard?

## **LABEL** - Text that describes a corresponding form field {#LABEL.correct}

The for attribute associates this element with a form field id. Important out of an accessibility standpoint, both because it gives screen readers better info and because it makes form fields clickable (in most browsers, but not Safari, thanks [Roger](http://www.456bereastreet.com/)).

## **LEGEND** - Heading for a fieldset element {#LEGEND.correct}

Wrap this element inside each of your fieldsets to provide a reason why you think the following fields belong together. Typical examples include "Credit card", "Full address", and "Shipment details".

Somewhat tricky to style since browsers handle them very differently. I tend to keep them pretty plain.

## **LI** - Items in [ordered](#OL "ordered list") or [unordered lists](#UL) {#LI.correct}

Gets different styling by default depending on browser: padding-left or margin-left. If you want to change the indention, make sure you first reset the other one.

## **LINK** - A way to define links to other elements {#LINK.correct}

Most often used to define external stylesheets for the document (use `rel="stylesheet"`)…

.. but can be used to define [other types of relations](http://www.subotnik.net/html/link.html.en) too. Some browsers show custom rel types to users like a list of bookmarks.

## **MAP** - Wrapper for image map areas {#MAP.almost}

Used together with the [area element](#AREA) for image maps.

## **META** - Information about the document {#META.correct}

Can be used to for custom information about the document.

Search engines use some [predefined names](http://searchenginewatch.com/showPage.html?page=2167931 "meta elements supported by search engines") that you should know about.

## **NOSCRIPT** - Content to show if the browser doesn't support javascript {#NOSCRIPT.incorrect}

The default should be to show content that does not require javascript, we don't need a certain element for that.

## **OBJECT** - Embedding other types of information in to document {#OBJECT.correct}

The new way of adding [flash](http://www.ambience.sk/flash-valid.htm), quicktime and other multimedia content to your site.

## **OL** - Ordered list of items {#OL.correct}

Ordering means that the content only makes sense in that order. This means that a step-by-step recipe is an ordered list, but a basic navigation menu is not (see [unordered list](#UL)).

## **OPTGROUP** - Group your option elements {#OPTGROUP.correct}

One of the least known elements in HTML. Impress your friends!

Similar to fieldset but for option elements. Wraps around them and uses the *label attribute* to name the group.

Nesting of optgroups is not allowed.

## **OPTION** - One of the choices in a select {#OPTION.correct}

If you set the value attribute, that value is sent instead of the text inside the element.

## **P** - Wrapper around each of your paragraphs {#P.correct}

Replacement for line breaks (the br element).

By wrapping all your paragraphs in a p element you can easily change the space between them with margin or padding.

## **PARAM** - Set properties on embedded objects {#PARAM.correct}

The exact param names used depends on what you embed, check the documentation for the document you are dealing with.

## **PRE** - Preformatted text {#PRE.almost}

Used to define that a certain piece of text is formatted (designed) in the HTML. While this is most often a bad idea there's applications in e.g. [ASCII art](http://www.chris.com/ASCII/), text-only e-mails, and Python code (thanks zcorpan).

Use `white-space: pre;` and `font-family: monospace;` to get the "pre design" with CSS.

## **Q** - Add quotations in a language independent way {#QU.almost}

Instead of setting what kind of quotes you use (there are several you know), you simply define that you're dealing with a quote and work out the details in a separate file.

Good idea, but no support by IE6 makes it a lot less useful.

## **SAMP** - Sample text or characters {#SAMP.almost}

Seriously, don't we have enough of the computer related elements already? If you need sample text that isn't code or keyboard type-in then fine, use this one.

## **SCRIPT** - Run javascript on your site {#SCRIPT.correct}

Remember to set the type attribute to text/javascript if that's what you use. Language is no longer needed.

## **SELECT** - Let the user select among a number of fixed options {#SELECT.correct}

Don't forget to use a [label](#LABEL) for this element too.

It's easy to make selects work without javascript, just add a submit button. Also check so that all options can be reached with the keyboard.

Selects take the size attribute which makes you able to show more than one option at the time. If you set size to something larger than one, you can use CSS to set a height.

## **SMALL** - Presentational way of setting font-size {#SMALL.incorrect}

Don't use. A presentational way of saying that some text is smaller than the rest. Use `font-size` in CSS instead!

I've seen some interesting ideas of using this tag for "fine print", those copyright messages that always are tiny. The idea is that the size really is tied to the content, and that small therefore is a good semantic way of representing it. I'm not sure, for now I won't recommend people using it.

## **SPAN** - Similar to [div](#DIV) but for inline elements {#SPAN.correct}

Can be used when you don't find a better representation. Make sure the class you set describes what you mark up instead.

## **STRONG** - Mark something as very important {#STRONG.correct}

Stronger than emphasis with the [em element](#EM).

## **STYLE** - Add style info to your page {#STYLE.correct}

Needs to be in the head section of the page, inside body isn't valid.

Don't forget to set the type attribute to "text/css".

In my opinion, using [link](#LINK) separates the design better than using the style element. It also makes the browser able to cache the CSS.

## **SUB**, **SUP** - Raised and lowered characters {#SUB.almost}

Don't use for lowering and raising letters with no semantic meaning.

Use in math or chemical formulas (see comments).

## **TABLE** - Row and column based data {#TABLE.correct}

Misused in the "tables for layout" days. Tables. Are. Not. For. Layout.

Proper use is for scientific, statistical, or other cell-based data.

Frequently forgotten elements include the [thead](#THEAD), [tbody](#TBODY), and [th](#TH) elements.

If you nest tables you are doing something wrong.

You can set `border-collapse: collapse;` to get rid of the annoying default cellpadding. No attributes need to be set in the HTML.

Combining border-collapse and a border on [td elements](#TD) makes it possible to get nice 1 pixel borders between all cells.

## **TBODY** - Container meant to separate the body of your table from your headers {#TBODY.correct}

Simply use this as a way to style your body different from your headers. Have [th elements](#TH) both in the tbody and thead? Then use `tbody th { ... }` to style only the ones in the header.

You can use several tbody elements, something that can be a nice way to divide one big table into several logical parts.

## **TD** - Represent one cell of data {#TD.correct}

Use padding, margin and border on td and th to change the spacing inside your table.

## **TEXTAREA** - Let users send big chunks of text {#TEXTAREA.correct}

The size can be specified with height and width in CSS.

Don't forget a corresponding [label element](#LABEL).

## **TFOOT** - Extra information in the bottom of a table {#TFOOT.correct}

I rarely use this one, most often a caption is what I want below.

A possible use case for tfoot is for adding column sums at the bottom of the table.

## **TH** - Specify that a certain cell is not part of the data, it just describes the other cells. {#TH.correct}

Very convenient way of specifying a different style for the headers of the table.

Takes the scope attribute if you want to specify what cells a certain table header describes.

## **THEAD** - Container for (some of) the metadata for a table {#THEAD.correct}

Some browsers repeat this element on all pages when printing long tables, very useful!

## **TITLE** - Topic of the page summarised in a few words {#TITLE.correct}

Single most important part of your site, think a while before setting it.

Meant for a single page, not the whole site.

Required for validation, and gives strange validation errors about "head not closed" if not included.

## **TR** - Way of specifying rows of table cells {#TR.correct}

Very few browsers support styling the tr element, so set your styles on the containing table cells instead. Example: If you want alternating row colors you can set a class on the tr element but style the table cells with `tr.odd td { background: ... }`.

## **TT** - Text formatted like if it was written on a typewriter {#TT.incorrect}

Don't use. Presentational way of adding text that looks like it was written on a typewriter. Use `font-family: monospace;` to get the same effect with CSS.

## **UL** - List where the order doesn't matter {#UL.correct}

Perfect for navigation menus, don't use br for that.

See tip on cross browser use with the ol element.

## **VAR** - Variable of some kind {#VAR.almost}

Another element from the computer science area. Some people claim this can be used for other variables too, but that's a really rare use case. No need to remember.

What did I miss? Please leave a comment!
