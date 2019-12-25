---
id: 323
title: Templated User Controls in ASP.NET
date: 2008-11-18T01:28:43
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=323
permalink: /other/templated-user-controls-in-aspnet/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205287889"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - HTML
  - Other
  - Tutorial
---
Good design repeats itself. It works hard to convey a whole, a feeling of consistency. Once you understand a part of such a design, you know your way around all of it. This is often done by repetition, using the same elements, colors, styles, positioning, and so on. This is a good thing.

Good code [never repeats itself](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself). The number of techniques to avoid it are numerous, and all new languages compete in trying to remove as much repetition as possible (Especially the dynamic ones).

**Good design repeats itself, good code does not.**

With interface development, you **face the conflict** above over and over again. You get a design that (rightly) reuses the same concepts over and over, and you need to implement them in code that makes you write the same logic only once. This same time both when writing the code and later when fixing bugs in it, and deep inside, all programmers know that it&#8217;s the correct way to do things.

I&#8217;m currently working in a .NET project (EPiServer CMS 5), and is faced with a design that uses the same kind of boxes all over the site. The boxes only differ by color and content, so things like shadows and rounded corners are clear repetition that I want to do only once. I&#8217;ll do the shadows and corners with CSS, but for that I need a couple of wrapper divs. Divs that I only want to specify once, and then reuse.

The prequisites are:

  1. I want a **flexible** solution, so I&#8217;m not tied to a specific HTML structure (number of divs, or even if I use the div tag or not).
  2. **No HTML in properties** that get sent to user-controls
  3. **No HTML in code-behind** (a common way in .NET to split logic (code-behind) and templates (ASP.NET and HTML))

What I came up with was [templated user controls](http://msdn.microsoft.com/en-us/library/36574bf6.aspx). They provide a way to write controls that wrap any other controls you may have, and add content around them. And it&#8217;s easy to write and user. This is how the one I wrote is used:

```aspx-cs
<MyProject:Box runat="server">
    <Contents>
        <h2>Random header...</h2>
        <asp:Repeater runat="server">...</asp:Repeater>
        ...
    </Contents>
</MyProject:Box>
```

It simply wraps anything inside it (in this case a heading tag and a asp repeater), and lets me do whatever I want with them. In my case, I wanted to add some generic HTML around lots of different content, but you could do anything you wanted.

This is how the above was implemented. First the code-behind:

```csharp
using System.Web.UI;
namespace MyProject.templates.units
{
    [ParseChildren(true)]
    public partial class Box : System.Web.UI.UserControl
    {
        private ITemplate contents = null;
        [TemplateContainer(typeof(TemplateControl))]
        [PersistenceMode(PersistenceMode.InnerProperty)]
        [TemplateInstance(TemplateInstance.Single)]
        public ITemplate Contents
        {
            get
            {
                return contents;
            }
            set
            {
                contents = value;
            }
        }
        void Page_Init()
        {
            if (contents != null)
                contents.InstantiateIn(PlaceHolder1);
        }
    }
}
```

&#8230; and then the &#8220;code-front&#8221;:

```aspx-cs
<%@ Control Language="C#" AutoEventWireup="true" CodeBehind="Box.ascx.cs" Inherits="MyProject.templates.units.Box" %>
<div class="box">
    <div class="boxwrapper">
        <asp:Placeholder runat="server" ID="PlaceHolder1" />
    </div>
</div>
```

I think this is a **really useful** way to write user controls, especially for those of you that work as interface developers in a .NET world. Asking the people around me I found that quite a few didn&#8217;t know how templated user controls worked, so I hope I will be of use to some of you out there. Happy coding!
