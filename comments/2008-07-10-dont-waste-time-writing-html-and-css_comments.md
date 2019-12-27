---
comments:
- comment_ID: '30806'
  comment_author: trobrock
  comment_author_url: http://www.serenitydesignonline.com
  comment_content: These are some very good tips. I often times find myself writing
    way too much code for the project I'm working on just because I want it to be
    too portable. Thanks for this, bookmarking it for when I get stalled.
  comment_date: '2008-07-10 02:06:17'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30807'
  comment_author: Jrf
  comment_author_url: ''
  comment_content: Good article. Flagged.\n\nOne remark about the regex and matching
    more than you want:\nThis can be easily avoided. You rightly point out that regexes
    are <em>greedy</em>. To make a regex <em>non-greedy</em>, add an '?' after the
    repetition qualifier.\n\nFor your example:\n<strong>&lt;.+&gt;</strong> is greedy\n<strong>&lt;.+?&gt;</strong>
    is the non-greedy version
  comment_date: '2008-07-10 02:44:41'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30808'
  comment_author: Jrf
  comment_author_url: ''
  comment_content: Darn.. your comment filter does not like regexes with less than/more
    than signs in the comments.... oh well... \nI hope the example is still clear
    enough even though the regex has been cut in half.
  comment_date: '2008-07-10 02:50:42'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30809'
  comment_author: Charlie Park
  comment_author_url: https://www.pearbudget.com/
  comment_content: Probably my best time saver is to <strong>have a bomb-proof structure
    for the CSS file</strong>, that I know cold. I've developed one that takes a while
    to explain (won't bore you with it now), but that works really well, even for
    huge, gangly files. Whatever your method for managing your CSS file, having a
    standard way of executing it, and knowing exactly where to look to find "div#into
    p.highlight a:hover {}" is key. I know exactly where in the file that would be.
  comment_date: '2008-07-10 03:33:33'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30810'
  comment_author: Charlie Park
  comment_author_url: https://www.pearbudget.com/
  comment_content: (That was supposed to be "div#intro", but you know what I was getting
    at.)
  comment_date: '2008-07-10 03:36:14'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30811'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jrf: Good catch, I didn''t know about that. I hope many of the
    regexp dialects used knows it! I (think) I fixed your regexp by using &amp;lt;
    instead of starting angel bracket. \n\n@Charlie Park: ah, I knew I forgot about
    one important point. I also have a <a href="http://friendlybit.com/css/how-to-structure-large-css-files/"
    rel="nofollow">CSS structure</a> I use.'
  comment_date: '2008-07-10 07:10:53'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '1'
- comment_ID: '30812'
  comment_author: James Socol
  comment_author_url: http://coffeeonthekeyboard.com/
  comment_content: Good tips, but I disagree with your first point. If something contains
    text, I want it to be flexible and scalable so that when people change the font
    size, my entire layout does not break. To see what happens when you <em>don't</em>
    make things scalable, go to the New York Times website and hit Ctrl-+ a couple
    of times.\n\nAnd like Emil and @Charlie Park, I have a similar <a href="http://coffeeonthekeyboard.com/work-pattern-designing-web-sites-93/"
    rel="nofollow">CSS structure</a> that I use to avoid breaking things. It saves
    a lot of time.
  comment_date: '2008-07-10 14:25:35'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30813'
  comment_author: Don’t waste time writing HTML and CSS | WhiteSandsDigital.com
  comment_author_url: http://whitesandsdigital.com/wordpress/2008/07/10/don%e2%80%99t-waste-time-writing-html-and-css/
  comment_content: '[...] four best ways to be a more effective front-end developer.
    Feel free to add more ideas as comments!read more | digg [...]'
  comment_date: '2008-07-10 14:44:48'
  comment_post_ID: '169'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '30814'
  comment_author: Heather
  comment_author_url: ''
  comment_content: Interesting read, even though I was a little taken aback by the
    headline. Great tips to help streamline the process.
  comment_date: '2008-07-10 15:21:22'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30815'
  comment_author: Stephen
  comment_author_url: http://www.wardontheweb.com/
  comment_content: I'd add neat, organized, readable coding to the list.  You can
    make good coding a habit such that it takes little or no additional time but saves
    loads of time when you or someone else has to come back and modify that code.  I
    can't tell you how many times I've scratched my head wondering, "How many close
    div tags do I need here?" because the designer hadn't used proper indentation.
  comment_date: '2008-07-10 15:27:30'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30817'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: <blockquote>To see what happens when you <em>don’t</em> make things
    scalable, go to the New York Times website and hit Ctrl-+ a couple of times.</blockquote>\n\nLooks
    fine in Opera, Firefox 3 and IE7.
  comment_date: '2008-07-10 18:06:16'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30818'
  comment_author: James Socol
  comment_author_url: http://coffeeonthekeyboard.com/
  comment_content: '@zcorpan: When you get 100% of users to adopt those three browsers,
    you can stop worrying about it. Try in FF2. (Of course, IE6 only has 5 text sizes,
    but if your margin of error is too small, it''ll still break.)'
  comment_date: '2008-07-10 18:38:26'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30819'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@James Socol: Even though you want oldfashon text-size increase
    you can fix the width, but make it scalable in height. Piece of cake, and save
    lots of time there too.\n\n@Heather: Sorry for the headline! Thanks for the linkback
    :)'
  comment_date: '2008-07-10 20:09:02'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '1'
- comment_ID: '30826'
  comment_author: James Socol
  comment_author_url: http://coffeeonthekeyboard.com/
  comment_content: '@Emil: That works until you have a long word. Accessibility is
    a key requirement for most of the work I do, and people do triple or quadruple
    font-size, but even when it''s not, I want to control the number of characters
    per line. Changing line lengths changes the way people read your text. People
    read shorter lines faster, and tend to skim and miss information. Long lines,
    on the other hand, slow people down. If I make a column wide or narrow, it''s
    usually on purpose, and I don''t want to give that up.'
  comment_date: '2008-07-11 15:10:59'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30830'
  comment_author: Rasmus Kaj
  comment_author_url: http://rasmus.krats.se/
  comment_content: 'Fixed content widths is excusable in one case only:  When more
    time is spent writing the css than the sum of the time all readers spend on the
    site!\n\nAnd I''d like to reverse the first item!  :-)\n\nMost of a site can and
    should be developed in plain html+css.  When that is no longer practical, some
    xslt/jsp/php/etc and/or javascript can be usefull.  In extreme cases, even flash
    can have its points.\n\nLots of sites seems to use flash and/or giant javascript
    toolboxes for no actual reason.  That''s fine for a playground project, but a
    real project for a real client should be built up from the usecase, not down from
    the cool widget ...\n\nDespite this, a good text and sound advice.  Thanks!  :-)'
  comment_date: '2008-07-12 20:32:57'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30846'
  comment_author: Tyler
  comment_author_url: ''
  comment_content: 'Great Post.\n\nMany good tips for increasing productivity. One
    suggestion with tip #4 is to get a second monitor. Having side by side monitors
    has made me close to 30% more efficient. It''s difficult to work without 2 monitors
    now.\n\nTyler,\nhttp://www.whatdivs.com'
  comment_date: '2008-07-18 22:33:41'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30850'
  comment_author: David McNorton
  comment_author_url: http://www.eboracom.co.uk
  comment_content: Excellent tips!
  comment_date: '2008-07-20 12:52:19'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30853'
  comment_author: ask
  comment_author_url: ''
  comment_content: I'd like to add one to your list. <i>Prototype everything that
    you're not 100% sure you can do for real</i>. The earlier you can flag items that
    are going to be difficult or will take a long time to build, the less time your
    customer, or designer, or stakeholder has to get attached to them. And I've found
    that customers can be real people too and will def drop items if they know they're
    gonna take an age to build. Cheers. Ask.
  comment_date: '2008-07-22 18:05:16'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30862'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@James Socol: There is no good way to handle long words in CSS,
    so I can''t see how that matters in the case of rounded corners. Do you mean that
    all boxes should be wide enough to be able to contain long words?\n\n@Rasmus Kaj:
    For the special case of expert users I agree with you. But for most other cases,
    people don''t have any idea of how to resize the browser window, so they will
    get too long lines.\n\n@Tyler, ask: Good tips!'
  comment_date: '2008-07-28 21:06:40'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '1'
- comment_ID: '30950'
  comment_author: Rasmus Kaj
  comment_author_url: http://rasmus.krats.se/
  comment_content: No, I'm not saying that you should use the full browser width for
    text, just that pixels are the wrong unit for it.  Use the em unit or a percentage!  I
    tend to use percentages, but also specify a max-width for the actual text containers
    in ems.\n\nToo many sites specify a content width in pixels, and a tiny font.  A
    user who finds tiny fonts uncomfortable soon learns to change the font size (ctrl
    +), but then many layouts break down.
  comment_date: '2008-08-28 10:00:16'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30966'
  comment_author: Johan
  comment_author_url: ''
  comment_content: '- File versioning to improve workflow (simply a last modified
    date hard-coded can be a good start)\n\n- Reusing code blocks'
  comment_date: '2008-09-01 09:03:11'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30978'
  comment_author: Justin Ferrara
  comment_author_url: http://www.noamdesign.com
  comment_content: 'Thanks for the tips.  I''ve found that tip #3 is very helpful
    when developing larger web applications, especially frameworks.'
  comment_date: '2008-09-02 18:46:38'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30984'
  comment_author: chrisco
  comment_author_url: http://buzzpal.com/team
  comment_content: 'Hi Emil,\n\nFound your blog through a link on the Geek Meet Stockholm
    page.  Glad I found it :)\n\nThanks,\nChris\nBuzzPal.com/Team\n\nPS: I am looking
    for concept development / user experience / user interaction design type folks.  Let
    me know if you know any good ones or send them my way.  Thanks.'
  comment_date: '2008-09-03 19:30:23'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30992'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@chrisco: Sorry, I''m not looking for another job at the moment.
    Please don''t use my comment board as an advertising system.'
  comment_date: '2008-09-04 22:39:19'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '1'
- comment_ID: '30997'
  comment_author: James Socol
  comment_author_url: http://coffeeonthekeyboard.com/
  comment_content: '@Emil I didn''t mean CSS should be used to handle long words;
    I meant that if you have the word "Corporation" in a pixel-width box, and make
    the text bigger in the still-extremely-common last generation of browsers, or
    even Chrome, it will bleed over the edge, unless you <code>overflow: hidden</code>,
    I suppose. (The New York Times'' site always comes to mind.)\n\nTwo things which
    are, in my experience, true: people change the text size, and lots of people still
    use IE6 and Firefox 2.\n\nMaybe you can choose to ignore the needs of that audience.
    I can''t. Especially in light of the Target vs NFB settlement in this country.'
  comment_date: '2008-09-05 15:37:58'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '30998'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@James Socol: So what do you propose? Which are the longest word
    you will allow in your boxes? No limit?'
  comment_date: '2008-09-06 00:37:28'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '1'
- comment_ID: '31015'
  comment_author: James Socol
  comment_author_url: http://coffeeonthekeyboard.com/
  comment_content: '@Emil: There''s no arbitrary, universal limit for word-length.
    But long words don''t wrap when you scale the text in a fixed-width box (pixels
    or percent). Use ems or another flexible-width measurement.\n\nI''m not worried
    about default behavior. Hopefully the design properly handles all the text at
    its default size (or you can manually hyphenate). I''m worried about what happens
    when you hit <code>ctrl +</code>.'
  comment_date: '2008-09-08 17:59:19'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '31016'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@James Socol: I understand what you mean. My argument goes like
    this: You don''t know what text people will put on the site (it changes all the
    time). You have to somehow select what font-size you want to support, by looking
    at some sample text and guessing. If you still do that, it''s not that hard to
    pick a pixel size that handles two zoom levels well, and stick with that. If it
    saves lots of time, you can focus on hacking .NET to make it accessible instead.
    It''s all about priorities.'
  comment_date: '2008-09-08 20:39:19'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '1'
- comment_ID: '31048'
  comment_author: James Socol
  comment_author_url: http://coffeeonthekeyboard.com/
  comment_content: '@Emil: Two zoom sizes is not enough. And since this is about not
    "wasting time," why write functions to scale the text to your predetermined sizes
    when you can just use scaling layouts? Surely wasting time in .NET (or whatever
    else) is as bad as wasting time in HTML and CSS.'
  comment_date: '2008-09-22 18:05:38'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '31049'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@James Socol: is it <strong>never</strong> enough? I''m not talking
    about writing functions to accommodate for just a couple of zoom levels, I''m
    talking about using scaling layouts, but don''t care if it breaks when you zoom
    too much. When something like that is enough or not is determined by the project
    and is not something general you can decide without a context.'
  comment_date: '2008-09-22 18:19:33'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '1'
- comment_ID: '31056'
  comment_author: James Socol
  comment_author_url: http://coffeeonthekeyboard.com/
  comment_content: '@Emil: Accessibility is general, at least not in the US. The  National
    Federation of the Blind vs. Target settlement, while not the strong precedence
    of a ruling, still sets a legal precedent. Everything needs to be accessible or
    is open to suit.\n\nNow, maybe you can say the risk of law suits is minimal, or
    you''re too small to care, or you just don''t care. But if you use <code>em</code>s,
    it will scale by itself, so it can''t zoom "too much."'
  comment_date: '2008-09-22 21:21:58'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '31062'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@James Socol: Well, it seems our ways of looking at accessibility
    are different. I''m very much against the notion of forcing accessibility by the
    law. People just following the law will make a shitty job.\n\nWe seem to also
    have different ideas about how to make a scaling layout. It''s not just about
    throwing some ems in there. But we''re not getting anywhere with this discussion,
    so lets just concentrate on something else. Thanks!'
  comment_date: '2008-09-23 07:35:08'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '1'
- comment_ID: '31330'
  comment_author: Denver Web Development
  comment_author_url: http://www.netcompose.com
  comment_content: Since there are so many layout tricks out there now, especially
    using layered Div's combined with tables even can be very effective.  Once you
    find your grove and what works best for you, go for it...
  comment_date: '2008-12-19 01:56:58'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '31688'
  comment_author: Anonymous
  comment_author_url: ''
  comment_content: These are excellent tips, I think that helps a great deal is having
    a reset css file.  If some of you readers haven't heard of those, it is a css
    file that will set all your html element margin and padding to 0.  Having everything
    set to 0, then you can decide how much spacing everything needs, instead of the
    browser.
  comment_date: '2009-04-07 07:39:18'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '31803'
  comment_author: Justin
  comment_author_url: http://makingcolor.com/
  comment_content: Hah! I never thought I'd see the day when someone would finally
    post this about our lovely html...\n\nthanks,\nmakingcolor staff
  comment_date: '2009-06-24 22:36:08'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
- comment_ID: '33440'
  comment_author: Case pariuri
  comment_author_url: ''
  comment_content: Yep, this is what I recommend to my associate too..he's wasting
    way too much time on CSS for every round corner to have a nice time. And when
    you're done doing everything and you see that an IE6 just cannot run your new
    designs, you need to start doing "the hard job". I strongly believe that Internet
    2.0 is more and more affected by the state of simplicity. All good websites have
    clear CSS and HTML structure. Few succeed in their way for always improving their
    product, as it simply gets more complex.\n\nThe Anonymous above me gave an excellent
    advice, ty for sharing it mate!
  comment_date: '2010-02-11 21:42:21'
  comment_post_ID: '169'
  comment_type: null
  is_admin: '0'
---