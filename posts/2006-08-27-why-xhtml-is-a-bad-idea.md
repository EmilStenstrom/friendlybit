---
id: 89
title: Why XHTML is a bad idea
date: 2006-08-27T15:11:26
author: Emil Stenström
layout: post
guid: http://friendlybit.com/html/why-xhtml-is-a-bad-idea/
permalink: /html/why-xhtml-is-a-bad-idea/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205468624"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - HTML
---
XHTML is often mentioned when you talk about web standards of different kinds, and many believe that it's the future of the web. I'm of a different opinion and this article explains my reasoning.

  * [Some HTML history](#history)
  * [XML enters the scene](#xml)
  * ["Let's make HTML work like XML"](#xhtml)
  * [Problems with using XML on the web](#problems)
  * [We can't expect beginners to use XHTML](#beginners)

## Some HTML history {#history}

A long time ago, in 1990, the first pieces of HTML came to use. It was built specifically for scientific documents and contained nothing by structural elements. The idea was that the user should be the one deciding what a certain document looked like; after all, you read reports for their content, not for their looks. The target audience for HTML was pretty clear, scientists and other computer literate people: programmers in some sense.

The web soon became mainstream. Everyone has now surfed the web and lots of people have their own websites. But far from everyone care for code quality and most websites contain serious code errors. Despite the errors it's worth to remember than most sites "work", that is, they display like the authors want. All thanks to the error-handling of the current browsers.

An angry community of programmers/webmasters has complained about bad code since the beginning and demanded that we force people to only produce valid code. I've been a part of this group in the past…

<img src="/images/item_xml.gif" alt="XML icon" class="secondary" />

## XML enters the scene {#xml}

Around 1998 the specification for the XML language was released. XML is a language that makes it easy to construct your own languages. Think of it like HTML, but where you make up your own tag names, and where errors are not allowed. The programmers took it in as their new favourite and it spread quickly.

XML has very precisely defined error-handling (unlike HTML): when the parser finds something unexpected it just stops and displays an error. This means two things: it makes editing XML documents closer to "real programming" (if you make a small error it doesn't compile), and since you don't need code for error-handling the parsers become both faster and easier to write. As you can imagine the programmers felt at home.

## "Let's make HTML work like XML" {#xhtml}

W3C was founded and the programmers from the angry HTML community had made an impression on them. They decided to do something about the lousy code people wrote and standardized a new language for the web. XHTML takes the tags from HTML but adapts the language so that it becomes compatible with XML. The result is a language that can (and should) be parsed with an XML parser.

So all is well then? No. As you poke around you'll soon notice that it's pretty damn hard to get XHTML parsed with an XML parser in current browsers. Let me explain: to decide what parser to use you need to send the correct MIME-type from your server. If you're using PHP you can do it like this:

```php
<?php
if ( stristr($_SERVER["HTTP_ACCEPT"],"application/xhtml+xml") ) {
   header("Content-type: application/xhtml+xml");
}
else {
   header("Content-type: text/html");
}
?>
```

That pretty much asks the browser if it can handle XML and if it can sends the XML MIME-type "application/xhtml+xml". If it can't handle it (Internet Explorer 6 and 7 can't) it gets fed the old MIME “text/html” (and errors are tolerated and corrected).

But that’s not the only change you need. In the late 2004, Ian Hixie wrote [Sending XHTML as text/html Considered Harmful](http://hixie.ch/advocacy/xhtml) (quite technical). As you read through it you see that you have to change a lot more than the MIME if you want your XHTML to work as intended. Summary: doing it the right way is hard.

<img src="/images/item_invalid.jpg" alt="Screenshot of invalid XHTML" class="secondary" />

## Problems with using XML on the web {#problems}

So XHTML is hard to get parsed the intended way in current browsers. Instead most people using it decide (or don't know otherwise) to parse it like if it was HTML. But doesn't that defeat the biggest reason to user XHTML in the first place? The only big difference between HTML 4.01 and XHTML is that XHTML can be parsed as XML! _As long as you parse your code as HTML there's no reason to use XHTML_.

If we have a look at the specification of XHTML there's a little table displaying [what versions of XHTML that should be sent with what MIME type](http://www.w3.org/TR/xhtml-media-types/#summary). You'll see that it's ok to send XHTML 1.0 as text/html (may). But looking forward to later versions you see that they "should not" be sent as XHTML. So pretty soon, parsing XHTML as HTML will not be allowed if you want to follow the standards. That leaves parsing it as XML.

Imagine some kind of dynamic site that allows readers to add content to it. The comments of this site are a good examples. If I used XHTML (and parsed it properly) and someone used invalid code in the comments the page would break. New users to the site would get a big and ugly error message with a line number and some code. Totally unacceptable. So I would have to find a way to parse the HTML in my comments and fix errors that could break the page. Ok.

Next I copy-paste some text from a site I want to quote to you. When I publish the article I get a big ugly error message because the site I pasted used another character encoding and that breaks my XHTML. I research the problem and find that this could be fixed by parsing all text in my admin console and making sure it's valid UTF-8 before storing it in the database. Ok.

Next I download a bit of javascript and try using it on the site. Again people get an ugly error message in their face when they enter. It seems javascript is handled a lot stricter in XHTML and inline javascript needs some strange CDATA characters at the beginning and end of the script element. Ok, so I fix that too.

And like that it continues, tiny differences in code makes the page break over and over again, and bugs in the parsers I write makes people able to break my site by posting content. I have a computer science education behind me, so I could probably fix the errors and keep patching the site until everything works. But do I want to? What's wrong with the current way of fixing errors when I notice them when validating? And what about all the non-programmers?

## We can't expect beginners to use XHTML {#beginners}

As you've read above it's damn hard to get XHTML right. Still the W3C pushes for XHTML as the new standard for the web. Despite how hard it will be for beginners to get things right. Despite that you will move error handling to the parsers of each website instead of the browsers. Despite that XHTML has almost no backwards compatibility so pretty much **all** sites on the entire web will have to update their code.

No, I won't parse things as XML on the sites I build. XHTML was a bad idea from the start and I'd rather go with the new version of HTML developed under the name [Web Applications 1.0](http://whatwg.org/specs/web-apps/current-work/) (also known as HTML 5).

I hope this article explains why a lot of web development blogs (including Friendly Bit) use HTML. What language do you use?

> **Update**: More reasons why you should use HTML
