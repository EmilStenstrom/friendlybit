---
comments:
- comment_ID: '30872'
  comment_author: Andreas
  comment_author_url: ''
  comment_content: Not very professional to have sheets that exceeds 1000 lines emil.
    better to have separate css for each component of a site and merge them together
    to one minified file in the deployment process....\n\nclients are already forced
    to parse and execute js, adding variables in css would just add another dimension
    when it comes to scaling and performence. even if the browser is smart enough
    to cache the parsed css, it will still make your front page load slower. \n\nIf
    you really would have needed css vars during all these years, you would have made
    some solution for your self by now, because thats how pros work. They make tools
    for themself when the current ones doesnt fit their needs.
  comment_date: '2008-08-07 18:37:34'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '30873'
  comment_author: devtrench
  comment_author_url: http://www.devtrench.com
  comment_content: 'I agree with Bert that css (or HTML as you propose) should not
    contain variables. Traditionally these languages have been void of programming
    features to keep them simple.  I think they should be kept that way and think
    the best argument that Bert makes is:\n\n"Even if the implementation cost of constants
    would be very small, it is still better to leave them out of CSS. That is a consideration
    for every addition to CSS: extending CSS makes implementing more difficult and
    programs bigger, which leads to fewer implementations and more bugs."\n\nCSS is
    already under implemented in browsers and sticking  this feature in could lead
    to more harm than good.  With all of the browser implementation problems we have
    now I can imagine how poorly this would be implemented.\n\nOne thing I didn''t
    see in either article (sorry if I missed it) is how variables would gracefully
    downgrade in older browsers. It''s pretty easy to tell a parser to ignore what
    it doesn''t know, like in the case of opacity.  But I don''t see how an older
    browser would parse something like color: $my_color.  No one better suggest we
    make 2 stylesheets :)\n\nMy 2c,\n\nJames'
  comment_date: '2008-08-07 19:14:30'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '30874'
  comment_author: Pelle
  comment_author_url: ''
  comment_content: I can see advantages with it as well.\n\nCSS variables would for
    example open up for some interesting optimizations possibilities as well - instead
    of having the same big values (background-images as data:urls can get particularly
    big) assigned at many different places it's only assigned at one place with a
    descriptive variable name which later an optimizer can replace with a single character.
  comment_date: '2008-08-07 19:16:04'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '30877'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Andreas: So you''re saying I''m not professional? I would say
    minifying something that doesn''t need to be minified is just as unprofessional.
    Just because Yahoo and Google needs to optimize to death does not mean everyone
    else needs to.\n\nIt doesn''t make parsing slower in any major sense. Webkit wouldn''t
    have implemented it if it did. Bert would also have put that argument forward
    then. What do you base that claim on?\n\nLastly. I work in several different languages
    (Java, C#, Ruby, Python), and often under tight deadlines. When in that situation
    I don''t sit down and construct a new template language. That would waste time
    for my customers, which is not how pros work.\n\n@devtrench: The argument you
    picked is really an argument to not extend CSS at all. I don''t agree with that.
    CSS3 should include more features than what we have today, features that are needed
    by todays professionals.\n\nI''m not sure there is any ideas of how to downgrade
    at the moment. The spec talks about using color: var(myColor); and perhaps you
    could just have a line with color: red above that one? If if can''t parse var,
    it drops the whole line.\n\n@Pelle: Yep, I agree. Although that isn''t the biggest
    gain since gzip (if you have that enabled) takes care of duplication pretty well.'
  comment_date: '2008-08-07 22:51:54'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '1'
- comment_ID: '30881'
  comment_author: Pära
  comment_author_url: ''
  comment_content: Hi,\n\nDont really know what vars in CSS would mean to me but i
    in my meaning CSS is already a, but reversed(?), form of variables.\n\nIf you
    for instance use "sprited" images, just register the css propery for image url
    once. Then add you selectors to that property set. \n\nIf accessing the same property
    value (say backgrounds, borders etc.) more than a few times I think one would
    have a fundamental problem in ones CSS. \n\nCatch my drift?\n\nCheers
  comment_date: '2008-08-08 18:50:39'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '30882'
  comment_author: Dutch
  comment_author_url: http://www.dutchhomepage.nl
  comment_content: I don't have any idea what you mean with variables? Do you have
    an example?\n\nCSS with 1000 lines? I don't have a large website, I only work
    for my private website, but I work with several websites, one with common lines
    which are used by every part, like divisions, menu etc. Other files are separate
    because I work with different backgrounds, menu colors etc.\n\nIs it smart to
    work with several stylesheets and are there more possibilities?
  comment_date: '2008-08-08 23:10:18'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '30884'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Pära, @Dutch: There are places where I can see variables simplify
    things. One place is skinning a page in different colors. Changing the skin would
    be made easier if there was a variable list at the top, that specified #342523
    as HeaderColor. Then you could use that variable <em>several times</em> in your
    stylesheet (for borders, backgrounds...). The same goes for margins that you set
    several times and need changeable from one location.\n\n@Dutch: 1000 lines is
    common since I often work on CMS:es, and those need to account for many many types
    of styling my editors. It isn''t uncommon that there''s no easy way to see what
    kind of page you have (article, section...) so you need to put all of them into
    one stylesheet. Big sites means big stylesheets :)'
  comment_date: '2008-08-09 12:35:12'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '1'
- comment_ID: '30895'
  comment_author: Jon Gilkison
  comment_author_url: http://interfacelab.com
  comment_content: 'Hi,\n\nI''m the author of the PHP implementation.\n\nJust to clarify,
    the PHP version is built to the exact same spec as the webkit version and the
    stylesheets can be used interchangeably.\n\nThe one difference, however, is that
    my implementation has an eval() statement that allows you to:\n\npadding: eval(somevar
    * 2);\nmargin: eval((anothervar / 2)*yetanother);\n\nPersonally, I don''t give
    a rip if anyone uses it or finds it useful.  We use it on a large site (massify.com)
    and have found it to be practical and a boon to productivity.  YMMV.\n\nAdditionally,
    the PHP version doesn''t compile it everytime, only if it has changed.  There
    is a command line version that will compile everything to static CSS files.'
  comment_date: '2008-08-10 00:26:38'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '30897'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jon Gilkison: I think your solution is a good one if they decide
    to not include that functionality in the CSS spec. The only problem I have is
    that PHP is just one of many languages, so I have to adapt to a slightly different
    template language each time. Why not implement them all to one spec as you have
    tried to then? That is a good idea, although each implementation will have their
    own extras, such as your quite useful calculations.\n\nWhat do you think about
    the inclusion of CSS Variables?'
  comment_date: '2008-08-10 02:39:35'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '1'
- comment_ID: '30900'
  comment_author: 'Prom?nné v CSS. A není to chyba? - Martin Hassman: blog nejen o
    prohlíže?ích'
  comment_author_url: http://met.blog.root.cz/2008/08/10/promenne-v-css-a-neni-to-chyba/
  comment_content: '[...] už to na internetu chodí, netrvalo dlouho, aby se objevili
    reakce, odkažme alespo? Why adding variables to  CSS is a good thing a Why CSS
    Variables are harmful : the pragmatic [...]'
  comment_date: '2008-08-10 14:26:24'
  comment_post_ID: '171'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '30907'
  comment_author: Jonah Dempcy
  comment_author_url: http://www.thetruetribe.com
  comment_content: '@Andreas: For performance reasons, you will ideally want to serve
    only one CSS file per page. If you want to separate the CSS file into multiple
    separate files, then you should write a build script that combines them all into
    a single file when deployed to the production website. You can still keep separate
    files for local development, if you like. \n\nPersonally, I prefer one file since
    I usually use inline find (CTRL+J) in Aptana to locate a given section of code.
    For those unfamiliar with inline find, it works the same as normal find but doesn''t
    cause a window to popup, so you can just start typing at any time. Firefox includes
    this as the default find behavior (when clicking CTRL+F).\n\nOn a side not, I
    abhor including separate IE stylesheets. It''s become commonplace now for sites
    to use conditional comments to include separate IE stylesheets, for instance:\n\n<code>\n&lt;!--[if
    lte IE 5.5] --&gt;\n&lt;!--[if IE 6]--&gt;\n&lt;!--[if gte IE 7]--&gt;\n</code>\n\nThis
    method frustrates me because I need to open 4 separate stylesheets to see all
    of the rules that are affecting an element. Instead, I much prefer this:\n\n<code>\n&lt;!--[if
    lte IE 5.5]--&gt;\n&lt;!--[if IE 6]--&gt;\n&lt;!--[if gte IE 7]--&gt;\n&lt;!--[if
    !IE]--&gt;\n</code>\nThis allows me to write CSS rules all in the same stylesheet,
    like so:\n\n<code>\n#some-element {\n    color: red;\n}\n.ie #some-element {\n    color:
    blue;\n}\n.ie6 #some-element {\n    padding-top: 10px;\n}\n.ie7 #some-element
    {\n    line-height: 120%;\n}\n</code>'
  comment_date: '2008-08-10 23:29:41'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '30909'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jonah Dempcy: Sorry, wordpress destroyed your code, I couldn''t
    restore it by guessing :( I see what you mean though. I tend to have one file
    for IE hacks, and one for all other browsers. Then again, I only support IE6 and
    IE7.'
  comment_date: '2008-08-11 21:49:06'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '1'
- comment_ID: '30913'
  comment_author: Rasmus Kaj
  comment_author_url: http://rasmus.krats.se/
  comment_content: When you say variables, I hope you mean symbolic constants?  In
    that case, I agree that they might be useful.  The semantics of such constants
    (regarding e.g. @include rules) might be complex enough, without considering changing
    values as well.\n\nAnd by the way, HTML already has such symbolic constants, they're
    called entities.  They can only be declared in the DOCTYPE, not in the page content,
    but they can still be usefull.  Last time I used them, I made sure to evaluate
    them in a preprocessing step, though.  Not in the browser.\n\nAnd preprosessing
    can be useful for css as well.  Plain old cpp or m4 is actually very useful, both
    for symbolic constants and for merging separate files to a single "end-user" file.
  comment_date: '2008-08-12 12:55:47'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '30914'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rasmus Kaj: Yes, I mean symbolic constants. They are called CSS
    Variables in the <a href="http://disruptive-innovations.com/zoo/cssvariables/"
    rel="nofollow">proposed spec</a>, that''s why I used that.\n\nDo you mean HTML
    character entities? Or are there some other kind of entity that I don''t know
    about? Another type of symbolic constant is the use of frames. It lets you divide
    your page into different parts and reuse them (Aside: <a href="http://www.w3.org/TR/WD-wwwicn.html"
    rel="nofollow">Fun spec</a>, found while googling).\n\nPreprocessing can solve
    these issues, but if preprocessing is something you always want, no matter what
    language, why not work at including it in the spec?'
  comment_date: '2008-08-12 20:16:13'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '1'
- comment_ID: '30924'
  comment_author: Anders Ytterström
  comment_author_url: http://madr.se
  comment_content: I can see the benefit. Adding variables on the presentation level
    should give one the opportunity to stop using "variables" on the content level.\n\nWith
    that, I mean the use of mutliple common classes to create a presentation of a
    block:\n<code>&lt;div class="nav horisontal tabbed"&gt;...&gt;</code>\n\nIt would
    be nice to instead create the css-variables nav, horisontal and tabbed in the
    css file(s) and use them internal. Would spare some non-content markup in the
    HTML.\n\nIs this a good reason, Emil, or have did I miss the whole real part of
    CSS variables?
  comment_date: '2008-08-16 13:23:28'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '31075'
  comment_author: Andreas
  comment_author_url: http://exscale.se
  comment_content: I've always been a fan of CSS-constants (they are constants are
    they not? They never change during run-time right?) but I'm not so sure they should
    be in there by default.\n\nThey're silly-easy to implement using _any_ server-side-language
    and the syntax in the CSS wouldn't have to change from server-side-language to
    language at all so you could re-use your CSS from server to server without problem.\n\n@Anders
    Ytterström - I like how you think and I had exactly the same ideas as you when
    I built my CSS constants PHP Class. To remove the need for classes altogether.\n\nI'm
    curious to know where you think HTML-constants (or variables) would be useful?
  comment_date: '2008-09-29 01:18:32'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '31077'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Andreas: Yes, constants is a better name, I just picked the name
    used in the references file.\n\nColoring is a perfect place where constants would
    be useful. If the client changes their mind concerning a color you just change
    that constant. No need for search/replace. And no need to write a Java-CSS wrapper...'
  comment_date: '2008-09-29 18:57:19'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '1'
- comment_ID: '31079'
  comment_author: Andreas
  comment_author_url: http://exscale.se
  comment_content: Thanks for the reply. But you never answered where you would find
    HTML-constants useful? Surely you don't specify colours in your markup?\n\nAlso
    - if you wanted to change the colour-scheme of a site (at least the ones I normally
    code) it wouldn't require the change of one single colour. It would require changes
    to probably 5-10 different colours _and_ background-images so I'm not sure constants
    would help that much in that case.\n\nI think the biggest benefit of constants
    is the one that Anders Ytterström mentions, to get rid of _all_ design-related
    stuff from the HTML. Classes like "box" or "self-clear" or anything that you put
    in there only because the current design requires it should be in the CSS - not
    the HTML.
  comment_date: '2008-09-30 00:27:44'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '31080'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Andreas: Ah, I read CSS-constants. HTML constants is something
    that I use every day, in different languages. In some they are called includes,
    in some they are masterpages and contentplaceholder, but they are all the same:
    Reusable components of HTML.\n\nI agree that we use lots of colors in the CSS
    today. The thing is, many of those can be abstracted away with alphatransparent
    PNG-images. If we only could get rid of IE6 they would be really usable.\n\nUsing
    CSS-constants like Anders suggests would be really useful, I agree!'
  comment_date: '2008-10-01 00:50:01'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '1'
- comment_ID: '31244'
  comment_author: Henrik Lissner
  comment_author_url: http://henrik.lissner.net
  comment_content: I do like the idea of CSS constants, but I do sympathize with Bert.
    However, I don't agree with the idea of having to develop per-language solutions
    for a CSS variable alternative.\n\nIt sounds like you're saying we should be developing
    parsers on a per-language basis. But why not make it a pre-deployment step?\n\nI
    have made my own custom solution, a quick 'n dirty php script that parses and
    rewrites my css files en mass. Done locally of course, and the result is uploaded.
    No need to do any active parsing.\n\nJust my 2 cents! Cheers!
  comment_date: '2008-12-02 08:52:45'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '31246'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Henrik Lissner: That is an interesting idea. The only bad thing
    about it I can see is that it must be a mess to maintain for people. If you''re
    using generated code you better give away your generator, and the original file
    too. Perhaps a website with your generator that people can use? That could in
    fact be a rather good solution for now.'
  comment_date: '2008-12-03 01:27:11'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '1'
- comment_ID: '31248'
  comment_author: Henrik Lissner
  comment_author_url: http://henrik.lissner.net
  comment_content: '@Emil: Yes, I did put that into consideration when I first thought
    it up. What I ended up doing was I set up a private web service, to which the
    CMS''s I''ve developed POST full stylesheets and receive the rewritten version
    (subsequently replacing the local stylesheet).\n\nThe problem comes when someone
    doesn''t get the CMS, but wants to alter their CSS files, but they usually come
    back to me in those cases; so I haven''t had to address that need just yet.\n\nI
    suppose I could simply put up a form on my site that could post to that web service.
    Just some food for thought.\n\nMaybe when the project becomes more mature I will
    make it public.'
  comment_date: '2008-12-03 04:35:28'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '31348'
  comment_author: Shane
  comment_author_url: ''
  comment_content: I think the issue not about using variables, but rather about having
    the ability to define named constants. The arguments that you make about setting
    the same margin values over and over again are a cry for named constants. There
    is a place for these in any language, stylistic (as in css) or otherwise. Given
    that numeric constants (numbers) were created to replace the more vague concepts
    of one, a handful, more than handful, many, more than many, etc, the use of named
    constants to allow for quick and easy manipulation and maintenance of an otherwise
    complex system just makes sense.
  comment_date: '2009-01-04 13:17:10'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
- comment_ID: '31783'
  comment_author: 'Variablen in CSS: Werkzeuge und Lösungsansätze | Dr. Web Magazin'
  comment_author_url: http://www.drweb.de/magazin/variablen-in-css-werkzeuge-und-losungsansatze/
  comment_content: '[...] das Design von Cascading Stylesheets mittels Variablen zu
    erleichtern und zu beschleunigen. Die Vorteile liegen auf der [...]'
  comment_date: '2009-06-09 08:11:45'
  comment_post_ID: '171'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '36739'
  comment_author: Kristoffer Nolgren
  comment_author_url: http://www.facebook.com/kristoffer.nolgren
  comment_content: Unless you have already, you should look in to \nhttp://sass-lang.com/tutorial.html\n\nIt's
    a helper that supports nested css, variables etc, it works seemlessly and ofc.
    wont effect performance.\n\nI LOVE the work you're doing on kundo btw!\n\nKristoffer,
    resihop
  comment_date: '2011-02-06 01:02:00'
  comment_post_ID: '171'
  comment_type: null
  is_admin: '0'
---
