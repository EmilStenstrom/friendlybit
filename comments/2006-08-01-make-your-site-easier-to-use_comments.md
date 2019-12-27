---
comments:
- comment_ID: '3473'
  comment_author: sherzy
  comment_author_url: http://www.sherzy.com
  comment_content: 'I am happy to see your tip about using labels, and the CSS: label
    { cursor: pointer; } seems like a nice idea, until you realize that it will make
    ALL of your labels appear clickable, which is not desirable. Remember, labels
    should be used for all form fields (text boxes and areas, select lists) in order
    to aid the disabled, as explained in the webstandards article.'
  comment_date: '2006-08-01 22:32:17'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '0'
- comment_ID: '3475'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@sherzy: Why not make the labels of the other form elements clickable
    too? Clicking on a text element''s label focuses the textbox. How is that bad?'
  comment_date: '2006-08-01 23:19:58'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '1'
- comment_ID: '3476'
  comment_author: sherzy
  comment_author_url: http://www.sherzy.com
  comment_content: 'Emil: That is a good point, and on my own site I may implement
    it. Unfortunately the designers and information architects where I work do not
    agree – they feel that it would confuse the user to have text and select list
    label appear clickable.'
  comment_date: '2006-08-01 23:57:41'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '0'
- comment_ID: '3478'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@sherzy: Interesting. Well I guess it doesn''t matter much as
    long as they use the &lt;label&gt; tags anyway. Perhaps classing the checkboxes
    and radiobuttons instead? You wouldn''t want people to miss the nice feature.\n\nTo
    add the cursor to only the other elements in newer browsers you can use:<code
    lang="css">\ninput[type="checkbox"]+label { cursor: pointer }\n</code> ...to affect
    only the checkboxes (Similar code for radio buttons). But of course IE (not even
    IE7) will support that.'
  comment_date: '2006-08-02 00:13:32'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '1'
- comment_ID: '3494'
  comment_author: Agrajag
  comment_author_url: ''
  comment_content: Hi\nI just thought I would point out that, rather ironically, you
    used the wrong 'to' in the last paragraph of the section about writing well :P.
    It should be replaced with 'too'.
  comment_date: '2006-08-02 05:55:25'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '0'
- comment_ID: '3499'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Agrajag: Very picky are we? :) *fixed*'
  comment_date: '2006-08-02 09:21:02'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '1'
- comment_ID: '3504'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: IE7 does support that selector, although you can probably make
    it a bit simpler:\n<code>input + label {...}</code>\n...since you normally only
    use the label after the input for check boxes and radio buttons anyway (unless
    you wrap the form control inside the label).\n\nIf you're using &lt;label&gt;
    elements and they aren't clickable then you're using them incorrectly, and they
    will not aid assistive technologies.\n\nOh, and by the way, I wouldn't recommend
    changing the cursor for labels. It is the responsibility of the browser to make
    labels appear clickable, and changing the cursor might be confusing or annoying.
  comment_date: '2006-08-02 11:59:38'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '0'
- comment_ID: '3509'
  comment_author: Martin Jansson
  comment_author_url: http://www.marja.se
  comment_content: When I use clickable labels for checkboxes and radio buttons (which
    I always do, by the way) I always put the input-element <em>inside</em> the label.
    In that way, you don't have to use the "for" -attribute for the label to be connected
    to the input-element. And it also makes positioning easier as you can position
    the label with the checkbox or radio button inside it.\n<code lang="html">&lt;label&gt;&lt;input
    type="checkbox"&gt; Click me!&lt;/label&gt;</code>
  comment_date: '2006-08-02 13:48:08'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '0'
- comment_ID: '3510'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@zcorpan: Ah, good to hear about IE7. Seems better than I expected.\n\nIf
    you read what sherzy said you''ll see that we only wanted to change the cursor
    for checkboxes and radio buttons. That was the point.\n\nI believe changing cursor
    is a good idea, it''s making it easier for the user to see that they don''t have
    to  click that tiny checkbox. The browsers don''t support it so we have to do
    it ourselves.'
  comment_date: '2006-08-02 13:50:07'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '1'
- comment_ID: '3524'
  comment_author: Roger Johansson
  comment_author_url: http://www.456bereastreet.com
  comment_content: 'Changing the cursor to pointer for label elements sounds like
    a good idea at first, but there are browsers (like Safari) that do not make label
    elements clickable. I find it very confusing to see the cursor change to a pointer
    when nothing happens if I click.\n\nMartin: There is better browser support for
    the for + id attributes than for wrapping form controls in label elements. Explicitly
    associating form elements with their labels is also what is recommended by WCAG.'
  comment_date: '2006-08-02 20:09:28'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '0'
- comment_ID: '3537'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Roger Johansson: I had no idea Safari didn''t support that, I
    guess it should get a nice little javascript to do it instead? Good comment.'
  comment_date: '2006-08-03 01:13:55'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '1'
- comment_ID: '3540'
  comment_author: Martin Jansson
  comment_author_url: http://www.marja.se
  comment_content: '@Roger Johansson: Oops, for some reason I thought that browsers
    supporting labels would support labels wrapping the input-element, but i was wrong:
    Internet Explorer (of course) don''t. However, adding the <code>for</code>-attribute
    to the wrapping label fixes this in IE.\n\nI do not have access to a screenreader
    to test the support for this method, all I have is the Fangs-plugin to Firefox,
    which displays all three methods (label with for, wrapping label and wrapping
    label with for) the same way.\n\nIf anyone would like to try it out in a screenreader
    you can use <a href="http://marja.se/tests/labels-testcase.html" rel="nofollow">this
    small test case</a>'
  comment_date: '2006-08-03 10:48:58'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '0'
- comment_ID: '3575'
  comment_author: Johan
  comment_author_url: ''
  comment_content: 'label { cursor: pointer; }\n\nwhy not cursor: help and add a title
    attribute to the label tag\n\n'
  comment_date: '2006-08-04 19:28:05'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '0'
- comment_ID: '3765'
  comment_author: Adam Zakreski
  comment_author_url: ''
  comment_content: While we're being picky...  Last sentence of the last paragraph
    of "Split up your content".  Directory is speelt rong.\n\nGood article though!
  comment_date: '2006-08-11 22:00:54'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '0'
- comment_ID: '3822'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Adam: Good you like it! (fixed the spelling error too, thanks
    :)'
  comment_date: '2006-08-16 12:38:37'
  comment_post_ID: '85'
  comment_type: null
  is_admin: '1'
---