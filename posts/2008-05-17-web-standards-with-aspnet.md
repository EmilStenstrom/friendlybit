---
author: Emil Stenström
categories:
- HTML
date: 2008-05-17 11:46:33
guid: http://friendlybit.com/html/web-standards-with-aspnet/
id: 157
permalink: /html/web-standards-with-aspnet/
title: Web standards with ASP.NET
---

Good interface code is a mix of CSS and HTML, and while most frameworks offer full control over the CSS, they rarely offer that for HTML. This article looks at how ASP.NET developers can help their interface developers gain that control. Disclaimer: I'm no .NET expert, but too few people write about this stuff, so I'll make a try.

## Controls that keep the HTML customizable

Splitting pages into "controls" is a common way to build sites in ASP.NET. There's lots of different kinds of controls available, and I can't list all of them or name their differences. But I know I don't want to compile a .cs file every time a change some HTML. That pretty much rules out anything but **user controls** (as far as I know, but any kind of control that fills the above requirements would do). User controls have two sides, one for C# code (code-behind), and one for tags (HTML and calls to other controls).

There's also the issue of built-in stuff. ASP ships with many pre-built controls that help developers push out things quickly, the problem is that almost all of them neglect the HTML (DataList, GridView, …). They only allow setting a few properties, sometimes a CSS class, and assume that's OK. It isn't. I need full control over both the CSS and the HTML to be productive. There's one tag in particular is built with my kind of mindset, and that's the **Repeater**. A repeater is used like a for loop, but outputs no HTML itself. Instead it allows you to specify some code to output before the loop, inside the loop, every other step, and afterwards. That goes a long way, and that's often enough. If the predefined templates are insufficient, like if you want the last item to be rendered differently, you're out of luck.

I think I agree with the [MVC Framework guys](http://forums.asp.net/p/1239961/2263220.aspx) in how to solve missing parameters of default controls and bad output: Use C# code inside your templates. Why is this different than the spaghetti code of old ASP? Because you only use layout related logic, nothing else. People tend to think mixing C# and HTML looks messy, but isn't it stranger to make two very different things look the same?

There's also tags like asp:hyperlink, asp:label, and so on; tags that essentially does exactly the same as the HTML they're hiding. Please don't use them, there's no abstraction layer needed for HTML.

## Don't repeat yourself - not even in the interface code

Often when developers move from writing C# code to writing interface code they throw their coding skill out the window. You never copy a C# method just to make it output a different number - you make that number a parameter to the method instead. In the same way, you should never copy a piece of HTML from one place to another - move that code to a common masterpage or usercontrol instead. I've seen this many times, even from experienced developers. Never copy code, it makes for nightmare maintainance.

Also, use nested masterpages. So if you have three pages you need to build, and they have some code in common, you break that common code our into a masterpage. If two of the pages have even more in common you break that out into another masterpage, and let that one use the first one you made. Each Aspx page should only contain what makes it different from the other pages! Repeated HTML can also come in the form of small snippets of code, maybe 10 lines. You might not be able to break that out into a masterpage because it shows up all over the place. For those cases, break the snippet out into a usercontrol instead, and call that. Simple, and DRY.

## Disable viewstate

HTTP is by default stateless. That means that each HTTP request to the server knows nothing about all the other requests made. For scalability and performance, that's a great thing. By default, ASP.NET makes web development stateful. Every form field you fill out gets saved into a hidden form field, called viewstate, and sent with every request. But I'm not talking about performance here, I'm talking about interface development:

To be able to save state across requests there's a hidden form field, and to be able to send that with every request there needs to be a form covering **all** your form fields. I can't help to think that handling statefulness in the HTML (the view) is the wrong place to do it. Aside from taking away some of my control over the HTML, it also has accessibility issues. JAWS, a popular screen reader, switch to a different reading mode when inside of forms, and while it's possible to get to all content inside a form, it's harder.

So, start by [disabling viewstate](http://www.google.com/search?q=disable+viewstate) by default. If you must have it for a certain control, only enable it for that control.

## Summary

There's lots of stuff you can do to make the HTML look better with ASP.NET, and that's a good thing. The bad thing is that it isn't that way by default. Now get out of here and go build some good HTML :)
