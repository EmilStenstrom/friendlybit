---
comments:
- comment_ID: '2823'
  comment_author: SitePoint Blogs &raquo; Jul 3, 2006 News Wire
  comment_author_url: http://www.sitepoint.com/blogs/2006/07/04/jul-3-2006-news-wire/
  comment_content: '[...] Current issues with Microformats Emil Stenström points out
    some of the downsides of microformats (e.g. they don’t use namespaces), and suggests
    how they might be addressed (e.g. meta tags to declare microformat versions in
    use). (tags: microformats) [...]'
  comment_date: '2006-07-03 22:46:43'
  comment_post_ID: '74'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '2837'
  comment_author: Richard Conyard
  comment_author_url: http://www.thinkcolony.com
  comment_content: Of the parts you mention I don't think you're issues with Microformats
    are likely to be addressed.  At present they are semantics for the rest of us,
    for proper semantics RDF and OWL would appear to be better options.
  comment_date: '2006-07-04 15:40:48'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '0'
- comment_ID: '2841'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Richard Conyard: Why not fix them? The fixes I propose are one
    line each and they make is easier for everyone involved. Except the specwriters...'
  comment_date: '2006-07-05 00:58:05'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '1'
- comment_ID: '2850'
  comment_author: John Drinkwater
  comment_author_url: http://johndrinkwater.name/
  comment_content: The approach microformats has used in some of their specs seems
    to me less semantic and a step back from where people are heading.\n\nIn respect
    to dates, would using ins tags to markup the time be suitable ? They already contain
    a datetime attr, and define what you are saying - "this has been inserted at/for".\nI
    cant really see using the class attr for yet more data.\n\nFor the meta proposal
    and parsers/bots, I presume sites without the meta tag should ignore classes as
    a special case?
  comment_date: '2006-07-05 21:31:17'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '0'
- comment_ID: '2851'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@John Drinkwater: using the ins element is a great idea! It does
    not hit 100% on target but it''s very close. \n\nMy proposal is that the meta
    element gets required, yes. If it doesn''t exist on a site the crawlers will not
    have to continue past the &lt;head> block.'
  comment_date: '2006-07-05 23:39:46'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '1'
- comment_ID: '2857'
  comment_author: Kevin Marks
  comment_author_url: http://epeus.blogspot.com
  comment_content: Namespaces are not needed, because microformats work to converge
    meaning, instead of diverging it. Adding profile link is helpful, but doing it
    with meta instead of link is an odd suggestion. In practice not all publishers
    can change the head of a page, so microformats are deliberately not strict about
    this. This does make a little more work for people writing parsers, but a lot
    less for those publishing the formats. This is intentional, as successful formats
    have far more publishers than parser writers.\nRegarding ISO 8601 and abbr, that
    is a legitimate semantic use - the title is more specific. If you don't like the
    form of 8601 Tantek used there, '20060621T1030-0700' can be expressed as '2006-06-21
    10:30-0700' which is broadly human readable too.\nSo, these don't need fixing,
    they are by design. Microformats do not add extra elements to HTML, they re-use
    existing semantic elements to converge and add meaning.
  comment_date: '2006-07-07 11:02:23'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '0'
- comment_ID: '2863'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Kevin Marks: Thanks for your comment. I''ll try to address the
    issues you bring up:\n\n1) In what way is specifying what you mean by the class
    "vcard" diverging? I''d say that''s specifying what you mean. \n\n2) I''m wasn''t
    aware that you could link to the profile too, but the way you do it is not really
    imortant, the point is that is will lead to hell if a namespace is not there.\n\n3)
    No, that''s not readable. The time and timezone looks like a strange interval
    of some kind. Also, UTC or GMT? They are there by design, but by faulty design,
    title is not there for computers.\n\n4) My fault at "extra elements". I ment "extra
    divs and spans", also known as "div hell" by some. I updated the paragraph to
    reflect that.\n\nI''m well aware that microformats are like they are by design,
    it''s the design I''m commenting on.'
  comment_date: '2006-07-07 18:57:15'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '1'
- comment_ID: '3348'
  comment_author: Martin
  comment_author_url: ''
  comment_content: Thanks for an interesting article.  You're quite right about new
    techniques related to web development and the lack of a critical look at them,
    and so as a newish user of microformats, your article came at just the right time.\n\nWhile
    the ideas behind microformats appeal to me no end, I found myself agreeing with
    many of your points, particularly the awkward use of the ABBR element and its
    title attribute.\n\nAnother specific limitation of the hcalendar format that I
    think is interesting to mention is its difficulty in handling <em>recurring</em>
    events - say, a radio show that happens at the same time every Monday evening.  Not
    much progress, it seems, has been made in terms of establishing an agreed way
    handling evebts like this, that are not restricted to a specific ordinal date
    (like Wednesday 26 July 2006 at 20:00), but rather need only a day and time to
    be specified.  The documentation at the microformats site admits this much.  \n\nSo
    far, the 'best' I have come up with in terms of marking-up recurring events in
    a schedule is to use the specific date of the first day the event occurs <em>after</em>
    Summer/Winter Daylight Saving changes kick in, specifying the appropriate amount
    of hours after GMT for the start time, specifying a duration time for that event
    (rather than a definite finish time), and declaring the frequency with which the
    event recurs using the RRULE class.  For example, for an event that happens every
    Wednesday at 20:00, lasting for 3 hours, I specify the first Wednesday after the
    time changes to Summertime (so, 20060329), GMT plus 2 hours (T2000+0200), and
    a duration of 3 hours (PT3H) to give me a dtstart value of "20060329T2000+0200/PT3H).  Then
    I declare the RRULE class on an element with the FREQ class inside a child element,
    giving that child element the value 'weekly'.\n\nI have no idea if this is sufficient.  Worse,
    does anybody? ;)
  comment_date: '2006-07-26 03:33:27'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '0'
- comment_ID: '3368'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Martin: Thanks.\n\nI''m afraid I can''t help you with hCalendar,
    I have no experience with the format.'
  comment_date: '2006-07-26 13:57:23'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '1'
- comment_ID: '3373'
  comment_author: Martin
  comment_author_url: ''
  comment_content: Emil,\n\nThat's OK, I didn't post with the intention of getting
    help.  I just wanted to point out for everyone an acknowledged shortcoming of
    the design of the format, in addition to the ones you mentioned.
  comment_date: '2006-07-26 15:15:38'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '0'
- comment_ID: '3418'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: Emil,\n\nI'm glad that you had a good time! Thanks for the writeup;
    very good and well-needed (you beat me to it! :-)).
  comment_date: '2006-07-29 13:23:12'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '0'
- comment_ID: '3431'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: Thanks Robert. I'm looking forward to the next meetup.
  comment_date: '2006-07-30 05:15:18'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '1'
- comment_ID: '3885'
  comment_author: Yeah, Nyman’s back - Robert’s talk
  comment_author_url: http://www.robertnyman.com/?p=491
  comment_content: '[...] We had a Geek Meet in June, and Emil did a good write-up
    of one of the presentations/talks in Current issues with Microformats. [...]'
  comment_date: '2006-08-22 14:29:26'
  comment_post_ID: '74'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '25121'
  comment_author: Rotem
  comment_author_url: ''
  comment_content: Hi, I'd just like to comment that (strictly speaking) GMT is not
    a time zone really. When people use "GMT" as a time zone, they actually refer
    to UTC+0. Time zone offsets always refer to UTC, so there's no ambiguity.\n\nThat's
    not to say I don't agree with the article, I just felt like sharing some knowledge.
    =)
  comment_date: '2007-06-10 23:34:26'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '0'
- comment_ID: '25151'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rotem: Thanks, reading up on timezones was good for me :) I changed
    the two examples to be GMT-7 and PDT-7 (instead of UTC-7 which would be the same
    zone ;). Anyway, I''ll keep GMT because people know what I mean when I use it,
    UTC is not as widely spread from what I know (in Sweden). Good comment.'
  comment_date: '2007-06-11 21:00:55'
  comment_post_ID: '74'
  comment_type: null
  is_admin: '1'
---