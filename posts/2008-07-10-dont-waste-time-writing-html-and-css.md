---
id: 169
title: 'Don’t waste time writing HTML and CSS'
date: 2008-07-10T00:02:50
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=169
permalink: /css/dont-waste-time-writing-html-and-css/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205895618"
btcnew_comment_counts:
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - HTML
---
When you&#8217;ve worked with front-end development for a while, you start thinking about effectiveness. So without further ado, here&#8217;s my four best ways to be a more effective front-end developer. Feel free to add more ideas as comments!

## 1. Do you need HTML or CSS for this?

Lots of times when I get stranded on hard problem and sit back, I realize that I really **shouldn&#8217;t be trying to use CSS to solve all layout problems**. Assuming a rounded corner box will have to scale in all directions (up to 8 images!), when it really is fixed width and height (1 image), is an indescribable waste of everyone&#8217;s time. Look closely at the design you&#8217;re trying to implement: does it really have to be as flexible and scalable as you think? Shifting to that mindset saves me hours of work per day.

One thing that many developers forget is that not all designers care for exact pixels. If something is really hard to develop, walk over to their table and suggest a change. You&#8217;ll soon start to notice that designers are real people too, and that they have as much flexibility as you do. It&#8217;s just as easy to call them up, so don&#8217;t let shyness waste your time.

## 2. Try to set properties once

When you know you have to do something (see above), try to **do things once**. This is really tricky in both HTML and CSS, languages that have no variables, and generally makes code reuse a pain. But it is possible.

**With CSS**; set widths of elements once, and trust inner elements to fill their parent. That&#8217;s the default behavior of block level elements, and you can set display: block, or width: 100% on most other elements. Don&#8217;t set heights at all if you can avoid them, and let elements expand to fill their containers. Combine similar CSS selectors to avoid typing things twice, and make new ones for common properties when few properties differ. Use floats and clearing instead of absolute positioning, and you&#8217;ll won&#8217;t have to micromanage positions all the time.

**With HTML**, make sure that you really know the template language. I&#8217;ve fighted with ASP.NET, JSP, JSTL, Smarty, WordPress Themes, RHTML, and Django&#8217;s Templating Language, and now know enough about all of them to be productive. You should never have to type the same structure out twice, even in HTML. If your template language have loops, if-clauses and includes you really have no excuse to copy large chunks of HTML around. Refactor your HTML and make your own life easy.

## 3. Learn your text editor

When code reuse isn&#8217;t possible, **use search/replace** in your favorite text editor.

Replacing all instances of one HTML tag name with another is about replacing &#8220;element>&#8221; with &#8220;element2>&#8221; (without the opening bracket). That way you replace both opening and ending tags at once. Check to see if your editor supports regular expressions in its search/replace tool. If it does you can save lots of time by learning it. Matching a HTML tag is &#8220;<[^>]+>&#8221;, a starting angel bracket, one or more non-brackets, followed by an ending angel bracket. Naive regexps can make you match the starting bracket of one tag and the end of another, which makes for a mess.

There&#8217;s lots of little tricks like that, if you learn them you save massive amounts of time.

## 4. Make sure your environment supports you

There&#8217;s more than the text editor that you have to work with. One essential part of front-end development is trial and error. It sounds silly but no matter what your skill is, sometimes you must resort to trying and testing your way to a solution. With HTML and CSS, this means being able to **quickly make a change, switch window, and see that change in the browser**. If that cycle takes more that 5 seconds, you&#8217;re losing valuable time.

Don&#8217;t use a virtual machine (even if it&#8217;s only for IE6) that you can&#8217;t quickly Alt-Tab out of. If you&#8217;re stuck using one, you need to have the text editor on that machine too. It&#8217;s worth your time fixing it.

Don&#8217;t accept build processes that makes you wait more than 5-10 seconds before you see your changes. With trial and error coding you will then waste 50% of your capacity doing nothing. Most often you can bypass this by copying just the HTML and CSS to the right place, without touching other source-code. I&#8217;ve managed to do this in all kinds of crappy environments, and it&#8217;s always worth it.

So.

I hope some of the above can help you save some time each day. The little things add up you know. What&#8217;s your best time-saver?