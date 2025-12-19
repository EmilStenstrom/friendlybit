---
author: Emil Stenström
categories:
- todo
date: 2025-12-19 12:00:00
guid: http://friendlybit.com/todo/new-post/
id: 1092
permalink: /todo/new-post/
title: 'JustHTML: Addressing some questions'
---

When Simon Willison wrote about JustHTML [\[1\]](https://simonwillison.net/2025/Dec/14/justhtml/) [\[2\]](https://simonwillison.net/2025/Dec/15/porting-justhtml/), suddenly everyone was interesetd in giving their view. After reading through (what I think is) all of them, I thought I'd address some questions that have arisen.

## "This is a copy / this is derived work!"
It is very unclear if JustHTML is a derived work. About half way in I did tell the LLM to "port html5ever", but I don't think that's what the LLM did. It started from the code structure of html5ever, but much of the code was trial and error against the html5lib-tests suite. In later versions I asked it to refactor much of the code, so don't think even the structure is there any more.

I asked an agent to try to find cross references between the two projects that still remain, but all it found were things that were also in the WHATWG HTML5 specification. This doesn't say it's **not** derivative work, but highlights that it's far from clear.

If you can find cases where the code is very similar (and not specifically required by spec), I would be happy to see it!

## "He stripped the authorship / laundered the license!"
This wording assumes an active attempt to strip it, which is opposite of me adding the html5ever [acknowledgement](https://github.com/EmilStenstrom/justhtml/blob/master/README.md#acknowledgments) to the JustHTML README. Just stop that nonsense. I have nothing but love for the html5ever developers. To put that to rest, I've decided to 1) add their copyright block to my license anyway and 2) [ask them specifically for guidance](https://github.com/servo/html5ever/issues/701). I'm looking forward to hearing their view.

For reference, this is the current `LICENSE` file in JustHTML:

```
MIT License

Copyright (c) 2025 Emil Stenström
Copyright (c) 2014-2017, The html5ever Project Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
...
```

## "He doesn't understand the code"
Many commenters were angry that I didn't *understand the code*. This is such an interesting take, especially in a society where not understanding is seen as weakness. We should be certain! We should know everything! But we don't. We're all fallible and walk around trying to figure things out.

In the specific case of the HTML5 specification, there are very few people—in the world—who understand it. HTML5 is an intricate web of algorithms, that interact in difficult-to-understand ways (see [htmlparser.info](https://htmlparser.info/) for a great guided tour). Did you know that the tokenizer and treebuilder affect each other?

Luckily for us, the authors decided to <s>shame</s> help browsers interoperate by publishing the fantastic html5lib-tests suite. It's an incredible feat of engineering, with thousands of integration tests that (almost) completely test the specification.

Here is a representative example of the kind of input those tests tests for:

```html
<p>One <b>two <i>three</b> four</i> five
<table><p><tr><td>cell</table>
<svg><foreignObject><p>inside svg</foreignObject></svg>
```

<small>That single snippet touches multiple "special" parts of the spec: mis-nested formatting elements (the adoption agency algorithm), implied end tags, table insertion mode oddities, and foreign content integration points.</small>

What's fantastic about html5lib-tests is that it gives us a way to look at our code from the outside and see if it works or not, **without us having to understand it**. If this feels extreme, think of low-level code—assembler—if you will. Do you understand how it flips the transistors in your computer? I don't. And that's fine, because you have other ways to know that your code works. You don't have to go into the details.

**LLMs are quickly becoming a new layer on top of the code we write. If we can find a way to prove that it works, we don't need to understand it. That opens up whole new possibilites!**

## "It's not high quality code, because it won't be maintained"

I'm very sure that this code is maintainable, because I have been maintaining it for a while already. As I was approaching 100% test coverage, a new HTML5 feature was added to the test suite: `<selectedcontent>`. This was easily supported with a couple of queries to the LLM.

I am planning to maintain it. The PRs are rolling in, and I have quite a clear image of where I want to take it. I think the API I've put on top of the parser is really attractive, with a very low learning curve. That's worth something, and it's missing from all the other libraries.

The first versions of the library were very hard to maintain, even with LLM help. When I looked under the hood there were messy nested if blocks, that mirrored some of the test data exactly. The LLM was cheating! I have not seen signs of this in the later versions of the code, and especially since LLM models got better.

---

I'm happy that my little experimant triggered so many discussion. Overall, I think (and you are free to disagree) that having this library is a big net positive for the Python community.
