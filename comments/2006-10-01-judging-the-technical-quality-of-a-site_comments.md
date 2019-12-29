---
comments:
- comment_ID: '5327'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: 1. Try to navigate the site with keyboard. I normally do this anyway.\n\n2.
    Disable images. Still accessible?\n\n3. Disable CSS. Still accessible?\n\n4. Disable
    JS. Still accessible?\n\n5. Have a glance at the markup to see if there is correct
    use of semantic markup.
  comment_date: '2006-10-01 04:05:22'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5329'
  comment_author: Sean Fraser
  comment_author_url: http://www.elementary-group-standards.com
  comment_content: I view source of every new site I visit and, on occaision, I'll
    revisit the source code of established sites. It's only on established sites that
    I perform <em>The Stenström Qualitative Test</em>. :-) \n\nI add "written content"
    and "scripts used" measurements as well.
  comment_date: '2006-10-01 04:48:13'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5336'
  comment_author: jarvklo
  comment_author_url: ''
  comment_content: I also view source on most new sites I encounter - especially sites
    advocating some sort of "best practices"...\n\n... and the code of this site is
    littered with practices contradicting what is described in the article.\n\nIMHO
    setting a good example by actually practicing what is preached is one of the most
    important issues for any standards / best practices advocate  sites out there.\n\nI
    mean - If us standardistas don't bother making our own site living up to the  standards
    and practices we preach - why should anyone bother to listen to what we are saying
    anyway?
  comment_date: '2006-10-01 11:43:24'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5339'
  comment_author: dk
  comment_author_url: ''
  comment_content: is this something that you try to follow by yourself when hacing
    up the html/css? :)
  comment_date: '2006-10-01 12:52:55'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5340'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@zcorpan: Good additions! #5 is in my list too :) Is your list
    the only thing you check or a compliment to my points?\n\n@Sean Fraser: Heh, nice
    name :) Could you describe your two tests a bit more?\n\n@jarvklo: Could you expand
    on what problems this site has? I know the markup and CSS is much better than
    most sites out there but you seem to not agree. I''d love to hear some <em>constructive
    criticism</em> on this. You can find my e-mail on the contact page...'
  comment_date: '2006-10-01 13:41:08'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '1'
- comment_ID: '5345'
  comment_author: Jarvklo
  comment_author_url: ''
  comment_content: Emil - For what it's worth I think your markup is just fine - I
    simply meant that you seeemingly contradict what you're saying in this article
    and tha that might not be a good thing...\n\nYou advocate semantic coding, yet
    this site is built using code like \n<blockquote>\n&lt;div class="h1"&gt;&lt;a
    href="http://friendlybit.com/"&gt;&lt;span&gt;Friendly Bit&lt;/span&gt;&lt;/a&gt;&lt;/div&gt;\n</blockquote>\n...
    which isnt't very rich in semantics for a site header.\n\nYour CSS doesn't currently
    validate... yet you make a point twice that validation is important.\n\nYou advocate
    that only "mediocre sites" use classnames like "wrapper" - yet your site uses
    no less than three wrappers named wrapper1, wrapper2 and wrapper3... and I fail
    to see how the code of this site could be considered mediocre.\n\n\nMy point is
    - still - to point out that the impression that comes across since the guidelines
    you advocate in the article (seemingly) are not important enough for you to make
    your own site live up to your own standards might be contradicting what you're
    trying to accomplish with the article in the first place... ;)\n
  comment_date: '2006-10-01 16:51:42'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5346'
  comment_author: Jarvklo
  comment_author_url: ''
  comment_content: '... oh and by the way, your comment editing mechanism seems to
    be broken ;)'
  comment_date: '2006-10-01 17:00:20'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5347'
  comment_author: Denny
  comment_author_url: http://ircinfo.ru
  comment_content: 'First of all I view text for using quotation marks and dashes:
    laquo and raquo instead of "" and mdash instead of - is a good signal.'
  comment_date: '2006-10-01 17:14:46'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5353'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jarvklo: ok, that puts it in another light. The markup for my
    header is using .h1 because &lt;h1> is used for the article title. I couldn''t
    repeat the header but I certainly should use another class name. This page didn''t
    validate becuase you didn''t close your blockquote :)\n\nThe CSS only validates
    if you add profile=css21 to the url. It''s a part of the clearfix method of clearing
    floats. That''s very different from saying that the site doesn''t validate. It
    does.\n\nAbout my wrappers. Each and every element on the page is needed, ther''s
    little gradients, tricks to make faux columns work,  source ordering, and so on.
    So belive me when I say that every wrapper is needed. About the naming: since
    they are needed to do design things, they have no semantic value, and no semantic
    value means there is not good way to name them. Currently I belive the current
    compromise is what works best.\n\nSo, from my own point of view I do follow the
    highly set standards I advocate.\n\nThe comment function is not broken, it''s
    just my caching mechanism that does not update the page until after one hour.
    Or do you mean some other error? Please be specific.\n\n(Btw, your feed is not
    validating either ;)'
  comment_date: '2006-10-01 20:58:18'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '1'
- comment_ID: '5354'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Denny: Why is that important? From what I know about those they
    are language specific, and rather annoying to write without the correct keyboard
    (I use a swedish one). What is the proper one to use for english?'
  comment_date: '2006-10-01 21:00:06'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '1'
- comment_ID: '5356'
  comment_author: Denny
  comment_author_url: http://ircinfo.ru
  comment_content: '2Emil Stenström: yes, you are right, they are language specific
    and these &raquo; and &laquo; are for russian language (that is why my English
    is so bad). I think, we should use a double prime " for computer languages or
    as an inch symbol, but not for text. It is so important, because it''s syntax/spelling
    right.\n\nI prefer web sites without grammar mistakes (In my opinion they are
    trustworthy) like books (most of them with correct quotes and dashes, especially
    which were make up without computers).\n\nYes, it''s difficult to use special
    characters, because there are no such symbols on keyboard. So I use mnemonic abbreviations
    for them mdash; &laquo; and &raquo; (last pair are for russian texts).\n\nIn English,
    AFAIK, better to use &ldquo; and &rdquo; for quotes and &mdash; for dashes (dash
    it is not hyphen or minus!).\n\nAlso about quotes you can read in last ALA article
    QTAG: http://www.alistapart.com/articles/qtag'
  comment_date: '2006-10-01 22:22:34'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5365'
  comment_author: Jarvklo
  comment_author_url: ''
  comment_content: <blockquote>(Btw, your feed is not validating either ;)</blockquote>\n\nEmil
    - I don't advocate "best practices" for feeds. I use Feedburner and delegate that
    to them so I just won't take you up on that obvious flame-bait ;)  \n\nAs for
    the comment editing mechanism...\nYour site somehow managed to mangle the closing
    blockquote, and then refused to accept several attempts to rectify the situation.
    You've got my email-address if you're interested about further details.
  comment_date: '2006-10-02 00:43:37'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5378'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Denny: thanks for the clairification.\n\n@Jarvklo: Only a comment
    on the parantesis? If that was a flamebait, yours was too.\n\nOk, I will have
    to look at the comment mechanism, I''m using the wordpress default though...'
  comment_date: '2006-10-02 10:43:59'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '1'
- comment_ID: '5388'
  comment_author: Sean Fraser
  comment_author_url: http://www.elementary-group-standards.com
  comment_content: 'Sure.\n\n"Written content" and "Scripts used" - for me - are both
    subjective and objective. The objective aspects remain within your <em>Technical</em>
    guidelines; subjective aspects are not technical but affect my perception of the
    qualitative state of a site.\n \nWritten content.\n\nObjective example: How do
    they present apostophes, ampersands, single quotes and double quotes in editorial
    content. Subjective examples: Does the site have a current copyright date. Are
    there typographical errors.\n\nScripts used.\n\nObjective example: Dreamweaver-generated
    scripts. Subjective example: What purpose does the obstrusive display of script
    behaviors serve, e.g., Web 2.0 Ajax on everything imaginable.\n\nAfter applying
    your guidelines, I - Readily - admit that my site is mediocre but then I doubt
    it will ever be <em>Semantically</em> correct. I prefer "plynth" over "footer".'
  comment_date: '2006-10-02 17:18:20'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5395'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: You want XBL2 for the wrapper divs... :-)\n\nMy list is complete.
    If a site passes my check list then it's a quality site, regardless of whether
    it passes validation or not (though it probably does).
  comment_date: '2006-10-02 23:41:00'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '5491'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: Oh, I might have forgotten one point in my list. If the site uses
    anything that requires plugins (like Flash) then disable plugins and check if
    the content is still accessible.
  comment_date: '2006-10-05 12:14:30'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '24294'
  comment_author: tom barnfield
  comment_author_url: http://www.runninghead.com
  comment_content: Great site, love the design. I don't bother with accessibility
    much myself as  it's more of a moral imperative than a commercial one, nice to
    see I meet most of your other standards though. I'm trying to learn everything
    regarding CSS and XHTML. I've made a page to collect all my gathered knowledge
    so far. Take a look at the source code if you get time, would appreciate your
    comments. Absolute beginners might find it useful as it's kind of a help sheet
    for a mate too. \nhttp://www.runninghead.com/aaa_Templates/centeringTemplate2.html
  comment_date: '2007-05-15 19:04:05'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '33843'
  comment_author: Co oznacza termin “dobra” strona? &laquo; Blog o ciekawostkach informatycznych
  comment_author_url: http://neonot.wordpress.com/2010/05/15/co-oznacza-termin-dobra-strona/
  comment_content: '[...] Co oznacza termin “dobra”&nbsp;strona?  15 05 2010   Jest
    to jeden z moich ulubionych tekstów, bardzo zwi??le mówi?cy o tym, jak pozna?
    si? na programi?cie/webmasterze strony – artyku? pt. “Judging the technical quality
    of a site”: http://friendlybit.com/tutorial/judging-the-technical-quality-of-a-site/
    [...]'
  comment_date: '2010-05-15 20:33:27'
  comment_post_ID: '95'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '36155'
  comment_author: Gregory
  comment_author_url: http://www.softxml.com
  comment_content: Technical quality of the website is only of interest to web developers
    and less to search engines for purpose of organic rankings.\n\nRegular website
    visitors are not interested in this kind of data but with some useful content
    they can read.\n\nTechnical quality can come into the play when you propose web
    development services to others. In this case you must have your own website made
    according to these rules.
  comment_date: '2010-12-28 15:05:45'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '0'
- comment_ID: '36301'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: I don't agree. Regular website visitors benefits from good code
    in that the page works in their browser, no matter what that browser is. If you
    start making up your own HTML, you will soon realize that browsers parse it differently,
    which means different visitors get a different experience... not a good thing
    (mostly).
  comment_date: '2010-12-30 14:08:21'
  comment_post_ID: '95'
  comment_type: null
  is_admin: '1'
---