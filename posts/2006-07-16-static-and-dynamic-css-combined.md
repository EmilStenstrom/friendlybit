---
id: 80
title: Static and dynamic CSS combined
date: 2006-07-16T18:56:03
author: Emil Stenström
layout: post
guid: http://friendlybit.com/css/static-and-dynamic-css-combined/
permalink: /css/static-and-dynamic-css-combined/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205286133"
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
Some of you have probably heard &#8220;dynamic CSS&#8221;. It originates from a need to serve different CSS at different times, to different people, or on different pages. You do this by first generating the CSS on the server and then sending it off to the users requesting it. There are problems though, since the CSS gets regenerated each time you lose the advantage of caching. You could send HTTP headers so that the file gets cached anyway, but then it&#8217;s no longer dynamic right? This article presents a way to both have dynamic CSS that changes on each request, and make sure the user loads it from cache when it can.

## How dynamic CSS works

Sometimes you want to send a different set of CSS rules depending on what page you are on. An example could be if your site was module based. Depending on what page you surf to you might get a calendar, some list of latest news or a small box showing the weather in, say, Stockholm.

The functionallity is not too hard to build with some server side language, but what about the CSS? Is it really necessary to load the calendar&#8217;s CSS on the news page, where the calendar is hidden? The same thing applies for each of the modules you have on your site; that list of news has certain CSS rules tied to it that isn&#8217;t needed on the gallery page. You get the point. So how do we solve this? We could do it my generating it on the fly (I&#8217;m using PHP here, but any other language would work):

PHP source:

```css
<?php
// This line makes sure the browser handles
// the file as CSS and not PHP.
header('Content-Type: text/css');

if ($module['calendar'] == true) {
   echo '
      .calendar { width: 300px; }
      .calendar table { background: pink;}
      ...
   ';
}
if ($module['newslist'] == true) {
   echo '
      .newslist { list-style: none; }
      .newslist li { display: inline; }
      ...
   ';
}
[and so on every new module added]
?>
```

Generated file:

```css
.calendar { width: 300px; }
.calendar table { background: pink; }
...
.newslist { list-style: none; }
.newslist li { display: inline; }
...
```

You save this file as &#8220;dynamic_stylesheet.php&#8221; and link it like you would if it was a static CSS file. Everything works fine and all the dynamic CSS makes the file sent to the user quite small. Both you and your users are all happy. The site starts growing.

## Problems with dynamic CSS

After a while you start getting reports of the site getting slow. After some research you find that it&#8217;s in fact the dynamic CSS that does it. The file has gotten quite big and regenerating it each time is a lot of work. So you read up on caching and find that all that&#8217;s needed is a few lines at the top of your dynamic CSS file:

```php
header('Cache-control: must-revalidate');
header('Expires: ' . gmdate('D, d M Y H:i:s', time() + 3600) . ' GMT');
```

This makes the browser load the file from cache for one hour instead of requesting it again. Problem solved! Right? Well, this means that you won&#8217;t get a regenerated file if you visit a new page on the site. The browser will load the style from cache instead and your users will get an unstyled calendar (or any other module) for an hour. Pretty annoying if you ask me.

Say we solve the problem above and get the page to only get cached on a per page basis. There&#8217;s still something that feels like a bit of a waste: we require the user to download the entire page again if just one of the modules changes. Say the user moves from the news list to checking out a certain news item. They will probably look pretty much the same, it&#8217;s just that the news list&#8217;s CSS won&#8217;t be needed on the news item page. We would need some way of only telling the browser to only cache parts of the files and make the loading of those parts dynamic.

## @import to the rescue

Caching only fragments of your style is certainly doable in a lot of ways. The easiest I have found is using CSS&#8217;s own @import command. You simply change the example above to:

```css
<?php
// This line makes sure the browser handles
// the file as CSS and not PHP.
header('Content-Type: text/css');

if ($module['calendar'] == true) {
   echo '
      @import "calendar.css";
   ';
}
else if ($module['newslist'] == true) {
   echo '
      @import "newslist.css";
   ';
}
[and so on every new module added]
?>
```

Generated file:

```css
@import "calendar.css";
@import "newslist.css";
```

This makes the individual CSS files get cached by the browser (just like directly linking a CSS file would) while still allowing each page to dynamically add the style blocks it needs. A simple solution to a hard problem, just the kind of solutions I like best. What do you think?
