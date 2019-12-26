---
id: 85
title: Tricks to make your site easier to use
date: 2006-08-01T19:17:40
author: Emil Stenström
layout: post
guid: http://friendlybit.com/html/make-your-site-easier-to-use/
permalink: /html/make-your-site-easier-to-use/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205286190"
categories:
  - HTML
  - Tutorial
---
There are lots of little tricks you can use to make your sites easy to use. Problem is that they are so obvious, you don’t think of them. This article is an attempt to share some of the ideas that I _did_ think of. I&#8217;m sure I missed some; feel free to add your own tricks in the comments.

You rarely think of sites as &#8220;easy to use&#8221;; they just work. You enter them, click here and there, and don&#8217;t think much about how the navigation works or what to do. That&#8217;s the feeling we should go for.

## Separate the interaction layer

A very simple way of making it easier for your users is clearly marking what can be interacted with. Are users expected to click on those small arrows of yours? Are the only links to your content through your headers? Then you better make sure those arrows or headers come across as clickable.

The fastest way to convey that something is clickable is using blue underlined text. Why? Because that&#8217;s what most sites use (see [Google](http://www.google.com), [Amazon](http://www.amazon.com), [eBay](http://www.ebay.com)). It&#8217;s what we have grown up with and it just works. Designers tend to dislike blue underlined links and have started to use other colors and skip the underlines. Jakob Nielsen, the notorious usability expert, writes about what you should think of in his [article about the visual style of links](http://www.useit.com/alertbox/20040510.html). It&#8217;s a good reminder.

You don&#8217;t have to stop with just the links though. Are your images clickable? Then make sure they connect with your links somehow. If you pick orange as your link color, make something around or in the images use that color too. Make your form fields use the same color. When someone enters your site it should be possible to quickly get an idea of what to do: &#8220;I can either click a link in the menu, search for a phrase, or click this thumbnail&#8221;. Don&#8217;t make people confused by mixing in orange on the static parts of your site.

With some cleverness I&#8217;m sure this idea can be expanded to work even without being dependent on color. A small figure? A border? Use your imagination, and be sure to tell me about it.

## Split up your content

You know those portal sites? There&#8217;s one big reason they don&#8217;t work. There&#8217;s too much content cramped into a too small area. A portal is rarely about something specific, it&#8217;s about everything that they can possibly fit in. Whatever content you are looking for you will have to search hard for it. Do you use the portal parts of Yahoo or MSN? Didn&#8217;t think so.

There has been a long discussion recently about how badly designed pages work better. [Like Andy Rutledge](http://www.andyrutledge.com/bad-design.php "Bad design harms business, it does not help it") I mostly disagree but I can understand how bad design works for ad-driven sites. Is the point of your pages to make people click ads? Then make them confused, make them think your navigation is the ads, I&#8217;m sure it drives your revenue up. If the point of your site is the content on it, stay away from being a portal.

The simplest way of avoiding the portal-look is splitting up your content. Do you have info on both crocodiles and stock numbers? Don&#8217;t put them on the same page. Make sure only the people interested in stocks get the stock info. Anyone else will just see them as &#8220;something I am not looking for&#8221;. If you have lots of info from diverse fields, perhaps a <a href="http://dmoz.org/" rel="nofollow">directory</a> is a better bet?

## Use `<label>` for form elements

Bad form elements are one of the most annoying things on the web. Worst are those tiny little checkboxes you need to check to specify if you like to get spammed or not. They are simply too small. There is an easy solution though, that everyone should be aware of: the label element. What it does is associate some text with the checkbox. The browsers use this information by making a click on the text check the box. Note: this also works for radio buttons. Here&#8217;s the markup you need:

```html
<form action="">
<input checked="checked" id="send_spam" type="checkbox"><br>
<label for="send_spam">Send me all your "newsletters"</label><br>
</form>
```

```css
label { cursor: pointer; }
```

There&#8217;s a lot more to learn about how to make your forms usable and accessible. Just head over to the Web standards project&#8217;s [Accessible forms tutorial](http://www.webstandards.org/learn/tutorials/accessible-forms/beginner/) (don&#8217;t miss the intermediate one either).

## Make it interesting

You have a few seconds to get you visitor hooked to your site. In that time the user needs to understand he&#8217;s on the right track. &#8220;Ah, this site seems to be about web development&#8221; is what I want my users to feel when they enter Friendly Bit. Therefore almost all my pages have a little info box that tells the visitors just that. To just put this info on your front page isn&#8217;t enough, search engines or other external links can make them enter deeper into your site. Please put this little info-box somewhere on all of your sites. It&#8217;s one of the best ways for me to see I&#8217;m where I want to be.

To actually get your content interesting you need to work on your writing. My best tip is to follow the points Liz Strauss summed up nicely in her post about [what a reader wants](http://www.successful-blog.com/1/9-1-things-every-reader-wants-from-a-writer/).

Read through your text over and over again, out loud if you need to. Pay attention to typography, don&#8217;t make your paragraphs too long and use headers extensively.

## Conclusion

These are just some of the tricks I find myself using on my sites. I&#8217;m sure this site does not follow all of them perfectly but that doesn&#8217;t stop me from telling you about them, does it? Pick and choose as you like, but try to reach make you visitors feel that &#8220;it just works&#8221;-feeling.

Do you have any tricks you can share?
