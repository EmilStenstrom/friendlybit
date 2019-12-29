---
comments:
- comment_ID: '30359'
  comment_author: madr
  comment_author_url: http://madr.se
  comment_content: 'Great list! I have been n a similar situation about documenting
    JavaScript. This list can be applied to that one too. \nAnother thing worth menioning
    is CSStidy, which can clean up and sort CSS when development is done. It can be
    a toll to keep CSS consistent.\n\n(fyi: I read this article and wrote this comment
    on lynx, since I doing som server confs at the moment. Works just fine.)'
  comment_date: '2008-02-28 00:11:34'
  comment_post_ID: '147'
  comment_type: null
  is_admin: '0'
- comment_ID: '30364'
  comment_author: Jens Wedin
  comment_author_url: http://jedisthlm.com
  comment_content: Good write-up. This is really important when leaving your precious
    style file to another developer. Just the "Where do I add my own stuff" is good.
    A good thing if you don´t use your own "framework" that you can reuse in every
    project is to have a look at other frameworks like Blueprint. There are some nice
    stuff that you can be inspired of like structure and documentation. I would also
    recommend to have a look at minify. It combines, minifies, removes comments etc
    with multiple css files. The good thing is that you can work a lot with comments
    within the file, minify then removes this on the fly and makes a cached copy of
    the file. It also have a bunch of other great stuff in it.\n\nHere's an example
    of my css and the minified copy\n\n<a href="http://jedisthlm.com/wp-content/themes/jedisthlmV/screen.css\nhttp://jedisthlm.com/minify.php?files=/wp-content/themes/jedisthlmV/screen.css\n\nhttp://code.google.com/p/minify/\nhttp://code.google.com/p/blueprintcss/"
    rel="nofollow">http://jedisthlm.com/wp-content/themes/jedisthlmV/screen.css\nhttp://jedisthlm.com/minify.php?files=/wp-content/themes/jedisthlmV/screen.css\n\nhttp://code.google.com/p/minify/\nhttp://code.google.com/p/blueprintcss/</a>
  comment_date: '2008-02-28 10:09:40'
  comment_post_ID: '147'
  comment_type: null
  is_admin: '0'
- comment_ID: '30366'
  comment_author: Andreas
  comment_author_url: http://exscale.se
  comment_content: 'I always structure my CSS like I structure all my code; modular.\n\nEach
    module gets its own CSS-file. Any selector in a module-CSS must start with that
    module''s ID-name (every module has a div with an ID of the same name as the module
    (div#recent-comments for example)).\n\nModule-files should _never_ style generic
    classes or elements. Everything should go through the #module-id.\n\nThis way
    modules cannot mess with other modules and you know that if there''s a layout-issue
    with the "Recent comments"-module you look in the recent-comments.css-file.\n\nGeneric
    styling and reseting/styling of basic elements is all done in general.css.\n\nSometimes
    I have a site.css which styles the header, navigation, content, sub-content and
    footer-modules in one file. It''s sometimes easier to get an overview of the design
    if they''re all in the same file.\n\nI''ve also written my own  constant-parser
    that removes the need for CSS-classes, and I save nifty constants in constants.css
    (or, if it gets massive I start dividing that up as well depending on what type
    of constant it is (list-styles, table-styles, div-styles, icons).\n\nAfter working
    on 150+ modules-sites for 2 years this is easily the most straight-forward, easy-to-grasp
    way of structuring your CSS and it leaves you with very few bugs.\n\nHow annoying
    isn''t it when you fix a bug in one module only to introduce a new one in another?
    Structuring your code like this will eliminate problems like that.'
  comment_date: '2008-02-28 12:24:04'
  comment_post_ID: '147'
  comment_type: null
  is_admin: '0'
- comment_ID: '30371'
  comment_author: madr
  comment_author_url: http://madr.se
  comment_content: '@Andreas, I work like that too, except I mark up every modules
    (or service, as it is called in our current project) with classes instead. \nThe
    CM lets the subscriber publish multiple instances of each service on a page, and
    this makes it impossible to mark services with unique IDs. :('
  comment_date: '2008-02-28 15:59:48'
  comment_post_ID: '147'
  comment_type: null
  is_admin: '0'
- comment_ID: '30375'
  comment_author: Andreas
  comment_author_url: http://exscale.se
  comment_content: Ah yes, in some cases I use a class rather than an ID as well if
    the module (or service (that's a new one to me, everybody here (Y!) says "modules"))
    will be included more than once.\n\nIn some cases tho, like an article-listing
    I'd consider the article-listing to be the module, not the article(s), so i'll
    have a div#article-listing wrapped around all the articles, and each article gets
    a div#article-1234 as well, rather than just a row of div.article:s.\n\nI try
    to steer clear of classes as much as possible. I don't know why really but I rarely
    see them used in a way that's actually relevant to the HTML.\n\nIn most cases
    classes represent too much design/behavior (.box, .left etc) for me to feel comfortable
    using them.\n\nThe div[id] around the module adds to the structure of the HTML
    and is not there for styling but only for consistency and structure.\n\nFact is
    <a href="http://code.google.com/p/aframework/" rel="nofollow">my framework</a>
    automatically adds wrapper divs around modules, this is great when you're updating
    a module using ajax and you want to fetch it without the wrapper-div because you're
    actually putting the response in the wrapper-div and should it contain a wrapper-div
    you'll end up with nested divs with the same IDs.\n\nObviously it all depends
    on how you use classes, but to me IDs make more sense to wrap modules.\n\nThink
    I just increased Friendlybit's height by another 400px with this comment :). Perhaps
    a little wider comment-area in the coming design?
  comment_date: '2008-02-28 18:20:50'
  comment_post_ID: '147'
  comment_type: null
  is_admin: '0'
- comment_ID: '30383'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jens Wedin, Andreas: Thanks for all those great links and structuring
    tips, I''ll look into them for my next project!'
  comment_date: '2008-02-29 09:08:32'
  comment_post_ID: '147'
  comment_type: null
  is_admin: '1'
- comment_ID: '30384'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Andreas: Yes, I really need a wider commenting area...'
  comment_date: '2008-02-29 09:08:53'
  comment_post_ID: '147'
  comment_type: null
  is_admin: '1'
---