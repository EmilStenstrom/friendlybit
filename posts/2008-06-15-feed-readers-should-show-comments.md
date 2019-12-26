---
id: 165
title: Feed readers should show comments
date: 2008-06-15T17:25:48
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=165
permalink: /css/feed-readers-should-show-comments/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205287617"
btcnew_comment_counts:
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
  - 'a:0:{}'
categories:
  - CSS
---
One thing I&#8217;ve noticed lately is that I read fewer comments. It isn&#8217;t that strange really: I read blogs using a feed reader and it doesn&#8217;t show a links to comments. I see a couple of reasons why comments are not cared for in feed readers:

## Why not #1: Feeds are meant to be fast

Many subscribe to feeds to be able to get news before everyone else. And getting things fast means getting it before anyone else have commented. Why add a lot of zeros below each feed item?

But, it isn&#8217;t unusual that **I read posts that are a couple of days old**. I don&#8217;t read my feeds every day, rather every second or third day. In those days there are most likely comments on good posts, and of course I don&#8217;t want to miss them. The older a post is, the more likely that it will have interesting comments.

## Why not #2: Comments are hard to detect

Perhaps feed readers have a hard time detecting if there are comments to a post or not. Comments are not included in the post, so wouldn&#8217;t they have to parse through the feed link for comments?

No, there is a tag called `<wfw:commentRss>`, that&#8217;s possible to use in both Atom and RSS (If I&#8217;m not mistaken), that gives **a link to the comment feed**. That means feed readers could easily get the comments too. The best thing here is that all WordPress blogs (and others too) have it already. It&#8217;s just a matter of using it!

## Why not #3: Each post will be too long!

If there are 50 comments to a post, the item in the feed reader will be too long to read. That would also affect download time and therefore make things slow.

Yes, it will mean downloading more data, but you also get more information. **Each feed reader is free to implement comments any way they like**, and I doubt it will be to expand the original post with all 50 comments. I little link that expands comments (don&#8217;t download any extra data until you expand)? Only show the first five, and a link to the page for more? There&#8217;s lots of good options here.

## Promote contributions more

Adding comments to your feed serves to promote your user&#8217;s contributions even more, and I&#8217;m really surprised that not everyone does it. I&#8217;m using feed burner for [my feed](/feed/) and can therefore use a feed flair (Click your feed / Optimize / FeedFlair / Comment count) to add a link to my comments at the end of the post. That&#8217;s a first step.

What would be much better was if **feed readers would get better at promoting comments**. Could we get them to somehow?
