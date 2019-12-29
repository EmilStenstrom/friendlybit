---
id: 147
title: Documenting CSS
date: 2008-02-27T23:55:00
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/documenting-css/
permalink: /css/documenting-css/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205973222"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
  - 'a:0:{}'
categories:
  - CSS
---
Just like all other programming the **CSS needs documentation**. I'm afraid I'm rather bad at it: the times I'm lucky I've been able to document by simply talking to the developer taking over, and the unlucky times I've left no documentation at all. Talking directly is of course superior to everything else, you don't waste time explaining things that are obvious (differs from person to person), but you don't always have that luxury. So what I thought I'd do is list things I think are important to document, for the times when you won't be available for answering questions.

Don't be fooled to think all projects are alike. Sometimes you're under tremendous stress just to get the basic CSS up and running; it isn't reasonable to expect the same kind of documentation then… But most often you have an hour extra to just jot down a couple of lines about your interface.

  * **How is the CSS file(s) structured?** When you build large sites you often end up with over 1000 lines of CSS, and if you don't structure them, you'll end up with a mess. Even if you DO have a structure, it takes a lot of time to figure out someone else's code. To give you some ideas of your own, I wrote about how I [structure my CSS](/css/how-to-structure-large-css-files/) previously. You don't have to use that one, just be conscious about your choice, and document it.
  * **Where do I add new styles?** Either it's obvious from the previous structure or you need to make it obvious how to add new stuff. What if I'm adding a deviation from how a certain section looks, should I put it near that section's styles, or near all other deviations? This question is especially important on sites with lots of campaign components with custom CSS. Trust me, your cleverly crafted structure will become a mess if you miss answering this question.
  * **What can I do with existing styles?** To make sure design ends up in the CSS and not in the HTML there needs to be some kind of overview of all available classes. Else people are going to hack things and try to duplicate your code. How do you handle columns, clearing, quotes, and floated images? Did you think of it yourself or do I have to add my own code? A good way might be to make a document where you tie the different classes to how they look when used.
  * **How are different browsers handled?** Struggling through browser hacks is a real pain in the ass, unless those hacks are properly documented. What browsers do you try to support, and which of them have you tested in? Did you plan for the future?
  * (Optional) **Web standard basics**. Working with web standards is rather different than working the old (table based) way . So if you know that oldschool developers will work with your code (are you sure they won't?), it could be a good idea to shortly summarize the modern web mindset. I recommend using a lot of links here, not to waste time; people are very different in what they know.

If you've answered the questions able you've come a long way. Your code is understandable, and will stay in shape for much longer. Not to mention when you're looking at some code in a year, thinking: "Who wrote this shit?! It's a mess!", and then figure out it was you.

Now, is there anything essential I'm missing, that you want to add?
