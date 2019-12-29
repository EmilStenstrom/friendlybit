---
comments:
- comment_ID: '31225'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: Well, object is not new at all. It worked this way at least since
    html 4. I'm not quite sure about html 3.Although the IE... But that's always the
    same.\n\nThere is 1 thing to mention when "including" html via object. The included
    page is a full html page. It may contain links. By clicking on one of those links
    only the embedded page changes. This may be useful, but in other circumstances
    not what you want to.\n\nGenerally including html is not a _that_ good idea. It
    is a security risk. You know including html via iframe? You know that mainly russian
    criminals include invisible trojans mainly via iframe? Including html in some
    other way opens more risks.\n\nThere is a common mechanism including html snippets
    (f.ex. a navigation menu) on the server side, called SSI (server side includes).
    No need for php or the like. The page is still delivered as a full html page.
    This feature was especially meant for including repetitive parts like navigation
    menues, footers and the like.
  comment_date: '2008-11-29 16:36:19'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31226'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Siegfriend: I had no idea it currently worked in Firefox, Opera
    and Safari (just tested). Unfortunately, it''s currently unusable for several
    reasons. I''ll update the post with more info about my findings.\n\nAs you say
    linking is a problem area that needs to be changed for this to be usable. Added
    it to the list at the bottom.\n\nIt''s not a security risk, you can either include
    things on the server or on the client, it''s equally secure. Including russian
    spyware HTML is stupid, I agree.\n\nSSI is a language just like PHP and the other.
    It''s not better in any way.'
  comment_date: '2008-11-29 17:17:57'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '1'
- comment_ID: '31229'
  comment_author: Rasmus Kaj
  comment_author_url: http://rasmus.krats.se/
  comment_content: An object is a separate object, it may be an image, a flash video
    or a java applet.  Or a html page, or anything else your browser can handle.  But
    it is a separate object, the contents of the object is not part of the DOM tree
    that contains an object.\n\nI think changing this for the special case of including
    html in html would be unfortunate.\n\nIt is, of course, possible to do such inclusion
    with javascript, but I still think baking ready-made pages on the server side
    is better.  The learning curve of plain old server side includes is very flat,
    and it can be enabled in practically every server there is.
  comment_date: '2008-11-29 22:41:03'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31234'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rasmus Kaj: Would it be better if it''s a separate tag? Not object?
    In the spec linked, there already is a section that spells out the special rules
    for each type of data, the HTML one is empty.\n\nFor beginners, learning includes
    is often all they need. You can build a perfectly fine site with just that little
    tool. Problem is, it''s different in every language, and often a hassle to get
    working (if you''re not a hacker like most of us). \n\nI believe the advantages
    of this outweighs that the models gets a little bit different for HTML includes.'
  comment_date: '2008-11-29 23:25:20'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '1'
- comment_ID: '31237'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de/
  comment_content: 'Hi,\n\ni''m currently (for development and testing) using a vrml
    object. This is a full 3D description format. If there is no vrml plugin available,
    i need a fallback.\n\nOne possible fallback would be a series of screenshots,
    navigatable by mouse clicks. So the fallback is not a simple image, but a html
    file, containing that image and an image map. Since the effect should be somewhat
    similar to the original vrml, clicking on a part of the image should only change
    that image. Exactly this is done by including this html file via object. \n\nSo
    at least for me i consider this objekt behaviour useful. I''d not like to change
    it.\n\nO.k. SSI is a language like any other. But SSI can only do 1 thing: Including.
    So it is extremely more easy to learn than f.ex. php.\n\nFor xhtml there may be
    more options. You can f.ex. use xsl. And xsl allows for including. And more, xsl
    allows for building the page at the client side. In this case you don''t even
    need xhtml, just xml+xsl. And xml itselt offers mechanisms for including (<a href="http://xml.silmaril.ie/authors/includes/)."
    rel="nofollow">http://xml.silmaril.ie/authors/includes/).</a> \n\nSo, although
    i think html 5 is a useful intermediate step, the next real step is still xhtml
    (and maybe simple xml). It offers many benefits.'
  comment_date: '2008-11-30 10:10:56'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31238'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de/
  comment_content: 'Ah, just 1 thing more: You know that building a web page of independent
    blocks would slow down page loading? And thus lowers page performance? Each independent
    block would need a separate http request. Although with caching this may result
    in faster loading then. But that depends on caching. And i know many (too many)
    sites disallowing cacheing.\n\nSo building a page out of parts would be be-fold.
    It may be an advantage, but, if not well designed, may be a disadvantage.\n\nFor
    the development process on the other side it would indeed be an advantage, no
    doupt.'
  comment_date: '2008-11-30 10:17:25'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31239'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Siegfried: Concerning the fallback: You could use an object tag,
    with an iframe inside it that works exactly like you said it would. Frames do
    contain the clicks inside them.\n\nYes, I could use XSL I guess, I just don''t
    like that language. Again, it''s a new language people have to learn... And although
    this one works on the client side, it''s still not enough for beginners I think.
    Good idea though, you really know your way around web technologies.\n\nAbout performance:
    Yes, this would need more http-requests initially, and fewer for subsequent pages.
    If developers feel this is too much of a performance hit, they can keep on using
    server-side includes instead.'
  comment_date: '2008-11-30 12:11:17'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '1'
- comment_ID: '31241'
  comment_author: Anders Ytterström
  comment_author_url: http://madr.se
  comment_content: It would be awesome! It would be a killer argument for not using  frames
    and iframes isntead of learning template languages.\n\nNo decent web developer
    writes HTML without includes or variables anyway, so to make it a part of the
    spec only seems reasonable to me.
  comment_date: '2008-11-30 23:33:17'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31245'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: You should check out the &lt;iframe seamless&gt; feature and its
    friends in HTML5.
  comment_date: '2008-12-02 09:46:50'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31247'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@zcorpan: Thanks, iframe seemless does exactly what I''m looking
    for. Hoping to see the first implementation soon! I''ve updated the post.'
  comment_date: '2008-12-03 01:37:07'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '1'
- comment_ID: '31277'
  comment_author: Stevie D
  comment_author_url: ''
  comment_content: I'm surprised it doesn't work in IE - I <em>used</em> to use [object]
    elements in my website (although not wrapped in a [figure] element), and that
    certainly worked in IE5 and IE6. It didn't look pretty, but it worked - up to
    a point.\n\nI stopped using [object] when I got my head round SSI, which is a
    much more effective way of achieving the end result. OK, so it doesn't allow cacheing,
    but everything else works better - it looks neater, fewer HTTP requests, fewer
    bytes if the user only looks at one page, easier to maintain, and solves the problem
    of search engines calling up the object data page as a stand-alone.
  comment_date: '2008-12-08 14:46:07'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31300'
  comment_author: Alon Peer
  comment_author_url: http://blog.alonpeer.com
  comment_content: One more issue that you have to think about before using this is
    SEO.\nA search engine's crawler needs to "know" that it needs to look into the
    HTML include file and count the text in it as part of the original page and not
    as a different one. Otherwise your website's pages might not be indexed correctly
    (i.e. if you have all of your main menu links inside such an include).\nSearch
    Engines (well, Google...) must first learn to deal with these includes before
    I will start using them. Until then it's PHP includes only.
  comment_date: '2008-12-09 23:52:46'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31305'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Alon Peer: Agreed, search engines really need to understand this
    before people will start to use it widely. \n\nBut even without that it could
    be immensely useful for prototyping things, or why not an intranet? Things that
    won''t necessarily need to be crawled.'
  comment_date: '2008-12-10 21:50:00'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '1'
- comment_ID: '31306'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Stevie D: You don''t happen to know exactly what you did to make
    it work in IE? I''d love to see an example. \n\n"Everything else works better":
    I don''t agree with that (especially not neatness), and I''ve given my arguments
    "pro seemless" in the article.'
  comment_date: '2008-12-10 22:26:56'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '1'
- comment_ID: '31323'
  comment_author: Stevie D
  comment_author_url: ''
  comment_content: What I used was\n<code>[p][object data="sourcefile.htm" type="text/html"
    height="..." width="..."][a href="sourcefile.htm"]Link to source file[/a] for
    browsers that don't support object element[/object][/p]</code>.\n\nIt definitely
    worked in IE5.5 and IE6, although it looked ugly as heck.\n\nI'm surprised you
    and Alon are talking about how it messes up Google. I had always understood that
    the page was served whole - the browsing agent wouldn't be aware that some of
    the code was sent by SSI include. Google would just see the final page, as your
    browser would, with the included code, erm, included with all the rest of the
    code.\n\nWhy do I think it works better to use SSI?\n\n* Neatness - because SSI
    drops a page fragment into the document flow, you can style it seamlessly with
    the rest of the page. Object elements have to have the size specified, which often
    results in scrollbars and ugly borders.\n\n* Capability - SSI allows you to insert
    any document fragment, it doesn't have to be a stand-alone object or set of elements,
    it could end mid-element if that serves your needs better! Object elements don't
    give you that flexibility.\n\n* Search resilient - because the included fragment
    is only ever served as part of the parent page, search engines treat it as though
    it was part of that page. With object elements, you have the risk that spiders
    won't read or index pages/fragments linked through the object element, won't treat
    them as part of the main page (for ranking and context purposes), and will return
    them as results in their own right, which means that surfers can be directed to
    a fragment page that probably doesn't answer their question and may not work as
    a self-contained page.\n\n* Accessibility - because SSI is all done server-side,
    all the user agent sees is the completed page, so if your coding is up to scratch,
    it's accessible straight away. Object elements are not supported by all user agents
    - some old browsers and, I suspect, mobile phones and assistive technologies,
    don't read object elements, so you have to include alternative content and remember
    to change it as needed, which is a headache to maintain, and adds to the bytes
    transferred. There is also the worry that, even if the user agent does render
    the object elements, features such as tabbing to links and fields may not work
    as intended or in the correct order.\n\nFrom reading the [iframe seamless] bit
    on HTML5, it sounds like they are just reinventing what we've already got with
    SSI, but relying on user agents to treat the included content in the manner specified
    (do we really want to do that?), whereas with SSI it is guaranteed. The only advantage
    I can see to using any form of [object] or [iframe] element is to allow cacheing
    of the included file, but is that really all that important these days?
  comment_date: '2008-12-15 14:56:41'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31365'
  comment_author: Rob
  comment_author_url: ''
  comment_content: Yes an object would allow you to include pages within HTML pages,
    however this has serious implications for search engines. Content within objects,
    frames and iframes might look right in a browser window, but search engines will
    not be able to view and parse your content.\n\nUsing PHP or ASP only requires
    one additional line of code to include another page such as a header or footer.
    You don't have to master an entire programming language at all.
  comment_date: '2009-01-11 16:23:20'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31367'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rob: Search engines would have to update their algorithms, just
    like browsers would. Nothing says that Google can''t make two requests to a website
    instead of one. (Minor note: please don''t use your company name as the name,
    that''s spamming).'
  comment_date: '2009-01-11 20:32:38'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '1'
- comment_ID: '31443'
  comment_author: Mikael Lundin
  comment_author_url: ''
  comment_content: What about <a href="http://en.wikipedia.org/wiki/XInclude" rel="nofollow">XInclude</a>?
    Is there any valid reason for the bad browser support of this technique?
  comment_date: '2009-02-07 13:48:41'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31444'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Mikael Lundin: I''ve never seen that one, which probably is one
    of the explainations for why it isn''t supported: People don''t know about it.
    I''m hoping for the most probable solution that will do what I listed in the article:
    and to me, that''s HTML5.'
  comment_date: '2009-02-07 16:32:47'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '1'
- comment_ID: '31445'
  comment_author: Mikael Lundin
  comment_author_url: ''
  comment_content: The difference is that XInclude would need a pre-parse before the
    DOM is loaded, and that  is an element in the DOM. XInclude is transparent to
    JavaScript. IFrame is not.\n\nXInclude is not intended to be used in HTML, but
    rather in XML and I actually found it useful when dealing with XML on the server
    side, and one time including data into a NAnt script :)\n\nIf the browser supports
    XHtml I can't see why it should not also support XInclude since it comes from
    the same family. There seems to be some support in IE7, and I guess thats because
    of the XSL-support in that browser. \n\nWell, that's my two cents anyway.
  comment_date: '2009-02-08 10:24:44'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
- comment_ID: '31450'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Mikael Lundin: Thanks for the explaination!'
  comment_date: '2009-02-13 17:59:49'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '1'
- comment_ID: '33306'
  comment_author: Jegan
  comment_author_url: http://www.srisoftwarez.com
  comment_content: Thanks for the code which works in all the Browser.
  comment_date: '2009-11-30 09:03:56'
  comment_post_ID: '320'
  comment_type: null
  is_admin: '0'
---