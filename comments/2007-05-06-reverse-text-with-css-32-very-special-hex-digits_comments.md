---
comments:
- comment_ID: '23982'
  comment_author: grimman
  comment_author_url: http://dlxmedia.net/
  comment_content: Ooh, seems like this could be useful in one app or another. ;)
  comment_date: '2007-05-06 18:24:26'
  comment_post_ID: '123'
  comment_type: null
  is_admin: '0'
- comment_ID: '24077'
  comment_author: jesse
  comment_author_url: http://geekosphere.org
  comment_content: omg, this is the best one ever.
  comment_date: '2007-05-09 22:10:43'
  comment_post_ID: '123'
  comment_type: null
  is_admin: '0'
- comment_ID: '24147'
  comment_author: Slap Happy
  comment_author_url: http://www.imarc.net/communique/view/305/the_newest_victim/
  comment_content: Um, the Diggers aren't rebels. The Diggers are lawbreakers. This
    is the lamest thing to ever be considered a revolution. Ever. It's an HD-DVD encryption
    key! Woo! Let's see the so-called "rebels" actually make a positive difference
    in the world. Now that would be a revolution.
  comment_date: '2007-05-11 19:49:23'
  comment_post_ID: '123'
  comment_type: null
  is_admin: '0'
- comment_ID: '24816'
  comment_author: Biscuitrat
  comment_author_url: ''
  comment_content: Very sneaky; it took me a second :P
  comment_date: '2007-05-30 19:09:40'
  comment_post_ID: '123'
  comment_type: null
  is_admin: '0'
- comment_ID: '33434'
  comment_author: Metric Stormtrooper
  comment_author_url: http://www.cheaphoteldealsaustralia.com/
  comment_content: Awesome - was looking for something like this to protect emails
    and phone numbers on a website from scrapers and bots!\n\nin case anyone else
    is interested:\n<code>\nfunction cProtect($text)\n{\n⇥//protect the contact info
    by reversing phone number and email, and then re-reverse it again via css\n⇥$phone
    = get_phone($text);\n⇥$email = get_email($text);\n⇥$revphone = str_mirror($phone);\n⇥$revemail
    = str_mirror($email);\n⇥\n⇥$text = str_replace($phone, $revphone, $text);\n⇥$text
    = str_replace($email, $revemail, $text);\n⇥return $text;\n}\n\nfunction str_mirror($string)\n{\n⇥$res
    = strrev($string);\n⇥$res = ''.$res.'';\n⇥return $res;\n}\n\nfunction get_phone($string)\n{\n⇥$regex
    = '/\(?([0-9]{2,4})\)?[-. ]?([0-9]{2,4})[-. ]?([0-9]{2,4})[-. ]?(([0-9]{2,4}))?[-.
    ]?([0-9]{2,4})?[-. ]?/is';\n⇥preg_match($regex, $string, $match);\n⇥if(isset($match[0]))\n⇥{\n⇥⇥return
    $match[0];\n⇥}\n⇥return false;\n}\n\nfunction get_email($string)\n{\n    $regex
    = "/([_a-z0-9-]+)(\.[_a-z0-9-]+)*@([a-z0-9-]+)(\.[a-z0-9-]+)*(\.[a-z]{2,4})/is";
    \n⇥preg_match($regex, $string, $match);\n⇥if(isset($match[0]))\n⇥{\n⇥⇥return $match[0];\n⇥}\n⇥return
    false;\n}\n\n$text = "please call at 123 456 789, or email me at test@example.com";\n\necho
    cProtect($text);\n\n</code> \n\nResult:\n<code>\nplease call at 987 654 321, or
    email me at moc.elpmaxe@tset\n</code>
  comment_date: '2010-02-10 23:40:29'
  comment_post_ID: '123'
  comment_type: null
  is_admin: '0'
- comment_ID: '33466'
  comment_author: Cubicle Generation
  comment_author_url: ''
  comment_content: '@ Metric Stormtrooper,\n\nThat''s all well and dandy, but when
    someone copy and pastes the e-mail address, it will be backwards still :)'
  comment_date: '2010-03-10 07:46:13'
  comment_post_ID: '123'
  comment_type: null
  is_admin: '0'
---