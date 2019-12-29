---
author: Emil Stenström
categories:
- HTML
- Tutorial
date: 2006-08-01 19:17:40
guid: http://friendlybit.com/html/make-your-site-easier-to-use/
id: 85
permalink: /html/make-your-site-easier-to-use/
title: Tricks to make your site easier to use
---

There are lots of little tricks you can use to make your sites easy to use. Problem is that they are so obvious, you don’t think of them. This article is an attempt to share some of the ideas that I _did_ think of. I'm sure I missed some; feel free to add your own tricks in the comments.

You rarely think of sites as "easy to use"; they just work. You enter them, click here and there, and don't think much about how the navigation works or what to do. That's the feeling we should go for.

## Separate the interaction layer

A very simple way of making it easier for your users is clearly marking what can be interacted with. Are users expected to click on those small arrows of yours? Are the only links to your content through your headers? Then you better make sure those arrows or headers come across as clickable.

The fastest way to convey that something is clickable is using blue underlined text. Why? Because that's what most sites use (see [Google](http://www.google.com), [Amazon](http://www.amazon.com), [eBay](http://www.ebay.com)). It's what we have grown up with and it just works. Designers tend to dislike blue underlined links and have started to use other colors and skip the underlines. Jakob Nielsen, the notorious usability expert, writes about what you should think of in his [article about the visual style of links](http://www.useit.com/alertbox/20040510.html). It's a good reminder.

You don't have to stop with just the links though. Are your images clickable? Then make sure they connect with your links somehow. If you pick orange as your link color, make something around or in the images use that color too. Make your form fields use the same color. When someone enters your site it should be possible to quickly get an idea of what to do: "I can either click a link in the menu, search for a phrase, or click this thumbnail". Don't make people confused by mixing in orange on the static parts of your site.

With some cleverness I'm sure this idea can be expanded to work even without being dependent on color. A small figure? A border? Use your imagination, and be sure to tell me about it.

## Split up your content

You know those portal sites? There's one big reason they don't work. There's too much content cramped into a too small area. A portal is rarely about something specific, it's about everything that they can possibly fit in. Whatever content you are looking for you will have to search hard for it. Do you use the portal parts of Yahoo or MSN? Didn't think so.

There has been a long discussion recently about how badly designed pages work better. [Like Andy Rutledge](http://www.andyrutledge.com/bad-design.php "Bad design harms business, it does not help it") I mostly disagree but I can understand how bad design works for ad-driven sites. Is the point of your pages to make people click ads? Then make them confused, make them think your navigation is the ads, I'm sure it drives your revenue up. If the point of your site is the content on it, stay away from being a portal.

The simplest way of avoiding the portal-look is splitting up your content. Do you have info on both crocodiles and stock numbers? Don't put them on the same page. Make sure only the people interested in stocks get the stock info. Anyone else will just see them as "something I am not looking for". If you have lots of info from diverse fields, perhaps a <a href="http://dmoz.org/" rel="nofollow">directory</a> is a better bet?

## Use `<label>` for form elements

Bad form elements are one of the most annoying things on the web. Worst are those tiny little checkboxes you need to check to specify if you like to get spammed or not. They are simply too small. There is an easy solution though, that everyone should be aware of: the label element. What it does is associate some text with the checkbox. The browsers use this information by making a click on the text check the box. Note: this also works for radio buttons. Here's the markup you need:

```html
<form action="">
<input checked="checked" id="send_spam" type="checkbox"><br>
<label for="send_spam">Send me all your "newsletters"</label><br>
</form>
```

```css
label { cursor: pointer; }
```

There's a lot more to learn about how to make your forms usable and accessible. Just head over to the Web standards project's [Accessible forms tutorial](http://www.webstandards.org/learn/tutorials/accessible-forms/beginner/) (don't miss the intermediate one either).

## Make it interesting

You have a few seconds to get you visitor hooked to your site. In that time the user needs to understand he's on the right track. "Ah, this site seems to be about web development" is what I want my users to feel when they enter Friendly Bit. Therefore almost all my pages have a little info box that tells the visitors just that. To just put this info on your front page isn't enough, search engines or other external links can make them enter deeper into your site. Please put this little info-box somewhere on all of your sites. It's one of the best ways for me to see I'm where I want to be.

To actually get your content interesting you need to work on your writing. My best tip is to follow the points Liz Strauss summed up nicely in her post about [what a reader wants](http://www.successful-blog.com/1/9-1-things-every-reader-wants-from-a-writer/).

Read through your text over and over again, out loud if you need to. Pay attention to typography, don't make your paragraphs too long and use headers extensively.

## Conclusion

These are just some of the tricks I find myself using on my sites. I'm sure this site does not follow all of them perfectly but that doesn't stop me from telling you about them, does it? Pick and choose as you like, but try to reach make you visitors feel that "it just works"-feeling.

Do you have any tricks you can share?
