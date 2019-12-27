---
comments:
- comment_ID: '32860'
  comment_author: Anders Ytterström
  comment_author_url: http://madr.se
  comment_content: Ouch! :(\n\nAnother framework which should have consulted an Interface
    developer during development. Sad to read this.\n\nIt's good to see an article
    about a framework not being .NET powered suck in HTML as well, people tend to
    believe that .NET-people is extraordiary bad in HTML knowledge which is for no
    good. Many Java frameworks tend to lack of Interface feedback during development
    phrase as well.
  comment_date: '2009-07-23 23:11:32'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '32863'
  comment_author: Ole
  comment_author_url: http://www.h2ok.de
  comment_content: 'Some months ago, i was templating for a clients CMS called "Dot
    Net Nuke (DNN)" which calls itself: "The Leading Open Source Web Content Management
    Framework for ASP.NET". IT WAS HORRIBLE!! I''ve delivered clean semantical valid
    HTML templates, but the system made horrible code out of it (about 200 Warnings).
    It was really frustrating!\n\nSo I''ll never ever work for the .NET platform anymore.
    And now also not for "Tapestry5". Thank you for that information.'
  comment_date: '2009-07-24 08:43:21'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '32865'
  comment_author: Andreas
  comment_author_url: http://andreaslagerkvist.com
  comment_content: 'Gah! that''s awful.\n\nRegarding the whitespace though, I''d think
    that was only positive?\n\nThe problems I tend to have with whitespace is that
    IE renders it when it shouldn''t.\n\nSo, removing whitespace altogether only seems
    like a good thing to me? Kindof like how some people do * {margin: 0; padding:
    0;}.\n\nAlso, the page you link to had some points on why one should remove whitespace
    (fewer text-nodes in the DOM and obviously smaller filesize).\n\nI implemented
    whitespace-removal in my own framework so that I could write my template-code
    any way I like without worrying about IE rendering the whitespace.'
  comment_date: '2009-07-24 12:43:25'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '32869'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Andreas: All browsers render whitespace between inline elements,
    so you can''t remove it and hope that the page will look the same. This is something
    that is specially annoying when it comes to form elements, which by default are
    inline. Instead of removing whitespace, use gzip to minimize the size of the HTML
    delivered.'
  comment_date: '2009-07-24 13:18:15'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
- comment_ID: '32870'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Ole: Don''t allow one or two bad frameworks affect your opinion
    on all of .NET. Just try <a href="http://www.asp.net/mvc/" rel="nofollow">ASP.NET
    MVC</a>; they are doing a really good job in working with HTML. I would hope more
    .NET frameworks would base their models on MVC like that.'
  comment_date: '2009-07-24 13:21:04'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
- comment_ID: '32871'
  comment_author: Andreas
  comment_author_url: http://andreaslagerkvist.com
  comment_content: 'I do gzip everything but I still minify my JS, CSS and HTML.\n\nAre
    forms inline by default? I''ve never had a form-element not linebreak before and
    after it unless I''ve set the form and everything inside it to display: inline;\n\nAlso,
    I don''t remove whitespace between inline-elements like this:\n\n<code>\n&lt;p&gt;Hello
    the &lt;strong&gt;spaces&lt;/strong&gt; in here will &lt;em&gt;not&amp;lt/em&gt;
    be removed&lt;/p&gt;\n</code>\n\nI do however remove all tabs and linebreaks etc.
    I''ve never noticed a difference in anything but IE.'
  comment_date: '2009-07-24 18:02:48'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '32872'
  comment_author: Howard M. Lewis Ship
  comment_author_url: http://tapestry.apache.org
  comment_content: Emil,\n\nIt's disappointing that you did not do proper research
    on Tapestry 5. All of the complaints you make about the framework reflect features
    that ARE correct for the vast majority of users, and CAN BE DISABLED quite easily.\n\nTapestry
    gives you very good control over the exact output generated from your template,
    you just have to actually read the component documentation. \n\nI'm not sure where
    you are coming from with a  tag being added via Ajax calls; that's not what Tapestry
    does at all.\n\nTapestry adds quite a bit of JavaScript to the page ... if you
    use Tapestry's JavaScript facilities.  This is part of Tapestry's approach to
    making things Just Work (tm) ... people don't want to read a five page treatise
    on how to get Ajax to work on a page, or client-side validation, or dynamic HTML
    ... they just want things to work without care to how they are implemented. That's
    what Tapestry does.\n\nI think you don't understand XML/XHTML correctly as  and  are
    exactly identical in XML (and if not, your browser is broken). What Tapestry does
    (by default) is to support broken browsers in HTML mode (SGML compatibility) where
    there is a difference between the two ... this is mostly to make the  tag work
    in broken browsers like IE.\n\nAdding conditional CSS support for IE is on the
    planning board. You clearly state you can achieve your goals while dissing the
    framework. The framework would be in error if it was NOT possible to achieve your
    goals; instead, you are saying that your very specific, very personal choice are
    the only valid choice for any developer. If that is the case, please write your
    own framework, because nothing else will ever satisfy you.\n\nTapestry does not
    blindly chaing the Form's id to "form"; it allocates a unique id for each form
    on the page, and you can control what that id is if you care to.\n\nTapestry does
    add elements to a  ... and is very careful to add the new invisible  and  tags
    in HTML compatible locations.\n\nTapestry is quite happy to use HTML5 or other
    elements but it does use an XML parser (though not a validating parser, your documents
    just need to be well formed).  The majority of components, including Form, the
    link components, TextField, etc., all support informal parameters ... what ever
    attribute you put in the template will be honored when Tapestry renders (unless
    the attributes directly conflict with an attribute generated inside component
    code).\n\nIn fact, Tapestry was specifically designed with user interface designers
    in mind; with discipline, it is possible to remove from the templates everything
    except a single attribute, t:id, for dynamic elements of the page, which makes
    it much more reasonable for interface developers to work on Tapestry templates
    using standard, off-the-shelf tools. This "invisible instrumentation" originated
    in Tapestry around 2003 and has been gradually adopted into other well-known Java
    web frameworks.\n\nI think if you take a look at Tapestry without blinders on,
    you'll find a lot more about it to like than to carelessly dismiss as you have
    so far.  The majority of Tapestry users have worked in multiple frameworks prior
    to Tapestry but have become passionate about Tapestry because it works fo well
    for them ... and this applies not just to Java developers but to the interface
    side of the equation.
  comment_date: '2009-07-24 18:49:26'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '32873'
  comment_author: Emil Stenström
  comment_author_url: ''
  comment_content: '@Howard M. Lewis Ship: Thanks for your thorough explanation from
    your standpoint, as the creator of the framework. \n\nYou''re saying, that these
    defaults "are correct for the vast majority of users". I''m certain that most
    interface developers (the audience of this blog) would disagree with that statement.
    Each of the issues I list, sprung from real problems I''ve encountered. I should
    of course have included those problem descriptions with the text. Sorry for being
    lazy, let me know if you want them.\n\nYou say that "with careful instrumentation",
    I can reset all the defaults this article describes to what I need. That I need
    to reset them in the first place, is the problem. From my side of the board, those
    defaults are a real obstacle that stops me from doing my job well. I''m sure you''re
    right that there are ways to sidestep most of the described issues (I mean, if
    anyone, you should know), but I''ve guessing that that''s lots of work for an
    overage Java/Tapestry developer, not to say an interface developer like me, with
    only little experience with Tapestry.\n\nNow. There are several things one could
    do to make an interface developer''s job easier. The simplest is probably to document
    how I would do the instrumentation you describe. I''ve given each of the issues
    I describe some serious Googling, without finding any reliable workarounds. Feel
    free to do that yourself. Another would be to release a sample project with the
    necessary changes made, that someone like me could use as a starting point.'
  comment_date: '2009-07-25 00:21:11'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
- comment_ID: '32874'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: 'And some specific answers: \n\nAbout "AJAX": What I''m saying
    is, you don''t always want a head element on each page you build. In our case,
    we made a stripped down version of a page with Tapestry, and then completed the
    HTML of that page according to a given HTML template later in the rendering cycle.
    Our head element was added later, but Tapestry forced it''s own head element in
    first. The same would be true for a AJAX search page. You would make a separate
    page with just the search results (no head element), and then fetch that page
    with an AJAX call and insert it into the current page.\n\nOn Tapestry''s javascript:
    Interface developers know how AJAX works, and don''t need frameowork features
    that "help" them. Tapestry does this for Java developers, who don''t know. If
    I don''t want that help, how do I remove those scripts and handle things myself?'
  comment_date: '2009-07-25 00:29:19'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
- comment_ID: '32875'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: 'About XML/XHTML: Sorry that the example tags disappeared, I blame
    Wordpress. I''m not sure what you mean (since the tags are missing probably),
    how is Tapestry compensating for bad browsers? You are right that self closing
    tags can be expanded in XML, but browsers have HTML parsers, not XML parsers,
    and therefor treat expanded tags different from self-closed ones. Why change the
    template at all?\n\nAbout conditional comments: They are not a "very specific,
    very personal choice". Conditional comments are best practice in the interface
    development world. Ask anyone. No framework needs to build their own method to
    send custom CSS to different versions of internet explorer, it''s there, it''s
    what we use everywhere else. \n\nAbout form id:s: I developer my page in another
    java framework (with &lt;form id="signup">, and CSS that referenced that id),
    when that page was migrated to Tapestry the CSS suddenly stopped working, since
    the id was changed to the default "form". To me, this is another example of small
    barriers that make an interface developers job harder.\n\nAbout HTML5 compliance:
    I might have exaggerated here, based on a single error in one of my templates.
    I tried to add "default="default"" to an option element (which is invalid, should
    be "selected"), and got an error from Tapestry which I interpreted as "your HTML
    is invalid". My mistake is that was an incorrect conclusion, I''m remove that
    point from the post to reflect this.'
  comment_date: '2009-07-25 00:47:50'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
- comment_ID: '32876'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: Added another point about adding prototype by default. As this
    framework clashes with jQuery, I had to rewrite my scripts to use jQuery:s no
    conflict mode. Again, minor annoyance that could have been avoided.
  comment_date: '2009-07-25 00:52:09'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
- comment_ID: '32877'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Andreas: I meant form elements as input, select, and label, not
    the form element itself. Sorry for the misunderstanding. \n\nIf you gzip your
    HTML, you will hardly gain any file-size by also removing whitespace. I think
    your way of removing it could work, but I''m rather sure that there are edge-cases
    where it might change the rendering.'
  comment_date: '2009-07-25 01:20:34'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
- comment_ID: '32882'
  comment_author: HTML Framework
  comment_author_url: http://www.rorkvell.de/news/2009/HTML_Framework
  comment_content: '[...] Emil Stendström schreibt in seinem neuesten Artikel über
    HTML Frameworks. Im konkreten Artikel über Tapestry 5. Er zerreisst das Produkt
    förmlich in der Luft. [...]'
  comment_date: '2009-07-27 09:35:32'
  comment_post_ID: '528'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '32888'
  comment_author: Cody
  comment_author_url: http://www.webhostdesignpost.com
  comment_content: I've never used Tapestry, I never knew anything about it.  But
    it sounds like a big mess for HTML standards.   I have used frameworks that behave
    the same way.  Some of them, there is nothing you can do to have valid code.  I
    total agree with you when you say - "just talk with people that work with HTML,
    CSS, and Javascript."
  comment_date: '2009-08-01 00:43:13'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '32900'
  comment_author: ''
  comment_author_url: ''
  comment_content: 'Thanks for writing this article. This way, other people can say
    that Tapestry is rubbish, without ever trying it themselves, which seems to be
    fashionable these days.\nSeems to me you are looking for perfection, but most
    of us understand that any web-related framework will ever be perfect for everybody,
    due to the nature of the beast.\nMy question is: what is the contribution of articles
    like these for the community?'
  comment_date: '2009-08-06 18:28:31'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '32901'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Anonymous: My hope is that some Tapestry developer will consider
    my main point: "Why is an interface developer this dissatisfied with Tapestry?"
    and "Is there something we can do to make his life less misserable?". If just
    one of the issues I bring up get fixed, or get documentation for workarounds,
    I''m glad I wrote the article. If nothing, then you''re right, this article was
    a waste.'
  comment_date: '2009-08-06 23:54:08'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
- comment_ID: '32997'
  comment_author: Alex
  comment_author_url: http://tipseri.net
  comment_content: '@Anonymous, After i read the article and all these comments i''ve
    decided that Tapestry worths a try.\n\nI think that article''s like this one are
    usefull not just for the community but also for the framework creator who can
    consider and repair all those HTML fights. It''s like a large feedback.\n\nI don''t
    think that Emil is looking for perfection, i think that the word which can be
    used here is called "improvement"\n\nRegarding those who read and not try i think
    that they should reconsider.'
  comment_date: '2009-09-12 15:22:42'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '33123'
  comment_author: Max
  comment_author_url: ''
  comment_content: I just made a T5 website, well not that big, some 25 pages and
    some 10 components or so, public pages and pages for registered users only and
    some individual JavaScript and Google Map integration. As I'm not a web designer
    at all, I had to work with a designer for the layout and style. The designer has
    a lot of experience, but did not know anything of T5 at all. What should I say,
    he had absolutely no complains about T5 and the way it handles html at all. He
    never ever said a word about having troubles with the way T5 does its job. So
    maybe it very much depends on ..., yes on what? On expectations? On the way of
    doing things?
  comment_date: '2009-10-13 11:31:13'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '33124'
  comment_author: Martin Reurings
  comment_author_url: ''
  comment_content: Bah, I couldn't even stand to read all the biased close-minded
    argumentation you were writing out here. Since you state your blog is for interface-developers
    (which I am) I should have expected a golden argumentation of what is and is not
    good about T5's support for interface development. Instead I got the argumentation
    of a kindergarten kid stumbling into a mathematics essay and complaining that
    the writing on the chalkboard makes no sense!\n\n.Net makes for some seriously
    screwed up html, I agree, out of the box it is most likely one of the most horrible
    frameworks out there. I can probably find you 50 others, strewn around php, java,
    python, etc... So let's get that out of the way, by default a framework is far
    from perfect, that's because interface-developer think differently from backend
    developers and what's even worse, they disagree between themselves!\n\nSame goes
    for Tapestry, out of the box, it ain't perfect! Surprisingly enough, out of the
    box it gets most of the stuff pretty close to perfect, from my personal perspective.\n-
    It forces id's on elements that need it, of course only if the developer didn't
    actually set one correctly in the first place!\n- It removes white-space from
    the page, and I like that, what's even better, should I really need white-space
    somewhere on the page, I can tell it to preserve that, only there!!!\n- All the
    default javascript and css can be disabled or overwritten, damn, that's so cool,
    it only takes a single configuration property for each! With other frameworks
    I was unable to even so much as think about such things.\n- The last point, about
    hidden elements you make? Really, get a live! Hidden elements rarely, if ever,
    screw up design, it's a lousy point to make when the result of those hidden elements
    have many benefits that have, indeed, nothing to do with your little narrow field
    of specialization.\n- Oh, did I mention that T5 can return only page-partials
    for Ajax-request, or JSON, or plain text, whatever you need? Guess you didn't
    know that, I also guess the developer you worked with had as little experience
    with T5 as you did, since returning a seperate page for an Ajax-request is not
    quite the logical way to do things. The developer you work with should have been
    able to tell you how to work it out with T5, actually, he probably should have
    done the work. If you didn't work with one, either you should not do the job,
    or you should get more serious about learning the framework you work in.\n\nOne
    last feature, plain html templating, the only non-html information you 'have'
    to add being t:id="..." to elements that require an actual T5 component to render
    in their place.\n\nAll of this just being the tip of the ice-berg. Suffice to
    say, I've seen plenty of frameworks come and go, I've never (from an html/js/css
    point of view) been more enthusiastic about the capabilities of a framework before.
    Should you really not like the fact that you may need to re-configure parts of
    [insert name of a framework here] to get it closer to your private perspective
    of perfection, build your own, or start using plain old .jsp or .php pages and
    hope your backend developers won't kill you :)
  comment_date: '2009-10-13 11:31:33'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '33127'
  comment_author: Ernst-Udo Wallenborn
  comment_author_url: ''
  comment_content: 'The whitespace compression can also be set on a global level,
    by configuring tapestry.compress-whitespace in web.xml or its equivalent in SymmbolConstants
    to ''false'', so the argument is kinda moot.\n\nAnd where the xml element expansion
    is concerned: why would you want to deliver XHTML to browsers who don''t speak
    XML in the first place? Why not use old-fashioned HTML instead?'
  comment_date: '2009-10-14 11:05:15'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '33133'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com/
  comment_content: '@Martin Reurings: Thanks for your "unbiased open-minded" comment
    (irony of course, you are as biased and close-minded as you claim I am). Your
    kindergarten/"I didn''t ever read the whole article"-comments are just childish.\n\nYou
    also seem to agree with my main point: Tapestry 5''s defaults are not as good
    as they could be. So, now we need two things: Change the defaults, and meanwhile,
    documentation of how to change the defaults to our liking.\n\nThere are many frameworks
    which are worse than Tapestry, no doubt, but that doesn''t mean Tapestry is perfect.'
  comment_date: '2009-10-17 13:56:31'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '33134'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com/
  comment_content: '@Ernst-Udo Wallenborn: Thanks for telling us how to disable white-space
    collapsing. That will help people like me who care about white-space. The default
    should be changed in my opinion, since removing white-space changed rendering
    so much.\n\nConcerning XHTML. I usually don''t use it, but I don''t see why a
    framework should disallow people to use it. If Tapestry developers wants to disallow
    XHTML, they of course can. But it would be easy to make it possible to use.'
  comment_date: '2009-10-17 14:35:18'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '33166'
  comment_author: Alan Earl D. Luayon
  comment_author_url: ''
  comment_content: Sorry but i love Tapestry5...\n\nIt depends the way you develop
    your application.\n\nTapestry is designed to be extremely scalable in several
    dimensions:\n\n    * Tapestry applications may contain large numbers of pages
    and many custom components.\n    * Tapestry applications may contain very complex
    functionality.\n    * Tapestry applications may be created by large, diverse teams.\n    *
    Tapestry applications can service large numbers of concurrent users.\n\nPlease
    read first ... before you give commentsssss...
  comment_date: '2009-11-05 06:53:13'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '33308'
  comment_author: Pierce Wetter
  comment_author_url: ''
  comment_content: I don't think your criticism is quite fair. Of all the frameworks
    out there, T5 is one of the best at taking regular, plain XHTML and making it
    dynamic. As opposed to most of the web frameworks out there which require you
    to shove in non HTML, T5 templates can be built in such a way that you can load
    them directly into your browser.\n\nI think some of your complaints are just inexperience
    with T5, and frankly with web frameworks in general, because some of your statements
    are just wrong.\n\nAlso, you're complaining about including JavaScript. I have
    to say, managing which JS libraries get loaded when can be a big pain in any of
    the application frameworks I've used. The fact that T5 has stuff to deal with
    that is a good thing.
  comment_date: '2009-12-03 18:00:33'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '33309'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Pierce Wetter: Are you saying that my ideas for improving T5
    are unfair because I don''t say it''s better than other frameworks? It sure is,
    I''ve used lots of other frameworks which are much worse. \n\nMy experience with
    T5 is limited, and I''ve not claimed otherwise, but I think a framework should
    handle that, either by being easy to learn (and by that I mean modify to ones
    liking, not simply using), or by being properly documented. My experience is that
    T5 is neither.\n\nFeel free to say *which* of my statements are wrong, and I will
    address your concerns.\n\nI''ve used several frameworks that let me choose the
    js frameworks myself, and that''s a good thing.'
  comment_date: '2009-12-03 21:27:34'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
- comment_ID: '33345'
  comment_author: Martin Reurings
  comment_author_url: ''
  comment_content: '@Emil Stenström It''s good to realise you actually understand
    what overkill reads like :) I went about as far as I possibly could in driving
    my point home, which was well passed fair or reasonable. What you feel about my
    comment seems to be exactly what I feel about your blog-post...\n\nYes, I have
    worked with Tapestry quite extensively and yes, I have quite different opinions
    of how to use html and css, but I ''personally'' think that gives my bias a much
    stronger foundation than yours. Unfortunately, only somebody who has actually
    worked with Tapestry is capable of figuring out the holes in your arguments, so
    anybody who actually believes your _opinion_ might turn to something that is far
    worse but didn''t get flamed by a developer who didn''t get enough time put into
    learning it properly.\n\nSo, yes, I am biased, but no, I''m not close-minded.
    Among other things that''s how I am able to realise that Tapestry works extremely
    well for me while I accept that this may not count for everybody. Why I believe
    that you ARE closeminded, and I quote: "No. Tapestry was clearly not built with
    an interface developer in mind." Which means that everybody does interface development
    the way you do, right?'
  comment_date: '2010-01-10 02:01:37'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '0'
- comment_ID: '33346'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Martin Reurings: Name-calling aside, you and me come from two
    different viewpoints. You are a "Tapestry Developer" (you have more Tapestry experience
    than I have), and I''m a "Interface Developer" (I have more HTML, CSS, and JS
    experience than you have). I work with several different web frameworks in parallel,
    which mean that when a framework doesn''t behave as I''m used to, I react to that.\n\nSo
    read this blog post as <strong>my</strong> (as an Interface Developer) reaction
    to working with Tapestry. Reactions like these can be avoided in two ways: \n\n1)
    Document why Tapestry have chosen a different path than most other frameworks
    (for instance concerning white-space-collapsing). I found almost no reasoning
    when googling about the issues I encountered.\n2) Change the defaults to more
    closely match when someone like me expect. From the comments I read that Tapestry
    developers don''t like to change any defaults, since they are used to things how
    they are. That''s fine. Do step 1 instead.'
  comment_date: '2010-01-10 14:21:42'
  comment_post_ID: '528'
  comment_type: null
  is_admin: '1'
---