---
author: Emil Stenström
categories:
- CSS
date: 2008-06-26 22:34:31
guid: http://friendlybit.com/css/upside-down-text-with-css/
id: 167
permalink: /css/upside-down-text-with-css/
title: Upside down text with CSS
---

Previously I've talked about [reversing text with CSS](/css/reverse-text-with-css-32-very-special-hex-digits/) by simply setting a few CSS attributes. Today we will try another trick: turning text **upside down**.

It's actually possible using a simple CSS property and works cross-browser today. The property to use it "text-gravity" with a value of "inverse".

```html
<span style="text-gravity: inverse">
write upside down text
</span>
```

… and this is the result:

<span style="text-gravity: inverse">ʇxǝʇ uʍop ǝpısdn ǝʇıɹʍ</span>

I'm really surprised to learn that so few people know about this property, and I recommend you to continue reading the [W3C specification of text-gravity](http://www.fliptext.info/index.php).

> **Update**: Sorry, I lied :) The above is done with a UTF-8 character generator (see the link the the "specification" above). Amazingly, you can find that most characters have their upside down equivalent somewhere else in the huge Unicode alphabet. Neat trick :)
