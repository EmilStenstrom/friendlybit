---
comments:
- comment_ID: '5664'
  comment_author: Niels Leenheer
  comment_author_url: http://rakaz.nl
  comment_content: 'Hi Emil,\n\nI believe there are two fundamental mistakes in your
    article. First of all, this is not a bug and secondly, there are two ways to specify
    the encoding of an css stylesheet.\n\nLet me explain. Western character encodings
    use a single byte for each character. UTF-8 uses multiple bytes. Some characters
    use a single byte, other two or three. The first byte of such a doublet or triplet
    is an indication of how many bytes that particular character is using. \n\nWhen
    you use the å character in one of the ISO-8859 encodings it will use the same
    byte value as the first byte in one of those UTF-8 multibyte characters. \n\nSo
    IE treats the å as the start of a multibyte character. The next bytes are part
    of the same character. Now, if that next byte is the asterisk of the comment closing
    marker it will break the marker and the comment will simply never end. For example
    /*å*/ will become something like this: /*?/. The questionmark represents one multibyte
    UTF-8 character.\n\nSo, this is normal behavoir and certainly not a bug. IE just
    parses the stylesheet as instructed.\n\nSecondly. There are two ways to specify
    the charset encoding of the stylesheet. First of all you can configure the server
    to tell the browser by using HTTP headers, or you could use the @charset "at-rule".
    For example, start your css file with: @charset "UTF-8";'
  comment_date: '2006-10-11 22:56:27'
  comment_post_ID: '97'
  comment_type: null
  is_admin: '0'
- comment_ID: '5665'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Niels: I could understand the bug if it was å*/, but as you see
    in the example there''s a space in between the å and the *. That''s a bug then
    isn''t it?\n\nI had heard of the @charset rule but didn''t think there where any
    browser support for it. Is there?\n\nThis blog is more practical than adhearing
    to specifications :) Good comment, and thanks for pointing out my errors.'
  comment_date: '2006-10-11 23:38:02'
  comment_post_ID: '97'
  comment_type: null
  is_admin: '1'
- comment_ID: '5668'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: IE6 treats the iso-8859-1 string "å *" as a three-byte character
    when interpreted as utf-8. Other browsers don't. (I'm not sure which is correct.)\n\n@charset
    is supported by at least Gecko, Opera and recent WebKit builds, and it seems IE6
    supports it too, actually.
  comment_date: '2006-10-12 00:18:53'
  comment_post_ID: '97'
  comment_type: null
  is_admin: '0'
- comment_ID: '5669'
  comment_author: Niels Leenheer
  comment_author_url: http://rakaz.nl
  comment_content: '@emil: In the ISO 8859 character set the character å is represented
    by the hexadecimal value of E5. \n\nIf the first byte of a character in the UTF-8
    charset starts with a hexadecimal value between E0 and EF, then the character
    consists of three bytes. \n\nSo, both the å, the space and the asterisk would
    be part of a single character...'
  comment_date: '2006-10-12 00:20:20'
  comment_post_ID: '97'
  comment_type: null
  is_admin: '0'
- comment_ID: '5720'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Niels: Interesting. Then it''s not a IE bug, just a difference
    in handling between IE and Firefox. Interesting to see Firefox handling stuff
    more code less strict than IE. I''m blessed with skilled readers!'
  comment_date: '2006-10-14 10:39:41'
  comment_post_ID: '97'
  comment_type: null
  is_admin: '1'
---