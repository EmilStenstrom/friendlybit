---
comments:
- comment_ID: '31187'
  comment_author: Jonatan Larsson
  comment_author_url: ''
  comment_content: Great article! This was news for me, and will come in handy in
    future projects.
  comment_date: '2008-11-18 20:23:26'
  comment_post_ID: '323'
  comment_type: null
  is_admin: '0'
- comment_ID: '31189'
  comment_author: Steve Celius
  comment_author_url: http://labs.episerver.com/en/Blogs/Steve-Celius/
  comment_content: Nice trick. I usually do this with controls inheriting from asp:panel,
    which lets me do this inline. I render html from code behind though (building
    my own control tree, not pasting markup).\n\nYour example is much cleaner, the
    surrounding markup can always be changed without having to recompile (when IE8
    comes out for an example :-)\n\n/Steve
  comment_date: '2008-11-19 15:59:27'
  comment_post_ID: '323'
  comment_type: null
  is_admin: '0'
- comment_ID: '31190'
  comment_author: Anders
  comment_author_url: ''
  comment_content: When do you think we should take the next step and start using
    css3 for purposes such as rounded corners? Browser support is not that good at
    the moment, i know, but don't you too think it sucks to insert those extra divs
    just to get the corner effect?
  comment_date: '2008-11-19 20:38:17'
  comment_post_ID: '323'
  comment_type: null
  is_admin: '0'
- comment_ID: '31191'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jonatan: Thanks!\n\n@Steve: Ah, interesting, I''ve never even
    heard of that trick. One more thing, did you find the article because it had "EPiServer"
    in it? You work with them right?\n\n@Anders: Well, not yet. I''m still struggling
    to get customers to not build for IE6, rounded corners with CSS is far, far, far
    away. (I''ll tell you when I switch, I promise :)'
  comment_date: '2008-11-19 21:37:24'
  comment_post_ID: '323'
  comment_type: null
  is_admin: '1'
- comment_ID: '31207'
  comment_author: Mårten Berg
  comment_author_url: ''
  comment_content: 'Thanks for the tip, really neat. However, due to a bug in ASP.NET
    there may be problems in the designer and code-behind using some nested web controls
    within the templated control. If you experience this, you need to explicitly point
    out the nested control in a slightly odd way: \n\n<code>\n\n   \n      \n      ...\n   \n</code>\nand
    in code-behind:\n<code>\nRepeater myNestedRepeater = (Repeater)MyBox.FindControl("PlaceHolder1").Controls[0];\n</code>\n\nHope
    it helps somebody.'
  comment_date: '2008-11-27 10:13:25'
  comment_post_ID: '323'
  comment_type: null
  is_admin: '0'
- comment_ID: '31208'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Mårten Berg: Yes, that''s why the example includes TemplateInstance.Single,
    which means that you can reference controls inside directly. It''s a neat trick
    that works well for all the simple cases (like this one). If you start looping
    you need to throw in some FindControls and remove the TemplateInstance.Single.
    Thanks for your comment!'
  comment_date: '2008-11-27 11:09:00'
  comment_post_ID: '323'
  comment_type: null
  is_admin: '1'
- comment_ID: '31785'
  comment_author: Ken Platt
  comment_author_url: ''
  comment_content: I just want to say thanks... I've been doing template controls
    for a while now and every once in a while I've gotten weird errors around the
    designer file not liking it. Your simple example allowed me to see what I was
    doing wrong. This is going to save me a TON of time!
  comment_date: '2009-06-10 23:21:50'
  comment_post_ID: '323'
  comment_type: null
  is_admin: '0'
- comment_ID: '31787'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Ken Platt: You''re welcome!'
  comment_date: '2009-06-12 09:41:25'
  comment_post_ID: '323'
  comment_type: null
  is_admin: '1'
---