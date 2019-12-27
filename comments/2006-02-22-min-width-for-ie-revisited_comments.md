---
comments:
- comment_ID: '219'
  comment_author: Pete
  comment_author_url: ''
  comment_content: Can max-width be done in CSS as well, or is javascript pretty much
    required?
  comment_date: '2006-02-26 14:52:44'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '0'
- comment_ID: '222'
  comment_author: Emil Stenström
  comment_author_url: http://
  comment_content: 'Pete: what kind of max-width? I can think of a few ways to do
    a one with percents (max-width: 90%?), is that what you''re looking for?'
  comment_date: '2006-02-27 19:09:36'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '1'
- comment_ID: '224'
  comment_author: Pete
  comment_author_url: ''
  comment_content: Something like a width in % and a min and max width in em's. As
    is used in this presentation:\n\nhttp://leftjustified.net/site-in-an-hour/
  comment_date: '2006-02-28 17:16:21'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '0'
- comment_ID: '228'
  comment_author: David
  comment_author_url: ''
  comment_content: Have you tested this on IE7?\n\nhttp://blogs.msdn.com/ie/archive/2005/09/02/460115.aspx
  comment_date: '2006-03-01 07:32:27'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '0'
- comment_ID: '230'
  comment_author: Emil Stenström
  comment_author_url: http://
  comment_content: '@David: No I havn''t. From what I''ve heard about IE7 it''s not
    even close to be released for the public (serious rendering bugs). I have therefor
    not started testing in that one yet. I''m guessing that this min-width won''t
    work there since IE7 does not supprort min-width but ignores * html. I will have
    to go back and fix my examples for IE7.'
  comment_date: '2006-03-01 09:41:17'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '1'
- comment_ID: '231'
  comment_author: Pete
  comment_author_url: ''
  comment_content: Just using conditional comments instead of hacks should fix the
    IE7 thing.
  comment_date: '2006-03-01 11:37:07'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '0'
- comment_ID: '255'
  comment_author: Misty
  comment_author_url: http://www.mdrideas.com
  comment_content: I am trying to make my web site to be customized to each individual
    user resolution.  Is this possible and if so how can I do that?
  comment_date: '2006-03-09 00:41:25'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '0'
- comment_ID: '387'
  comment_author: Mislav
  comment_author_url: ''
  comment_content: 'Misty: you can hardly afford to customize to <strong>each</strong>
    individual resolution (there are too many out there). But you can make to or three
    variants of the default stylesheet for mutliple sizes and connect them with the
    dynamic resolution dependent layout solutions out there: <a href="http://www.themaninblue.com/writing/perspective/2006/01/19/"
    rel="nofollow">The man in blue</a> / <a href="http://particletree.com/features/dynamic-resolution-dependent-layouts/"
    rel="nofollow">particletree</a>.'
  comment_date: '2006-04-07 11:41:55'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '0'
- comment_ID: '5696'
  comment_author: Anonymous
  comment_author_url: ''
  comment_content: IE treats width like modern browsers treat max-width, so it can
    be alleviated easily by using:\n\n.object { max-width:500px; }\n* html .object
    { width:500px; }
  comment_date: '2006-10-13 04:49:25'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '0'
- comment_ID: '21101'
  comment_author: tom
  comment_author_url: ''
  comment_content: These bastards from ms when are they going to make a standart compliant
    browser. U know what in my new website i am going to write that it doesnt support
    IE cause of its crappy rendering!
  comment_date: '2007-02-13 20:45:41'
  comment_post_ID: '47'
  comment_type: null
  is_admin: '0'
---