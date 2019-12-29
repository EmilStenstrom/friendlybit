---
comments:
- comment_ID: '24730'
  comment_author: Martin Jansson
  comment_author_url: http://marja.se
  comment_content: Nice template, it's tricky to get it right sometimes. \n\nMay I
    suggest a fallback width for IE?  Expressions are dependent on javascript to work,
    and if the user has scripting turned of, the width of the element will be 100%
    no matter what the width of the browser window is, which may cause very long lines.\n\nThe
    fix is to have a width-declaration of, say, 960px for this example, before the
    width-declaration containing the expression.
  comment_date: '2007-05-28 22:03:20'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '24731'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Martin: Great addition, added it to the sample.'
  comment_date: '2007-05-28 22:13:34'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '1'
- comment_ID: '24742'
  comment_author: Matthijs
  comment_author_url: http://www.sitestone.nl
  comment_content: Emil, you might want to adjust the expression a bit to prevent
    a nasty bug in IE. It freezes up when resizing the window if you use the expression
    you described. See <a href="http://www.cameronmoll.com/archives/000892.html "
    rel="nofollow">this post</a> on Cameron's site. I encounterd this bug once and
    it's definitely a bad bug..\nKeep up the good work.
  comment_date: '2007-05-29 06:30:52'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '24745'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Matthijs: Another healthy fix, thanks! (I''ve never encountered
    the freeze but I trust you that it can happen in some instances). Added it to
    the template.'
  comment_date: '2007-05-29 07:22:16'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '1'
- comment_ID: '24756'
  comment_author: Jens Wedin
  comment_author_url: http://jedisthlm.com
  comment_content: What is the difference with this script and the one on:\n\n<a href="http://doxdesk.com/software/js/minmax.html"
    rel="nofollow">http://doxdesk.com/software/js/minmax.html</a>
  comment_date: '2007-05-29 13:00:04'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '24763'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jens: well, this one is shorter :) That one does a lot of other
    stuff that you don''t really need. It enables support for max-height among others...'
  comment_date: '2007-05-29 15:37:38'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '1'
- comment_ID: '24799'
  comment_author: Jens Wedin
  comment_author_url: http://jedisthlm.com
  comment_content: Thanks, shorter is better, right?
  comment_date: '2007-05-30 08:21:38'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '24826'
  comment_author: lewis
  comment_author_url: http://www.ldexterldesign.co.uk/
  comment_content: having moved from a 19"  to a 22" monitor in the past few weeks
    not only has it provoked a re-evaluation of how i view the web but i've developed
    a habit for browsing in vertically tiled windows (two pages/sites side by side).
    don't ask me why when you can use tabs, but nevertheless...\n\nthis raises the
    question of designing (reverting for some who design at 1024x minimum) in 800x
    wrappers again. where once i would find an 800x width too small i now embrace
    it.\n\nregardless, it does re-emphasize the importance of liquid layouts. this
    issue is something i'm going to enjoy pondering at some point this summer.\n\ncheers
    for highlighting it emil.
  comment_date: '2007-05-31 05:00:48'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '25000'
  comment_author: Kevin Moore
  comment_author_url: ''
  comment_content: This is a very good suggestion, particularly on the max-width end.
    My only concern about min-width is that more people are browsing with their cell
    phones and other hand-held devices that have much smaller screens. Also, users
    tend to disable javascript to minimize downloading time. Setting a minimum width
    could create access problems for them.
  comment_date: '2007-06-06 05:02:28'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '25020'
  comment_author: Jeena Paradies
  comment_author_url: http://jeenaparadies.net
  comment_content: 'Hi,\n\nThere is a problem with IE 6 in standard compilant mode,
    it uses an other method to get the width than all other IEs. Therefore I developed
    this version:\n\n* html #foo {\n width: 995px;\n width: expression(\n  (document.documentElement
    &amp;&amp; document.documentElement.clientHeight) ?\n   (document.documentElement.clientWidth
    &gt; 1265 ) ? "1265px" : "auto") :\n   (document.body.clientWidth &gt; 1265 )
    ? "1265px" : "auto")\n );\n}'
  comment_date: '2007-06-06 18:31:55'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '25022'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Kevin Moore: My suggestion for that problem is to have a handheld
    CSS that changes the layout to something that works on mobile phones.'
  comment_date: '2007-06-06 19:47:24'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '1'
- comment_ID: '25023'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jeena: The code I posted works on IE6 in standards mode so I''m
    not sure how your code fixes anything? I always develop in standards mode, so
    I don''t need fallback in quirks. Other than that your code does exactly the same
    as the one posted.'
  comment_date: '2007-06-06 19:51:47'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '1'
- comment_ID: '25090'
  comment_author: Jeena Paradies
  comment_author_url: http://jeenaparadies.net
  comment_content: 'Hej Emil,\n\nThere is no document.documentElement.clientWidth
    in IE 5.x, but there is document.body.clientWidth. The problem: IE6 frezes with
    document.body.clientWidth in standard compilant mode.\n\nSorry I was a little
    bit confused when I wrote ma last comment :-D'
  comment_date: '2007-06-09 20:29:12'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '25161'
  comment_author: jonny_noog
  comment_author_url: ''
  comment_content: Hi Emil,\n\nThe problem I have found recently with quite a number
    of hand-held devices is that they are not picking up on hand-held stylesheets.
    Sadly it seems that many manufacturers are either unaware of this feature, or
    do not wish to implement it. :(
  comment_date: '2007-06-11 23:52:06'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '25891'
  comment_author: Kravvitz
  comment_author_url: http://www.dynamicsitesolutions.com/
  comment_content: Setting a width triggers hasLayout, so using height:1% is unnecessary
    here.
  comment_date: '2007-07-03 22:45:52'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '31394'
  comment_author: Rick
  comment_author_url: http://www.lincolnavenuewillowglen.com
  comment_content: 'Hi,\n\nWhat happened to:\n   min-width: 760px;\n   max-width:
    960px;\n   width: 100%;\nShown in the 1st example, that is not included in the
    2nd example (the one for the IE6 fix)?\nShould it be included?\nIf so, where?\nThanks
    :)'
  comment_date: '2009-01-25 19:10:10'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '31397'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rick: See the example in the end, it includes everything you
    need. You can test that page in multiple browsers to confirm that it does if you
    want to.'
  comment_date: '2009-01-26 00:07:57'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '1'
- comment_ID: '31401'
  comment_author: Rick
  comment_author_url: ''
  comment_content: Hey Emil,\n\nThanks much for answering this so quickly (esp. since
    the\nlast post here was 1.5 years ago!).\nI just totally missed that link.\n\nYour
    solution worked wonderfully, and I sincerely appreciate it! :)\n\nRick
  comment_date: '2009-01-26 15:26:37'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
- comment_ID: '33154'
  comment_author: IT???? | IE6???CSS???????????????????
  comment_author_url: http://smkn.xsrv.jp/blog/2009/10/hack-for-some-ie6-bugs/
  comment_content: '[...] Min-width and Max-width template – Friendly Bit [...]'
  comment_date: '2009-10-28 02:55:25'
  comment_post_ID: '126'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33161'
  comment_author: Alex
  comment_author_url: http://www.webdesign-villingen.de/
  comment_content: And this works? I mean JavaScript inside CSS, what says the W3C-Validator
    for stylesheet, is that solution CSS 2.1 valid?
  comment_date: '2009-11-03 23:03:35'
  comment_post_ID: '126'
  comment_type: null
  is_admin: '0'
---