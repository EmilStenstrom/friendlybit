---
comments:
- comment_ID: '4299'
  comment_author: matthijs
  comment_author_url: ''
  comment_content: Cool. Thanks for the write-up. Imagine can be frustrating to deal
    with this one if you don't know a solution yet. \n\nSo, besides this one, have
    you encountered other problems in container-divless layouts?  I always used a
    container div because of the IE5 problems, but since it's time to leave that one
    behind I might go divless as well.
  comment_date: '2006-09-05 09:31:11'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '4310'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@matthijs: Nope, no other problems. I sometimes use both html
    and body and add background images and widths to both, and even that can work
    well. I recently wrote a writup on the <a href="http://friendlybit.com/css/kth-goes-web-standards/"
    rel="nofollow">KTH website</a>. That one uses styling on both html and body. Thanks
    for your comment!'
  comment_date: '2006-09-05 20:06:07'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '1'
- comment_ID: '4329'
  comment_author: Matthijs
  comment_author_url: ''
  comment_content: Thanks for your answer Emil. I'l be using the wrap-divless technique
    in a redisign in which I cannot change the html. Using the body will save me from
    having to place the rules on lots of other elements.
  comment_date: '2006-09-06 09:06:46'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '4346'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: THANK YOU! Currently I'm doing work for a client where I've encountered
    this exact problem! Tomorrow, first thing I'll do is test your solution!
  comment_date: '2006-09-06 20:21:19'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '4349'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: 'Hmm, come to think of, most likely it won''t solve my specific
    problem...\n\nI''m using it to create <a href="http://www.imaputz.com/cssStuff/bigFourVersion.html"
    rel="nofollow">a CSS Scrollable Table with Fixed Header</a> and there I have it
    to emulate a fixed positioning.\n\nWhen I add <code>position: relative;</code>
    to any of the parent elements to the one that acts fixed, the bug goes away (i.e.
    it doesn''t have to be the <code>body</code> element) but then I also lose the
    the effect of a fixed header...'
  comment_date: '2006-09-06 21:44:05'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '4367'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Robert Nyman: Setting it to a parent element made that element
    become "fixed until reload" in my examples. I''m afraid I  don''t have any experience
    from the fixed thead example you link to, all I know is that IE is very bad at
    redesigning table elements.'
  comment_date: '2006-09-07 06:50:44'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '1'
- comment_ID: '4383'
  comment_author: stefano
  comment_author_url: http://www.smolinari.com
  comment_content: I have to thank you because I also got crazy with this but was
    not able to find out the bug. Great! \nSte
  comment_date: '2006-09-07 16:18:53'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '4551'
  comment_author: Paula
  comment_author_url: ''
  comment_content: This bug is not only IE6.\n\nI use IE7 BETA 2, and I had this problem.
  comment_date: '2006-09-11 21:39:18'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '4555'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Paula: very interesting, seems like this fix was needed after
    all.'
  comment_date: '2006-09-11 22:14:32'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '1'
- comment_ID: '4589'
  comment_author: Paula
  comment_author_url: ''
  comment_content: 'it lacked to say: this same error in the IE7 BETA 2, is corrected
    with position: relative in body.\n=D'
  comment_date: '2006-09-12 15:44:53'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '4702'
  comment_author: Lightbox feature added to JaS - JavaScript Slides - Robert&#8217;s
    talk
  comment_author_url: http://www.robertnyman.com/2006/09/15/lightbox-feature-added-to-jas-javascript-slides/
  comment_content: '[...] The position: relative is applied to the body element to
    get rid of the unexpected position: fixed effect in IE when setting position:
    relative to an element within a floated element. For more info, read Emil&#8217;s
    IE6 resize bug (position: relative becomes fixed). [...]'
  comment_date: '2006-09-15 15:09:26'
  comment_post_ID: '91'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '5169'
  comment_author: Roger Johansson
  comment_author_url: http://www.456bereastreet.com
  comment_content: The bug is still there in IE 7 RC1, so don't expect it to go away
    any time soon. Grr.
  comment_date: '2006-09-26 08:33:46'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '5824'
  comment_author: Kane
  comment_author_url: ''
  comment_content: Thanks! It was very useful. Just discovered this bug and spent
    30 mins trying to solve it, but accidentally found your site!
  comment_date: '2006-10-19 17:46:04'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '5831'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Roger: Damn (but good for this article :) I guess it will be
    valid a while longer.\n\n@Kane: Good to know you found it useful :)'
  comment_date: '2006-10-19 21:24:09'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '1'
- comment_ID: '8155'
  comment_author: Brian
  comment_author_url: http://briankramp.spaces.live.com
  comment_content: I ran into this problem as well, but putting position:relative
    on the body tag didn't fix it for me.\n\nI think it is because I had a table and
    table cell with align=center on the page.  After I put position:relative on the
    element inside the centered table cell, it worked.\n\nThanks for pointing me in
    the right direction.
  comment_date: '2006-12-01 00:36:05'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '8419'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Brian: Yeah, I''ve noticed that too, this does not work for all
    cases. You shouldn''t use the align attribute though, it''s design and should
    be in the CSS (text-align: center).'
  comment_date: '2006-12-04 20:14:09'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '1'
- comment_ID: '22799'
  comment_author: Ido Tzang
  comment_author_url: ''
  comment_content: I was so happy to find this post - i have that same exact problem...
    only thing is - your patch didn't solve the problem for me.\nDo happen to have
    any other helpful ideas / directions ?\n10x,\nIdo
  comment_date: '2007-03-28 20:53:10'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '23042'
  comment_author: SAM0077
  comment_author_url: ''
  comment_content: 'Thank you Emil for the fix. I tried it and I am having trouble
    with it.  Is there anything else than positon: relative; to add to the CSS body?'
  comment_date: '2007-04-04 03:20:16'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '23086'
  comment_author: Stuart Radley
  comment_author_url: ''
  comment_content: Wow, I actually developed a technique for NOT using position relative
    because of this problem - although it caused great frustration. I was amazed that
    this works perfectly in IE7 (don't have 6 to hand). I can't wait to start using
    this again! Thanks!
  comment_date: '2007-04-05 14:19:49'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '23565'
  comment_author: Phil
  comment_author_url: http://philipmanser.com
  comment_content: Thanks! Really helpful.
  comment_date: '2007-04-20 16:43:04'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '24616'
  comment_author: Terry McGuire
  comment_author_url: ''
  comment_content: You rock!\n\nThis saved me such a headache:\nie6-resize-bug\n\nThank
    you.
  comment_date: '2007-05-25 11:41:00'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '24882'
  comment_author: James
  comment_author_url: ''
  comment_content: OMG! Thank you so much, this was driving me insane!!!!!! easy fix
    indeed!
  comment_date: '2007-06-02 03:37:32'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '26076'
  comment_author: thomas
  comment_author_url: ''
  comment_content: Thank you for this blogentry, it was extremely helpful for me!\n\ncheers
  comment_date: '2007-07-12 19:44:56'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '27449'
  comment_author: Vibhore
  comment_author_url: http://www.cocubes.com
  comment_content: Thanks a lot for the tip, i just wasted 5 hrs fixing it and i am
    sure i would have never tried this fix on my own!!!
  comment_date: '2007-09-17 23:45:10'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '28369'
  comment_author: Peter
  comment_author_url: ''
  comment_content: Appreciate your sharing the fix. I was pretty freaked out when
    I just discovered this bug, but thankfully Google led me to your page. Thanks
    again!
  comment_date: '2007-10-16 22:35:24'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '28750'
  comment_author: Peter Morris
  comment_author_url: ''
  comment_content: Thanks very much! Such an easy fix! Wish I'd read your blog before
    tearing the remainder of my hair out!
  comment_date: '2007-10-29 12:30:11'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '29368'
  comment_author: tim
  comment_author_url: ''
  comment_content: you are a savior, this has been bugging me for months!
  comment_date: '2007-11-22 05:47:10'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30140'
  comment_author: sciontphono
  comment_author_url: ''
  comment_content: Really good...I was getting crazy trying to solve this bug...THANKS!
  comment_date: '2008-01-17 17:16:53'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30346'
  comment_author: Rodrigo
  comment_author_url: ''
  comment_content: Thanks.. your post and examples helped me a lot!!
  comment_date: '2008-02-26 14:37:04'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30487'
  comment_author: anonymous
  comment_author_url: ''
  comment_content: Awesome! Thanks for the post.  But looks like you need it for your
    website itself.  I resized the window on this article and it was not snapping
    into place... tsk tsk.
  comment_date: '2008-03-25 15:18:13'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30520'
  comment_author: Nilesh Ashra
  comment_author_url: http://migrantroo.com
  comment_content: Hi dude,\n\nThis page was first hit on google when searching for
    "ie6 position resize" and fixed my problem instantly - thanks a lot :)
  comment_date: '2008-04-01 21:39:09'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30534'
  comment_author: Cas
  comment_author_url: http://absolutemg.com
  comment_content: This bug was driving me nuts until I found your fix - and as an
    aside - I found this bug was in effect in IE 7 as well (but my page rendered fine
    in Firefox and Safari, which was what had me stumped). THANK YOU.
  comment_date: '2008-04-08 16:55:33'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30535'
  comment_author: 'IE6 resize bug position: relative becomes fixed | Absolute Blog'
  comment_author_url: http://www.absolutemg.com/blog/?p=32
  comment_content: '[...] IE6 resize bug position: relative becomes fixed - Friendly
    Bit [...]'
  comment_date: '2008-04-08 17:22:56'
  comment_post_ID: '91'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '30554'
  comment_author: Jay
  comment_author_url: ''
  comment_content: You're my hero of the hour! I was going nuts wondering why it was
    doing that in IE for a site I'm developing. I found this article after Googling
    the problem - tried the solution, and it works. I hate IE, but without it I'd
    bill a lot less hours when developing a site.
  comment_date: '2008-04-23 04:27:58'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30555'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: Hi all, cool to see that you like my little fix :)
  comment_date: '2008-04-23 22:57:08'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '1'
- comment_ID: '30572'
  comment_author: kev
  comment_author_url: ''
  comment_content: This is just what I have been looking for as part of a multiple
    solution to an IE and Firefox bug.  I  am toggling between two divs that both
    contain different text.  The first fix was to make sure that position:relative
    was put into the text layers so that they would inherit their proper z-index from
    their position in the code.  The second fix is this one described on this page,
    so that those relatively positioned divs will move correctly on page resize for
    both IE and Firefox.  Thanks all.
  comment_date: '2008-05-07 18:52:18'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30623'
  comment_author: gaurav
  comment_author_url: ''
  comment_content: Thanks for the article. I was facing the same concern on one of
    the web pages I am working on right now. Since I am from Java/J2EE background,
    I don't work on CSS so much. \n\nThanks again.
  comment_date: '2008-05-22 18:35:52'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30677'
  comment_author: Michael
  comment_author_url: ''
  comment_content: Thank you so much, friend! This has been driving me nuts for two
    days now. Your solution fixed EVERYTHING. You so rock!
  comment_date: '2008-05-31 00:57:07'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30800'
  comment_author: lyndonaus
  comment_author_url: ''
  comment_content: You have restored a 68yr old man's faith in human nature with your
    generosity in sharing this fix!!!
  comment_date: '2008-07-08 05:52:40'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30852'
  comment_author: Nathaniel B
  comment_author_url: ''
  comment_content: <b>Many thanks for this fix!</b> I was wondering what was going
    on!
  comment_date: '2008-07-21 14:58:43'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30856'
  comment_author: James
  comment_author_url: ''
  comment_content: Thanks so much!!! This was so frustrating.
  comment_date: '2008-07-24 15:22:44'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30858'
  comment_author: Lucy
  comment_author_url: ''
  comment_content: Thank you!  I was puzzled by that ...
  comment_date: '2008-07-25 13:30:47'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '30871'
  comment_author: Jon
  comment_author_url: http://www.udmercy.edu
  comment_content: Thanks Emil!  Interestingly, this bug was more a problem for me
    in IE7 than IE6 (I have all kinds of position values going on).  You helped me
    end my day on a high note!!  Thanks again.  \n\nJon
  comment_date: '2008-08-06 21:40:03'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31065'
  comment_author: Emanuele Ciriachi
  comment_author_url: http://www.espares.co.uk
  comment_content: You sir, just spared me a lot of trouble. Our website will hopefully
    be updated tomorrow without this problem, if you hurry you can still see it today
    (shows up in the "Featured Products" section).
  comment_date: '2008-09-24 14:38:38'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31086'
  comment_author: senen
  comment_author_url: ''
  comment_content: Was going crazy trying to fix the problem, im using so much time
    just for trying to keep the same look on ie as on all the other browsers. hate
    ie. thx alot for the help
  comment_date: '2008-10-04 18:43:36'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31096'
  comment_author: volomike
  comment_author_url: http://volomike.com
  comment_content: Emil. You the man -- even 2 years after posting this article. Had
    a client project and this came up. Was baffling and only occurred with IE-type
    browsers. Opera, Safari, FF -- they all worked fine. It's sad that even IE7 final
    version has this glaring bug. And I'm sure that bug report will fall on deaf ears
    at Microsoft. Your fix set me straight.
  comment_date: '2008-10-12 08:53:08'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31097'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: Thanks everyone! Nice to see that my silly articles help people
    :)
  comment_date: '2008-10-12 11:46:59'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '1'
- comment_ID: '31120'
  comment_author: Aaron
  comment_author_url: ''
  comment_content: I just spent the last day and half trying to squash this bug. Thanks
    for posting about it. My frustration level just dropped a bunch.
  comment_date: '2008-10-22 19:30:34'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31307'
  comment_author: Smitty
  comment_author_url: http://smittyology.com
  comment_content: You are the freaking man. I've been having issues with a very important
    client and this helped out so much. I knew it was the relative positioning but
    I didn't know the fix. Thanks for NOT keeping that to yourself.
  comment_date: '2008-12-11 00:05:00'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31309'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Aaron, Smitty: Thanks for taking the time to thank me! :) I was
    in your exact position and was force to reverse-engineer a fix. I thought I might
    as well post it here.'
  comment_date: '2008-12-11 00:46:16'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '1'
- comment_ID: '31383'
  comment_author: Devin
  comment_author_url: ''
  comment_content: Thanks for the post.  I ended up having to use absolute positioning
    to get my div in the right place- but I appreciate the info.
  comment_date: '2009-01-23 22:40:37'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31405'
  comment_author: Roman
  comment_author_url: http://xbcms.com
  comment_content: Thank you very much for your research and post! It seems to work.
  comment_date: '2009-01-28 19:45:17'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31412'
  comment_author: Leonardo A. Souza
  comment_author_url: http://www.mundi.com.br/
  comment_content: Thank you! Thank you! Thank you! Thank you a lot! You save the
    time (and the live) for a desperate brazilian developer!
  comment_date: '2009-01-30 20:53:20'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31436'
  comment_author: jason
  comment_author_url: ''
  comment_content: DUDE. i have been freaking out with this pathetic ie6 bug for so
    long now...bashing my head against a mined spiked poisoned wall for ages trying
    to understand why setting position to relative or absolute was behaving as fixed
    in my scrollable div.\n\nthe solution was simply to set the containing element
    to position:relative. so simple yet impossible to guess. \n\nthanks man. you've
    really saved my life as i was about to go jump in front of a semi-truck just to
    finally achieve peace of mind.
  comment_date: '2009-02-03 01:38:21'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31606'
  comment_author: Farzan
  comment_author_url: ''
  comment_content: Thank you, thank you, thank you.\n\nThis hack saved my neck...
    my customer was killing me and I didn't know how I could fix it.
  comment_date: '2009-03-07 00:12:44'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31686'
  comment_author: wingMan
  comment_author_url: ''
  comment_content: Thanks for posting Bro!\n\nThis has been driving me nuts for the
    last month.
  comment_date: '2009-04-05 04:48:23'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31727'
  comment_author: PavelGee
  comment_author_url: ''
  comment_content: Thanks so much! Being a non-professional, and facing so many bugs
    in IE at the onset of the project left me desperate at times.\nLucky I came across
    your page!
  comment_date: '2009-04-30 18:58:34'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '31793'
  comment_author: Juan Araya
  comment_author_url: http://juanaraya.pip.verisignlabs.com/
  comment_content: Emil !!!\n\nTHANK YOU! THANK YOU!! THANK YOU!!!!\n\nHad noticed
    this issue in some websites but was not aware I was a victim of it. A client just
    sent me an email complaining about this.\n\nThanks again for your excellent documentation.
  comment_date: '2009-06-18 06:09:08'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '32149'
  comment_author: Clinton Montague
  comment_author_url: http://slightlymore.co.uk
  comment_content: Thanks for posting the answer to this problem, it would have caused
    a lot of brain-ache if I didn't stumble across this post. I'll be writing a post
    about this problem in the near future linking back here :)\n\nThanks again
  comment_date: '2009-07-06 14:47:14'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '33031'
  comment_author: Sam
  comment_author_url: ''
  comment_content: Thanks very much for posting this -- so simple to fix, but so very
    frustrating if you don't know how!  I can't understand how an operation the size
    of Microsoft can still put out a product that fails to meet basic standards.  mindblowing.  Cheers!
  comment_date: '2009-09-23 13:44:13'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '33096'
  comment_author: anonymous
  comment_author_url: ''
  comment_content: All these bugs are a pain in the bum!\nit's good to be informed
    about them.
  comment_date: '2009-10-03 12:57:23'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '33110'
  comment_author: Wolf Oliver Abbas
  comment_author_url: ''
  comment_content: I can not believe it. Your post is three years old and the bug
    is still not fixed. I got the very same problem. Thank you for the solution!
  comment_date: '2009-10-09 09:52:50'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '33350'
  comment_author: Michael
  comment_author_url: ''
  comment_content: 'BEWARE: this fix may have side affects to existing sites! My site
    wasn''t able to show thickbox popups any more in IE6, after I had added position:relative
    to the body element. So it is''t the solution for me... :('
  comment_date: '2010-01-11 15:21:48'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '33399'
  comment_author: IE6???????IE6? 25+ Bugs(?) &laquo; ?????(We are UEDs,??????????????)
  comment_author_url: http://www.beiju123.cn/blog/?p=208
  comment_content: '[...] ??body???????IE????????????body?????????????????Emil Stenström???IE6
    Resize Bug??????????body??position:relative;?????????~ [...]'
  comment_date: '2010-02-03 09:03:58'
  comment_post_ID: '91'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33411'
  comment_author: Jasper
  comment_author_url: http://jspr.tndy.me
  comment_content: '@Michael, just use a container div instead of body, then it''ll
    work.'
  comment_date: '2010-02-05 17:12:17'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '33886'
  comment_author: daniel
  comment_author_url: ''
  comment_content: Very useful to me also, thank you very much!!!!
  comment_date: '2010-05-26 19:26:39'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '33897'
  comment_author: Anurag Dwivedi
  comment_author_url: ''
  comment_content: Thanks for you effort to help. \nBut it did not work out for me.  \n\nHowever,
    I got a solution by giving a fixed width (in px) to the parent div of problematic
    (those moving with resize) elements.
  comment_date: '2010-06-02 13:22:45'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '33920'
  comment_author: Millarian | IE7 resize window problem
  comment_author_url: http://millarian.com/programming/ie7-resize-window-problem/
  comment_content: '[...] with these clues, I was able to find a post by Emil Stenström
    that documented the existence of this bug in IE6 and IE7 beta 2. He has a great
    explanation about [...]'
  comment_date: '2010-06-14 18:35:02'
  comment_post_ID: '91'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '33929'
  comment_author: fireguns.net&raquo; Blog Archive &raquo; [?][?]IE6???????IE6? 25+
    Bugs
  comment_author_url: http://www.fireguns.net/?p=3
  comment_content: '[...] ??body???????IE????????????body?????????????????Emil Stenström???IE6
    Resize Bug??????????body??position:relative;?????????~ [...]'
  comment_date: '2010-06-18 10:11:21'
  comment_post_ID: '91'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '34155'
  comment_author: bob
  comment_author_url: ''
  comment_content: THANK YOU. Driving me insane - have not dealt with IE6 in years.
  comment_date: '2010-10-16 01:18:55'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
- comment_ID: '36746'
  comment_author: Francesco Spreafico
  comment_author_url: http://twitter.com/Laz75
  comment_content: I seriously love you. Just lost an hour after this bug... I'd never
    stumbled into it before! Thank you a lot!
  comment_date: '2011-02-15 09:00:00'
  comment_post_ID: '91'
  comment_type: null
  is_admin: '0'
---