---
id: 59
title: Datatypes of HTML; why HTML is great for structure
date: 2006-05-01T15:42:26
author: Emil Stenström
layout: post
guid: http://friendlybit.com/html/datatypes-of-html/
permalink: /html/datatypes-of-html/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "205285823"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - HTML
---
<p class="first">
  HTML is often bashed by people for being a bad language. People, often used to XML, talk about the lack of good elements for marking up things like authors and dates. While I agree that HTML would need a few more tags that help with marking the meaning of things I do think HTML is good at structure. This article is a attempt to show HTML's power by mapping how different datatypes in the common programming languages map to elements in HTML.
</p>

  * [Arrays, Lists, Vectors](#lists)
  * [2D-Arrays, Datasets](#tables)
  * [Trees](#trees)
  * [Hashtables, Dictionaries](#deflists)

## Arrays, Lists, Vectors {#lists}

All programming languages have some way of storing a list of elements. While they are called different names in different languages and support different ways of adding elements they are very similar. HTML supports two kinds of single element lists, the _ordered and the unordered list_. When selecting which one of them you should use you just have to ask yourself: "Does this list make sense in another order?”. If it does it's an unordered list, if not it's an ordered one.

```html
Unordered list:
<ul>
    <li>Blue item</li>
    <li>Gray item</li>
    <li>Pink item</li>
    ...
</ul>
Ordered list:
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    ...
</ol>
```

## 2D-Arrays, Datasets {#tables}

Most languages also support some way of arranging your data in a two dimensional grid. The ordinary way is just letting people nest lists inside each other and get several dimensions like that. HTML has recognized the need for a simple way of marking up two-dimensional data in an easy way and therefore added the _table element_. Since two dimensions make the data a bit more complex to understand the HTML authors decided to add a few elements that describe what columns and rows mean. Below is a table with the essential elements for metadata added.

```html
<table summary="Prices for apples in Sweden">
    <caption>Table 1: Prices for various apples in Swedish stores</caption>
    <thead>
        <tr>
            <th>Kind of apple</th>
            <th>Color</th>
            <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Granny Smith</td>
            <td>Light Green</td>
            <td>3 SEK</td>
        </tr>
        <tr>
            <td>Golden Delicious</td>
            <td>Yellow</td>
            <td>6 SEK</td>
        </tr>
        <tr>
            <td>McIntosh</td>
            <td>Golden</td>
            <td>30 SEK</td>
        </tr>
    </tbody>
</table>
```

## Trees {#trees}

Sometimes you want to have a tree of data; it might be to display a nice view of your historical ancestors or simply the probabilities of something happening. Many programming languages have decided not to include a certain type for this and instead let programmers build their own type with the help of nodes and pointers. HTML instead relies on nested lists for this purpose. The example below shows a nested navigation menu in two levels:

```html
<ul>
    <li>Home</li>
    <li>About this site</li>
    <li>Sections
        <ul>
            <li>Blue Fishes
                <ul>
                    <li>Light blue Fishes</li>
                    <li>Dark blue Fishes</li>
                </ul>
            </li>
            <li>Black Fishes</li>
            <li>Red Fishes</li>
        </ul>
    </li>
    <li>Contact us</li>
</ul>
```

Worth a note is that lists only can contain list items, not other lists. This means that all sublist needs to be wrapped inside a list item like I have done above (the fishes are inside of Sections list item).

## Hashtables, Dictionaries {#deflists}

Moving on we find the more advanced types of data. Quite often in programming we want to map a string to another string. This can be the case if we are building a dictionary or even if we want to store the price of different products. To me both of the above examples are cases where I would use a HTML _definition list_. Definition lists also has a way to mark that certain items might map to several other. By setting two dts after each other you make them both apply to the following dd.

I've made an example below of how to markup a list of properties.

```html
<dl>
    <dt>Weight:</dt>
    <dd>45 kg</dd>

    <dt>Length:</dt>
    <dd>12 m</dd>

    <dt>Colors:</dt>
    <dd>Blue</dd>

    <dd>Red</dd>
    <dd>White</dd>

    <dt>Cost:</dt>
    <dd>500 SEK</dd>
</dl>
```

Definition lists where originally made to just store definitions (as the name suggests) but it's my opinion that they can be used for more than that. HTML lacks a lot of semantics and this is a way to extend it a bit. Feel free to leave a comment if you disagree.

&nbsp;

It's my opinion that HTML is good at marking up structure. Sure there are some types of data that can't be represented with HTML but the most common types are easy to do. Do you have more types to add to the list? Leave a comment!
