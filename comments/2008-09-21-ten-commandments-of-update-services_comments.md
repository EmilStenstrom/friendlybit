---
comments:
- comment_ID: '31039'
  comment_author: Rasmus Kaj
  comment_author_url: http://rasmus.krats.se/
  comment_content: The probelem is, of course, that there isn't an update service
    in windows that apps can hook in to.  And the reason for that is that, as far
    as I can see, there is no package system in windows!\n\nYou install a program,
    it just leaves its files all over your disk, and if you are lucky there is a specific
    program to uninstall the program -- and if you are really lucky, there might even
    be a specific program for updating related software.\n\nAnd here you are complaining
    about the fact that those updating systems, in the rare and good case where they
    exists, sucks ...
  comment_date: '2008-09-22 01:11:20'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31043'
  comment_author: Emil Hesslow
  comment_author_url: http://extensions.hesslow.se
  comment_content: 'You forgot Apple. Sending Safari as an update of Itunes and doing
    all kind of bad things. This is the latest: <a href="http://www.edbott.com/weblog/?p=2148"
    rel="nofollow">http://www.edbott.com/weblog/?p=2148</a>'
  comment_date: '2008-09-22 09:52:55'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31044'
  comment_author: Rotem
  comment_author_url: ''
  comment_content: 'I agree with most of your commandments, but some might be problematic:\n\n#2
    - If the app has to wait for the update check, the entire startup process is slowed
    down. My suggestion is to check on startup (and then periodically), but include
    "Remind me when I close the app" and/or "Remind me in x minutes" options. Then
    again, some security issues should be fixed ASAP (browsers, Flash, MS Office,
    etc.). This is why I can understand Microsoft''s restart nagging.\n\n#7 - There
    has to be a reason for having to close Firefox. Perhaps it was updating a Flash
    component and Firefox was using it? Still, with some effort they could probably
    create a method to tell browsers to stop using Flash while it''s updating. or
    something. Similar story with #9.\n\nBTW, about losing your tabs in Firefox, you
    can always restore the browsing session (I guess you need yet another extension
    to do it "the Mozilla way").'
  comment_date: '2008-09-22 09:56:16'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31045'
  comment_author: Chris
  comment_author_url: ''
  comment_content: You write like you're ready to switch to an OS with apt. (or any
    other OS with a modern package manager).
  comment_date: '2008-09-22 11:58:37'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31047'
  comment_author: James Socol
  comment_author_url: http://coffeeonthekeyboard.com/
  comment_content: 'Like Rotem said, the startup check would slow it down. Maybe a
    choice "Check for updates before starting" or "Check for updates before closing"
    or "neither."\n\nBut one other thing: 11. Roll sequential updates so I only need
    to download one. If I have version 1.0.0, and the current is 1.0.3, I shouldn''t
    need to download 1.0.1 and 1.0.2 separately. Hell, even if I have v1 and the current
    version is v3, there should be a single download.'
  comment_date: '2008-09-22 18:00:36'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31050'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Rasmus Kaj: I see what you mean, but apt-get isn''t much better
    than the ones I describe. An update service shouldn''t update stuff I don''t care
    about, most linux based update systems does that. So here I am, wanting to make
    stuff better :)\n\n@Rotem: #2: If you limit that to a single HTTP request to a
    certain URL, that shouldn''t take more than a second. If you only make that request
    once a week, few will even notice.\n\n#7: If there is a good reason, then I agree,
    please restart my browser. I fear that most often there isn''t a good reason.
    Lets say someone finds that closing Firefox prevents stopping some extension working
    properly. Is that I reason to require a restart? I think not, but update services
    seems to always assume that as soon as some tiny problem gets solved by restarting,
    lets do it.'
  comment_date: '2008-09-22 18:26:53'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '1'
- comment_ID: '31051'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Chris: Well, does apt get any of the ten points right?\n\n@James
    Socol: About startup time, see my previous answer. Point number 11, great addition,
    added to the list!'
  comment_date: '2008-09-22 18:29:14'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '1'
- comment_ID: '31052'
  comment_author: Exec
  comment_author_url: ''
  comment_content: Slow it down? It takes some part of a second for Firefox to check
    for updates for both itself and every extension installed... They should be able
    to trump that, shouldn't they? They could also limit it to once a day if you're
    afraid of having issues with startup time.\n\nWindows and boxes that regularly
    pop-up and get in the way just trains the user to close any similar things without
    giving it a second thought.
  comment_date: '2008-09-22 18:37:02'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31053'
  comment_author: Exec
  comment_author_url: ''
  comment_content: Woah, I write too slowly...\n\nAbout apt-get/aptitude/Synaptic
    (GUI "version")\n1. Not web based.\n2. N/A checks whenever you set it to check,
    or manually if you prefer that.\n3, 4. N/A\n5. Depends on the package but most
    often there's a lot of info and there usually are a list of buglinks.\n6. You
    can set it to install security updates, all updates or no updates automatically.\n7.
    Downloads and/or installs in the background, depending on your settings. (It does
    it in the background, but you can chose if you want to manually install what id
    downloads)\n8. I've only ever seen commercial apps do this without having a checkbox
    that is unchecked by default.\n9. From my experience only kernel updates and some
    driver updates (graphics card) require a restart. It also tells you when a specific
    program need to be restarted, after the installation is made.\n10. Well, it restarts
    the applications, so yeah...\n11. Afaik, it does that.\n\nThis is based on experience
    and not knowledge so there might be a few misconceptions of mine in there.
  comment_date: '2008-09-22 18:54:49'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31054'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@exec: The problem with your list above is that many of the options
    contain a "manually", "you choose", "your settings". I know this is the foundation
    of linux, letting people choose, but I don''t think you should have to choose
    how you update your program. I know I don''t want to. I want to use the damn program.\n\nAlso,
    from my experience of Ubuntu, it does not update by program, rather a large batch
    of updates for all your programs, with an icon in the taskbar which (naturally)
    says there''s updates all the time (since there are, I just don''t use telnet-SSL-config-kerbal-widget-gadget
    ever). \n\nThe Linux way is far from perfect (not saying that''s what you where
    implying).'
  comment_date: '2008-09-22 19:15:03'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '1'
- comment_ID: '31055'
  comment_author: Chris
  comment_author_url: ''
  comment_content: '@Emil:\nhuh ... let''s try:\n1. n/a\n2. n/a (update check is independent
    from program)\n3. yup.\n4. n/a (update check checks everything)\n5. yup.\n6. nope.\n7.
    yup.\n8. yup.\n9. yup. Only Kernel updates require restarts.\n10. n/a\n\nBy the
    way. One of the biggest annoyances at all are programs that steal focus. I really
    hate it (it''s great typing credentials in chat windows because chat client just
    finished starting. haha)'
  comment_date: '2008-09-22 19:39:04'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31057'
  comment_author: Adam Z
  comment_author_url: ''
  comment_content: It annoys me that some programs install updaters that now have
    to load at boot time, but as long as they're slow I can live with it.  I understand
    there's no standard API they can hook into.  But don't you dare slow down my boot
    time!\n\nNext, how bout you check for updates when the screensaver is running!
    I leave my work and home computer running 24 hours a day most of the time (not
    weekends).  It runs BOINC and other jobs during that time.  For the hours I'm
    using it, I want its undivided attention.  When I'm not using it, by all means
    go ahead and download and install (if I preauthorize it) the updates.\n\nDon't
    check when I'm starting my computer.  Don't check when I'm starting the app.  Don't
    check when I'm shutting things down.  Those are 3 times when I am guaranteed to
    be at my computer and am waiting for it to do something for me.  Don't interrupt
    it!\n\nLast point for me, if you're going to check for updates, ask me if I want
    to be notified every time.  I don't need an application to start up to say, "Checking
    for Updates", and then "No updates found".  If you didn't do anything, I don't
    care.
  comment_date: '2008-09-22 22:55:24'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31058'
  comment_author: Adam Z
  comment_author_url: ''
  comment_content: 'Edit: slow = small obviously'
  comment_date: '2008-09-22 22:57:12'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31059'
  comment_author: Robert Nyman
  comment_author_url: http://www.robertnyman.com
  comment_content: Bitches, eh? :-)\nNice rant, the updating procedures bug me to
    no end as well.
  comment_date: '2008-09-22 23:17:20'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31060'
  comment_author: Adam Z
  comment_author_url: ''
  comment_content: The worst part is that they don't have to!  It's just they were
    designed as an afterthought by the programmers and not by the people who actually
    use it.  I guess I'd have to ask, how many software companies do focus groups
    on their updating software, eh?
  comment_date: '2008-09-23 00:30:39'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
- comment_ID: '31061'
  comment_author: Diez mandamientos de los servicios de actualización
  comment_author_url: http://www.maestrosdelweb.com/actualidad/diez-mandamientos-de-los-servicios-de-actualizacion/
  comment_content: '[...] situaciones como la anterior es la que comentan en el recomendado
    post de Friendly Bit » Ten commandments of update services y propone lo que deberían
    ser los 10 mandamientos en servicios de actualización de [...]'
  comment_date: '2008-09-23 01:09:47'
  comment_post_ID: '239'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '31063'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Adam Z: Hehe, good point. They could really make updating programs
    transparent if they wanted. But hey, then your boss won''t see what you''re doing!
    Better make it in-your-face.\n\nThe problem with doing things when you''re not
    at the computer is that you get updates you don''t want. You get trapped in the
    "update everything" mentality that linux is in too. If you''re not using a program,
    there''s no need to update it. That''s why I think searching for updates once
    a week on startup wouldn''t be such a bad idea.'
  comment_date: '2008-09-23 07:42:16'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '1'
- comment_ID: '31064'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Emil Hesslow: Sorry for not replying until now, your comment
    stuck in the spam box, sorry! Yes, I forgot about Apple completely, they are annoying
    to the point that I''m starting to think I can live without quicktime altogether.'
  comment_date: '2008-09-24 07:46:34'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '1'
- comment_ID: '31066'
  comment_author: Los Diez Mandamientos de los servicios de actualización | Andrebills
  comment_author_url: http://www.andrebills.com/?p=1113
  comment_content: '[...] situaciones como la anterior es la que comentan en el recomendado
    post de Friendly Bit » Ten commandments of update services y propone lo que deberían
    ser los 10 mandamientos en servicios de actualización de [...]'
  comment_date: '2008-09-25 00:19:46'
  comment_post_ID: '239'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '31072'
  comment_author: Rasmus Kaj
  comment_author_url: http://rasmus.krats.se/
  comment_content: Updating everyting, when the updater is part of the OS and actually
    can update <em>everything</em> is way better than updating a single program.\n\nThe
    ubuntu updater checks once a day for updates of anything, rather than checking
    for updates of one specific program each time you start a program (I <em>really</em>
    wouldn't want anything to take half a second extra each time I run grep).  And
    id checks silently in the background, showing a non-intrusive icon if it finds
    anything to update.\n\nFor me, it finds something to update maybe one or two times
    a week.  I click "update it" when I'm not to busy with anything else.  Maybe once
    a month it tells me I must restart an app, but then I can keep using the app until
    it is convenient for me to restart (or close) it.  Same with reboots, only at
    an even lower frequency.\n\nActually, I find it hard to even imagine a better
    way to handle updates, apart from the enigmatic "don't put the bugs there to start
    with, so you won't have to fix them" ... :-)
  comment_date: '2008-09-26 23:55:20'
  comment_post_ID: '239'
  comment_type: null
  is_admin: '0'
---