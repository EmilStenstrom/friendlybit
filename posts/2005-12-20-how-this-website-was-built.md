---
id: 29
title: How this website was built
date: 2005-12-20T00:00:36
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/how-this-website-was-built/
permalink: /css/how-this-website-was-built/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205285096"
categories:
  - CSS
---
Hi there early readers! Welcome to a newly started web development blog. I know that there are a lot of those around so I will work hard to make it different and hopefully earn your trust. This site will mainly consist of new stuff; very few of those “news about news” posts, there are better places for that. “Web development” I say, and by that I most often will mean client side techniques like HTML, CSS and Javascript. This is the idea and I hope it will work out.

This site has been worked on for over a year so it's about time I get it up and working. This article will talk mostly about how this site has been built. You will hopefully notice that to me it's important that you practice what you preach.

## WordPress as backbone

I'm running the blog software WordPress 2.0 as the base for all this. I've read a lot of good things about it and I know PHP so I thought why not give it a try? In just a week I had written my own theme and a few plug-ins to go with it. WordPress really is well built and easy to use. Any problems I've had have been answered in the IRC help-channel by nice people. Kudos to the WordPress team for doing a great job.

## Fireworks for building the idea

All my layouts start out in Macromedia Fireworks. Fireworks is a nice program to work in even though I'm not used to their other programs. I have tried Photoshop but it just didn't work out between us. Floating toolboxes? Startup time that makes me fall to sleep? No, I wanted something that’s easy to get started with, and if possible something that had special tools for web development. Fireworks is perfect for this, it’s like a combination of Illustrator and Photoshop and has a user interface that even a beginner learns quickly.

I played with a few different layouts until I found something I liked. The idea with this one is to put the content in focus. Everything except the content column is dark so the white will stick out. The text starts a bit above the text in the left column and has a big `<h1>` so you know where to start. The comments are placed in the sidebar, mostly because there probably will be very few in the beginning. Don't take that as an insult, I want to hear what you say, but this is not a forum or wiki :)

## CSS elastic faux columns for implementing it

This site does not use tables for layout (of course!). I'm an operator of a help channel for CSS so that would be unacceptable :) A lot of work has gone to make sure the layout works like it should.

The layout in Fireworks was complete and I had the hard part left, converting my mock-up to a web site. After many tries I finally decided to go with a zoomable layout. I know this is hard to work with, especially with complex sites like this one but I thought I’d give it a try. Worked out pretty well I think. The biggest bug I know of is that the header look strange in Opera and Safari, as far as I can understand it's because of a bug in both their rendering engines when calculating percentages. Anyhow, the site works well in both Internet Explorer 6 and Firefox so I hope most of you will see it like it's meant to.

The layout is made zoomable by using the em unit on the parent container. When text-zooming (Ctrl + Plus in Firefox and View -> Text Size in <acronym title="Internet Explorer">IE</acronym>) the em unit adjusts to what you select so everything gets nice. There is one big problem with changing text-size though: images do not change size when you text-zoom. So certain parts of the site need to stay fixed and some need to move for the site not to collapse.

I wanted background-images in all my three columns so having all columns change their sizes started to look hard. Then I stumbled over an article about faux columns that used percentages to position a background-image so that it could grow in both directions. The faux columns technique uses a repeating background-image to fake columns. By using two of those images I could get it working on a 3 column layout with percentages.

The next step was making the site zoomable. If I set the container to a fixed em width and then use faux columns with percentages throughout the site I get what I want. Everything worked out and I could start working in the small parts. Want to see how much trouble IE gave me? Just have a look in my "decoration" stylesheet, I commented every browser problem I encountered in IE, Opera and FF and solved most of them :)

## Miscellaneous

All images used are from [SXC.hu](http://www.sxc.hu), the excellent stock image directory. Highly recommended.

That's it people, my site and the idea behind it. I hope you will come back and read my articles. Thanks for reading.
