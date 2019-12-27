---
comments:
- comment_ID: '31833'
  comment_author: Ole
  comment_author_url: http://www.h2ok.de
  comment_content: Good work. I've used the <a href="http://newism.com.au/blog/post/58/bigtarget-js-increasing-the-size-of-clickable-targets/"
    rel="nofollow">bigTarget jQuery plugin</a> so far, but your code is much more
    tiny...\n\nThanks for that, i'll try this out.
  comment_date: '2009-07-01 08:47:44'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '31839'
  comment_author: grimen
  comment_author_url: ''
  comment_content: Great! I did some polishing (well, depending on what one is looking
    for):\n\n(function($)\n{\n  $.fn.clickable = function(options)\n  {\n    var clickable
    = this;\n    \n    clickable.each(function()\n    {\n      var e = $(this);\n      \n      e.click(function()\n      {\n        window.location
    = $(this).find('a:first').attr('href')\n      });\n      \n      e.hover(function()\n      {\n        window.status
    = $(this).find('a:first').attr('href')\n      }, function()\n      {\n        window.status
    = ''\n      });\n      \n      e.addClass('anchor');\n    });\n    \n    return
    clickable;\n  };\n})(jQuery);
  comment_date: '2009-07-01 11:02:34'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '31847'
  comment_author: trovster
  comment_author_url: http://www.trovster.com
  comment_content: It seems there are a few of us who have realised this progressive
    enhancement is really useful. Like Ole mentioned, my friend Leevi released his
    <a href="http://newism.com.au/blog/post/58/bigtarget-js-increasing-the-size-of-clickable-targets/"
    rel="nofollow">bigTarget jQuery plugin</a>. At pretty much the same time I got
    my demo page up for the code I've been using for a while, check out my <a href="http://www.trovster.com/lab/plugins/fitted/"
    rel="nofollow">Fitted jQuery plugin</a> which achieves similar things.
  comment_date: '2009-07-01 13:50:47'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '31854'
  comment_author: Zach Leatherman
  comment_author_url: http://www.zachleat.com/
  comment_content: I'm not a huge fan of this approach, as it doesn't allow things
    like right click to open in a new tab, or middle click for the same.\n\nJames
    Padosley had a good method for this:\nhttp://james.padolsey.com/javascript/table-rows-as-clickable-anchors/
  comment_date: '2009-07-01 17:03:37'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '31860'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Ole, trovster, grimen: Yeah, I found your suggested plugins right
    after I posted. I''m not sure I need it in plugin form, I usually just use this
    for a couple of boxes on the start page, which means supporting a single class,
    and 12 lines of code, is fine. Thanks though.'
  comment_date: '2009-07-01 19:10:22'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '1'
- comment_ID: '31868'
  comment_author: Anon
  comment_author_url: ''
  comment_content: Why not just give links more padding? Making elements clickable
    that are normally not clickable leads to confusion and is not a behavior users
    expect.
  comment_date: '2009-07-01 22:29:05'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '31875'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Zach Leatherman: That''s a very valid concern. I''ll see if I
    can add middle-click to the snippet if I get the time. Should be possible to forward
    the event from the block to the link somehow.\n\n@Anon: What kind of confusion?
    These are all extra features, that make things easier for the user. If you look
    at the example, you''ll see that more padding just doesn''t work. Bigger clickable
    area (which the design should reflect, of course), means easier for user to hit
    it. I see only good things.'
  comment_date: '2009-07-02 00:10:05'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '1'
- comment_ID: '31954'
  comment_author: Krijn Hoetmer
  comment_author_url: http://krijnhoetmer.nl/
  comment_content: Please try HTML 5, where you can have block level elements inside
    an <code>a</code> element.
  comment_date: '2009-07-02 22:12:56'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32027'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Krijn Hoetmer: That''s actually a really good idea. Why should
    validation put us down? The only downpart I see is that it wouldn''t allow me
    to have other links inside it (as in the example). Because I guess HTML5 doesn''t
    allow links inside links, right? But that''s not such a big issue. Looking forward
    to good HTML5 support in browsers.'
  comment_date: '2009-07-03 23:18:02'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '1'
- comment_ID: '32144'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: 'Interesting. But i hope that xhtml 2 will come faster. This will
    allow href attribs for any element. So making a div clickable in xhtml 2 is straightforward:
    &lt;div href="http://www.some.where.com"/&gt;...\n\nThe better solution i think
    :)'
  comment_date: '2009-07-06 11:55:03'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32146'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Siegfried: XHTML 2 has been canceled, and will be replaced with
    HTML 5. So no href attributes in sight.'
  comment_date: '2009-07-06 12:09:41'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '1'
- comment_ID: '32834'
  comment_author: Krijn Hoetmer
  comment_author_url: http://krijnhoetmer.nl/
  comment_content: '@Emil: It already "validates", when you use the HTML5 doctype.
    You can''t have nested links indeed, but that makes sense in a way :) And it already
    works cross-browser <em>today</em>; you only need to put <code>display: block;</code>
    on your links (and make sure to use closing <code>p</code> tags, etc.), so it''s
    one of the safe parts of the draft you can already use, imho. The only problem
    this doesn''t solve is making entire <code>tr</code> elements <code>href</code>able,
    due to table parsing and the magic that involves. You still need JavaScript for
    that.'
  comment_date: '2009-07-13 11:03:20'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32835'
  comment_author: Krijn Hoetmer
  comment_author_url: http://krijnhoetmer.nl/
  comment_content: Also, using this, you get <code>:hover</code> styles for free (without
    using JS hacks) in IE6, since that babe only understands <code>:hover</code> on
    <code>a[href]</code>.\n\nI only wonder how search engines and AT work with this.
    "Click here" links clearly suck, but perhaps linking entire blocks of text, including
    headings, sucks as well. Would using <code>title=""</code> on the link solve that?
    Somebody should do some study in that field :)
  comment_date: '2009-07-13 11:12:23'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32843'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Krijn Hoetmer: Great comments, you know a lot about stuff :)
    A search engine experiment with block links would be interesting. My guess is
    that the more words you have inside your link, the less weight each of them have.
    So for SEO, this might not be the most optimal solution. On the other hand, search
    engines care about words around a link too, so I''m not sure how much of a difference
    it makes.'
  comment_date: '2009-07-15 08:39:06'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '1'
- comment_ID: '32846'
  comment_author: Anders Ytterström
  comment_author_url: http://madr.se
  comment_content: In really extreme cases (that is, 80+ teasers) further enhancements
    can be done by letting a global click listener do the job with event delegation.\n\nThat
    will save a few buck on DOMready, especially in IE which is really slow in comparison.
  comment_date: '2009-07-15 21:33:22'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32857'
  comment_author: Stevie D
  comment_author_url: http://getdown.org.uk/bus/search/bedale.shtml
  comment_content: Brilliant! I have been doing this manually on my website for a
    few years, just adding an <code>onClick</code> event to the containing <code>div</code>
    - see website link for example. But this looks like a better solution, means I
    don't need to worry about putting in the links twice every time.\n\n<blockquote>Why
    not just give links more padding? Making elements clickable that are normally
    not clickable leads to confusion and is not a behavior users expect.</blockquote>\nIt
    depends on the nature of the content. In some cases, extra padding, leading or
    spacing will do a good job. In other cases, it helps to make surrounding content
    clickable. For example, on my website, there is a 'panel' that contains several
    items, and making the entire panel into a link makes it easier for users to select
    it - while, of course, retaining on old fasioned anchor on the first line for
    accessibility and spiders.\n\nBy applying <code>:hover</code> properties to the
    <code>div</code>, you give the visual affordance of a link to users (hand cursor,
    change of colour), so there should be no problem with unexpected behaviour.
  comment_date: '2009-07-23 14:07:01'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32858'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Stevie D: Nice to see that my scribbling is of use to someone
    :)'
  comment_date: '2009-07-23 20:47:32'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '1'
- comment_ID: '32867'
  comment_author: Andreas
  comment_author_url: http://andreaslagerkvist.com
  comment_content: Simply positioning an a-element absolutely on top of the div with
    a width and height of 100% would achieve the same thing, no? _And_ it would act
    exactly the same as a real link (as it _is_ a real link).\n\nI've done it this
    way before though as well, just a thought.\n\nRegarding the JS-only CSS; I've
    used a js-enabled/js-disabled class on the body-element for ages now and it's
    perfect for things like this.\n\nI add the js-enabled class immediately after
    the opening body-tag so there'll be no lag for the JS-only styling:\n\n<code>\n&lt;body
    class="js-disabled"&gt;\n&lt;script type="text/javascript"&gt;\ndocument.body.className
    = 'js-enabled';\n&lt;/script&gt;\n</code>\n\nAs any performance-aware front-end
    developer I include all my JS before the _closing_ body-tag so it normally takes
    a couple of seconds before it kicks in. Giving body the js-enabled class at the
    top avoids styles blinking in though.
  comment_date: '2009-07-24 12:58:43'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32868'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Andreas: It''s actually not exactly the same, as it has some
    strange side effects. Since the image covers all the text and images in the teaser,
    you can select or save the text or the image. And you can''t have more than one
    link in the same teaser, something that might matter for some (although few) people.
    On the other hand you get the possibility to middle-click the link, and all that.↵↵Nah,
    I still like the HTML5 solution (see above comment) best I think.'
  comment_date: '2009-07-24 13:11:55'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '1'
- comment_ID: '32920'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: Do you think that by using this javascript method the SEO of that
    page will remain the same? Google has some issues reading javascript..\n\nAnyway
    the demo looks great!
  comment_date: '2009-08-21 20:13:02'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32922'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Alex: This way of doing this is unobtrusive, which means that
    even if Google wouldn''t read the data, it could still find and parse the link.'
  comment_date: '2009-08-22 19:27:07'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '1'
- comment_ID: '32925'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: '@Emil, if that''s cleared, how can we make the link to open in
    a new tab/windows on right click?'
  comment_date: '2009-08-23 18:03:26'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32926'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Alex: Unfortunately, there''s no easy way to do that to the whole
    block. Though you could right-click on the real link, and do what you want there.'
  comment_date: '2009-08-24 21:51:53'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32927'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: '@Emil, sorry i noticed that the real link retains it''s capabilities
    only after i''ve posted my last comment. \n\nWhat i really like is that even if
    javascript is disabled you don''t get any error messages and the div block remains
    as if there is no javascript there.'
  comment_date: '2009-08-25 04:04:16'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '32987'
  comment_author: Hacer un div clicable | Artimedia Blog
  comment_author_url: http://www.artimedia.es/blog/diseno-web/maquetacion/hacer-un-div-clicable/
  comment_content: '[...] veces interesa hacer una zona clicable en vez de un enlace
    de texto pequeño. En este artículo de friendlybit.com se presenta el código para
    hacer un div clicable que además puede contener otros enlaces [...]'
  comment_date: '2009-09-10 17:23:21'
  comment_post_ID: '498'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33131'
  comment_author: Lewis Litanzios
  comment_author_url: http://www.ldexterldesign.co.uk/
  comment_content: 'Yea, the "1''s" in pagination are a culprit here - pet usability
    hate of mine!\n\nI used this typa technique recently on a ''Read more...'' link:
    http://is.gd/4n09N (pulling in the post title URL and then hiding the title).'
  comment_date: '2009-10-17 00:38:04'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '33356'
  comment_author: Kristopher
  comment_author_url: http://www.shuttlebox.net
  comment_content: Nice! I love the fallback method and using the first link, instead
    of just hard coding some URL on the div. Very cool!
  comment_date: '2010-01-19 14:16:32'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '33480'
  comment_author: Sheena Rai
  comment_author_url: http://www.technetto.com
  comment_content: Div Click able Is A Nice Way to have test with image background
    to look like a image and make in more SEO friendly
  comment_date: '2010-03-24 21:53:16'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '33492'
  comment_author: Mac
  comment_author_url: ''
  comment_content: Thanks for this - I have a question I want to make 3 div's like
    this on my page, each one with a different anchor.\n\n1)How do I change the code
    for the 3 divs? \n2)Where does the script actually go? \n\nSorry for the simple
    questions, I'm not a programmer!
  comment_date: '2010-04-10 00:00:56'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '33494'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Mac: Just use several divs with the class "teaser", no other
    changes is needed for it to support multiple clickable blocks. \n\nFor a working
    example, and descriptions of where the script goes, check out the demo page, and
    copy code from there.'
  comment_date: '2010-04-11 17:19:04'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '1'
- comment_ID: '33847'
  comment_author: andy
  comment_author_url: ''
  comment_content: The demo looks great!
  comment_date: '2010-05-18 09:54:38'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '33848'
  comment_author: andy
  comment_author_url: ''
  comment_content: it’s a really good example of good use of javascript.
  comment_date: '2010-05-18 09:55:58'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
- comment_ID: '33938'
  comment_author: Robin Parduez
  comment_author_url: http://rpardz.com/
  comment_content: I've been using this technique for a while, but I have seen some
    examples of people using clickable divs without including a fallback link within
    the div for non-JS users. However, your JS technique handles this nicely, due
    to pulling the href from the link contained within the div. Thanks
  comment_date: '2010-06-25 10:52:45'
  comment_post_ID: '498'
  comment_type: null
  is_admin: '0'
---