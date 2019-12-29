---
comments:
- comment_ID: '30591'
  comment_author: Nick Dunn
  comment_author_url: http://nick-dunn.co.uk
  comment_content: I agree wholeheartedly with your comments here. I'll add a few
    more points:\n\n- Set the xHtmlConformanceMode to "strict" in the Web.config.
    This way, even if you do use server controls which generate a lot of HTML, it
    will at least be valid.\n\n- Don't write off the ASP:Label control. It's main
    purpose is for form labels and it achieves this very well. Using an ASP:Label
    and ASP:TextBox pair will generate the same HTML markup I would write by hand
    anyway (except the auto-generated ID/name attributes).\n\nThe ASP:Label control
    becomes confusing when no AssociatedControlId is set, as it outputs a SPAN rather
    than a LABEL to the HTML.\n\nThe two most powerful server controls for the standards-aware
    developer are the ASP:Repeater (as you mentioned) and the ASP:Literal. The latter
    is simply an empty placeholder into which you can stuff any text or HTML.\n\nAvoid
    the Validation server controls like the plague, if you care about markup. Adding
    a validator will add an onsubmit() handler to your form, and force the client
    to download a ton of JavaScript.\n\nASP.NET is incredibly powerful and indeed
    web-standards compliant. But only in the right hands :-)
  comment_date: '2008-05-17 13:38:55'
  comment_post_ID: '157'
  comment_type: null
  is_admin: '0'
- comment_ID: '30592'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Nick Dunn: Great comment Nick! The only reason I don''t like
    asp:label is because it really isn''t needed. Writing a label by hand is just
    as easy, even though you have to get the ClientID of the control then for the
    for attribute.\n\nThe same with asp:literal, you could use &lt;%= text %&gt; instead
    if you wanted.\n\nNo matter what, I don''t think that distinction is too important.
    As long as you know what you''re doing and care about the HTML.'
  comment_date: '2008-05-17 13:59:05'
  comment_post_ID: '157'
  comment_type: null
  is_admin: '1'
- comment_ID: '30594'
  comment_author: Martin S.
  comment_author_url: http://www.dileno.com
  comment_content: 'Indeed a good blog post. I agree with most of the stuff written
    here. A lot of things can be written on this subject, but I narrow it down to
    some more tips:\n\n- CSS adapters for better semantics: <a href="http://www.asp.net/CssAdapters/\n\n-"
    rel="nofollow">http://www.asp.net/CssAdapters/\n\n-</a> How to control adapters:
    <a href="http://www.singingeels.com/Articles/How_To_Control_Adapters.aspx\n\nBtw,"
    rel="nofollow">http://www.singingeels.com/Articles/How_To_Control_Adapters.aspx\n\nBtw,</a>
    use Literal instead of Label when you need to output text from codebehind, unless
    it should be  - then you can use the AssociatedControlId attribute. And PlaceHolder
    is always better than a Panel. The Panel creates a wrapping div, which PlaceHolder
    does not.'
  comment_date: '2008-05-17 14:19:58'
  comment_post_ID: '157'
  comment_type: null
  is_admin: '0'
- comment_ID: '30598'
  comment_author: buckley
  comment_author_url: ''
  comment_content: <a href="http://www.west-wind.com/WebLog/posts/127340.aspx\n\n"Maybe"
    rel="nofollow">http://www.west-wind.com/WebLog/posts/127340.aspx\n\n"Maybe</a>
    the most important feature of this control is that like the Repeater control it
    provides much more control over the rendering process at the cost of more markup
    code in the page."
  comment_date: '2008-05-18 00:54:52'
  comment_post_ID: '157'
  comment_type: null
  is_admin: '0'
- comment_ID: '30600'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Martin S, buckley: Great comments! I really need to expand the
    comments area, you are adding invaluable data to my posts :)'
  comment_date: '2008-05-18 11:24:59'
  comment_post_ID: '157'
  comment_type: null
  is_admin: '1'
- comment_ID: '30672'
  comment_author: Anna Kolesnik
  comment_author_url: http://blogs.helion-prime.com
  comment_content: I like to follow standards. I'm using all w3c validators from strict
    markup to link checkers, and  I'm always glad to find something new .. \nthank
    you
  comment_date: '2008-05-30 14:56:27'
  comment_post_ID: '157'
  comment_type: null
  is_admin: '0'
- comment_ID: '30692'
  comment_author: Alan Cyment
  comment_author_url: http://www.aggiorno.com
  comment_content: 'You might want to give Aggiorno a try next time you want to try
    and make an ASP.NET site standard. It can make an entire site XHTML 1.0 Transitional
    compliant with a few clicks, including a wizard that will take you over all the
    images that lack an ALT description and a very very smart tag closing agent. It''s
    currently in beta phase and beta is not time limited in any sense, so you might
    as well get a decent version for free: <a href="http://www.aggiorno.com/download.aspx"
    rel="nofollow">http://www.aggiorno.com/download.aspx</a> \n\nCheers,\nAlan'
  comment_date: '2008-06-02 15:05:05'
  comment_post_ID: '157'
  comment_type: null
  is_admin: '0'
- comment_ID: '30798'
  comment_author: Scott
  comment_author_url: http://reusablecode.blogspot.com
  comment_content: This is exactly what kept me from jumping into ASP.NET; I'd like
    to see more info on how to write good ASP.NET code.
  comment_date: '2008-07-06 15:07:36'
  comment_post_ID: '157'
  comment_type: null
  is_admin: '0'
---