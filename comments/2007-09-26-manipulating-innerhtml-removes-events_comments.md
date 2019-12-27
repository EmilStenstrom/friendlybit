---
comments:
- comment_ID: '27862'
  comment_author: Nate Klaiber
  comment_author_url: http://www.nateklaiber.com
  comment_content: thats why you avoid using innerHTML :)\n\nJust kidding. Do you
    have the same results if you were to try appending via the DOM instead of innerHTML?
  comment_date: '2007-09-27 02:48:56'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '27867'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Nate: No, using DOM methods instead keeps the events as they
    should be. That''s one workaround. The other one is to attach events <strong>after</strong>
    using  innerHTML.'
  comment_date: '2007-09-27 08:49:13'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '1'
- comment_ID: '27869'
  comment_author: Freddy
  comment_author_url: ''
  comment_content: I'll have to call 'duh' on that one. Obviously, events on an element
    cannot be retained if the element is replaced by a completely different string
    using innerHTML. You basically throw away that part of the DOM and write it new.
    Don't have to tell you that.\n\nThe only thing slightly noteworthy is that this
    also applies when using the + unary operator ("+="). And given that it is required
    to call GetValue() and return the sum, which is in turn written back as a whole,
    it is not very surprising.
  comment_date: '2007-09-27 11:55:00'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '27870'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Freddy: Good that you found it obvious, I just had to think for
    a while before it came to me. I thought I might save someone''s time by stating
    it, but deeming by your tone I might have been wrong about that.\n\nAs you said,
    the confusing part here is that adding to and replacing innerHTML is the same.
    \n\nThanks for commenting.'
  comment_date: '2007-09-27 14:11:20'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '1'
- comment_ID: '27871'
  comment_author: Freddy
  comment_author_url: ''
  comment_content: '@Emil: I didn''t want to sound elitist, sorry if it came across
    as such. JFTR: In JavaScript, there is no "adding to" strings; Adding using the
    unary + ("+=") is just a "shorthand" for reading, adding, and reassigning values
    (internally, they convert number/string types, but that''s not relevant in this
    context).'
  comment_date: '2007-09-27 14:17:25'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '27876'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Freddy: Ah, thanks. It makes even more sense then.'
  comment_date: '2007-09-27 17:19:20'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '1'
- comment_ID: '27878'
  comment_author: Johan Lind
  comment_author_url: ''
  comment_content: Hmm, nothing happens when I click on any of those elements in Safari
    and Camino.\nIs this an IE only thing?
  comment_date: '2007-09-27 17:44:38'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '27879'
  comment_author: Kalle Persson
  comment_author_url: http://nemus.se
  comment_content: Nice, I did not know this.\n\nJohan Lind:\nLook at the source of
    the example page, the JavaScript isn't <em>supposed to</em> do anything when you
    click the span, because of the innerHTML change.
  comment_date: '2007-09-27 18:38:51'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '27881'
  comment_author: Jose Carrero
  comment_author_url: ''
  comment_content: Maybe i'm missing something but why add the onClick event using
    span.onclick=function()?, if you put the "onClick" inside the HTML tag it works
    fine even after the innerHTML change
  comment_date: '2007-09-27 19:13:10'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '27924'
  comment_author: Ara Pehlivanian
  comment_author_url: http://arapehlivanian.com/
  comment_content: Yeah, I came across this problem when writing an Ajax driven playlist
    for a project here at work. I was adding the new contents to the DOM with innerHTML
    and had to rebind all of the events for the entire list every time. Using DOM
    methods though will avoid this problem.
  comment_date: '2007-09-28 14:54:30'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '27925'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: Freddy,\n\nThanks for explaining that! It threw us off for a while,
    so we just needed to think in alternate terms. In this case it was an AJAX call
    that could return any kind of HTML code, so using proper DOM methods wasn't a
    viable option.
  comment_date: '2007-09-28 14:59:47'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '27958'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Jose Carrero: Many believe (including me) that adding things
    inline in the code like that is littering. You attach behaviour into the structure
    of the document. JS files should add their events from an external file, with
    onclick or something fancier.'
  comment_date: '2007-09-28 20:55:56'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '1'
- comment_ID: '28159'
  comment_author: Anders Ringqvist
  comment_author_url: ''
  comment_content: A viable soultion could be to use event delegation instead of ”classic”
    event handling.\n\nI let Christian Heilmann speak:\n\nhttp://icant.co.uk/sandbox/eventdelegation/
  comment_date: '2007-10-03 14:22:01'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '28178'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Anders Ringqvist: Very interesting technique, thanks for linking!
    If I understand it correctly it''s simply setting a listener on the outermost
    element, and waiting for the event to bubble there. Good way to avoid this problem.'
  comment_date: '2007-10-04 21:19:34'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '1'
- comment_ID: '30057'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: Another way around this problem is to create your own appendHTML()
    method like so:\n\nHTMLElement.prototype.appendHTML = function(s) {\n  var div
    = document.createElement('div');\n  div.innerHTML = s;\n  while (div.firstChild)\n    this.appendChild(div.firstChild);\n}\n\nThis
    does what you thought "innerHTML +=" did (except that script blocks inserted this
    way will be executed).
  comment_date: '2008-01-02 00:01:44'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '34331'
  comment_author: wongkachun
  comment_author_url: ''
  comment_content: Dear all,\n\nI try to use div instead of span on the above coding.\nThe
    result is that the event of div is kept while span's is "killed".\n\nkachun
  comment_date: '2010-11-10 05:08:04'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
- comment_ID: '34332'
  comment_author: wongkachun
  comment_author_url: ''
  comment_content: Dear All,\n\nIn conclusion, the innerHTML, DOM and html methods
    are used in following codes to show the event differences:\n\n\n\n\nevents of
    innerHtml and DOM dynamic html\n\n\n    function changeinnerhtml(_id)\n    {\n        var
    obj = document.getElementById(_id);\n        obj.onclick = function(){alert(_id
    + ' is clicked!')};\n        var objparent = document.getElementById('para1');\n        objparent.innerHTML
    += ' <a href="http://yahoo.com.hk" rel="nofollow">YAHOO click me!</a>';    \n    }\n    function
    changedom(_id)\n    {\n        var obj = document.getElementById(_id);\n        obj.onclick
    = function(){alert(_id + ' is clicked!')};\n        var objparent = document.getElementById('para1');\n        var
    objnew = document.createElement('a');\n        objnew.setAttribute("href","http://google.com.hk");\n        objnew.appendChild(document.createTextNode("GOOGLE
    click me!"));\n        obj.appendChild(objnew);        \n    }\n\n\n\n\n\nCompare
    about event handlers of innerHTML, DOM and static html\ninnerHTML here\nDOM here\nhard
    coded html here\n\n(1)When you click "innerHTML here", no alert because parent
    tag (&amp;lt p &amp;gt) changed by innerHTML destroys the event.\n(2)When you
    click "DOM here", alert prompts dom tree is built within parent tag (&amp;lt p
    &amp;gt).\n(3)When you click "hard coded html here", alert should prompt because
    no structure changing within parent tag (&amp;lt p &amp;gt).\n    \n    changeinnerhtml('span1');\n    changedom('span2');\n\n\n\n\n\nRegards,\nwongkachun
  comment_date: '2010-11-10 06:13:49'
  comment_post_ID: '137'
  comment_type: null
  is_admin: '0'
---