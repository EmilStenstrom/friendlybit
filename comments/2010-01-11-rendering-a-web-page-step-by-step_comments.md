---
comments:
- comment_ID: '33347'
  comment_author: madr
  comment_author_url: http://madr.se
  comment_content: '13), sad but true ...\n\nFurther frustration:\n\nStylesheets are
    parsed as they turns up, and can create a flash of white screen when not placed
    in .\n\nThe same goes for scripts: it doesn''t wait until all other stuffs have
    been downloaded.\n\nScripts <strong>blocks</strong> pararell downloads (step 3-15)
    for all resources until it''s happy. That''s because people still use document.write
    these days. \n\nLovely!'
  comment_date: '2010-01-11 09:00:40'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33348'
  comment_author: Roland Bouman
  comment_author_url: http://rpbouman.blogspot.com/
  comment_content: 'Nice writeup! But I feel you did leave out a rather important
    point: browser cache lookup. And one step further: webserver proxies and their
    cache lookups.'
  comment_date: '2010-01-11 09:14:32'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33351'
  comment_author: Craig Buchek
  comment_author_url: http://craigbuchek.com
  comment_content: Pretty good, although I'd consider this to be a bit simplified.
    For example, step 5 requires 3 packets to be exchanged (the 3-way TCP handshake).
    Also, a lot of web sites have load balancers (or even multiple tiers of load balancers)
    or more server tiers. And there's a good chance that the client is behind a proxy
    server as well. And don't forget all the routers, switches, and firewalls also
    involved.
  comment_date: '2010-01-11 23:01:20'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33353'
  comment_author: Loon
  comment_author_url: ''
  comment_content: Was going to add steps, but this page was so slow... probably due
    to me looking at it from a proxy, routed from England and back. Proxy steps perhaps?
  comment_date: '2010-01-14 14:02:49'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33354'
  comment_author: Cody
  comment_author_url: http://www.webhostdesignpost.com
  comment_content: Dang I didn't realize there were so many steps to render a webpage.  Even
    if I stopped and thought about it, I wouldn't have know about all of these different
    steps it has to go through.  I guess we are spoiled, because most of the time
    it takes seconds to complete.
  comment_date: '2010-01-15 23:29:10'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33357'
  comment_author: Kristopher
  comment_author_url: http://www.shuttlebox.net
  comment_content: 'From a networking and transit perspective, there''s easily 10
    sub steps under #6.'
  comment_date: '2010-01-19 14:22:24'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33378'
  comment_author: Robin
  comment_author_url: http://robinjakobsson.se
  comment_content: This is bookmarked and printed for reference! Thanks for a great
    one :) !
  comment_date: '2010-01-25 10:47:33'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33409'
  comment_author: Pariloto
  comment_author_url: http://www.pariloto.net
  comment_content: I think that this is also a good guide for understanding how you
    can speed up a web site, by controling and optimizing some of the above steps.\n\nI
    think that a "correct" html combined with a good browser will get you happy as
    all the steps above will be made under the tenth of a second that you talked about.
  comment_date: '2010-02-05 08:05:16'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33441'
  comment_author: Case pariuri
  comment_author_url: ''
  comment_content: So true! And as a happy-end and pain-beginning, this is just the
    beginning - steps for arriving at you - after that it's the process of loading
    it! I guess there can be millions of processes loaded around this action!
  comment_date: '2010-02-11 21:44:44'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33453'
  comment_author: Markus
  comment_author_url: ''
  comment_content: Interesting stuff, I never thought about how many steps it goes
    through.
  comment_date: '2010-02-22 06:39:12'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33482'
  comment_author: Mac
  comment_author_url: http://www.macfilerecovery.net
  comment_content: Some of these steps could have been combined and the last one is
    not really a 'step'.
  comment_date: '2010-03-26 00:26:47'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33495'
  comment_author: Gkanell
  comment_author_url: http://www.hyperlinc.gr
  comment_content: Very nice article...thnx for sharing...
  comment_date: '2010-04-13 16:34:14'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33499'
  comment_author: Guillermo
  comment_author_url: ''
  comment_content: 'Wow! Try to figure all this stuff in the old (no so good) days
    of the /360 or VAX-11... \nBy the way, sometimes here in Montevideo, with mobile
    ADSL it seems that we are still in that era. That''s why I prefer information
    over spectacularity: ¡avoid heavy pages!\nGreat article, very helpful, ¡Gracias!
    \nGuillermo.'
  comment_date: '2010-04-23 02:21:43'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33510'
  comment_author: Siegfried
  comment_author_url: http://www.rorkvell.de
  comment_content: Nice, but not always true.\n\n1. Not all web pages are built out
    of a database. So you may skip this steps for all socalled static web pages. I
    think constructing static pages dynamically is nonsense. \n\n2. The page is rendered
    earlier. At least in modern browsers. As soon as the html is loaded and parsed,
    the page is rendered (while loading other resources like stylesheets). After loading
    the stylesheets the page is rendered again. And after loading each image the page
    is rendered again. And after loading and parsing the javascript the page is rendered
    again.
  comment_date: '2010-04-26 14:40:33'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33512'
  comment_author: R2J WebWorld
  comment_author_url: ''
  comment_content: Wow, this is such a super, long step taken for a split-second process!
    @ Mac, I think the last 2 weren't a step at all.
  comment_date: '2010-04-26 17:20:09'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33895'
  comment_author: jeffatrackaid
  comment_author_url: http://www.rackaid.com/
  comment_content: When you break down a HTTP request like this you can begin to see
    why a site may take a long time to load.  Consider a graphics laden site with
    dozens of images. This process has to repeat for every request.  Many browsers
    restrict the number of simultaneous downloads to a server, so even if the server
    and network is fast, the page may load slowly as it handles dozens of request.  Tools
    like YSlow and Page Speed (FireFox add-ons) can help you pinpoint problems in
    your site.  I see a lot of companies waste money on hardware upgrades when tweaking
    a page design to limit HTTP requests would have provided much greater bang for
    the buck.
  comment_date: '2010-06-01 19:50:25'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '33954'
  comment_author: Rodrigo Alves Vieira
  comment_author_url: ''
  comment_content: Thanks for the writing!
  comment_date: '2010-07-03 03:17:16'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '34050'
  comment_author: washburn
  comment_author_url: http://www.dreadnoughtguitar.net
  comment_content: Thank for slowing thing down for us. we surf the net every day
    not thinking about what is taking place in the background.\nwe have come a far
    way
  comment_date: '2010-09-01 18:43:46'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '34299'
  comment_author: moocr
  comment_author_url: http://moocr.com/
  comment_content: This is a very clear steps list from type a url to show a web page.\nI
    just develop a very simple blowser using java, it can not display any image or
    picture, it just show the links, hehe, I study the steps by this way!
  comment_date: '2010-11-02 03:27:58'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
- comment_ID: '36711'
  comment_author: Hasan Sheikh
  comment_author_url: ''
  comment_content: good one!
  comment_date: '2011-01-21 14:44:00'
  comment_post_ID: '580'
  comment_type: null
  is_admin: '0'
---