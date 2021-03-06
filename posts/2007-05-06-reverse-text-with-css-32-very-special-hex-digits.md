---
author: Emil Stenström
categories:
- CSS
date: 2007-05-06 18:13:32
guid: http://friendlybit.com/css/reverse-text-with-css-32-very-special-hex-digits/
id: 123
permalink: /css/reverse-text-with-css-32-very-special-hex-digits/
title: Reverse text with CSS (32 very special hex digits)
---

Sometimes you wake up and feel that [big things](http://yro.slashdot.org/article.pl?sid=07/05/02/0235228) are moving around you. You follow the news and find that people are uniting over something simple as a number. You read about people [calling them rebels](http://technology.timesonline.co.uk/tol/news/tech_and_web/article1749672.ece).

I think this is a good time to show a little CSS trick.

Let me present two properties that together reverse a string of text: direction and unicode-bidi:

```html
<p style="direction: rtl; unicode-bidi: bidi-override;">
0C 88 65 36 5C 65 14 8D B5 3E 47 D9 20 11 9F 90
</p>
```

The result, when this is posted on your blog (\*hint\*) is the following:

<code style="direction: rtl; unicode-bidi: bidi-override;">
0C 88 65 36 5C 65 14 8D B5 3E 47 D9 20 11 9F 90</code>

Am I a CSS rebel now? And are they going to sue me on the basis of my HTML or my CSS?
