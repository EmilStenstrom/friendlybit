---
id: 110
title: Style tables with CSS
date: 2008-03-14T01:10:28
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/style-tables-with-css/
permalink: /css/style-tables-with-css/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205286760"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
I don&#8217;t deal too much with tables. Not because I don&#8217;t want to but because clients hardly ever want to use them. My guess is that they are too hard to create with todays WYSIWYG editors, and therefore get left out. It happens though that I have one or two static tables I need to style, and then I get to use a couple of my tricks.

**All of the examples below work across browsers. Including IE6.**

  * [Add a gradient to your cells](#gradient)
  * [Remove the space between the cells with CSS](#spacing)
  * [Obey the set width](#width)
  * [Styling columns](#columns)

## Add a gradient to your cells {#gradient}

One easy way to make tables look better is to add a [subtle gradient](http://9rules.com/blog/2006/08/a-gradient-tutorial/) to the cells. That&#8217;s easy to do. But make sure you also set a background color with one of the edge colors from the gradient, and use the top or bottom keyword. You never know the height of your cells when people zoom the text.

```css
td {
   background: #2B2B3C url(item_gradient.gif) repeat-x bottom;
}
```

## Remove the space between the cells with CSS {#spacing}

When designing tables you rarely want the ugly double border between two cells that appear when you set a border on td. Neither do you want the space in between them&#8230; Many believe the only way to remove that space is to use the cellspacing and cellpadding attributes in HTML. You don&#8217;t:

```css
table {
   border-collapse: collapse;
}
td {
   border: 1px solid silver;
}
```

See? No ugly HTML attributes needed.

## Obey the set width {#width}

Many of you have probably seen tables that do not stay within the width you have set on them. It can be long words or sometimes URLs that are wider than what can fit. By default, the browser puts content before style, and therefore expands the table to show the content. But what many don&#8217;t know is that you can change them to always obey the set width:

```css
table {
   table-layout: fixed;
   width: 100px;
}
```

Easy, and now the table will be 100px, no matter what.

## Styling columns {#columns}

Sometimes you want to style some columns differently than all other cells, and I&#8217;ve seen that most people add a special class to each of the cells in that column. Wouldn&#8217;t it be nice if there was a way to just specify the class once? There is!

```html
<table>
<col class="first">
<col class="second">
<tr>
<th>Header 1</th>
<th>Header 2</th>
</tr>
<tr>
<td>Cell 1</td>
<td>Cell 2</td>
</tr>
</table>
```

```css
col.second {
   width: 100px:
}
```

Convenient isn&#8217;t it? There&#8217;s one thing you should know though&#8230; The col attribute only allows [four attributes](http://www.w3.org/TR/CSS21/tables.html#columns): Border, Background, Width, and Visibility. What the heck? Well, there is performance issues with implementing more complex things so W3C decided not to include it. So what if you need to set, say, text-align on a column? You can be clever:

```css
col.second {
   text-align: right;
}
td:first-child + td {
   text-align: right;
}
```

The above works because IE allows setting more properties on columns than the spec allows ([Hixie explains it well](http://ln.hixie.ch/?start=1070385285&count=1)). Firefox on the other hand, ignores the set text-align, but instead allows you to use a sibling selector to select the &#8220;second td after the first one&#8221; (you can add another &#8220;+ td&#8221; to select the third one, and so on&#8230;). Voilá! Cross browser column specification.

That&#8217;s all for now, did you know all of them?
