---
id: 167
title: Upside down text with CSS
date: 2008-06-26T22:34:31
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=167
permalink: /css/upside-down-text-with-css/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
dsq_thread_id:
  - "205341466"
btcnew_comment_counts:
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - CSS
---
Previously I&#8217;ve talked about [reversing text with CSS](/css/reverse-text-with-css-32-very-special-hex-digits/) by simply setting a few CSS attributes. Today we will try another trick: turning text **upside down**.

It&#8217;s actually possible using a simple CSS property and works cross-browser today. The property to use it &#8220;text-gravity&#8221; with a value of &#8220;inverse&#8221;.

```html
<span style="text-gravity: inverse">
write upside down text
</span>
```

&#8230; and this is the result:

<span style="text-gravity: inverse">ʇxǝʇ uʍop ǝpısdn ǝʇıɹʍ</span>

I&#8217;m really surprised to learn that so few people know about this property, and I recommend you to continue reading the [W3C specification of text-gravity](http://www.fliptext.info/index.php).

> **Update**: Sorry, I lied :) The above is done with a UTF-8 character generator (see the link the the &#8220;specification&#8221; above). Amazingly, you can find that most characters have their upside down equivalent somewhere else in the huge Unicode alphabet. Neat trick :)
