---
id: 32
title: Simple CSS templates
date: 2006-01-07T16:25:48
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/simple-css-templates/
permalink: /css/simple-css-templates/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205285148"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - Tutorial
---
The most frequent question in the #CSS channel I&#8217;m in is about how you make a 2 column layout. Most beginners seems to have problems understanding how floats work since they are quite different from tables. So I sat down and made some simple layout templates for you. These layouts will all be made with floats since that&#8217;s the easiest way to do things. I could have set out to use absolute positioning but that can get tricky when it comes to placing the footer. Let&#8217;s stay with floats.

I&#8217;ll recap how a floats work. A float is applied by simply setting `float: left` or `float: right` on an element in your CSS-file. The element then gets pushed as far to the left or right as possible and the next element will follow to the right (if floated left) or left (if floated right). The closest HTML comparision is the effect you get when setting align=&#8221;left&#8221; on an image. In the beginning it helped me to think of floats like that.

There are basically two ways to make 2 column layouts with floats. Either you float all the columns (float-float) or you float all but the last one (float-margin). The former method makes it easier to work with clearing inside of the second columns though, so if you&#8217;re going for a complex layout float-float might be better. The latter has the advantage that you don&#8217;t have to set a width on the last column. It will fill whatever space is availiable. My favourite is still float-margin though, the automatically expanding second column makes sure the the full width is used no matter what.

For the examples below I will use the HTML I outlined in my previous article about [CSS basics](/css/beginners-guide-to-css-and-standards/4/).

## The float-margin method

Let&#8217;s start by looking at some examples:

  * [2 columns using float-margin](/files/templates/?style=2columns_float_margin)
  * [3 columns using float-margin](/files/templates/?style=3columns_float_float_margin&cols=3)

Ok, so how does this work? The first example: The navigation is floated left which means that the next element will follow to the right of it. This sounds right but we are forgetting one thing, what happens if the navigation is very short? Then the text in the right column will continue [below the float](/files/templates/float_example.html), probably not what we wanted. So, to fix this we add a margin-left to our content division. Voilà!

The 3 column example is based on the same idea. Here we start by floating the navigation left, floating the first content block right and finally add margins to the second content block. The last block needs to have both a margin-left and a margin-right to stop the text from continuing below the left and right columns. Makes sense? Take a look at the code and I hope it will.

## The float-float method

Another method of doing the same is floating each of the columns left. This means that the columns will show up on the webpage in the same order as you put them in the HTML (that was _not_ the case in the previous example, content1 was to the right and content2 in the middle). Some examples for you:

  * [2 columns using float-float](/files/templates/?style=2columns_float_float)
  * [3 columns using float-float](/files/templates/?style=3columns_float_float_float&cols=3)
  * [4 columns using float-float](/files/templates/?style=4columns_float_float_float_float&cols=4)

There isn&#8217;t much explaination needed here, only thing different from the float-margin method is that you need to set a width on all your columns. You should easily be able to expand this method to kazillion columns :)

That&#8217;s all, be sure to poke around with the different layouts to get a feel of how they work for you. In my next post I will go through some less static layouts, namely elastic and fluid layout. Comments are availiable for questions.

> **Update**: Added an article on [Common questions beginners ask](/css/what-beginners-ask-for-and-what-i-tell-them/)
