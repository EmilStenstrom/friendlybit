---
comments:
- comment_ID: '7940'
  comment_author: Cerebral
  comment_author_url: http://www.cere.be
  comment_content: Good to know. Do you know another site than PIE(maybe you should
    contact them to add this one to their list) which gathers all those IE6 bugs ?
  comment_date: '2006-11-27 22:55:35'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '7946'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Cerebral: Good idea, I have a lot of these little bugs in my
    posts, I''ll contact them.'
  comment_date: '2006-11-28 00:45:13'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '1'
- comment_ID: '7985'
  comment_author: Adam
  comment_author_url: http://www.ctrlfreak.com
  comment_content: 'I''ve come across this before and found that:\n\n<code>\na:hover
    {\n⇥cursor: pointer;\n}\n</code>\n\nalso works.'
  comment_date: '2006-11-28 18:03:01'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '8006'
  comment_author: Cerebral
  comment_author_url: http://www.cere.be
  comment_content: Yeah I found this one too ;-)
  comment_date: '2006-11-28 23:07:14'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '8017'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Adam: Seems that setting almost anything on a:hover works.'
  comment_date: '2006-11-29 01:15:17'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '1'
- comment_ID: '8123'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: There is another IE bug with links. I already posted it on several
    sites, but this seems to be ignored.\nAs you know, inside any anchor (a element)
    there may be any text or html inline element, and anything which is rendered visually
    then becomes clickable and should lead to the destination referenced by the href
    attribute. Not so with the IE. Just try to put a button inside the anchor. The
    destination is shown in the status line, but clicking on that link does nothing.
    This is a bug in the most basic and important feature of the web.
  comment_date: '2006-11-30 12:26:43'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '8130'
  comment_author: Rasmus Kaj
  comment_author_url: http://www.stacken.kth.se/~kaj/
  comment_content: This feels somwehat related to the fact that IE6 ignores :hover
    on elements other than a ...\n\nIs that fixed in IE7?
  comment_date: '2006-11-30 15:08:47'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '8147'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: Siegfried, a button inside a link is invalid, and HTML4 does not
    define what should happen when you click on a button that is inside a link, so
    no behavior is wrong.
  comment_date: '2006-11-30 23:37:17'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '8421'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rasmus Kaj: Sorry for not answering until now. I don''t think
    they are related. IE probably does not even generate an event for mouseover on
    anything other than links, and I doubt that''s the problem here.'
  comment_date: '2006-12-04 20:18:43'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '1'
- comment_ID: '24031'
  comment_author: Arne
  comment_author_url: http://www.arnekolja.com
  comment_content: It seems that this fix doesn't work for all combinations. At least
    when using adjacent sibling selectors the fix doesn't work.\n\na:hover + .nextElement
    { display:block; }\n\ndoes not work in IE6, no matter what I am trying. Have you
    got a tipp how I could get this running with IE6?
  comment_date: '2007-05-08 14:06:26'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '24036'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Arne: That''s easy, IE6 does not support the adjecent sibling
    selector at all. You''ll have to use javascript for that... Annoying, isn''t it?'
  comment_date: '2007-05-08 18:46:19'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '1'
- comment_ID: '24143'
  comment_author: Arne
  comment_author_url: http://www.arnekolja.com
  comment_content: Yes, but it isn't just annoying, it's really corrupting the web...
    this crappy browser... :-(\n\nI really hope that systems with OS' "below" Windows
    XP will disappear soon, as we can assume that in the world of Windows XP we will
    at least see a great migration from IE6 to IE7 this year. Doesn't solve all the
    problems, but the most annoying ones I think. Microsoft should only be more rigorous
    in distributing the new version... and yes, to users of illegal versions too,
    as they are a great amount of windows users at all. So if they really want to
    help us developers and the web itself they should make possible to update to IE7
    without genuine authentication I think. I think it's a better choice to help the
    web than to manage excluding illegal versions...
  comment_date: '2007-05-11 18:55:20'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '24317'
  comment_author: Roger Gordon
  comment_author_url: ''
  comment_content: 'Thank you so much for this sanity-saving fix. I''ve spent the
    last 6+ hours trying to figure this one out with no luck. It works perfectly now
    with\na:hover {paddding-top: 0;} applied.\nMuch appreciated, and I agree that
    you should contact the guys over at P.I.E with this bug, as I couldn''t find a
    solution to this problem there.'
  comment_date: '2007-05-16 11:22:14'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '27886'
  comment_author: Jared
  comment_author_url: ''
  comment_content: '@zcorpan\n\n\n  Cancel\n\n\nIs valid and has the same problem.'
  comment_date: '2007-09-28 01:22:08'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '33518'
  comment_author: raetsel
  comment_author_url: ''
  comment_content: thank you for this! :)\ni just wasted so much time trying to fix
    this exactly :)
  comment_date: '2010-04-27 20:41:36'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '33892'
  comment_author: '?E6 sorunu: Ba?lant? içi elemanlarda hover sorunu &laquo; CSS Feed'
  comment_author_url: http://www.cssfeed.net/?p=26
  comment_content: '[...] <a href="http://friendlybit.com/css/ie6-bug-ignored-selector-hover-bug/"
    rel="nofollow">http://friendlybit.com/css/ie6-bug-ignored-selector-hover-bug/</a>
    [...]'
  comment_date: '2010-05-29 21:44:59'
  comment_post_ID: '107'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33905'
  comment_author: gavin
  comment_author_url: ''
  comment_content: thank you :)
  comment_date: '2010-06-05 14:07:05'
  comment_post_ID: '107'
  comment_type: null
  is_admin: '0'
- comment_ID: '33970'
  comment_author: Nethizmet Online kütüphanesi
  comment_author_url: http://www.nethizmet.tk/css/ie6-sorunu-baglanti-ici-elemanlarda-hover-sorunu/
  comment_content: '[...] <a href="http://friendlybit.com/css/ie6-bug-ignored-selector-hover-bug/"
    rel="nofollow">http://friendlybit.com/css/ie6-bug-ignored-selector-hover-bug/</a>
    [...]'
  comment_date: '2010-07-15 22:14:12'
  comment_post_ID: '107'
  comment_type: pingback
  is_admin: '0'
---