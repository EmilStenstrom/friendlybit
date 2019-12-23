---
id: 94
title: Encyclopedia of HTML elements
date: 2006-09-20T23:53:36
author: Emil Stenström
layout: post
guid: http://friendlybit.com/html/encyclopedia-of-html-elements/
permalink: /html/encyclopedia-of-html-elements/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205286413"
categories:
  - HTML
---
HTML is a much richer language than what it&#8217;s used for. There are 77 elements and each one has a certain purpose. It is possible to find that reason by reading the specification, but who does that? I wrote this list as a way to tell you what I think each of the HTML tags should be used for, common problems you might encounter, and general advise about each one.

I&#8217;ve included all the elements from HTML 4.01 _Strict_. It&#8217;s a long one, but I&#8217;m sure you have more &#8220;tips and tricks&#8221; to add to it. Leave a comment and I&#8217;ll add yours to the list too. Let&#8217;s start off with a list of all the elements:

<p class="linkblock">
  <a href="#A">A</a>, <a href="#ABBR">ABBR</a>, <a href="#ACRONYM">ACRONYM</a>, <a href="#ADDRESS">ADDRESS</a>, <a href="#AREA">AREA</a>, <a href="#B">B</a>, <a href="#BASE">BASE</a>, <a href="#BDO">BDO</a>, <a href="#BIG">BIG</a>, <a href="#BLOCKQUOTE">BLOCKQUOTE</a>, <a href="#BODY">BODY</a>, <a href="#BR">BR</a>, <a href="#BUTTON">BUTTON</a>, <a href="#CAPTION">CAPTION</a>, <a href="#CITE">CITE</a>, <a href="#CODE">CODE</a>, <a href="#COL">COL</a>, <a href="#COLGROUP">COLGROUP</a>, <a href="#DD">DD</a>, <a href="#DEL">DEL</a>, <a href="#DFN">DFN</a>, <a href="#DIV">DIV</a>, <a href="#DL">DL</a>, <a href="#DT">DT</a>, <a href="#EM">EM</a>, <a href="#FIELDSET">FIELDSET</a>, <a href="#FORM">FORM</a>, <a href="#H1">H1</a>, <a href="#H1">H2</a>, <a href="#H1">H3</a>, <a href="#H1">H4</a>, <a href="#H1">H5</a>, <a href="#H1">H6</a>, <a href="#HEAD">HEAD</a>, <a href="#HR">HR</a>, <a href="#HTML">HTML</a>, <a href="#I"> I </a>, <a href="#IMG">IMG</a>, <a href="#INPUT">INPUT</a>, <a href="#INS">INS</a>, <a href="#KBD">KBD</a>, <a href="#LABEL">LABEL</a>, <a href="#LEGEND">LEGEND</a>, <a href="#LI">LI</a>, <a href="#LINK">LINK</a>, <a href="#MAP">MAP</a>, <a href="#META">META</a>, <a href="#NOSCRIPT">NOSCRIPT</a>, <a href="#OBJECT">OBJECT</a>, <a href="#OL">OL</a>, <a href="#OPTGROUP">OPTGROUP</a>, <a href="#OPTION">OPTION</a>, <a href="#P">P</a>, <a href="#PARAM">PARAM</a>, <a href="#PRE">PRE</a>, <a href="#QU">Q</a>, <a href="#SAMP">SAMP</a>, <a href="#SCRIPT">SCRIPT</a>, <a href="#SELECT">SELECT</a>, <a href="#SMALL">SMALL</a>, <a href="#SPAN">SPAN</a>, <a href="#STRONG">STRONG</a>, <a href="#STYLE">STYLE</a>, <a href="#SUB">SUB</a>, <a href="#SUB">SUP</a>, <a href="#TABLE">TABLE</a>, <a href="#TBODY">TBODY</a>, <a href="#TD">TD</a>, <a href="#TEXTAREA">TEXTAREA</a>, <a href="#TFOOT">TFOOT</a>, <a href="#TH">TH</a>, <a href="#THEAD">THEAD</a>, <a href="#TITLE">TITLE</a>, <a href="#TR">TR</a>, <a href="#TT">TT</a>, <a href="#UL">UL</a>, <a href="#VAR">VAR</a>


For people that view this site in a visual browser I added colored bars on all the elements. They represent if an element is recommended to use or not. Green bar means &#8220;Use this!&#8221;, Yellow means &#8220;Consider if you really need it&#8221;, and Red means &#8220;Don&#8217;t use this unless you have a really good reason&#8221;.

## **A** &#8211; Links, the very foundation of the web {#A.correct}

Should have the href attribute, but be sure to not include & in it. Write that as & instead.

Don&#8217;t put blocks ([divisions](#DIV), [paragraphs](#P)) inside of links or you will get a validation error.

If you set `display: block` on a link, you can set its width and height with CSS.

## **ABBR** &#8211; Explain what your abbreviations mean {#ABBR.correct}

Abbreviations are words which are short forms of a longer word or phrase. Examples include HTML, int, and Amex

Should have a title attribute with the explaination of your term.

Make sure this explanation is humanly readable (unlike how it&#8217;s used in [microformats](/html/current-issues-with-microformats/)). It&#8217;s here to help _people_ not machines.

## **ACRONYM** &#8211; Special case of the above where the word is formed from beginning parts of the words in a phrase {#ACRONYM.almost}

No need to use this one, abbr is enough. Do we really need to differ between acronyms and abbreviations? What about initialisms and the other types of words?

## **ADDRESS** &#8211; Contact information of some kind {#ADDRESS.correct}

Can be used for more than just street addresses, be creative! E-mail address and other contact info?

## **AREA** &#8211; Define links in any shape {#AREA.almost}

Useful if you need clickable links in odd shapes. A possible example of this is a map with clickable regions.

[CSS sprites](http://alistapart.com/articles/sprites#irregularshapes) is another way of doing something similar using CSS.

Don&#8217;t forget to specify alt text for your area links.

Isn&#8217;t the shape of links really design? Should be specified in the CSS then, not in the HTML.

## **B** &#8211; Make text look bold {#B.incorrect}

Don&#8217;t use. Boldness is design and should be specified in the CSS using `font-weight: bold;`

If you intended to show that something was very important you can use `<strong></strong>` instead. It describes the meaning better and has the same default styling.

## **BASE** &#8211; Change your links to be relative to this address {#BASE.incorrect}

If you have to use this one, you&#8217;re probably doing something wrong. I&#8217;ve seen terrible sites using this one.

There&#8217;s a very strange [Internet Explorer bug with the base element](http://www.456bereastreet.com/archive/200608/base_elements_cause_text_selection_problems_in_ie/)

## **BDO** &#8211; For foreign languages (ie. Hebrew), mark text direction {#BDO.almost}

This is a tricky one. I wouldn&#8217;t say text direction is structure (and belong to the HTML), but it isn&#8217;t design either (and belong in the CSS). Perhaps it&#8217;s content?

Text direction can be set in the CSS with the `dir` attribute

## **BIG** &#8211; set larger text relative to surrounding text {#BIG.incorrect}

Don&#8217;t use. This is design and should be in the CSS. Use `font-size` instead.

## **BLOCKQUOTE** &#8211; Longer quotes {#BLOCKQUOTE.correct}

Include one or many paragraph(s) inside of this one.

Takes a cite attribute but this isn&#8217;t rendered in browsers so use the cite _element_ instead.

Don&#8217;t ever use this one for indenting text, there&#8217;s margin and padding in CSS for that.

## **BODY** &#8211; All your real content goes inside this one {#BODY.correct}

Always use (even though a page without it for strange reasons still validate).

Never use bgcolor, background or the a-/v-/link attributes on body. Those can be set by using CSS instead.

Set a class or id to the body on each of your different pages if you want to style them differently. By using `body#contact div`, you can easily style all the divs on only the contact page.

## **BR** &#8211; Line break {#BR.almost}

Instead of marking the line-breaks between your items, mark the items! For ordinary text use [paragraphs](#P) around each text block instead of breaks between them. Use a [lists](#UL) and add a [line item](#LI) around each of the items instead of separating them with line breaks.

A valid use-case is poems, where line breaks are part of poems themselves.

## **BUTTON** &#8211; Alternative to inputs with types submit and reset {#BUTTON.correct}

A much more general way to add buttons to your form elements (Thanks [Rowan Lewis](http://pixelcarnage.net/) for correcting my misstake.)

Allows you to add more than just text as the label, wrap the content you want inside of the button element.

## **CAPTION** &#8211; Description of a table {#CAPTION.correct}

As many other [table](#TABLE) elements, caption is sometimes hard to style with CSS in some browsers. If you start to get into trouble, use a header instead.

## **CITE** &#8211; Source where quoted text originated {#CITE.correct}

Use together with [blockquote](#BLOCKQUOTE) to connect the quotation and source.

Can be used to mark something as reference by wrapping cite around it. This could be useful if you are talking about a book but don&#8217;t have a link to it.

## **CODE** &#8211; Computer code example {#CODE.correct}

Perfect for authors writing about computer code.

Don&#8217;t fall into the trap of using the lang attribute on code to specify what computer language your code is written in. The [specification clearly states](http://www.w3.org/TR/html4/struct/dirlang.html#h-8.1.1) that&#8217;s not allowed (I need to fix one of my plug-ins that does that on this blog). Thanks trovster.

## **COL** &#8211; Used to specify that some table cells belong together in columns {#COL.correct}

A very nice way of setting attributes of columns of cells in a table. Why not use this to set a class on that last column of cells you want to give that grey background?

Keep using [table headers](#TH), this is not a replacement for them

## **COLGROUP** &#8211; Shorter way of specifying table columns {#COLGROUP.correct}

Use colgroup instead of several col elements by setting the span attribute to the number of columns you want to affect.

## **DD** &#8211; Description of a term in a [definition list](#DL) {#DD.correct}

Several dd:s after each other means that there&#8217;s many meanings to a certain term.

## **DEL** &#8211; Mark deleted text in documents {#DEL.almost}

Good for marking up document revisions, where one author makes changes and what to clearly mark where.

An interesting idea is to use this for version management (together with [ins](#ins)). Probably rare but an interesting idea. An example is how this is used at Wikipedia when comparing historical versions of an article (thanks Fredrico).

I have never seen an example where this element would be appropriate. Very rare.

Some screen readers are uncertain of what to do with the text inside of a del element. Should it be included in the page content or not? Be careful (Thanks [Peter Krantz](http://www.standards-schmandards.com/))

## **DFN** &#8211; Term that&#8217;s being explained by you {#DFN.correct}

Useful when you explain a term in the middle of a sentence. Add dfn around the word you explain.

A [definition list](#DL) is more appropriate if you want to explain many terms at the same time.

## **DIV** &#8211; Divider into logical parts {#DIV.correct}

Divide the page into logical parts. Typical examples are &#8220;header&#8221;, &#8220;content&#8221;, &#8220;sidebar&#8221; and &#8220;footer&#8221;.

Divisions should only be used when there&#8217;s no other better fitted element available. Keep the number of divs down as much as you can.

A similar element for inline stuff is the [span element](#SPAN)

## **DL** &#8211; List of definitions {#DL.correct}

Very useful for glossaries where you provide a term and it&#8217;s explanation.

I use it much wider than just the above, more like a structure for matching key and value. Say you have a list of people and their preferred colors. I would use a definition for that.

Use dt for the key and dd for the value

## **DT** &#8211; What you define in a definition list {#DT.correct}

If you put two dt elements after each other that means that the two terms means the same. The explaination that follows applies to them both.

## **EM** &#8211; Important phrase {#EM.correct}

Use this to mark some part of your text a bit more important. Try not the think of the default styling, think importance.

If you want something stronger, use [strong](#STRONG).

It&#8217;s not always possible to just change a italic element to a em element, are you really using it to mark up importance?

## **FIELDSET** &#8211; Groups form elements that belong together {#FIELDSET.correct}

Perfect if you have a first and last name in two different text fields and want to show that they belong together.

A [legend element](#LEGEND) should be put inside of the fieldset to label it.

Fieldset borders are tricky with different browsers, I generally disable them with `border: none`.

Don&#8217;t fall into the trap of using fieldsets for non-form elements. They are meant for grouping form elements, nothing else.

## **FORM** &#8211; Wrapper for all kinds of form fields {#FORM.correct}

Use the form element just like you would use a [div](#DIV), like a wrapper.

If possible make sure your forms work without javascript enabled. I&#8217;m not asking that your sliding-fadeout-gradients are working, just make sure the basic stuff gets through.

## **H1, H2, H3, H4, H5, H6** &#8211; Headings for your sections {#H1.correct}

One of the most important elements in HTML. If you don&#8217;t have any headers on a certain page you&#8217;re most certainly doing something wrong. Think about your structure!

Always start with the h1 element. If you don&#8217;t like the size, change it with `font-size`.

Don&#8217;t skip levels of headings. If you have a h5 on the page, all four previous levels should be there too.

Different browsers have different default sizes for headings. Make sure you set the size for every one of them to get rid of that problem.

## **HEAD** &#8211; Container for meta data in the document {#HEAD.correct}

For validation, you only need a [title](#TITLE) inside this element, but typical documents have a [link element](#LINK) for the stylesheet, a [script element](#SCRIPT) for the javascript, and some meta data inside [meta elements](#META).

## **HR** &#8211; Horizontal line {#HR.incorrect}

Don&#8217;t use. This is design, the same effect can be accomplished through `border-bottom` in CSS.

Some people claim that hr is a section divider, but isn&#8217;t that what we have [divisions](#DIV) for?

## **HTML** &#8211; Wrapper for everything except the doctype {#HTML.correct}

The HTML element can be used as a wrapper (an outer div around all content). Use this to get rid of one unnessesary wrapper.

Also takes the lang attribute that tells browsers what lanugage the site is written in (thanks [Ben Millard](http://sitesurgeon.co.uk/)). This is extra useful for screen readers that needs to change their pronunciations. [Language codes](http://www.loc.gov/standards/iso639-2/langcodes.html) are available through the US Library of congress. Use the two letter variants.

## **I** &#8211; Italic text {#I.incorrect}

Don&#8217;t use. Purely presentational way of adding italic styling. Use the [em element](#EM) instead.

## **IMG** &#8211; Embedded image {#IMG.correct}

Used incorrectly very frequently. IMG should only be used for images that can be considered content on the page. An example of this is a thumbnail gallery or a helpful image somehow connected to the text. Things that shouldn&#8217;t be img elements are decorations: rounded corners, bullet points in lists, and page dividers. Use `background-image` in CSS for that instead.

If the image contains information that you want to convey, use the alt attribute to give that information to user-agents that doesn&#8217;t load images.

## **INPUT** &#8211; Radio button, check box, text field, button, or hidden data {#INPUT.correct}

Element used as a building block for form fields. The type is determined by the setting the type attribute to either radio, checkbox, text, image, submit, reset, or hidden.

Other elements normally used together with this one is [select](#SELECT) and [textarea](#TEXTAREA).

Make sure you add an id to each input field and tie an [label element](#LABEL) to it. No input should be without it.

Wrap your inputs and labels in a [fieldset](#FIELDSET), paragraph or div to stop the validator from complaining that elements are not allowed where they are.

## **INS** &#8211; Inserted text {#INS.almost}

Similar to [del](#DEL), this element can be used to mark deleted text.

Might be useful for tracking changes in your document but again, I have never seen a site where this element was needed.

## **KBD** &#8211; Text that should be entered on the keyboard {#KBD.correct}

One of the numerous elements that can be used to mark up documents about computers. Rarely used.

How do you know your user will use the keyboard?

## **LABEL** &#8211; Text that describes a corresponding form field {#LABEL.correct}

The for attribute associates this element with a form field id. Important out of an accessibility standpoint, both because it gives screen readers better info and because it makes form fields clickable (in most browsers, but not Safari, thanks [Roger](http://www.456bereastreet.com/)).

## **LEGEND** &#8211; Heading for a fieldset element {#LEGEND.correct}

Wrap this element inside each of your fieldsets to provide a reason why you think the following fields belong together. Typical examples include &#8220;Credit card&#8221;, &#8220;Full address&#8221;, and &#8220;Shipment details&#8221;.

Somewhat tricky to style since browsers handle them very differently. I tend to keep them pretty plain.

## **LI** &#8211; Items in [ordered](#OL "ordered list") or [unordered lists](#UL) {#LI.correct}

Gets different styling by default depending on browser: padding-left or margin-left. If you want to change the indention, make sure you first reset the other one.

## **LINK** &#8211; A way to define links to other elements {#LINK.correct}

Most often used to define external stylesheets for the document (use `rel="stylesheet"`)&#8230;

.. but can be used to define [other types of relations](http://www.subotnik.net/html/link.html.en) too. Some browsers show custom rel types to users like a list of bookmarks.

## **MAP** &#8211; Wrapper for image map areas {#MAP.almost}

Used together with the [area element](#AREA) for image maps.

## **META** &#8211; Information about the document {#META.correct}

Can be used to for custom information about the document.

Search engines use some [predefined names](http://searchenginewatch.com/showPage.html?page=2167931 "meta elements supported by search engines") that you should know about.

## **NOSCRIPT** &#8211; Content to show if the browser doesn&#8217;t support javascript {#NOSCRIPT.incorrect}

The default should be to show content that does not require javascript, we don&#8217;t need a certain element for that.

## **OBJECT** &#8211; Embedding other types of information in to document {#OBJECT.correct}

The new way of adding [flash](http://www.ambience.sk/flash-valid.htm), quicktime and other multimedia content to your site.

## **OL** &#8211; Ordered list of items {#OL.correct}

Ordering means that the content only makes sense in that order. This means that a step-by-step recipe is an ordered list, but a basic navigation menu is not (see [unordered list](#UL)).

## **OPTGROUP** &#8211; Group your option elements {#OPTGROUP.correct}

One of the least known elements in HTML. Impress your friends!

Similar to fieldset but for option elements. Wraps around them and uses the _label attribute_ to name the group.

Nesting of optgroups is not allowed.

## **OPTION** &#8211; One of the choices in a select {#OPTION.correct}

If you set the value attribute, that value is sent instead of the text inside the element.

## **P** &#8211; Wrapper around each of your paragraphs {#P.correct}

Replacement for line breaks (the br element).

By wrapping all your paragraphs in a p element you can easily change the space between them with margin or padding.

## **PARAM** &#8211; Set properties on embedded objects {#PARAM.correct}

The exact param names used depends on what you embed, check the documentation for the document you are dealing with.

## **PRE** &#8211; Preformatted text {#PRE.almost}

Used to define that a certain piece of text is formatted (designed) in the HTML. While this is most often a bad idea there&#8217;s applications in e.g. [ASCII art](http://www.chris.com/ASCII/), text-only e-mails, and Python code (thanks zcorpan).

Use `white-space: pre;` and `font-family: monospace;` to get the &#8220;pre design&#8221; with CSS.

## **Q** &#8211; Add quotations in a language independent way {#QU.almost}

Instead of setting what kind of quotes you use (there are several you know), you simply define that you&#8217;re dealing with a quote and work out the details in a separate file.

Good idea, but no support by IE6 makes it a lot less useful.

## **SAMP** &#8211; Sample text or characters {#SAMP.almost}

Seriously, don&#8217;t we have enough of the computer related elements already? If you need sample text that isn&#8217;t code or keyboard type-in then fine, use this one.

## **SCRIPT** &#8211; Run javascript on your site {#SCRIPT.correct}

Remember to set the type attribute to text/javascript if that&#8217;s what you use. Language is no longer needed.

## **SELECT** &#8211; Let the user select among a number of fixed options {#SELECT.correct}

Don&#8217;t forget to use a [label](#LABEL) for this element too.

It&#8217;s easy to make selects work without javascript, just add a submit button. Also check so that all options can be reached with the keyboard.

Selects take the size attribute which makes you able to show more than one option at the time. If you set size to something larger than one, you can use CSS to set a height.

## **SMALL** &#8211; Presentational way of setting font-size {#SMALL.incorrect}

Don&#8217;t use. A presentational way of saying that some text is smaller than the rest. Use `font-size` in CSS instead!

I&#8217;ve seen some interesting ideas of using this tag for &#8220;fine print&#8221;, those copyright messages that always are tiny. The idea is that the size really is tied to the content, and that small therefore is a good semantic way of representing it. I&#8217;m not sure, for now I won&#8217;t recommend people using it.

## **SPAN** &#8211; Similar to [div](#DIV) but for inline elements {#SPAN.correct}

Can be used when you don&#8217;t find a better representation. Make sure the class you set describes what you mark up instead.

## **STRONG** &#8211; Mark something as very important {#STRONG.correct}

Stronger than emphasis with the [em element](#EM).

## **STYLE** &#8211; Add style info to your page {#STYLE.correct}

Needs to be in the head section of the page, inside body isn&#8217;t valid.

Don&#8217;t forget to set the type attribute to &#8220;text/css&#8221;.

In my opinion, using [link](#LINK) separates the design better than using the style element. It also makes the browser able to cache the CSS.

## **SUB**, **SUP** &#8211; Raised and lowered characters {#SUB.almost}

Don&#8217;t use for lowering and raising letters with no semantic meaning.

Use in math or chemical formulas (see comments).

## **TABLE** &#8211; Row and column based data {#TABLE.correct}

Misused in the &#8220;tables for layout&#8221; days. Tables. Are. Not. For. Layout.

Proper use is for scientific, statistical, or other cell-based data.

Frequently forgotten elements include the [thead](#THEAD), [tbody](#TBODY), and [th](#TH) elements.

If you nest tables you are doing something wrong.

You can set `border-collapse: collapse;` to get rid of the annoying default cellpadding. No attributes need to be set in the HTML.

Combining border-collapse and a border on [td elements](#TD) makes it possible to get nice 1 pixel borders between all cells.

## **TBODY** &#8211; Container meant to separate the body of your table from your headers {#TBODY.correct}

Simply use this as a way to style your body different from your headers. Have [th elements](#TH) both in the tbody and thead? Then use `tbody th { ... }` to style only the ones in the header.

You can use several tbody elements, something that can be a nice way to divide one big table into several logical parts.

## **TD** &#8211; Represent one cell of data {#TD.correct}

Use padding, margin and border on td and th to change the spacing inside your table.

## **TEXTAREA** &#8211; Let users send big chunks of text {#TEXTAREA.correct}

The size can be specified with height and width in CSS.

Don&#8217;t forget a corresponding [label element](#LABEL).

## **TFOOT** &#8211; Extra information in the bottom of a table {#TFOOT.correct}

I rarely use this one, most often a caption is what I want below.

A possible use case for tfoot is for adding column sums at the bottom of the table.

## **TH** &#8211; Specify that a certain cell is not part of the data, it just describes the other cells. {#TH.correct}

Very convenient way of specifying a different style for the headers of the table.

Takes the scope attribute if you want to specify what cells a certain table header describes.

## **THEAD** &#8211; Container for (some of) the metadata for a table {#THEAD.correct}

Some browsers repeat this element on all pages when printing long tables, very useful!

## **TITLE** &#8211; Topic of the page summarised in a few words {#TITLE.correct}

Single most important part of your site, think a while before setting it.

Meant for a single page, not the whole site.

Required for validation, and gives strange validation errors about &#8220;head not closed&#8221; if not included.

## **TR** &#8211; Way of specifying rows of table cells {#TR.correct}

Very few browsers support styling the tr element, so set your styles on the containing table cells instead. Example: If you want alternating row colors you can set a class on the tr element but style the table cells with `tr.odd td { background: ... }`.

## **TT** &#8211; Text formatted like if it was written on a typewriter {#TT.incorrect}

Don&#8217;t use. Presentational way of adding text that looks like it was written on a typewriter. Use `font-family: monospace;` to get the same effect with CSS.

## **UL** &#8211; List where the order doesn&#8217;t matter {#UL.correct}

Perfect for navigation menus, don&#8217;t use br for that.

See tip on cross browser use with the ol element.

## **VAR** &#8211; Variable of some kind {#VAR.almost}

Another element from the computer science area. Some people claim this can be used for other variables too, but that&#8217;s a really rare use case. No need to remember.

What did I miss? Please leave a comment!
