---
id: 87
title: KTH goes web standards
date: 2006-08-23T00:36:28
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/kth-goes-web-standards/
permalink: /css/kth-goes-web-standards/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205286224"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - HTML
---
Sweden&#8217;s [largest technological university, KTH](http://www.kth.se), just launched their new site and I&#8217;m proud to say that I&#8217;ve been responsible for the HTML and CSS for it. I&#8217;d thought I&#8217;d take some time and tell you about the techniques I used and the reasons behind using them. Let’s start with some background:

[<img src="/images/item_kth.jpg" alt="Blue KTH logotype" class="secondary" />](http://www.kth.se)

## About KTH

KTH is an initialism for &#8220;Kungliga tekniska högskolan&#8221; which translates to &#8220;Royal Institute of Technology&#8221; in English. It&#8217;s the biggest technology focused university in Sweden with almost 17000 registered students for 04/05 ([source](http://www.scb.se/statistik/UF/UF0205/2005A02/Web_GR1_RegUnivKon.xls "Number of registered students on KTH")). Add over 3000 employees to that and you&#8217;ll start to see the number of people affected by the update. KTH hosts a lot of content, [Google reports 1,930,000 pages](http://www.google.com/search?hl=en&q=site%3Akth.se). Not all pages are included in current the update, but it gives a pointer to what kind of site we are looking at. In summary, a standards based update of KTH affects a lot of people.

## Polopoly and the HTML

I entered the project quite late in the process ([Valtech found me](/css/valtech-my-new-employer/)), about a month before launch. Most of the back-end work had already been completed and authors responsible for different parts of the organisation had started filling the database with content. The CMS used was a platform known as Cortina, based on top of the CMS framework [Polopoly](http://www.polopoly.com).

Everything was modular and the changes I wanted to do to the HTML nicely cascaded out over the site. When you look at the HTML you&#8217;ll notice that it contains a lot of strange whitespace, making the code somewhat difficult to read. That&#8217;s because of the template language used, [JSTL](http://java.sun.com/products/jsp/jstl/), which leaves whitespace after each element. I therefore recommend using the [HTML validator extension for Firefox](http://users.skynet.be/mgueury/mozilla/) , selecting view source, and then using the button &#8220;Clean up the page&#8221; in the bottom right corner. That makes the code a bit easier to read for you on the outside. I hope you won&#8217;t be too upset over that :)

You&#8217;ll find that all new pages validates as HTML 4.01 Strict (or at least very close, I know of some ampersand encoding errors on one page) and I&#8217;m very proud of the outputted HTML. It maps the structure of the content nicely and is easy to browse without CSS enabled. It contains very few elements that are there just as &#8220;style hooks&#8221; and the id and class names describes the contents of the elements, not their design.

## CSS and the techniques used

The new site makes full use of CSS for its layout. We targeted mainly Firefox 1.5 and Internet Explorer 6 with the new site but using web standards I wouldn&#8217;t be surprised if it works well in other modern browsers too. For those of you that like fancy terms I can say that the site is a fixed width, zoomable, source ordered, 3 column equal height layout. I&#8217;ll talk a little about the fancy terms above and explain the reasoning behind them.

<img src="/images/item_ruler.jpg" alt="Image of a Ruler" class="secondary" />

### Fixed width layout

Let&#8217;s start with the most controversial of the design decisions. The site is optimized for 1024&#215;768 pixel resolutions and up. This was a hard decision but given the content of the site, the design at hand, and the target audience we felt that it was a good one. Let me explain our reasoning:

KTH has a lot of information to display. Many different parts of the site need to get exposure and the wider 1024 format made that possible. Many of the images were also designed for the wide format and changing the width would mean we would have to examine all of them and decide how to cut each one. Surf around on the site and you&#8217;ll see the problems that would bring. Objects in images, meant to be centered, would be offset and some items would be cut. Those content and design issues, together with the somewhat &#8220;technological&#8221; target audience, convinced us that 1024 was the right decision.

### Zoomable layout

We wanted to make the user able to change the font-size if they wanted to. This meant that quite a few boxes needed to expand with the text, to prevent the text from overflowing them. This was solved by selectively using em units making the boxes expand with the text-zoom. This worked well, and I&#8217;m especially proud of the [front-page](http://www.kth.se "KTH:s front-page"), with all the different elements expanding and collapsing together. There are a few glitches in the zoomed layouts, a couple of pixels missing here and there, but from the testing we have done those are few (there’s currently one line too much content in the middle box, making the zooming uneven, don’t worry about that :).

<img src="/images/item_order.jpg" alt="List of groceries in order" class="secondary" />

### Source ordering and skip links

The layout is a rather typical 3 column layout with a header and footer. The leftmost column is for navigation, the middle one for the real content, and the right one for additional information. In terms of importance the content is the most important, followed by the additional information column, followed by the navigation. This called for use of a technique known as source ordering, having the content in one order structurally and in another visually.

Using source ordering is a good way of making it easier for non visual browsers (screen readers, text browsers, and search engines) to get the most important information first. This is not the right article to explain the method in full (some wrapper divs and some clever floats); I&#8217;ll save that for a later article. Anyway, what matters is that there are some advantages to using this method and that we decided to use it.

Others prefer to be able to jump to whatever place in the source they want. For this, &#8220;skip links&#8221; are quite effective. Skip links are internal links (links pointing to an id somewhere on the same page) that you put in the beginning of the HTML. Clicking the link moves the focus to the corresponding place in the content. We felt that this was a simple way to provide navigation for users with CSS disabled. The skip links where hidden for everyone else.

### 3 column equal height

As many of the column layouts today this one was made with all columns of equal height. It&#8217;s a common complaint amongst the &#8220;table for layout&#8221; users that these kinds of layouts are too hard to do with CSS. They are not. An easy technique for doing this is known as [faux columns](/files/templates/?style=faux_columns&cols=3&nofooter=1) and is simply: putting your columns in a wrapper, floating them left, and setting a background image in the wrapper. The wrapper expands whenever any of the columns expand and shows more of the tiled background image as needed. It&#8217;s a simple technique, it works well, doesn’t contain any hacks, and is easy to learn. CSS vs. Tables: 1 &#8211; 0.

<img src="/images/item_matrixd.jpg" alt="One of the 5 layouts available" class="secondary" />

### Front page grid

One of my favourite parts of the site is a feature that most users only will notice over time: The top left part of the front page can be switched between five different layouts, depending on what the editors feel fits their content best. This means that the editors are given a big chance to &#8220;design&#8221; the front page; a very nice move from the designer.

For me, as the one responsible for implementing this, I had a couple of though days. But I learnt a lot and ended up using a min-height set with em units on the different boxes. This way I could make boxes at totally different parts of the page zoom together. IE6 handles height as min-height so setting &#8220;fixed&#8221; heights in a separate file for IE ensured that the design worked there too. After using and testing this method for a couple of weeks I must say that I like the it, it gives me a nice grid to work with, but not a fixed one as with tables. This one expands depending on what the content requires. I recommend you to try it out.

### Conclusion

The developers behind the new KTH website have constructed a site that was incredibly fun to work with. I consider myself lucky to having worked with such a good team and have learnt a lot in the process.

Also, as a student of KTH for many years I know that the site will be well received by fellow students; and at the end of the day, isn’t that what matters?
