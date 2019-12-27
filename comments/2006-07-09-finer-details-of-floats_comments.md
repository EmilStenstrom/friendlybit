---
comments:
- comment_ID: '2961'
  comment_author: Cerebral
  comment_author_url: ''
  comment_content: Yeah indeed, good to know this subtlety. That's the kind of things
    you never know until you encounter a problem related to it cause you seriously
    can't know all the specs (which are like you wrote "not meant to be easy to read")
  comment_date: '2006-07-09 17:44:17'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '0'
- comment_ID: '2966'
  comment_author: Mark C.
  comment_author_url: http://www.gigadesign.be
  comment_content: Somthimes you will find strange stuff happening.\nThanks for the
    tip
  comment_date: '2006-07-09 20:08:21'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '0'
- comment_ID: '2981'
  comment_author: Rowan Lewis
  comment_author_url: http://www.pixelcarnage.com/
  comment_content: Its things like this that make me think the w3c got it wrong...\n\nBut
    its too late to complain now :(
  comment_date: '2006-07-10 06:01:24'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '0'
- comment_ID: '3022'
  comment_author: Skalman
  comment_author_url: ''
  comment_content: I don't agree with Rowan. I think it's a bit obvious. The specs
    are logical this way, and I can't think why it shouldn't be that way.\n\nI agree
    that it could be a problem, and I believe there isn't a solution, without JavaScript,
    or some kind of future conditional CSS.
  comment_date: '2006-07-12 00:59:09'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '0'
- comment_ID: '3029'
  comment_author: Rowan Lewis
  comment_author_url: http://www.pixelcarnage.com/
  comment_content: 'Let me explain a little more, by doing this they have removed
    a chance to make CSS more flexible, what they should have done is written it to
    behave like Internet Explorer <em>unless</em> <code>clear: *;</code> had been
    set.\n\nThis would let us choose how we want the design to work, because I can
    see that both options are useful.'
  comment_date: '2006-07-12 06:32:55'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '0'
- comment_ID: '3031'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: I think the reason for this rule has to do with making the rendering
    faster. Progressive rendering perhaps?\n\nIt's not too bad in my opinion, putting
    the boxes in two "column divs" was easy enough (even though that gives another
    source order).\n\nAs long as browsers render things _one_ way, whether that way
    is good or bad, I'm all happy :)
  comment_date: '2006-07-12 12:12:49'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '1'
- comment_ID: '3034'
  comment_author: Jennifer Grucza
  comment_author_url: ''
  comment_content: So, just curious, what did you end up doing to get the layout you
    wanted?
  comment_date: '2006-07-12 19:32:03'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '0'
- comment_ID: '3037'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jennifer Grucza: I ended up looping over the list twice server-side
    and build two lists of content. Each list was wrapped in a div and of course displayed
    appropriately. I''m pretty sure it can be done using some other method but I simply
    didn''t have the time to experiment more. This made everything work like it should
    except none styled browsers, they got the content in the wrong order.'
  comment_date: '2006-07-13 00:27:44'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '1'
- comment_ID: '3320'
  comment_author: exe
  comment_author_url: ''
  comment_content: '<br />\n<p>Shouldn''t going over it once be enough? Something
    like this:</p>\n<ol>\n<li>Create an array from the list</li>\n<li>Create a second
    array</li>\n<li>Loop over the first list once and for each item: if number is
    odd copy the item to the second list and after that delete the item in the first
    list.</li>\n<li>Print each list in the correct wrapper.</li>\n</ol>'
  comment_date: '2006-07-25 16:24:30'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '0'
- comment_ID: '3347'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@exe: Yes, once would be enough. The solution chosen was best
    in the context (avoid hard code, small list or items)'
  comment_date: '2006-07-26 02:10:33'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '1'
- comment_ID: '4274'
  comment_author: Adedeji Olowe
  comment_author_url: http://www.dejiolowe.com
  comment_content: Nice article. Is there a place where one could read web standards
    in plain "English"?
  comment_date: '2006-09-03 14:39:00'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '0'
- comment_ID: '4288'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Adedeji Olowe: I''m hoping this site is trying to do that :)
    Stay tuned.'
  comment_date: '2006-09-03 22:38:06'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '1'
- comment_ID: '30649'
  comment_author: Engraellat de caixes - blog.esbudellat, esbudellant estàndards
  comment_author_url: http://esbudellat.net/engraellat-de-caixes/
  comment_content: '[...] Finer details of floats [...]'
  comment_date: '2008-05-25 17:48:06'
  comment_post_ID: '76'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '31019'
  comment_author: gotMilk
  comment_author_url: ''
  comment_content: 'At the end of rule 2:\n''#child2 must be moved below #child2 instead''
    should read ''#child2 must be moved below #child instead'', no? ;)'
  comment_date: '2008-09-09 13:22:34'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '0'
- comment_ID: '31021'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@gotMilk: Thanks! I corrected it.'
  comment_date: '2008-09-09 23:37:45'
  comment_post_ID: '76'
  comment_type: null
  is_admin: '1'
---