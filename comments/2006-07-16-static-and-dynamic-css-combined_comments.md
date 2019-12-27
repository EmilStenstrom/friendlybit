---
comments:
- comment_ID: '3073'
  comment_author: Fredrik Wärnsberg
  comment_author_url: http://warnis.com
  comment_content: I'm not sure since I havent tested this at all, but would only
    echoing one line (@import) really be that much faster than echoing out all rules
    to the css-file, or am I missing something here?
  comment_date: '2006-07-16 19:44:11'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '0'
- comment_ID: '3080'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Fredrik Wärnsberg: compare echoing out 1000 lines of CSS each
    time versus echoing out 20 lines where each line references a static CSS file.\n\nFor
    small sites this wouldn\''t matter, for bigger I think it would.'
  comment_date: '2006-07-16 23:25:07'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '1'
- comment_ID: '3081'
  comment_author: r21vp
  comment_author_url: http://r21vo.id.lv
  comment_content: I guess it would be even easier to use style tag in document header
    instead (containing generated @import references). This way we can save one webserver
    request.
  comment_date: '2006-07-16 23:46:00'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '0'
- comment_ID: '3082'
  comment_author: Fredrik Wärnsberg
  comment_author_url: http://warnis.com
  comment_content: '@Emil then perhaps readfile() would be an even better option?
    I''m not positive though - some testing might  be in place.'
  comment_date: '2006-07-17 01:40:16'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '0'
- comment_ID: '3090'
  comment_author: Phill Sparks
  comment_author_url: ''
  comment_content: '@Fredrik: The point is to allow the browser to cache as much css
    as possible but at the same time only load the css that''s needed.  If you were
    to output all of the css onto the page, or into a single file then you run into
    caching or updating problems (pick the worse of two evils).  Whereas outputting
    a list of @imports, each referencing a cachable file, solves both of these problems
    and only adds a small amount of extra load.'
  comment_date: '2006-07-17 11:39:02'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '0'
- comment_ID: '3091'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@r21vp: Yes, that would probably be a bit faster. Feels a bit
    dirty to include 10 lines of imports though, but I guess that could work.'
  comment_date: '2006-07-17 12:15:29'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '1'
- comment_ID: '3094'
  comment_author: ozgur alaz
  comment_author_url: ''
  comment_content: 'Great article is worth to be homepage of digg. The story has dugg
    now, please add your diggs: \nhttp://digg.com/programming/Static_and_dynamic_CSS_combined'
  comment_date: '2006-07-17 13:05:39'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '0'
- comment_ID: '3103'
  comment_author: SitePoint Blogs &raquo; Jul 17, 2006 News Wire
  comment_author_url: http://www.sitepoint.com/blogs/2006/07/18/jul-17-2006-news-wire/
  comment_content: '[...] Static and dynamic CSS combined With version 4 browsers
    nearly a dim memory, we can start putting the CSS @import command to good use.
    One problem it can neatly solve is giving cacheability to dynamic CSS. (tags:
    css php) [...]'
  comment_date: '2006-07-18 01:32:47'
  comment_post_ID: '80'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '3124'
  comment_author: Johan
  comment_author_url: ''
  comment_content: how about using the link tag (alternate stylesheets) to import
    the different stylesheets
  comment_date: '2006-07-18 20:02:53'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '0'
- comment_ID: '3142'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Johan: that works for a few "modules" but as soon as you get
    over 5 diffent it starts to feel strange. Feels a little better handling it in
    the CSS file altogether in my opinion.'
  comment_date: '2006-07-19 01:57:03'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '1'
- comment_ID: '3146'
  comment_author: Juan Calderón - Desarrollo Web &raquo; Combinando CSS estático y
    dinámico
  comment_author_url: http://jcwebdesign.wordpress.com/2006/07/19/combinando-css-estatico-y-dinamico/
  comment_content: '[...] Friendly Bit » Static and dynamic CSS combined [...]'
  comment_date: '2006-07-19 07:06:17'
  comment_post_ID: '80'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '3184'
  comment_author: project.47 - Portfolio &#38; Personal Website &raquo; Blog Archive
    &raquo; Combinao de CSS esttico e dinmico
  comment_author_url: http://project47.viscountbox.com/combinacao-de-css-estatico-e-dinamico/
  comment_content: '[...] Encontrei um artigo (em ingls) no Friendly Bit ensinando
    como fazer essa dinamicidade do CSS, abrindo, somente, quando pertinente. Trata-se
    de um script PHP simples e funcional. [...]'
  comment_date: '2006-07-20 03:58:22'
  comment_post_ID: '80'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '3188'
  comment_author: Static and dynamic CSS combined &middot; Style Grind
  comment_author_url: http://stylegrind.com/static-and-dynamic-css-combined/
  comment_content: '[...] Check out the code from Friendly Bit. [...]'
  comment_date: '2006-07-20 14:01:08'
  comment_post_ID: '80'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '3234'
  comment_author: Johan
  comment_author_url: ''
  comment_content: How about combining both:\n\nimported stylesheets and linked stylesheets.
    Eg:\nlinked stylesheet module 1:\nimport CSS module 1.1\nimport CSS module 1.2
  comment_date: '2006-07-22 16:10:12'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '0'
- comment_ID: '3260'
  comment_author: Recursos de fin de semana (II)
  comment_author_url: http://www.buayacorp.com/archivos/recursos-de-fin-de-semana-ii/
  comment_content: '[...] Combinando CSS dinámico y estático. [...]'
  comment_date: '2006-07-23 07:32:01'
  comment_post_ID: '80'
  comment_type: pingback
  is_admin: '0'
- comment_ID: '22545'
  comment_author: Dave Hallam
  comment_author_url: http://www.hallamfamily.co.uk
  comment_content: I have a php script for family history site which I am rebuilding.
    I have 4 families (grandparents). The script has a template with css. I am looking
    to have each family pages a different color (switched) in the background via PHP.
    Each family has the php code ending in tree=01 or tree=02 etc, could you give
    me advice how to do this please?\nmany thanks,\nDave
  comment_date: '2007-03-21 00:10:59'
  comment_post_ID: '80'
  comment_type: null
  is_admin: '0'
- comment_ID: '25608'
  comment_author: SolucioPC - Blog &raquo; Blog Archive &raquo; Crear hojas de estilo
    dinámicas con php
  comment_author_url: http://www.soluciopc.com/blog/crear-hojas-de-estilo-dinamicas-con-php/
  comment_content: '[...] http://friendlybit.com/css/static-and-dynamic-css-combined/
    [...]'
  comment_date: '2007-06-25 14:51:29'
  comment_post_ID: '80'
  comment_type: pingback
  is_admin: '0'
---