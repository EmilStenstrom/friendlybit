---
comments:
- comment_ID: '4016'
  comment_author: Rowan Lewis
  comment_author_url: http://www.pixelcarnage.net/
  comment_content: 'Hate to disagree, but its not really that hard to use XHTML: The
    tools are there.\n\nFor example, by simply using HTML Tidy on your output, you''ll
    never see a single error.\n\nBut better than that is to use a script that is capable
    of correctly handling user input, creating the right entities and so on. WordPress
    doesn''t do this by default.\n\nThe best thing about using XHTML for me: I can
    do whatever I like with it, I can parse it with an XML parser, or transform it
    with XSLTs.\n\nIts really not that hard, all the tools you need have already been
    written and maintained for years.'
  comment_date: '2006-08-27 16:51:50'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4017'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rowan Lewis: the problem is, do you expect everyone to be able
    to use XHTML? I mean you are clearly a skilled programmer, just as I am, so of
    course we can make it. But W3C markets XHTML as a replacement for HTML, the new
    standard all new document should be written in. I can understand that programmers
    like XHTML, but expecting everyone to use it? I think not.\n\nThanks for commenting.'
  comment_date: '2006-08-27 16:56:19'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4025'
  comment_author: Sarven Capadisli
  comment_author_url: http://www.csarven.ca
  comment_content: I don't think XHTML is as problematic as you and others (including
    myself sometimes) as make it out to be. \n\nWe can expect beginners to use XHTML
    the same way we expect beginners to use any other language. Do we expect the Java
    language to be more forgiving? Why should XHTML be a special case?\n\nThe bigger
    problem is pushing a dynamic set of standards which makes it difficult to adapt
    to. The Web languages are perhaps evolving at a faster rate then the classic programming
    languages since this 'information highway' medium has a wide range of expectations
    for today's requirements.
  comment_date: '2006-08-27 20:58:22'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4029'
  comment_author: draco
  comment_author_url: ''
  comment_content: '@Sarven: Because Java wouldn''t compile if written incorrect but
    HTML will display (properly?) in browsers even if it''s _wrong_ (think quirks
    mode). Browsers are lenient so most web authors couldn''t care two hoot.\n\nAnyway
    I agree that there''s no true reason to use XHTML unless you plan to serve it
    with the proper MIME type and use extras like MathML and the likes, or else why
    restrict your site to 20% of the Internet users? And no point in content negotiation,
    really.\n\nBesides, when XHTML 2.0 eventually appears, it''s not backward-compatible.
    So imho HTML 4.01 (and microformats!) will suffice for now... But I''ve been wrong
    before. ;)'
  comment_date: '2006-08-27 21:51:51'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4030'
  comment_author: Coda Hale
  comment_author_url: http://blog.codahale.com
  comment_content: You can either trust that your users know XHTML and deal with the
    consequences, or you can relieve them of the need to know XHTML by allowing them
    to use humane markup languages like Markdown or Textile for their formatting needs.\n\nI
    mean, you also can't trust your users to construct well-formed HTTP requests,
    which is why you require a browser instead of trying to walk them through opening
    a terminal, launching telnet, etc., and then getting mad when they forget to CGI
    encode their path strings.\n\nXHTML 1.0 is fine, except for the mime type issue
    (thanks IE6!). XHTML 2.0, on the other hand, looks absolutely horrendous, and
    I don't plan on using it. Ever.
  comment_date: '2006-08-27 22:06:46'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4031'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: 'Great comments people!\n\n@csarven: You''re comparing XHTML to
    Java, a language that''s a lot harder to learn than HTML. Beginners learn HTML
    in a week, Java takes one full semester. I see your point but I really don''t
    see any good reasons to force XHTML upon people that already are struggling with
    HTML. Keep it simple!\n\n@draco: Exactly, you don''t even need to be in quirks
    mode. Standards mode code with some minor errors displays fine.\n\n@Coda Hale:
    on a personal basis: yes, I could go through the hassle and make it work on this
    site. Think bigger though, how do you expect to tell beginners about the CDATA
    characters that they have to put around their inline javascript? What about some
    PHP scripter that writes his first guestbook, how will you explain character set
    conversion to him? I really think XHTML is a bad idea for most sites.'
  comment_date: '2006-08-27 22:23:23'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4032'
  comment_author: Coda Hale
  comment_author_url: http://blog.codahale.com
  comment_content: If someone can master the basics of Javascript, I think it's kind
    of silly to worry about exploding their heads with XML CDATA sections. I mean--how
    will you explain the Document Object Model to someone? How will you explain CSS?
    Hell, how will you explain when you can and cannot leave off a terminating tag
    for an element in HTML, and why that's an OK thing to do?\n\n"XHTML is hard" is
    not a good reason to avoid XHTML.
  comment_date: '2006-08-27 23:30:15'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4033'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Coda Hale: All of those examples add another layer of difficulty
    to making a website. CSS and Javascript both takes time to learn. And you don''t
    need to explain why you can skip ending tags, who cares as long as i works? XHTML
    adds another layer of difficulty to _HTML_, a layer that has very few advantages.
    I believe ease of use (HTML is an easy language) has taken the web to where it
    is today. Let''s not throw that away.'
  comment_date: '2006-08-27 23:39:58'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4036'
  comment_author: Kalle
  comment_author_url: ''
  comment_content: Great article! I have used XHTML for a long time now and gotten
    quite used to it but your arguments why it shouldn't be used makes sense. I didn't
    know about HTML 5, looking formward to that.
  comment_date: '2006-08-28 00:45:09'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4037'
  comment_author: Jarvklo
  comment_author_url: ''
  comment_content: Oh well... \n\nBeing "Anti XHTML" seems to be all the rage these
    days... :P\n\n*sight* \n\nIn my opinion HTML and XHTML are equally mature mainstream
    sister technologies and both will most likely  co-exist on the web for a long
    time... \n\nSo what's the point of arguing one way or the other? There are things
    you can do in XHTML that you cannot do in HTML and vice versa...\n\nIsn't it better
    to write comparisons that focus om when to use one over the other instead of ranting
    about one of them ? (sorry Emil, I fail to se anything but a rant here)\n\n\nIf
    I had one wish tonight, it'd be that you allowed yourself to take a deep breath
    and calmly consider the following before you flame me for my opinions:\n\n* XML
    is a good thing on and off the web - right? \n\n* When you know an use XML, XHTML
    could be a logical choice for web pages given that you already know how to handle
    XML - right ?\n\n* If you don't plan to use XML (or if youre not willing to make
    the effort to learn it) - then simply don't use it and go for HTML instead! \n\nAs
    long as you make an informed decision , it doesn't matter what you use  - at least
    as long as your pages are accessible to your focus group (i.e. validate and then
    some :) )
  comment_date: '2006-08-28 00:54:21'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4042'
  comment_author: One Person
  comment_author_url: ''
  comment_content: XHTML is good becuse the syntax of the language is clearer when
    you first learn it (I am a designer). It is also better to have these structural
    languages more similar than have a special case for HTML.\n\nI mean it is up to
    the programmers to make a application / solution that makes XHTML easy to produce
    for non-programmers. CMS or Wysiwyg that works or such.
  comment_date: '2006-08-28 02:44:00'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4043'
  comment_author: Nicole
  comment_author_url: http://blog.websitestyle.com
  comment_content: Well, there are a lot of benefits to people using XHTML in my opinion.
    I think it teaches people to code in the direction that the web is moving with
    all the feeds and online apps and data gathering we have going on. Now, on your
    statement about the javascript and how to serve the XHTML... that's really not
    a major issue. Because IE doesn't properly understand XHTML if its served as xml
    application, then the suggestion (from the W3C and others) is to serve XHTML as
    text for now. In which case, if its served as text, the CDATA issue doesn't exist.
    On the other hand, if you do serve it as xml then you can simply put the javascript
    in an external file and it won't be a problem at all. So, my view is to just teach
    people the easy way - serve XHTML as text.
  comment_date: '2006-08-28 02:59:42'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4047'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jarvklo: Hehe, of course you won''t change your mind on XHTML,
    you have the domain name ;)\n\nYour third point is what I''m getting at. Do we
    need to use XML? The cases where people actually want to embed MathML or SVG on
    their sites are <em>very</em> few. XHTML is just a technical quirk for the 1%
    that needs that stuff. But W3C is not marketing it like that, they want it to
    <em>replace HTML</em>. I simply don''t agree with that.\n\n@One Person: I don''t
    agree there. The only difference between the lanugages that will matter structurally
    to a beginner is that you have to add a "/" to empty tags in XHTML. \n\nAlso,
    why move XHTML generation to the websites when the browsers are already good at
    it?\n\n@Nicole: most people reason like you do, just send it as text. But that
    defeats it''s sole purpose, what good is a language that is made to be parseble
    with an XML parser if you send it as HTML? It''s the very purpose of the conversion!'
  comment_date: '2006-08-28 07:20:54'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4051'
  comment_author: Rowan Lewis
  comment_author_url: http://www.pixelcarnage.net/
  comment_content: Emil, serving XHTML as text doesn't defeat its purpose (unless
    you want the advanced tools) because you should still be validating your output
    every time you change it.\n\nI'm ashamed of the current state of the web, HTML
    lets people think sites like MySpace are ok, and that their code is acceptable
    when in fact it's beyond useless.\n\nThe looseness of HTML was a big mistake,
    it has taken years of progress off the Internet. How? Because more than half the
    time browser developers spend working on their rendering engines is wasted looking
    for ways to support people who are clueless in regard to the standard.\n\nPlus,
    it allowed every man and his dog to "code" a website, regardless of weather it
    followed the standards or not.\n\nHTML has broken the web, XHTML(2) is here to
    fix it.\n\n* Rowan hops off the high horse...
  comment_date: '2006-08-28 11:37:33'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4058'
  comment_author: draco
  comment_author_url: ''
  comment_content: '@Rowan: I hope you don''t think that XHTML is any better than
    HTML in fixing the looseness of the state of code. We have HTML 4.01 Stric t too.
    :-)\n\nXHTML is just a formulation of HTML into XML. No more, no less. I just
    don''t consider having properly-closed tags "fixing the looseness".\n\nI write
    my site in HTML 4.01 Strict and I don''t consider the code pretty tight too.\n\nJust
    my 2cents.'
  comment_date: '2006-08-28 13:12:58'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4059'
  comment_author: draco
  comment_author_url: ''
  comment_content: I'm sorry, I meant "I consider the code pretty tight too." without
    the negative "dont".
  comment_date: '2006-08-28 13:24:26'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4061'
  comment_author: Rowan Lewis
  comment_author_url: http://www.pixelcarnage.net/
  comment_content: draco, yes I do consider it as a fix, however only in browsers
    that support it.\n\nAlso, because HTML allows you to exclude end tags, thats all
    right, what I meant by looseness is lack of semantics and lack of appreciation
    for validation.
  comment_date: '2006-08-28 13:59:02'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4072'
  comment_author: Mark Donohue
  comment_author_url: ''
  comment_content: 'As a programmer, I can certainly see arguments for a more rigid
    standard like XHTML: efficiency, flexibility, extensibility, etc...  However,
    my personal hunch has been that some small part of the motive for XHTML is out
    of haughty resentment by "programmers" over the loss of web development as the
    sole domain of the computer elite in the wake of the internet''s popularity in
    the 90''s.  This is their way of taking back the web and drawing a line separating
    themselves from the rest of the HTML hobbyists: by developing and pushing standards
    that will finally break their stupid sites and <b>BOLDLY</b> announce, "<i>See?</i>
    You''re just not <i>skilled</i> enough to make websites. Only <b><i>WE</i></b>
    may do the web. <i>(Insert smug Conan-style dance here.)</i>"'
  comment_date: '2006-08-28 19:19:30'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4075'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rowan Lewis: I agree that the current state of the web is bad,
    but only form a programming state of view. Isn''t it fantastic that anyone can
    learn how to make a website in a couple of days?\n\nForcing strictness on those
    people is <strong>not</strong> the right way forward, education and voluntary
    validation is.\n\n@Mark Donohue: <strong>AMEN!</strong>'
  comment_date: '2006-08-28 21:34:27'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4100'
  comment_author: Tony Marston
  comment_author_url: http://www.tonymarston.net
  comment_content: The worst feature I have found with XHTML is that it is case sensitive.
    WTF! Introducing case sensitivity is not a solution to any problem that I know
    of, so if it isn't a solution it should not be implemented. In fact case sensitivity
    causes more problems than it solves - it regards  and  as different whereas most
    humans consider them to be exactly the same. This can make debugging very difficult.
  comment_date: '2006-08-29 09:57:24'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4101'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Tony Marston: XHTML is a stricter language, that''s the whole
    idea. I think it''s good practice to use only lower case characters in your tags,
    but what this article is about is that it shouldn''t be forced upon people.'
  comment_date: '2006-08-29 10:03:43'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4109'
  comment_author: Neil Jacques
  comment_author_url: ''
  comment_content: In response to Rowan's comments in particular, surely that's one
    of the most important things about the web - that "every man and his dog" is able
    contribute, and to express themselves for the entire world to see? Surely the
    mechanism for publishing to the web should be as simple as possible, and error
    tolerant, so as to remove as many barriers to the beginner as possible? I can
    see a place for standards such as XHTML &amp; XML - but surely the relative simplicity
    of HTML, far from holding back progress, has made the web the popular and diverse
    place it is today?
  comment_date: '2006-08-29 13:47:35'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4115'
  comment_author: Martin Payne
  comment_author_url: ''
  comment_content: It’s an interesting argument. I’m neither for or against the use
    of XHTML, but I use it because I think it’s the right choice for <em>me</em>.\n\nI
    don’t think it’s unreasonable to expect beginners to learn XHTML, but I think
    what is more important is to make sure they write <em>valid</em> code—whether
    it be HTML or XHTML. The main problem seems to be that the people who are teaching
    web design don’t even know how to do it properly themselves, so their students
    have <strong>no</strong> chance. I’ve seen far too many publications which haphazardly
    mix HTML and XHTML syntax together, with nonsensical tags such as <code>&lt;P/&gt;</code>.\n\nFrom
    the experience of university lecturers, it seems they learned HTML in the mid
    90s, and don’t realise how much things have changed since then…
  comment_date: '2006-08-29 16:13:06'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4118'
  comment_author: Ben Millard
  comment_author_url: http://sitesurgeon.co.uk/
  comment_content: 'I agree fully with Emil. It''s not a new fad to be opposed to
    <acronym title="Extensible Hypertext Markup Language">XHTML</acronym>; almost
    no websites use <code>application/xml</code> or <code>application/xhtml+xml</code>.
    Website developers the world over have already made their preference known: they
    like the <em>friendly</em> behaviour of <code>text/html</code>. :-)\n\nThe additional
    strictness of <acronym title="Extensible Hypertext Markup Language">XHTML</acronym>
    moves the burden of error correction to every author using markup. That would
    make it impossible for people without an unhealthy amount of markup knowledge
    to participate -- a point well made by this article.\n\nIt''s much more practical
    for errors to be handled by a few well-funded browser manufacturers, especially
    since they already have sophisticated error handling.\n\n<acronym title="Hypertext
    Markup Language">HTML</acronym>5 is defining error handling for <acronym title="Hypertext
    Markup Language">HTML</acronym> parsers, as well as for handling common <acronym
    title="Multipurpose Internet Mail Extensions">MIME</acronym> mis-labelling and
    suchlike. This will mean future websites can be highly interoperable <em>even
    if their code isn''t perfect</em>.\n\nThe rennaisance of <acronym title="Hypertext
    Markup Language">HTML</acronym> is good news for all those amateurs blogging and
    browsing the web.'
  comment_date: '2006-08-29 16:24:49'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4119'
  comment_author: Gamermk
  comment_author_url: http://TrulyBored.com
  comment_content: The idea that web standards should apply to beginners is the fundamental
    flaw in your argument.
  comment_date: '2006-08-29 16:33:10'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4126'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: 'Damn people, you''re making the comments more interesting than
    my article ;)\n\n@Gamermk: I''m not saying they should. Web standards is the ideal
    that we should all strive for, not something to force upon people.'
  comment_date: '2006-08-29 20:05:31'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4167'
  comment_author: Sarven Capadisli
  comment_author_url: http://www.csarven.ca
  comment_content: If we let (or rely on) the browsers define and handle errors then
    we are still depending on them regardless of some standard for parsing.\n\nThe
    fundamental idea behind 'Web Standards' is to move away from relying on browsers
    to handle our markup but to pass a markup specification that is consistent, well-defined
    and used by all.\n\nTherefore I believe not moving forward with XHTML is a step
    away from such Standards.
  comment_date: '2006-08-31 03:55:19'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4184'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Sarven Capadisli: So you''re saying that XHTML is more of a standard
    than HTML? \n\nNo matter what language you use you are still dependent on browsers.'
  comment_date: '2006-08-31 21:07:27'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4192'
  comment_author: Sarven Capadisli
  comment_author_url: http://www.csarven.ca
  comment_content: '@Emil Stenström: Browsers handle errors differently between HTML
    and XHTML documents. There could be many versions of an HTML which essentially
    gets to work because the browsers do a lot more interpreting of the document.
    This is not the case in XHTML. Which therefore allows us to rely less on browsers
    but to focus on writing proper documents.\n\nThis is a better Standard to set
    in my opinion.'
  comment_date: '2006-09-01 01:32:09'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4203'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Sarven: And I don''t agree.'
  comment_date: '2006-09-01 08:24:32'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4210'
  comment_author: david
  comment_author_url: http://climaxdesigns.com
  comment_content: '@Mark Donohue, I''ll second Emil''s <b>AMEN</b>'
  comment_date: '2006-09-01 15:57:02'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4214'
  comment_author: Mark Reeder
  comment_author_url: http://www.subliminalfusion.com
  comment_content: Interesting article, but I think you've made a number of completely
    specious arguments. I won't go into it too much, but I don't feel that there's
    no reason to use XHTML if you're parsing as HTML (for me one of the primary reasons
    is that closing every tag you open makes more sense than having a few like &lt;img&gt;
    that you don't close). But that's the least of my disagreements.\nFirst - You
    mention dynamic sites. If you're allowing users to add content, their content
    should *never* break your site, which is why just about every comment system filters
    out tags. If you're not, you're asking for serious trouble.\nSecond - with javascript,
    you shouldn't be using inline javascript at all if you want proper separation
    of content, display and behavior.\nFinally - the argument has been made that it's
    actually easier to teach XHTML than HTML to a beginner because it's more structured
    and gives instant feedback if you do something wrong. How many beginners that
    you know actually validate their code or are even taught to do so?\nWhat this
    all comes down to is that there are two very different approaches (get people
    doing things correctly from the beginning out of necessity - XHTML, or lowering
    the bar and letting stuff that's not quite right get through without complaint
    - HTML). Don't get me wrong, I don't think HTML is going to disappear, however
    I do think that within a few years that it will be considered second-tier/amateur
    in much the same way that table-based layouts are considered today.
  comment_date: '2006-09-01 18:12:02'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4217'
  comment_author: Chad Calhoun
  comment_author_url: ''
  comment_content: Some of the info in that article is relevant, some not...  Things
    like the design working for the author because it displays as he intended probably
    isn't true because more times than not, it doesn't display correctly in one browser
    or another...  Following standards can be a never ending nightmare to deal with
    errors when you have a CMS or comments,  but that's why it needs to be somewhat
    flexible with errors, as it is.    However, having standards and higher degree's
    of compliance is the only way to progress as I see it.  If people don't use the
    standards, browsers won't continue building off them and progressing... everybody
    will do what they want at the time, probably all in different directions
  comment_date: '2006-09-01 19:22:47'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4219'
  comment_author: Just Me
  comment_author_url: ''
  comment_content: All of those examples add another layer of difficulty to making
    a website. CSS and Javascript both takes time to learn. And you don’t need to
    explain why you can skip ending tags, who cares as long as i works?\nHmm...I think
    I might use that same argument to keep using tables for layout...who cares as
    long as it works! Not too mention how much easier it is for the beginners.
  comment_date: '2006-09-01 19:48:25'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4220'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Mark Reeder: Some replies, first: There''s more than tags that
    can break your site. Non UTF-8 characters is a popular one that most systems today
    fail recognising. \n\nSecond: No, you shouldn''t be using inline Javascript. But
    lots of people install premade scripts of different kinds on their site and many
    of them will mean that the site breaks (if inline), or that the script stops working
    (if it uses document.write...)\n\nThird: I''ve thought about that. I feel the
    positive feedback beginners get by seeing something work right away is more important
    than making them produce great code from the start. There''s time for that later.\n\nThanks
    for commenting! \n\n@Chad Calhoun: From my experience beginners rarely care about
    pixel precision or that it works cross browser. I think that''s something that
    could come later.\n\nNote that I am fully pro standards here, the HTML standard.
    I''d recommend anyone to write valid code, and I do it daily at work, I just don''t
    think we should force validity upon beginners like XHTML do it.\n\n@Just Me: Note
    the difference between what a "web professional" is expected to do and what a
    beginner is expected to. My method of teching people is starting out simple and
    giving them lots of positive feedback. Then working on the validity and standards
    bits. Following that track, yes, I think it''s ok telling beginners how to use
    tables for layout.'
  comment_date: '2006-09-01 20:11:30'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4224'
  comment_author: Matt
  comment_author_url: ''
  comment_content: Honestly, HTML is hard enough for users, so the argument that XHTML
    is too much harder is moot. Like someone said before, give your users markdown
    or textile, and filter your dynamically generated markup so it's valid (shouldn't
    you be doing this anyways?). \n\nNeither is HTML easier because it allows a novice
    page designer to see his/her creation more quickly despite errors. This is behavior
    is the exact opposite of what I would say is best, which is to point out the errors
    right away instead of hide invalid markup, which leads to more difficult compounded
    errors later which a novice user would inevitably find more frustrating. \n\nBut
    what's the point of this article if both HTML and XHTML are available to web designers
    and aren't going away soon? My choice of one or the other doesn't affect a novice
    designer one bit.
  comment_date: '2006-09-01 23:22:31'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4237'
  comment_author: Friendly Bit &raquo; 9rules Network Official Blog
  comment_author_url: http://9rules.com/blog/2006/09/friendly-bit-2/
  comment_content: '[...] Friendly Bit strives to be one of the best blogs for easily
    digested info about client side web development. The articles are easy to follow,
    and I’m sure you’ll find something you should bookmark because you learned something
    or you laughed. [...]'
  comment_date: '2006-09-02 04:20:40'
  comment_post_ID: '89'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '4247'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Matt: How does the difficulty of HTML affect that XHTML is harder?\n\nExactly
    how many web site developers have the skill to write a textile or markdown parser
    for their site? A beginner has no chance of doing that.\n\nYou are talking of
    the best behaviour, I''m talking about the one that makes it easy for the beginner.
    Invalid markup is an OK first step, when they''re online and are starting to learn
    more you and I will step in and continue the lecture.\n\nYour choice surely affects
    beginners. An easy way to get a site online is to just copy and paste someone
    elses. If you''re unsure about what to use you check to see what others do.'
  comment_date: '2006-09-02 12:28:42'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4249'
  comment_author: Johan
  comment_author_url: ''
  comment_content: I think it is an ideological dilemma! Standardistas (also the non-programmers!)
    feel XHTML is better because it is stricter and feels more like a standard. But
    that is wrong thinking! Using a STRICT DOCTYPE is the thing that makes HTML 4.01
    strict or XHTML pu t out better code! Eg depreciated tags are not allowed in HTML
    strict and XHTML strict , this is the only thing that matters for now. In the
    far future, no one knows if HTML will still be used? But will that be XHTML?\n\nLots
    of people are confused by this! But basically XML is a descriptive language that
    can describe records/data with self declared tags, I see a better future with
    XML eg AJAX uses XML?
  comment_date: '2006-09-02 16:41:11'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4250'
  comment_author: Johan
  comment_author_url: ''
  comment_content: 'The only thing I dont know for sure: do XHTML parsed pages render
    faster than HTML?'
  comment_date: '2006-09-02 16:43:04'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4251'
  comment_author: Johan
  comment_author_url: ''
  comment_content: Also I think standartistas love the X that stands before HTML.
    It makes them feel they are using Xtra Powers in a new informatica era?!
  comment_date: '2006-09-02 16:47:05'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4255'
  comment_author: Martin Payne
  comment_author_url: ''
  comment_content: '<blockquote cite="http://friendlybit.com/html/why-xhtml-is-a-bad-idea/#comment-4249">\nEg
    depreciated tags are not allowed in HTML strict and XHTML strict\n</blockquote>\n\nNeither
    are deprecated tags… ;o)\n\n<blockquote cite="http://friendlybit.com/html/why-xhtml-is-a-bad-idea/#comment-4250">\nThe
    only thing I dont know for sure: do XHTML parsed pages render faster than HTML?\n</blockquote>\n\nIt
    tends to be slower due to the way in which most (all?) XHTML browsers currently
    work—they download the entire page, check it for well?formed?ness, and only then
    will they render it. HTML browsers on the other hand, will start to render a page
    as soon as it receives data. Of course that doesn’t take into account the time
    it takes to download the associated images, CSS, scripts etc.'
  comment_date: '2006-09-02 21:51:52'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4262'
  comment_author: Michael Yevdokimov
  comment_author_url: ''
  comment_content: '<blockquote>All of those examples add another layer of difficulty
    to making a website. CSS and Javascript both takes time to learn. And you don’t
    need to explain why you can skip ending tags, who cares as long as i works? XHTML
    adds another layer of difficulty to _HTML_, a layer that has very few advantages.
    I believe ease of use (HTML is an easy language) has taken the web to where it
    is today. Let’s not throw that away.</blockquote>\n\nHello Emil,\nThe article
    is good, though I am disagree with some major points. I agree that there is no
    enough "correct" support by different browsers. I would say even block models
    differ from browser to browser. But even this all does not mean that something
    should very easy for the users. Well, we are not living in perfect world. If you
    are not a technical man, you usually read manuals and learn how to use something,
    right? XHTML is not difficult at all. It has its own rules which are good. Yes,
    it adds extra layer of "difficulty". But that layer is important because in the
    end you will well-structured code. You would say again your 5 cents to protect
    user from all these "difficulties". I still think XHTML is a step forward which
    forces you to split structure from styles. I think HTML was a real mistake, but
    was not be able to avoid it. All first versions of any products have its "limitations",
    in reality they are not limitations themselves but rather the realization of what
    was in developer''s mind at that time. Time pasts, we grow. \n\nDoes everyone
    build cars? Does everyone buils airplanes? Does everyone program in PHP? No, not
    really. In this way why everyone should be coding in HTML? :) If you are not the
    programmer, just use the special tool, like Dreamweaver or something cheaper which
    would handle that coding for you. Otherwise, if you gonna grow as a developer
    use the correct tools. Otherwise, pay money to professional. It''s a pity that
    &lt;br /&gt; is not a real standard for HTML, instead I should use not-closed
    tag. Everything should have its order. Presentation is presentation, structure
    is structure. I don''t have much doupts about XHTML. The only thing I hate is
    "buggy" browsers and using hacks for CSS.\n\nUnfortunately, it happened that everyone
    once tried HTML think they are pros since that moment and can do real business.
    In the end we get what have now: billions of unstructured pages. Who cares? We,
    developers, do. The situation is very similar to digital photography market. :))))
    Somebody buys digital camera, "pornography" begins. Yes, it''s all now looks simplier,
    but still you must keep your head and hands on the places where they are growing
    from. Otherwise, it''s a mass. \n\nPlease excuse me for my big message. I think
    this is an endless theme. :)'
  comment_date: '2006-09-03 04:44:41'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4265'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Michael Yevdokimov: One of the big arguments you use is that
    XHTML is better at separating structure from presentation. That''s simply false.
    Using the strict version of the HTML doctype (like this site does) ensures that
    no deprecated elements can be used. That''s not a difference between HTML and
    XHTML, it''s a difference between transitional and strict doctypes of the two.\n\nYou
    compare building websites with building airplanes. But the fact is that many are
    able to build a site right now, using HTML. Let''s say that HTML takes a week
    to learn. What I fear is that XHTML doubles that learning time. Can you learn
    to build an airplane in a week?\n\nLet''s keep HTML and let''s educate instead
    of force users to do the right thing. That''s what I try to do with Friendly Bit.'
  comment_date: '2006-09-03 10:05:28'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4267'
  comment_author: Georg
  comment_author_url: ''
  comment_content: I think I'll stick to my own interpretation of the whole HTML vs.
    XHTML vs. whatever...  \n\n"Relying on error-recovery is generally a bad idea,
    and doing so doesn't help anyone to learn anything about mark-up."
  comment_date: '2006-09-03 12:03:10'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4270'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Georg: I''m all pro strictly validating sites, but for the majority
    of people HTML is already too hard. Adding extra rules will not make more sites
    valid, it will make fewer of them valid. A web that does not need error recovery
    would be great, but why do we need XHTML for that? One of the few things they
    add is, that''s right, well defined error-recovery.'
  comment_date: '2006-09-03 12:50:32'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4277'
  comment_author: Adedeji Olowe
  comment_author_url: http://www.dejiolowe.com
  comment_content: Sometimes I think XML is a solution in search of  problem. Why
    must web pages be XML compliant? If something works, no need to fix it!
  comment_date: '2006-09-03 14:50:35'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4278'
  comment_author: Georg
  comment_author_url: http://www.gunlaug.no/contents/main_author.html
  comment_content: 'Validity in itself isn''t all that important, but standards aren''t
    of much value if we tell the majority of people that they don''t matter.  \n\nOne
    of the ideas behind standards were that one should not have to hand-write or manually
    check and maintain pages/sites. The standards should in themselves create a base
    for tools as well as interpretation. This would have solved the problem for the
    majority of people, and left the road open for the minority to explore and create
    beyond what the tools could provide for at any given time.  \n\nNow we have come
    somewhat closer to "all browsers = same interpretation" since they are, at least
    on paper, supporting the same standards. It is even closer if we serve XHTML properly,
    as ''application/xhtml+xml''.  \n\nReliable and standard-based tools that provide
    room for creativity are still pretty much a joke on the ''text/html'' level, and
    completely non-existent on the ''application/xhtml+xml'' level. Thus, the majority
    of people who don''t know - and most often don''t care - about standards as long
    as it works, can''t get much, if any, help from tools.  \n\nThe only help the
    majority of people get is **error-recovery** in browsers, while it should have
    been **error-corrections** in tools before their "creations" ever got near a browser.  \n\nIf
    we want the quality to deteriorate even more, then we can just keep on telling
    the majority of people that applying standards is too hard so they shouldn''t
    bother. That should keep the need for proper tools at FrontPage level for the
    foreseeable future, so no real improvements will be needed in that sector.  \nI
    don''t think anyone in their right mind want that, but this - and many other articles
    lately, are providing the ground for web design at such a low level of quality
    to be accepted as a de facto "standard".  \n\nUnderstand me right: I don''t read
    your article in such a negative way, and I do in fact agree with much of what
    you have written. However, I don''t think the majority of people will read and
    use such articles as anything but excuses for not bothering, and unless that is
    what you wrote it for then it certainly should have been angled differently and
    the title should have been changed.'
  comment_date: '2006-09-03 15:22:21'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4287'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Georg: I''m not telling people that standards don''t matter.
    HTML is a fine standard, and if you look at the source of this site you''ll see
    that one can make wonders with it :)\n\nIs using HTML strict setting the bar too
    low? I think not. Also, I totally see your point, I just don''t agree.'
  comment_date: '2006-09-03 22:35:58'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4290'
  comment_author: Cpawl
  comment_author_url: ''
  comment_content: Emil, \nYou keep making the point that you are all for standards
    and using HTML strict is the way yet you also make comments saying beginners should
    have not to worry about such things because it's "too hard" and they can learn
    them later.\n\nYour paradox makes no sense.  Would you encourge language students
    to say the words half right, because it makes them happy that they accomplished
    something, instead of correctly?  As long as a math student feels good inside,
    would he be allowed to get his algebra only somewhat right... he can learn the
    rest later.\n\nAnyone interested in web design, whether with the goal of a pro
    or as a novelist should know the rules, apply them (even if it's too too hard
    for their little minds as you make them out to be) or else go do somthing else
    with their time.  HTML alone allows too many errors, depends too much on someone
    else (in this case the browser) to keep up after you. The web is polluted with
    horrible code because beginners were encouraged to not really give a poop, where
    given tools that cared less too, and where taught by people who said, "Although
    I care you do not need to little first timer."\n\nWith your "but the poor beginners"
    argument, I ask why you even bother to use strict HTML?  If it is really pointless
    in the end, if the browser can just simply fix it anyway, if this is what you
    encourage and teach, then why bother yourself?  Just go ahead and forget to close
    some tags, use all caps, whatever man.  This is the beauty of HTML remember?
  comment_date: '2006-09-04 08:33:23'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4291'
  comment_author: Georg
  comment_author_url: http://www.gunlaug.no/contents/main_author.html
  comment_content: 'HTML 4.01 Strict isn''t too low - as long as that is what it is.
    No problems there. In fact: I have no problems with the use of any standard -
    or even no standard at all - as long as it is what it claims to be.  \n\nSo called
    "XHTML" that can only work when served as ''text/html'' isn''t a standard at all
    - it''s a joke, and I think that is what you have problems with and are calling
    "...a bad idea". I have no problems with such a statement either, since you''re
    just saying that serving non-standard and non-working markup is a bad idea.  \n\nHowever,
    since you''re actually saying that "XHTML is a bad idea", and "...it’s damn hard
    to get XHTML right", then I do have a problem with what you''re saying.  Proper
    XHTML 1.0, that can be served either way, isn''t a bad idea, and it certainly
    isn''t harder to get right than any other markup standard - just slightly different.  \n\nThe
    problem with "XHTML" is that the joke (that: if it is "valid" and is working when
    served as ''text/html'', then it is XHTML) has been kept alive and maintained
    on too many high profile sites for too long. "Fix it with the right doctype" is
    one of the worst statements out here, as no doctype can "fix" anything. Triggering
    mode-switching in browsers isn''t a real fix. It''s the markup that should be
    fixed so it goes with the chosen doctype (read: standard), and the browsers should
    treat it accordingly.  \n\nMost, if not all, tools are crippled, and can''t go
    beyond ''text/html'', and a major player on the browser-side have ignored the
    existence of properly served XHTML (as they have ignored just about everything
    else) for too long.  \n\nNeither of the present shortcomings can be blamed on
    XHTML as a standard, so I have a problem with your article on that point. \nWhether
    or not XHTML can, or will, ever be developed into something useful beyond 1.x,
    is an entirely different matter. Working in a vacuum within a vacuum, must be
    pretty frustrating.'
  comment_date: '2006-09-04 09:21:01'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4297'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Cpawl: Thanks for your long comment!\n\nYour example with the
    language students is really a good one. If you start correcting every little error
    someone makes when trying to speak a new language they will get bored and stop
    trying. That''s basic pedagogy!\n\nThis is not about beginners being stupider
    than the rest of the world. Both you and I know that, we both where beginners
    once. \n\nWe are already seeing a web where the onces producing the most content
    is the people that knows most about technology. For every time we raise the bar
    for beginners to learn we will help that shift.\n\nOn web standards: We can''t
    make the web better by forcing developers. The only thing that helps is education.
    \n\nYou may close your tags with HTML, and yes, I think that''s better from a
    programming standpoint. Forcing me to use lowercase tags is just silly.'
  comment_date: '2006-09-04 18:35:37'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4300'
  comment_author: bruceyeah
  comment_author_url: ''
  comment_content: An interesting post... it's got a hint of troll about it so I'm
    sure you'll get a lot of hits to your blog after writing this.\n\nI just wanted
    to point out a little history. When Tim Berners Lee invented the web, he never
    intended 'beginners' to be writing HTML. Software was meant to handle all that
    and hide the tags from the end user. It's just an unfortunate accident of history
    (ie. the explosive growth of Mosaic) that lead to beginners writing their own
    HTML everywhere.\n\nXHTML might be a little more difficult to learn, but there's
    a few things I wanted to point out about this:-\n\n1) in an ideal world where
    web browsers are better, 'beginners' will never have to deal with writing XHTML
    themselves.\n2) you are underestimating the value of a valid XML format. Valid
    XML means that the document can be read by machines as well as humans. It ensures
    that documents don't become messy and unparseable in future. Don't forget that
    the uses we find for web pages may not be obvious until well into the future.
    Also... how can you use DHTML and AJAX type features if you can't parse a valid
    DOM structure from a page?
  comment_date: '2006-09-05 09:34:10'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4311'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@bruceyeah: I think the "trolliness" comes from the fact that
    my opinion differs a lot from what many people think. This is an important discussion
    though and many points have been made in the comments. And no, I don''t get much
    hits to this post, most people are regulars commenting.\n\n1) I belive it''s wonderful
    that a beginner can write &lt;b>Some text&lt;/b> in a textfile, open it in their
    browsers, and see bold text. It gives them the feeling that the web is easy to
    deal with and does not require them to buy expensive tools for the task.\n\n2)
    I know the value of XML. But beginners don''t need AJAX, SOAP, and DOM parsing.
    They just want to slap something together and show to their friends. The next
    step is making  working upwards in the foodchain and become a web professional.'
  comment_date: '2006-09-05 20:13:46'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4321'
  comment_author: carter
  comment_author_url: ''
  comment_content: i use xhtml. It's bomb. And i'm a beginner.
  comment_date: '2006-09-06 00:55:19'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4332'
  comment_author: Martin Payne
  comment_author_url: ''
  comment_content: <blockquote cite="http://friendlybit.com/html/why-xhtml-is-a-bad-idea/#comment-4297">You
    may close your tags with HTML, and yes, I think that’s better from a programming
    standpoint. Forcing me to use lowercase tags is just silly.</blockquote>\n\nI
    don’t really see why. For instance in C, “<code>char *myString</code>” and “<code>char
    *MyString</code>” are two completely different variables. So why shouldn’t XML
    consider “<code>&lt;foo:myElement&gt;</code>”, “<code>&lt;foo:MyElement&gt;</code>”
    and “<code>&lt;bar:MyElement&gt;</code>” as being different from each other?
  comment_date: '2006-09-06 12:53:57'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4358'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Martin Payne: again, that''s programming. And beginners make
    misstakes of that kind of stuff all the time. All kinds of beginners start out
    with Visual Basic and learn programming there (and then move on to something else).'
  comment_date: '2006-09-07 00:06:40'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4572'
  comment_author: La domo de karotoj &raquo; XHTML ne estas malbona ideo
  comment_author_url: http://zooplah.farvista.net/blogo/index.php/2006/09/12/xhtml-ne-estas-malbona-ideo/
  comment_content: '[...] ?use Emil STENSTR&Ouml;M blogis, ke XHTML estas malbona
    ideo. ?u tio veras? Mi opinias: ne. [...]'
  comment_date: '2006-09-12 03:41:25'
  comment_post_ID: '89'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '4666'
  comment_author: Greger Lundström
  comment_author_url: ''
  comment_content: 'Emil, I see your point concerning beginners. And most of the web
    of today is built by amateurs of different levels. And I agree the web must continue
    to be for everyone and not only the pros.\nBut I don''t see the contradiction
    between a harder, more strict language and letting beginners create their own
    sites. That''s what tools that produce valid code are for. Language of the output
    doesn''t matter.\nMy biggest concern is that while it''s easy enough to get started
    with html you get a lot of bad habits as browsers and standards are soo forgiving.
    Bad habits die hard and as you progress these habits become a burden. Many semi-professionals
    produce a lot of invalid code for professional sites. They continue to do so because:
    it''s easy, it works most of the time, their clients doesn''t know. When the day
    comes and a client needs and demands valid code, he can''t deliver. The step between
    beginner and pro becomes unnecessary hard because you''ll have to relearn to do
    things you''ve been doing for years. I''ve taken this road myself the past years
    and I would have been much easier to learn to do it right the first time than
    relearning as I go along.'
  comment_date: '2006-09-14 10:10:05'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4678'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Greger: So where are the tools that produce good XHTML? As far
    as I know there are none that does it satisfactory. \n\nI see your other concern
    and I''ve thought about it. There''s a limit in how difficult you can make a language.
    If XHTML was even more strict, would you still recommend it for them? There''s
    a line to be drawn somewhere, and I think that line should be drawn before XHTML.'
  comment_date: '2006-09-14 21:40:04'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '4693'
  comment_author: Greger Lundström
  comment_author_url: ''
  comment_content: If we don't push standards and strave to follow them there's no
    need for developers to create the tools for them either. If we embrace the standards
    and use them, developers will be forced to create better tools for it. HTML-tools
    didn't produce correct code for a very long time (too long) and some still struggle.
    But we didn't stop using HTML because of it. The same will be true for XHTML until
    we demand something better.
  comment_date: '2006-09-15 07:47:31'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '4946'
  comment_author: Matt
  comment_author_url: http://www.takemorerisks.com
  comment_content: You put across a compelling argument! HTML 5?!?!? Who would have
    thunk it!
  comment_date: '2006-09-21 23:07:15'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '5199'
  comment_author: Henrik Feldt
  comment_author_url: ''
  comment_content: 'Hello Emil,\n\nIt''s been a while. I came to visit your site because
    I''ve started my own web developing business, and I''m looking into people I had
    time to talk with before the international baccalaureate tests that I had this
    spring.\n\nSo what do I find, when entering your site? A big headline - "Why XHTML
    is a bad idea". Too bad I think... That power of the dark forces have gotten hold
    of him... And he seemed to be such a nice guy and all!\n\nLet me first say that
    I agree with what Mark said in the comments previously, and I do believe some
    other people have made some very strong points about it being easier to learn
    because of the structure of it. Then I''m not talking about XHTML 1.1 served with
    the correct mime type, but rather the structure of XHTML itself - the structure
    of XML, which is very logical in itself. How would it be, had we gone back to
    the books teaching:\n\nThat would suck, wouldn''t it? XHTML is the structure the
    web needed, and there is no logical reason as to why one would simply turn it
    down. (especially since you may serve it as text/html)\n\nMathML is a beautiful
    creation - being able to convey maths with ease to ordinary people. I wrote my
    Higher Lever math essay in XHTML 1.1 because it enabled me to use CSS to style
    consistently and MathML to insert maths that would otherwhise be really hard to
    harmonize with images.\n\nAnyhow, I also would like to say that there ARE tools
    that produce good XHTML. For example XStandard which is excellent to use in content
    management systems.\n<a href="http://www.xstandard.com/" rel="nofollow">http://www.xstandard.com/</a>\n\nAnother
    point you seem to miss out on is that XHTML does indeed not stand alone - it is
    designed with CSS and made dynamic with javascript. Hence it does indeed display
    very nicely in old browsers - they simply don''t display all the goodies, nor
    should they - you musn''t become too conservative and say that "we have to allow
    for IE 5.0 (which was - 10 years ago?)"...\n\nOverall I think the article is rather
    narrow-minded - you should focus on progression, not regression -- for example:
    you could explain the features of HTML 5, because I don''t know them, you could
    explain the features of MathML instead of bad-mouthing it, you could explain the
    potential welfare-gains in society by using open-source image editing tools to
    provide SVG images for the web, instead of buying expensive proprietary software.
    You could focus on the tighter integration between XHTML, CSS, Javascript, Flash
    and Server-side - how it all can be used to make the web more fun and usable for
    even the tech-savvy.\n\nhenke'
  comment_date: '2006-09-27 00:52:02'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '5200'
  comment_author: Henrik Feldt
  comment_author_url: ''
  comment_content: '* the code that didn''t surface:\n\nI can''t write code in here
    ...'
  comment_date: '2006-09-27 00:55:19'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '5201'
  comment_author: Henrik Feldt
  comment_author_url: ''
  comment_content: I just have to clarify - I don't mean my comment to be regarded
    as hostile - I'm just a wee bit tired right now ;)\n\nSov gott.
  comment_date: '2006-09-27 01:08:13'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '5672'
  comment_author: Perrymc
  comment_author_url: ''
  comment_content: 'Wow! One not-so-small topic generating so much conversation!  Thank
    all of you for helping me choose to use HTML at this time.  Over twenty years
    ago I worked as a computer programmer, using JOVIAL; the tortuous, tedious, wordy
    COBOL (back in the time of punched card input, before it was simplified with function
    keys), and had much fun programming in UNIVAC assembler language. I left the field
    and now, with only a little home-grown PC experience, at 56 I have been asked
    by a fledgling animal rescue non-profit organization to set up a web page for
    them.  Less than 10 minutes of reading to see if I was even capable of  such an
    endeavor led to my very first question: “To HTML or to XTHML?”  My main concern
    is to be sure I give them as ‘professional’ a product as I can given severe limitations
    on time and resources.  I want to set it up as simply as possible (html), require
    as little maintenance as possible (xhtml) and yet be functional on what appears
    to be an ever changing web(xhtml).  So, from all of your comments it appears there
    is a host of peripheral considerations when using XHTML.  Under different circumstances
    and from all of your comments I would probably choose to learn XHTML and go forward
    from there.  Considering my limitations, HTML makes more sense.  Now, when you
    all refer to “HTML strict” are you referring to a variant of HTML or just to applying
    HTML standards properly? I have a handful of library books and now I would like
    to find an HTML beginner-friendly website that uses a ‘checklist’ approach to
    creating a webpage that is followed up with a detailed how-to for each element.  I
    think I need this visual picture to see what I am really getting myself into!  Any
    inputs from anyone?  \n\nEmil, thanks for Friendly Bit.  It has given me considerable
    food for thought!'
  comment_date: '2006-10-12 03:05:14'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '5722'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Perrymc: Perhaps it could help to see a real site growing? I
    wrote an article some time ago about <a href="http://friendlybit.com/css/semantic-poker-template/"
    rel="nofollow">building a poker site</a>.\n\nIf you start learning HTML you also
    have the basics of XHTML. XHTML adds some stuff to be XML compliant and in my
    opinion you can add that afterwards.\n\nGood hearing that you too like my readers
    :)'
  comment_date: '2006-10-14 10:49:40'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '5972'
  comment_author: Max Pagels
  comment_author_url: http://www.maxpagels.com
  comment_content: Thank you very much for an excellent article.\n\nBeing a newbie
    to the world of valid (X)HTML i have to say that i agree with most of what this
    article has to say. In the beginng, i found it very difficult to write valid markup,
    and would as such definitely not recommend XHTML to beginners.
  comment_date: '2006-10-23 19:35:45'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '6004'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Max Pagels: Thanks!'
  comment_date: '2006-10-24 13:06:25'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '7079'
  comment_author: FROIDURE Nicolas
  comment_author_url: http://bbcomposer.elitwork.com
  comment_content: I think using XHTML is a good idea because when every navigators
    will be compatible, XHTML will be the most used technology.
  comment_date: '2006-11-13 15:08:16'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '7866'
  comment_author: aRgus
  comment_author_url: ''
  comment_content: I use XHTML and am often asked why by other developer types.\n\nI
    don't care about the anal retentive tag structure making my content more "hardcore".
    I don't care about the "XHTML STRICT!" banner on the bottom of my pages.\n\nI
    do it for the warm and fuzzies I get of having a "well formed document"  that
    can be predictably parsed by any software that is able to understand the doctype.\n\nSure,
    HTML can be viewed broken and I'm happy for that. I don't want people to have
    to know how to split an atom to post content that I want to view. As a user, as
    long as it looks good in my browser I don't care what they use.\n\nNow as a developer,
    I am inclined to do some extra work on my part, to insure uniformity in my code
    regardless of it's context or application.\n\nSomeone may want to parse my work
    into another format, text reader, whatever. I publish content for others to use.
    I do what I can to insure they can  parse, view, format, whatever my content any
    way they wish.\n\nShould everyone be FORCED into XHTML? No. That doesn't make
    XHTML itself a bad idea either. There is definitely something to be said for uniformity
    in code.
  comment_date: '2006-11-26 08:19:55'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '7884'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@aRgus: So how do you mean that adding a slash to empty elements
    make it easier to parse? HTML can be made perfectly valid, well-formed, and strict.
    I''m compelled to think that you add the slash for some other reason... what is
    it?'
  comment_date: '2006-11-26 15:40:34'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '8645'
  comment_author: fan-tiger
  comment_author_url: ''
  comment_content: The problem You see by learning or using XHTML I do not agree,
    because if You only learn XHTML you don´t mind HTML, you even don´t know it. And
    because there are all the tools out there, it´s also easy for beginners to use
    XHTML.\nWell, after I learned XHTML 1.0 y first tried to use it as is. The problem
    at this time was the missing compatibility of browsers. So I had to learn about
    how to get contents displayed in older browsers.\nAnd dammned, <b>there´s still
    no standard, which is fullfilled by all!</b>\nSo finally it was an good idea to
    get HTML parsed as XML, but the only version to use is 1.0 and only, if there´s
    no other way of working with data.\nSome words to HTML:\nThe META statement for
    the used version is still very tricky, because only transitional will get the
    content displayed well in most browsers.\nI even don´t know anyone, who´s using
    &quot;strict&quot;, but I know very much pages using different versions like 4.0
    and 4.01 because of formatting tables. So how do You explain a beginner this?
  comment_date: '2006-12-07 14:08:38'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '12159'
  comment_author: Kamran
  comment_author_url: http://socialgeek.wordpress.com
  comment_content: I think XHTML is something that SAVES you from making a mess of
    your web pages.\n\nI agree with the idea of XHTML i.e. to saparate the content
    and presentation in different pieces.\n\nOf course, everything has its pluses
    and minuses, but when it comes to me, I feel XHTML has more pluses in the long
    run than the minuses.
  comment_date: '2007-01-03 12:17:12'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '12193'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Kamran: separation of content and style has nothing to do with
    XHTML, it''s just a matter of selecting the strict doctype. The idea of separation
    comes from CSS, a language that works together with both XHTML and HTML.'
  comment_date: '2007-01-03 19:04:31'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '16527'
  comment_author: Will
  comment_author_url: ''
  comment_content: This is what beginners are taught by the W3C. This is why we use
    the XHTML DTD :\n\n"XHTML is a stricter and cleaner version of HTML."\n\n"XHTML
    is aimed to  replace HTML"\n\n"XHTML is almost  identical to HTML 4.01"\n\nSo
    for those wanting to learn HTML, ideally what W3C schools should be pushing is
    the use of strict HTML instead of pushing people to use XHTML as it's unncessary
    if your website is only text/html.\n\nFrom a beginners perspective this is quite
    confusing. I'll definitely look more into this with the links provided.
  comment_date: '2007-01-26 13:54:35'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '17780'
  comment_author: lamandriel
  comment_author_url: ''
  comment_content: I disagree with the statement that HTML is and could be learned
    by a beginner in a short amount of time. I mean, hey, there are a <em>lot</em>
    of extremely smart people working for Microsoft, Opera, Apple, Mozilla, KDE &amp;
    Co. and they haven't been able to learn HTML in <em>14 years</em>! Just all those
    omissability rules of SGML alone are so incredibly complex, it just blows one's
    mind.I don't know any browser that would parse the following code even remotely
    correct:<blockquote><p>&lt;!DOCTYPE i PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot;&gt;&lt;i//</p></blockquote>And,
    yes, that <em>is</em> perfectly valid HTML.
  comment_date: '2007-01-31 04:28:16'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '18280'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Will: I totally agree.\n\n@lamandriel: There''s a difference
    here. No one would ever use the code you describe. When I talk about learning
    HTML I mean learn it to do stuff you want to do, not some theoretical crap :)'
  comment_date: '2007-02-02 00:04:07'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '18783'
  comment_author: Dutch
  comment_author_url: ''
  comment_content: It's nearly impossible to read all comments to search for the question
    I have.\n\nW3C advises to use XML to change data in the future I understood with
    wordprocessors, databases, spreadsheet applications. They expect the application
    programmers to adapt these programms which makes exchanging data easier.\n\nEmil,
    what do you think about this W3C motivation?\n\nAnother question:\nI already changed
    my website to XHTML 1.0, before reading your article, should I be worried now
    that relatively older browsers won't see the website?
  comment_date: '2007-02-03 17:24:49'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '18959'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Dutch: As my article tries to say I don''t think XHTML is a good
    idea, so I think W3C is doing something wrong by pushing it. You don''t need to
    worry about your site though, it will probably work on older browsers too (unless
    you did everything right, which very few know ;)'
  comment_date: '2007-02-04 09:43:19'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '19065'
  comment_author: Dutch
  comment_author_url: http://www.dutchhomepage.nl
  comment_content: 'Thank you for your quick reply Emil! \n\nBut I can''t find an
    answer to my first question about W3C''s motivation for using XHTML: easer exchanging
    data for the next future.\n\nI doubt new websitewriters have interest in exchanging
    data yet, but if youngsters learn writing XHTML with CSS correctly in an early
    stage, I can''t really think what would be against this. It might depend on the
    education level, I guess?\n\nI agree W3C shouldn''t push XHTML especially not
    for beginners, like you said!'
  comment_date: '2007-02-04 16:26:39'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '22176'
  comment_author: Jordan
  comment_author_url: ''
  comment_content: 'Nice article, Emil! It highlights a very crucial problem of transparency
    which needs to be addressed before we can progress much further with web standards.\n\nOne
    of my co-workers, not a fellow of the programmer mindset and accustomed to designing
    with tables in Dreamweaver, was trying to get to grips with using valid <abbr
    title="HyperText Markup Language">HTML</abbr> and <abbr title="Cascading Style
    Sheets">CSS</abbr> to design websites. The process was painful and agonising to
    watch; sometimes, I wanted to scream after looking at the code he produced. (And
    then I remember that I used to write code like that.)\n\nAll this agony, and we
    hadn''t discussed convincing him to use minimal <code>&lt;div&gt;</code> tags
    and semantic markup! I''m convinced that if, at that point, I tried to introduce
    him to the distinction between <code>&lt;acronym&gt;</code> <abbr title="versus">vs.</abbr>
    <code>&lt;abbr&gt;</code>, he would flip out completely, slaughtering the office
    in a bloody rage. Never mind explaining the problems with using <code>&lt;abbr&gt;</code>  in
    <abbr title="Internet Explorer">IE</abbr>. As for the debate over the <code>&lt;q&gt;</code>
    element&hellip; Even I wanted to defenestrate after wading through that one.\n\nThis
    man isn''t clueless, either. He''s been designing websites since before I even
    saw a webpage for the first time!\n\nThere is no way on earth that the vast majority
    of the online population have any place being asked to consider the complex rules
    governing character encodings and <acronym title="Multipurpose Internet Mail Extensions">MIME</acronym>
    types. At this level of technical detail there should be limited user involvement;
    common <abbr title="eXtensible HyperText Markup Language">XHTML</abbr> problems
    should be dealt with by an abstraction layer which can take care of it without
    the need for low-level supervision. We need smarter tools to lighten the cognitive
    load for non-technical users.\n\nUsing your examples, here''s the sort of thing
    I mean:\n\n<blockquote><p>If I used <abbr title="eXtensible HyperText Markup Language">XHTML</abbr>
    (and parsed it properly) and someone used invalid code in the comments the page
    would break.</p></blockquote>\n\nBrowsers should provide better built-in semantic
    editing tools, circumventing the need for Javascript/plugins. Blogging sites need
    built-in tools which can handle and deal with receiving malformed input. New coders
    should be strongly encouraged to use existing abstraction layers rather than hand-coding
    them.\n\n<blockquote><p>Next I copy-paste some text from a site I want to quote
    to you. When I publish the article I get a big ugly error message because the
    site I pasted used another character encoding and that breaks my XHTML.</p></blockquote>\n\nWhatever
    <abbr title="Content Management System">CMS</abbr> you are using to publish articles
    should already be able to deal with different character encodings; again, those
    who want to write their own <abbr title="Content Management System">CMS</abbr>
    should be directed to use existing modules which take care of these complicated
    problems before they arise.\n\n<blockquote><p>Next I download a bit of javascript
    and try using it on the site. Again people get an ugly error message in their
    face when they enter. It seems javascript is handled a lot stricter in <abbr title="eXtensible
    HyperText Markup Language">XHTML</abbr> and inline javascript needs some strange
    CDATA characters at the beginning and end of the script element.</p></blockquote>\n\nJavascript
    is a tricky one. For one thing, I think that <strong>all</strong> Javascript should
    be contained in external resources; this avoids problems with CDATA sections.
    However, we need to develop better procedures for packaging, documenting and integrating
    Javascript into webpages. I think that what we really need are IDEs which enforce
    modularisation of Javascript and external resources, clearly identifying dependencies
    between modules; then, when the site is launched or tested, the necessary files
    are "precompiled" into a distribution directory. This is similar to how Java programmers
    have been working for a while. In my opinion, this will be much easier when most
    browsers support newer versions of Javascript with an "<code>import</code>" directive.\n\nSo
    I agree that <acronym>HTML</acronym> is the best current solution <em>at the moment</em>
    for new web designers. However, once tools, technologies and applications have
    evolved which make producing and interacting with <abbr title="eXtensible HyperText
    Markup Language">XHTML</abbr> as easy and useful as it was always intended to
    be, I won''t be surprised if <abbr title="HyperText Markup Language">HTML</abbr>
    is swiftly abandoned in favour of its more powerful sibling.\n\nOne final note:
    a huge part of the responsibility here lies with browser vendors. When we can
    finally rely on valid markup and <abbr title="Cascading Style Sheets">CSS</abbr>
    being interpreted correctly, and uniform Javascript support across different platforms,
    I predict that progress will be made in leaps and bounds. Here''s to <abbr title="Internet
    Explorer">IE</abbr> 8!'
  comment_date: '2007-03-08 12:19:54'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '23154'
  comment_author: Anders M.J.
  comment_author_url: ''
  comment_content: This is a good article Emil and just today, I have switched to
    HTML 4.01 Strict from XHTML 1.0 Transitional, after reading your advice here.\n\nThe
    majority of users use IE and since this browser doesn't support XHTML, there's
    no reason to use this standard yet (and I don't use XML, so why code in XHTML).
    Might as well stick with good ol' HTML 4.01 then.\n\nI had not coded in Strict
    before today, but still never used any deprecated tags, so the convert wasn't
    that painful. :-)\n\n/Anders
  comment_date: '2007-04-07 20:02:58'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '26595'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: 'I undrestand your thoughts, but i disagree with your conclusion.
    O.k., old style html will always have its place. For the casual web page writer
    it may be more easy to handle. But html is limited. The ''X'' in xhtml stands
    for ''extensible''. That is: In xhtml you could use xml namespaces and then include
    other xml dialects in the page. Most notably would be rdf and its derivates. Or
    think of svg to directly include vector graphics into the code. You could include
    anything. \nIf you use html, you can''t directly include it. You may include such
    things via object, but then: If the browser is capable to parse xml to render
    an external svg object, why then not directly parse xhtml as xml? It is the same
    parser. \nSure, using xhtml this way enforces the use of application/xhtml+xml
    to get those benefits. If you send it as text/html, in fact you just send malformed
    html which the browsers error handler fixes. So i agree it would not be useful
    to limit yourself to the html possibilities, send your files as text/html but
    still pretend to code it as xhtml. This _may_ be useful during a learning phase,
    but not more. \nSo as a conclusion: As long as you are well of with what html
    offers you, it should be sufficient to code and send as html. As soon as you plan
    to add more to your pages you should think of switching to xhtml. Using xhtml
    consequently breakes every limit. Your possibilities virtually become unlimited.
    _This_ is why xhtml is the future. html 5 just extends the current html limits,
    but it still has limits and will always have. Many times html 5 will be absolutely
    sufficient. But as soon as you can get more, there will be an increasing demand
    for more, so you will have to switch to xhtml at some point.\nAnd, BTW, it is
    still possible to automatically convert xhtml to html using xsl. It is nearly
    impossible to automatically convert erroneous html files to proper xhtml.'
  comment_date: '2007-08-07 08:26:57'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '26611'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Siegfried: I see your point, and I can agree that XHTML is a
    good idea IF you want to use the extensibility features. Most people do not though,
    not now, and not in any distant future, and there''s no reason for them to change.
    \n\nOn a sidenote, HTML5 includes a variant that allows XHTML syntax, so they
    try to cater to that side too. Might be good to know.'
  comment_date: '2007-08-07 21:58:47'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '26616'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: Yes, i know. And it's not the worst idea. Just the naming convention
    is very bad. Calling the html version html 5.0 is logically. Calling the xhtml
    version xhtml 5.0 is nonsense. It would be much better calling it xhtml 1.5. The
    real, although not near future is xhtml 2.0.\nThe problem with the html effords
    is, you always have to add new features to the monolitic block of html. With xml
    you freely get modularisation. So in fact this is the way to go.\nYou're right,
    those additional features are not much needed today. For most issues html 4.01
    is just sufficient. Su as long as you accept the limits you may stick to html.
    And since the IE does not understand xml (not without an xsl stylesheet), today
    it is generally better to at least offer a parallel html version, if not just
    an html version alone. But the point will come where you have to switch. It is
    your personal decision, when to switch. But some day it will be necessary. Old
    style html will then be just a markup language for the casual hobby web page producer.
    Professionals will need xml. In the future :)
  comment_date: '2007-08-08 07:56:04'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '27361'
  comment_author: William O. Yates
  comment_author_url: ''
  comment_content: I looked away from a tree, and found a forest...\n\nBetter tools
    for common users could nullify this entire debate.\n\nA well built composer <em>should</em>
    publish pages following all the standards.  (HA!)\n\nSome of the "DOM" tricks
    lost to HTML/XHTML/XML from SGML are environmental "hints" which would allow the
    composer software to "learn" which code base to use and what attribute switches
    to select.\n\nI built such a composer for IBM's BookManager product back in 1992.  It
    handled 1200 or so of the most commonly used tags in a research environment.  Secretaries
    were using it with a couple hours introduction.\n\nBUT, (sigh...), I still use
    my hammer and chisel to code my web pages by hand (html-401 strict of course :-).
  comment_date: '2007-09-14 16:07:27'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '27420'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@William: I''m not such better tools fully fixes the problem.
    We still have the issue of error-handling in the browser... XML has one way of
    handling errors that just doesn''t work on the web.'
  comment_date: '2007-09-16 11:18:22'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '30059'
  comment_author: Christian
  comment_author_url: http://www.christianziebarth.com
  comment_content: You can learn HTML in 5 days and XHTML in 5.03 days. So, what's
    there to worry about?\n\nYou can learn tables-based layout in 3.6 days and CSS-based
    layouts in 3.8 days. What's there to worry about?\n\nBut if you learn things correctly
    there really is no difference in learning time.\n\nAnd if you use XHTML from the
    beginning it'll be easier for you to work with your code later.
  comment_date: '2008-01-02 20:36:39'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '30455'
  comment_author: RomanAge
  comment_author_url: ''
  comment_content: 'Having some programming skill will be much more common for normal
    people in the future, a bit like reading and writing has been for a long time
    (avaliable to people from age 6). More and more people will use these skills merely
    as a tool that allow them to do whatever they are interested in: art, science,
    communicating... therefore being a professional programmer (and just that) may
    loose a lot of its value (unless very specialized), let''s get used to that, have
    trust in people''s capacity, and not fear a standart even if it is more demanding.
    I believe XHTML is a move in the right direction.'
  comment_date: '2008-03-18 04:34:35'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '30468'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Christian: There is a difference. You can <strong>think</strong>
    that you learn HTML, XHTML, or CSS in 4 days, but you really haven''t. All you
    know by that time is enough to get you by. In the case of HTML and CSS, it isn''t
    that bad, but for XHTML it really breaks things. Severely.'
  comment_date: '2008-03-20 07:53:49'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '30473'
  comment_author: xhtml &laquo; Rofrol blog
  comment_author_url: http://rofrol.wordpress.com/2008/03/21/xhtml/
  comment_content: '[...] Emil Stenström - Why XHTML is a bad idea [...]'
  comment_date: '2008-03-21 17:55:12'
  comment_post_ID: '89'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '31693'
  comment_author: Jim Westergren
  comment_author_url: http://www.jimwestergren.com
  comment_content: Hi Emil,\n\nGood article and good point.\n\nOn my latest major
    site that I am currently building I am using XHTML 1.0 strict - mostly to be prepared
    for the future. \n\nI tried sending it in XML with a similar PHP script that you
    have here but I disabled that after some testing. I can't have my site breaking
    with parsing error because I missed to close a p element or forgot to unescape
    an &amp; in an URL. Can't take that risk.\n\nPerhaps HTML 5 is the way to go.
    I have read some on that. But I guess it will take quite some years for that to
    be fully ready and supported.
  comment_date: '2009-04-14 01:59:50'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '31713'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jim Westergren: Nice that you liked the article :) \n\nSince
    HTML5 is the future, it shouldn''t matter if you use HTML 4 Strict, or XHTML 1.0
    Strict, they are all incorporated into HTML5. I truly believe that''s the best
    thing for the future of the web. It will take a couple of years, but browsers
    are already building offline storage and stuff like that. Also, big parts of the
    spec are just respecifications of how browsers have implemented stuff.'
  comment_date: '2009-04-19 22:21:08'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
- comment_ID: '31724'
  comment_author: Jim Westergren
  comment_author_url: http://www.jimwestergren.com
  comment_content: Oh, that's well. HTML5 have quite many new elements which I think
    will be great for usability and perhaps even future SEO. Looking forward to it.
  comment_date: '2009-04-27 16:22:41'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '33163'
  comment_author: MWin
  comment_author_url: ''
  comment_content: Hello Everyone,\n\ni read that article, and Emil does have some
    points...\nbut i want to add something to the "leave the error-handling to the
    browsers" topic:\n\nOne of the reasons why XHTML was introduced as a "cleaned
    up" HTML so-to-speak, is the increasing usage of internet on mobile devices, such
    as mobile phones, PDAs, that sort.\n\nI know, hardware performance is constantly
    increasing, but so far most mobile devices just dont have the cpu for extended
    html-code-analysis and exception-handling, if they had, they would be even slower
    as they already are...\n\nBut in the end (at least until HTML5 is published, but
    even then) it's the webdesigner's choice which technology to use, i suppose they
    all have their pros and contras...\n\nJust my thoughts, have a nice day,\n\nMike
  comment_date: '2009-11-04 19:09:24'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '33164'
  comment_author: MWin
  comment_author_url: ''
  comment_content: One more thing...\n\nas for the looseness of html:\n\nconsider
    following, simplified, code:\n\n<code>\n\n    Paragraph 1\n    Paragraph 2\n    Pargaraph
    3\n\n</code>\n\nnow, these 3 paragraphs, are they siblings to each other, or descendants?\n\nI'm
    one of them programmer types, so for me this in fact is an issue...\n\nas for
    the above example, as far as i could find out, FireFox (3.5) considers them siblings
    (automatically closes all non-closed paragraphs when a new one opens, i.e. paragraphs
    cant contain other paragraphs, just like the html4 dtd specifies), so does IE
    (7), netscape considers them descendants, and amaya wouldnt let me find out at
    all...\n\nso, i guess thats one point on XHTMLs scoreboard...\n\nhand\n\nMike
  comment_date: '2009-11-04 19:17:52'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '33165'
  comment_author: MWin
  comment_author_url: ''
  comment_content: Hmm, didnt keep my html code snipped...\n\ntry this:\n\n&lt;body&gt;\n&lt;p&gt;
    Pragraph 1\n&lt;p&gt; Pragraph 2\n&lt;p&gt; Pragraph 3\n&lt;/body&gt;
  comment_date: '2009-11-04 19:19:38'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '33342'
  comment_author: 'Web Design: What DOCTYPE do I use? &laquo; Obvious In Hindsight'
  comment_author_url: http://obviousinhindsight.wordpress.com/2010/01/09/web-design-what-doctype-do-i-use/
  comment_content: '[...] If you’d like to research an alternative opinion on why
    not to use XHTML, read here (Note: It’s an old article, much of it may not apply
    but interesting no less): <a href="http://friendlybit.com/html/why-xhtml-is-a-bad-idea/"
    rel="nofollow">http://friendlybit.com/html/why-xhtml-is-a-bad-idea/</a> [...]'
  comment_date: '2010-01-09 05:03:09'
  comment_post_ID: '89'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33343'
  comment_author: 'Web Design: What is XHTML? &laquo; Obvious In Hindsight'
  comment_author_url: http://obviousinhindsight.wordpress.com/2010/01/09/web-design-what-is-xhtml/
  comment_content: '[...] <a href="http://friendlybit.com/html/why-xhtml-is-a-bad-idea/"
    rel="nofollow">http://friendlybit.com/html/why-xhtml-is-a-bad-idea/</a> [...]'
  comment_date: '2010-01-09 05:50:45'
  comment_post_ID: '89'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33465'
  comment_author: Steve Savage
  comment_author_url: http://www.stevenksavage.com
  comment_content: 'After several years away from the web, I''ve decided to revitalize
    my site.  I''d been debating providing both an XHTML (for application/xhtml+xml
    browsers) and HTML version (for text/html browsers).\n\nI''m leaning towards just
    <em>publishing</em> HTML5 right now for the simple fact: if I decide to put advertisements
    on my site I will no longer have complete control of the markup, and I''d rather
    have the tag-soup parser kick in then have "XML Parsing Error: mismatched tag"
    show up instead of my content.\n\nBUT, I emphasized the word publishing for a
    reason.   I will probably use an XHTML editor behind the scenes for the content
    I write, so I can use XSLTs to convert my XHTML documents to other formats.'
  comment_date: '2010-03-07 17:48:03'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '33915'
  comment_author: K
  comment_author_url: ''
  comment_content: This is an old blog post, but, boy am I glad I found it. Finally,
    someone who speaks clearly about this nonsense. I finally understand. Thank you,
    Emil.\n\nIn hindsight, what should have happened in the early 2000's is, instead
    of pushing XHTML, authors and industry should have advocated and taught proper/recommended
    HTML4 &amp; CSS coding.\n\nIn reality, that is what average web dev students were
    seeking back then. Most, like me, had hobby pages in the late 90's with no sense
    of direction. Focus turned to XHTML with total lack of understanding of XHTML's
    true purpose.\n\nIf I only understood back then, I would have never focused on
    XHTML - or focused on WAP but that's a different story - and continued enjoying
    HTML.\n\nI am excited about HTML5 and eager to learn about it soon... and it might
    lessen my perfectionist anxieties. Maybe XHTML caused it? :)
  comment_date: '2010-06-10 21:53:42'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '0'
- comment_ID: '33916'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@K: Thanks for your comment, and good to hear that I make sense
    in a world of information overload :)\n\nI truly think XHTML was one of the big
    reasons HTML5 has started to catch on now. People where simply not OK with some
    parts of XHTML, and wanted others. HTML5 (and XHTML5) are excellent alternatives.'
  comment_date: '2010-06-11 08:25:46'
  comment_post_ID: '89'
  comment_type: null
  is_admin: '1'
---