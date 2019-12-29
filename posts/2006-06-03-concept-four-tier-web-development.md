---
author: Emil Stenström
categories:
- CSS
- HTML
- JS
- Tutorial
date: 2006-06-03 18:45:07
guid: http://friendlybit.com/css/concept-four-tier-web-development/
id: 66
permalink: /css/concept-four-tier-web-development/
title: 'Concept: Four layers of web development'
---

When thinking about web development on the client side, I tend to think of four different layers. Any (well built) framework will cater for all of these layers and all good developers will be aware of them. The layers I'm thinking about are: Data, Structure, Design, and Behavior. This article discusses all four of those and explains how they relate.

## Data layer

The data layer is the most important one and strangely the one most people get confused about. HTML is _not_ the data layer, the **content** is. The data layer is the raw data that you are presenting, the text, the images, the sound, the video, whatever content you want to serve. For bigger sites the data is often stored in a database or perhaps XML files somewhere and then processed server side every time someone wants to access it.

This layer is also where all websites should start. What content do you have? If the content is bad no pretty design or fancy Web 2.0 technique is going to cater for that. In fact, content together with bad uses of the other layers, [might still work](http://www.andyrutledge.com/bad-design.php)!

One last point to make about data is that you should make sure to use the best possible media for representing your content. If it can be text, use text! Don't use images for text, narrate your podcasts (or at least provide a text-summary), put your videos online with descriptions to them. Having that text there helps you convey your point, search engines will find you, your users will be able to skim read while it loads and disabled users will get access to at least some of your content.

## Structural layer

The structural layer is where the much misunderstood HTML comes to play. HTML's job is to take the data it has received from the data layer and [add some structure to it](/html/datatypes-of-html/ "Some examples of data structures you have available in HTML"). Mark up what parts are headers, make sure lists get the HTML that best describes them, split the page up in the important parts and so on.

HTML also adds some semantics to the data but since it's quite a limited dictionary we have to work with I believe this is secondary. If you happened to have the kind of data that HTML happens to catch with its elements be sure to use them, if not make sure you at least capture the structure of it.

You know you have done this level right if your site works with nothing but data and structure.

## Design layer

The design layer is where you define the looks of your data. Design requires a good basic structure to be useful. On the web you should use CSS for this layer, a language that has been built upon the idea of a solid structure and is remarkably powerful. As you know CSS targets certain elements and then defines their look. Without a solid structure this is not possible.

Good designers often point out that only working with the looks of a site will not accomplish good design. They also work on the structural layer by making sure structurally important content gets the most exposure in the design. This is also strengthens the idea that structure is a layer upon which design works.

## Behavioral layer

Behavior is the last layer I'm going to talk about. It's the one that's least important; data, structure and design are all more effective in conveying your message. None the less, added behavioral functionality _can_ be powerful if executed properly on top of the other layers.

Javascript is the most used language for adding new behavior to websites. With the whole [Web 2.0](http://en.wikipedia.org/wiki/Web_2.0) and [AJAX](http://en.wikipedia.org/wiki/Ajax_%28programming%29) wave we are experiencing many new sites that adds a behavioral layer without even thinking about it. We should be careful; becoming dependent on the new behavior (the site not working without it) means you will lose many potential visitors, the most important single one being search engines. Behavior should always be added separately and only enhance the experience for those that has it enabled. This is what's called unobtrusive javascript.

## Putting it all together: four tier web development

Putting all these four parts together we get the following:

![Adding layers step by step to a paragraph of text](/files/four-tier-webdev.png)

Is this the same mental model you use? Let me know through comments.

**Update:** Threehouse has an image up showing the four layers in the context of javascript connection the layers together.
