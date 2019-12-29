---
comments:
- comment_ID: '30435'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: Good write-up.\n\nAs we've seen in a mutual project, border-collapsing
    doesn't work properly in Firefox, when the table has a 100% width and a border
    itself
  comment_date: '2008-03-14 11:51:32'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '30437'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Robert Nyman: I remember the case of the disappearing outer border.
    But there were many more variables to fuck things up there. If you get to that
    point, then sure, use your cellspacing attribute :)'
  comment_date: '2008-03-14 12:16:38'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '1'
- comment_ID: '30438'
  comment_author: Nita
  comment_author_url: ''
  comment_content: Nice overview, thanks! But isn't it "border-collapse"?  :)
  comment_date: '2008-03-14 15:22:33'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '30440'
  comment_author: madr
  comment_author_url: http://madr.se
  comment_content: The trick with using COL has crossed my mind now and then for about
    two years now, but I never tried it - as you said, one does not use tables that
    much.\n\nNice to see that CSS does as one can expect it to. :)\n\nReally good
    writeup anyways. I will definitely show this to my collegues - since they tend
    to classitis all tables.
  comment_date: '2008-03-14 16:28:05'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '30449'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Nita: It sure is, thanks for correcting me :)'
  comment_date: '2008-03-17 08:45:28'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '1'
- comment_ID: '30453'
  comment_author: unwiredbrain
  comment_author_url: ''
  comment_content: 'Watch out! It''s not ''border-collapsing'', it''s ''border-collapse'':
    http://www.w3.org/TR/CSS21/tables.html#propdef-border-collapse'
  comment_date: '2008-03-18 01:55:24'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '30454'
  comment_author: unwiredbrain
  comment_author_url: ''
  comment_content: Err... :-\ I was reading the pre-updated. But after the update
    it still looks buggy! :) :P
  comment_date: '2008-03-18 01:58:08'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '30456'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@unwiredbrain: Thanks, but it should be correct now, I''ve double-checked.'
  comment_date: '2008-03-18 07:09:28'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '1'
- comment_ID: '30458'
  comment_author: unwiredbrain
  comment_author_url: ''
  comment_content: Really... I don't want to be dull, but what I see is 'border-collape'...\n\nOr
    you're missing a 's' or you want mokeys in your codes! :) :P\n\nHave a nice day.\nPeace
    &amp; Love\n--\nuwb
  comment_date: '2008-03-18 11:38:31'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '30460'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@unwiredbrain: Ehmm... I don''t see any missssspellings? Thanks
    again...'
  comment_date: '2008-03-18 23:44:55'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '1'
- comment_ID: '30461'
  comment_author: unwiredbrain
  comment_author_url: ''
  comment_content: 'OK. now the code section 2 ("Remove the space between the cells
    with CSS") rightly states:\n<code>table { border-collapse: collapse; }</code>'
  comment_date: '2008-03-19 03:06:32'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '30489'
  comment_author: Rob
  comment_author_url: http://brightscape.net
  comment_content: I'm working on some table -based graphs at the moment and am styling
    them with CSS. Thanks for this article, it couldn't  have come at a better time.
  comment_date: '2008-03-26 16:20:34'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '30545'
  comment_author: Sharing Best Practices!
  comment_author_url: http://mohitaneja.com
  comment_content: I was looking for the gradient background stuff for custom WordPress
    theme, the client needs the theme colors to be changed anytime. \n\nI am sure
    this is gonna help me a lot. Will give it a try.\n\nThanks for sharing..
  comment_date: '2008-04-12 07:06:32'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '30948'
  comment_author: Shafaat Awan
  comment_author_url: http://www.makadco.com
  comment_content: For me, tables are not bad, Its better to use custom CCS layout
    instead of this, tables are good for tabular data. They are not built for structuring
    the layout.
  comment_date: '2008-08-27 22:35:17'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '31683'
  comment_author: Vincenzo Romano
  comment_author_url: ''
  comment_content: I've read Hixie's interesting page.\nBut it's still not clear why
    width or border properties are different from text-align!\nWhatever the CSS mechanism
    does with the former ones, can be done for the latter. It sounds straightforward
    to my ears (but maybe I'm wrong).\nIn my opinion, it makes perfect sense to define
    table styles either by rows or by columns accordingly to the specific table.\nIn
    general, if you have items on the rows and their properties on the columns, styling
    by column makes better sense.\n\nYour suggested workaround is ... just a workaround.
    A working one, indeed.\nBut column styles should not rely on column ordering!
    And your solution does.
  comment_date: '2009-04-03 12:39:21'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '31684'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Vincenzo Romano: I agree that it''s not a perfect solution, but
    it''s the only one that works. I think hixie''s explaination simply is that width
    and border affects other cells in the table, so it you set column widths calculating
    table cell widths gets really hairy. That''s my guess anyhow.'
  comment_date: '2009-04-03 16:48:09'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '1'
- comment_ID: '31754'
  comment_author: Cody
  comment_author_url: http://www.webhostdesignpost.com
  comment_content: 'Hey thanks for the CSS table tips.  There were a couple of techniques
    I never knew about.  Like the table-layout: fixed; I always wonder how you can
    make tables obey your width element.  Also great trick with the  tag.'
  comment_date: '2009-05-20 01:28:45'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
- comment_ID: '33937'
  comment_author: Simon
  comment_author_url: ''
  comment_content: Thanks, I've used this on a site I'm working on at the moment.
    Great stuff!!
  comment_date: '2010-06-25 10:37:00'
  comment_post_ID: '110'
  comment_type: null
  is_admin: '0'
---