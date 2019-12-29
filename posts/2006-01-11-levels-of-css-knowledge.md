---
id: 33
title: Levels of CSS knowledge
date: 2006-01-11T01:25:29
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/levels-of-css-knowledge/
permalink: /css/levels-of-css-knowledge/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205285221"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
As you might have understood by now I'm very much pro web standards. The current widely accepted standards are: (X)HTML for page structure, CSS for design, and Javascript for behaviour. HTML is pretty well known by now, it has been there since the beginning of the web and there are tutorials everywhere that gets you started. CSS is starting to get a grip, large companies are switching their sites to CSS based layouts and the webdev blogosphere reaches more and more people.

When you promote web standards, like many of us do, you get to talk to a lot of people. If you promote it in a live chat room like #CSS on EFNet it gets even clearer: there are a lot of different levels of CSS knowledge out there. This article is going to list some of those levels along a rating of how this kind of developer will affect the web. Here we go:

## Level 0

> "CSS? Isn’t that a multiplayer game?"

These people have probably never made a webpage in their life. If they did it was pure HTML and they barely knew what they were doing. We get some of these people in #CSS, not because they want to start learning but because they think they've come to another channel, often looking for <acronym title="Counter-Strike: Source">CS:S</acronym>. No need to worry about these people, they probably won't do many webpages in their lives so they can't do much harm.

## Level 1

> "Yeah, I use it to remove underlines on links sometimes"

Different from Level 0, the people in this level do actually know basic HTML. They probably learned it at least five years ago and have made a couple of simple sites. They use very little CSS, only when they need to do simple stuff you can't do with HTML only, like removing underlines and setting line-height (No! don't even think about setting line-height with HTML). While these people could present us with some badly coded sites they rarely have any large and well visited ones. This means that they won't do much harm either.

## Level 2

> "No, I don't like divs; tables are much easier to work with"

Instead of just playing with HTML, like those from Level 1, some continued their quest. They mastered HTML tables and started using it to make things look just like they wanted. Somewhere around reaching HTML mastery they stopped looking at new ways of working. They heard about other people using "divs to design their pages" and even took some time one day to try to learn what the fuss was about. After a few hours of not getting it they gave up, went back to the familiar land of tabled layouts, and stayed there. Many do know CSS syntax and sometimes even some background but they believe it's far too hard and ill-supported to use instead of tables.

Watch it! These are dangerous people, some even webmasters of big corporate websites. Since they have been in the business for a while many are leaders for their web departments. These are the people it's most important to reach, and if we do it means a lot for the web. Concentrate on these people all you standards advocates.

## Level 3

> "Yes I've heard it's good, but I can't use it because of…"

While people in this group still don't use CSS for positioning they do know some CSS and perhaps heard good things about it. They've tried making simple layouts and some even liked how it felt to work with. Problem here is that something is stopping them. Perhaps they have a Level 2 boss, perhaps their website needs to cater for Netscape 4 users, there might be many different reasons but something is in the way.

These people need to know that while CSS _does not_ work everywhere that isn't the end of the world. Old browsers will still get all your content, just pure content. Instead of them you will reach a new audience: there may be accessibility and usability benefits, newer browsers will get a _richer_ experience and the site might even get easier to add content to (which will lead to more content). Tell this to the people in this group. If you're unlucky they are not be the ones making decisions but in that case their influence on Level 2 Bosses will still be worth it.

## Level 4

> "CSS? Oh! Yes, I use divs for all my layouts"

It's not unusual that these people use only divs on their sites. Each part of their page gets a div, often with a carefully crafted id (#toprightredline or even #r5_c7 with r standing for row and c for column), and then they position their divs with absolute positioning by the pixel. The result looks good, hey, it even validates as XHTML 1.1(!) but what they have missed is that most of the benefits of CSS has been lost. These pages are terrible when it comes to a screen reader interpreting it. Same with older non-CSS browsers, they won't get the content… they will get one big block of text. When using bad class names and ids you loose the possibility to change the layout: if that red line needs to be changed to black you'll need to change all your HTML documents too (can be hundreds). Don't fall into the trap of telling them they are stupid or make them google "css", they know they are smart people and they did learn about CSS from google in the first place. Tell them exactly what could be improved on their sites. Tell them what the benefits are. Keep your cool and tell them _why_.

People of Level 4 produce sites that are rather bad. The damage is reduced though by them often being open to new ideas. After all, not to long ago they did manage to learn and start to use CSS.

Some of the reasons for people thinking this way is because of what <acronym title="What You See Is What You Get">WYSIWYG</acronym> editors are doing. Most such editors produce terrible div-only code but I'm hearing that there are gradual improvements in this field. This is a good thing and hopefully this will help people move from Level 4 to the higher levels.

## Level 5

> "I use CSS for design, it's better than tables because of…"

After a lot of reading, talking to people and thinking most people arrive at Level 5. This is where you both _can use_ CSS and _know why_ it's better. Some people in this level have minor problems on the sites they produce but it's nothing serious. When asked they can argue why separating structure and design is a good thing and they have worked with CSS long enough to know the common pitfalls. I'm guessing many of the readers of this article are on this level and I feel I am. But this is not the best we can do…

## Level 6

> "What version of CSS? Yes, I do. Did you read my book about…"

For some people knowing how and why isn't enough. These people strive to improve how CSS is used and are publishing great articles on new ways of using it. They constantly go back to the basic needs CSS is filling and attack problems from new angles, often resulting in more great articles. Some have actually read the whole W3C specification on CSS (sic) and they certainly know which parts are supported by which browsers. They function as role models for beginners and do great things for the web with their influence. Many work with the [Web Standards Project](http://webstandards.org). If you ever find an error on their site there is a reason for it. Ask them and they'll tell you why.

&nbsp;

<p class="first">
  That's it. I hope this article gave you some inspiration to keep pushing the web to new victories. At which level are you? Do you have examples of people in last level?
</p>
