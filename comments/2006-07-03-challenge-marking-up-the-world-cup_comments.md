---
comments:
- comment_ID: '2836'
  comment_author: Christian Tietze
  comment_author_url: ''
  comment_content: Well, your question isn't that easy to answer. In fact, I'm not
    sure whether I can do something like that...\nTables, either they experienced
    markup or are viewn in plain text mode, they look ordered anyhow. And, well, it
    actually <em>is</em> some kind of tabular data, I think.\nLists would be semantically
    stronger (?) but have to be written in the wrong order. One would have to nest
    them, therefore the final round is at the very beginning and the "round of 16"
    is the deepest level of all available. That might be strange, but with ordered
    lists the meaning could be clarified a bit (curse FIFA for giving away a third
    place as well, because that doesn't fit well into the hierarchy).\nThe problem
    is the brackets. Final rounds have to be on the very right of the page so every
    new level has to be positioned farther left (relative to its parent). Inserting
    bracket image things makes my head smoke now. That's really a hard task! Maybe
    I can figure out something during the day :S
  comment_date: '2006-07-04 09:31:11'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '2839'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Christian: Good luck :)'
  comment_date: '2006-07-04 19:49:13'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '1'
- comment_ID: '2844'
  comment_author: Jesse Skinner
  comment_author_url: http://www.thefutureoftheweb.com/
  comment_content: I'm thinking a table with one row and a column for each round,
    then a definition list within each column. Each DT contains the date, time &amp;
    location, followed by 2 DDs, one for each team.\n\nTo actually format the thing,
    I think I'd highly recommend absolute or relative positioning.. or put a class
    on each round and try to set the padding, margins and backgrounds to line everything
    up okay, maybe even using em or % if you are very patient and talented.
  comment_date: '2006-07-05 10:00:49'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '2854'
  comment_author: Just-A-Lurker
  comment_author_url: ''
  comment_content: This is actually a pretty common type of data that the HTML spec
    doesn't seem to account for...  There is a ton of sports data, geneology, etc
    out there on the web.  Maybe we need to notify the w3c?
  comment_date: '2006-07-06 22:07:54'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '2855'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Just-A-Lurker: I don''t think so. HTML in its simplicity can
    be used to mark up a lot of complex things. You just need a little imagination.'
  comment_date: '2006-07-06 23:04:27'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '1'
- comment_ID: '2860'
  comment_author: exe
  comment_author_url: ''
  comment_content: Tried to make this by just using defintion lists, for fun.\nBut
    I couldn't find a way to get the round titles at the right position.\nSo I ended
    up with, basicly, the layout Jesse describes.\nRight now, the only problem is
    getting the matches evenly distributet vertically...\nAlso, of course, IE compatibility
    if one wants that.
  comment_date: '2006-07-07 16:19:05'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '2862'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: 'exe: keep on working, no one has posted their attempt yet, so
    I''m still waiting :)'
  comment_date: '2006-07-07 18:45:28'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '1'
- comment_ID: '2870'
  comment_author: exe
  comment_author_url: ''
  comment_content: Ok, I'm very new with this so there's probably some problems with
    the semantics.\nAnyway I made one basicly in the way Jesse describes it, but I
    didn't like it, too much scrolling, empty space and it got cluttered without CSS
    on, so I made a new one using only definition lists.\nI personally think that
    the new one is much easier to read and friendlier for small screens and the like
    and hopefully the markup makes more sense :)\n\nThe links\n<a href="http://phoenix.nox.googlepages.com/2006FIFAWoldCup_Bracket--DLtables.html"
    title="Definition Lists and Table version" rel="nofollow">dl+table</a>\n<a href="http://phoenix.nox.googlepages.com/2006FIFAWoldCup_Bracket--DL.html"
    title="Definition Lists Only Version" rel="nofollow">dl only</a>\n\n\nI will probably
    try and throw something better togheter, the dl+table one is just a try to make
    it look like the Wiki one. Which you hopefully noticed.
  comment_date: '2006-07-08 01:12:10'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '3061'
  comment_author: zcorpan
  comment_author_url: ''
  comment_content: <a href="http://simon.html5.org/sandbox/html/fifa" rel="nofollow">Nested
    tables</a>, anyone? This is the first time I see a valid use case for nesting
    tables.\n\nMy reasoning is simple. The overall structure is best marked up using
    a table, because it has columns and headers for each column. Then rowspan can
    be used to achieve the "tree" relation.\n\nThe inner tables are tables because
    they have a caption. They could even have column headers as well ("Country", "Results"),
    but that would be too verbose.\n\nThe Third place table is a bit tricky. Structurally,
    it has the same "parents" as Final, but there are only so many dimensions a table
    can have. (I've thought about the axis attribute, but I'm not sure how it helps.)\n\nI've
    only addressed one problem here. I'll hand over the styling to someone else.
  comment_date: '2006-07-14 01:13:25'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '3066'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@exe: That, my friend, is a damn good example. Well done! I''m
    not fully sure about the table there, just because it has headers doesn''t mean
    a table is needed right? None the less, I''m really impressed, thanks!\n\n@zcorpan:
    Interesting idea! Certainly makes styling easy, does it? ;) I''m not fully sure
    about representing a match as a table but I guess it could be thought of as having
    a "team" and "score" header like you say. Well done!\n\nI''ll try to wrap something
    up later tonight and post about it.'
  comment_date: '2006-07-14 07:12:57'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '1'
- comment_ID: '3068'
  comment_author: exe
  comment_author_url: ''
  comment_content: Thanks :), though mostly it's based on what Jesse said.Well, I
    wasn't too sure about the tables myself, not even so sure about the rest either,
    but I couldn't think of any other markup that would allow me to style it like
    the Wiki version, without restricting scaleability.Maybe left floated or inline
    headers, followed by 4 floated lists with definition lists in them could work
    too?\nI've updated the pages a bit so it should render more nicely in IE now,
    probably
  comment_date: '2006-07-15 10:06:13'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '3078'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: Ok, I finally got the time to sit down and play with this :)\n\nHere's
    my <a href="/files/worldcup/worldcup_bracket.html" rel="nofollow">world cup bracket</a>
    markup and CSS suggestion. \n\nI focused on the tree-like relationships of the
    data instead of the "vertical" relationship of "matches belonging to semi-finals"
    like the examples above did. Which one you want to use it up to you.
  comment_date: '2006-07-16 23:00:18'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '1'
- comment_ID: '3083'
  comment_author: Ben Millard
  comment_author_url: http://sitesurgeon.co.uk/
  comment_content: I've created an <a href="http://sitesurgeon.co.uk/!dev/fifa2006/ben-millard.html"
    rel="nofollow">unlayered, regular <code>&lt;table&gt;</code> version</a>.\n\nThis
    approach places each match on its own row, with columns for the properties of
    each match.\n\nEach stage is grouped into a &lt;tbody&gt; with a row heading that
    spans all the rows in that stage.\n\nThe matches are ordered by the time and date
    they were played on, like a timetable.\n\nThe <code>scope</code> attribute is
    used on heading cells to make their relationships clearer to software.\n\nI think
    some of the other attempts may have been a bit too interested in how the result
    looks in their browser and creating weird markup to make it look right?\n\nEmil,
    your list example is interesting...like a reversed-chronological heirarchy. It
    is difficult to understand without the CSS, although it looks nice with it. c{:¬)\n\n(A
    preview button would be very helpful!)
  comment_date: '2006-07-17 05:49:39'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '3127'
  comment_author: Haralan Dobrev
  comment_author_url: ''
  comment_content: That site that you have made about the worldcup is very good as
    the ingo and the statistics.But the visitors of your site want design.Real design.They
    can find the statistics about WC 2006 anywhere in web sites with a good design.
    So give the customers what they want - design.
  comment_date: '2006-07-18 21:19:55'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '3143'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Haralan Dobrev: this article is not about design, only the code
    behind :) But sure, for these solutions to be worth anything in the real world
    you need a good design.'
  comment_date: '2006-07-19 01:59:39'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '1'
- comment_ID: '3213'
  comment_author: Joachim
  comment_author_url: ''
  comment_content: I follow this discussion from the beginning. Al ideas so far so
    good, but what about the "lines" or "connections" between the single data’s as
    on the original site? I think position of data is not the problem, more the "absolute
    original layout", you know what I mean? Greetings from Amsterdam
  comment_date: '2006-07-21 22:53:24'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '0'
- comment_ID: '3215'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Joachim: I would say that''s design. I could have added that
    to my example with a background image, but it would be a mess to position :)'
  comment_date: '2006-07-22 00:24:15'
  comment_post_ID: '75'
  comment_type: null
  is_admin: '1'
---