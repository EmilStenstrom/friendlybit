---
id: 276
title: Yellow fade with CSS and a simple image
date: 2008-10-04T20:19:09
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=276
permalink: /css/yellow-fade-with-css-and-a-simple-image/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205287784"
btcnew_comment_counts:
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
Via [Think Vitamin](http://www.thinkvitamin.com/features/css/stay-on-target) I find a cool way to highlight the current element. Lots of people do this by calling some kind of javascript library, it&#8217;s so common it&#8217;s been dubbed the [yellow fade technique](http://www.37signals.com/svn/archives/000558.php). But javascript isn&#8217;t really needed, you just need CSS and an image.

<p id="example">
  First: you can jump to any id on the current page by appending #some-id-here to the url. This includes all the &#8220;semantic&#8221; ids you&#8217;ve added to the page such as #content, #sidebar, and so on. Very useful if you want to point out a certain section of a page to a friend, just look at the source, try to find an id nearby, and add it to the url.
</p>

If you want to make things even easier on your own site, you can visually highlight things that get referenced via the above method. That&#8217;s where the :target psuedo selector jumps in to save your day. Please note that :target is CSS3, and only currently works in [non-crap browsers](http://reference.sitepoint.com/css/pseudoclass-target). But perhaps this effect is something not all users really need?

```css
a:target {
   background: #234af5;
}
```

This highlights all links that get referenced via the URL with a nice blue color. So they need an id added. Makes perfect sense for all kinds of documentation where you want to refer someone to a certain method or even sentence.

But it gets better:

```css
:target {
   background: url("/images/yellow-fade.gif");
}
```

We&#8217;ve removed the limit of only targeting links with by using :target straight off. So all targeted elements will get affected by this rule. What next? Well, we use a small animated image to fade from one color to the next. It&#8217;s a really easy way to add dynamics to a page.

Try the effect by [jumping to the code example](#example) above.

I really think this makes internal links a whole lot more useful, especially for jumping to the bottom of the page, where it&#8217;s not possible for the browser to scroll down enough to get the targeted element to the top. Needless to say, I&#8217;ve added this effect to this site too. Hope you can find something to use it for too.
