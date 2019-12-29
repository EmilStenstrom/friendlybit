---
id: 128
title: Quick Accessibility Testing
date: 2007-06-24T21:57:53
author: Emil Stenström
layout: post
guid: http://friendlybit.com/tutorial/quick-accessibility-testing/
permalink: /tutorial/quick-accessibility-testing/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
dsq_thread_id:
  - "206191574"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - Tutorial
---
A recent project of mine required me to do a quick review of the accessibility level of a site. Nothing serious, just to show what was possible to test and where the site scored right now. I managed to assemble a small list of tools that I believe did a rather good job. This article is a list of those tools, and some tips on how to use them.

First off, to do a real accessibility test, you need real people, with real tasks to accomplish. These are not tools to replace people. Instead, they can give you a quick rundown on where you stand, and find things you've missed. I like to compare it with HTML validation: Validation is a great way to find your errors, but just because you validate does not mean you have good code.

Oh, by the way, I limited this to only free tools. Thought you'd like that. Also, for your enjoyment, I've split this article into three parts (you're just soooo spoiled):

  * [Automatic testing](#auto)
  * [Semi-automatic testing](#semi)
  * [Manual testing](#manual)

## Automatic testing {#auto}

Automatic testing is one of the quickest way you can check your site's accessibility. What the authors of the below tools have done is to go through the available standards, and tried to find things that a computer can check. The tools will not find every error, but the things they do find, they find quickly. This is why I like to start with these.

  * **[W3C Markup Validation Service](http://validator.w3.org/)** - This is a real classic. It goes through your HTML or XHTML and makes sure you follow the basic syntactic rules. What does this have to do with accessibility? Well, if you deliver invalid code, you have no chance but to test every user agent and how it renders your page. Will you do that? Didn't think so.
      * **Bonus #1**: Test up to 100 pages of your site at once with the [WDG HTML Validator](http://htmlhelp.com/tools/validator/), just check "Validate entire site" before you validate.
      * **Bonus #2**: As a developer it's handy to get to know directly if the page you're looking at validates or not. [HTML Validator for Firefox](http://users.skynet.be/mgueury/mozilla/) is an extension that sits in your browser's status bar, and shows a red cross when something is wrong. When you double click the icon it shows you the exact error. Very handy.
  * **[W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/)** - Even though screen readers don't care much about the CSS you need to make sure it's alright. Why? Because there's more to accessibility than screen readers. Surely, most people that need your help are people surfing with their ordinary browsers: Internet Explorer, Firefox, and so on. To make sure all of them see the content and can interact with it, check your CSS for obvious errors automatically.
  * **[Cynthia Says](http://www.cynthiasays.com/)**, **WebXACT**, and **Wave Accessibility Tool** are all testing tools that are aimed at accessibility testing. They support both Section 508 (an American accessibility standard) and WCAG 1.0 (W3C's own standard). Like the W3C tools above they do not catch all errors, in fact, most of the feedback you get is that you should check things manually. None the less, they often find simple errors that you have missed. Make sure you enable all extra options when using them.
  * **Basic accessibility analyzer** is a much less known, but very impressive accessibility tester. Among other things it adds checks for proper heading structure and form labels, two things many have problems getting right. Built by Peter Krantz (former colleague of mine) and based on his [accessibility library](http://www.peterkrantz.com/raakt/wiki/) for Ruby).
  * **[W3C Link Checker](http://validator.w3.org/checklink)** is another tool that's easy to forget about. It walks through your site and picks out all the links it finds, checking that each of them works. Using a tool like this makes sense for more than accessibility reasons, but accessibility alone is a reason to use it.
  * **[Juicy Studio](http://juicystudio.com/services.php#hosted)** hosts a whole series of useful online automatic tools. There's tests for Readability, Your CSS file, Luminosity and Color Contrast (really useful), and an Image tester. You will most certainly find something to improve here.
  * **[Nikita the spider](http://nikitathespider.com/)** is a great tool going through a lot of pages in search for errors. It crawls through a site and reports broken links, missing doctypes, and validation errors. Good for big batch checks after the fact.

## Semi-automatic testing {#semi}

Semi-automatic tools do part of the work for you but also requires that you twiddle with the results yourself. They can't give you a "passed validation" stamp to put on your site, but correctly used they can give you deeper knowledge than the automatic ones.

  * **[Accessibility Toolbar](http://www.visionaustralia.org.au/ais/toolbar/)** for Internet Explorer is a collection of accessibility tools bundled as a toolbar. The best part of it is it's support for color and contrast testing. Click "Colour -> Contrast Analyzer [application]". By selecting "Simulation" from the menu you can see what your site looks like with different vision impairments. If you rely on color alone for some feature it will be obvious with some testing with this tool.
  * **[Fangs](http://www.standards-schmandards.com/projects/fangs)** is a screen reader simulator in the form of a Firefox plugin. It's simply shows (not reads) the text on a page as it would be read by a screen reader. This is a great way to get a feel of how your site works with non-visual browsers. Due to a bug in Firefox you need to run an English version of the browser before installing Fangs. It's worth switching language to run Fangs, it helps that much.

## Manual testing {#manual}

Then we have the old fashioned gruntwork, manual testing. I'm going to put things here that you don't use special tools for, just the browser and your accessibility knowledge.

  * **Testing in several browsers** is of course the most obvious way to test a site. If 10% of your users can't access the site because it doesn't work in Firefox you have a problem. So fire up both versions of Internet Explorer (6 and 7, not 5.5, it's dead), the latest version of Firefox and Opera. If you have access to a Mac make sure it works on Safari there too. If not you have to try with the buggy [Safari 3 beta for Windows](/other/safari-now-available-on-windows/) (it's better than nothing).
  * **Text zoom** is one of the first things you should try. Firefox and Internet Explorer 6 relies on only enlarging the text, and not the whole window, so make sure you test that. Internet Explorer refuses to zoom text set in pixels, so keep a lookout for that. Text zoom helped me greatly when my old monitor broke and got all blurry. Thanks for letting me zoom!
  * **Turning off CSS and Javascript** is another great way to make sure people can access your content. You don't need to mind what the content _looks like_, just make sure it's understandable and that things work as expected.
  * **Remove images** and replace them with alt text. There's options to do this with both [Web Developer Toolbar](http://chrispederick.com/work/web-developer/) and the previously mentioned Accessibility Toolbar. Testing your image alternatives helps both people that gets their content read to them and those that disable image loading due to a slow dialup connection.
  * **Keyboard navigation** is another thing to test. Just push your mouse to the side and navigate using only the keyboard (use the tab-key, arrows and enter). Does things work like you expect? Good, you passed.

That's it. Lots of little tools and tricks you can use to make your site accessible to more people. If you ask [Jakob Nielsen](http://www.useit.com/alertbox/) or [Roger Johansson](http://www.456bereastreet.com/) if this is enough they will of course say no, but I say you should be proud anyway! Passing most of the above tests isn't easy, and you're certainly on the right track now. Well done!

Feel free to tip me off on more tools using the comments. Thanks for reading!
