---
id: 45
title: What beginners ask for (and what I tell them)
date: 2006-03-27T22:22:07
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/what-beginners-ask-for-and-what-i-tell-them/
permalink: /css/what-beginners-ask-for-and-what-i-tell-them/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "205285706"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
  - HTML
  - Tutorial
---
Being in an IRC help channel lets you meet a lot of people. Many are fresh beginners that just wrote their first lines of CSS and stumbled over something they found strange. When you look at their questions from a perspective you quickly find that many of them are repeated and come back over and over again. This article is an attempt to list a few of the important concepts that people seem to have trouble with.

## Separation of content and design {#separation}

Separation is the fundamental idea that CSS builds upon. Ten years ago there was only one way to make pages that worked across browsers: you mixed everything in one large file and copied that file if you wanted pages that looked similar. Then [Håkon](/css/interview-why-did-css-succeed/ "Interview with Håkon Wium Lie") and Bert came up with CSS and things got much easier. Their idea is to make the code easier to maintain by extracting everything that has to do with design, put it in an external file and link to that file when we want a certain look. CSS is all about design and HTML is all about content and structure.

Even though this sounds good in theory there are a lot of cases where it&#8217;s hard to determine whether something is design or not. Is the company logo design or content? When you start thinking about those kinds of problems you know you&#8217;re on the right track. You can find a couple of examples of the separation I&#8217;m talking about on the second page of my [beginners guide](/css/beginners-guide-to-css-and-standards/2/).

## Clearing floats {#clearing}

Floats and clearing is another problem almost everyone has in the beginning. What I like to use when I explain how floats work is the old align-attribute on images. Long time ago, when you only could use HTML for design, and wanted the text to &#8220;flow around the image&#8221; you used:

```html {.incorrect}
<img src="/files/post-media/image.jpg" align="right">
```

The above code is clearly design (placement of the image) so we should use CSS instead of HTML for this.

```css {.correct}
img#id_of_image { float: right; }
```

CSS is not restricted to float only images, all elements can be floated. This opens up to both new layout methods and confusion. To place three divisions side by side, just give them a width and float them. You can see a layout based on this in my [article about layouts](/css/simple-css-templates/) or the [3-column example](/files/templates/?style=3columns_float_float_float&cols=3).

_Clear_ is also important to know of. Setting `clear: both;` on an element makes it move downwards until it&#8217;s below all previous floats. That was how the footer in the above example was made.

Floats and clears are not always easy to understand though. One thing people often ask about is what&#8217;s wrong when their container isn&#8217;t expanded to contain everything inside it. Eric Meyer excellently explains both that problem and its solution in the article [Containing Floats](http://www.complexspiral.com/publications/containing-floats/).

## Validation is a timesaver {#validation}

Why is validation so important? Because I just can&#8217;t stand you forgetting your alt attributes? Because I think that valid pages are better than non-valid? No and No. It&#8217;s because validation finds the simple errors. If I misspell width or some other property a validation will find it. If I nest my tags incorrectly a validation will find it. If I forget to close a quote in a link? A validation will find it. Validation is a great timesaver because it actually finds all the small errors that humans have trouble finding. To make validation even easier I use the [Html Validator extension](http://users.skynet.be/mgueury/mozilla/) for Firefox. A little icon in the bottom right corner tells me when I have an HTML error. Validation is a great tool, use it.

## Accessibility is not about blind users {#accessibility}

It could be that I&#8217;m trying to explain why someone should add labels to their form. I say something in the lines of:

> **Me**: "Not having labels hurts your site’s accessibility"

> **User**: "But I don&#8217;t have any blind users on my site!"

Accessibility is about making it easy for as many as possible to access your content. With, often simple, means you can make it much easier for people to access your site. Let me give you some examples or people your can help by thinking about accessibiliy.

| User                                                                                                                            | How you can help                                 |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| Partly color blind                                                                                                             | Don&#8217;t use only color to convey information |
| People unable to use a mouse. Either because of some physical disability or simply that they are linux hackers and dislike it. | Make sure keyboard navigation works as intended  |
| Young users or users with another native language than yours                                                                   | Don&#8217;t overcomplicate your text             |
| People with a slow connection                                                                                                  | Mind the size of your site                       |

The list could continue for a whole article. People from those groups would very much like to see your site and buy your stuff just like anyone else. Read up on the basics of accessiblity, it helps a lot of people. Robert Johansson has written a nice article about how you could [evaluate your website&#8217;s accessibility](http://www.456bereastreet.com/archive/200603/evaluating_website_accessibility_part_1_background_and_preparation/).

## Some things are harder to do with CSS, that does not mean CSS is a bad language {#harder}

People that are switching from tables to CSS often complain about what a bad language CSS is for not supporting _[insert favourite feature]_. I did so too in the beginning. What makes me like the language is all the other powers it gives me. It is not possible to do everything as easily with CSS as it is with tables. But other things are much easier, and some things aren&#8217;t even possible with tables. There are good parts and bad parts and to me the good parts greatly outweigh the bad ones.

## Equal height columns {#equal}

The last thing I&#8217;m going to talk about in this article is equal height columns. The problem is that your have two or three columns of content that stretch down the page. You want the columns to stretch as far as the longest column but the content inside does not expand the columns that far.

This problem is most easily solved by a technique known as _faux columns_. Add a container to the columns you have and then add a background image to that container. The image will repeat down that page and make it look like your columns take up exactly as much vertical space. I&#8217;ve added a [faux column example](/files/templates/?style=faux_columns&cols=3&nofooter=1) for you to look at.
