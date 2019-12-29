---
comments:
- comment_ID: '33556'
  comment_author: Dean Higginbotham
  comment_author_url: ''
  comment_content: What an awesome writeup! Really good info and I love the break-down
    comparisons and proofs.\n\nTotally bookmarking this to give it a thorough read-through!
    I've been looking for this info for a long time and everywhere else it's a mish-mash
    of "do this!", "no, do this!", "no, this is the right way!", etc...
  comment_date: '2010-05-08 02:59:32'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33577'
  comment_author: Morgan Cheng
  comment_author_url: http://www.morgancheng.com
  comment_content: Nice article!\n\nIn my experience, since jQuery is used, most actions
    can be done at 'DomContentLoaded' event instead of 'load' event. So, it really
    doesn't matter async loaded javscript delay 'load' event. Is there any specific
    requirement that the javascript should not delay 'load'?
  comment_date: '2010-05-08 06:23:54'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33606'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '<strong>Update</strong>: Switched to using <a href="http://www.slideshare.net/souders/jsconf-us-2010/13"
    rel="nofollow">insertBefore instead of appendChild</a> in all script due to a
    IE6 bug with unclosed tags in the head. Thanks <a href="http://fleecelabs.se/"
    rel="nofollow">Peter Lindberg</a>!'
  comment_date: '2010-05-08 10:17:40'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '33607'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Dean: Glad you like it, that''s why I keep writing :)\n\n@Morgan:
    I have no idea what techniques my customers are using, so I don''t know if they
    use jQuery, prototype or just native javascripts relying on the onloaded event.
    Would be great if I knew that all of them used a library that triggered their
    scripts on domcontentloaded, but I can''t know that for sure.'
  comment_date: '2010-05-08 10:20:21'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '33617'
  comment_author: jarvklo
  comment_author_url: http://jarvklo.se
  comment_content: Awesome.\nThanks for sharing!
  comment_date: '2010-05-08 11:53:46'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33618'
  comment_author: Kristoffer Nolgren
  comment_author_url: http://resihop.nu
  comment_content: Jaha, är du med och bygger den, vi använder den på resihop,nu och
    är galet nöjda! (i alla fall jag, min optimeringshysteriska kollega hade gärna
    haft något som laddade snabbare och vill bygga nått själv, men designen och hastigheten
    är grym)
  comment_date: '2010-05-08 11:59:47'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33621'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@jarvklo: Thanks for reading!\n\n@Kristoffer: Som du märker så
    jobbar vi hårt på att få upp hastigheten :) Det kommer mera framöver!'
  comment_date: '2010-05-08 12:08:30'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '33627'
  comment_author: Kristoffer Nolgren
  comment_author_url: http://resihop.nu
  comment_content: Ja, den är ju grymt snabb redan nu!\n\nEn tanke jag haft, som ni
    kanske också har övervägt är att erbjuda en serverside-lösning, i alla fall för
    själva knappen, som ju är vad de allra flesta av användarna upplever. \n\nEgentligen
    är det kanske inte så jättemycket som ni faktiskt behöver koda, bara att erkänna
    det som "good practice" att inte ladda knappen via javascriptet. Vi har valt att
    inte göra det för att undvika att nått pajjar vid uppdateringar och så.
  comment_date: '2010-05-08 12:54:38'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33661'
  comment_author: Mathias
  comment_author_url: http://mathiasbynens.be/
  comment_content: 'Nice write-up!\n\n<blockquote><strong>Small.</strong> I don’t
    want a big mess for them to include on their sites. 10-15 lines, tops.</blockquote>\n\nWell,
    you could optimize this snippet even more if you wanted to. For example, why are
    you setting <code>s.type = ''text/javascript'';</code>? It’s completely unnecessary.
    You could also cache the string <code>''script''</code> and a store a reference
    to <code>document</code> in a variable, and re-use those to save even more bytes.
    (This is exactly what’s going on in <a href="http://mathiasbynens.be/notes/async-analytics-snippet"
    title="Optimizing the asynchronous Google Analytics snippet" rel="nofollow">my
    optimized asynchronous Google Analytics snippet</a>.)\n\nAlso, if you don''t want
    to pollute the global namespace, you should probably prepend <code>x = document.getElementsByTagName(''script'')[0];</code>
    with <code>var</code>.\n\nThe <code>if</code> check at the end can be rewritten
    as follows:\n\n<code>window.attachEvent ? window.attachEvent(''onload'', async_load)
    : window.addEventListener(''load'', async_load, false);</code>'
  comment_date: '2010-05-08 15:25:19'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33674'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Mathias: That''s a great article, thanks! When I said short,
    I really meant "not too long", which I think my final snippet fulfills. I think
    people wanting to optimize even more will use your hints to do it. Thanks!'
  comment_date: '2010-05-08 16:46:31'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '33675'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Kristoffer: Customers are free to host the button on their own
    sites if they want to, but we have avoided this to keep the number of steps needed
    to get started with kundo to a minimum. We''ll see what happens in the future.'
  comment_date: '2010-05-08 16:48:15'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '33719'
  comment_author: Roland Bouman
  comment_author_url: http://rpbouman.blogspot.com/
  comment_content: Really, really useful info, and marvelously written. Kudos! \n\nthanks
    for sharing :)\n\nRoland.
  comment_date: '2010-05-08 23:23:38'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33751'
  comment_author: Aki Kärkkäinen
  comment_author_url: http://www.akikoo.org
  comment_content: Good stuff! Just finished reading Steve Souders' book Even Faster
    Web Sites so your article will come in handy. Nice to have weapons and tools in
    the current "browser speed war" ;) It seems that it's all about fast loading time
    nowadays (which is good for users and everybody of course!).
  comment_date: '2010-05-09 14:47:32'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33756'
  comment_author: Wayne State Web Communications Blog &raquo; Blog Archive &raquo;
    [Friday Links] The Monday Edition
  comment_author_url: http://wcs.wayne.edu/blog/2010/05/10/friday-links-the-monday-edition/
  comment_content: '[...] Lazy Loading Asyncronous Javascript – Friendly Bit [...]'
  comment_date: '2010-05-10 15:43:19'
  comment_post_ID: '613'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33757'
  comment_author: Bryan
  comment_author_url: http://www.urgack.com
  comment_content: When you declare <code>x</code> without the <code>var</code> keyword,
    does that not expose it to any external methods? I thought that you needed to
    use <code>var</code> to keep the scope local to that function.
  comment_date: '2010-05-10 16:59:43'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33758'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Bryan: Of course, my fault. I''ve updated the code with a "var"
    in front of the x variable. Thanks!'
  comment_date: '2010-05-10 17:30:57'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '33828'
  comment_author: Rizo
  comment_author_url: http://www.from-rizo.se
  comment_content: Really good writeup Emil. Simple, yet great :)
  comment_date: '2010-05-12 15:42:13'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33830'
  comment_author: Robin Jakobsson
  comment_author_url: http://robinjakobsson.se/blog
  comment_content: Great article Emil!\nValuable lessons,\nthanks!
  comment_date: '2010-05-13 09:13:59'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33838'
  comment_author: Wayne State Web Communications Blog &raquo; Blog Archive &raquo;
    [Friday Links] The Startup Weekend Edition
  comment_author_url: http://wcs.wayne.edu/blog/2010/05/14/friday-links-the-startup-weekend-edition/
  comment_content: '[...] Lazy Loading Asyncronous Javascript [...]'
  comment_date: '2010-05-14 16:02:35'
  comment_post_ID: '613'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33858'
  comment_author: CodeMyConcept
  comment_author_url: http://www.codemyconcept.com
  comment_content: You did a great sum up of the regular issues. This article is being
    bookmarked right now!\nThank you!
  comment_date: '2010-05-24 23:09:00'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33861'
  comment_author: Linus G Thiel
  comment_author_url: http://hanssonlarsson.se/
  comment_content: Great solution, Emil. I will definitely be using this. Thanks for
    the linkback, even though I weren't of much help!
  comment_date: '2010-05-25 09:48:37'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33862'
  comment_author: Stephan Schubert
  comment_author_url: http://www.familie-gutschein.de
  comment_content: 'Nice writeup how it works - here''s a jQuery version for the Google
    Analytics snippet: http://gist.github.com/361051'
  comment_date: '2010-05-25 10:23:53'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33870'
  comment_author: Josh
  comment_author_url: http://www.snapbill.com
  comment_content: With the final piece of code you might want to remove the 's.async
    = true;' line? It seems a little irrelevant if the code is only added after onLoad.
  comment_date: '2010-05-25 11:59:52'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33873'
  comment_author: Riyad Kalla
  comment_author_url: ''
  comment_content: Stenström,\n\nBrilliant writeup. I didn't expect you to walk through
    all past-and-present options for async loading... this is going in my JS quick-reference
    toolbox of bookmarks. Bravo dude.
  comment_date: '2010-05-25 14:42:35'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33882'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Josh: Good question, and I thought about that too. Thing is,
    there could be more than one script triggering on onload, and I would hate this
    script to block the other ones. That''s the reason it''s still there.'
  comment_date: '2010-05-26 10:25:38'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '33907'
  comment_author: Steve
  comment_author_url: http://www.technewsblog.co.uk
  comment_content: Very informative post.\n\nI've never thought about loading external
    scripts much, I am just getting in to Javascript and this has helped me out lots.\n\nThanks
    :)
  comment_date: '2010-06-07 16:03:57'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33918'
  comment_author: Ashish
  comment_author_url: http://www.simransoftwaresolutions.com
  comment_content: Hey,\n\nIt's nice post, We have already tried this in few of our
    website projects and it works flawless.\n\nThanks :-)
  comment_date: '2010-06-11 15:35:05'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33919'
  comment_author: Roi
  comment_author_url: ''
  comment_content: Great post.\n\nThank you!
  comment_date: '2010-06-14 11:51:05'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '33931'
  comment_author: onequad
  comment_author_url: http://ball.in.th
  comment_content: Thanks for sharing! I've looking for a way to do just this. I've
    tried loading  http://tracker.stats.in.th/tracker.php?uid=18244 but it didn't
    work. I am guessing that the external script has document.write and  that messes
    things up. Is there a work around for this?
  comment_date: '2010-06-20 16:40:40'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34047'
  comment_author: Steve Souders
  comment_author_url: http://stevesouders.com/
  comment_content: Great article! A few comments:\n\nUnder Script Tag you have script
    type="", but I think you mean script src="".\n\nAsync Pattern (dynamically added
    SCRIPT element) is rejected because it blocks the onload event. Although this
    is true in Firefox, Chrome, and Safari, it's not true in IE and Opera. Also, I
    haven't tested this recently with growing support for the SCRIPT ASYNC attribute
    (altho the HTML5 spec says onload should be blocked, so I'm not optimistic). \n\nCertainly
    waiting until after the load event has fired avoids blocking the page, but if
    a widget's content is valuable to the page it's important to load earlier. Note
    that 5-15% of pages don't reach the load event - users click through before that
    happens.
  comment_date: '2010-08-31 18:53:26'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34048'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Steve Souders: Thanks for you comment. I''ve fixed the first
    issue, and added a clarification about blocking.\n\nAbout onload: Yeah, it''s
    unfortunate to have to wait that long. As a supplier of an external service, we
    feel that the customers own site always have to be prioritized above our script.
    So blocking their onload event is not something that we think is acceptable.\n\nI
    can only wish that all ad suppliers did that same.'
  comment_date: '2010-09-01 00:08:59'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '34049'
  comment_author: Aaron Peters
  comment_author_url: http://www.aaronpeters.nl/en/
  comment_content: Great article!\n\nHave you considered dynamically creating an iframe?\nI
    know the Meebo guys went down this path and are very happy with the result, although
    it wasn't easy to get this to work cross-browser.\nhttp://blog.meebo.com/?p=2633
  comment_date: '2010-09-01 10:07:01'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34052'
  comment_author: Gavin
  comment_author_url: http://gavtaylor.co.uk
  comment_content: a great article, and great solution to a common problem.\nthe perfect
    way to include 3rd party code without affecting page load
  comment_date: '2010-09-02 10:58:53'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34062'
  comment_author: Martin
  comment_author_url: ''
  comment_content: Nice job! \n\nI'm using the Async pattern but I'd changed the closure
    statment by a setTimeout call. It's working perfect on IE and Opera.
  comment_date: '2010-09-07 21:10:16'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34065'
  comment_author: Enrico
  comment_author_url: ''
  comment_content: 'Nice article, helped me a lot. \nBut I encounter a problem with
    browser caching and the version with the onload event. The browser does then no
    longer recognize any changes in the loaded javascript. \nI also opened a question
    at stackoverflow: \nhttp://stackoverflow.com/questions/3674830/caching-problem-with-asynchronous-javascript-loading-with-onload-event\n\nMaybe
    somebody knows a solution to this?'
  comment_date: '2010-09-09 10:22:35'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34066'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Enrico: Thanks! I replied to your question on StackOverflow,
    hope it helped.'
  comment_date: '2010-09-09 13:05:29'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '34067'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Martin: Good idea. Does files loaded that way block other downloads?'
  comment_date: '2010-09-09 17:14:32'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '34068'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Aaron: No, I haven''t, sounds lite an interesting article, thanks
    for the tip!'
  comment_date: '2010-09-09 17:16:44'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '34094'
  comment_author: Alexander
  comment_author_url: http://alexsorokin.ru/
  comment_content: Thank you for such a great explanation! saved my time
  comment_date: '2010-09-18 18:55:01'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34095'
  comment_author: ??????????? ???????? ???????? ? HTML ???????? &laquo; ?????????
  comment_author_url: http://alexsorokin.ru/2010/09/javascript-async-load/
  comment_content: '[...] http://friendlybit.com/js/lazy-loading-asyncronous-javascript/
    [...]'
  comment_date: '2010-09-18 19:18:31'
  comment_post_ID: '613'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '34097'
  comment_author: Nicolas
  comment_author_url: http://www.nicolas-chevallier.fr/
  comment_content: Thanks for this study, I love to read new articles about web performance
    :)
  comment_date: '2010-09-18 20:52:45'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34105'
  comment_author: Damien P.
  comment_author_url: http://www.damienpetitjean.fr
  comment_content: I knew loading asyncronous javascript was difficult but i never
    thought someone could do it as easy as this. Thanks !
  comment_date: '2010-09-23 16:37:20'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34304'
  comment_author: G
  comment_author_url: ''
  comment_content: Thanks for the great write-up Emil.\n\nCan you elaborate a bit
    on what the best-practices are for the script that gets inserted (http://yourdomain.com/script.js
    in your example code).\n\nWhat should be in there? I tried to look into your http://static.kundo.se/embed.js
    code but that is minified.\n\nThanks in advance!
  comment_date: '2010-11-04 18:03:20'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34328'
  comment_author: Peter
  comment_author_url: ''
  comment_content: Wow, great article Emil! I am building a website which loads a
    lot of scripts (jQuery, Cycle, Hyphenator, Highslide, SWFObject, GA, etc) so I
    need good asynchronous loading!\n\nI have one question. Is it possible to have
    fallback scripts for when a external script fails to load? For example, I would
    like to use Google's version of jQuery since that will already be cached by many
    users, but I need a local fallback version in case Google is not available (Google
    is blocked in several countries). However, how do I check if an asynchronous scripts
    is properly loaded?\n\nThanks anyway for the great explanation!
  comment_date: '2010-11-09 17:40:17'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
- comment_ID: '34330'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: 'Hi Peter,\n\nWhat most people do it first try to load the jQuery
    script, and then check if the global object "jQuery" is defined, otherwise load
    it another way. Here''s a thread from StackOverflow with lots of good answers:
    <a href="http://stackoverflow.com/questions/1014203/" rel="nofollow">http://stackoverflow.com/questions/1014203/</a>'
  comment_date: '2010-11-09 23:33:39'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '1'
- comment_ID: '36752'
  comment_author: DealsKing
  comment_author_url: ''
  comment_content: You should check out the optimized GA snippet from HTML5 Boilerplate,
    it's even more minimal :)
  comment_date: '2011-02-24 15:58:00'
  comment_post_ID: '613'
  comment_type: null
  is_admin: '0'
---