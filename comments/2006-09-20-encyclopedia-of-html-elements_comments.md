---
comments:
- comment_ID: '4888'
  comment_author: Elliot Swan
  comment_author_url: ''
  comment_content: Wow, that must have taken some determination. Nice job.
  comment_date: '2006-09-21 01:08:36'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4892'
  comment_author: Sean Fraser
  comment_author_url: http://www.elementary-group-standards.com
  comment_content: Very cool. What do the color bars represent? And, will you be making
    this available in a print and/or PDF format?
  comment_date: '2006-09-21 02:10:31'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4895'
  comment_author: Federico
  comment_author_url: ''
  comment_content: '* The CITE element has not a cite attribute.\n* INS and DEL may
    be used at the Wikipedia when comparing historical versions of an article.\n*
    Element I may not be always safely replaced by EM.'
  comment_date: '2006-09-21 03:35:41'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4896'
  comment_author: Rowan Lewis
  comment_author_url: http://pixelcarnage.net/
  comment_content: 'I''ve had to learn just how complecated it is...\n\nOver the past
    few weeks I''ve been writing a script that:\n- Corrects bad tag nesting: [b][i][/b][/i].\n-
    Cleans element attributes, removing those which don''t belong on the current element
    and adding the required attributes with their default values.\n- Removes any elements
    which don''t belong unter their parent elements: [a][p]text[/p][/a] =&gt; [a]text[/a].\n-
    And so much more...\n\nMy head hurts.'
  comment_date: '2006-09-21 03:42:39'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4901'
  comment_author: TJ
  comment_author_url: ''
  comment_content: I disagree with your NOSCRIPT bashing, so I did some googling.  Apparently
    both <a href="http://www.quirksmode.org/blog/archives/2005/06/three_javascrip_1.html"
    rel="nofollow">PPK</a> and <a href="http://www.robertnyman.com/2005/07/01/no-noscript-mkay/"
    rel="nofollow">Robert Nyman</a> agree with you.\n\n"Just do it with javascript"
    isn't good enough.  Yeah, you could write some DOM that hides a paragraph if javascript
    is enabled, but to make sure it degrades gracefully, works for all browsers, and
    selects every element that you want to hide, you will just get bloated code for
    a simple result.  Noscript is semantically correct, less code, and works in every
    situation where a javascript workaround could.
  comment_date: '2006-09-21 05:34:57'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4903'
  comment_author: Rowan Lewis
  comment_author_url: http://pixelcarnage.net/
  comment_content: 'I also want to have a little nitpick about a few things:\n\n1.
    BUTTON elements do have a default action: submit, exactly the same as with an
    INPUT element with the TYPE attribute set to "submit".\n2. BUTTON elements give
    you more control over the button label.\n3. PRE elements are good, they describe
    exactly the type of content they contain: preformatted text.\n\nAnyhow, I''m working
    on a copy of your list with code examples...'
  comment_date: '2006-09-21 06:23:25'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4904'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Elliot Swan: Thanks! Now you know the reason for the lack of
    posts for a couple of days ;)\n\n@Sean Fraser: Oh, I forgot to tell you about
    the bars, I''ll add that info.\n\n@Fredrico: Thanks for the updates, I have no
    idea what I was thinking with cite.\n\n@TJ: I think it''s a matter of how you
    look at javascript. To me it''s a way to add extra stuff, not something that should
    be required. Thanks for the links. It''s not hard writing javascript that hides
    content, even getting it cross browser.\n\n@Rowan Lewis: Thanks for the fixes,
    I agree with all of them except the pre element. Hmm... Ok if I add code examples
    too? It has been on my radar all along.'
  comment_date: '2006-09-21 07:01:25'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '4905'
  comment_author: Sean Fraser
  comment_author_url: http://www.elementary-group-standards.com
  comment_content: Will this one be available as a PDF?\n\n(Deleted this comment by
    misstake, sorry!)
  comment_date: '2006-09-21 07:08:48'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '4906'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Sean Fraser: I''ll have a look at it, nice idea!'
  comment_date: '2006-09-21 07:10:26'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '4907'
  comment_author: TJ
  comment_author_url: ''
  comment_content: <em>"To me it’s a way to add extra stuff, not something that should
    be required"</em>.  A fair evaluation.  I wish I could always provide alternate
    solution, but it's not easy.\n\nThanks for this list.  It's a great expansion
    of w3school's indispensable HTML reference.
  comment_date: '2006-09-21 07:16:44'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4909'
  comment_author: Rowan Lewis
  comment_author_url: http://pixelcarnage.net/
  comment_content: Emil, the reason I'm pro PRE element is because its the best thing
    suited for the job, I've known people to use display:block; on CODE elements,
    but that is wrong, since its a strictly inline element.
  comment_date: '2006-09-21 09:26:15'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4911'
  comment_author: Peter Krantz
  comment_author_url: http://www.standards-schmandards.com
  comment_content: 'Thank you for an interesting summary! Contrary to what you write,
    I think that HTML isn''t rich at all. It has a background in computer science
    publication which is evident when looking at the domain specific elements KBD,
    VAR, etc. \n\nSome other feedback:\n\nSUB, SUP: They just say that content should
    go up or down. This means that you can not parse any valuable meaning from them
    (is the expression squared or is it a footnote reference?). What practical use
    can you make from that?\n\nINS, DEL: Although they mean something many browsing
    devices do not know what to do with them. Is it clear to a user that something
    has been deleted just because you style it with strikethrough? Some screen readers
    ignore these elements and read all of the text which may have unintended consequences.
    Be careful.\n\nHR: This element actually menas something. It acts as a section
    divider and is there even when styling is switched off. DIV has no meaning and
    should be used to structure the document without affecting the content. Unfortunately
    the name implies a horizontal line. In XHTML2 it has been renamed to separator
    which properly describes it''s use.\n\nI, B: Well, these actually have a meaning
    if your content is about typography. But maybe that is a special case.'
  comment_date: '2006-09-21 09:55:22'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4915'
  comment_author: Enciclopedia de Entidades HTML - aNieto2K
  comment_author_url: http://www.anieto2k.com/2006/09/21/enciclopedia-de-entidades-html/
  comment_content: '[...] Recopilación en forma de enciclopedia de las entidades HTML.
    Útil para conocerlas todas y no dejarte ninguna [...]'
  comment_date: '2006-09-21 11:24:09'
  comment_post_ID: '94'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '4917'
  comment_author: What&#8217;s hot and what&#8217;s not in HTML at The Blog Herald
  comment_author_url: http://www.blogherald.com/2006/09/21/whats-hot-and-whats-not-in-html/
  comment_content: '[...] Emil over at Friendly Bit has written a nice post called
    Encyclopedia of HTML elements where he comments on what elements he thinks are
    OK to use and how, and what’s not. It’s a good read, especially for the not so
    experienced webdesigner who don’t quite grasp what all those web standard advocates
    are bitching about. [...]'
  comment_date: '2006-09-21 11:31:11'
  comment_post_ID: '94'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '4921'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Peter Krantz: It isn''t contrary to what I write at all, it just
    has to do with what you compare with. Modern HTML is a lot richer than oldfashoned
    table layouts. That was what I was getting at with my comment. HTML certainly
    lacks elements from areas outside of the computer science domain.\n\nSUP and SUB:
    After some consideration I agree. I was not thinking of "to the square of" or
    "atom number" rather than just design like the spec states. Updated.\n\nINS and
    DEL: Text updated, I had no idea.\n\nHR: I don''t agree. In my world div has the
    semantical meaning of representing a section of the page, a division. This is
    what HR tries to define too, but instead of marking the section it marks the space
    in between them. Similar to BR and simply not the best way of doing things.\n\nI
    and B: You could say that about all elements. "If you write about horizontal lines
    HR is a semantical element". It might be valid use, but like you say, it''s a
    border case .'
  comment_date: '2006-09-21 12:39:40'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '4925'
  comment_author: Ben Millard
  comment_author_url: http://sitesurgeon.co.uk/
  comment_content: '<code>&lt;html&gt;</code> is very useful for setting the primary
    language of the document via the <code>lang</code> attribute.\n\nThe reason many
    tags are optional is because they can be inferred programattically. Many end tags
    are optional in HTML so that code-heavy structures (like lists and tables) aren''t
    quite so inefficient.\n\nYou can set images via the <code>background</code> shorthand
    property in CSS. This allows a colour to be set as a fallback for areas the image
    doesn''t cover and it will be used when the image cannot be displayed.\n\nA user
    without a keyboard (or assistive peripherals capable of sending keycodes to the
    device) obviously can''t use the contents of <code>&lt;kbd&gt;</code>. Explain
    the same operation when using a mouse (or equivalen assistive peripheral) if you
    are <em>that worried</em> about device independance. :P\n\nYou can use multiple
    <code>&lt;tbody&gt;</code> elements in a <code>&lt;table&gt;</code> if the table
    has several sections. An use-case example of this would be the final stages of
    the <a href="http://sitesurgeon.co.uk/!dev/fifa2006/ben-millard.html" rel="nofollow">FIFA
    2006 Tournament</a>.\n\nTypo: In the <a href="#TR" rel="nofollow">TR section</a>,
    you refer to "th" instead.\n\nI think marking up your tag names (like you do with
    CSS property names) would make these explanations easier to follow. Using the
    same case for all tag names would help, too; currently some are uppercase and
    some are lowercase.\n\n(EDIT) Your use of <code>&lt;dt&gt;</code> in the article
    doesn''t seem right, even when taking a "key=>value" interpretatation of. You
    often include a description (value) of the tag name as part of the term (key)
    when descriptions (values) should be in <code>&lt;dd&gt;</code>s?\n\nI''d suggest
    using headings and paragraphs instead of an enourmous <code>&lt;dl&gt;</code>.
    Headings would better describe the structure of the document by spliting the content
    area subsections, since each tag has a significant amount of content about it.'
  comment_date: '2006-09-21 15:21:08'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4932'
  comment_author: Mis Algoritmos &raquo; Blog Archive &raquo; Enciclopedia de los
    elementos HTML
  comment_author_url: http://www.mis-algoritmos.com/2006/09/21/enciclopedia-de-los-elementos-html/
  comment_content: '[...] Enciclopedia de los elementos HTML [...]'
  comment_date: '2006-09-21 17:08:37'
  comment_post_ID: '94'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '4944'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Ben Millard: Thanks for your comments, the comment section is
    becomming a resource in itself. I updated the lists on some places.\n\nI think
    the use of a dl is ok here. It is a <em>list</em> of elements, not headers. This
    is certainly key -> value where you can look up an element (key) and see the tips
    connected to it (values). I only use caps in the dt as far as I see. That''s the
    intended way.\n\nThanks again.'
  comment_date: '2006-09-21 22:57:40'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '4950'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: 'ABBR is for abbreviations, not terms.\n\nADDRESS is for contact
    information about the author, not addresses.\n\nI disagree about the use of B.
    If you use bold for a purpose of which HTML doesn''t have an element type (e.g.,
    the name of a product) then B is appropriate and STRONG is not. EM and STRONG
    are not replacements for B and I.\n\nBDO is for rtl text. CSS is an optional layer
    and the text should still be readable without CSS, so BDO should be used when
    you want bidi-override.\n\nCITE can also be used for references.\n\nEM is for
    stress emphasis, not importance. STRONG is importance (see Web Apps).\n\nHR isn''t
    a section divider, it''s a paragraph divider. They are common in books as "* * *"
    or some such which represents, e.g., "meanwhile" or "later on". (This will eventually
    be defined in Web Apps.)\n\nThe HTML element can''t be used just like any DIV.
    It is specifically the root element of an HTML document and may not be used elsewhere.\n\nKBD
    is about user input, not specifically keyboard user input. Also note that keyboard
    buttons are not user input. (Web Apps defines numerious ways to nest KBD/SAMP
    to represent different things.)\n\nNOSCRIPT is only useful for document.write()
    scripts, which arguably should be avoided anyway.\n\nPRE: Preformatted text means
    that line breaks and white space is significant. Applications other than ASCII
    art includes text-only e-mails and Python code.\n\nSAMP is for computer output.\n\nSUB/SUP,
    while they are presentational by nature, HTML doesn''t have an element which represents
    "the power of" in the mathemathical sense, so if you don''t intend to use MathML
    or some other math markup SUP is better than SPAN to express "the power of" (and
    other things), because at least it has correct typographical representation and
    typographical representations are not limited to visual presentations (screen
    readers could announce superscript, for instance). (In Web Apps, they are appropriate
    when the absense of them would change the meaning.)\n\nVAR is not only for computer
    variables, but for any type of variable, and can be used in general prose.'
  comment_date: '2006-09-21 23:23:07'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4953'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@zcorpan: \nABBR, I didn''t want to use the "abbrreviations" word
    at first because people might not know what it means. I change the text to use
    it but explains it below instead.\n\nADDRESS, HTML, VAR, updated the wording there.\n\nB,
    I, SUP, SUB: This is about structure, we can''t start using elements just because
    their default look in some browser. I don''t agree.\n\nBDO, you can also represent
    this in the content, by using certain UTF-8 characters. I think that''s a better
    way than claiming this has with semantics or structure to do. Where''s the direction
    for western text?\n\nThanks for your comments. Our opinions seems to differ on
    some points, but I think that''s mostly because you base your statements on Web
    Apps and I base mine on what feels right for me.'
  comment_date: '2006-09-21 23:57:14'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '4964'
  comment_author: qureyoon
  comment_author_url: http://qureyoon.blogspot.com/
  comment_content: this is very very helpfull ;) xpcialy 4 those who have limited
    knowledge of html ;)\n\ncan i link it to my blog ;) \n\nthank you very much ^^
  comment_date: '2006-09-22 06:02:15'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4965'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@qureyoon: Thanks! If you want to link to it, please do, the code
    for it is at the bottom of the page.'
  comment_date: '2006-09-22 06:44:26'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '4985'
  comment_author: me
  comment_author_url: ''
  comment_content: I've always wondered why browsers render PRE as monospace, when
    that's the purpose of tt.\nNothing is stopping PRE from being rendered as variable
    width text.
  comment_date: '2006-09-22 15:11:15'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4989'
  comment_author: blaise
  comment_author_url: ''
  comment_content: <blockquote>BODY - All (...)\nAlways use (even though a page without
    it for strange reasons still validate). </blockquote>Why? Is there a special reason
    for this?
  comment_date: '2006-09-22 17:20:28'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4994'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: Very good work Emil, and lots of valid and interesting comments
    too!
  comment_date: '2006-09-22 19:42:59'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '4996'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@me: Yeah, the default styling is very strange in some cases...\n\n@blaise:
    Good question! I use it because I think it''s a nice way of separating what''s
    meta information <em>about</em> the page and what''s the real content. You can
    also use it as a wrapper :)'
  comment_date: '2006-09-22 21:03:58'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '5003'
  comment_author: Evan
  comment_author_url: http://www.goer.org/
  comment_content: First, I'd like to say, you put a lot of work into this, and thanks
    for doing it. It looks very useful. But I do have some disagreements with your
    definitions, along the lines of zcorpan above.\n\nIf something is really just
    “presentational" and not "semantic" at all, then <em>nothing should happen to
    the meaning if we alter the presentation</em>. Consider SUP when used in mathematics:\n\n<strong>X2</strong>
    vs. <strong>X2</strong>\n\nThe physical positioning of the "2" <em>means</em>
    something, just like a physical line break in a poem.
  comment_date: '2006-09-22 23:15:39'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '5006'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Evan: If we markup that example with X&lt;span class="powerof">2&lt;/span>
    we don''t change the meaning by removing style. You see what I mean?'
  comment_date: '2006-09-23 00:03:52'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '5013'
  comment_author: links for 2006-09-23 &laquo; Donghai Ma
  comment_author_url: http://donghaima.wordpress.com/2006/09/23/links-for-2006-09-23/
  comment_content: '[...] Encyclopedia of HTML elements - Friendly Bit (tags: design
    reference software tips tutorial web) [...]'
  comment_date: '2006-09-23 06:22:04'
  comment_post_ID: '94'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '5018'
  comment_author: Dan Pettersson
  comment_author_url: ''
  comment_content: 'May I translate parts of this list? Of course I''ll link here,
    as a reference.\n@Emil: I agree with Evan. &lt;sup&gt;/&lt;sub&gt; <i>does</i>
    have a meaning, even if it may vary depending on whether it is used in mathematics,
    as a note, or in e.g. chemistry. Even if it''s not the "perfect" element there
    is a need to specify raised and lowered characters, even when CSS is turned off,
    and since the elements <code>&lt;pow&gt;, &lt;base&gt;, &lt;note&gt;, &lt;elcharge&gt;</code>
    (and quite a few more if you include various terms in physics and chemistry) don''t
    exist, I think we might as well use &lt;sup&gt;/&lt;sub&gt;.'
  comment_date: '2006-09-23 09:25:50'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '5086'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Dan Pettersson: yes you may translate it. Just make sure the
    original gets a link from somewhere in the beginning.\n\nI don''t agree on sub
    and sub, they are no better than b and i.'
  comment_date: '2006-09-24 16:10:43'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '5111'
  comment_author: Rowan Lewis
  comment_author_url: http://pixelcarnage.net/
  comment_content: But Emil, thats the same reason the PRE element is so important,
    it has to represent preformatted text no matter what, you can't just place the
    text in a paragraph and style it with CSS, because what then happens to search
    engines, text browsers and screen readers?\n\nBy the way, you're never on IRC...?
  comment_date: '2006-09-25 02:55:00'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '5113'
  comment_author: Johan
  comment_author_url: ''
  comment_content: I bet not everyoen will ever use all of these tags. Can anyone
    make a webpage that contains all these tags.\n\nIt is also important to know when
    to use what.\n\nAnd what tags are useful in which case.\n\nFor a webpage that
    is meant for a general website, you wont be needing all of them.\n\nwhat is the
    SEO value of all these tags?\n\nWhich attributes go with the corresponding tags?
  comment_date: '2006-09-25 04:01:49'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '5123'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rowan Lewis: I''m not sure what you mean. The formating of the
    text doesn''t matter to Search engines, screen readers and the likes, so why does
    it matter if it''s inside a pre block or not?\n\n@Johan: I have used all of the
    above tags, at least once (including the don''t-use ones. The article is all about
    when to use what tag, wasn''t that clear?\n\nI won''t list all the attributes,
    that''s far too much information at one place. I do list common misstakes with
    attributes though...\n\nFor SEO: title is most important, then the header tags,
    followed by strong and em (which has the same weight as b and i).'
  comment_date: '2006-09-25 12:35:02'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '5132'
  comment_author: Rowan Lewis
  comment_author_url: http://pixelcarnage.net/
  comment_content: Emil, because if you place source code or other preformatted text
    in a P element or something else, it'll be the bigest mess and completely unreadable.
  comment_date: '2006-09-25 15:43:27'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '5137'
  comment_author: Johan
  comment_author_url: ''
  comment_content: '&gt; For SEO: title is most important, then the header tags, followed
    by strong and em (which has the same weight as b and i). \n\nI know that. I even
    thought that h1 has more weight than h2. Or is it just the consistent use of \nheadings
    as titles of any content block, eg archives, testimonials, etcetera which in turn
    results into a higher number og headings.\n\nAlso the number of links  do count
    for SEO, search engines take in account links.\n\nAnd images?\n\nI agree that
    there is a whole lot more to get deeper into.\n\nNow people dont have an excuse
    anymore.'
  comment_date: '2006-09-25 18:31:50'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '5203'
  comment_author: Dustin
  comment_author_url: ''
  comment_content: I was reading about your discussion of the HR, and I feel that
    it is still useful. Let's say, for instance, I have a sidebar that also has my
    "bottom links" in it, and I've used CSS to have it be all pretty with rounded
    edges and whatnot. I don't want two seperate divisions, making two of these boxes.
    I want one box, with all of this information neatly divided. How else to do that
    but with HR?
  comment_date: '2006-09-27 01:49:55'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '5414'
  comment_author: Harmen Janssen
  comment_author_url: http://www.whatstyle.net
  comment_content: First of all; very nice work! It's a great list, very helpful.\n\nYou
    said you didn't want to go too deep into attributes, but I'm wondering; the INS-attribute
    "datetime" should, according to the W3C be formatted as YYYYMMDD. Is this mandatory?
    I think it would be more readable (and therefore more valuable) when the author
    can format this date to his likings (for instance, inserting hyphens).\nThis would
    certainly help when your content is non-English and national date-formatting rules
    differ from YYYYMMDD.
  comment_date: '2006-10-03 12:59:13'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '5635'
  comment_author: Kal Ström
  comment_author_url: ''
  comment_content: But SUB and SUP has semantical meaning. Just like emphasis (EM)
    and strong emphasis (STRONG) has.\n\nIt's a way to give meaning to content. What
    does the superscripted number mean in relation to its context. That's the important
    thing and that is why it is not simply just presentational. Just like EM and STRONG
    isn't.
  comment_date: '2006-10-09 22:56:42'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '6309'
  comment_author: links for 2006-10-16 at willkoca
  comment_author_url: http://www.willkoca.com/2006/10/16/links-for-2006-10-16/
  comment_content: '[...] Encyclopedia of HTML elements - Friendly Bit (tags: html
    reference xhtml) [...]'
  comment_date: '2006-11-01 00:30:44'
  comment_post_ID: '94'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '8506'
  comment_author: Brianary
  comment_author_url: http://webcoder.info/
  comment_content: '&gt; KBD: Rarely used.\n\nReally? If so, that''s probably because
    FrontPage, etc. don''t use it, and everyone else is glibly dismissive of it.\n\n&gt;
    KBD: How do you know your user will use the keyboard?\n\nIf you are documenting
    a command-line interface, text to be entered into a web form, a command to type
    at a prompt, or the name of a file to enter into a Save As dialog, chances are
    good that the user will not be using a mouse for this.\n\n&gt; SAMP: Seriously,
    don’t we have enough of the computer related elements already?\n\nWell, if we''ve
    got an element for program input (KBD), it only makes sense to have one for program
    output.\n\n&gt; SAMP: If you need sample text that isn’t code or keyboard type-in
    then fine, use this one.\n\nSuch as status messages, error messages, or records
    output?\n\n&gt; SMALL: The idea is that the size really is tied to the content...\n\nThe
    times that I''ve used the element this way, I''ve considered "small" to describe
    the prominence or importance (rather than the physical size) of the text.\n\n&gt;
    VAR: Another element from the computer science area.\n\nNot exclusively. "Indicates
    an instance of a variable or program argument." This includes math variables,
    or any other kind of placeholder such as "I, [state your name], pledge to ...".'
  comment_date: '2006-12-05 18:20:04'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '8519'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Brianary: How often do you use the kbd, samp or var elements?
    I''ve never used any of them on this blog and this site is surely on a computer
    topic. Now even that out over all sites on the net. I''d say  that they are not
    needed.\n\nAbout small, yeah I''ve used it like that too. Strictly speaking, how''s
    that different than using b(old) and thinking of it like "important"?'
  comment_date: '2006-12-05 22:01:53'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '9040'
  comment_author: Moria
  comment_author_url: ''
  comment_content: I'm a copywriter and while I will probably (O.K. surely) never
    program a Web site I try to learn as much as I can about how they are built. You
    site has become a reference for  me. Thanks for your dedication and willingness
    to share.
  comment_date: '2006-12-13 01:10:10'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '9075'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Moria: Hi! Glad you like it. I tend to forget that not all of
    my readers are professional web developers, your comment nicely remind me of that.'
  comment_date: '2006-12-13 08:32:01'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '16942'
  comment_author: Wilmington
  comment_author_url: ''
  comment_content: I really like the layout and colors that you chose for this website!
    It certainly is incredible! :)
  comment_date: '2007-01-28 01:42:43'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '23250'
  comment_author: WebDevTools &raquo; Blog Archive &raquo; The Encyclopedia of HTML
    elements
  comment_author_url: http://www.webdevtools.net/?p=4
  comment_content: '[...] Friendly Bit&#8217;s Encyclopedia of HTML  [...]'
  comment_date: '2007-04-10 12:38:03'
  comment_post_ID: '94'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '24600'
  comment_author: Rotem
  comment_author_url: ''
  comment_content: I would regard the BDO element as content, since it is used to
    ensure the correct processing of text itself.\n\nAlso, note that BDO is not the
    same as the HTML "dir" attribute (or the parallel CSS "direction" property); the
    latter is absolutely necessary in Hebrew/Arabic documents, whereas BDO is quite
    an exotic thing.
  comment_date: '2007-05-24 19:06:32'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '25136'
  comment_author: Rotem
  comment_author_url: ''
  comment_content: Oh, I just noticed that BDO has been discussed in the comments.
    Indeed, there are a few invisible "direction characters" in Unicode, but none
    of them work in Windows XP the way BDO does. (You could emulate BDO by nesting
    *each and every* visible/space character within invisible ones, but that's just
    silly.)\n\nAnd what about the DIR attribute? That is simply impossible to do with
    "direction characters" (at least in Windows XP), and DIR is extremely important
    (unlike BDO). So unfortunately, this whole direction business has to be done within
    HTML.\n\nCSS has equivalent properties, but why should CSS-less users get strangely
    ordered text? Direction is a language thing, and thus it's purely content, just
    like the LANG attribute.\n\nSorry if I'm being boring, the knowledge-sharing urge
    hit me again. Kudos for this wonderful site! =)
  comment_date: '2007-06-11 16:07:17'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '25150'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rotem: You''re saying that text direction is content but still
    you want to use HTML to add that info? Isn''t HTML there for structure rather
    than content? Although I don''t agree when looking at it from an ideology standpoint
    I do believe you when you talk out of browser compliance. It BDO is one of the
    few ways to present some text it should certainly stay. Thanks for contributing!
    :)'
  comment_date: '2007-06-11 20:38:11'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '25380'
  comment_author: Rotem
  comment_author_url: ''
  comment_content: 'Okay, my bad - browsers <em>do</em> support Unicode formatting
    codes, but many applications don''t. But the point is, it''s extremely difficult
    to manage these codes: they''re not universally supported, they''re invisible
    and they can easily create nesting problems. I just came across a <a href="http://www.w3.org/International/questions/qa-bidi-controls.en.php"
    rel="nofollow">W3C answer</a> that recommends using markup for text direction
    (for the above reasons).\n\nMaybe these things can be thought of as meta data
    about the text? Just like you use the LANG attribute to describe the text''s language,
    you use the DIR attribute and BDO tag to describe its direction. (Okay, I do</em>
    agree it''s silly to have an element just for this... They could''ve done something
    like dir="rtl bdo" instead.)'
  comment_date: '2007-06-20 11:33:34'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '26183'
  comment_author: Peter Vigren
  comment_author_url: ''
  comment_content: 'Hm, I just noticed that you use SMALL in the comment form, yet
    you encourage people to <em>not</em> use it. So I guessed it''s because of Wordpress
    and thought you should know about it.\n\nAnd I looked at your example with a SPAN
    with the class of "powerof" in order to convey the meaning of SUP but I don''t
    quite follow, since that would be like having a SPAN with the class "paragraph"
    instead of P. I agree that SUP can mean a lot, depending on context, but some
    elements are like that. They are not precise, nor perfect, but they are there,
    for a reason. I understand how you think about presentation but I don''t think
    it apply here. Hm... think of it this way: STRONG renders most often with a high
    boldness because that is how it looks in your head, that is, it is perceived more
    clearly than the rest. But it has semantic meaning while having a clear sense
    of how it is rendered. As do SUP and SUB because that is how they look and give
    meaning. A screen reader (I don''t know if those support the elements but bear
    with me) wouldn''t look at SPAN as something with semantic meaning (since it shall
    have none) but SUP and SUB should, just like STRONG.\n\nBy the way, your new photo
    looks really good (don''t remember the old one though).\n\nAnd sorry if I''m not
    too clear in the text, me too tired but I really thought I should post this comment
    now lest I would forget about it.'
  comment_date: '2007-07-19 03:40:33'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '26190'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Peter Vigren: Thanks for your thought-out comment! About small,
    it''s because I''ve added it there myself, wordpress is not to blame. The explaination
    is that this site is getting old, if I would redo it today I wouldn''t use it.\n\nAbout
    Sup and Sub: I''m starting to agree. Since this article was written, I''ve slowly
    changed my mind on them. Sure you can never know what you mean by them (power
    of, variable index, pure presentation, and so on), but hopefully the context tells
    you that. In something that looks like a formula, you do know that Sup is always
    the power of.\n\nThanks for the compliment about the photo ;) and even more thanks
    for the good content.'
  comment_date: '2007-07-19 11:07:50'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '26211'
  comment_author: Stevie D
  comment_author_url: ''
  comment_content: A couple of things where I agree more with the comments than the
    original (apart from these, great resource Emil!)\n\n\nThe superscriptness of
    the 2 in x2 is part of the content. You could alternatively render it as x^2,
    in the same way that instead of using [strong] you could wrap text in *asterisks*,
    but that is not making full use of what HTML has available.\nThe subscriptness
    of the 2 in, for example, H2O is again important to the chemical formula. I don't
    accept that it is purely presentational, and it is a big waste of bytes to define
    a class to be sub/superscript and then wrap all those digits in a span, when there
    are perfectly good [sub] and [sup] elements.\nWe don't need [big] because we have
    [strong], [em] and [h1/2/3/4/5/6] to cover the different reasons to <em>emphasise</em>
    text. Apart from [small], there is no way to <em>de-emphasise</em> text, so I'm
    happy to use it for that purpose. As it appears are the HTML5 working group (not
    that that is <em>necessarily</em> a recommentation!)
  comment_date: '2007-07-20 13:35:34'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '27257'
  comment_author: Kathi
  comment_author_url: ''
  comment_content: A great reference for html tags, Emil.\nEspecially the anchors
    to the single tag explanation are very useful.\nOnly I miss a link to get back
    to the top of the page under an explanation.
  comment_date: '2007-09-08 15:54:45'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '27358'
  comment_author: William O. Yates
  comment_author_url: ''
  comment_content: Hello Emil, great work... \n\nMany of the debates about your list
    stem from the history of the tags themselves.\n\nHTML is derived from IBM's progression
    of typesetting languages, starting with GML (Generalized Markup Language), to
    BookManager, to SGML (Standard Generalized Markup Language), and then cut down
    to the relative few HTML tags.\n\nFull typesetting languages can control content
    meaning in whatever presentation space desired with the thousands of tags available.\n\nThe
    SUB/SUP tags (and many others) were fought over for years, but they managed to
    live through committee when they should not have.\n\nCSS is finally "fixing" this
    heritage of typesetting origin, by separating content and presentation spaces,
    but content meaning should never be allowed to be altered by any use of tags to
    "pretty up" the content itself.\n\nUsing crippled tags in the manner originally
    designed, without the support required from surrounding tags and attributes of
    a full typesetting environment can only lead to frustration...\n\n(I know about
    the frustration part quiet well, I was there...)\n\nAgain, great work...\n\nWilliam...
  comment_date: '2007-09-14 14:30:08'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '28242'
  comment_author: QC
  comment_author_url: ''
  comment_content: I just noticed, shouldn't\n\n<blockquote>Don’t fall into the trap
    of using fieldset for non-form elements. This is meant for grouping forms, nothing
    else.</blockquote>\n\nbe\n\n<blockquote>Don’t fall into the trap of using fieldset
    for non-form elements. This is meant for grouping form elements, nothing else.</blockquote>\n
  comment_date: '2007-10-08 20:19:15'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '0'
- comment_ID: '28288'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@QC: Well said, your version is much clearer. I updated that line.
    Thanks!'
  comment_date: '2007-10-10 12:43:32'
  comment_post_ID: '94'
  comment_type: null
  is_admin: '1'
- comment_ID: '36682'
  comment_author: Enciclopedia de los elementos HTML | Carlos Montalvo
  comment_author_url: http://www.carlosmontalvo.com/2011/01/enciclopedia-de-los-elementos-html
  comment_content: '[...] Enciclopedia de los elementos HTML muy buena para que pedir
    más&#8230;   google_ad_client = &quot;pub-9635237586618960&quot;; /* 468x60, creado
    16/01/10 */ google_ad_slot = &quot;2939202578&quot;; google_ad_width = 468; google_ad_height
    = 60;   Otros temas RelacionadosCheat Sheets (o chuletas) para desarrollo webConvertir
    plantilla HTML a joomla [...]'
  comment_date: '2011-01-11 15:04:17'
  comment_post_ID: '94'
  comment_type: pingback
  is_admin: '0'
---