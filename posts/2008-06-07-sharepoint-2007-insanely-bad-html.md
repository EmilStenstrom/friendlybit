---
id: 163
title: 'Sharepoint 2007 – insanely bad HTML'
date: 2008-06-07T01:42:51
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=163
permalink: /html/sharepoint-2007-insanely-bad-html/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205287568"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - HTML
---
Sharepoint 2007 continues to amaze me with its terrible interface code. This is code you stumble over **all** over the place, both in places where you can hack your way around them, and in places where you just have to live with them. Some things are very hard to live with, let me show you:

ASP.NET developers made a decision once to include some hidden form fields, called viewstate, on all aspx pages. When deciding how to include those fields they chose an input with the type set to hidden. When the Sharepoint developers wanted to do something similar they decided on another route:

```html
<input type="text" name="__spDummyText1" style="display:none;" size=1/>
<input type="text" name="__spDummyText2" style="display:none;" size=1/>
```

So we have a visible textbox, hidden with CSS, that has a size of 1 character. No wait, we have two textboxes and they both have very descriptive names (NOT). What the heck were they thinking? Why not type=&#8221;hidden&#8221;, and remove size? Or, I know, don&#8217;t add them at all, they are only dummy right? Note that they are empty.

Another strange interface decision is the one to include a skiplink in the page. Skip links are links that help screen readers (and others) to navigate to important areas quickly. There&#8217;s many different ways to implement them, here&#8217;s the Sharepoint way:

```html
<A href="javascript:;" onclick="javascript:this.href='#mainContent';" class="ms-skip">
```

The .ms-skip class positions it far off screen to the left, and the javascript&#8230; wait, javascript on a skip link? Why on earth did they not add #mainContent to the href attribute directly? Only they know&#8230;

Next in this post is a more philosophical piece of HTML. Look at this:

```html
<span dir="none"><table...>...</table>
</span>
```

I&#8217;ve heard about setting text direction to rtl (right to left), and ltr (left to right, for some eastern languages), but never to none. Where do text go that has no direction? Inwards? And what about having a table inside a span element?

ASP.NET also have user controls, a way to abstract out important pieces of code, to make reuse easy. Sharepoint of course uses this convenient tool regularly, and comes with a couple of useful ones:

```html
<SharePoint:SPRememberScroll runat="server" id="TreeViewRememberScroll"
onscroll="javascript:_spRecordScrollPositions(this);" Style="overflow:
auto;height: 400px;width: 150px; "> ...
```

In the [documentation for SPRememberScroll](http://msdn.microsoft.com/en-us/library/microsoft.sharepoint.webcontrols.sprememberscroll.aspx) you can learn&#8230; absolutely nothing about it. It seems to strangely interact with a TreeView somehow, and even worse, it has a width and height! I guess it&#8217;s good that it&#8217;s separate from the TreeView itself, so we can remove it from there if we want to forget where we&#8217;ve scrolled to. What?

Sharepoint 2007, note the year there, also both have the classical spacer gif and a new one; the spacer span:

```html
Spacer gif:
<td width="4px"><IMG SRC="/_layouts/images/blank.gif" width=4 height=1 alt=""></td>
Spacer span: <span style="width: 3px; height: 5px;"> </span>
```

Starting with the spacer gif: Luckily they have their width set twice, both on the image and the cell. Note the &#8220;4px&#8221; there, you can&#8217;t use CSS units when you&#8217;re writing HTML, HTML only knows about pixels. You&#8217;re glad you wrote the width twice now, right? The spacer span is a fairly new thing I guess, the strange thing here is that you can&#8217;t set a width and height on inline elements. It just doesn&#8217;t work, sorry.

If you&#8217;ve built your user controls really bad, you might need a way to let people customize its HTML to make sense. Sharepoint has a couple of different ways to do this, one that they use themselves like this:

```html
<SharePoint:DelegateControl runat="server" ControlId="PublishingConsole"
PrefixHtml="<tr><td colspan="4" id="mpdmconsole" class="ms-consolemptablerow">"
SuffixHtml="</td></tr>">
```

If you manage to read that, you can see that they are injecting a table row somewhere inside their control (which of course generates a table). Is it just me that feels the urge to add an ending table tag to SuffixHtml just to see what happens?

Another truly interesting interface construct is the datepicker. It&#8217;s one of these ordinary little calendar icons that opens in a little box and lets you pick a date. How did the Sharepoint guys (or girls) implement that?

```html
<...A href="#" onclick='clickDatePicker(<long id here>, <long url here>, ""); return false;' >
<IMG src="/_layouts/images/calendar.gif" border="0" alt="Select a date from the calendar.">
</IMG></A></td>
<IFRAME SRC="/_layouts/images/blank.gif" FRAMEBORDER=0 SCROLLING=no
style="DISPLAY:none;POSITION:absolute; width:200px; Z-INDEX:101;"
title="Select a date from the calendar."></IFRAME>
<td>...
```

Ok, lots of code to analyse here, and I&#8217;ve still only cut out the middle of a couple of nested tables. A link with an onclick that opens the datepicker is fairly standard, all parameters needed are encoded into a long url sent to that method. There&#8217;s an image to click, with a strange img ending tag, but that could have been a mistake. The strange thing here is the iframe that points to a blank image. It&#8217;s inserted into a table right **between** two cells (yes, you read that right). That&#8217;s just insane. If you for some sensational reason have to use an iframe to display some HTML, output it javascript instead of just setting the src with js. Seriously people. Nice accessibility feature though, to have the alt text both on the image and on the iframe. Twice as accessible!

Another not-so-fine interface implementation is the following: They want to show a heading and a list of links. Personally, I would have used a heading tag, and an ul with links in. Sharepoint does it like this:

![Black heading, list items with yellow dot before](/files/headingandlist.png)

```html
<div style="margin-left: 4px;">
<div class="level-header"><span id="header" class="headertitle">Division</span></div>
<div class="level-item-pos level-item level-bullet"><span id="header">
    <a href="<url>">Information Technology</a></span></div>
<div class="level-item-pos level-item level-bullet"><span id="header">
    <a href="<url>">Research & Development</a></span></div>
...
```

They break their own scheme of prefixing all their classes with &#8220;ms-&#8221; (something that severely messed up my header), they repeat ids, they use only divs and spans, and inline styles.

Do I need to say more? Want to spread the word? [Vote on reddit](http://www.reddit.com/info/6mepf/comments/).
