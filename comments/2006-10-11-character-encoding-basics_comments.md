---
comments:
- comment_ID: '5670'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: Python is without the semi-colon. ;-)
  comment_date: '2006-10-12 00:49:28'
  comment_post_ID: '96'
  comment_type: null
  is_admin: '0'
- comment_ID: '5674'
  comment_author: Juani
  comment_author_url: ''
  comment_content: Hi Emil! Thank you very much for this article! Until now I was
    manually/automatic encoding my chars (I develop in spanish) and was really painfull,
    now I only have to save it in UTF-8... simply brilliant!
  comment_date: '2006-10-12 04:17:27'
  comment_post_ID: '96'
  comment_type: null
  is_admin: '0'
- comment_ID: '5723'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Juani: Yeah, I have some experience with manually maintaining
    local languages with entities.UTF-8 is just way better :)'
  comment_date: '2006-10-14 10:53:07'
  comment_post_ID: '96'
  comment_type: null
  is_admin: '1'
- comment_ID: '5865'
  comment_author: Birgit
  comment_author_url: http://ice-horse.de
  comment_content: Hey, thanks a lot, this really helps! I never knew about the "View
    response headers" option and never understood why I have to encode certain characters
    although I set the encoding in the HTML header...now I know :)
  comment_date: '2006-10-21 11:36:55'
  comment_post_ID: '96'
  comment_type: null
  is_admin: '0'
- comment_ID: '6117'
  comment_author: Mark McDonnell
  comment_author_url: ''
  comment_content: Strange, I used the "View Response Headers" on one of our websites:\n\nhttp://www.firetuck.co.uk/Home.asp\n\n...and
    found that the response headers didn't show anything for Content-Type OR Content-Encoding.\n\nContent-Type
    did show "text/html" but nothing about the character encoding.\n\nAny suggestions?
  comment_date: '2006-10-27 14:47:41'
  comment_post_ID: '96'
  comment_type: null
  is_admin: '0'
- comment_ID: '6125'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Mark McDonnell: That means that you don''t send *any* encoding
    at all (not that uncommon). Have a look at the example code for you language and
    add it to your main template. No need to keep the browser guessing what encoding
    you use.'
  comment_date: '2006-10-27 18:10:29'
  comment_post_ID: '96'
  comment_type: null
  is_admin: '1'
- comment_ID: '6128'
  comment_author: Nita
  comment_author_url: ''
  comment_content: 'So, rely on your server to send the right encoding.\n\nThat''s
    easy to say, but not everyone has the power to set server headers ;)\n\nHere''s
    a fun article on the inner workings of character sets, if anyone''s interested:
    http://www.joelonsoftware.com/articles/Unicode.html'
  comment_date: '2006-10-27 19:10:33'
  comment_post_ID: '96'
  comment_type: null
  is_admin: '0'
- comment_ID: '7673'
  comment_author: Rasmus Kaj
  comment_author_url: http://www.stacken.kth.se/~kaj/
  comment_content: Actually, at first computer people thought 128 characters to be
    enough, and thats what ASCII is. The eight bit was used for checksumming or (often)
    not at all.  There was localized versions of the 7-bit character set, such as
    the one replacing [|]{\} with the Swedish åäöÅÄÖ.\n\nAfter a while, to important
    steps were taken; 1) The eight bit was used, doubling the number of characters,
    and 2) ways of specifying the character set in (mainly) email started to develop.\n\nFrom
    that, the story goes pretty much as you tell it ... :-)
  comment_date: '2006-11-23 00:12:51'
  comment_post_ID: '96'
  comment_type: null
  is_admin: '0'
- comment_ID: '7677'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rasmus Kaj: Thanks for the clarifications :)'
  comment_date: '2006-11-23 00:32:23'
  comment_post_ID: '96'
  comment_type: null
  is_admin: '1'
---