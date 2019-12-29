---
author: Emil Stenström
categories:
- JS
- Modern web
- Strategy
- Tutorial
date: 2007-03-10 00:59:52
guid: http://friendlybit.com/js/what-is-web-20-really/
id: 118
permalink: /js/what-is-web-20-really/
title: What is Web 2.0? Really.
---

Web 2.0 is really hot right now. One of Sweden's biggest newspapers recently wrote a long article on their debate section. They had started linking back to blogs that linked to them, in a little box next to the article. The problem was that they had got into trouble with what blogs to link to. After all, you can't just link to anything, right?

Aside from starting to think about the implications of blog links, I got another interesting question in my head. What is Web 2.0 really? Most people working with interface development would say that Web 2.0 is everything that uses AJAX. But the newspaper didn't use AJAX at all, and still they claim links to blogs is Web 2.0. Time for some research!

## The hunt for a definition

The phrase "Web 2.0" was first put into widespread use at an O'Reilly conference in 2004. The organizers wanted to talk about a change that has happened on the web, and just bumping the version of the web seemed like a good idea. Paul Graham found this [first try at defining Web 2.0](http://www.paulgraham.com/web20.html#f1n) at the conference:

> "While the first wave of the Web was closely tied to the browser, the second wave extends applications across the web and enables a new generation of services and business opportunities."

Note that there's no mention of AJAX there. Hell, there's no mention of users either! They must have meant something else, and the definition might have changed over the years since then. Let's keep looking for a good definition.

Tim O'Reilly comments on the issue two years later, in a [clarification on his blog](http://radar.oreilly.com/archives/2006/12/web_20_compact.html):

> Web 2.0 is the business revolution in the computer industry caused by the move to the internet as platform, and an attempt to understand the rules for success on that new platform. Chief among those rules is this: Build applications that harness network effects to get better the more people use them.

Tim acknowledges the change in meaning and talks about "network effects" here, something that starts to look a little bit more like what my idea of Web 2.0 is. But isn't there still something missing? To me, that looks only like a small part of what I call Web 2.0. Let's keep looking…

Gartner has tried to convince companies of the merits of Web 2.0 for a rather long time. In one of their many (business oriented) PowerPoint presentations they attempt to define "three anchor points around Web 2.0":

>   * **Technology and Architecture** — Consisting of Web-oriented architecture (WOA) and Web platforms.
>   * **Community** — Looks at the dynamics around social networks and other personal content public/shared models, wiki and other collaborative content models.
>   * **Business Model** — Web service-enabled business models, mashup/remix applications and so forth.

I believe we're getting closer. Gartner is making business models a separate point which I don't agree with. Many of the biggest Web 2.0 sites didn't have a business model when they started (and many still don't). Digg has troubles covering their hosting cost with the tiny bit of money they acquire from their ads. Del.icio.us still doesn't make any direct money (although they got sold to Yahoo, and they surely use the data…). My point is, a business plan isn't one third of Web 2.0, it's something sites add afterwards if things work out.

So let me state my own (slightly more general) definition of Web 2.0:

> "A collection of ideas and techniques that can be used to make more interactive sites"

The thing is, just doing something in AJAX does not mean it gets the Web 2.0 stamp of approval. You need several of the ideas or techniques and you need to combine them in clever ways. So lets agree on the definition above and got look for ideas.

## Ideas that are part of Web 2.0

I'd like to gather a whole bunch of ideas under the Web 2.0 roof. My selection is of course not all there is. Googling could uncover more I'm sure, but I think this is a good start.

  * [User generated content](#generated)
  * [Radical trust](#trust)
  * [Syndication of content and services](#syndication)
  * [Long tail](#tail)
  * [Collective intelligence](#collective)

### User generated Content {#generated}

Many companies still view the web as a one-way medium, an extension of a paper catalog, it's main advantage being that it can be distributed to more people. It's not like that any more! There are people that want to add content to your site, that want to contribute their ideas and thoughts. Why are you denying them to help you?

User generated content is content that your users are willing to give you. It can be everything from a simple "like it" or "don't like it", to fully featured articles written by users. The two most used ways of contributions are the simple ones: votes and comments. The author is still in full control of the content but users are given a chance to chip in with minor corrections. This is the least you can do. It's what I do on this blog; let you chip in by commenting.

But if you have users that are passionate about your subject, users that are willing to use your site to get their ideas out, you should really endorse that! Allow them to post articles on your site, allow them to regroup and re-prioritize according to their own wishes. It is technically possible, even rather easy to do; you just have to do it.

Six simple things your users can help you with:

  * Reviews of your products
  * Comments on your articles
  * Stories about how people use your product
  * Multimedia using your product
  * Questions about your products
  * Articles in an area you choose

### Radical trust {#trust}

<img class="secondary" src="/files/web20/wikipedia.png" alt="Logotype of Wikipedia" />

Another approach many sites have taken can be summarized as "radical trust". It builds on the simple idea that users know what they want better than you do. So let them order, categorize, sort, select your data as they like!

This is exactly what wikis do. They acknowledge that there are more users doing good than doing bad. If that's the case, why not let them in on your content directly, letting them edit and improve it like they want. They few people that do bad can be hunted away with a combination with versioning (saving old versions of content that's easy to restore), and some simple monitoring. Wikis trust users, do you?

### Syndication of content and services {#syndication}

Web 2.0 is not only about "user to website" interactivity. It's also about letting other sites and tools interact with your site directly. This is often summarized as "syndication".

It's a very fancy word for a simple concept. Let me try to explain.

Somewhere you have some kind of database with your content, be it products in your e-store or posts on your blog. Usually you take that content, add some structure (HTML) to it, and send it to the user.

Another website that wants to access the same information could parse the HTML and try to understand what it means, something called "screen scraping" (or microformats ;). The problem with that method is that it's very dependent on that the webmaster doesn't decide to change the HTML. The other problem is that computers and humans often want different types of information. A computer that is going to parse a list of your products doesn't need navigation like humans do. What you do is send your data directly to computers instead, without messing it up with HTML. Formats include: RDF, RSS, or perhaps custom XML through a Web Service.

Thing is, when you start syndicating your data you make it easier for others build services based on it. Now people get several entrances into your content instead of the one you produced. Again, your users are helping you reach more people.

Allowing full RSS feeds is another way of syndicating, I'm switching right now. Do you syndicate?

### Long tail {#tail}

<img class="secondary" src="/files/web20/tail.png" alt="Graph of a sold units per item" />

The theory of the long tail is one of the ideas that are usually associated with Web 2.0. It's a business model that many companies that are successful on the web use. As with most business models they are invented after the fact, and as such I'm not sure it really belongs on this list, but people always bring it up, so let’s go. I'll let you choose yourself.

Wikipedia describes the long tail like this:

> "Products that are in low demand […] can collectively make up a market share that rivals or exceeds the relatively few current bestsellers and blockbusters, if the store or distribution channel is large enough"

Most physical stores need to aim for the bestsellers to sell anything. There's simply too few interested in odd products, to make it worth hiring store space and personnel to sell it.

Web based stores are in a different position. Selling another product usually means just adding another page to your site, no extra store space or personnel needed. In addition people are prepared to wait a couple of days before receiving their products. That time span means you can skip warehouses and not start producing your products until you have an order ready.

No more is there a need to estimate what people will be interested in and pre-order them. For the right kind of product the internet is a huge benefit. Amazon did it with books, iTunes did it with music, do you do it?

### Collective intelligence {#collective}

You have let each user customize their experience and add content of their own. Now it's time to organize that content to better help the everyone benefit from it. There's hundreds of ways of doing it, but here's a couple of things that you can present to your users:

  * **The most popular Swedish article right now…** - Crawl all Swedish blogs and keep track of what they link to.
  * **Others that bought this book also bought…** - Query your shipment table. Pick a product, select the number of times each other product appeared together with said product, and recommend that product to your customers. Amazon does this and it's said that it has increased their profits considerably.
  * **You probably think this movie is a four out of five** - A Swedish movie site give its users personalized ratings of movies. They find users that have similar taste as you have (based on your previous grades) and then checks what those people have rated the movie as.
  * **This is probably spam** - Write a word filter that learns what is considered spam when users mark them. Share that filter with fellow users and let their markings stop your spam. A form of collective sieve filtering, Akismet does this.

None of them are technologically hard to do, you just Google and copy other people's samples. Why not?

## Techniques involved in Web 2.0

But there are techniques involved too. Let's go through a few of the important ones.

  * [AJAX (and other javascript)](#ajax)
  * [Feeds (RSS, Atom)](#feeds)
  * [Tags](#tags)

### AJAX (and other javascript) {#ajax}

Everyone talks about AJAX together with Web 2.0, but I think it's important they are kept separate.

AJAX is just a technology that helps prevent (full) page reloads. Instead you connect to the server silently in the background and receive your data that way. What's the revolutionary about this technique? Nothing. It has been in use for at least 5 years. They new thing about it is that people started using it to build better interfaces.

Javascript is language that enables AJAX, and playing with reloads is not all it can do. Through some nifty use you can change attributes on any HTML element on the page. Move things around, react to mouse movement, fade and animate, it's your choice. This means a lot of new controls become possible, ranging from simple sliders to interactive maps.

Why do most accessibility people hate it? Because most developers don't know enough about accessibility. And when those start to use AJAX they disregard accessibility completely. Javascript and AJAX have different goals and I think a good compromise is making sure the basic functions of the site (buy a product and pay for it) works without javascript, but enabling it adds additional features.

When was the last time you used javascript to enhance your site? What was the last control you invented?

### Feeds (RSS, Atom) {#feeds}

<img class="secondary" src="/files/web20/feeds.png" alt="The official feed icon" />

Feeds are great for syndication of content. There are many different feed formats to choose from but they all have one purpose: to communicate pure data, skipping all design.

A feed is simply a list of feed items, each with an unique identifier. A user adds the address to their "feed reader" and it starts polling you, asking for updates. I have my reader set to just a couple of minutes, making sure I quickly notice changes in people's feeds.

The good thing about feeds is that they make it easy to follow several at once. There's no annoying different designs in the way if you don't want to (you can always just visit the site if you want design). Feeds are getting more and more of a commodity; you should already be allowing your users the possibility to subscribe your content. Do you?

### Tags {#tags}

Tags is another hip concept. It deals with the collective intelligence idea and how to categorize content efficiently. A tag consists of a phrase of some kind that describes a piece of content. This blog post could have the tag "javascript".

There's several ways you can use them. One is the just fix what tags are allowed and use them as regularly groups you can assign content to. But allowing more than one tag enable you to do more than just split things into groups, you can instead pick all contents bits that have the same tag. You can go further, allowing custom tags that the users can pick themselves. That gives you a wide array of descriptive words for your content, free to play around with. For example, if many users pick the same word, that one is probably a better descriptor.

Picking many bits of content and analyzing all tags tied to them can be easily done with a tag cloud. In that you simply print all tags used after each other, and make those used often bigger. Doing this on a whole site is an effective way of giving users a snapshot of what you write about, something I know I like.

Can tags help you solve a categorization problem you have?

## Summary

Now. To build a Web 2.0 site, pick from both of the lists above. You Google for more ideas and you work hard to interact with your users as much as possible. Web 2.0 is the combination that happens when your ideas and technology finally just works.

Your users want to help you, do you let them in?
