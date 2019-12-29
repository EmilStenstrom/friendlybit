---
author: Emil Stenström
categories:
- Browsers
- Fonts
date: 2009-05-08 20:20:17
guid: http://friendlybit.com/?p=480
id: 480
permalink: /browsers/custom-fonts-using-cufon/
title: Custom fonts using Cufón
---

If you've worked with webdev professionally you know how it goes. "Why can't a company with a strong visual brand get to use their own font?", the designer asks. Then a long discussion about web fonts follow, where you decide to replace the font with a "web safe" font instead. Or do you?

You could think it's strange that in 2009, we can't use any fonts we want on the web, and I would fully agree. You could ask whose fault that is, and I would reply with a quote from a [meeting between browser makers in august 2008](http://www.w3.org/Fonts/Misc/minutes-2008-10):

> "My understanding, from Chris, is that supporting direct linking of the fonts would be a great disservice to the independent font industry. **A high-level decision within MS** says we won't implement that in IE. So what is done other than EOT is [probably] not going to interop with IE. "

"MS" is of course Microsoft, and "Chris", is referring to Chris Wilson, Platform Architect of the Internet Explorer Platform team. The same Chris has also written a [longer text about font linking](http://cwilso.com/2008/07/23/fonts-embedding-vs-linking/) on his blog. I first thought that this was something the font foundries had pushed through, but on the above post it seems that this is also a personal opinion. Browsers (but only IE) need to protect fonts from getting pirated.

And that's the whole reason why we don't have cross-browser fonts on the web today. (Although direct linking to fonts work in all the latest versions of Firefox, Opera, and Safari). Nice isn't it?

## Embedding fonts anyway

Of course, there's still a need to embed custom fonts on webpages. That means clever developers will develop techniques will work around a broken internet explorer. No matter what the font founderies and Internet Explorer team thinks.

My reasoning for why this is a good thing is because that's how everything else works in the browser. Even though anyone can copy an image, we have a big market for stock images. Even though anyone can copy the HTML, CSS, and Javascript of a whole site, we still have people building websites for money. **Fonts are no different**, and the exact same business model that works for stock images can work for fonts.

\***

One popular technique is sIFR, a way to use javascript to replace regular html with flash. Inside the flash you embed the font you want, and voilá, you can use any font you want. sIFR misses one crucial point though: It's far too annoying to embed a font inside a flash movie. You need a commercial program, and you need to know what you're doing. And you're dependent on flash support. It's not that bad, but a bit annoying to work with.

So for a recent project I've been playing with [Cufón](http://wiki.github.com/sorccu/cufon/about), which uses javascript, but draws on canvas, or in VML for browsers that don't support canvas (IE). They have an extremely friendly website, which walks you through the process of getting things to work, and the font conversion needed is available directly on the website. I've only used it for simple cases, but it works really well.

All in all, Cufón is a great alternative until IE gets its shit together.

PS. Famous people that don't agree with me:

  * [Richard Rutter](http://clagnut.com/), author of the clagnut blog suggests that font founderies [server-side generate our fonts on demand](http://clagnut.com/blog/2166/), much like Google Maps only sends a part of the map, and not all of it.
  * [Joe Clark](http://joeclark.org/): "Quite simply, there is [no broad clamour](http://blog.fawny.org/2008/07/22/billhillsite/) among Web _designers_ to use any font they want."
  * [Jason Santa Maria](http://jasonsantamaria.com/): "embedding normal typefaces without any sort of precautions is putting it on a silver platter for anyone to take freely. That’s like saying people steal from stores anyway, so let’s just leave the doors unlocked at night :)"
  * And of course, the IE team…
  * …and all the typeface makers in the world.
