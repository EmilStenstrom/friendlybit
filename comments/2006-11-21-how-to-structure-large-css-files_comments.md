---
comments:
- comment_ID: '7589'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: A note, this site does not use this method (yet). If you want to
    see it in action, have a look at the <a href="http://www.kth.se" rel="nofollow">KTH
    site</a> I coded earlier this year. Since it's a real world project it isn't perfect,
    but it should give you an idea of how the method works.
  comment_date: '2006-11-21 22:10:39'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '7594'
  comment_author: Christian Tietze
  comment_author_url: ''
  comment_content: 'I structure the CSS this way:\n\nFirst I add all usual markup.
    Like removing margin and padding from all elements, removing borders from images
    and so on. Standard indentations for lists are (re-)set here as well.\n\nSecond,
    there are all the layout-relevant divs (#content, #menu), ordered by appearance
    on screen, so header comes before content etc.\n\nThird there ist the content
    markup. I may repeat #content itself, but this time it''d be for some standard
    styling. Ordinarily, I just put all the <code>#content p em</code>-like stuff
    in this second part of the code. The headings first, then paragraphs, lists etc.,
    then some special containers like the options for blogposts which show the amount
    of comments, or the author or so.\n\nYour method sounds nice as well. But what''s
    with large documents? I think it''s hard to indent nested layouts very well. If
    the layout is centered, split and whatnot, you got two or three levels for nothing
    but a div at the beginning.\nBut the structure sounds like it''s maing sense.\n\nSo,
    what do you suggest for the CSS markup "content"? \nDo you put float, margin,
    width etc. above font and border?'
  comment_date: '2006-11-21 23:08:48'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7599'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Christian Tietze: Interesting to hear! You probably have to give
    me that explanation in a comment for me to understand it :)\n\nI don''t think
    large documents is such a big issue. Selectors are a small part of the code, the
    declarations take much more space. As for wrapper divs I don''t indent them, like
    you say it feels like a mess, and it won''t confuse anyone that I don''t.\n\nMy
    suggestions for declarations are at the bottom :) one per line and in alphabetic
    order.'
  comment_date: '2006-11-22 00:29:27'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '7607'
  comment_author: Kalle
  comment_author_url: ''
  comment_content: Interesting article! I also want to keep my CSS as tidy as possible
    and I'm following most of the methods you mention here, except for the alphabetic
    and indent methods which are really interesting by the way. I'm gonna try those
    at work tomorrow and see if it helps me.
  comment_date: '2006-11-22 01:33:25'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7609'
  comment_author: Antti Kupila
  comment_author_url: http://www.anttikupila.com
  comment_content: Interesting indeed. I however don't really see the point with using
    "the whole path", since it adds to the document size and doesn't really give anything.
    I think a well structured (sematically ordered and correctly indented) document
    gives you enough info. Of course it's a bit easier to read (especially for somebody
    who isn't the original author), but with larger documents it can easily add up.\nOther
    than that i agree with everything you're saying and actually do most of my css
    the same way. \nA new idea was to order the properties alphabetically. Could give
    it a try :)
  comment_date: '2006-11-22 02:11:10'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7614'
  comment_author: Rowan Lewis
  comment_author_url: http://pixelcarnage.net/
  comment_content: I'm a freak:\nhttp://pixelcarnage.net/Projects/OneCommune/003/HTML/Styles/Global.css\nhttp://pixelcarnage.net/Projects/OneCommune/003/HTML/Styles/Screen.css\n\nI'm
    sure those two files will scare someone...
  comment_date: '2006-11-22 02:44:01'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7654'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: I agree with everything except "full path" selectors and alphabetic
    ordered declarations. Since the rules are indented you can tell where things belong
    anyway, and keeping selectors short and simple is good for performance (for what
    it's worth).\n\nI don't bother writing the declarations alphabetically. I usually
    don't have a problem finding a specific declaration. Sorting them is extra work
    with little benefit.
  comment_date: '2006-11-22 12:40:21'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7668'
  comment_author: Christian Tietze
  comment_author_url: ''
  comment_content: '@Rowan Lewis: I personally enjoyed reading our Screen.css. My
    CSS files look even worse. Indentation seems to clear things up a bit. Or probably
    your CSS code is just too simple :D\n\n@Emil: What exactly do you want me to explain?'
  comment_date: '2006-11-22 20:39:53'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7675'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Kalle: good to hear, seems people are already using parts of
    the method.\n\n@Antti Kupila, zcorpan: full paths is really the most important
    of them. With large files you need to read 100 lines up to find the top parent
    to a rule. If you include the full path that info is on the same line. I find
    that I scroll back and fourth *a lot* less when using when using them. \n\n@Rowan:
    Nice! I''m just missing the full paths :)\n\n@Christian Tietze: I just mean that
    what you wrote in the comment here probably is needed in a commented section in
    the beginning of your CSS-file. I need to try and just give one of my files to
    see if they can handle it without instructions. I hope so!'
  comment_date: '2006-11-23 00:27:26'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '7715'
  comment_author: 'links for 2006-11-23 &laquo; mayvelous : m-a-e-e'
  comment_author_url: http://mayvelous.wordpress.com/2006/11/23/links-for-2006-11-23/
  comment_content: '[...] How to structure large CSS files - Friendly Bit (tags: CSS
    structure webdev webdesign tips techniques) [...]'
  comment_date: '2006-11-23 12:22:31'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '7725'
  comment_author: Jens Wedin
  comment_author_url: http://jedisthlm.com
  comment_content: This is how we did it for a large project for Nordea. It's a mix
    of what you write about.\n\nhttp://www.nordea.se/sitemod/upload/Root/eGuidelines/stylesheets/screen_common.css
  comment_date: '2006-11-23 16:35:06'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7749'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jens Wedin: Cool, although it doesn''t follow any of the five
    points I wrote about in the article, so I''m not sure how it''s a mix :)\n\nI''m
    sure yours works too though :)'
  comment_date: '2006-11-24 01:26:40'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '7780'
  comment_author: Rob Schlüter
  comment_author_url: http://kwebble.com/
  comment_content: 'The order for CSS rules is roughly what Christian Tietze wrote:
    generic parts, single HTML selectors, layout divs and specific content. I like
    to set up the CSS so that identical styles are only defined once, like normalizing
    database tables. This may mean the order may need to differ. \n\nProperty order
    is positioning, display, color, specific stuff (list properties, table rules),
    font and ends with box properties from the inside out: padding, border and margin.\n\nI
    recently changed from writing every property on it''s own line to combining them
    all on one line with the selector. I find that this gives me a better overview
    over the used selectors.\n\nTo overrule some CSS on specific templates you can
    also include a second CSS file, called the same as the template it belongs to
    and override styles there.'
  comment_date: '2006-11-24 16:51:56'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7823'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rob Schlüter: The problem with all advanced schemes like that
    is that they differ between developers. So when you open up a CSS file made by
    someone else you are utterly confused.\n\nI prefer to keep it simple.'
  comment_date: '2006-11-25 15:21:14'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '7825'
  comment_author: Philip Karpiak
  comment_author_url: http://eswat.ca
  comment_content: Great write-up. I write my code in a similar fashion, but without
    the indentation and alphabetical sorting. But I go one step further with ordering
    selectors by making comment headers to separate them. Probably overkill since
    it's already easy to recognize a block of selectors. But I find it useful if I
    need to scan a file quickly.
  comment_date: '2006-11-25 19:38:36'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7830'
  comment_author: John
  comment_author_url: ''
  comment_content: It's great that the css for this page is such a mess.
  comment_date: '2006-11-25 21:10:56'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7831'
  comment_author: John
  comment_author_url: ''
  comment_content: The nordea.se css is very impressive though
  comment_date: '2006-11-25 21:13:00'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7832'
  comment_author: Steve Streza
  comment_author_url: http://www.tubularapp.com
  comment_content: The alternative is using a tool for CSS power editors.  On Mac,
    there's <a href="http://macrabbit.com" rel="nofollow">CSSEdit</a>.
  comment_date: '2006-11-25 21:16:14'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7833'
  comment_author: Seamus
  comment_author_url: http://moronicbajebus.com
  comment_content: For the past month at work we have been developing conventions
    for our CSS.  An idea we are using, which would extend your idea of ordering the
    selectors the same as the HTML, is to use @import to  split the out major layout
    sections into their own files. For example, we have a stylesheet for the header,
    content, sidebar, and footer. Besides the benefit of finding rules easier, it
    also allows multiple people to work on different parts of the layout without stepping
    on each others toes.
  comment_date: '2006-11-25 21:27:25'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7835'
  comment_author: Paul
  comment_author_url: http://www.iheartthat.com/
  comment_content: I have considered every one of your statements in the past. I have
    explored the potential of each rule, except the most obvious -- alphabetize the
    declarations.  Your argument works for me, that blocks contain at most 10 declarations.  I
    used that argument to keep them out of order in favor of importance.  After writing
    tens of stylesheets, alphabetical just makes more sense.\n\nNow that you've put
    these rules in print, I think it's time I follow them rigorously.  Thanks for
    the post.
  comment_date: '2006-11-25 22:26:20'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7838'
  comment_author: Linky na víkend 36 na depi.sk - IT & Life Weblog
  comment_author_url: http://depi.sk/2006/11/25/linky-na-vikend-36/
  comment_content: '[...] How to structure large CSS files – ako štrukturalizova?
    rozsiahle CSS súbory [...]'
  comment_date: '2006-11-25 22:42:36'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '7839'
  comment_author: Kyle
  comment_author_url: ''
  comment_content: Whoever wrote this article should really think about using /*comments*/
    as well.
  comment_date: '2006-11-25 23:50:43'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7841'
  comment_author: Amir’s Blog &raquo; How to structure large CSS files (Yes, you do
    need to structure them)
  comment_author_url: http://amirsblog.freehostia.com/?p=35
  comment_content: '[...] Many methods exist to structure your CSS. This article tries
    to describe the method I use. I call it the “Tree method”, since it structures
    the CSS like… that’s right, a tree structure. Why not give it a try in your next
    project?read more&nbsp;|&nbsp;digg story [...]'
  comment_date: '2006-11-25 23:54:16'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '7842'
  comment_author: Ash Haque
  comment_author_url: http://www.bballcity.com/
  comment_content: My hardcore super organized css file:\n\nhttp://www.bballcity.com/wp-content/themes/foxtrot/style.css
  comment_date: '2006-11-26 00:39:13'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7849'
  comment_author: Bruce Boughton
  comment_author_url: ''
  comment_content: Using full paths in CSS selectors is not necessarily a good idea.
    This is because of specificity. The fuller the path, the more specific the rule
    and so the greater the importance applied to it.\n\nIt's generally better to be
    as concise as possible in selectors so that when you need to override a rule it's
    fairly easy to be more specific.
  comment_date: '2006-11-26 02:49:41'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7850'
  comment_author: Bruce Boughton
  comment_author_url: ''
  comment_content: 'And anyone who puts declarations all one line is an idiot!  That''s
    the most unreadable form of CSS.  It should go without saying that each declaration
    should be a new line. Also, alternated selectors should be on a new line.\n\ne.g.\n\n<pre>\na#link,\na#visited
    {\n  font-color: purple;\n  text-decoration: none;\n  padding: 0 0.3em;\n}\n</pre>'
  comment_date: '2006-11-26 02:51:52'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7858'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@John: Yes, this sites CSS is a mess (as I wrote in the first
    comment). It''s because it''s over a year old and I didn''t know this method then.\n\n@Seamus:
    Good idea. You could take it even further and make little modules with CSS rules
    that you only include if they are needed. I wrote about that some time ago in
    the article  <a href="http://friendlybit.com/css/static-and-dynamic-css-combined/"
    rel="nofollow">Static and dynamic CSS combined</a>.\n\n@Paul: Good to hear. I
    don''t want to set hard rules you never should break, always adapt the rules to
    the situation at hand.\n\n@Kyle: Yes, I should have mentioned commenting as well,
    thanks.\n\n@Bruce Boughton: On the contrary. I''d say a bigger problem is when
    other rules collide with yours and you end up with unexpected behavior. Knowing
    about specificity is a must though, thanks for adding it.\n\nPeople that put everything
    on one line has their reason for it. If you want to call people idiot, please
    stick to digg.com :)'
  comment_date: '2006-11-26 05:11:49'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '7864'
  comment_author: Stuart
  comment_author_url: ''
  comment_content: Like stated earlier using the /*Comment*/ within CSS is a better
    way to structure CSS then to just indent everything.
  comment_date: '2006-11-26 07:47:41'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7880'
  comment_author: Fatih Hayrio?lu’nun not defteri &raquo; 26 Kas?m WEb’den seçme haberler
  comment_author_url: http://www.fatihhayrioglu.com/?p=224
  comment_content: '[...] Büyük boyutlu CSS dosyalar?n? nas?l organize edece?imiz
    anlatan güzel bir makale http://friendlybit.com/css/how-to-structure-large-css-files/
    [...]'
  comment_date: '2006-11-26 14:40:21'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '7883'
  comment_author: Matt Wilcox
  comment_author_url: http://mattwilcox.net
  comment_content: 'Always use full path to elements - this is something I would disagree
    with. Such an approach is not a good idea, as the it leads you to use the maximum
    specificity for the rule''s selector straight away - this can lead to problems
    when you need to over-ride a general rule with a more specific one later on.\n\np
    { attribute : value; }\n\ncan be over-ridden by\n\n#content p { attribute : value2;
    }\n\nIf you always use the ''full path'' you can no longer over-ride a rule later
    in the document. You are ignoring the importance of the cascade and specificity
    by instructing people to ''always'' use the full path. This is harmful to a proper
    understanding and use of CSS.\n\n\nOther than that, there are some good ideas
    here. Nice one. :)'
  comment_date: '2006-11-26 15:36:55'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7886'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Stuart: Why not do it *too*? I find that seeing the structure
    by looking at the code is better than having to read through documentation. Sure,
    comment when needed, but make sure it''s not needed that often.\n\n@Matt Wilcox:
    I don''t find that a problem. Since you''re adding rules at the most specific
    case (full paths), you only specify the style for that specific case. Why would
    you want to change that later on? The only case I see is when another "template"
    on your site wants to change it. That case is handled by using the suggested "body#template
    [full path]" trick, something that gives higher specificity and therefore works.
    Try it, it really works well.'
  comment_date: '2006-11-26 16:38:06'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '7901'
  comment_author: Minimizr &raquo; Blog Archive &raquo; Minimal CSS
  comment_author_url: http://www.minimizr.com/blog/2006/10/minimal-css/
  comment_content: '[...] How to structure large CSS files Added 2006-11-26 [...]'
  comment_date: '2006-11-26 22:56:02'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '7903'
  comment_author: Jonathan Nicol
  comment_author_url: http://f6design.com/journal/
  comment_content: Great article Emil.\n\nI'm glad to see you advocate placing each
    declaration on a separate line. In Jonathan Snook's recent post on the same topic
    he was in favor of placing all declarations on the same line, but to me, that
    way is a very difficult to interpret and maintain (even if it does make file sizes
    smaller).\n\nIndentation is something I've recently begun to do, and I find it
    greatly helps with readability.\n\nI'll try your alphabetical suggestion on my
    next site...
  comment_date: '2006-11-26 23:35:02'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '7907'
  comment_author: How to Structure CSS Files &raquo; Another Blogger
  comment_author_url: http://www.anotherblogger.com/2006/11/26/how-to-structure-css-files/
  comment_content: '[...] How to Structure CSS Files   Sometimes things come across
    my aggregator at just the right time. Like when I saw How to structure large CSS
    files via a del.icio.us feed as I’m gearing up on working on a brand new WordPress
    theme.  tagged as: css, del.icio.us [...]'
  comment_date: '2006-11-27 00:49:58'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '7922'
  comment_author: its about time&raquo; Blog Archive &raquo; links for 2006-11-26
  comment_author_url: http://timelady.com/blog/2006/11/27/links-for-2006-11-26/
  comment_content: '[...] How to structure large CSS files - Friendly Bit This is
    a useful view of managing large css files (tags: css webdesign tips structure
    webdev optimization guide tutorial design article) [...]'
  comment_date: '2006-11-27 07:55:52'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '7926'
  comment_author: I Only Wish &raquo; Blog Archive &raquo; How to structure large
    CSS files (Yes, you do need to structure them)
  comment_author_url: http://www.ionlywish.com/?p=300
  comment_content: '[...] read more&nbsp;|&nbsp;digg story [...]'
  comment_date: '2006-11-27 09:19:12'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '7957'
  comment_author: 11/27/2006 8:03 PM - Matthew Gifford
  comment_author_url: http://www.matthewgifford.com/2006/11/27/1301/
  comment_content: '[...] As a web developer, one of the things I struggle with is
    keeping my CSS files from becoming a complete disaster. I’m sure that some of
    you reading this share my pain. A couple days ago, I ran across a post by Emil
    Stenström about what he calls the Tree Method. [...]'
  comment_date: '2006-11-28 06:04:03'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '7993'
  comment_author: Philip Withnall
  comment_author_url: http://tecnocode.co.uk/
  comment_content: I would advise against using the second one ("full path" to elements),
    as it means you can't use CSS specificity to override your own rules in other
    files, or later on. In fact, I'd go as far as to say that you should always use
    the smallest path possible for a rule, and use classes where semantically appropriate.
    This means that you can easily override your rules later, with more specific ones.
  comment_date: '2006-11-28 19:33:28'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '8004'
  comment_author: django forums
  comment_author_url: ''
  comment_content: I cant stand indentation in anything but code. I hate HTML that
    is indented, maybe im still hardcore to the notepad days where if anything was
    indented it would go all off the side or when word-wrapped would be nasty mess.\n\nI
    also prefer no space after the colon :p\n\nok that was anal-retentive but oh well
    :p
  comment_date: '2006-11-28 22:53:03'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '8018'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@django forums: Nice to hear your opinion, I''m guessing you use
    an entirely different method to keep your CSS:es structured and organized. And
    of course that''s just fine :)'
  comment_date: '2006-11-29 01:16:32'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '8019'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Philip Withnall: See my reply to Matt Wilcox above. It''s not
    a problem in my experience.'
  comment_date: '2006-11-29 01:17:56'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '8035'
  comment_author: xocea &raquo; How to Structure Large CSS Files
  comment_author_url: http://www.xocea.com/blog/?p=141
  comment_content: '[...] Via friendlybit: Many methods exist to structure your CSS.
    This article tries to describe the method I use. I call it the “Tree method”,
    since it structures the CSS like… that’s right, a tree structure. I want to stress
    that it isn’t my invention; I just describe and give reasons for its rules. [...]'
  comment_date: '2006-11-29 05:59:19'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '8049'
  comment_author: How to structure large css files &laquo; Crossing the net as I work
  comment_author_url: http://netrunning.wordpress.com/2006/11/29/how-to-structure-large-css-files/
  comment_content: '[...] Friendly bits tell use how to structure large css files.
    Everyone that has built a bigger site has had to deal with the mess CSS so easily
    become. There are ids and classes all over the place, and to find where a certain
    class is defined you usually need to use some search feature in your editor. Matching
    the other way, from the CSS to the HTML is even harder; you don’t even know what
    file a certain class is defined in. It’s a mess. The Tree method tries to structure
    the CSS into logical blocks; blocks taken from the HTML. [...]'
  comment_date: '2006-11-29 13:25:14'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '8053'
  comment_author: Structuring large css files at bling bling nivas.hr blog - white
    and nerdy edition
  comment_author_url: http://www.nivas.hr/blog/2006/11/29/structuring-large-css-files/
  comment_content: '[...] Whats a smart way to structure your css for easy editing
    and navigation? Give it a read here, curtosy of Emil Stenstrom.  Share and Enjoy:These
    icons link to social bookmarking sites where readers can share and discover new
    web pages. [...]'
  comment_date: '2006-11-29 15:11:54'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '8077'
  comment_author: Adam McIntyre
  comment_author_url: ''
  comment_content: 'A very good article As someone who routinely writes giant chunks
    of CSS, I can attest to the fact that these things work.\nI was never a big fan
    of alphabetizing properties - I always grouped "related" items - until I gave
    it a chance. Now, instead of having to jump around a list of properties (width
    and height may "jump up" in the order if position isn''t present) I can scan much
    more quickly.\nTo join the battle    on specificity, I''m with Emil: as specific
    as possible from the get-go. This doesn''t limit you from things like the cascade;
    rather, it lets you use  the cascade to apply general properties to a large group
    of elements  and very specific properties to very specific elements. I think specificity
    forces you to think about grouping and the cascade and helps reduce elements with
    duplicated or redundant properties, replacing them with elements gradually increasing
    in property specificity.'
  comment_date: '2006-11-29 22:45:24'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '8085'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Adam McIntyre: Couldn''t agree with you more! Don''t miss Maurice''s
    script linked to at the end, if you use the same structure that I do it''s a big
    timesaver.'
  comment_date: '2006-11-30 00:30:27'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '8988'
  comment_author: Technikwürze &raquo; Technikwürze 50 - Das Doppeljubiläum
  comment_author_url: http://www.technikwuerze.de/podcast/technikwuerze50/
  comment_content: '[...] Eine Möglichkeit, größere CSS-Dateien gut zu strukturieren,
    zeigt Emil Stenström in seinem Artikel How to structure large CSS files.   Podcast
    anhören Jetzt hören: [...]'
  comment_date: '2006-12-12 00:33:34'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '9218'
  comment_author: Andrew Stewart
  comment_author_url: http://airbladesoftware.com
  comment_content: If you're on Rails, you might like my css_dryer plugin which lets
    you nest selectors to avoid duplication.  So:\n\n<pre>\n#header {\n  h1 { ...
    }\n  h2 {\n    p { ... }\n  }\n}\n</pre>\n\nbecomes:\n\n<pre>\n#header { ... }\n#header
    h1 { ... }\n#header h2 { ... }\n#header h2 p { ... }\n</pre>\n
  comment_date: '2006-12-14 12:20:24'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '9223'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Andrew Stewart: very interesting Andrew! I think I like the different
    syntax you use, but it''s feels a little like a step backwards to the macro-age.
    It does become less typing on your part, but you miss important things (that are
    on your ToDo) like cachning. Good idea though.'
  comment_date: '2006-12-14 13:34:44'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '9499'
  comment_author: Cum sa-ti structurezi fisierele CSS - 100%Design
  comment_author_url: http://www.100la100design.ro/xhtml-css/2006/12/cum-sa-ti-structurezi-fisierele-css/
  comment_content: '[...] autor: Emil Stenström pe 21 Noiembrie, 2006 sursa: http://friendlybit.com/css/how-to-structure-large-css-files/    Categoria:
    XHTML &amp; CSS        Search [...]'
  comment_date: '2006-12-16 16:00:56'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '9794'
  comment_author: links for 2006-11-26 // willkoca
  comment_author_url: http://www.willkoca.com/2006/11/26/links-for-2006-11-26/
  comment_content: '[...] How to structure large CSS files - Friendly Bit (tags: css
    webdesign optimization) [...]'
  comment_date: '2006-12-19 23:08:16'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '17700'
  comment_author: '??? ??????.NET &raquo; ?????? #284'
  comment_author_url: http://alick.ru/2007/01/31/p200
  comment_content: '[...] case the fingerprint you want to forge) one should rely
    on well tested forensic research methods.How to structure large CSS files. ?????????
    ???????? ??????? ?? ?????????????? ????? ? [...]'
  comment_date: '2007-01-30 22:31:14'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '21825'
  comment_author: '&raquo; - &raquo; Estruturando o código CSS Tableless.com.br -
    Web Standards com Farinha e Pimenta'
  comment_author_url: http://www.tableless.com.br/estruturando-o-codigo-css
  comment_content: '[...] era um assunto que eu queria falar aqui a muito tempo. Vi
    este link no URL Sinistras e me animei a escrever [...]'
  comment_date: '2007-02-22 01:27:16'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '28194'
  comment_author: How to structure large CSS files (Yes, you do need to structure
    them) &laquo; Programming News
  comment_author_url: http://dontezm.wordpress.com/2007/10/06/how-to-structure-large-css-files-yes-you-do-need-to-structure-them/
  comment_content: '[...] read more | digg story [...]'
  comment_date: '2007-10-06 09:53:13'
  comment_post_ID: '106'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '30184'
  comment_author: Johaness
  comment_author_url: ''
  comment_content: Another solution would be to break up the large CSS files into
    multiple CSS files. The top-level CSS file would have rules common to all pages.
    The other CSS files will either over-ride the rules of the main CSS file or define
    new ones.\n\nThe problem is if you use server side includes (e.g. PHP) and have
    the page header (with the opening *and* closing HEAD tags ), you will include
    the exact same CSS files for every page. \n\nE.g. I include this on top of every
    page:\n\n<pre><code lang="html">\n CSS \n\n/* all css files included here */\n\n&lt;!--
    menu -->\n &lt;a href="#" rel="nofollow"> Home &lt;/a> \n &lt;a href="#" rel="nofollow">
    Other Page&lt;/a>\n</code></pre>\n\nThat problem can be solved with a very messy
    and misguided solution - conditional if statements that test for the name of each
    page and include accordingly.\n\nThe better way would be to use an MVC framework
    or plain Object Oriented PHP for a far more elegant solution.
  comment_date: '2008-01-24 19:20:22'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '30408'
  comment_author: lewis litanzios
  comment_author_url: http://www.ldexterldesign.co.uk/
  comment_content: i've loosely based my latest project on andy budd's (http://tinyurl.com/2oucvd)
    approach; splitting  default, basic, links &amp; navigation, layout, typography,
    colour, forms, and tables up into separate sections. obviously an alternative
    would be to source independent, dedicated, css files - this approach has never
    enticed me into using it. it's just too fragmented imo, not to mention load time.\n\none
    downside to splitting this info up into dedicated sections is you often find your
    self writing the selectors two or three times in different sections when you could,
    in theory, just include all properties under one selector in one place.\n\nbreaking
    things up has far more benefits though. for instance you can sit down and concentrate
    specifically on the typography for instance (although in my next project i'll
    be deciding upon my type before i do any layout). it's far to easy to become a
    whore to type once the layout is all done and dusted.\n\nthink i agree on the
    full path issue; i'll be implementing that in my next project. look at it this
    way, if you do use full paths it ties in with the alphabetical approach nicely.\n\nnot
    sure about the indentation thing, but nevertheless interesting. i'm one of those
    people that uses 'the least human readable approach', in one liners, for my css
    presentation. my justification is it's less scrolling down to get to what you
    want; once there you can obvious format it how you like when/if editing it.\n\ni'm
    a big fan of CSS Formatter and Optimiser (http://tinyurl.com/2vpxfe) and use it
    at the end of every project to tidy things up, group selectors, shorten property
    values (hex colours, shorthand padding/margins etc) and generally get a nudge
    in the write direction for how i could make things a bit tighter in the next project.\n\nmy
    3 cents :)\n\ncheers emil!
  comment_date: '2008-03-06 19:16:50'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '30409'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Johaness: Yeah, if you look at a full site with lots of different
    subpages it gets more difficult, and I''ve often resorted to something like you
    describe. One CSS for global sites, and one for each subsection. I use server-side
    code to decide what to include when.\n\n@lewis litanzios: Great comment, thanks!
    I can see how people want to work with different sections at different times,
    but that''s not how I work. I always start with box layout, and then complete
    the same rules with typography information afterwards. Works well for me. \n\nI''ve
    actually never used a CSS Formater, but then again, I''m _very_ picky about what
    CSS i write, and it''s almost always already optimized when I first write it.'
  comment_date: '2008-03-06 20:23:58'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '30465'
  comment_author: lewis litanzios
  comment_author_url: http://www.ldexterldesign.co.uk/
  comment_content: '''I’ve actually never used a CSS Formater, but then again, I’m
    very_ picky about what CSS i write, and it’s almost always already optimized when
    I first write it.'' - haha, i wish i could say i coded so neatly. workin'' on
    it as always. check it out and let me know if you find any of it useful.\n\n''I
    always start with box layout, and then complete the same rules with typography
    information afterwards.'' - so let me get this straight. you will have your universal
    h1, h2, h3... p typographical elements defined and then you''ll target h3''s and
    p''s (and whatever) in their native divs to give them extra styling, where appropriate?\n\nup
    until now i''ve really done my best to stick with my universal styles, but now
    i''m finding myself needing more than six-odd fonts per page, so am beginning
    to embrace semantic conventions e.g. a date font might be styled as .date{...}\n\ni''m
    toying with the idea of posting a blog entry in the hope of getting some email
    advice;\n\n''to use semantic id''s sitewide (and have to name stuff all over the
    place), or use reusable classes'' - what''s your take?\n\ncheers emil. big aid.'
  comment_date: '2008-03-19 18:29:03'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '30587'
  comment_author: James O'Kelly
  comment_author_url: http://www.railsjitsu.com
  comment_content: Of course if you are lucky enough to use Ruby on Rails to build
    websites you can generate the whole mess using Sass :)
  comment_date: '2008-05-17 07:06:15'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '30869'
  comment_author: suraj
  comment_author_url: http://surajnaikin.blogspot.com
  comment_content: hi check out my blog,\n\nthis is the way i manage my css file...&amp;
    i have been succesfully used this over more than 50 projects\n\nhttp://surajnaikin.blogspot.com/2008/07/how-to-manage-your-style-sheet.html
  comment_date: '2008-08-05 21:31:47'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '31083'
  comment_author: craig
  comment_author_url: ''
  comment_content: I am just starting to document &amp; structure my html and here
    is the documention i have done so far. Just thought I'd share.\n\nDocumentation
    of CSS file.doc
  comment_date: '2008-10-02 23:57:24'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '31085'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@craig: Cool documentation, I have a lot to learn from that one!
    Thanks a lot for sharing it, I''m sure lots of people will find it useful.'
  comment_date: '2008-10-04 00:21:13'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '1'
- comment_ID: '31633'
  comment_author: Damjan Mozetic
  comment_author_url: http://scarfoo.com
  comment_content: Can't agree on the Always use the “full path” to elements rule.
    If you do that you will probably encounter a case later on, which will require
    you to override the previous rule with a new, more specific one and you won't
    be able to do that unless you use the !important CSS rule. \n\nI'd rather opt
    for as short selectors as possible and comment my code sections appropriately
    to quickly find which selector represents what.
  comment_date: '2009-03-11 12:12:58'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '32916'
  comment_author: kit
  comment_author_url: ''
  comment_content: This article is great and I utilized most of these techniques for
    a while until I started to adapt things a bit and I didnt see this technique mentioned
    in other comments so I thought I'd add my 1cent...\n\nI now group related properties
    on the same line, especially position-left-top; width-height; I then sort everything
    alphabetically. I find this makes the scanning simpler when navigating styles.\n\n#example{\n  position:value;
    top:value; left:value;\n  width:value; height:value;\n}\n\nI do think the catagory
    ordering could be useful, especially for font styling and I'll have to see how
    that works out in my next project.\n\nAlso using 2 spaces for tabbing is nice
    too when I start getting into more complex designs
  comment_date: '2009-08-20 02:34:29'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '34103'
  comment_author: Richard Knop
  comment_author_url: http://richardknop.com/
  comment_content: I like to divide my css into multiple files such as:\n\n<code>\ngeneral.css\nlayout.css\nheader.css\nnavigation.css\ncontent.css\nsidebar.css\nfooter.css\nother.css\n</code>\n\nThen,
    I have one main stylesheet called default.css whee I import all the CSS files
    like this:\n\n<code>\n@import url('/css/general.css');\n\n@import url('/css/layout.css');\n\n@import
    url('/css/header.css');\n\n@import url('/css/navigation.css');\n\n@import url('/css/content.css');\n\n@import
    url('/css/sidebar.css');\n\n@import url('/css/footer.css');\n\n@import url('/css/other.css');\n</code>\n\nThis
    way the individual stylesheet files related to individual parts of the web application
    are smaller in size (which means I can faster find what I'm looking for and it's
    easier to make changes) and contain only relevant styles.\n\nI also like to order
    the selectors in individual stylesheet files in the same order as they appear
    in the HTML markup.
  comment_date: '2010-09-23 09:47:10'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
- comment_ID: '34106'
  comment_author: Damien P.
  comment_author_url: http://www.damienpetitjean.fr
  comment_content: 'I use to do like this :\n\nfirst, I put all global selector like
    p, h1, etc.\nsecond, I put generic classes .strong, .clear\nafter that, I put
    my selectors #header, #footer\nand at the end bug fixes.'
  comment_date: '2010-09-23 17:20:19'
  comment_post_ID: '106'
  comment_type: null
  is_admin: '0'
---