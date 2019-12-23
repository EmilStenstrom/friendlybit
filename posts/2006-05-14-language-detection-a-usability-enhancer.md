---
id: 63
title: Language detection, a usability enhancer?
date: 2006-05-14T01:05:19
author: Emil Stenström
layout: post
guid: http://friendlybit.com/other/language-detection-a-usability-enhancer/
permalink: /other/language-detection-a-usability-enhancer/
btc_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
  - 'a:0:{}'
  - 'a:0:{}'
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - Other
---
Natural language is by many considered something with very little structure. What many people don&#8217;t know is that there are parts that are easily analysed. This article explains a simple but very effective algorithm for detecting what language a text are written in and continues to discuss possible applications.

More and more of the worlds population comes online and far from everyone want to write in English. In fact, most of the content online is not in English. This leads to the need for more tools that handle different languages; that translate, finds synonyms and so on. Different languages are important so we are going to need tools to handle that. This article handles the latin alphabet, simply becuase it&#8217;s the only one I know. I&#8217;m sure you can apply the same ideas to other alphabets aswell.

## How to detect language

When looking at the differences between languages you can find that they are many. Words, grammar, sentence length, number or syllables&#8230; we can go on forever. People skilled in both languages and algorithmics quickly found a very reliable way to tell languages apart: _Bigram statistics_. A bigram is just a pair of two letters like &#8220;xt&#8221; or &#8220;ty&#8221;.

It turns out that bigram statistics for a text stays fairly constant (there&#8217;s always few &#8220;tp&#8221; in English) and sometimes you don&#8217;t need more than a sentence to determine the language. This is how the algorithm works:

  1. **Remove or translate characters** you don&#8217;t want to count. You might want to take into account special characters in different languages like É and Ü and decide how to handle them. Be sure not to remove the space character, it gives good statistics over with which letter words start and end.
  2. **Split the text into bigrams**. For this to work you need to take all bigrams in each word, that is, each letter is included twice. Example: &#8220;hello&#8221; contains &#8220;\_h&#8221;, &#8220;he&#8221;, &#8220;el&#8221;, &#8220;ll&#8221;, &#8220;lo&#8221;, &#8220;o\_&#8221; (&#8220;_&#8221; means space). The more text, the more reliable the result will be.
  3. **Count the occurrence** of each bigram in a long list that contains all the bigrams.
  4. **Calculate statistics** over how often each bigram occurred.
  5. **Compare** with precalculated lists over different languages. You need to compile this list yourself but it&#8217;s easy. Use [Google Advanced Search](http://www.google.com/advanced_search) and set the language you want from there.
  6. **Pick the language** that has the most similar list.

The only hard part to program is the comparing of two lists. For this we will use the [Euclidean distance](http://en.wikipedia.org/wiki/Euclidean_distance) of the two lists of numbers. In essence, this is how Euclidean distance works:

  1. **Pick the values** for the first bigram from the two lists you want to compare.
  2. **Calculate the difference** between the two values and **square it**.
  3. **Repeat 1 and 2** until you have one result for each bigram pair.
  4. **Add all those results** together and calculate the **square root** of that sum. You have your distance.

Euclidean distance gives us a number. The lower the number the more like each other the two lists are. So we compare the calculated list with the precompiled lists for other languages and pick the language with the lowest number.

## Real world applications

As you&#8217;ve see above detecting language isn&#8217;t rocket science. Anyone with some solid programming skills could implement the algorithm above no matter what programming language. Anyone could also gather the statistics needed to make some bigram lists for different languages. So you could expect that this is used all over right? Wrong. A few examples:

Since my native language is Swedish I have downloaded an extra dictionary for Thunderbird to make it able to check both my Swedish and English e-mails for errors. It works well except for one thing. Since about half of the e-mails I send are in each of the languages, the dictionary is almost always set to the wrong one. Since the language is not shown anywhere I usually type a few words, think &#8220;what, isn&#8217;t that correct?&#8221;, and then remember that the wrong dictionary is selected. You can see where the language detection above would fit in right? They don&#8217;t even need to see what I&#8217;m going to type; the language I will reply with will be the same as in the e-mail I&#8217;m answering to. That&#8217;s usability.

Another example. Too few webmasters know about the [lang attribute](http://www.w3.org/TR/html4/struct/dirlang.html#h-8.1). It can be set on all HTML elements and specifies what language the content is in. The HTML 4 specification lists the following reasons to why you should use lang:

  * Assisting search engines
  * Assisting speech synthesizers
  * Helping a user agent select glyph variants for high quality typography
  * Helping a user agent choose a set of quotation marks
  * Helping a user agent make decisions about hyphenation, ligatures, and spacing
  * Assisting spell checkers and grammar checkers

It all boils down to: it&#8217;s a good thing to say what language a page is written in. The problem is, not many know that the lang attribute even exists. Solution? Let the screen reader, browser, or search engine (they are doing it) auto-detect the language and act on it.

A third example is all those chat rooms. There are rooms all over the place and the topics range from poker strategies to horse equipment. What they all have are lots and lots of users and rooms where you can talk, in any language you want. Wouldn&#8217;t it be nice if the chat software automatically detected which language was spoken in a room? Then you could see even before joining. Or even what languages a certain user speaks.

I&#8217;ll call that the end of this article. It moved a bit outside of the webdev area but I hope you still liked it. Have any more ideas of where this could be useful? Want to show your javascript/python/ruby/etc implementation of it to me? Leave a comment.
