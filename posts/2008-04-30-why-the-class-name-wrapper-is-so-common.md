---
author: Emil Stenström
categories:
- HTML
date: 2008-04-30 15:06:27
guid: http://friendlybit.com/html/why-the-class-name-wrapper-is-so-common/
id: 159
permalink: /html/why-the-class-name-wrapper-is-so-common/
title: Why the class name "wrapper" is so common
---

We've all heard about how bad it is to use "left" and "yellow" as class names and ids. If you name an element "left", and then decide to move that element to the right, you have to go through all your pages and change that name. Too much work.

If you instead had called it "licenseAgreement", you would have been better off. Right? Perhaps not. Because we're forgetting about CMS:es. Those often have some kind of templates, where you as an interface developer define how the HTML should look. But as a interface developer, you have no idea of what kind of content editors will put into your templates. A couple of clicks later your "semantic id" is wrong.

**I think this is one of the reasons semantics hasn't gotten a hold of the CMS world**. CMS:es have no idea of what kind of content people will store in them. Their main business goal is to make something generic, that doesn't assume semantics.

This is why "wrapper" is such a common class name.
