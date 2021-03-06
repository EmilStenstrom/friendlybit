---
author: Emil Stenström
categories:
- JS
date: 2007-01-16 00:02:35
guid: http://friendlybit.com/js/flash-only-vs-ajax-sites/
id: 111
permalink: /js/flash-only-vs-ajax-sites/
title: Flash-only vs. AJAX sites
---

Even though web developers like me have discouraged from building Flash-only sites for as long as I remember, they are popping up all over the place. For no reason! We are ready to make the leap to standards. And our weapon with be AJAX.

## What kind of sites are built with only Flash?

Let's start by having a look at a few big Flash sites. Because they exist, and keep popping up all over the place. Here's a couple of movie sites using it: [Departed](http://thedeparted.warnerbros.com/), [Underworld Evolution](http://www.sonypictures.com/homevideo/underworldevolution/index.html), [Matrix](http://whatisthematrix.warnerbros.com/); Here's a couple of big brands: [Coca-cola](http://www.coca-cola.se), Nike, [Electrolux](http://electrolux.com/). These sites are more than just animated images, they have their own content and often need to get updated continuously.

## What's the purpose of them?

Before deciding on anything we need to examine what purpose these sites have. It's not OK to change the purpose of the site just because we dislike the technology behind it. I can't possibly know the reasons behind all of the campaigns going on today but I believe there's a core that most sites are after.

  * **Promote something new** - Someone wants to to push some of their products/deals/ideas to the spotlight.
  * **Specific target audience** - Companies are well aware that what kind of people they reach initially will define if the product is successful or not. Many want the hip people.

## Updating flash files is hard

Many years ago it was ok just to throw up static information on a site and have a good site. Don't get me wrong, content is still king, what has changed is that content alone isn't enough. We demand much more from a good website. Coca Cola can't just publish a press release telling us that there is a new taste out. It's the Web 2.0 age and we want to be able to send our own tasting stories in, we want to be able to see live counters of the number of bottles sold, and we want forums to talk amongst ourselves about our experiences. We want tags! You get the point.

How does this affect the choice of flash or not? We need dynamics, ways for both editors and users to add content to the site, and **Flash files are hard to update**! Just the fact that I need a special program to edit them speaks for itself.

Another fact: As you probably know, it's rare (in the real world) to have the same person both writing code and publishing content. The coders need to cater for that, and make sure it's easy for editors to add new content. Now. Even if you've bought licenses and are able to edit flash files, you can't expect editors to understand all about how flash works. So you need to build a content management system (CMS) of some kind. If you buy one, you still need to integrate it with your current code.

"But", I hear you say, "…you have that same problem with non-Flash sites!". Yes, but the difference is that CMS tools that publish HTML have existed a lot longer. This affects both the quality, usability and ease of integration with current systems. A HTML-based site will therefore be easier to update, making for both more and fresher content that reaches more people. If it's easy enough to update the site, you can even let users do it, Web 2.0 style.

## Flash is not hip any longer

Publishing a site with Flash today is hardly going to get mentioned at all. AJAX has completely taken over the scene and anyone even whispering AJAX gets to the front page of digg.

Aside from the technology buzz we have had some real changes rather recently: Javascript can now deliver what was once only available with Flash. It can fade, move, round corners, drag-drop, auto-save, validate, the list could go on forever… There's several effect libraries available that makes using all those effects easity. All the good ones are even free.

## Flash-only vs. AJAX - The showdown

I've made a small list of things that matters when you build a website today, and evaluated each one of them for both Flash-only and AJAX.

<table>
  <tr>
    <td>
    </td>
    <th scope="col">
      Flash
    </th>
    <th scope="col">
      AJAX
    </th>
  </tr>
  <tr>
    <th scope="row">
      Accessibility
    </th>
    <td class="incorrect">
      <strong>Poor</strong>. There's problems with everything from how a flash app gets its initial focus from the browser window, to unusual interaction controls, to lack of text resize. In summary, zero points.
    </td>
    <td class="almost">
      <strong>Moderate</strong>. AJAX has problems with requiring js for accessing data, but smart developers have started thinking in terms of accessibility and fixed many of AJAX initial flaws. <a href="http://www.robertnyman.com/2006/02/08/ask-ajax-source-kit">Nyman's ASK</a> is one way.
    </td>
  </tr>
  <tr>
    <th scope="row">
      Search Engine Optimization (SEO)
    </th>
    <td class="incorrect">
      <strong>Poor</strong>. Search engines don't read flash files (even though they probably could). Some people claim that you should <a href="http://blog.deconcept.com/2006/03/13/modern-approach-flash-seo/">duplicate all your content</a>. I say that will be a mess to update.
    </td>
    <td class="almost">
      <strong>Moderate</strong>. If you just use the javascript effects you are fine, if you fetch data with javascript you need to write a little script that reloads the content and gets it that way instead. It is possible, but not easy enough. Bonus: if you fix accessibility you often get this too.
    </td>
  </tr>
  <tr>
    <th scope="row">
      Ease of content change
    </th>
    <td class="incorrect">
      <strong>Poor</strong>. You need an expensive program to edit the files. ? Only available on PCs running Windows. Few CMS:es available (any?) that makes it easy for editors to update content.
    </td>
    <td class="correct">
      <strong>Strong</strong>. All the big CMS:es can be used together with an AJAX app, it's just a matter of changing the templates on the front. Systems like Ruby on Rails (while not being a CMS) have built in support for AJAX stuff, but including a framework in older systems is no big deal.
    </td>
  </tr>
  <tr>
    <th scope="row">
      Hipness
    </th>
    <td class="incorrect">
      <strong>Poor</strong>. There used to be a big community of flash developers that got incredible respect in the webdev community with their flash-only sites. Many of these communities have been replaced by CSS Galleries of different kinds.
    </td>
    <td class="correct">
      <strong>Strong</strong>. While Flash-only developers focused mainly on visuals the AJAX community have focused more on user experience, building applications that <em>feels</em> better to use. Together with the technology buzz behind it AJAX solutions have gotten (and still get) a great response from the start. The potential for marketing campaigns based on user experience in huge.
    </td>
  </tr>
  <tr>
    <th scope="row">
      Graphic effects
    </th>
    <td class="correct">
      <strong>Strong</strong>. This wouldn't be a fair comparison if we didn't acknowledge that Flash is far ahead of AJAX when it comes to graphic effects. Most of this is based in the fact that you are working in an application instead of a website, and things like anti-aliasing, drop shadows, transitions, and filters have existed for long.
    </td>
    <td class="almost">
      <strong>Moderate</strong>. Websites was long lacking pretty interfaces but in the recent years we've seen an explosion of graphic effects even in the standards world, probably starting with the famous <a href="http://www.csszengarden.com/">CSS Zengarden</a>.
    </td>
  </tr>
  <tr>
    <th scope="row">
      Integration with existing sites
    </th>
    <td class="almost">
      <strong>Moderate</strong>. Few code libraries are written to work well together with flash, so often you have to do the integration yourself. In it's latest version Flash has gotten more integration points with the possibility to communicate with javascript, import HTML and so on. Better, but not perfect.
    </td>
    <td class="correct">
      <strong>Strong</strong>. Most effect libraries are built to be as easy to include as possible. The usual way to make use of one is two lines long: link a javascript file and call the right function. The more advanced libraries that enable asynchronous loading require some more work, but unless you want advanced error handling it's no big deal.
    </td>
  </tr>
</table>

Next time a customer ask for a Flash-only site, tell them about AJAX and it's advantages.
