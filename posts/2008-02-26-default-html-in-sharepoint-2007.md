---
id: 151
title: Default HTML in Sharepoint 2007
date: 2008-02-26T00:27:33
author: Emil Stenström
layout: post
guid: http://friendlybit.com/html/default-html-in-sharepoint-2007/
permalink: /html/default-html-in-sharepoint-2007/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205287362"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - HTML
---
As I&#8217;ve said before, I&#8217;ve been [spending time with Sharepoint 2007](/css/sharepoint-2007-from-an-interface-developers-view/) recently. The HTML it produces is really bad, and today I thought I show you just how bad.

Sharepoint 2007 has been &#8220;updated&#8221; to support [masterpages](http://msdn2.microsoft.com/en-us/library/wtxbf3hh.aspx), a concept from .NET 2.0. Sharepoint&#8217;s implementation of masterpages has several problems, but none of them even come close to the biggest problem of them all: default.master.

Default.master is the page that ships with Sharepoint and is used everywhere by default. A quick glimpse at it would make any seasoned web developer feel sick, and I quickly replaced it with something homemade. If you keep reading you will see why. Let&#8217;s get going with the first line:

<div class="incorrect">
```html
<HTML xmlns:o="urn:schemas-microsoft-com:office:office"
dir="ltr" __expr-val-dir="ltr">
```
</div>

Things start out really bad, without a doctype on the first line. This mean that all default pages will render in [quirks mode](http://en.wikipedia.org/wiki/Quirks_mode), making rendering unreliable across browsers. Next they set an XML namespace, which after some googling points to very [thorough documentation (pun intended)](http://msdn2.microsoft.com/en-us/library/ms875215(EXCHG.65).aspx). So they mean that it&#8217;s an XHTML document? No, because XHTML has lowercase tags, and here they use uppercase. The attribute <span class="incorrect">`__expr-val-dir`</span> just doesn&#8217;t exist.

A hardcoded link to the 4000 line &#8220;core.css&#8221; (filled with classnames you have to override by hand), and five external hardcoded javascripts then follow. Then 30 lines of inline CSS and javascript. Then comes the next real beauty, the body tag:

<div class="incorrect">
```html
<BODY scroll="yes" onload="javascript:
   if (typeof(_spBodyOnLoadWrapper) != 'undefined')
   _spBodyOnLoadWrapper();">
```
</div>

The funniest thing here is the scroll attribute. Let me paraphrase [html.com](http://html.com/attributes/body-scroll/) (found through quick googling):

> SCROLL, which is only recognized by MSIE, indicates if there be scroll bars on the page. The default value is YES, so the only reason to use SCROLL is to set it to NO. SCROLL serves little purpose except to confuse and annoy readers by removing scroll bars which are there for a good reason.

I couldn&#8217;t have said it better myself. There&#8217;s no reason, whatsoever, to use the scroll attribute. Ever. Especially with &#8220;yes&#8221; set. _Pause for deep breaths_. Then we have the inline javascript. Did you know that you could put javascript: inside of onload? Despite all odds, it seems to work. _spBodyOnLoadWrapper() is by the way Sharepoint&#8217;s way of letting you add javascript to pages. You first do a <span class="incorrect">`_spBodyOnLoadFunctionNames.push("YourFunctionName");`</span>, and then that code will get run. Insane.

Then we have the typical ASP.NET form, encapsulating the whole page, followed by 18 hidden HTML fields (including the infamous viewstate). Directly afterwards, we have a 60 line mix of inline and external javascript, contained in 7 different code blocks (two that&#8217;s missing the type and language attribute).

The next discovery can be found three _nested tables_ later:

<div class="incorrect">
```html
<span id="TurnOnAccessibility" style="display: none">
   <a onclick="SetIsAccessibilityFeatureEnabled(true);
   UpdateAccessibilityUI();return false;" href="#"
   class="ms-skip">Turn on more accessible mode</a>
</span>
<a onclick="javascript:this.href='#mainContent';" href="javascript:;">
class="ms-skip" AccessKey="J">Skip to main content</a>
```
</div>

I&#8217;ll wait until you regain consciousness. Hi, welcome back. Yes, they are using <span class="incorrect">`display: none`</span> and javascript calls to enable &#8220;accessibility mode&#8221;. I mean seriously, screen readers ignore things with display: none set, and we can certainly not always trust that javascript is enabled. I also love the skiplink, and how it sets its own href attibute to an internal link. Note how this code is (mostly) lowercase.

And this is where it starts to get ugly. Every Sharepoint page has a Personal menu and a Site menu on it, containing things you want to do with your account or the current site. Fair enough. This is the (rather lengthy) code for the Personal menu:

<div class="incorrect">
```html
<span style="display:none">
<menu type='ServerMenu' id="zz3_ID_PersonalActionMenu"
   largeIconMode="true">
      <ie:menuitem id="zz4_ID_PersonalInformation"
      type="option" iconSrc="/_layouts/images/menuprofile.gif"
      onMenuClick="javascript:GoToPage([url]);return false;"
      text="My Settings" description="Update your user information, regional settings, and alerts."
      menuGroupId="100"></ie:menuitem>
      ... [three more "ie:menuitem"] ...
   </menu>
</span>
<span title="Open Menu">
<div  id="zz8_Menu_t" class="ms-SPLink ms-SpLinkButtonInActive"
   onmouseover="MMU_PopMenuIfShowing(this);MMU_EcbTableMouseOverOut(this, true)"
   hoverActive="ms-SPLink ms-SpLinkButtonActive"
   hoverInactive="ms-SPLink ms-SpLinkButtonInActive"
   onclick=" MMU_Open(byid('zz3_ID_PersonalActionMenu'), MMU_GetMenuFromClientId('zz8_Menu'),event,false, null, 0);"
   foa="MMU_GetMenuFromClientId('zz8_Menu')"
   oncontextmenu="this.click(); return false;" nowrap="nowrap">
      <a id="zz8_Menu" accesskey="L" href="#" onclick="javascript:return false;"
      style="cursor:pointer;white-space:nowrap;"
      ... [five more eventhandlers] ...
      menuTokenValues="MENUCLIENTID=zz8_Menu,TEMPLATECLIENTID=zz3_ID_PersonalActionMenu"
      serverclientid="zz8_Menu">
         Welcome Emil Stenström<img src="/_layouts/images/blank.gif" border="0" alt="Use SHIFT+ENTER to open the menu (new window)."/>
      </a>
      <img align="absbottom" src="/_layouts/images/menudark.gif" alt="" />
   </div>
</span>
```
</div>

There&#8217;s several things worth a note here (in a bad way). The menu tag Sharepoint uses is in fact a real HTML tag, [deprecated in HTML 4.01](http://www.w3.org/TR/html401/struct/lists.html#h-10.4). Inside of that we have a tag called ie:menuitem that I really can&#8217;t understand. What on earth is ie:menuitem? Did they intentionally not make it work in other browsers? Everything is wrapped inside a <span class="incorrect">`display: none;`</span> As you see, tags are also cluttered with event handlers, both real and made up ones. The contextmenu is blocked twice, and a spacer gif is used to add alternate text to the link. The menu icon is hardcoded into everything.

It goes on in the same manner, with tables with the &#8220;TOPLEVEL&#8221; attribute (and no value), divs with a WebPartId set, PlaceHolder tags rendered directly out in the HTML (instead of parsed by ASP.NET), to end with 200 lines of mixed inline javascript and css. Everything embedded in several layers of nested tables.

## In conclusion

Default.master contains the worst code I&#8217;ve ever seen, and it&#8217;s really disappointing to see that from a product with &#8220;2007&#8221; in it. Microsoft have failed in every possible way when it comes to the interface code, and I believe the only way out is to rebuild Sharepoint from scratch (not likely to happen). Having to work with Sharepoint is a real pain, and I honestly don&#8217;t recommend it to anyone. Put your curiosity to use into something more interesting, like the [ASP.NET MVC Framework](http://weblogs.asp.net/scottgu/archive/2007/10/14/asp-net-mvc-framework.aspx) instead. Thanks for listening.
