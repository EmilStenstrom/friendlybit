---
comments:
- comment_ID: '32930'
  comment_author: Emil Hesslow
  comment_author_url: http://extensions.hesslow.se
  comment_content: http://a.deveria.com/caniuse/ , nice page where you could see which
    features you can use in which browser.
  comment_date: '2009-08-27 00:02:32'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32931'
  comment_author: Csaba Kétszeri
  comment_author_url: http://www.ketszeri.hu/
  comment_content: A "please drop your current browser and use something better" message
    is too similar to the old "optimized for Netscape Navigator" ones.\n\nIt simply
    sends out a negative message about the page.\n\nIf the sale/marketing and the
    customer service department agrees in that this kind of message should be on the
    page, it is fine for the IT to put it on. After all, a world without IE6 is a
    better world. :)
  comment_date: '2009-08-27 07:27:13'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32932'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Csaba Kétszeri: Are you arguing that we should <em>never</em>
    let go of IE6? Because that "optimized for..."-message will look just as bad in
    2014 when Microsoft''s support for IE6 is dropped. Btw. that dropping could be
    something as simple as disabling the CSS for IE6, while still letting them get
    to the content.'
  comment_date: '2009-08-27 08:04:14'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '1'
- comment_ID: '32933'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Emil Hesslow: That''s a great reference list. I love the summary
    box at the bottom, stating that 96% of the features in the list does not work
    in IE6.'
  comment_date: '2009-08-27 08:05:47'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '1'
- comment_ID: '32934'
  comment_author: Roland Bouman
  comment_author_url: http://rpbouman.blogspot.com/
  comment_content: Hi!\n\nyeah, I can't wait for it to die out too. Another thing
    that is sorely missing in IE6 is a print preview that doesn't suck.\n\nBTW:\n\n"Multiple
    classes/ids on the same element"\n\nAFAIK, multiple classes on the same element
    works fine in IE6. At least I use the feature and it seems to work for me. Am
    I missing something?
  comment_date: '2009-08-27 11:19:17'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32935'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Roland Bouman: It''s easy to think that multiple classes work,
    but in fact they don''t. Try styling something like .class1.class2 { [css here]
    }. You''ll notice that everything with class2 gets that styling, whether or not
    it has class1 applied too. It''s trixa, and very easy to miss.'
  comment_date: '2009-08-27 12:09:37'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '1'
- comment_ID: '32936'
  comment_author: Roland Bouman
  comment_author_url: http://rpbouman.blogspot.com/
  comment_content: 'Hi Emil! \n\nWhen you wrote "multiple classes on the same element"
    I thought you meant:\n<code>\n&lt;style type="text/css"&gt;...\n.class1 { font-weight:
    bold}\n.class2 { background-color: red}\n&lt;/style&gt;\n...\n&lt;div class="class1
    class2"&gt;...&lt;/div&gt;\n</code>\nand this works fine - the div is styled bold
    with a red background.\n\nWhat you are describing in your reply seems more like
    a ruleset with multiple class selectors. I tried it, but I can''t get your particular
    example to work at all (tried Chrome, IE8 and FF 3.5). Am I missing something?'
  comment_date: '2009-08-27 16:38:10'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32937'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Roland Bouman: Here''s an example applying CSS to elements with
    multiple classes: http://www.webdevout.net/test?01Z - scroll down to see the result.'
  comment_date: '2009-08-27 20:15:39'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '1'
- comment_ID: '32938'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: 'The min/max height can be set in IE6 with the followings:\n\nFor
    max height:\n<code>* html div#division {\nheight: expression( this.scrollHeight
    &gt; 332 ? “333px” : “auto” ); /* sets max-height for IE */\nmax-height: 333px;
    /* sets max-height value for all standards-compliant browsers */\n}</code>\n\nFor
    max witdh:\n<code>* html div#division {\nwidth: expression( document.body.clientWidth
    &lt; 334 ? “333px” : “auto” ); /* set min-width for IE */\nmin-width: 333px; /*
    sets min-width value for all standards-compliant browsers */\n}</code>\n\nAnyway,
    i think that we could all e-mail Microsoft with suggestions about these facts.'
  comment_date: '2009-08-27 22:43:16'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32939'
  comment_author: John Stathon
  comment_author_url: http://biletul-zilei.net
  comment_content: I think that the biggest problem with IE and the big thing that
    IE6 can't do is offer you protection. \n\nIt has many vulnerabilities as it benefits
    from a poor update system.\n\nIf you don't want to include the code that @Emil
    published in your websites you should know the following tips to avoid problems
    with your site design in IE6.\n\n1.Use a doctype\n2.Use display:inline for all
    floated elements\n3.Use only <code>&lt;a></code> tags formhovered elements. (the
    CSS hover effects that IE6 can only apply are limited to <code>&lt;a></code> tags)\n4.Avoid
    Percentage dimensions\n\nI think that is a good idea to create a website with
    this theme of discussion, or support the existing ones.
  comment_date: '2009-08-27 23:38:40'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32940'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: Have a look at what Microsoft has to say about this:\n\nhttp://news.bbc.co.uk/2/hi/technology/8196242.stm\n\n'The
    software giant said it would support IE6 until 2014 - four years beyond the original
    deadline.'
  comment_date: '2009-08-27 23:59:35'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32941'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Alex: I linked to an article about that in the first sentence
    :) "except Microsoft themselves".'
  comment_date: '2009-08-28 07:35:20'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '1'
- comment_ID: '32942'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Alex: About your max-width/max-width suggestions. Using expressions
    is not a recommended way to work around IE6:s problems. The problem is that they
    are evaluated too often, even as you <a href="http://robertnyman.com/2007/11/13/stop-using-poor-performance-css-expressions-use-javascript-instead/"
    rel="nofollow">move your mouse around</a>. Slow computers get a very sluggish
    behaviour, which is why optimization tools like <a href="http://developer.yahoo.com/performance/rules.html#css_expressions"
    rel="nofollow">YSlow recommends against</a> using them at all. \n\nThe point here
    isn''t that there are no workarounds. There are. It''s about developers being
    able to focus on CSS, not those workarounds, and therefore be more productive.'
  comment_date: '2009-08-28 07:56:14'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '1'
- comment_ID: '32946'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: '@Emil, i had adblock enabled on Firefox and the “except Microsoft
    themselves” link had a full banner ad so the page was not loading. \n\nAnyway,
    the majority of surfers that use IE6 are begginers so without Microsoft help it''s
    very hard to make them change/upgrade their browser.\n\nRegarding your last comment,
    what is the best way to avoid problems with Min-height, Max-height, Min-width,
    Max-width in IE6?'
  comment_date: '2009-08-29 14:42:25'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32947'
  comment_author: John Stathon
  comment_author_url: http://biletul-zilei.net
  comment_content: I think that is very hard to optimize your site for IE6 and i don't
    think that it worths it.
  comment_date: '2009-08-29 14:54:22'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32948'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Alex: Ah, an adblocker :) Regarding max/min-width/height: if
    you need it for IE6 you can easily use <a href="http://robertnyman.com/2007/11/13/stop-using-poor-performance-css-expressions-use-javascript-instead/"
    rel="nofollow">regular javascript</a> to do exactly the same thing, just with
    less resources.'
  comment_date: '2009-08-30 00:58:28'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '1'
- comment_ID: '32954'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: '@Emil, i guess i have to change all the expressions that i''ve
    used till now. \n\nAnyway, i''m thinking that it should look good if i use your
    "<a href="http://friendlybit.com/browsers/motivation-for-building-for-ie6/" rel="nofollow">8
    years old browser alert</a>" and urge all those who use IE6 to upgrade as soon
    as possible.'
  comment_date: '2009-08-30 18:33:57'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32961'
  comment_author: Jeff Seager
  comment_author_url: http://peregrineproject.com
  comment_content: Tough question, Emil. I think a positive statement is almost always
    better than a negative one. What do you think about <strong>briefly</strong> noting
    the advantages of viewing your site with a modern standards-compliant browser
    (IE7 or higher, Opera 7 or highter, Firefox 2 or higher ... etc.) -- then linking
    to <a href="http://www.webstandards.org/" rel="nofollow">The Web Standards Project</a>
    or something like that?\n\nI wouldn't want to do that with a pop-up window. Maybe
    with something like we now use with the <code>noscript</code> tag that alerts
    people to enhancements only available with javascript enabled. Using javascript
    or another method, you could detect IE6 users and deliver that message only to
    them.\n\nIn the end, I think the only way to choke out bad practices is to practice
    doing it right. We cannot insist that people upgrade their browser, but it's good
    to point out how upgrading will benefit them.
  comment_date: '2009-08-31 19:38:02'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32970'
  comment_author: Jan Willem
  comment_author_url: http://members.casema.nl/jwnieuwerth/
  comment_content: I agree with you, especially not supporting these PNG. I use it
    in my menu. Altough I still write separate CSS files for IE 6, because it's still
    used by enough 13.6% off all browsers (according to w3schools.com statistics.\n\nEn
    yes, I thinks IT fokes are lazy, lately we got new updates on every department
    and I remember the last programm became suitable for Explorer 8, so all programms
    are ready for browser update. Still they didn't update the browser, still they
    didn't give me a good reason why they didn't. Perhaps because I'm the only complaining
    about this. I don't understand my collegue, they all got newer browsers at home!\n\nI
    have a support section in home some time which gives a message if people use IE
    6. I think everyone should do this. It's time to move on, the only thing which
    should be done is install the new browser and if necessary (mostly even not) implement
    online programms.
  comment_date: '2009-09-02 23:52:02'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32971'
  comment_author: Jan Willem
  comment_author_url: http://members.casema.nl/jwnieuwerth/
  comment_content: 'Oh, I forgot: great list, Emil!'
  comment_date: '2009-09-02 23:54:35'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '32978'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: I found out a nice free tool to test your website compatibily with
    all IE versions. It has no adware/malware/spyware and it's a very usefull tool
    for a webdesigner.\n\nhttp://www.my-debugbar.com/wiki/IETester/HomePage
  comment_date: '2009-09-07 07:14:14'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '33002'
  comment_author: terry
  comment_author_url: http://www.download4a.com
  comment_content: ie6 support till 2014 ? microsoft fails again :((\n@Alex - you
    can try http://browsershots.org/ to check various browser compatibility
  comment_date: '2009-09-13 20:18:26'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '33008'
  comment_author: Jim Westergren
  comment_author_url: http://www.jimwestergren.com
  comment_content: Hi Emil,\n\nFrom your third link I found http://www.ie6nomore.com/code-samples.html
    which I saved for later use - I think it is great.\n\nWhat about floating anchors
    on inline lists? Isn't that a bug in IE6? Maybe I don't know the exact bug but
    I always have a headache writing the CSS for an ul element that is the nav menu.
  comment_date: '2009-09-17 18:06:54'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '33010'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: '@Terry - your solution for checking browser compatibility is great
    but very time consuming. If you want to test only IE and you want to do it fast
    like you had that browser installed on your operating system, you can use the
    tool that i wrote about in my last post.'
  comment_date: '2009-09-18 07:33:31'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '33013'
  comment_author: Cody
  comment_author_url: http://www.webhostdesignpost.com/webdesign/
  comment_content: Wow IE6 until 2014 - Ouch!\n\nEither way I think I'll be most excited
    not to worry about PNG transparency and the min and max heights and widths.\n\nI
    seen some people looking for options to test IE.  This is what I use if anyone
    is interested.\n\nwww.my-debugbar.com/wiki/IETester/HomePage
  comment_date: '2009-09-18 20:12:38'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '33111'
  comment_author: maxpagels.com
  comment_author_url: http://www.maxpagels.com/2009/10/09/454/
  comment_content: '[...] always interesting Friendly Bit blog has a list of techniques
    that don&#8217;t work in Internet Explorer 6 but do in IE7. Included in the post&#8217;s
    comments is a link to &#8220;When can I use&#8230;&#8221; a site that [...]'
  comment_date: '2009-10-09 11:16:38'
  comment_post_ID: '496'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33115'
  comment_author: Alex
  comment_author_url: ''
  comment_content: Have you seen that youtube have stopped supporting IE 6?
  comment_date: '2009-10-10 19:18:03'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '33435'
  comment_author: Randy Comeau
  comment_author_url: ''
  comment_content: Agreed, IE is dead.  IE in general... Why doesn't MS just lay down
    and die!
  comment_date: '2010-02-11 02:35:30'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '33509'
  comment_author: Sean
  comment_author_url: http://www.seangw.com/wordpress/
  comment_content: I can say I'm looking forward to PNG being fully viable, and the
    use of multiple class selectors (although the additional  selector pool may be
    enough once I can use some more CSS elements -- I love :first-child and :last-child).
    \n\nIE6 is the browser that just won't die.
  comment_date: '2010-04-26 14:29:12'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '33913'
  comment_author: JP
  comment_author_url: ''
  comment_content: IMO, IE will continue to survive because they bundle it with windowz
    :)
  comment_date: '2010-06-10 18:14:52'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '33933'
  comment_author: Vanessa
  comment_author_url: ''
  comment_content: Wow IE6 until 2014 - Ouch!Either way I think I'll be most excited
    not to worry about PNG transparency and the min and max heights and widths.I seen
    some people looking for options to test IE.  This is what I use if anyone is interested.www.my-debugbar.com/wiki/IETester/HomePage
  comment_date: '2010-06-21 15:41:42'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '34009'
  comment_author: tswaters
  comment_author_url: ''
  comment_content: 'I think the best possible way to deal with old browsers is to
    not apply any hacks and let the layout break. Don''t waste time testing sites
    in a wide variety of older browsers, just assume they''ll fail and let them.  \n\nIf
    users of ancient browsers navigate around the internet and see that everything
    still works -- they will assume there is nothing wrong with their browsing experience.  If
    every third page they see is broken, they might just get a clue -- and that''s
    better than a push from Microsoft, IMO. \n\nThen again, I should say I don''t
    have customers, per say, visiting my web sites -- optimizing a site for a mass
    number of computer configurations isn''t exactly a priority of mine.  This is
    all anyone sees when they visit my site on an older browser:  "Your browser is
    not future friendly. Upgrading as soon as possible will bring you a better internet
    experience, I promise."'
  comment_date: '2010-08-05 03:17:19'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
- comment_ID: '36718'
  comment_author: jb007
  comment_author_url: ''
  comment_content: Really, your article is super. thanks.....
  comment_date: '2011-01-24 11:32:00'
  comment_post_ID: '496'
  comment_type: null
  is_admin: '0'
---
