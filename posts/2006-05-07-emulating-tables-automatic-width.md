---
id: 62
title: 'Emulating tables: Automatic width'
date: 2006-05-07T01:59:50
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/emulating-tables-automatic-width/
permalink: /css/emulating-tables-automatic-width/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "206460524"
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
Moving from tables to layouts based on CSS is a tough move for many. Things don't behave the way they use to and some effects are much harder to do with CSS. This article is about one of the tricks you might want when trying to get table-like effects using CSS: the dynamic width column, where you let the width be decided by an image. You may jump ahead and look at the [dynamic width column](/files/dynamic_left_column/) right away if you want.

## The problem

What we are after is a way to emulate a simple effect when using tables. Look at this code:

```html {.incorrect}
<table>
    <tr>
        <td><img src="/files/post-media/huvet_southpark.png"></td>
        <td>Some sample text here</td>
    </tr>
</table>
```

The code above will render two columns, and the width of the left one will be equal to the width of the image. This can be useful on a very dynamic site, where you don't know the width of the image and so you don't want to set it using CSS.

Looking at the code above you might see the problem though. Tables are for tabular data, and and image and some text are certainly not tabular. We need something better.

## The solution

When you start to look at the problem you quickly realize that the image needs to be floated. There is just a few ways to put things side by side in CSS and floating is one of the few ways that works like we want it to. The image moves to the left and text flows around it. This looks all nice but if you add a border the other column you see that they are not really side by side. All that has happened is that the _text_ has been moved to the left, not the container.

This can be solved by setting `overflow: auto;` on the right column. After setting this the container nicely contracts and sits where it should. IE6 doesn't play by the same rules though. Here you instead need to set `height: 1%;` to make it behave.

This final CSS looks like this:

```css
img#cartoon {
   float: left;
}
#example div {
   overflow: auto;
   height: auto !important;
   height: 1%;
}
```

**Update:** After Rowan Lewis suggestion I now use `height: auto !important;` to send a correct height to modern browsers. IE6 does not understand `!important` and will therefore overwrite the height with the 1% value.

And the following HTML:

```html
<div id="example">
    <img src="/files/post-media/huvet_southpark.png" id="cartoon">
    <div>
      Here's all the text
      Even more text here!
      Even more text here!
      Even more text here!
    </div>
</div>
```

Have a look at the example of the [table-like behaviour](/files/dynamic_left_column/).
