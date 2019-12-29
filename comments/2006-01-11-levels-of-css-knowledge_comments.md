---
comments:
- comment_ID: '13'
  comment_author: Trevor
  comment_author_url: http://www.personaldevelopment.ca
  comment_content: Level 4 seems to be the most common misunderstanding about web
    standards. People assume that replacing tables with divs is the right answer.
    About 10 mins of helping usually turns them away from that though and start seeing
    the benefits :)
  comment_date: '2006-01-11 01:59:17'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '14'
  comment_author: bnovc
  comment_author_url: http://bnovc.com
  comment_content: Well layed out and nice looking/interesting.
  comment_date: '2006-01-11 02:07:39'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '16'
  comment_author: Moe
  comment_author_url: ''
  comment_content: Great article! I think i'am at level 5 but it took it's time. To
    answer you're question about trend setters, the first person how comes to mind
    is Roger Johansson over at 456bereastreet.com.
  comment_date: '2006-01-11 13:58:00'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '17'
  comment_author: Gavin
  comment_author_url: ''
  comment_content: Nice little post, might even help those who are afraid of CSS understand
    how to make the links between what knowledge they do and don't know. And why it
    takes time to piece it together.
  comment_date: '2006-01-11 15:05:07'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '18'
  comment_author: grexican
  comment_author_url: ''
  comment_content: 2v2 no mod you serve!?
  comment_date: '2006-01-11 15:30:34'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '19'
  comment_author: Veracon
  comment_author_url: http://www.veracon.net/
  comment_content: I hate when people call CSS design 'using divs' -- divisions are
    unsemantic and should be carefully used. A bunch of nested divisions really isn't
    much better than a layout using tables.
  comment_date: '2006-01-11 16:50:11'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '20'
  comment_author: Greg
  comment_author_url: http://www.eeight.com
  comment_content: Not a helpful article, but very true and interesting. Great observation
    by the author.
  comment_date: '2006-01-11 16:50:22'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '22'
  comment_author: Thomas Sydorowski
  comment_author_url: ''
  comment_content: Interesting.
  comment_date: '2006-01-11 21:55:54'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '23'
  comment_author: Dustin Diaz
  comment_author_url: http://www.dustindiaz.com
  comment_content: I classify the first four groups all into one and then weed out
    the talkers from the professionals. I would be more interested to know how their
    cross-browser strategies of CSS come into play or what kind (if any) architecture's
    they use to maintain their style sheets. What are their thoughts on hack management?
    What's the benefit (or drawbacks) of conditional comments?\n\nBtw, did you read
    my book on...
  comment_date: '2006-01-12 00:37:52'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '24'
  comment_author: Emil Stenström
  comment_author_url: http://
  comment_content: '@Dustin: Jokes aside, those are great topics for later articles!
    :) I''ll see what I can do.'
  comment_date: '2006-01-12 01:30:14'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '25'
  comment_author: Andrew Vit
  comment_author_url: ''
  comment_content: I like the classifications you propose. However, one thing that
    most CSS zealots won’t readily acknowledge is that complex flexible or “liquid”
    layouts are still either impossible (if you want to support IE) or very fragile
    without adding a table as a placeholder for overall layout. (Visit any 3-column
    pure-CSS site and resize the window to watch the content squeeze out the bottom.)\n\nThis
    isn’t the fault of CSS2. IE6 is unfortunately still the majority browser, and
    we still have to support it. Until we can use <code>min-width</code> reliably
    to keep things from collapsing too far, pure CSS layouts will be restricted to
    two columns or fixed-width. (I‘m a big fan of <em>em</em>s personally, but some
    clients still want those 3 columns that “fill the screen.” I've done a lot of
    complex fixed-width work using semantic markup and CSS, but I'm still waiting
    for a robust flexible CSS layout that can match what could be done using the basic
    old-school 3-column table.
  comment_date: '2006-01-12 03:38:13'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '26'
  comment_author: Emil Stenström
  comment_author_url: http://
  comment_content: '@Andrew: did you try zooming the layout on this page? It''s a
    three-column thing and it resizes to really, really small sizes just fine. It''s
    perhaps not fluid though, more elastic, so I''m not sure we''re talking about
    the same thing. \n\nI think CSS works just fine to do 3 col layouts with and I
    don''t see the problem with it.'
  comment_date: '2006-01-12 08:49:07'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '28'
  comment_author: Andrew Vit
  comment_author_url: ''
  comment_content: Emil, I would still consider your layout to be fixed-width, even
    though it uses ems. Whether you use ems or pixels, the width of your page is independent
    of the widht of the window. This is my preferred method too, since it scales nicely
    with the font size on the user’s browser and gives predictable results. What I
    was talking about are the kinds of very common table-based layouts where you have
    a 200px column on the left and right, and the middle stretches to fill the window
    when it's resized.\nA few months ago I had really high hopes for the <a href="http://www.positioniseverything.net/articles/onetruelayout/"
    rel="nofollow">One True Layout</a>, but after working with it I found it has limitations
    in this area too. Its author simply brushes off the fact that it can’t mix 2 fixed
    and 1 liquid columns by saying "I don’t have any use for that kind of layout."\nRecently
    I read Apple’s article on <a href="http://developer.apple.com/internet/webcontent/bestwebdev.html"
    rel="nofollow">Web Development Best Practices</a> and found that I agree with
    much of what they say. Yes, the table is an unsemantic wrapper to hold the overall
    layout, but in many cases I have found this method necessary. I would like to
    see more opinions on these “best practices.”
  comment_date: '2006-01-12 18:29:23'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30'
  comment_author: jose
  comment_author_url: http://www.cabanadigital.com
  comment_content: I think that I’m in some place between level 4 and level 5. I’m
    trying to improve my knowledge about accessibility and semantic markup, it’s a
    long way but at the same time it’s a lot of fun!
  comment_date: '2006-01-12 23:57:54'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '33'
  comment_author: Emil Stenström
  comment_author_url: http://
  comment_content: '@Andrew: Perhaps you just do more web development work than I
    do. I have never had to resort to using tables for layout, and to be honest I''d
    rather rethink my design than doing so. I understand clients might have problem
    with that. \n\nThanks for that Apple link, always interesting to see what big
    corprations are doing.'
  comment_date: '2006-01-13 00:48:38'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '36'
  comment_author: Frida
  comment_author_url: ''
  comment_content: Great article!
  comment_date: '2006-01-14 13:46:42'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '44'
  comment_author: Adam
  comment_author_url: ''
  comment_content: The best part of this article was the fact that I remember being
    at each step, all the way up to where i am at now :)  It was fun to read and made
    me realize how far I've come
  comment_date: '2006-01-15 19:17:58'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '110'
  comment_author: draco
  comment_author_url: ''
  comment_content: Maybe that's why you put a (!) there, but there's really no strict
    dtd in XHTML 1.1.\n\nAnd to me, a <code>div</code> only site is way better than
    a <code>table</code>full site in all senses. At least they give screen readers
    an easier job.\n\nI could be wrong. lol.
  comment_date: '2006-01-31 22:06:24'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '119'
  comment_author: Emil Stenström
  comment_author_url: http://
  comment_content: '@draco: Thanks, I see now that XHTML 1.1 is just an "extension"
    of XHTML 1.0 Strict. Removed the word strict from the text above.'
  comment_date: '2006-02-02 23:40:56'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '141'
  comment_author: Ross
  comment_author_url: ''
  comment_content: I would say I'm a level five, however I'm not really at the implementation
    stage - I understand why I should be using it but I don't have the experience
    behind me to really utilise it - I'm currently looking at a website I frequent
    and have offered to upgrade their site from basic HTML to CSS. They were using
    the XHTML Standard and had over 290 errors, simply by switching to HTML Strict
    I reduced to the error count by 110.
  comment_date: '2006-02-07 20:43:55'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '165'
  comment_author: Andrew Norris
  comment_author_url: http://listeningtoreason.blogspot.com/
  comment_content: Interesting post. I'm a software engineer who is still learning
    the proper methods of web development, and I am in the process of trying to learn
    to get to level 5 at the moment, though in the site I've been building lately,
    I still have some stray HTML inserted for layout reasons and my CSS is pretty
    poorly organized and includes too many one-off classes and id-level styles. This
    definitely inspired me to try to work harder to clean things up and learn how
    to do it right. Thanks.
  comment_date: '2006-02-13 04:35:30'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '170'
  comment_author: Chris Charlton
  comment_author_url: http://feeds.feedburner.com/webdevdesign
  comment_content: I'm defenitely on transition from Level 5 to 6, w00t!\n\n:)
  comment_date: '2006-02-14 01:00:34'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '249'
  comment_author: Timothy Gray
  comment_author_url: http://www.codeispoetry.com
  comment_content: Good stuff!  Regrettably, I'm a level five.  I need to get moving
    on that level six status...
  comment_date: '2006-03-08 22:25:33'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '250'
  comment_author: Jeff
  comment_author_url: ''
  comment_content: You missed one - Level 10\n'Yes, I will have that done today.'\nThey
    use everything available to make things work, can tell you why and why not, and
    don't worry about whether or not its 'right' by some arbitrary standard.  Also,
    they are too busy to write self-congratulatory posts on a random site about how
    people who don't use CSS properly write bad code. Congrats on your vacuous story.
  comment_date: '2006-03-08 22:50:50'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '251'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jeff: I see what you mean. Good code and getting things done
    are different things and from what I hear it''s not often possible to combine
    them. I don''t look down on the people that are not experts, this is a list that
    I myself have climbed, from one to five where I think I am now. My intent is not
    to insult anyone :) (Hope that''s clear enough)'
  comment_date: '2006-03-08 23:05:29'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '252'
  comment_author: Keith McLaughlin
  comment_author_url: http://www.wiredvision.com
  comment_content: I think I'm part Level 3, Level 4 and Level 5. I'm still learning.
    I know the benefits. But it's not coming to me as easily as it might have to others.\n\n(P.S
    I'm working on a web standards version of my site at present).
  comment_date: '2006-03-08 23:36:50'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '253'
  comment_author: Dawn
  comment_author_url: ''
  comment_content: Nice post. I'd say I'm somewhere between a 4 and 5 myself, and
    I'm actually finding that clients requirements (SEO, accessibility) are pushing
    me to put more of my CSS knowledge into practice. My boyfriend just made the jump
    from a level 2 to a level 4 with a little help from a nice job offer. I'm happy
    to see he's finally making some progress and learning how capable CSS is.
  comment_date: '2006-03-08 23:44:36'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '254'
  comment_author: Jeff
  comment_author_url: http://jrm.cc/
  comment_content: I totally beat level 5 -- the boss was really hard.
  comment_date: '2006-03-09 00:37:13'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '259'
  comment_author: nosebleed
  comment_author_url: ''
  comment_content: Good points. Although, I will say that it seems a little pretentious
    to me. As if being level 4 or 5 is REALLY that bad? I consider myself a level
    5, but do I want to be level 6? As much as I'd like to be the new innovative and
    progressive CSS god where CSS isn't just a "programming language", but an art
    form that one knows how to shape and mold to their desires. I guess as a level
    5er I think of it as a "tool that I can use to make my site pretty, and do other
    cool and useful things with"
  comment_date: '2006-03-09 01:57:12'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '260'
  comment_author: Allan
  comment_author_url: ''
  comment_content: '@Jeff: I guess that leaves rooms for level 11, then. Those people
    who can say: "Yes, I will have that done today," AND do it correctly.\n\nStandards
    are arbitrary? It''s somewhat sad that you think so; HTML/CSS standards are certainly
    _not_ arbitrary. They were carefully considered and thought out by very smart
    people for reasons that aren''t bloated by commercial considerations. It''s science,
    not "who can make the worst web site the fastest."\n\nAnd true professionals always
    _make_ time to advocate for the correct way of doing things. Just because you
    think it''s all a waste of time, does not mean that you are righteous in posting
    condescending comments in response to a well written post--vacuous indeed.\n\nThis
    blog is title "Friendly Bit". If you''re not going to attempt to be friendly,
    please try another venue to outlet your frustration :)'
  comment_date: '2006-03-09 02:35:45'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '261'
  comment_author: Priti
  comment_author_url: ''
  comment_content: Its a well written article. I think im on level 4, although I make
    sure that I dont use table less layouts just for the heck of it. There is this
    design which is complete of images with an internal scroll of text along with
    navigation. After creating a css based layout, realised that it was more confusing
    and tedious than the table one. The code was running real long too. Hence used  a
    table for the basic layout and divs for the scroll and other text elements. There
    is this one site I have created which is completely in CSS last year. Would like
    to know your review on it..mistakes,improvements,etc. its www.ishanya.com
  comment_date: '2006-03-09 06:49:08'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '269'
  comment_author: Nik Steffen
  comment_author_url: ''
  comment_content: Level 5, thats about me. Mind you, I quite enjoy a good game of
    CS:S aswell.
  comment_date: '2006-03-09 12:29:00'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '270'
  comment_author: Artueel blog &raquo; Blog Archive &raquo; Hoe goed beheers jij CSS?
  comment_author_url: http://blog.artueel.be/hoe-goed-beheers-jij-css/
  comment_content: '[...] Dat meer en meer mensen css en (x)html leren is niets nieuw.
    Maar hoe goed beheers jij css? Emil Stenström onderwerpt je op zijn website niet
    aan een quis - neen hij werkt met levels gaande van 0 tot 6, per level een korte
    uitleg. [...]'
  comment_date: '2006-03-09 12:33:04'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '271'
  comment_author: Ahren Gerber
  comment_author_url: ''
  comment_content: I liked this article, but I think there is a stage between stages
    4 and 5. I consider myself, by your standards, to be a stage 4.5-4.75.\n\n\nI
    am not yet confident that I could solve any CSS problem that comes my way, I still
    have trouble figuring out how to separate my css documents (as done in ALA) but
    I'm also not using fireworks DIV slicing or anything. I do my best to create semantic
    code, with resonable tagging, avoiding "divitis" as best I can, and I also take
    SEO into consideration while doing the front end coding for my company. I think
    that level of complexity perhaps warrants another level of development.\n
  comment_date: '2006-03-09 15:48:23'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '273'
  comment_author: Johan De Silva
  comment_author_url: http://www.johandesilva.co.uk
  comment_content: I think I am at Level 5 but I never design within my limitations
    of CSS so some designs maybe too complex and I need to fall back to using a table
    for part of the frame design.
  comment_date: '2006-03-09 16:26:52'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '274'
  comment_author: Shawn
  comment_author_url: ''
  comment_content: I work at university and help maintain 4 department and 3 audience
    based sites which all share the same code base. Recently we decided to go from
    a left aligned layout to a centered layout. It took 2 lines of code added to one
    wrapper to change hundreds of pages instantly. Do that with your stupid tables.
  comment_date: '2006-03-09 16:51:16'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '275'
  comment_author: Jeff Clark
  comment_author_url: http://www.ihiredjeffclark.com
  comment_content: Sadly (?) I'm only at level 5.
  comment_date: '2006-03-09 17:42:15'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '276'
  comment_author: Kumar
  comment_author_url: http://home.no.net/kumar
  comment_content: Very good article. I do feel noe i can improve and with the list
    you provided I can have an idea about what needs to be done. Think I am somewhere
    between level 4 and 5...\n\nThanks fot the article.
  comment_date: '2006-03-09 18:18:16'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '280'
  comment_author: MarkL
  comment_author_url: ''
  comment_content: '{Hi, my name is Mark, and I''m a Level 3. Hi Mark!!} \n\nGreat
    article. Through my own development, I can relate to each level somewhat. I''m
    currently at L3 but want desperately to get to L5. I''m trying to learn divs,
    but for some reason, I keep hitting a wall. I do see the value and want to end
    my dependency on tables. {Hence, my intro.}'
  comment_date: '2006-03-09 21:32:43'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '282'
  comment_author: Tommy
  comment_author_url: ''
  comment_content: What a terribly pompous, condescending article!\n\nI really like
    css as a tool, but you people who write about it are perhaps as annnoying and
    self-righteous bunch as I've ever come across.  \n\nMore importantly, there are
    lots of people I've met who don't want to learn css largely because of the obnoxious,
    quasi-messianic bent of its proponents, and the raft of books, blogs and articles
    with the thinly veiled subtext of  "everything YOU do is wrong".\n\nUsers who
    don't know as much as you about something or (gasp) disagree with you are "dangerous"?\n\n\nYou
    design webpages.  \nNo one starves if you fail.  No one's immortal soul is involved.\n\nGet
    a freakin grip!
  comment_date: '2006-03-10 18:16:06'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '283'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Tommy: See my comment to Jeff above. These are the steps I myself
    have climbed. I''ve also seen others move from step to step in this list. The
    purpose is not to be condescending, it''s to show that there is more to learn
    for anyone.'
  comment_date: '2006-03-10 20:06:41'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '285'
  comment_author: ryanahamilton.com &raquo; Blog Archive &raquo; What is your level
    of CSS Knowledge?
  comment_author_url: http://www.ryanahamilton.com/?p=35
  comment_content: '[...] Levels of CSS Knowledge [...]'
  comment_date: '2006-03-10 21:14:08'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '286'
  comment_author: Shane
  comment_author_url: http://www.freshclickmedia.com/blog
  comment_content: I know quite a few designers who are at 'Gold' Level 1.  How inconvenient
    for someone to come along and insert another level into your carefully constructed
    heirarchy.\n\nYeh, the guys I know work for a 'market-leading' company; they have
    not only removed underlines from links, but have progressed to font size (using
    pts of course), font family, font colors and so on.  So, it's fonts and colors
    basically.  If they want padding (they don't know they want it, but they do),
    they'll opt for a spacer.gif.\nSod it - I'm going to demote them to Level 1.
  comment_date: '2006-03-11 10:55:50'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '296'
  comment_author: michael
  comment_author_url: ''
  comment_content: horrendously stuck at <strong>Level 4</strong>...reading and playing
    like mad to get to Level 5 or 6...\n\n<i>any</i> help is always appreciated.
  comment_date: '2006-03-12 18:35:01'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '298'
  comment_author: Tim
  comment_author_url: ''
  comment_content: 'I think it''s a mistake to assume that it''s possible to master
    html without mastering css. \n\nI mean, ever tried to hand code a table based
    layout? 99,9% of all the table based layouts are probably created using a wysiwyg
    editor. And let''s face it : Dreamweaver''s design view makes it easy to twist
    and merge table cells to your liking, but it doesn''t make you think about writing
    semantically appropriate html.\n\nSo there :\n\nhtml level 0 = css level 0\nhtml
    level 1 = css levels 1 through 3 (wysiwyg editor players)\nhtml level 2 = css
    level 4\nhtml level 3 = css levels 5 through 6 ("Yes, I can make a doctype decision
    and I know what <code>&lt;dl&gt;</code> stands for").\nhtml level 4 = css levels
    5 through 6 (anything between "I actually read the W3C specs" and "I actually
    wrote the w3c specs")\n'
  comment_date: '2006-03-13 08:38:18'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '302'
  comment_author: www.jammo.net &raquo; Friendly Bit » Levels of CSS knowledge
  comment_author_url: http://www.jammo.net/2006/03/13/levels-of-css-knowledge/
  comment_content: '[...] Friendly Bit &raquo; Levels of CSS knowledge<a href="http://friendlybit.com/css/levels-of-css-knowledge/"
    rel="nofollow">http://friendlybit.com/css/levels-of-css-knowledge/</a> [...]'
  comment_date: '2006-03-14 09:30:57'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '304'
  comment_author: Stefan Asemota Weblog | Web Standards Quiz — Archive
  comment_author_url: http://www.asemota.de/weblog/13/web-standards-quiz/
  comment_content: '[...] If you are a web designer and you think you know your craft,
    go ahead and try out this quiz. While you’re at it, you might also want to read
    Emil Stenström’s Levels of CSS knowledge [...]'
  comment_date: '2006-03-14 20:27:16'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '317'
  comment_author: supa
  comment_author_url: http://www.supamb.com/supafine
  comment_content: I agree, there should be a Level 4.5, or maybe 5.25 -- it's not
    enough to know and understand XHTML and CSS; the downfall is that you must know
    hacks, bugs, fixes and workarounds for a variety of browsers. I can code just
    fine, but there's another level of knowledge you have to get to in order for your
    work to actually present itself as intended on certain browsers/platforms. That's
    what keeps me from really being thrilled about CSS as it stands today. Tables
    aren't semantic at all for design but at least they translate well.
  comment_date: '2006-03-16 06:13:31'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '336'
  comment_author: Liam Hesse
  comment_author_url: http://www.lemm.me.uk
  comment_content: <b>&lt;Tommy, Mar 10&gt;</b> <i>You design webpages.\nNo one starves
    if you fail. No one’s immortal soul is involved.</i>\nNo, but hundreds of man-hours
    are lost. Wasted. <i>Frittered away</i> by having to comb through some horrific
    malformed table-based monstrosity. It damages productivity, and that <i>is</i>
    dangerous.\n\nTake my word for it. I am a web developer, and I've had to fix other
    people's table-based work before. It's not just a <i>figurative</i> headache,
    I assure you.
  comment_date: '2006-03-21 13:27:49'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '339'
  comment_author: Matt Williams
  comment_author_url: ''
  comment_content: Great post.\nHow about some suggestions on how to get to increase
    your current level?\nWebsite recommendations?\nBook recommendations?
  comment_date: '2006-03-21 18:06:17'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '340'
  comment_author: Dewey Williams
  comment_author_url: ''
  comment_content: There is one more level that I seem to run into often.  These are
    the graphic/ad designers, that design a site in PhotoShop, slice the big picture
    into a lot of small pictures, throw it into GoLive, publish it to a server and
    call it a website.  I have explained, argued, taught and berated some of them
    to no avail.  They seem to believe what they are doing is web design/best practices/professional
    sites.  I don't know how to get through to these people.
  comment_date: '2006-03-21 22:07:16'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '342'
  comment_author: About Web Designing &raquo; Blog Archive &raquo; Levels of CSS knowledge
  comment_author_url: http://www.aboutwebdesigning.com/2006/03/22/levels-of-css-knowledge
  comment_content: '[...] In a nice post discussing various levels of CSS design knowledge
    Emil lists 5 levels of people who know CSS or are aware of its existence. CSS
    layouts are tough if you are just a beginner, and they are labor-intensive once
    you begin to know your way around the labyrinthine DIV definitions. Still, CSS
    layouts are far, far, far better than those table layouts because the way you
    can manipulate them. What’s my level of CSS knowledge? [...]'
  comment_date: '2006-03-22 16:28:23'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '344'
  comment_author: Brad Fults
  comment_author_url: http://h3h.net/
  comment_content: Excellent breakdown. Most people would have tried to break it into
    3 levels, but I think all 6 of yours are necessary and distinct.\n\nThanks.
  comment_date: '2006-03-22 21:21:00'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '345'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Matt Williams: The only way I''ve found works is a combination
    of reading and trying things out yourself. I listen to people talking about CSS
    daily and I think that helps to. You''ll be Level 6 if you just keep pushing.
    \n\n@Dewey Williams: I know exactly what kind of people you are talking about
    :) I wouls call them graphic artists, not web designers. In fact, building a whole
    site in flash is very similar, you don''t use the features of the web, so how
    it that web development?\n\n@Brad Fults: Good to hear you like it!'
  comment_date: '2006-03-23 00:33:12'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '348'
  comment_author: Dirk Diggler
  comment_author_url: ''
  comment_content: You people are way too impressed with your ability to deal with
    crappy browsers and somewhat implemented standards to produce a layout. You do
    the same thing as magazine layout designers, except they dont have to worry about
    people stretching their magazine page or switching the font sizes on them.\n\nI
    can't believe anyone would feel snooty or talk down on people that make web pages
    that aren't all produced from xml/xslt/css/dom/give it a rest, technology is supposed
    to make your life easier - as a software designer I fail to see why web designers
    are so masochistic and get pleasure from having to use convoluted hacks to make
    something "standards compliant", or work with the .0001% of blind people that
    may look at their site.
  comment_date: '2006-03-23 17:27:03'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '349'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Dirk Diggler: As I have previously stated I''m not trying to
    talk down people. These are steps that exist, I''ve heard many people say "I''ve
    been a level 2 guy". I have full respect for people that have other reasons for
    not using web standards.\n\nI promote using HTML and CSS to produce good websites
    (not any XML/XSLT) instead of just HTML, is that such a big step? You seem to
    think this standards stuff is hard so let me tell you this: it''s not.'
  comment_date: '2006-03-23 22:49:28'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '351'
  comment_author: Dan Black
  comment_author_url: http://www.dystopiapop.com
  comment_content: I feel as though you need a level 5.5
  comment_date: '2006-03-24 02:50:54'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '355'
  comment_author: Midnight Cappuccino &raquo; 6 livelli della CSS-aggine
  comment_author_url: http://midnightcappuccino.com/archivi/2006/03/6-livelli-della-css-aggine/
  comment_content: '[...] Per restare in tema, da saldo 5° gradino vi presento i 6
    livelli della CSS-aggine. [...]'
  comment_date: '2006-03-24 11:47:14'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '361'
  comment_author: Narga Laboratory &raquo; Blog Archive &raquo; Levels of CSS knowledge
  comment_author_url: http://www.narga.net/145/levels-of-css-knowledge
  comment_content: '[...] From thisv very good content  As you might have understood
    by now I’m very much pro web standards. The current widely accepted standards
    are: (X)HTML for page structure, CSS for design, and Javascript for behaviour.
    HTML is pretty well known by now, it has been there since the beginning of the
    web and there are tutorials everywhere that gets you started. CSS is starting
    to get a grip, large companies are switching their sites to CSS based layouts
    and the webdev blogosphere reaches more and more people. [...]'
  comment_date: '2006-03-27 14:11:02'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '364'
  comment_author: Stupid Wordpress Tricks &raquo; Blog Archive &raquo; Levels of CSS
    Knowledge
  comment_author_url: http://www.irakrakow.com/wptips/2006/03/28/levels-of-css-knowledge/
  comment_content: '[...] CSS is a complicated topic.&nbsp; This article, by Emil
    Stenstrom, called Levels of CSS Knowledge, describes the 6 levels, from total
    ignorance (”CSS?&nbsp; Isn’t that a multiplayer game?”) to guru (”What version
    of CSS? … Did you read my book about…”).&nbsp; It’s an entertaing read.&nbsp;
    At the bottom of the article are some interesting related articles about the challenges
    of CSS, especially to those used to HTML tables. [...]'
  comment_date: '2006-03-29 02:56:44'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '370'
  comment_author: Bjorn
  comment_author_url: http://www.sharewonders.com
  comment_content: Another naive CSS evangelist fulfilling his obligation to shamelessly
    spread the CSS Gospel. To be honest, this article stinks of elitism. Who could
    imagined that such an evangelist would put qualities that spread the 'good CSS
    news' in the highest category. Yes DIV's are better than TABLES, but you don't
    have to be a dick about it.
  comment_date: '2006-03-31 09:54:52'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '372'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Bjorn: If you had read the comments I''ve made eariler to similar
    comments like yours you would see that these are steps I have myself been at.
    How is that a bad thing?'
  comment_date: '2006-03-31 16:02:14'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '380'
  comment_author: Imran Nazar
  comment_author_url: http://oopsilon.com/
  comment_content: '\nRe: the comment about table-based sites not being coded by hand,
    I actually did that one: a table-and-frame monstrosity with JS, all in Notepad.
    And I was proud of it at the time.\n\n\n\nThat''s the point this article is trying
    to get across, it seems: everyone who''s learning web development goes through
    these steps, including the best.\n'
  comment_date: '2006-04-04 11:22:11'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '404'
  comment_author: Graham King
  comment_author_url: http://www.devshack.co.uk
  comment_content: Great article. It's a shame about the negativity of some of the
    posts. There's nothing pompous about identifying bad practice and doing your bit
    to promote best use of standards. (And this from someone who knows very little
    about the power of CSS, but knows they have a lot to learn from people like yourself,
    and why they should bother to do so - not sure if I'm covered in your list though!)
  comment_date: '2006-04-11 16:53:57'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '405'
  comment_author: Holy Toledo More Lamers Version 2
  comment_author_url: ''
  comment_content: 'You sound so pontific way up there on your soap box. You know
    what Level 6 is: Humbly to  understand that there are millions of people who do
    this and because the w3c says "its the correct standard" that really means nothing.
    Heck the most popular browser in the world doesnt even follow w3c rules. Me personally,
    I like to incorporate at once 7-10 different languages in the LEAST into one of
    my web(worlds)- So if that means it is STILL going to work across the scope of
    web browsers and I have to go ouside the w3c "rules" to create a way to loop,
    hook, attach something the rules of the w3c are usless to me --just as long as
    it works and --continues to still work in the browser(s) - THEN , my little lernt
    friend-  so be it. Lastly- If you love CSS so very much, learn something new,
    because if your a level five ( whatever that means) - and your not going to level
    six -- your wasting away at least 3 layers....'
  comment_date: '2006-04-12 23:09:38'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '407'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: 'Anonymous (silly): It''s always nice with comments like yours
    from people that read one post and then assume that they know everything about
    you. I currently know Java, C#, C++, Php, Javascript and a few more at a basic
    level so I fully understand that the world is larger than just CSS. But that doesn''t
    matter in an article about "the levels of CSS" does it? Feel free to write your
    own list!'
  comment_date: '2006-04-13 12:06:18'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '454'
  comment_author: mike bliss
  comment_author_url: http://www.theblisspages.com
  comment_content: I try to follow the CSS rules on my site but your article has given
    me a nudge to remove more design from my HTML code (mainly image alignment). I
    will put a link to your site from my web design page. Thanks
  comment_date: '2006-04-20 17:16:31'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '497'
  comment_author: Justin
  comment_author_url: ''
  comment_content: well,i am at Level 4
  comment_date: '2006-04-25 03:02:29'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '536'
  comment_author: getting back, getting ahead
  comment_author_url: ''
  comment_content: I appreciate this article. I was a front end coder for 5 years
    and was laid-off in 2001, 3 months before my company finally evaporated along
    with its ping pong table and fully stocked kitchen. I've been doing other fun
    things for the past 5 years since there were no jobs for quite a while.  I miss
    the industry and I am on my way back. I am very aware that things have changed
    drastically and what I was an expert in back then, is basic knowledge now. I have
    a lot to learn to catch up to my colleagues who stuck it out. This article has
    been a great help in my awareness of where I am at, and where I need to be. Thanks
    very much for writing it.:)
  comment_date: '2006-05-01 17:19:53'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '538'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@getting back: Thanks for commenting, it''s always nice to hear
    that my writing helps someone. Surfing around you''ll find a lot of good resources
    to help you get back on track. I''ll meet you at your next ping pong table! :)'
  comment_date: '2006-05-01 19:37:42'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '539'
  comment_author: Dan Lee
  comment_author_url: http://katundu.com
  comment_content: “CSS? Isn’t that a multiplayer game?” :) I love it. I would have
    to say that I am at level five. I understand why CSS is a good thing and I use
    it though I would be pants at talking about it in conversations. It would be nice
    to be a bit more gifted with CSS when it comes down to it.
  comment_date: '2006-05-01 23:20:40'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '566'
  comment_author: Vitaly
  comment_author_url: ''
  comment_content: 'To be true, I do not remember the last time I used "table"s, not
    more then 2 years though.\nI think strong Level-5 is   for me, but thanks a lot
    to those from Level-6 who make it possible for others to know something new. The
    reason I make post here is to show for beginers: there are planty developers who
    made it professional with CSS, so JOIN! :)\nThank you,Emil.\nSorry for my English...'
  comment_date: '2006-05-06 09:00:34'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '622'
  comment_author: learner
  comment_author_url: ''
  comment_content: think at at level 1 :((\njust trying to learn now... and so am  here...
    will see after i trying making one site atleast...
  comment_date: '2006-05-11 15:55:59'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '729'
  comment_author: Ruby
  comment_author_url: http://quizilla.com/users/poisonruby/
  comment_content: Hi, I just found out that I am level 5 at CSS, which is quite surprising.
    I make website layouts as a hobby and your site is very useful. =]\n\nBest wishes,
    Ruby
  comment_date: '2006-05-19 11:10:39'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '836'
  comment_author: Seb
  comment_author_url: http://www.sebsworld.co.uk/
  comment_content: I'm on level 5, but still feels like I'm on level 1, as I still
    having to constantly refer back to www.w3.org
  comment_date: '2006-05-22 17:21:41'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '904'
  comment_author: En Español &raquo; Niveles de conocimiento CSS
  comment_author_url: http://www.enespanol.com.ar/2006/05/29/niveles-de-conocimiento-css/
  comment_content: '[...] Artículo Original: Levels of CSS knowledge [...]'
  comment_date: '2006-05-29 06:21:28'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '936'
  comment_author: syzygy
  comment_author_url: ''
  comment_content: This is gay, another egotist site. your site layout sucks too.
  comment_date: '2006-05-31 21:46:15'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '937'
  comment_author: jay
  comment_author_url: ''
  comment_content: I get very frustrated with people in level 0, 1 and 2. Anyway looks
    like I'm at level 5.
  comment_date: '2006-05-31 21:47:58'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '942'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@syzygy: As you might notice I don''t mention myself here at all.
    These are the steps I''ve heard more people than myself climb, how does that make
    it an egoist site? You''re also one of the first person to say the layout sucks,
    good to know.\n\n@jay: Those that don''t want to learn never will, so I don''t
    even try to convince people on the lower levels of why web standards should be
    used.'
  comment_date: '2006-06-01 00:03:34'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '947'
  comment_author: James A. Arconati
  comment_author_url: http://arconati.us/
  comment_content: GREAT ARTICLE, found you through del.icio.us.  Made me laugh though
    as it means I am a Level 4 or 5 in CSS Knowledge and I also am a level 12 Paladin.  *GROAN*  Thank
    you anyway!
  comment_date: '2006-06-01 07:28:22'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '950'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@James A. Arconati: Good to see someone got the point ;)'
  comment_date: '2006-06-01 09:42:15'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '952'
  comment_author: dandyna
  comment_author_url: http://dandyland.org
  comment_content: level 5 for me... how i wish I wrote a book as well :)
  comment_date: '2006-06-01 12:19:40'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '957'
  comment_author: CSS und HTML Ranking Checklisten
  comment_author_url: http://www.webdesign-in.de/mts/css-und-html-ranking-checklisten/
  comment_content: '[...] Emil Stenström [...]'
  comment_date: '2006-06-01 21:59:14'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '969'
  comment_author: Levels of Accessibility Knowledge – Le «blog personnel» de Joe Clark
  comment_author_url: http://blog.fawny.org/2006/06/02/niveaux/
  comment_content: '[...] I admit in advance that I am about to flirt with an Internet
    meme, the “Internet meme” (often mispronounced as though it were French and used
    a circumflex). But if dashing Swede Rohgayr Johansson can delineate levels of
    HTML knowledge and a somewhat-less-dashing Swede can delineate levels of CSS knowledge,
    perhaps it is time for… Levels of Accessibility Knowledge. [...]'
  comment_date: '2006-06-02 19:36:03'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '980'
  comment_author: 'Designers who Blog: Design, Illustration, Photography, Web, Advertising,
    Branding …'
  comment_author_url: http://www.designers-who-blog.com/?p=259
  comment_content: '[...] For a quick dip: Check out Emil’s  Levels of CSS knowledge.
    Then swing over to 456 Berea Street for a sister article on  Levels of HTML knowledge.
    [...]'
  comment_date: '2006-06-03 02:42:12'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '981'
  comment_author: Sean Fraser
  comment_author_url: ''
  comment_content: I'd say Level 6 but I haven't found any reasons for using CSS3
    (or, the other half of CSS2). So, I guess that would - Actually - be 5. I guess
    I could Malarkey two different sites, i.e., Two Tone and Mod, but IE 7 ruined
    that.
  comment_date: '2006-06-03 02:46:40'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '986'
  comment_author: Simon
  comment_author_url: ''
  comment_content: I'm on level 5. Yeay baby...!
  comment_date: '2006-06-03 07:34:47'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1017'
  comment_author: Linky na víkend 12 na depi.sk - IT & Life Weblog
  comment_author_url: http://depi.sk/2006/06/04/linky-na-vikend-12/
  comment_content: '[...] Levels of CSS knowledge [...]'
  comment_date: '2006-06-04 11:43:00'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1026'
  comment_author: Night Dreaming (by Sudar) &raquo; What is your Level of web knowledge?
  comment_author_url: http://sudarmuthu.com/blog/2006/06/04/what-is-your-level-of-web-knowledge.html
  comment_content: '[...] Well I am going to flirt with an Internet Meme which is
    getting spread around. It all started when Emil wrote Levels of CSS knowledge.
    This inspired Roger to write Levels of HTML knowledge and that got followed by
    Levels of Javascript knowledge, the levels of Accessibility knowledge etc. [...]'
  comment_date: '2006-06-04 17:25:12'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1037'
  comment_author: ??Web-Level????? | BiZwiKi.CN - ?? PK ??
  comment_author_url: http://www.bizwiki.cn/teamblog/?p=99
  comment_content: '[...] Levels of HTML knowledge 1 Levels of HTML knowledge 2 Levels
    of CSS knowledge Levels of JavaScript Knowledge Levels of Accessibility Knowledge
    [...]'
  comment_date: '2006-06-04 23:53:59'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1038'
  comment_author: Hecgo.com &raquo; ¿Qué tanto sabes de CSS, HTML y JavaScript?
  comment_author_url: http://www.hecgo.com/?p=147
  comment_content: '[...] Todo empezó con el post de Emil Stenström Levels of CSS
    knowledge donde en una escala de 0 a 6 propone los niveles de conocimiento, de
    tal forma que: 0 = “CSS? Isn’t that a multiplayer game?” 1 = “Yeah, I use it to
    remove underlines on links sometimes” 2 = “No, I don’t like divs; tables are much
    easier to work with” 3 = “Yes I’ve heard it’s good, but I can’t use it because
    of…” 4 = “CSS? Oh! Yes, I use divs for all my layouts” 5 = “I use CSS for design,
    it’s better than tables because of…” 6 = “What version of CSS? Yes, I do. Did
    you read my book about…” [...]'
  comment_date: '2006-06-05 00:56:13'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1045'
  comment_author: YELLOW BOY FOR ECONOMICS &raquo; Levels of Accessibility Knowledge
  comment_author_url: http://towmoons.edublogs.org/2006/06/04/levels-of-accessibility-knowledge/
  comment_content: '[...] June 4, 2006 @ 10:27 pm · Filed under yellow boy   I admit
    in advance that I am about to flirt with an Internet meme, the “Internet meme”
    (often mispronounced as though it were French and used a circumflex). But if dashing
    Swede Rohgayr Johansson can delineate levels of HTML knowledge and a somewhat-less-dashing
    Swede can delineate levels of CSS knowledge, perhaps it is time for… Levels of
    Accessibility Knowledge. [...]'
  comment_date: '2006-06-05 04:27:30'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1068'
  comment_author: Jeff
  comment_author_url: ''
  comment_content: I liked this article. I am just a beginner. I got started by taking
    a html class and thought it was fun. I got pretty good with tables, but I have
    hit some dead ends with them. I started to learn css for blogging and I am starting
    to like it. I would say that this puts me at a level three.
  comment_date: '2006-06-06 05:01:22'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1098'
  comment_author: Practical Web Design magazine &raquo; Blog Archive &raquo; *New
    podcast* Choosing the right layout
  comment_author_url: http://www.pwdmag.co.uk/?p=56
  comment_content: '[...] How to assess your competence in HTML, CSS and Accessibility
    [...]'
  comment_date: '2006-06-07 00:35:53'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1107'
  comment_author: Ramenos Blog &raquo; Evaluer votre niveau en HTML et CSS
  comment_author_url: http://blog.ramenos.net/design/evaluer-votre-niveau-en-html-et-css/
  comment_content: '[...] Voici deux études (en anglais) qui permettent de situer
    rapidement votre niveau concernant les CSS et l’HTML. Pour ma part, je me considère
    level 5 en HTML et entre 4 et 5 en CSS. [...]'
  comment_date: '2006-06-07 10:01:27'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1127'
  comment_author: ephraim hohn
  comment_author_url: ''
  comment_content: u r som pros :D *shake* diz is senseless.. the fact that ur rating
    does not go further shows ur incompetence, sry
  comment_date: '2006-06-07 21:19:16'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1128'
  comment_author: Ricardo
  comment_author_url: ''
  comment_content: I'm at a level 2 or two, and I can use all the help that I can
    get.\nThere's times that I use a table to position two more images on a web page.\nI
    know there some CSS to do that, but old habits are hard to break.\nI usually just
    use CSS on each web page instead of one external CSS page.\nBecause I want to
    keep control of each web page.\nThanks for all your information.\nIt lets us know
    that there still hope\n\nSemper Fidelis\nRicardo
  comment_date: '2006-06-07 21:54:16'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1130'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@ephraim hohn: relax, note the jokes in there.\n\n@Ricardo: Keep
    reading, there''s a lot of good blogs out there.'
  comment_date: '2006-06-08 01:20:06'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '1133'
  comment_author: Stacy
  comment_author_url: ''
  comment_content: Suppose your using Firefox and you browse to <a href="http://www.w3.org/Style/CSS/,"
    rel="nofollow">http://www.w3.org/Style/CSS/,</a> then you choose View-&gt;Page
    Style. What would you expect? <a href="http://www.w3.org/TR/REC-CSS1" rel="nofollow">http://www.w3.org/TR/REC-CSS1</a>
    makes a little more practical use of this. Strange that more sites don't understand
    that CSS can be a more dynamic means of information transferance. Do I get it?
  comment_date: '2006-06-08 06:51:41'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1134'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Stacy: I don''t see what you mean (probably my fault). What you
    show is one of the good parts about CSS, any page can have several layers of design
    that you can let the user pick from. It''s a nice feature.'
  comment_date: '2006-06-08 07:59:57'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '1140'
  comment_author: Stacy
  comment_author_url: ''
  comment_content: Exactly my point. CSS is about presentation. Presentation can take
    on many flavors and if needed or useful an author should provide that. The <a
    href="http://www.w3.org/TR/REC-CSS1" rel="nofollow">http://www.w3.org/TR/REC-CSS1</a>
    example shows (you have to scroll a bit) that an author can offer up two vews
    of the same content to provide different prospectives of the data. errata verses
    the current status. This is all accomplished through concurrent (alternat) style
    sheets. A user can choose per se to see the change bars or not. Seperation of
    content vs presentation. An idea I think under appriciated.
  comment_date: '2006-06-08 09:37:49'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1141'
  comment_author: Stacy
  comment_author_url: ''
  comment_content: Sure wish you had a preview and/or spellcheck option for comments.
    I butchered that last one :)
  comment_date: '2006-06-08 09:45:32'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1142'
  comment_author: Stacy
  comment_author_url: ''
  comment_content: 'I guess what I''m saying is your site for one (out of many) could
    provide an alternate css that provided the following \n\n\n.item_contents {\n  display:
    none;\n}\n\nor something similar... It''s late and I don''t feel like sifting
    through the css/tags/elements/whatever, but it would be nice to be able to turn
    off all comments via an alternat style sheet.'
  comment_date: '2006-06-08 09:57:50'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1144'
  comment_author: Gareth Powell
  comment_author_url: http://www.bloggeroff.com
  comment_content: Neat. CSS is plainly a very good thing and reminds me of a style
    sheet which I used for my magazines in Adobe's Pagemaker.\nSo I use it to control
    type sizes and colors and what have you.\nWhere CSS totally fails - in my opinion
    - is getting across to people like me that it can be used for far, far more than
    just type definitions.\nI am really not stupid and a relatively fast study but
    I cannot get to grips with it. My feeling is that perhaps people who DO understand
    CSS do not understand communication.\nAnd so potential users of the full scope
    of CSS - and I am one of them - stop half way simply because no one is giving
    and intelligent, intelligible, interesting, explanation complete with snazzy samples.\n\nGareth
    in Sussex where it is warm and wonderful. This week.
  comment_date: '2006-06-08 12:40:15'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1145'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Stacy: I''m well aware of the possibility of adding separate
    stylesheets but I don''t feel the need to add it. If an individual user wants
    to customize something they can use a custom stylesheet  and apply it.'
  comment_date: '2006-06-08 12:51:41'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '1153'
  comment_author: Debbie
  comment_author_url: http://www.parallaxwebdesign.com
  comment_content: I'm at level 5 and very comfortable with that. I don't plan on
    writing any books. :)
  comment_date: '2006-06-08 17:46:57'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1155'
  comment_author: Carla Pendergraft
  comment_author_url: ''
  comment_content: This seems like an inherently odd system. Usually, a higher level
    will include greater levels of skill. To me, it would make more sense to say a
    level 2 uses only the most basic CSS tags. The higher level would use perhaps
    more complex ones. Instead, this one focuses on attitudes toward CSS. So it's
    not levels of knowledge with a gradual progression toward sophistication. It's
    just a bunch of attitudes, some of which you say yourself not really "better"
    or "worse" than other, higher levels. You ought to reformat this whole "levels
    of learning" table into some other semantic structure.
  comment_date: '2006-06-08 17:50:36'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1156'
  comment_author: Roman
  comment_author_url: http://www.ctinc.ca
  comment_content: 'If claim "I’m very much pro web standards. The current widely
    accepted standards are: (X)HTML" why does this page read "" as it''s first line?\n\n:-)'
  comment_date: '2006-06-08 19:00:08'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1157'
  comment_author: Roman
  comment_author_url: http://www.ctinc.ca
  comment_content: The HTML line in my previous post was just cut out instead of converted
    to display HTML. Just right click the page and "View Page Source". Then read the
    first line.
  comment_date: '2006-06-08 19:04:29'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1170'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Carla Pendergraft: I believe that CSS is an entirely different
    mindset from table based design. To grasp that new mindset there are several things
    you need to understand and I believe those things are in the list above.\n\n@Roman:
    Note the paranthesis around the X.  I continuosly recommend that you use either
    HTML or XHTML (doesn''t matter which) as long as you use the strict versions.
    Feel free to look through the sourcecode of this site, I have nothing to hide.'
  comment_date: '2006-06-09 00:25:18'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '1172'
  comment_author: ben
  comment_author_url: ''
  comment_content: I'm a class 5 mutant, and I love to play CS:S but more of a 1,3,5
    level CSSer.  I like CSS, it is very cool.  Not the total final solution for all
    things.  I would have to agree that a lot of articles about CSS and web standards
    sound very elitist and annoying, this one is partially included, although not
    too mean.  (A side note, whether you intended it to or not doesn't matter, it
    still sounds that way :)) It would be ok to just admit it, or say sorry, but that
    wouldn't be very CSS-Elitist like.  Still an interesting read. Thanks :)  -Nightcrawler
  comment_date: '2006-06-09 01:02:21'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1196'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@ben: Sorry!'
  comment_date: '2006-06-09 09:33:59'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '1210'
  comment_author: David Golding
  comment_author_url: ''
  comment_content: A very informative article - thank you. Mix of level 2 and 3 now
    inspired to achieve 5...
  comment_date: '2006-06-09 13:29:07'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1212'
  comment_author: T-dude
  comment_author_url: http://tibit.net
  comment_content: 'Word!\nThere is another interesting .class of people: The postbubblers.
    they learned the craft without knowing what IE5 or Netscape 4 <em>was</em>. Many
    of them use different techniques, tool etc, but don''t know or care about standards.
    However, with their fast learning curve, they probably could make a significant
    contribution to web standards use. I know I''ve met a few, but didn,t have the
    time, knowledge or patience to convince them at the time.'
  comment_date: '2006-06-09 14:03:47'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1249'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@T-dude: Good addition, those people need to be talked to and
    convinced. Send them here :)'
  comment_date: '2006-06-10 02:02:20'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '1271'
  comment_author: Evaluate your CSS and HTML Knowledge @ SEO Principle | Search Engine
    Optimization Blog
  comment_author_url: http://www.seoprinciple.com/evaluate-your-css-and-html-knowledge/10/
  comment_content: '[...] I came across an article that is both funny and accurate
    called Levels of CSS knowledge, from Emil Stenström. It lists 6 levels of CSS
    knowledge and explains how each one is affecting the web, from the average user
    to the most renowned web designers. [...]'
  comment_date: '2006-06-10 15:29:11'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1334'
  comment_author: Henrik Feldt
  comment_author_url: ''
  comment_content: You don't have to have written a book about css to be at level
    6, really ;); at least that's what I think, and perhaps some people above have
    said so, too. The problem with level 6 in your article is that it assumes that
    if you know css very well, you automatically start to write about it and tell
    people how to use it. That's not the case for me. It's very seldom I stumble upon
    something that I don't know in CSS, for example.\n\nAlthough I have actually started
    to write a very long tutorial on how to start with CSS, it just takes too much
    time. What I would love to do would be to be a web design teacher - and not only
    html and css, but also c#/ASP.net, n-tier, javascript, graphical design (photoshop/flash/illustrator).\n\nThat
    would be great fun!
  comment_date: '2006-06-11 17:34:01'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1336'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Henrik: I belive the differece between 5 and 6 is to reach out
    and teach other people what you know.  A 5:er and 6:er might even know as much
    about the language. Teaching would be fun!'
  comment_date: '2006-06-11 17:41:03'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '1376'
  comment_author: Spanky
  comment_author_url: ''
  comment_content: While these are funny at times. I wonder what are you doing to
    help change the situation? To help people understand what YOU see in CSS!! It's
    like laughing at the kid whose fly is undone without telling him it's undone ...
    immature and doesn't move you forward.\nStep up. Be bigger than you are.
  comment_date: '2006-06-13 01:23:25'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '1386'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Spanky: This whole site is my way of helping people "get" CSS
    and modern web development. I''ve heard several people that has been motivated
    by reading this article. Feel free to give suggestions on other ways to help people,
    I''d love to hear them.'
  comment_date: '2006-06-13 09:58:56'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '1402'
  comment_author: The Lime Blog &raquo; Role Playing and Web Design
  comment_author_url: http://www.diamondlime.com/Blog/?p=76
  comment_content: '[...] Go to FriendlyBit to determine your CSS level [...]'
  comment_date: '2006-06-13 21:53:48'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1406'
  comment_author: arconati.net &raquo; Blog Archive &raquo; links for 2006-06-01
  comment_author_url: http://james.a.arconati.net/?p=85
  comment_content: '[...] Friendly Bit » Levels of CSS knowledge As you might have
    understood by now I’m very much pro web standards. The current widely accepted
    standards are: (X)HTML for page structure, CSS for design, and Javascript for
    behaviour. HTML is pretty well known by now, it has been there since the begin
    (tags: web-developer web-developer/css reference community articles blogs) [...]'
  comment_date: '2006-06-14 07:52:00'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1411'
  comment_author: wigblog &raquo; Blog Archive &raquo; Levels of knowledge…
  comment_author_url: http://thinkmuch.com/blog/archives/2006/06/13/levels-of-knowledge/
  comment_content: '[...] Levels of CSS knowledge [...]'
  comment_date: '2006-06-14 08:36:12'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '1433'
  comment_author: Soup
  comment_author_url: ''
  comment_content: '@Spanky: You bitter about something? This article''s tone was
    professional and friendly, and has helped me better gauge where I''m at with CSS
    and where I''m going. I don''t feel laughed at. Why do you?'
  comment_date: '2006-06-15 01:40:30'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '2601'
  comment_author: Tombrarian &raquo; Levels of CSS Knowledge
  comment_author_url: http://tombrarian.wordpress.com/2006/06/28/levels-of-css-knowledge/
  comment_content: '[...] Emil Stenström over at Friendly Bit has come up with 6 levels
    of CSS knowledge. In theory, I’d optimistically put myself around level 5 because
    I had developed a test site for the library that used CSS positioning instead
    of tables. However, our university Web team has not bought into CSS positioning,
    so the new library site will still be laid out using tables. To be fair, designing
    a site as complex as a library site using CSS positioning is quite a challenge.
    The test site I developed still had a long way to go before I would have been
    satisfied with it. [...]'
  comment_date: '2006-06-28 17:20:55'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '2790'
  comment_author: Ian
  comment_author_url: http://www.elementaldesign.co.uk
  comment_content: I'm level 3.5 with the skills of Level 5! By that I mean produce
    good CSS but some elements of page are better done with tables in my view. For
    example, position something 50 pixels from the right margin sound sgreat but if
    someone has a very low resolution or very high, then this just won't work and
    causes the section positioned to cover another part of the page.
  comment_date: '2006-07-02 07:36:11'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '3210'
  comment_author: Dutch
  comment_author_url: http://home.planet.nl/~nieu0151/
  comment_content: At this moment I start a new mirrorwebsite (access still via my
    old website, I'm still busy with searching on the web) and I use since a short
    time a first css file.\n\nI'm glad reading this at this moment knowing and I hope
    remembering some traps. Great article, I saw a lot familiar items, I hope I don't
    make these failures and will keep clean work in my future css.\n\nDutch (webs
    nickname)
  comment_date: '2006-07-21 20:38:38'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '3309'
  comment_author: JesterBlue
  comment_author_url: ''
  comment_content: Very nice article; and the comments -- looks like some people worked
    hard at learning to flame and, by golly...\nA friend emailed me a link to this
    and laughed at my level 2 stripes.  There is fun in working through issues, learning,
    and solving problems.  If we didn't enjoy this aspect of the work, we would probably
    have a miserable time being sand-rakers in BoraBora golf courses too.\nHere's
    the wrinkle (from my twisted level-2 view) -- I don't get why tables, with CSS
    bits, are worse than div(ot)s -- it all looks pretty sloppy to me.  \nFeel free
    to rub my nose in it 'till I get it -- I'm a big boy.
  comment_date: '2006-07-25 04:17:44'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '3795'
  comment_author: Leon
  comment_author_url: ''
  comment_content: Hey Emil! I just found your website today and it is excellent.
    It has inspired me to rebuild my page and maybe even add some tech/CSS/XHTML articles!\n\nI'm
    from Russia but currently live in NYC doing WebDesign/Development for a firm.\n\nI
    will be redesigning their website to eventually implement CSS/XHTML (right now
    its just HTML/PHP).\n\nThanks again!
  comment_date: '2006-08-14 20:33:17'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '3821'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@JesterBlue: I''m working on an article on why you shouldn''t
    use tables for layout, stay tuned ;)\n\n@Leon: That''s fantastic to hear! :) Keep
    up with the good work.'
  comment_date: '2006-08-16 12:36:14'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '3874'
  comment_author: Markus from Frankfurt
  comment_author_url: http://4wdmedia.de
  comment_content: Year, but what about Mr. Spooks? He might be a level 7 agent! ;)
  comment_date: '2006-08-20 22:01:34'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '3891'
  comment_author: Mark
  comment_author_url: ''
  comment_content: Sounds a little bit elitarinist. And I hate pages that can't be
    saved to harddisk just because they use some feature that are incompatible with
    the dirty browsers were forced to live with - at least as long as I get a more
    than 50% guarantee I will find a broken link instead of interesting content if
    I bookmark or link instead of saving to disk. \nPeople profiting from incoming
    links for their google rankings while not caring for the webmasters that have
    to check broken links all the time instead of creating new content are the REAL
    web problem today, not levels of (technical) design purity.
  comment_date: '2006-08-22 22:13:59'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '3894'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Mark: Agreed, a lot of other aspects of the web are more important
    than the technical knowledge one posess. What matters here is that knowledge about
    CSS does not hurt the other areas, in terms of accessibility it might even help.
    \n\nClaiming that the above list was all that was needed would be elitist, that''s
    why I don''t.'
  comment_date: '2006-08-22 23:57:57'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '4200'
  comment_author: links for 2006-07-25 at willkoca
  comment_author_url: http://www.willkoca.com/2006/07/25/links-for-2006-07-25/
  comment_content: '[...] Friendly Bit » Levels of CSS knowledge (tags: css webstandards
    webdesign) [...]'
  comment_date: '2006-09-01 06:59:49'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '4391'
  comment_author: Aaron
  comment_author_url: ''
  comment_content: Nice article, but you already knew that since it is the most popular
    on your site.  I would just like to point out a slight typo in the level 0 paragraph.  In
    the first sentence "These people have probably never made a webpage in their life.
    If they did it was pure HTML and they barely knew what they where doing." it appears
    that you use the word where, when I believe you meant to type the word were.  Again,
    thanks for the informative article.  Oh and feel free to delete or not to publish
    this comment, it is just meant for the web admin.
  comment_date: '2006-09-07 21:19:21'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '4395'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Aaron: Thanks for the comment, typo fixed and compliment recieved
    :)'
  comment_date: '2006-09-07 21:55:57'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '4547'
  comment_author: brian
  comment_author_url: ''
  comment_content: i'm a 2!\nhahaha\n\nTables rock. Using 100% CSS takes way to long
    to get looking right on all browsers, and is also stupid. There are plenty of
    other plain HTML tags out there that get the job done very easily, rather than
    spending the agonizing time trying position everything solely with CSS. What are
    we doing here? Are we trying to abolish html? Are tables "of the devil"?  I say
    design how you want. If you're comfortable with nothing but CSS and divs, then
    heck, use it. If tables work for you and it makes you proficient in web design,
    use them. Not trying to argue with anyone, i just don't see the point and saying
    one is better than the other... I think some people stop realizing the reason
    for CSS. Heck, i saw a website that a guy created a table completely out of CSS...
    The code was insane!! Why bother... Anyway, funny article. I like the way you
    broke them down, I can recall getting to each of those levels (except for the
    book one). It's obvious you've "been there".  :)
  comment_date: '2006-09-11 19:17:39'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '4548'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@brian: Thanks for your comment! CSS is really about separating
    the content from the design. If you don''t agree with that design goal, then use
    tables all you want. After learning CSS and now getting employed because of it,
    I really feel it''s the best way of constructing a good website.'
  comment_date: '2006-09-11 19:32:56'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '4706'
  comment_author: Stephen Tudor
  comment_author_url: ''
  comment_content: I appreciated your article and didn't find it condescending at
    all, Emil.  Several commenters seem (perhaps rightfully) insecure about their
    own code fu with CSS.\n\nHowever, I can't help but wonder if I would have a similar
    reaction if I were a bit lower on your hierarchy.  I'm not a 6 yet, but I'd definitely
    like to get there at some point.\n\nI personally know people in each level you
    describe, and I think I'm now better equipped to help them out where they are.  Good
    perspective.
  comment_date: '2006-09-15 16:00:13'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '5234'
  comment_author: Levels of RSS Knowledge &laquo; Sweet!
  comment_author_url: http://notronwest.wordpress.com/2006/09/28/levels-of-rss-knowledge/
  comment_content: '[...] I have posted a bit on RSS and while I am not a “super”
    expert on RSS but I am a big fan and I have posted a bit on this topic in the
    past so when I saw the following link: “Levels of JavaScript Knowledge” which
    was based on “Levels of HTML Knowledge” which was in turn based on “Levels of
    CSS Knowledge” I thought - what better way to describe what I have seen lately
    as we hire for PaperThin. [...]'
  comment_date: '2006-09-28 06:08:06'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '6095'
  comment_author: James Clements
  comment_author_url: ''
  comment_content: 'I''m at level green, or maybe z. Consider this: Instead of just
    two categories, content and styles, there are three: content, styles, and layout.
    In the beginning people used tables for layout because there was a need for layout.
    Then people found they could use css for layout. In both cases you''re using a
    tool to do something it wasn''t really intended for. What''s needed is a true
    layout tool. Until we have that the fact is that tables for layout is easy and
    css for layout is hard. There are reasons to prefer one over the other, but it
    is mostly a personal preference.'
  comment_date: '2006-10-26 22:05:38'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '7266'
  comment_author: Ivan
  comment_author_url: ''
  comment_content: Excellent breakdown.  I can categorize myself at level 3.  I might
    have gone higher, but I made the transition to backend developer and no time was
    left to take css through mastery.  I'm glad you highlighted the difference between
    someone who claims mastery and someone who actually is;  I believe the distinction
    is very important.
  comment_date: '2006-11-16 20:34:00'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '7276'
  comment_author: Nomar
  comment_author_url: http://www.kingnomar.com
  comment_content: Good Article, I think I am on Level 2 or 3, I use it a little,
    but not that much
  comment_date: '2006-11-16 22:56:05'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '7380'
  comment_author: Fwitz
  comment_author_url: ''
  comment_content: I enjoyed the comments rather more than I did the article, which
    has  naive overtones. I can understand why so many people were put off, and conversely,
    why so many others found the urge to rate themselves somewhere in the 5-6 range
    so compelling. So maybe that makes it a successful article :) \n\nWhile the rating
    system is flawed, it is important to emphasize the places where graphic design
    ends and web design begins. \n\nWhat chaps my ass are the graphic designers who
    couldn't code their way out of a paper bag in any language, least of all CSS or
    HTML. Such "web designers" try to place themselves above the "coders," and sometimes
    I get the same vibe from designers who know CSS as well, that they hide their
    lack of understanding of programming underneath an assumed arrogance. Whatever.
    The web won't wait for them either.\n\nI don't care if a designer uses HTML or
    CSS as long as the thing works. And if I have the misfortune  of having to work
    with someone's super-messy HTML code I'll write a script to clean it up.\n\nHowever,
    I don't find your argument so convincing. I my experience, CSS - OTHER people's
    1000+ line CSS convolutions - has been at times as more difficult to work with
    than tables. At least with HTML, it's all there in front of you, and if you know
    HTML, you know the few browser discrepancies. But with CSS, the separation of
    content and presentation only magnifies the problem when the CSS is convoluted
    and poorly designed. \n\nYour Level Six CSS Guru could also be a real pain to
    work with, and so I think your system is not completely accurate. Just because
    you "found a job" because of your CSS does not mean that CSS is the cat's meow
    for every situation.\n\nI still use HTML tables at times, because it's easier
    for me to know EXACTLY where things will go when a database is spitting out the
    content through a loop. It's not worth my time or my client's money for me to
    code in a way that is as of today only marginally advantageous (at least to my
    clients), unless if I aim to please the CSS pundits, which I don't. \n\nAnd since
    I generate most of my resulting output programatically anyway, it's much easier
    to call a php  function that spits out a clear gif dot at my desired dimensions
    rather than coding a div just for that purpose.\n\nFor me, CSS is useful for page
    layout, but HTML also has its place for its granularity and guaranteed rendering.
    It is possible to rock out with both.\n\nThanks for the article. \n
  comment_date: '2006-11-18 19:29:52'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '7387'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Fwitz: As you probably know I don''t agree with your that using
    tables for layout is OK. I doubt I''d be able to convince you in these comments
    though so I won''t even try :)\n\nThe level system is not a scale of how easy
    people are to work with, just how good they are at CSS. Don''t confuse it with
    anything else...\n\nThanks for your comment and perhaps stay a while? I just might
    convince you in a couple of articles :)'
  comment_date: '2006-11-18 21:36:54'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '7440'
  comment_author: Fwitz
  comment_author_url: ''
  comment_content: nah, I'm not looking to be conviced of anything. I know what I'm
    doing. Good luck.
  comment_date: '2006-11-19 17:09:23'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '8014'
  comment_author: RJay
  comment_author_url: http://www.rocketjam.com
  comment_content: I had to read this to find out where I stand in your rating system.
    I'm probably almost a 4. I'd really like to get competent at CSS because I think
    it will help me maintain and update the two sites I take care of.\nI've successfully
    done a couple of pages with more than a basic layout, but really getting my head
    around it is kicking my ass.\nI've purchased a couple of books, which sometimes
    give conflicting advice which doesn't help. And the pages I've done, don't degrade
    "gracefully" in old browsers and I'm not sure why.\nAnyway, I enjoyed the article,
    and will continue to try to "get" CSS.
  comment_date: '2006-11-29 00:29:59'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '8059'
  comment_author: John Schwartz
  comment_author_url: ''
  comment_content: Thanks for the article. I'm wondering if you have a post/article
    somewhere that goes into depth about proper use of divs? :)
  comment_date: '2006-11-29 18:04:32'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '8070'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@John Schwartz: Only use them for the main sections of your site.
    It''s that easy. :)'
  comment_date: '2006-11-29 20:45:13'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '11813'
  comment_author: Jessi
  comment_author_url: ''
  comment_content: Year, but what about Mr. Spooks? He might be a level 7 agent! ;)
  comment_date: '2007-01-01 16:28:21'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '16356'
  comment_author: Swing tanzen verboten! &raquo; Levels of knowledge
  comment_author_url: http://swing-tanzen-verboten.de/wordpress/index.php/2007/01/10/levels-of-knowledge/
  comment_content: '[...] CSS [...]'
  comment_date: '2007-01-25 22:47:14'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '19367'
  comment_author: Tom from Yaway
  comment_author_url: http://www.yaway.de
  comment_content: Thanks for this great article. I build websites with CSS since
    2004 and i think I´m on level 5. i love it. CSS changed my way of designing and
    programming   web projects.
  comment_date: '2007-02-05 22:38:17'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '21253'
  comment_author: techblog.tilllate.com &raquo; Unsichtbare Tabellen zur Seitengestaltung?
  comment_author_url: http://techblog.tilllate.com/2007/02/14/unsichtbare-tabellen-zur-seitengestaltung/
  comment_content: '[...] und ULs gestapelt. Das gibt den CSS-Zen-Garden-Effekt, wenn
    man das Stylesheet deaktiviert, das den Level 4-CSS-Anwender strahlen [...]'
  comment_date: '2007-02-14 22:32:22'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '23116'
  comment_author: One night in paris
  comment_author_url: ''
  comment_content: I’d say Level 6 but I haven’t found any reasons for using CSS3
    (or, the other half of CSS2). So, I guess that would - Actually - be 5. I guess
    I could Malarkey two different sites, i.e., Two Tone and Mod, but IE 7 ruined
    that.
  comment_date: '2007-04-06 08:47:12'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '23176'
  comment_author: Anders M.J.
  comment_author_url: ''
  comment_content: '@One night in paris,\nThe new features in the CSS3 specification
    isn''t supported by any browser yet so you can''t use it yet.'
  comment_date: '2007-04-08 12:34:01'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '23360'
  comment_author: fee
  comment_author_url: http://www.blog-gu.com
  comment_content: Excellent breakdown. I can categorize myself at level 3. I might
    have gone higher, but I made the transition to backend developer and no time was
    left to take css through mastery. I’m glad you highlighted the difference between
    someone who claims mastery and someone who actually is; I believe the distinction
    is very important.
  comment_date: '2007-04-14 16:14:32'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '23551'
  comment_author: IPC
  comment_author_url: http://www.ipc.at
  comment_content: Interesting article. I think I am between 4 and 5.
  comment_date: '2007-04-20 08:02:57'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '24112'
  comment_author: Jason’s Weblog &raquo; Levels of Web Designer Knowledge
  comment_author_url: http://evolv.cc/2006/12/28/levels-of-web-designer-knowledge/
  comment_content: '[...] Levels of CSS Knowledge [...]'
  comment_date: '2007-05-11 05:19:46'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '24572'
  comment_author: tom barnfield
  comment_author_url: http://www.runninghead.com
  comment_content: Someone once said using CSS is like skiing down a mountain safe
    in the knowledge that, while the bridge at the bottom may be out, repairs are
    scheduled for next Tuesday. Still think accessibility's a waste of time. No CSS?
    javascript turned off? images turned off? Are you sure your computer's not still
    in the box?
  comment_date: '2007-05-23 17:18:22'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '24814'
  comment_author: Dave Spreefelt
  comment_author_url: ''
  comment_content: I wish to gosh the Level 2 designation were true and CSS didn't
    have a collection of browser-only hacks.  People who know the pitfalls of div-only
    layouts and revert to a CSS/tables mix obviously know what they're doing.  Swap
    Level 5 and level 2.  Show me a div-only site that uses relative positioning successfully.   Youre
    site doesn't.
  comment_date: '2007-05-30 18:06:05'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '24815'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Dave Spreefelt: What do you mean by relative positioning? I certainly
    don''t agree with you.'
  comment_date: '2007-05-30 18:28:20'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '24822'
  comment_author: Dave Spreefelt
  comment_author_url: http://joeclark.org/book/sashay/serialization/Chapter10.html
  comment_content: couldn't say it better myself, see the link...
  comment_date: '2007-05-30 22:33:01'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '24878'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Dave Spreefelt: That article says: "You can have tables and still
    be accessible". At the same way you can drink poison and not die, seems logical
    to me...'
  comment_date: '2007-06-02 00:07:12'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '24887'
  comment_author: tom barnfield
  comment_author_url: http://www.runninghead.com
  comment_content: '@Dave Spreefelt\nIt''s easier to do layout with tables certainly.\nNo
    hassles with absolutely positioning elements in relatively positioned ancestors
    while floating your div to the left in both compliant and non-compliant browsers,
    blah blah, blah... man, I thought CSS was meant to increase clarity!? ;)\nSeriously
    though I love CSS and having tried both table and css methods I''d have to say
    CSS is, on the whole, better. If there are people out there who aren''t using
    relative positioning properly it''s just poor design, not an issue with CSS.\n
    Table-based designs have been around longer and any idiot can  use tables to layout
    content but that apparent simplicity comes at a cost. Next to modern, well-formed
    CSS designs they look amateurish and restricted. Css is actually not unreliable
    or obscure, and once you''ve made the effort to really learn it everything does
    become clear and simpler and a whole lot easier to maintain and change.'
  comment_date: '2007-06-02 07:54:11'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '25549'
  comment_author: Levels of CSS knowledge
  comment_author_url: http://www.narga.net/138/levels-of-css-knowledge/2006/03/27
  comment_content: '[...] Full article here, very good content  As you might have
    understood by now I’m very much pro web standards. The current widely accepted
    standards are: (X)HTML for page structure, CSS for design, and Javascript for
    behaviour. HTML is pretty well known by now, it has been there since the beginning
    of the web and there are tutorials everywhere that gets you started. CSS is starting
    to get a grip, large companies are switching their sites to CSS based layouts
    and the webdev blogosphere reaches more and more people. [...]'
  comment_date: '2007-06-24 05:15:56'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '29940'
  comment_author: Antony Williams
  comment_author_url: ''
  comment_content: I'm at level somewhere between 3 and 5. Help!!\n\nAnt :0)
  comment_date: '2007-12-08 16:01:22'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30112'
  comment_author: 'Sexta-feira dos Web Standards #10 &middot; project.47 - Portfolio
    e blog sobre Web Standards'
  comment_author_url: http://project47.viscountbox.com/sexta-feira-dos-web-standards-10/
  comment_content: '[...] Levels of CSS knowledge - Como o t?tulo diz, este artigo
    mostra os diversos n?veis de conhecimento em CSS e suas particularidades. Interessante
    para saber em qual n?vel voc? se enquadra. [...]'
  comment_date: '2008-01-12 02:58:08'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '30139'
  comment_author: Mukesh Yadav
  comment_author_url: http://cssmantra.wordpress.com
  comment_content: Great it's motivating article i feel i am level 4 and slowly moving
    to 5.............
  comment_date: '2008-01-17 11:09:16'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30187'
  comment_author: NicMartel
  comment_author_url: ''
  comment_content: 'Wonderful... the discussion generated combined with the article
    is what makes it all a positive experience. My level is a wannabe 5, yet I am
    forced to stagnate at 4 because I am too busy on rush jobs.  It would be nice
    if some one could kick me in by showing me where I can find a sample CSS layout(as
    follows):  Left navigation pane with a percent width and a right display pane
    to take up the rest of the screen, a bottom pane(footer) about one to 2 lines
    high that never leaves the screen.  I am able to do that with frames quite easily.  The
    left pane is programmatically populated from DB with image thumbnails links that
    trigger a full size image in the right pane. The bottom pane(full screen width)is
    reserved for controls the user interacts with.  The left pane of course scrolls
    up/down without interfering with the bottom pane.  I can also programmatically
    negate the left pane so that the right pane takes the full width of the screen,
    again the bottom pane is still visible and unaffected.  Finally I can hide and
    show a 4th pane(frame), that is the same width as the right pane and 3 to 5 lines
    high to display some description and allow some interaction with controls. All
    functions via javascript except the left pane which requires a redraw when reloaded.  I
    am able to control the size of the frames via javascript or by simply grabbing
    the invisible borders of the frames so the thumbnails can be made larger automatically,
    and scrollbars appear/disappear as needed on the proper verticals or horizontals.  I
    stress again, the bottom pane NEVER is affected, it is always on the screen with
    its controls in their various states, and it is FULL SCREEN width... Will I be
    able to match this layout and functionlality with CSS?  If so, will the different
    sections be DIVs? will I be able to get and set the width/height and height of
    the different sections as I now do with the frames via javascript? Also, when
    I display an object that is larger than the available space(pane), will the object
    oveflow BEHIND the other panes leaving them completely unaffected?  I am most
    appreciative.'
  comment_date: '2008-01-25 18:11:14'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30190'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@NicMartel: This is not the right place to get help coding a full
    CSS layout. Try googling for "layout gala", you might find something there.'
  comment_date: '2008-01-25 21:43:55'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '30193'
  comment_author: NicMartel
  comment_author_url: ''
  comment_content: Emil, thank you for the pointer... I had looked and looked and
    found nothing... hopefully this will do the trick.  I actually do not need help,
    as I have since coded my first layout to match the above description...  was just
    trying get some up-front information to save me from finding out the hard way
    that CSS may not meet my requirement.  Thank you.
  comment_date: '2008-01-26 14:07:26'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30432'
  comment_author: Dmitri Farkov
  comment_author_url: ''
  comment_content: Skimmed over. One problem I have is the statement that CSS is better.
    I am sure you meant it for the layout purposes. One must never forget though,
    tables are designed for tabular data, no amount of css will replace formatting
    of tabular data in tables. Very humorous article otherwise.
  comment_date: '2008-03-14 04:55:42'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30436'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Dmitri Farkov: If you had followed the site more closely you
    shouldn''t have to point out silly things like that. Of course tabular data should
    be in tables.'
  comment_date: '2008-03-14 12:05:50'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '30533'
  comment_author: resimler
  comment_author_url: http://www.resimden.com
  comment_content: Excellent breakdown. Most people would have tried to break it into
    3 levels, but I think all 6 of yours are necessary and distinct.
  comment_date: '2008-04-08 03:10:44'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30596'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: Interesting. And fun to read. Although i wonder what level i'd
    be :)\nI'm a software developer since more than 30 years now. I got hands on computers
    before the mouse was invented, and so i'm used to use console and extremely simple
    text editors for all. As i see it, this has some advantages in understanding what's
    going on.\nWeb coding is not my profession, it is more a hobby. So i'm not bothered
    with pressure to blow out half-done sites and have every time to tinker with the
    features and possibilities of the web. I really do understand people not having
    the time to produce perfect pages.\nThe separation of different parts is bare
    basics in software development and is called modularization. So separating content
    (and its semantics) from presentation and behaviour for me was quite logical.
    Although it took some time to actually do this consequently (more or less :) ).
    I think it's worth every second of learning it. And in fact, if you do it really
    consequently you do not need more time to produce sites, you need less time. But
    if you stick to combining all three parts into the html, and then just pro forma
    pull out the css into a separate file you have a hard time.\nSo consequently i
    do not agree with one of the statements found at the w3c. There it says, that
    the main purpose of class and id attributes is to provide a handle to css (presentation).
    That could not be true. Those classes and attributes are part of the html and
    as this part of the semantic. So consequently classes and ids are to be used to
    add semantics to a content. In cases of div and span this means setting the only
    semantics this content has, since these 2 do not have own semantics. For other
    elements class and id attributes are to make the semantics of their content more
    precise. This adding to semantic has absolutely nothing to do with presentation.
    These classes _can_ be used as css handles, but their main purpose is pure semantics,
    nothing else. If you are able to separate that consequently, you actually do not
    style words, you style semantics. And if you do so, you have a much easier way
    then afterwards. And, as a nice benefit, you get a much easier maintenance for
    sites then. The only drawback is that you have to master a long and sometimes
    painful learning curve. And this is the longer, the more experienced you are with
    html 3.2.
  comment_date: '2008-05-17 17:47:00'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30790'
  comment_author: Dmitri Farkov
  comment_author_url: ''
  comment_content: '@Emil Stenström: Just a tad rude, no?'
  comment_date: '2008-06-30 04:54:53'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30792'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Dmitri Farkov: Yes, sorry. Got a little annoyed with the "skimmed
    over your article and think you''ve fundamentally misunderstood CSS". I see now
    that you didn''t mean it like that.'
  comment_date: '2008-07-01 07:58:45'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '30801'
  comment_author: lyndonaus
  comment_author_url: ''
  comment_content: Level-wise, I think I am somewhere in L4 but scratching hard to
    climb up to L5. \nI do web sites for non-profit organisations as a volunteer,
    having developed my interest over the last couple of years in my retirement. I
    believe that standards should be followed and it is so frustrating when I (and
    thousands of others)discover that IE does not do as expected.\nFor the second
    time to-day I find myself in awe at the ease in which layout problems can be solved
    so easily, particularly, those relating to IE6 using code from this site.\nThanks
    again!!!
  comment_date: '2008-07-08 07:47:37'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30857'
  comment_author: miko
  comment_author_url: ''
  comment_content: pogi ako
  comment_date: '2008-07-25 03:41:39'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30983'
  comment_author: Carla Pendergraft
  comment_author_url: http://www.carlapendergraft.com
  comment_content: 'You know, I just think it has to relate back to your goals. If
    your goal is purity, go for pure CSS. If your goal is to rapidly produce websites
    that use tried and true methods (and for me, that''s a combination of tables and
    CSS), then a hybrid approach is best. I look for the way I can get a properly
    working, stable website up and running without fuss. Once the browsers are better
    at implementing CSS in a consistent way, I''ll make the switch to the "pure" system.
    \n\nAnd my complaint against CSS is that every time I use some clever new technique
    (example: opacity), it breaks in Safari or whatever. It wastes my time because
    of the inconsistent rendering. You know, we used to have font tags peppered all
    over our pages. In some ways, things haven''t improved. I have seen style sheets
    that were so ridiculously long, I can''t imagine anyone could have understood
    them. We''ve separate the replacement for our old font tags from the actual content,
    but sometimes it doesn''t look like the greatest improvement to me, if one is
    in favor of simplicity.'
  comment_date: '2008-09-03 14:26:16'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '0'
- comment_ID: '30991'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Carla Pendergraft: You know, CSS is a tried technology. I''ve
    used it professionally for two years now, and about two more on private sites.
    There is really no need for tables. Really. I also work in a highly agile environment
    where things change often, and I thank CSS for me being able to change that quickly.\n\nOpacity
    is a CSS3 feature, so it''s hardly working anywhere. Floats do work, have worked
    for a long while, and replace tables nicely.\n\nYou can write bad CSS, but you
    don''t have to, do you? If YOU know what''s good and bad, there''s no reason to
    repeat what others did.'
  comment_date: '2008-09-04 22:37:45'
  comment_post_ID: '33'
  comment_type: null
  is_admin: '1'
- comment_ID: '31675'
  comment_author: 'Levels of knowledge : Rebecca Thomas Designs'
  comment_author_url: http://rebeccathomasdesigns.com/2006/06/13/levels-of-knowledge/
  comment_content: '[...] CSS (I’m at Level 5, surprisingly, but I think it’s because
    of how I learned CSS.) [...]'
  comment_date: '2009-03-27 19:59:21'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33307'
  comment_author: I livelli di conoscenza dell’HTML &raquo; chalda.it
  comment_author_url: http://blog.chalda.it/i-livelli-di-conoscenza-dellhtml-58.html
  comment_content: '[...] livelli di conoscenza dell’HTML   Prendendo ispirazione
    dai Livelli di Conoscenza del CSS di  Emil Stenström,  ho iniziato a pensare ai
    diversi gradi di   conoscenza dell’ HTML  tra le persone che [...]'
  comment_date: '2009-12-01 02:30:29'
  comment_post_ID: '33'
  comment_type: pingback
  is_admin: '0'
---