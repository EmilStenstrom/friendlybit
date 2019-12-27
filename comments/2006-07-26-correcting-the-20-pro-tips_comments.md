---
comments:
- comment_ID: '3371'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: 8) The margin is not included in the width/height calculation in
    IE5's box model, only the padding and border are.\n\n11) Photoshop's PNGs aren't
    compressed to the format's full potential, and it labels them which causes the
    color problems in IE. However, you can run your PNGs (and GIFs) though <a href="http://advsys.net/ken/utils.htm"
    rel="nofollow">PNGOUT</a> which compresses the image losslessly, and fixes the
    color labeling problems in IE (although not the gamma correction problems in old
    Safari).
  comment_date: '2006-07-26 14:50:51'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '0'
- comment_ID: '3372'
  comment_author: Nate
  comment_author_url: http://www.theklaibers.com
  comment_content: I would agree with your revised list, and many of those were things
    I was thinking while reading through the previous article. It seemed too shallow
    - yours seems more solidified (practically - like NOT using inline styles and
    the align attribute - goes against using CSS in the first place).\n\nAnd, as you
    have said - NS4 and IE5 are dinosaurs, and so each site should check to see if
    they have any users from those browsers. The site I work for has NO users from
    NS4, at all, and a few IE5 (some are IE5 on Mac from me - which his no longer
    supported by Microsoft or Mac - so I have stopped supporting it as well).\n\nNice
    revisions!
  comment_date: '2006-07-26 15:12:35'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '0'
- comment_ID: '3384'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@zcorpan: Thanks for pointing out that margin is not included
    in IE5''s width, I updated the text to reflect that.\n\nAlso good points about
    Photoshops handling of PNGs. I use Fireworks myself (they use PNG as their default
    format) and have not experienced any problems with it''s PNGs. Worth a note though
    is that the internal PNGs should not be put on the web directly, use the export
    option.\n\n@Nate: Thanks!'
  comment_date: '2006-07-26 19:44:26'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '1'
- comment_ID: '3398'
  comment_author: Jon
  comment_author_url: http://mondaybynoon.com
  comment_content: It seems like you've made some really good points here -- I've
    just started browsing around the .NET site since coming across the article and
    I'm intrigued... it's too bad you can only snag it in the UK.  I'll have to stick
    with what they publish to the Web.
  comment_date: '2006-07-27 14:39:27'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '0'
- comment_ID: '3426'
  comment_author: Johan
  comment_author_url: ''
  comment_content: Good points about image formats. Use 8-bit PNGs instead of GIF,
    it makes you smaller files. \n\nNot always, small gifs (eg  4K) can be smaller
    than saving it as png (eg 7K), when the images get larger in fliesize I never
    see a gif being smaller than a png in filesize. This could be a fault of Photoshop
    or even Fireworks to not compress enough the pngs (png-8) that is
  comment_date: '2006-07-29 22:46:35'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '0'
- comment_ID: '3427'
  comment_author: Johan
  comment_author_url: ''
  comment_content: why repeat the alt text?\n\ncould be intentional since not all
    browsers show the alt as a tooltip ??
  comment_date: '2006-07-29 22:48:52'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '0'
- comment_ID: '3432'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Johan: You might be right about the small images there. I tend
    not to use GIF anyways though since mixing formats on one site feels strange.\n\nAbout
    alt text: if you add it on both places you might end up with a screen reader reading
    your description twice, something you want to avoid. Perhaps leaving the alt text
    empty would be better in that case.'
  comment_date: '2006-07-30 05:27:12'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '1'
- comment_ID: '3433'
  comment_author: Rowan Lewis
  comment_author_url: http://www.pixelcarnage.com/
  comment_content: Johan, I find that The GIMP tends to compress PNG images a lot
    better than Photoshop.\n\nI now use both Photoshop and The Gimp, simply because
    Photoshop makes a mess of PNGs. So instead of splicing  up my designs in Photoshop,
    I save them as a bitmap then open it in The GIMP :)
  comment_date: '2006-07-30 13:20:23'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '0'
- comment_ID: '3727'
  comment_author: Nick Shaw
  comment_author_url: ''
  comment_content: Point 6 Use simple PHP to build sites the article is right. It
    states the file CALLING the includes should end .php which is correct. The example
    (html) is the file being included in .php file.
  comment_date: '2006-08-10 15:31:33'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '0'
- comment_ID: '3829'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Nick Shaw: Ah, misstake on my side, I guess we all do them. I
    removed that correction. Thanks.'
  comment_date: '2006-08-16 15:28:52'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '1'
- comment_ID: '4177'
  comment_author: Brian
  comment_author_url: ''
  comment_content: 'Why call these corrections? Aren''t most of these opinions, or
    suggestions? I appreciate your suggestions, but that sounds a bit presumptuous.\n\nRe:
    the use of inline CSS. There is a very good reason why the W3C developed CSS with
    inline capability. In Dynamic web development, there are times when an inline
    CSS definition can be used to override an existing definition in the CSS file.
    This would (technically) also separate content from presentation, as the presentation
    data would be stored as a variable in PHP or stored in a database as opposed to
    being written statically in the HTML file.'
  comment_date: '2006-08-31 15:53:27'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '0'
- comment_ID: '4185'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Brian: The .NET article is aimed at beginners and got a lot of
    exposure on big CSS sites. Since I find it slightly annoying with errors when
    I''m learning myself I thought that it might help someone else too. The things
    pointed out are things that I consider are best practices and I''ve not seen much
    complaints in the comments (believe me, people notice those things here ;) so
    I think they agree. \n\nOn inline CSS: I know what they where originally thought
    for, that doesn''t change anything :)'
  comment_date: '2006-08-31 21:57:44'
  comment_post_ID: '84'
  comment_type: null
  is_admin: '1'
---