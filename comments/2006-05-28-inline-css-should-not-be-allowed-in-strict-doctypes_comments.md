---
comments:
- comment_ID: '901'
  comment_author: Sarven Capadisli
  comment_author_url: http://www.csarven.ca
  comment_content: Perhaps it would be ideal to dynamically apply a selector to the
    element instead of an inline style.\n\nHowever inline styles seems to come in
    handy as a quickfix, where it may be more costy to apply the styles on an external
    stylesheet?\n\nTo answer your question, why the proper inline styling in Strict
    doctypes is better then transitional inline styling.. well, one can still easily
    remove styling from the markup without actually touching the HTML components.
    It is a minor separation in affect, but still containerizes styling as supposed
    to mixing markup and styling on the same level.\n\nHaving said that, I agree,
    although inline styles are allowed, they should be discouraged for use in Strict
    doctypes.
  comment_date: '2006-05-28 23:16:26'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '902'
  comment_author: Dennis
  comment_author_url: http://www.checkengineusa.com
  comment_content: Good point, Emil. Your example is a good illustration of why inline
    CSS isn't much of an improvement. Sarvin makes a good point, too, in that inline
    CSS is good for a quick fix only, which I have been guilty of once in a great
    while. Hopefully if a web developer is smart enough to use XHTML strict, he will
    not be writing inline CSS.
  comment_date: '2006-05-29 03:53:59'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '907'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Sarven: A "quickfix" sounds just like throwing in a little table
    here and there. I also don''t agree that we are dealing with "minor separation".
    The style attribute is embedded design, nothing else.'
  comment_date: '2006-05-29 09:04:38'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '914'
  comment_author: Ara Pehlivanian
  comment_author_url: http://arapehlivanian.com
  comment_content: Not even in the case where you're doing Image Replacements for
    multiple languages and are dynamically pointing to different images based on the
    locale that's available as a variable in the page?\n\nThen again, I suppose you
    *could* write a dynamic stylesheet that would contain all of the style rules w/
    variables (i.e. in a .php file).
  comment_date: '2006-05-29 20:36:31'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '918'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Ara Pehlivanian: The point here is that you want separation of
    design and content. How is adding an image with style separation? I agree that
    it''s harder to do it without using style but isn''t that a typical transitional
    page? \n\nLike you say, most of the problems can be solved with a dynamic CSS-file,
    that is, <em>dynamic design</em> instead of <em>dynamic content</em>.'
  comment_date: '2006-05-30 12:21:07'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '958'
  comment_author: karl
  comment_author_url: http://www.la-grange.net/
  comment_content: 'Use Case.\n\nWysiwyg environment: \nCut and Paste (with style)
    from one document to another one.\n\nHow do you move the style context?\n\nIt''s
    not that easy. :)'
  comment_date: '2006-06-02 03:10:01'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '965'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@karl: I would say it <em>is</em> that easy. Are you saying that
    it should be ok to embed style in content because it''s hard to do otherwise programmatically?
    Transitional certainly sounds like the solution to that problem.'
  comment_date: '2006-06-02 12:47:34'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '1075'
  comment_author: Anne van Kesteren
  comment_author_url: http://annevankesteren.nl/
  comment_content: It's not about DOCTYPEs anymore. They are merely a way of telling
    the browser which rendering mode you want in text/html.\n\nI agree that the attribute
    should not be used though and as far as I know HTML5 does not have it as part
    of the allowed attributes.
  comment_date: '2006-06-06 15:39:48'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1076'
  comment_author: Sarven Capadisli
  comment_author_url: http://www.csarven.ca
  comment_content: Just wanted to reiterate the point of why inline styles are better
    then going ahead with transitional methods (your question); with inline styles,
    styling is still containerized for a given element (just as internal stylesheets),
    and they can be safely removed or altered without touching the actually structure
    of the document. \n\nOn the other hand, with transitional markups, deprecated
    code allows the developer to mess with the 'structure' of the document for presentational
    purposes and surely if they wish to apply any changes, it can be troublesome.
    \n\nProper XHTML [content type, real XML markup (side note to those use trailing
    spaces and then a slash on empty elements.. there is no such thing in XML - such
    convention is introduced to cater older browsers)], enforces this idea of separation
    even further. HTML however, is not as... lets say 'strict'.
  comment_date: '2006-06-06 16:16:17'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1077'
  comment_author: Are inline styles bad? | ara pehlivanian—Web Standards, Web Culture,
    Web Everything.™
  comment_author_url: http://arapehlivanian.com/2006/06/06/are-inline-styles-bad/
  comment_content: '[...] Posted originally as a comment on 456 Berea Street. I had
    also originally posted a comment on this very same topic on Emil Stenström’s Friendly
    Bit [...]'
  comment_date: '2006-06-06 17:57:13'
  comment_post_ID: '65'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1091'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: '<blockquote><p>I hear the obvious reply: “What if I load design
    info from a database? I need to use inline CSS then!”. To me, that sounds like
    a perfect case where you need to go transitional, if you can’t manage to separate
    the two - don’t.</p></blockquote>\n\nWhile I agree with your general notion of
    separating CSS from the HTML, I disagree with the above comment. Naturally the
    <code>style</code> attribute could be removed if every detail in every web site
    out there was handcoded, but as we all know, that''s not the situation. That statement
    means that <em>every</em> site producing dynamic CSS values from a database, or
    basically any CMS in general (not that many of them they''re any good, but work
    with me here... :-)) should use a transitional doctype.\n\nThe perfect solution
    in those cases would to have a style block at the top of the HTML file and then
    an <code>id</code>/<code>class</code> connection,  or maybe even a dynamically
    generated CSS file, but in real-life situations of today that''s rarely not the
    options that are available in most contexts.\n\nHowever, the biggest downside
    about telling people to use a transitional doctype for that fairly minor problem
    is what Anne was touching on above: rendering modes. I would never use a doctype
    triggering a less strict rendering mode just because my situation forces me to
    use an inline <code>style</code> attribute in just one or a couple of cases.\n\nSo,
    in my humble opinion, the idea is good but I don''t think it works all the way
    in real world web developing as it is today.'
  comment_date: '2006-06-06 21:27:57'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1102'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Anne: I believe it is about doctypes still, but that''s another
    discussion. Good to hear about HTML5, that spec really looks good.\n\n@Sarven
    and Ara: I see your point. In my opinion putting style in an attribute inside
    your structure isn''t enough separation. A <code lang="css">&lt;style&gt;</code>
    should be the least separation requirement.\n\n@Robert: I didn''t mean that all
    database driven designs automatically should go transitional. <a href="http://www.456bereastreet.com/archive/200606/why_is_the_style_attribute_allowed_in_strict_doctypes.html"
    rel="nofollow">Like Roger suggested</a>, everything that can be done with the
    style attribute can also be classed and referenced from a style block in the head.
    That''s a solution for all dynamic designs out there and makes for much better
    separation.\n\nAdditionally, transitional does not nessesarily force you into
    a lesser rendering mode, if you use Transitional with an URL you will <a href="http://gutfeldt.ch/matthias/articles/doctypeswitch/table.html"
    rel="nofollow">still get the standards mode rendering</a> across browsers.'
  comment_date: '2006-06-07 08:09:01'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '1106'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: <blockquote><p>...everything that can be done with the style attribute
    can also be classed and referenced from a style block in the head.</p></blockquote>\n\nAbsolutely,
    from a CSS perspective. But what I was going for was the perspective of CMS-driven
    solutions and their likes, the ones we're currently working with, that don't offer
    this support as of today. Real world vs. a protected environment web developing
    (yes, most CMSs are flawed, but that's another story...)...\n\n<blockquote><p>...transitional
    does not nessesarily force you into a lesser rendering mode...</p></blockquote>\n\nThere
    aren't just standards mode and quirks mode out there, there's also something called
    Almost Standards Mode (please read more in <a href="http://developer.mozilla.org/en/docs/Mozilla%27s_DOCTYPE_sniffing"
    rel="nofollow">Mozilla's DOCTYPE sniffing</a> and <a href="http://hsivonen.iki.fi/doctype/"
    rel="nofollow">Activating the Right Layout Mode Using the Doctype Declaration</a>).
    Basically, what this means is that although you get a somewhat standards mode
    rendering with a transitional doctype, you will never get <em>the</em> strictest
    one available.
  comment_date: '2006-06-07 09:18:30'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1109'
  comment_author: Anne van Kesteren
  comment_author_url: http://annevankesteren.nl/
  comment_content: Yeah, you should absolutely avoid transitional DOCTYPEs. They are
    just harmful and encourage you to produce almost standards compliant sites, but
    not quite as you start relying on specific browser quirks.
  comment_date: '2006-06-07 11:22:20'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1110'
  comment_author: Johan
  comment_author_url: ''
  comment_content: what about inline styles added/removed through DOM scripts?\n\nGenerated
    code that is\n\nMost scripts I have seen use styles and not eg classes
  comment_date: '2006-06-07 11:45:01'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1111'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Robert and Anne: Good points, we shouldn''t force existing (flawed)
    CMS:es and the likes into transitional just because the style attribute was a
    bad idea. But, if style wasn''t in the strict doctype from the beginning, perhaps
    we would have had less ugly CMS solutions. \n\nSo, it was a mistake adding it
    but it''s there now and there''s nothing we can do about it. Is that a conclusion
    you can agree with?\n\n@Johan: I belive we shoudl add classes to things instead
    of styling them with inline. Control the design with CSS and the behaviour through
    JS.'
  comment_date: '2006-06-07 12:39:51'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '1113'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: Oh and another thing, is "Almost standards mode" that bad? The
    only difference between that and standards mode is the "layout of images inside
    table cells" <a href="http://developer.mozilla.org/en/docs/Gecko%27s_%22Almost_Standards%22_Mode"
    title="Gecko's Almost standards mode" rel="nofollow">[1]</a>, if you avoid that
    situation you are not relying on bugs.\n\n(and yes, I need to fix the rendering
    of blockquotes in comments, thanks Robert :)
  comment_date: '2006-06-07 12:45:10'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '1114'
  comment_author: Johan
  comment_author_url: ''
  comment_content: Control the design with CSS and the behaviour through JS.\n\nI
    know but using styles or classes does not make that premise any different.\n\n\n\nProblem
    is multiple classes, if I need to change 1 style at the time I need in analogy
    1 class at the time. So i need to remove the last added class to replaced by the
    new one andf so on.
  comment_date: '2006-06-07 13:03:02'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1115'
  comment_author: Johan
  comment_author_url: ''
  comment_content: '... In fact if you mean seperate content and style you have more
    flexibility with classes.'
  comment_date: '2006-06-07 13:04:25'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1118'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: I'm sorry for messing up your comments... :-)\n\nMy take is that
    (most) CMS vendors wouldn't have cared if the <code>style</code> attribute was
    in the specification or not for strict doctypes...\n\nBut basically, yeah. This
    is the current situation and it's what we have to deal with.\n\nAlmost Standards
    Mode is something in Mozilla browsers, but I'm fairly sure Opera has got its interpretation
    of it and maybe Safari as well. By using a transitional doctype you risk different
    rendering in different web browsers (when it comes to image aligning in table
    cell, when using a transitional doctype there will be a different rendering between
    Mozilla browsers and IE, who has only got quirks and "strict" mode).\n\nThe gist
    is that using a transitional doctype might be like opening Pandora's Box, and
    it's definitely not worth it for a simple <code>style</code> attribute... :-)
  comment_date: '2006-06-07 13:17:06'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1120'
  comment_author: Nate
  comment_author_url: http://www.theklaibers.com
  comment_content: Again, as I said on Roger's site - just think about it a little
    bit. I dynamically create stylesheets with PHP and then use the content-type header
    of text/css to render the document (or I could do it on the server end and have
    all css parsed as PHP - either way). This gives me great flexibility. I can declare
    styles as necessary, and build them on the fly according to info from the database.\n\nI
    agree with what both you and Roger are saying on this topic, to me, its no better
    than using your first example with 'bgcolor'. It defeats the purpose of true separation.\n\nI
    come from a programming background and the MVC design pattern - where there is
    a separation of my database model, my business logic, and my display. It would
    be like me adding my logic to the view, simply because it was easier than using
    the controller file. Overall, in the end, it defeats the whole purpose of separating
    the three. Same goes with the css, html, js, etc.
  comment_date: '2006-06-07 14:58:17'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1125'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Robert Nyman: you''re probably right about the CMS vendors. What
    annoys me though is that those using only the style attribute for design and can
    brag about being strictly compliant. \n\nConcerning almost standards mode, <a
    href="" title="Activating the right layout mode..." rel="nofollow">the page you
    linked to</a> both Mozilla, Opera and Safari have it and they treat it the same
    way. Since it only affects images inside tables I would say it''s safe to use
    (Of course we shouldn''t recommend it though).\n\n@Nate: Yeah, that''s also a
    good solution... you have to be careful though so you don''t miss out on proper
    caching, one of the benefits of external CSS files. \n\nI like the MVC view on
    things, but I''m sure the people that wrote the specs had that in mind too.'
  comment_date: '2006-06-07 20:09:42'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '1126'
  comment_author: Anne van Kesteren
  comment_author_url: http://annevankesteren.nl/
  comment_content: That page seems incomplete. There are other differences as well.
    For example, at some point we had special comment parsing only for standards compliant
    mode because people mess that up all the time. (Now all that is changed, so that
    is more or less reverted I guess.)\n\nFWIW, triggering the right layout mode is
    in my opinion more important than validation. Even if style="" was disallowed
    in strict mode you certainly shouldn't be starting to use a transitional DOCTYPE
    just to validate.
  comment_date: '2006-06-07 21:07:51'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1131'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Anne: Perhaps pull some strings for documentation of the differencies
    in Opera between the different modes? Could be useful for some.\n\nAbout switching
    to transitional, as I said, I take that back. Even though style="" should be there
    it isn''t right now and we have to live with that.'
  comment_date: '2006-06-08 01:24:18'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '1136'
  comment_author: Johan
  comment_author_url: ''
  comment_content: http://www.quirksmode.org/blog/archives/2005/07/benchmark_tests.html
  comment_date: '2006-06-08 08:34:08'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1137'
  comment_author: Johan
  comment_author_url: ''
  comment_content: My end conclusion is styles  \ncan be useful to change the appearance
    of a element when using JS/DOM to do that. In the quirksmode article it states
    that using styles on heavy scripts that class is faster. But for one simple element,
    I dont see the advantage of using classes. This is not all of course ...\n\nFor
    styling an element (static) by using only HTML and the CSS to style it. Of course,
    styles are not used often. Thought to make one change in a page, it is extremely
    handy. You dont have to create an extra class for just implementing one style.\n\nDoctypes
    that use the strict doctype are better coding practices to make the layout work
    crossbrowser and futureproof.\n\nBut if you need to use depreciated elements,
    you cannot use strict since it wont validate.\n\nI think it is very important
    to go further the standard way but you also have to take in account the past which
    is transitional or styles. Not everyone codes the same way.
  comment_date: '2006-06-08 08:45:13'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1138'
  comment_author: Andrew Vit
  comment_author_url: ''
  comment_content: 'Without inline styles, how else would you override a stylesheet''s
    class/id styles using JavaScript to create behaviour on elements? You still need
    a way to set attributes on an element directly, whether the inline style is spelled
    out in the source HTML or created dynamically. \nAlso, sometimes the style is
    actually the content. Semantically, if you are presenting color swatches, the
    content is the color: it should not be defined anywhere else but directly on the
    element of the content.\nAlso, in some cases you may need to style something which
    is a one-off unique element that cannot be classified or otherwise has no reason
    to be identified except for some very local stylistic reason. Trust me, clients
    are like that sometimes... Not having inline styles would require us to identify
    these elements and create separate style definitions for them when all we actually
    want to do is break out of the norm for one specific case.\nRegardless of doctype,
    inline styles are quite necessary. The fact that the styles are formalized into
    a single style attribute without separate color/align/bgcolor attributes is really
    what makes it "strict" in my opinion.'
  comment_date: '2006-06-08 09:14:05'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1143'
  comment_author: trovster
  comment_author_url: http://www.trovster.com
  comment_content: Andrew, you shouldn't add style attributes with JavaScript, you're
    then mixing style and behaviour. Instead, you should add classes/ids and reference
    them in the stylesheet. Not ideal in a few cases, but the majority of the time
    that's the best solution.
  comment_date: '2006-06-08 11:33:16'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1147'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Johan: the benefit of not using style="" is separation. If we
    start recommening that for single changes (to the DOM or directly) we could as
    well suggest bgcolor or something similar. \n\nAlso, "handy" shouldn''t be an
    argument for it: tables are indeed handy for equal height columns but we still
    work hard to use CSS instead.\n\n@Andrew: I agree with trovster here, adding style
    from javascript is no better than mixing content and design. Switch between states
    with classes instead.\n\nYour example with color swatches is an interesting one
    and so are all examples where the design is acctualy the content. I''m not sure
    how to handle that, perhaps style has use in that case... You could of course
    use an image then (in the colro swatches case a php script could use GD to make
    a 1px thing).\n\nFor one-off cases you simply use a style block on your head where
    you define your style. That way it''s still separated from the content. I do not
    believe style="" is separated, attributes apply to the element they are inside
    and that''s where the separation breaks.'
  comment_date: '2006-06-08 13:06:16'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '1286'
  comment_author: sunshine
  comment_author_url: ''
  comment_content: I agree with Andrew and Anne. I understand the argument but from
    a objects point of view... \n\n(x)html elements can have style (unlike xml), therefore
    (x)html elements should have a style attribute). \n\nIf not then we get class
    names like "blueborder" or "superbold" for those semi-rare (unless you work with
    my clients) but existing instances where you want to apply style completely arbitrarily
    and there is no good structure descriptor. \n\nIt seems that html elements may
    not be <em>purely</em> structural just because they can "own" style... heck they
    are styled by default. Yes people should use the style attribute wisely but I
    don't believe it should be removed it from the spec.
  comment_date: '2006-06-10 19:41:36'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1287'
  comment_author: sunshine
  comment_author_url: ''
  comment_content: Also it's a slippery slope to say that style might as well be bgcolor.
    There will always be <em>better</em> ways to do something that still may not be
    <em>perfect</em>. style is more seperation than bgcolor because all of the visual
    stuff is confined to one uniform attribute. Complete seperation, as I mentioned
    before doesn't seem to be something html specs can aim for.. that's why we have
    xml\n\nAlso I apologize for not closing my tag. Could you fix it for me? :)
  comment_date: '2006-06-10 19:47:33'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1290'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@sunshine: I belive we are moving in the direction of complete
    separation. WIth CSS3 we will no longer have to use many of the classnames we
    push in today. The style attribute might be convienient for a few cases, but then
    you move away from the separation strict is all about. \n\nBeing able to move
    a customers idea of what a page looks like to code should be a programming issue
    the CMS solves, not something you use markup for.'
  comment_date: '2006-06-10 20:38:17'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '1442'
  comment_author: Paul
  comment_author_url: ''
  comment_content: Honestly, sometimes it's not feasible to switch out the doctype
    on a single page of a large database driven site. I think that inline styles are
    perfectly valid in a strict doctype. They still conform to all the rules of CSS
    and can be overridden from a global stylesheet by an "!important" delcaration,
    or by a rule which exceeds the inline style's specificity. A sledgehammer is still
    a tool and still has its purpose. I think inline styles are an example of what
    happens when theory hits the pavement, so to speak. ;)
  comment_date: '2006-06-15 08:54:48'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1483'
  comment_author: Matthew Brundage
  comment_author_url: http://mattbrundage.com
  comment_content: Remember that the word "cascading" appears in "CSS". Inline styles,
    while not esthetically pleasing, nevertheless allow for economy of code.\n\nIf,
    for instance, you implement a style that appears only once on only one page, than
    an inline style makes sense. Or, if you find yourself implementing that style
    in multiple areas of your site, then by all means, place it in an external document.\n\nThe
    beauty of CASCADING style sheets is that a style can be implemented on a single
    tag, a single page, or multiple sites, depending on your desired level of specificity.
  comment_date: '2006-06-16 16:35:31'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1618'
  comment_author: Andrew Vit
  comment_author_url: ''
  comment_content: 'Regarding: "I agree with trovster here, adding style from javascript
    is no better than mixing content and design. Switch between states with classes
    instead."\nHow would you then position elements on top of a base layer, say like
    Google Maps? Or make elements draggable? You would really make a new class for
    each possible coordinate? No...\nPlease keep in mind that there exist websites
    that aren''t blogs, where everything is classifiable!'
  comment_date: '2006-06-19 03:45:28'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '1648'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Paul: I belive that it''s a tool that destroys what strict is
    trying to accomplish. It _is_ valid right now, but should it?\n\n@Matthew Brundage:
    That exact argument can be applied to using tables for layout once on a page.
    Economy of code is not all that''s important. You can still apply style to an
    element without the style attrib.'
  comment_date: '2006-06-19 12:10:52'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '2034'
  comment_author: Max Design - standards based web design, development and training
    &raquo; Blog Archive &raquo; Some links for light reading (23/6/06)
  comment_author_url: http://www.maxdesign.com.au/2006/06/23/some-links-86/
  comment_content: '[...] Inline CSS should not be allowed in strict doctypes [...]'
  comment_date: '2006-06-22 17:27:03'
  comment_post_ID: '65'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '2036'
  comment_author: Justin Perkins
  comment_author_url: http://iamjp.com
  comment_content: This is an arguement for purists/philosophers.\n\nTell me how to
    do this without inline styles and I'll bow down...\n\nimportance = 10\n<em>em"&gt;Inline
    Styles</em>\n\n*There is no limit to how important something can be in the above
    example.
  comment_date: '2006-06-22 17:44:49'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '2039'
  comment_author: Justin Perkins
  comment_author_url: http://iamjp.com
  comment_content: That didn't render too well, but it's not important anyway. I know
    you purists are just going to suggest I use dynamic styles and place them in the
    head of the document. I'm sorry but that's simply quite impractical. That sounds
    as silly as not including target attributes in your markup so you can validate,
    only to use JavaScript to add them back.\n\nAs for the arguement that JavaScript
    should not be changes the style attribute of an elment, and instead change a class...\n\nPlease
    explain how this would work with one of the many effects libraries, like Scriptaculous
    or Rico?
  comment_date: '2006-06-22 17:54:21'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '2081'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Justin Perkins: Just to get that out of the way, you shouldn''t
    open new windows. If the user is skilled enough to want it, he will know how to
    open them. Easy as that and no javascript or target needed.\n\nI''m guessing you
    want to add lots of levels of importance to your code, things like a tag cloud?
    Right? That''s dynamic CSS right there which means it''s as much work writing
    it to a CSS class as writing it inline. I perfer not polluting my structure with
    style.'
  comment_date: '2006-06-22 23:31:40'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '2121'
  comment_author: Justin Perkins
  comment_author_url: http://iamjp.com
  comment_content: '&gt; Just to get that out of the way, you shouldn’t open new windows.
    If the user is skilled enough to want it, he will know how to open them.\n\nOk,
    but I''m just trying to equate the anti-new window argument to the anti-inline
    style one. I think they are very similar, philosophically speaking.\n\nSo, we''re
    talking tag clounds (ala Flickr vs. Technorati). If I want to implement a tag
    cloud like Flickr does (imo is the *proper* way to do it), what''s the cost of
    doing it the dynamic CSS class way vs. inline styles. Is it worth it (not just
    to you, but to whoever you are billing/working for)?\n\n&gt; That’s dynamic CSS
    right there which means it’s as much work writing it to a CSS class as writing
    it inline\n\nI''m not buying that argument. Every one of your views (a purist
    like you has to be MVC right?) is passing up dynamic CSS to be stuffed into the
    document head? Talk about muddling up the code!\n\nI don''t see how this:\n<code><em>I
    love inline styles</em></code>\n\nIs worse than this:\n<code>\n<em>I hate inline
    styles</em></code>\n\nIn fact, that is just too ludicrous to even insinuate.'
  comment_date: '2006-06-23 07:23:57'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '2123'
  comment_author: Justin Perkins
  comment_author_url: http://iamjp.com
  comment_content: Sorry, that really sucked.\n\nI posted what I was trying to say
    on my site if you want to see what I so poorly tried to explain.
  comment_date: '2006-06-23 07:35:29'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '2129'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Justin Perkins: Of course I see your point too. Using inline
    styles is easier and <em>there are</em> places where it makes sense. \n\nI would
    implement a tagcloud by picking 10 font-sizes (users won''t notice the difference
    of 100 different levels) and make a class for each one of them. Then set the size
    for each tag to one of the above.\n\nLet''s just agree to disagree on that one.'
  comment_date: '2006-06-23 10:57:19'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '2147'
  comment_author: Justin Perkins
  comment_author_url: http://iamjp.com
  comment_content: I'm with you on that one Emil, great discussion you promoted here
    :)
  comment_date: '2006-06-23 15:47:38'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '2856'
  comment_author: About Web Designing &raquo; Blog Archive &raquo; Inline CSS should
    not be allowed in strict doctypes
  comment_author_url: http://www.aboutwebdesigning.com/2006/06/09/inline-css-should-not-be-allowed-in-strict-doctypes
  comment_content: '[...] Instead, according to friendly bit, the strict doctype requires
    us to define all CSS in a different file. [...]'
  comment_date: '2006-07-07 08:16:33'
  comment_post_ID: '65'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '4068'
  comment_author: Esqueça o atributo style. Estilos inline em doctype strict são resquícios
    do câncer de um passado sem padrões. &raquo; Revolução Etc - Web Standards em
    uma casca de noz!
  comment_author_url: http://www.revolucao.etc.br/archives/esqueca-o-atributo-style-estilos-inline-em-doctype-strict-sao-resquicios-do-cancer-de-um-passado-sem-padroes/
  comment_content: '[...] Seguindo o exemplo de Emil Stenström qual a diferença entre
    os dois exemplos abaixo na sua opinião? [...]'
  comment_date: '2006-08-28 18:08:09'
  comment_post_ID: '65'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '5843'
  comment_author: Pozycjonowanie
  comment_author_url: http://www.profesjonalna-reklama.pl
  comment_content: Max, you shouldn’t add style attributes with JavaScript, you’re
    then mixing style and behaviour. Instead, you should add classes/ids and reference
    them in the stylesheet. Not ideal in a few cases, but the majority of the time
    that’s the best solution.
  comment_date: '2006-10-20 18:07:37'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '10146'
  comment_author: Jeremy Nicoll
  comment_author_url: http://www.seemysites.net
  comment_content: The strict doctype has no relation to whether inline styles are
    used or not.  The main idea of CSS is to separate content and styling, and so
    inline styling is discouraged - but this is something that CSS experts generally
    encourage and has nothing to do with doctypes. In strict mode, inline styling
    is perfectly valid as style is a valid property of most objects.  The only time
    that I ever use inline styling is when I am applying a style to an element that
    I am only going to use once.  Why clutter up my CSS file with something that is
    only going to be used once?
  comment_date: '2006-12-23 04:25:36'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '10231'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jeremy Nicoll: The relation is clear, whether you choose to see
    it or not. Doctypes define what elements and attributes are allowed in a document.
    It could therefore disallow  the style attribute...\n\nWhy you shouldn''t be allowed
    to use it "only once"? Because once rarely stay once when you deal with real world
    websites. If you''ve allowed one step away from the content/style separation you''ll
    easily do more of them.'
  comment_date: '2006-12-23 16:19:33'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '13454'
  comment_author: Sean Fraser
  comment_author_url: http://www.elementary-group-standards.com
  comment_content: When I read this in May I nodded and thought how true. Inline styles
    in Strict should not be done. However. I've recently had the <em>pleasure</em>
    of working on a Strict site where I was not allowed to touch the style sheets
    but given access to the products' HTML content. [Styles sheets were in the CMS
    of the design agency; product pages were client accessible. Don't ask.] I used
    inline styles for new HTML elements. A real world website, indeed.
  comment_date: '2007-01-12 03:45:58'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '13490'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Sean Fraser: I''ve done that too, real world projects sometimes
    require you to work with only inline styles. Thing is, the html of those sites
    are so bad it''s just silly calling them valid anything. You''re in there really
    mixing style and content in worse ways than we did in 1996! \n\nI''ve done the
    same, but I don''t think that''s an argument against removing it.'
  comment_date: '2007-01-12 07:52:06'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '13682'
  comment_author: Sean Fraser
  comment_author_url: http://www.elementary-group-standards.com
  comment_content: 'Emil: I agree: inline styles should not be allowed in Strict documents.
    I found twisted irony in <strong>my</strong> having to do so.'
  comment_date: '2007-01-13 03:59:04'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '24418'
  comment_author: mogens overbeck
  comment_author_url: ''
  comment_content: In my view inline styles *are* actually a good thing, since you
    can use them during the initial markup phase - that's often the way I do it, anyway.
    I mark up, styling as I go, and in the end transfer the css to an external stylesheet,
    so for me it's just a handy way of speeding up the workflow. I see your point
    though, if it wasn't allowed, people would be forced to learn better development
    practices, but I'm not sure I agree that's the way to go about it :o)
  comment_date: '2007-05-19 15:06:38'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '30662'
  comment_author: prezenty
  comment_author_url: http://www.extraprezenty.pl
  comment_content: This is interesting article, I did not it think that it yes. Interesting
    it knew persons about this how much. Sorry if I wrote bad there now my English
    is novice and I do not it write yet good.
  comment_date: '2008-05-28 17:58:09'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '32906'
  comment_author: Alex Design
  comment_author_url: http://tipseri.net
  comment_content: Hello Emil,\n\nI'm sorry for digging up this old post but after
    the release of Firefox 3.5.2 i have a bunch of problems with the inline CSS. \n\nFirst
    of all i have to say that i don't have as much experience as many designers do,
    but i give my best to acomplish my projects. The reason why i'm writing this comment
    is that after the release of the new Firefox version a project of mine shows completely
    different. It's like the inline CSS is ignored or something like this. I wrote
    an e-mail to firefox with this problem but i didn't got any reply.\n\nI hope you
    can help me in this matter because i have no more options. \n\nBest regards,\nAlex
  comment_date: '2009-08-12 13:50:04'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '32909'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Alex Design: Not much have changed when it comes to CSS in the
    latest version of Firefox. My best bet is that you have an error there somewhere,
    and the best way to figure that out is to simply move out all your CSS to an external
    file and validate it. Annoying, but something really should do.'
  comment_date: '2009-08-15 15:39:17'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '32911'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: You were right Emil. Validating the CSS solves my problem. Thanks
    a lot!
  comment_date: '2009-08-17 20:58:09'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '33471'
  comment_author: Oyunlar
  comment_author_url: http://www.oyunyolu.net
  comment_content: You were right Emil. Validating the CSS solves my problem. Thanks
    a lot!
  comment_date: '2010-03-12 23:50:44'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '33853'
  comment_author: Wm Tipton
  comment_author_url: ''
  comment_content: No offense to the author, but frankly I LOVE inline styling.\nI
    use pretty much all 3 types of styling, a external, internal and inline, but I
    use inline more time than not because I like to make each page...and each part
    of a page...unique...and I dont want to have to keep checking back to another
    style sheet file to do it.\n\nIf they ever do away with inline styling, Im going
    back to using cheap software to build my websites.
  comment_date: '2010-05-22 03:00:43'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '33854'
  comment_author: Wm Tipton
  comment_author_url: ''
  comment_content: Why should you want to include design information inside of a document
    that you just explicitly stated would separate the two?\n=============================================\nYoure
    forgetting, friend, that NOT ALL of us WANT to do away with even HTML 'styling'.\nI
    like CSS much better, so Im fine with it as long as I have an alternative, but
    I frankly like being able to style on the fly and not having to keep referring
    back to another huge css file trying to track down where a specific part of the
    code is in that file.\nI prefer having the style code right there on the page
    Im working on.\n\nI use a style.css file typically for things that will be used
    on EVERY page...such as backgrounds, page width and such and such.\n\nWhen it
    comes to the individual page I like having the css ON the page itself.\n\nI dont
    get bent out of shape or write negative articles about people who dont do it the
    way I do...and I really dont think anyone should waste their time worrying about
    how *I* do it...know what I mean ?\n\nwm
  comment_date: '2010-05-22 03:07:29'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '33855'
  comment_author: Wm Tipton
  comment_author_url: ''
  comment_content: What annoys me though is that those using only the style attribute
    for design and can brag about being strictly compliant.\n=============================\nDear
    God man...what difference does it make to YOU ?\nI mean really. Is your life any
    worse off ?\nI honestly think we need to find a hobby or something when I see
    this sort of complaint.
  comment_date: '2010-05-22 03:21:06'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '33857'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Wm Tipton: I guess I struck a nerve there. Thing is, the whole
    idea of strict compliance is to encourage people to remove all stying properties
    from the HTML. It is, you can go read the spec to confirm it. \n\nSo, if the whole
    idea is to promote external stylesheets, why do people that don''t abide to that
    idea get to be compliant?\n\nThis is not about what I like and not, it''s about
    what the spec says. If there was a "Blue compliant mode", I wouldn''t say that
    red pages where valid blue.'
  comment_date: '2010-05-23 12:40:19'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '1'
- comment_ID: '33922'
  comment_author: martin
  comment_author_url: http://dream2reality.co.uk
  comment_content: There is nothing wrong with inline, and there is a good reason
    to use CSS.  Firstly, we do all this separation so that screen readers only read  content
    instead of style.  Also, if you style with css and the reader is visually impaired,
    their own setup will adjust the css accordingly.\n\nInline or external makes absolutely
    no odds to this.  External is useful if you want to use the same styles on multiple
    pages.  Inline is essential for unique pages because you don't want to be drawing
    in several style sheets when you can do everything on that one page and you definitely
    don't want to cloud up your general styles with hundreds of styles that are only
    used once or twice around your many pages.
  comment_date: '2010-06-15 13:26:11'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '33952'
  comment_author: Wm Tipton
  comment_author_url: http://web77.org
  comment_content: "@Wm Tipton: I guess I struck a nerve there. Thing is, the whole
    idea of strict compliance is to encourage people to remove all stying properties
    from the HTML. It is, you can go read the spec to confirm it.\\n==============================================\\n\\nAnd
    it IS removed from the 'HTML' in that HTML wont be doing the styling. Seems simple
    enough.\\nWhat I dont like is for someone who doesnt USE something to say that
    the REST of us should be deprived of it as well. \\nI ONLY use an External CSS
    file for CSS that will apply to MORE than one page. I also use Server Side includes
    where I have code that will also do the same.\\nBut about 80% of my coding is
    very much element oriented and to be robbed of inline styling because someone
    else doesnt like it is, well, communism at its finest. Why dont we just start
    burning books that the rest of us read if YOU dont personally like them ?\\n\\nHaving
    three options for CCS styling means YOU dont have to EVER use inline if YOU dont
    personally like it. That goes for the rest who dont either. I respect that.\\nBut
    its NOT right for you to bash inline simply because YOU dont use it or like it....even
    if you hate it, its irrelevant because no one is FORCING you to use it...kwim
    ?\\n\\nThe whole idea clearly is to use External style sheets where they are LOGICAL....not
    where they are not.\\nI dont want a 100,000 line stylesheet with styling it it
    for every single element in my entire website.\\nMOST of my sites use position:relative
    for my wrapper/container with a LOT of elements being position:absolute within
    that container.\\nI DO NOT want to have to keep jumping back and forth between
    my page and a css file trying to track down EVERY SINGLE element in that huge
    file.\\nWhen its done how *I* do my sites inline is the ONLY way to go...I know
    because Ive tried it both ways and it gets bad really quickly once a few hundred
    absolutely positioned elements are on the site.\\n\\nOn my sites where an element
    is exactly the same every time (rarely happens except for header and navigation
    on my websites) then I toss that stuff into an external CSS file.\\nBut that simply
    isnt much at all and its far easier for me to use SSI's for my navigation to begin
    with.\\n\\nIf they take away inline styling, I'll go back to using crap software
    to design my websites or I'll just stop designing websites altogether.\\n\\nThose
    of you who want to get rid of inline are simply thinking of YOUR manner of site
    design. You arent taking into account that there are a LOT Of us here who dont
    do it the way you do. \\n\\nwm\n33953\t65\tWm Tipton\t0\thttp://web77.org\t2010-07-03
    03:07:18\tInline or external makes absolutely no odds to this. External is useful
    if you want to use the same styles on multiple pages. Inline is essential for
    unique pages because you don’t want to be drawing in several style sheets when
    you can do everything on that one page and you definitely don’t want to cloud
    up your general styles with hundreds of styles that are only used once or twice
    around your many pages.\\n================================================\\nEXACTLY
    !\\n\\nMOST of my webpages (I do webmastering for others also) require that I
    use quite a bit of absolute positioning for a lot of elements on the page. \\nFor
    instance a guy wants a image bumped up 4 pixels and to the right 10 pixels. Well
    that used to throw something else out of place and so eventually I got smart and
    just started using the relative position for the container and absolute for elements.
    So now if I need to bump something nothing else is affected and I can overlap
    images too, which is something this one client likes as well for some of his pages.\\n\\nBefore
    everything on the page had to fall where it wanted to. I had a little bit of room
    for play, but now by using the inline relative/absolute styling I have absolute
    control over everything on my pages right down to the pixel.\\n\\nBut it requires
    that every element be positioned individually and that is a LOT of elements to
    be putting into a separate CSS file that I was driving myself insane with hopping
    back and forth and then sometimes changing  the wrong thing and having to change
    it again.\\n\\nWith inline I know EXACTLY which element is being affected...theres
    no way to be wrong and I dont have to scroll thru hundreds and thousands of lines
    of styling to find the one Im looking for....its right there on the page itself.\\n\\nThis
    really is a no brainer.\\nThose who dont like inline...DONT USE IT :-)\\nThose
    who absolutely require it...like me...just use it and not say a word about it
    to anyone....\\n\\nwm"
  comment_date: '2010-07-03 02:55:25'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
- comment_ID: '33955'
  comment_author: Wm Tipton
  comment_author_url: http://web77.org
  comment_content: I perfer not polluting my structure with style.\n=====================================\nAnd
    that is your prerogative. No one has any business judging your decision in the
    matter AS LONG AS you are not judging anyone else.\n\nCSS removes the need for
    HTML styling. We simply have more than one option for using CSS on a web page.\nIf
    you dont personally like having styling within your HTML, that is great....more
    power to ya. But you shouldnt be allowed to speak for those of use who DO want
    to use inline styling....kwim ?\n\nAnd my question is....HOW are YOU affected
    if *I* use inline styling ?\nIf you are browsing my sites either way the styling
    is going to have the same effect in the browser whether its inline or external.
    The viewer isnt going to know the difference and doesnt need to concern themselves
    with it.\n\nIll be honest here and I mean no offense, but to me this seems to
    be a topic for geeks to have something to complain about. There is no honest reason
    for anyone who doesnt like inline styling and doesnt use it to whine about it....no
    VALID reason whatsoever.\nIf we just admit this fact maybe we can move on and
    all get along :-)
  comment_date: '2010-07-03 05:22:45'
  comment_post_ID: '65'
  comment_type: null
  is_admin: '0'
---