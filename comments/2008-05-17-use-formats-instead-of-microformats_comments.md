---
comments:
- comment_ID: '30590'
  comment_author: Nick Dunn
  comment_author_url: http://nick-dunn.co.uk
  comment_content: I see your point, but I think you're overlooking one of the fundamental
    advantages of using microformats. On the vast majority of occasions, the data
    you want to expose to machines is already available in the HTML.\n\nTake hCard
    for example. If you want to provide a basic vCard, then it's likely your contact
    page already contains your name, telephone number and e-mail address. Why copy
    this information into a separate file just to expose it to machines? Don't Repeat
    Yourself, surely.\n\nSimilarly with hAtom (marking up blog-type content), this
    saves having to create separate functionality for creating syndication feeds for
    RSS1, RSS2.0, Atom, plain XML and so on. You have your data marked up once, and
    it can be parsed and converted as appropriate. This is where some microformat
    XSLT parsing would be very useful.\n\nTechnically speaking, with my contacts example,
    if the details were stored in a database then generating a vCard file from this
    data would alleviate the data-duplication issue. However not all sites run from
    a CMS and very often this information is buried in the HTML.\n\nThat's the simplified
    beauty of microformats.
  comment_date: '2008-05-17 13:31:22'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30593'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Nick Dunn: Thanks again, great comment. I agree that if your
    contacts are buried inside a HTML chunk, it''s somewhat easier to make them a
    hCard than a vCard. But it''s not <strong>that</strong> much easier. Not storing
    important information like contacts in HTML of course gives you lots of other
    extras too.\n\nvCards are very rarely made by hand, so it wouldn''t be repeating
    oneself. Rendering machine data from a machine makes more sense to me.'
  comment_date: '2008-05-17 14:09:34'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30595'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: 'reals formats versus "microformats" is nonsense.\n\nBesides that
    vCard is indeed a long existing format that should be used. And there is already
    a proposal for that. It is part of the RDFa proposals (see http://www.w3.org/TR/2006/WD-xhtml-rdfa-primer-20060516/
    ). But RDFa is for XHTML, not for HTML. So, to say it short: Microformats hCard
    is for now, RDFa/vCard is for the (near?) future.'
  comment_date: '2008-05-17 16:33:09'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30601'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Siegfried: If you throw out that the whole article is "nonsense",
    I at least expect some arguments. My article is full of them, your comment only
    talks about RDFa. Better arguments please.'
  comment_date: '2008-05-18 11:33:54'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30602'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: 'No! I just said that "real formats versus microformats" is nonsense.
    There is no "versus". And exactly for that i already wrote arguments.\n\nTo repeat
    it: Embedding vCard in xhtml the correct way is via RDFa. But that is limited
    to xhtml. It is not possible for html. So embedding vCard the RDFa way is for
    the future, embedding hCard into html is for now. Both methods have their usage
    and their place. So there is no "versus". As long as you stick to html, you have
    to stick to hCard. As soon as you switch to xhtml you have the option to switch
    to RDFa/vCard. \n\nIn the title of this article there are two nonsense points.
    First is claiming some "versus" between microformats and vCard. Second is implying
    that microformats is no "real" format. It is a real format the same way RDFa is.
    \n\nThe remainder of the article is mostly correct. And i agree that vCard is
    the way to go - in the (near?) future.'
  comment_date: '2008-05-18 17:01:02'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30603'
  comment_author: Gert
  comment_author_url: ''
  comment_content: Personally I've never understood the statement that microformats
    are "design for humans first, machines second”. I feel indeed it's the opposite.
    Speaking of hCalendar, you put a human readable event date on your page. In the
    background you add the microformat in the HTML. But I like it. And tools like
    the Operator extension for Firefox, or Optimus, make it perfectly usable.
  comment_date: '2008-05-19 08:16:23'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30604'
  comment_author: Pelle
  comment_author_url: ''
  comment_content: The reasons to use microformats is that you without any additional
    effort can make the computer understand existing content on a page.\n\nSure -
    it needs spans or other tags but the content would most of the time be printed
    on the page anyway so adding a tag that makes the computer understands doesn't
    take much of an effort.\n\nAnd by the way - hCards opens as vCards very easily.
    Check out Operator, Tails and Microformats bookmarklets - they all export as vCards.\n\nReal
    formats are good - they are better than microformats. But microformats are better
    than nothing and doesn't exclude real formats.
  comment_date: '2008-05-19 08:51:00'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30605'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Siegfried: I don''t agree that it''s a nonsense point. It''s
    really about embedding formats in HTML or not. Embedding formats (RDFa or Microformats),
    or linking to formats (vCard or whatever).\n\nDevelopment is about priorities,
    and I agree that adding both would be a good idea. Real world examples contradict
    that though, people that use microformats withdraw from making data available
    as non-embedded formats.\n\n@Gert & Pelle: Firefox extensions make them usable,
    but far too few people use them to motivate a developer to implement them. A big
    search engine like technorati could of course crawl and search for them, but even
    then: crawling for non-embedded formats would be easier.'
  comment_date: '2008-05-19 15:41:41'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30606'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: The by far most widespread "browser" is the IE. The IE does not
    understand XHTML (if you properly deliver it as application/xhtml+xml). So consequently
    the majority still sticks to HTML. Embedding Microformats in HTML is straightforward
    and has at least some basic rudimentary acceptance. So Microformats can already
    be used today. RDFa is limited to real XHTML (because of the namespaces). As you
    can see at the start of this comment, it does not make much sense to deliver productive
    pages as XHTML. So for such sites you have Microformats, nothing else. XHTML/RDFa
    is for early adopters which plan for the future already today. These are very
    vew people. They indeed should switch from Microformats to RDFa. And somewhen
    these few early adopters then will have an advantage. \n\nBut there will be very
    much water going down the Rhine river until we reach that day. Just consider that
    the majority of the web designers of today still stick to the concepts and methods
    of HTML 3.2. Even if they use the HTML 4 doctype they still code and design likeback
    in the old days of HTML 3.2. So don't expect the adoption of semantic markup,
    in what standard ever, too soon. And if there will be some minor adoption of the
    bare idea of web pages having not only a "look", but also a semantic, the first
    step will be small. And microformats allows for the smaller first step.
  comment_date: '2008-05-19 19:53:17'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30608'
  comment_author: Sarven Capadisli
  comment_author_url: http://www.csarven.ca
  comment_content: 'Emil, you (and others) have a lot of misconceptions about microformats.
    Give this a read: http://www.csarven.ca/microformats-misconceptions \n\nor check
    out the principles, goals, criticism or faqs on the microformats Wiki: http://microformats.org/wiki\n\nHope
    that helps.'
  comment_date: '2008-05-20 07:55:48'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30609'
  comment_author: Jesse Skinner
  comment_author_url: http://www.thefutureoftheweb.com/
  comment_content: I guess Microformats could let you practice DRY (Don't Repeat Yourself).
    You could have your contact details on a contact page, mark it up with hCard format,
    then let people download a vCard generated from the hCard using a service like
    http://suda.co.uk/projects/microformats/hcard/
  comment_date: '2008-05-20 11:04:15'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30610'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Siegfried: I too think RDFa is a better choice for the future.
    This article isn''t about that though. It''s about embedded vs. standalone formats.\n\n@Sarven
    Capadisli: Instead of mindless self-promotion, tell me what I''ve misunderstood.\n\n@Jesse
    Skinner: Well, perhaps DRY is a reason, could be. But wouldn''t it make sense
    to not store contact information some other way than in a HTML chunk in your database?
    And if you generate a vCard from that, there''s very little reason to do hCard
    too.'
  comment_date: '2008-05-20 22:32:05'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30612'
  comment_author: Sarven Capadisli
  comment_author_url: http://www.csarven.ca
  comment_content: 'Mindless promotion? I beg to differ. If you feel that it is so
    "mindless", please remove the links. Believe me, I''m neither looking for a promotion
    nor need your site to do that if I choose to do it. I was merely trying to help
    you.\n\nIf all the comments above telling you that your views are incorrect because
    of pre-misconceptions, perhaps it is time to learn what microformats is really
    about or what it is really trying to solve at the end of the day. In any case,
    the fact that you don''t like microformats (or perhaps feel that you are left
    behind and trying to make up a case for it) shouldn''t get in the way to educate
    yourself on it. Don''t expect people to give you all answers if you are not willing
    to put the time to learn.\n\nBut for the sake of the argument, I can point a few
    more things about your post that''s wrong on top of the above comments:\n\nMicroformats
    is not trying to replace existing formats. It is a way to use existing formats
    in (X)HTML. Whether you want to use a separate file to keep track of a vCard or
    not is totally up to you. Note that, since you are already writing HTML, you might
    as well use certain names in your HTML that match those in widely accepted standards.
    Because that way, you can pull off a vCard by having a single instance for the
    data. Are you huffing about names like "entry_title" being useless and you rather
    go for "my_foo_title" instead? What''s the problem? If you are going to use a
    name you might as well use a standard name and have the advantage of parsers being
    able to understand your document among others. Maybe you don''t want to do that.
    That''s your call.\n\nYou are thinking code bloat? You need to learn about writing
    HTML on different environments and how they differ at the end of the day. Cases
    where you need to move code around or keep consistency and define things on a
    granular level. Above all, maintenance. microformats can lead you in that direction,
    if, of course, you choose to understand how to make use of it in your own work.\n\nTechnorati
    is not in charge of microformats by any means. Many formats have been developed
    after XFN and still being researched and developed by an open community. I take
    slight offense to this because I contribute my share. Believe me, the discussions
    are a lot more complex then anything under this URL. It caries out analysis and
    constructive feedback from the community.\n\nYou''ve clearly missed the point
    of "design for humans first, machines second". The idea is to mark "visible" data
    that we are already providing to humans so that the machines can also understand
    them. The tags and attributes that you speak of is a way to do that. It is like
    focusing on "social tagging" instead of meta-keywords. Can you guess why meta-keywords
    is dropped in favour of social tagging? microformats favors visible data as opposed
    to meta-data, keep that in mind.\n\nmicroformats is not a new language nor is
    it trying to revolutionise the way we work. It is a step in the right direction.
    It will not solve all our problems but it will get us 80% there because it is
    pretty reasonable right now. microformats is not competing against RDF(a). They
    are meant to solve a similar (but quite different) problem in a different way.
    If you want to cover your "Semantic Web"ness, perhaps microformats is not for
    you. If you want to have a way to provide a way for machines to understand it
    on the existing Web then microformats is for you. You also need to understand
    the state of the Web though. Don''t expect to go from zero to "Semantic Web" over
    night. microformats can help you bootstrap it though.\n\nConsider this a freebie.
    Now go read about it instead of making uneducated claims because you are adding
    noise to the Web without doing proper research.\n\n(This comment form is not very
    user friendly: dimensions of the container is too small for a comfortable writing.
    I am actually typing this out in a text editor and will paste it back.)'
  comment_date: '2008-05-21 03:37:43'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30613'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: 'O.k., if this artikle is not about embedded formats but about
    standalone formats then the title at least is not nonsense (though still i do
    not agree). Your artikle was fuzzy about that. \n\nO.k., HTML, or, in the (hopefully
    near) future is _the_ web format. Instead of tons of proprietary and very different
    formats in tons of files it is indeed better to have them embedded into a single
    file. The main advantage is that this could then be used simply by humans by simply
    reading it. It could be used by humans that even do not know of vCards and the
    like. You could just sit down in front of the monitor, take a pen and paper and
    write down that telephone number to call that person. You could try that with
    vCrard, too. And if you know enough about computer data you probably will succeed.
    But the average noob is far better off with a visually appealing nice web page.\n\nOn
    the other hand embedded data can be extracted by programs to automatically enhance
    usability and usefulness of that information. You could still write down the address
    information on paper and then add it to your e-mail client manually. But is adds
    to usability if the computer does it for you by a simple click. \n\nAdditionaly
    this information, let''s say an address information, is, if embedded into a web
    page, within a context. The address information is part of the complete information
    of that page. If you extract that address information, you get a naked address.
    For what purpose is this address? Why do you have it? The vCard data format profides
    no information about that. A web page does. This contextual information is completely
    lost when you extract this piece of data. \n\nOf course you may _link_ to that
    standalone data from your web page. This has advantages and disadvantages. The
    context is not available ad hoc as when embedded. But you get an immediate access
    to a format ready to use, without some program involved. To combine both, i have
    done both on my impressum page. I have the address information on the page marked
    up with hCard, and have alink to a pre-done vCard file. Often, it''s not a question
    about this _or_ that, but best practise would be to offer both.\n\nBTW: Since
    i''m already offer my pages in HTML and XHTML, i''m currently working on switching
    the XHTML files to RDFa while still using Microformats on the HTML versions :)'
  comment_date: '2008-05-21 08:38:55'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30614'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Sarven Capadisli, Siegfried: Thanks for your replies, I''ll reply
    later tonight (and also fix the narrow comment area, I agree that it sucks).'
  comment_date: '2008-05-21 11:55:27'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30615'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Sarven Capadisli: Sorry for the harsh tone, my guess is that
    you get as annoyed by me not understanding you, as I get when people don''t understand
    me. \n\n<ol>\n<li>I know what microformats are for, and I know what they are trying
    to accomplish (I don''t need a FAQ or RTFM). Thanks anyway for typing it down
    here.</li>\n<li>Replacing. They are not meant to replace formats, but they do.
    Very few sites that use microformats do also implement their corresponding "real"
    format. That''s what this whole article is about, and that''s also what everyone
    is misinterpreting. I''ll update the article.</li>\n<li>No one said technorati
    was in charge of anything.</li>\n<li>Thanks for the ending rudeness, we''re even.</li>\n</ol>'
  comment_date: '2008-05-22 00:19:01'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30616'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Siegfried: Yes, it was fuzzy about that, I''m sorry, will add
    an update at the end of it explaining.\n\nI see what you mean, and what you''re
    getting at, but I still don''t agree. One thing you''re saying is that the future
    is one format. But webpages of today already consist of many different formats.
    We have HTML, XSS, JS, PNG, JPG, SWF, and so on. Each format has a certain specific
    thing it accomplishes and it does it well. Other file types the user get to decide
    what to do with. If you click a vCard file you get a friendly Outlook "add contact"
    window. It works, for real users today.\n\nGood point about context, I didn''t
    think about that. As you say, it''s a bit harder for machines to resolve things
    based on links, but they probably still will have to do that across different
    pages.\n\nI agree that doing both, as you have on your impressum page, is the
    best way to do things right now. But if one of my clients gives me a couple of
    hours and asks me to make their contact information page more usable by ordinary
    people, I''d still pick vCard. First.'
  comment_date: '2008-05-22 00:29:34'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30617'
  comment_author: Sarven Capadisli
  comment_author_url: http://www.csarven.ca
  comment_content: Emil, I reacted, I apologise.\n\n(Implementing all those corresponding
    "real" formats, is not easy. Othwerise, we'd see it more often. Implementing microformats
    is simple and we let the scripts to do that extra work for us. This is trying
    to solve a real world problem and it is not meant to solve all problems either.)
  comment_date: '2008-05-22 03:02:10'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30622'
  comment_author: Thuy
  comment_author_url: ''
  comment_content: 'I don''t have time to read the entire discussion here, but I''m
    confused. I just started learning how to use microformats. I thought the purpose
    of microformats was to display information on a web page (so humans have instant
    access to it) and then provide the option to download a vCard (so humans can manipulate
    this useful information with a machine).\n\nAm I misunderstanding this? Is there
    a way to display a vCard directly on the page? I thought the point of microformats
    was to get the best of both worlds: microformats can be manipulated by machines/programming
    while not requiring extra interaction from the user.'
  comment_date: '2008-05-22 17:50:14'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30626'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Thuy: You are right. The problem is that very few people have
    the browser extensions needed to convert microformats to "real" formats.'
  comment_date: '2008-05-22 20:55:37'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30629'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: 'Hmmm, well... :)\nJust to be precise: I do not think that there
    will only be one format. This one format, html, will just be the one main container.
    Just as it is a container for formats like jpg, gif and png (and others). Embedding
    these formats is simple, well known and approved. \n\nNow about embedding other
    formats. Or not embed it but link to it. These are the 2 options you have. If
    you embed it, you have to adapt it to what is possible in your container. The
    container is html. If you do that, you have the information immediately embedded
    into a web pages whole context. There is no need for any human to do anything
    additional to see this information and to recognize it within its context. The
    drawback is indeed that you need some extra computer functionality to get that
    information in this standalone format. This is why microformats per se are not
    very useful. They become useful if there are functions to extract and convert
    them.\n\nIf you do not embed them, but link to them, the advantage is that you
    get the information directly (well, mostly direct, you have to do an extra klick)
    in the format usable in your programs. That is nice, and you do not need any script
    snippet to extract that for you. But the information is out of context. And there
    is an extra action needed for the human in front of the computer. \n\nSo both
    have its advantages and disadvantages. And i think, we both agree that the best
    way would be to offer both to combine the advantages of both while getting rid
    of the disadvatages. But then it is still no "versus" between both methods. \n\nAnd
    last point: I personally think that for the future we will have one basic format
    for all kind of meta data: RDF. This could be very well embedded into xhtml, and
    it could as well be a perfect standalone format. So with rdf you have a format
    combining the advantages of all we have today.'
  comment_date: '2008-05-23 08:19:00'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30638'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Siegfried: We both agree that the first priority is to supply
    both. I still think that if you have to chose one, you should pick the external
    format instead of the embedded one. Good summary of the two options you have.'
  comment_date: '2008-05-24 00:33:10'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30641'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: :)\nI'd prefere the embedded version. But this is indeed debatable.
  comment_date: '2008-05-24 08:50:52'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30661'
  comment_author: Stephanie
  comment_author_url: http://sillybean.net/
  comment_content: <q>The problem is that very few people have the browser extensions
    needed to convert microformats to “real” formats.</q>\n\nTrue enough. However,
    they don't need to. Technorati provides a service through which HTML authors can
    generate vCards from hCards by adding a few parameters to a link. It's relatively
    simple (especially with an example to work from) for semi-trained authors to use.\n\nRather
    than an end to microformats, which are so easy to create, we need more format
    conversion tools like Technorati's service -- preferably open source scripts that
    can be run locally.
  comment_date: '2008-05-28 17:21:33'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30667'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Stephanie: Or they could render a vCard themselves, if that''s
    the intent they''re after. vCards are clickable today, without the need for a
    third party service. I don''t think usability is the main argument for microformats,
    it might be in authoring (you can easily make a hCard in your existing CMS!).'
  comment_date: '2008-05-29 10:34:53'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '1'
- comment_ID: '30668'
  comment_author: Stephanie
  comment_author_url: http://sillybean.net/
  comment_content: For people who aren't running a CMS -- and you wouldn't believe
    how many university departments still use plain old HTML files, often authored
    in an ancient copy of Dreamweaver or even FrontPage -- creating a vCard is an
    intimidating process. They understand how to write HTML.
  comment_date: '2008-05-29 15:54:39'
  comment_post_ID: '161'
  comment_type: null
  is_admin: '0'
- comment_ID: '30674'
  comment_author: Your Internet Classroom | Coffee on the Keyboard
  comment_author_url: http://coffeeonthekeyboard.com/your-internet-classroom-95/
  comment_content: '[...] a great example of someone who does get involved, check
    out Emil Stenström’s post about microformats. He’s the cool prof who likes to
    engage you in a discussion, will support his theories and [...]'
  comment_date: '2008-05-30 16:45:03'
  comment_post_ID: '161'
  comment_type: pingback
  is_admin: '0'
---