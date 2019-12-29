---
comments:
- comment_ID: '38214'
  comment_author: jazplyer
  comment_author_url: ''
  comment_content: 'I agree. I''ve been doing infosec for 10 years and average people
    would NEVER understand pgp/etc. \n\nWhat you are describing is basically equivalent
    to DKIM: except it''s encryption instead of signing\n\nDKIM has basically worked
    as a protocol, so the encryption equivalent should be doable too'
  comment_date: '2016-10-28 23:58:10'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '0'
- comment_ID: '38215'
  comment_author: Peter
  comment_author_url: ''
  comment_content: Your scheme seems a reasonable workable idea.\n\nCan I suggest
    an additonal bit of commentary, between 'Decrypt incoming e-mails using the private
    key of that user' and 'Deliver the e-mail using the normal protocols', of 'Spam
    and malware content checking'.\n\nAs the email is encrypted, it cannot be content
    checked in transit. The point I'm trying to clarify is that the receiving client
    can check the content, after decryption, but before delivery to the user.
  comment_date: '2016-10-29 00:57:15'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '0'
- comment_ID: '38216'
  comment_author: Matthew Steel
  comment_author_url: http://Repsilat.com
  comment_content: '&gt; Some may frown reading that I suggest leaving the private
    key in the hands of your e-mail provider.\n\nIt''s a strict improvement over "no
    encryption," and has a simple upgrade path to "true privacy" for those people/providers
    who want it: users give a public key to their email provider, and their provider
    delivers still-encrypted emails to the client.'
  comment_date: '2016-10-29 01:02:27'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '0'
- comment_ID: '38217'
  comment_author: Jonathan B.
  comment_author_url: ''
  comment_content: I gave $1,000 last year to EFF with a note to direct my funds to
    this very issue.  It's a very hard problem and needs big players to solve it.  More
    people need to get involved to lay out a fully-baked solution.  That takes money,
    at least to some degree.\n\nFor me, more people need to complain to EFF since
    they seem to have the biggest bullhorn.\n\nWhat do you think?  How do we increase
    the activism around this issue?
  comment_date: '2016-10-29 02:31:27'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '0'
- comment_ID: '38218'
  comment_author: PassingBy
  comment_author_url: ''
  comment_content: I understand that this is means your e-mail provider can read your
    e-mail, so it won’t work for everyone. But I think most people will accept that
    the same way they accept that their bank can read their bank statement. If we
    can trade this for usability it’s still a HUGE step up for privacy\n\nPerhaps
    many fail to understand that millions of users are exactly trying to avoid their
    providers having the least chance to read their mails. And no, this is not the
    same as a bank statement. Perhaps in the US or somewhere else in the Anglosphere
    where people said goodbye to their privacy altogether. \n\nIt wouldn't work for
    millions of users. The system as it's now simply grants no safety at all. Your
    chances that your mails are intercepted by strangers are relatively low. The chance
    your mail provider (from Google to outlook passing through yahoo or any other
    us based platform) will collect data on you for sure. That's the problem in a
    nutshell. And encryption is not enough. Those mails simply shouldn't be routed
    through those operators nor they should be stored in the cloud. From a security
    point of view, direct end-to-end with cryptography would be safer (in that case
    the OS would be the issue, yet better than having your personal data in somebody
    else's server).
  comment_date: '2016-10-29 02:34:19'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '0'
- comment_ID: '38219'
  comment_author: pizaninja
  comment_author_url: ''
  comment_content: 'The first entity I don''t trust is my email system provider (e.g.
    gmail) so I''m not at all confortable with the ideal of letting a third party
    managing any of my private key.\n\nA primary missing rule is that your private
    key must still be private, and managed like a real physical key: you must get
    it when required, and keep it near you.\n\nSo, the servers of your email provider
    should be able to share your public key, that''s Ok.\nBut your private key must
    be only yours.\n\nAnd so, if you really want to keep the ability to get your email
    from a cybercoffe, why not use a third party service to retrieve your encrypted
    private key, but please, don''t let your private keynésien to your email service
    provider.\n\nAnd then, web browsers should be able to provide trusty features
    to manage your keys:\n- ability to exchange with your own third party key server\n-
    ability to decrypt/encrypt your data on the fly\n- ability to forget your credentials
    when you leave your web session\n- ability to generate asymetric key pair for
    you\n- ability to use your already existing gpg (or even ssh) keys if any.'
  comment_date: '2016-10-29 03:09:35'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '0'
- comment_ID: '38220'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: 'To the people commenting that any solution that doesn''t perform
    end-to-end encryption won''t work: Unless you suggest another solution to the
    usability problem that key management puts on users, I don''t see any alternative.'
  comment_date: '2016-10-29 10:12:04'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '1'
- comment_ID: '38221'
  comment_author: Georgi
  comment_author_url: ''
  comment_content: Splitting emails with multiple recipients into several emails will
    loose the "thread", so users will not be able to "reply to all". Multi-recipient
    emails are important part of the way business operate today, so this is major
    issue here.
  comment_date: '2016-10-29 15:50:12'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '0'
- comment_ID: '38222'
  comment_author: Emil Stenström
  comment_author_url: http://friendlybit.com
  comment_content: '@Georgi: This is not true. All other recipients would still be
    included in the e-mail, just not the public, unencrypted part of it. After decryption
    it would look exactly the same as before. The idea between splitting it is so
    that each part can be encrypted with that persons individual encryption key.'
  comment_date: '2016-10-29 23:04:22'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '1'
- comment_ID: '38224'
  comment_author: Martin
  comment_author_url: http://www.prettyeasyprivacy.com
  comment_content: I'd like to point to this white paper <a href="http://pep.foundation/docs/pEp-whitepaper.pdf"
    rel="nofollow">http://pep.foundation/docs/pEp-whitepaper.pdf</a> It's exactly
    solving issues you described in the article. Encryption and anonymity also for
    business. Open source solution which is already in current enigmail code.
  comment_date: '2016-11-02 10:50:08'
  comment_post_ID: '1086'
  comment_type: null
  is_admin: '0'
---