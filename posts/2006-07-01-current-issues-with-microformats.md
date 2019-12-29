---
id: 74
title: Current issues with Microformats
date: 2006-07-01T17:52:06
author: Emil Stenström
layout: post
guid: http://friendlybit.com/html/current-issues-with-microformats/
permalink: /html/current-issues-with-microformats/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205621548"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - HTML
---
A couple of weeks ago I attended [Geek Meet](http://www.robertnyman.com/geekmeet) in Stockholm. It's a small group of people gathering to talk about semantics and share their knowledge of front-end webdev. It was the second meet and, just like on the last one, I had a great time. It's something special meeting up with people that share your interest for the small niche front-end web development is.

On that meeting [Peter Krantz](http://www.peterkrantz.com/) held a presentation about microformats, a way to standardize small snippets of HTML you use often. What was different with the presentation is that it wasn't just praise like many new techniques get. The presentation showed both the good and bad sides, and didn’t close with a final conclusion of whether it should be used or not. This article is my view of microformats (and includes some of the issues from Peter’s presentation).

## What are microformats?

Microformats are small standardized snippets of HTML. They are standardized to make it easier for crawlers/robots to find certain types of information. One idea could be to make contact information easier to find for a robot and letting anyone build a directory out of this information. Browsers could support this and display information in some special way. Sounds like a pretty good idea to start with, doesn't it?

Microformats are not restricted to contact information, hCards. There's also hCalendar for description of events, hReview for reviews of things and so on. You'll find the full list on the [microformats wiki](http://microformats.org/wiki/Main_Page).

An example of a hCard:

```html
<div class="vcard">
   <a class="url fn" href="http://tantek.com/">Tantek Çelik</a>
<div class="org">Technorati</div>
</div>
```

## Serious problems with the format

Microformats are not perfect. The first problem is that they don't use namespaces. Namespaces are some way of describing what you mean with a word and in this case it applies to the class name of the formats. Check the example above. If you wrote a robot, how would you recognise an hCard? The only information available is the class name of the above. This means you would need to search each page for that class name. This is quite inefficient from a parser’s point of view.

What's worse, this means no one can use the class name "vcard" on their pages, that would make the robots get faulty information. Even this post probably breaks a few parsers because the code example above looks pretty much like an hCard. I hear the counter argument, "but no one uses vcard as a class name if they don't use it for that", I can only tell you I just did.

Multiplying the damage of not using namespaces is versioning. Compare with HTML, where in early versions of HTML a [Doctype](http://hsivonen.iki.fi/doctype/) was not needed. Then the authors decided that the format needed an update, and with the update new elements were added. Without a doctype the browsers couldn't tell the difference between the formats and the doctype was added in. This is exactly what will happen with hCard (or any other microformat that doesn't use namespaces) if needs to get updated.

Is versioning a problem? Not if the format is perfect from the start, without any kinds of problems that need to be fixed in future releases. You see where this is going right?

Except for the issue with namespaces and parsing of class names we also have dates. Dates with time included are in the hCalendar format marked up with the abbr element. It looks something like this:

```html
<abbr class="dtstart" title="20060621T1030-0700">21 june 10:30</abbr>
```

Is the title attribute used correctly here? I think not. The abbr element is meant to give users that do not know what a certain term/expression stands for a short explaination. In the example above it's not easy guessing that "T" stands for time and that the number afterwards is a notation of time zone (GMT-7 or PDT-7?). All of this is of course possible to read from the ISO specification, but people hovering your link will not do that. The title attribute on abbr elements should be humanly readable!

If you still don't agree with that you can check out ISOs own text about ISO 8601. Under "Advantages of ISO 8601" you can see:

  * Easily readable and writeable by systems
  * Easily comparable and sortable
  * Language independent
  * Larger units are written in front of smaller units
  * For most representations the notation is short and of constant length

While all of those are good points, none of them have anything to do with being easy to read for a human. This is the very point of the title attribute of the abbr element. For the sake of discussion Tantek wrote about the [choice of ISO 8601](http://tantek.com/log/2005/01.html#d26t0100 "Reasons behind choosing ISO 8601 for microformats") when the use of title was included.

## Improving the format

The idea of making it easier for robots to parse pages is a good idea, but I'm not sure embedding content for robots into the human content is the best solution. What about putting this information into your [web feed](/feed/ "Friendlybit's web feed") instead? Feeds are made to be readable by robots and since they are xml they can easily be expanded with new types of data.

If I were to consider microformats I would like the two main issues above to be fixed first. _Add some kind of namespaces to the formats_ and make them required. One idea would be to use a meta element for each format you want to use inside the document. The name is the format you use, the content is what version you are using, and the scheme is a link to the [microformat profile](http://microformats.org/wiki/xmdp-brainstorming) that corresponds to that format. Note that the use of this element should be required, not optional.

It would look something like this (you can of course use several formats by repeating the meta element):

```html
<meta name="hCard" content="1.0" scheme="http://www.w3.org/2006/03/hcard">
```

The second improvement would be to _use something else than the title attribute for the dates_. Titles should be used for human readable content, not machine readable so that needs to change. Switching to another format for dates seems like a bad idea since ISO 8601 is so widely spread. So, what to do? I'm not sure. My best bet would be to use the class attribute like most of the microformats are built up on. The dates do not have a space in them so they can be parsed just like other class names.

## Conclusion

Even though microformats are basically trying to make it easier to parse the web (an idea I like) I'm not sure this is the right way of doing it. Human and robot content are most often different things and mixing those in the same document could mean you end up with a mess. I have not touched upon all the extra divs and spans microformats add to the code but that's also a sign that we're moving the wrong way.

If the authors of microformats want their formats to spread they need to fix the two issues above. The two suggestions of improvement I made above would make me consider using them. Right now I don't feel it’s worth it.
