---
id: 155
title: Fixing Sharepoint 2007
date: 2008-03-27T23:22:53
author: Emil Stenström
layout: post
guid: http://friendlybit.com/other/fixing-sharepoint-2007/
permalink: /other/fixing-sharepoint-2007/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205287421"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - Other
---
I&#8217;m sorry for all the Sharepoint 2007 posts lately, if you&#8217;re not interested, just skip to the next post :). Anyway. The Sharepoint team recently announced further support of an addon called Accessibility Kit for SharePoint (abbreviated AKS) in a blog post about the future of Sharepoint on their official blog.

I thought I&#8217;d comment on the future plans, and get a bit more constructive and point to things that are rather easy to fix. Perhaps I can affect what gets focus in the next version? With a release cycle of 30-34 months (!), any changes won&#8217;t get implemented anytime soon, but I guess getting on the right track is a first step.

## Shift focus from accessibility to customization

First of all, I&#8217;ve only briefly touched accessibility on my two posts about Sharepoint ([Default HTML in Sharepoint 2007](/html/default-html-in-sharepoint-2007/) and [Sharepoint 2007 from an interface developer’s view](/css/sharepoint-2007-from-an-interface-developers-view). But to me, accessibility is the second step, being able to customize things, is the first. Let me repeat that **I care more about being able to customize the Sharepoint interface, than the default interface being accessible**. Right now, large parts of the interface are locked down, deep inside of the Sharepoint core. If I could customize things, I could correct the accessibility issues myself. I really think the focus should be customization first, and accessibility second.

## But it&#8217;s possible to customize some parts!

Lots of people have commented on my previous posts saying that it in fact _is possible_ to get Sharepoint to produce valid HTML. It&#8217;s possible to some extent, by rewriting all masterpages and many default controls that come with Sharepoint. Of course you can build a good interface if you only use Sharepoint for storage, and build the interface from scratch. But that&#8217;s skipping a lot of the things you bought Sharepoint for, all the existing components!

And you still can&#8217;t change the collaborative parts. And as soon as you want to add content to the site or change settings, you&#8217;re back in lock-in, no control, Sharepoint interface land.

## Deliver as a service pack, not an addon

So, back to the announcement. I think it&#8217;s a shame that AKS is delivered as an add-on, and not as a service pack to Sharepoint. Accessibility is a user concern (they are the ones that need stuff done), not one that developers desperately need. So the focus should be to push this one to as many users as possible, and make it very easy to enable it for developers. A service pack would accomplish that much more effectively than an addon does. Most developers won&#8217;t even know the addon exists!

## Control adapters are not the best solution

In the announcement is something called Smart adapters, from what I understand a way to automate replacing .NET controls with your own controls. So when Sharepoint calls that breadcrumb control, you redirect it to call your own breadcrumb instead. The problem here is that I have to rebuild the whole control from scratch, instead of just changing how it&#8217;s output.

Instead, if Sharepoint could expose a .NET List (the breadcrumb links) to me, I could decide the rendering myself. That&#8217;s customization!

## Don&#8217;t repeat yourself, use master pages

More suggestions of changes: One of the biggest annoyances in Sharepoint is the bad implementation of master pages. Sharepoint only allows each site to have one Master page set, so you really can&#8217;t use your master pages for controlling things like number of columns. Putting that in the masterpage would means you would need to use that number of columns on all your pages. In Sharepoint, you instead have to wash out the bare essentials that all your pages have (a html and body element?), and set that in the masterpage. If two of your pages are similar, copy/paste the code between them. Terrible! What I want to be able to do, is to set several masterpages per site, and use inheritance between those masterpages. That&#8217;s fundamental master page concepts, that Sharepoint is lacking.

## Organization of CSS and Javascript

When you ship code to your customers (Sharepoint is a framework, so Microsoft is essentially selling code to developers), you need to make sure that code is readable, and understandable. That does not only apply to C# code, it applies to the full interface as well. That&#8217;s simply not the case with Sharepoint. There&#8217;s two humongous files, core.css and core.js, where most CSS and Javascript have been poured into, with no consideration of organization or namespaces. There&#8217;s no indication how certain C# components interact with the CSS and Javascript and very very little documentation (often added after the fact, by annoyed developers like me). This just **have to change**, we need organization, modules, separation. We need an interface that we can understand without reverse engineering!

Another thing, releasing controls that are thought to be reused, really mean that they need to work in [standards mode](http://www.quirksmode.org/css/quirksmode.html). All controls, even webparts. It isn&#8217;t reasonable to have to [patch things inside your Javascript chaos](http://blogs.msdn.com/feldman/archive/2007/11/18/sharepoint-doctype-and-master-pages.aspx) to make basic things work! It isn&#8217;t reasonable to have to patch CSS for standards mode either. It shouldn&#8217;t have relied on quirks mode in the first place!

## Examples are good, but&#8230;

The announcement also mentions examples. Releasing examples of how to make Sharepoint validate, conform to WCAG 2.0 AA (really?), or any other standard, can of course be of help. A lot more help than no documentation. But it&#8217;s also pushing over the problem to the customers. &#8220;We couldn&#8217;t make our product validate, but you can fix that, but doing this, this, then this, and that&#8221;. A default site shouldn&#8217;t have 200 errors out of the box, you can do better than that.

## WYSIWYG editor and Firefox

The Accessibility Kit also mentions a new WYSIWYG editor, &#8220;aRTE&#8221;, that can be used instead of the default editor. It&#8217;s of course well needed, the default editor doesn&#8217;t work at all outside of Internet Explorer, and I really doubt that it&#8217;s accessible. So why is this released as an addon? You&#8217;ve built a better content editor, give it to people!

Also, the new editor takes you another step closer to supporting Firefox. You&#8217;re pretty near, but not being able to edit content in a CMS with Firefox really is bad. That should be the baseline. Really, I could understand if the ActiveX über-COM Silverlight Vista integration didn&#8217;t work, but editing content, or maybe interacting with webparts? To cling to Internet Explorer in this day and age is not going to work.

## In summary

I hope that some of the improvement areas mentioned in this post will be taken into consideration in the development of the next version of Sharepoint. My tone is harsh, but that&#8217;s because I&#8217;ve really been slowed down my Sharepoint in my daily work. Customers complain because tiny interface changes takes days to complete. I hope you can see past my frustration, and see that there are big areas where you really can improve how Sharepoint work. I&#8217;m willing to help pointing in (what I think is) the right direction.
