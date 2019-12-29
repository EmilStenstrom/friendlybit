---
author: Emil Stenström
categories:
- Security
date: 2016-10-28 23:26:00
guid: https://friendlybit.com/?p=1086
id: 1086
permalink: /security/how-to-make-e-mail-encrypted-for-everyone/
title: How to make e-mail encrypted for everyone
---

> **Update**: This post is a little naive. For the real deal, look at this video from the CTO of ProtonMail: <https://vimeo.com/216747532>

When you send an e-mail today it's sent in plaintext. This means that when you connect to your local coffee shop's WiFi they can intercept all e-mail that is sent through their router. This is probably not the relationship you have with your barista…

E-mail is way more important than this, and should receive the same privacy protection as the web has with HTTPS. I haven't seen any meaningful progress on e-mail encryption in a long time, so this article is a suggestion of how to get things moving.

The base idea is this: **We should make e-mail work just like the web in terms on encryption**:

  * Encryption should be added gradually, without breaking backwards compatibility (interoperability)
  * Intermediate servers shouldn't be able to read the message (privacy)
  * Users should be able to keep sending and receiving e-mail like they always have (usability)
  * E-mail clients and e-mail providers should be able to easily implement the scheme (simplicity)

## Encrypt as much as possible of the e-mail message

For web traffic, we've encrypting everything [except the domain name](https://idea.popcount.org/2012-06-16-dissecting-ssl-handshake/) of the site we're connecting to, this is how e-mail should work too. Since we need to know who to send the e-mail to, we should encrypt everything except the recipient address.

Some of you might have read about [STARTTLS](https://en.wikipedia.org/wiki/Opportunistic_TLS), a way to make SMTP encrypted. Unfortunately STARTTLS has [several problems](https://blog.filippo.io/the-sad-state-of-smtp-encryption/) that makes it unfit to solve the privacy problem:

  * It only encrypts the message **between** the many servers your e-mail passes through. Your e-mail is decrypted and exists in plaintext on each of the intermediate servers. If any of the intermediate servers is hacked they get full access to all e-mails passing through. You likely don't have that kind of relationship with your ISP network administrator either…
  * If any of the intermediate servers doesn't support STARTTLS, the connection is downgraded to plaintext instead. One old server and the whole chain breaks.

We should apply encryption on the client when sending, and decrypt at the recipient. No intermediate servers should get access to the message.

## Encrypt with public-key cryptography (without the hassle)

The best way to handle this encryption is with [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography), where the sender first fetches the public key of the receiver, sends the message encrypted with that key, and then that the receiver decrypts it using their private key.

People are already sending e-mail this way with [PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy), so way not just use this everywhere? It has several big usability problems:

  * **You need to do key management yourself**. On the web the browser handles all cryptography for you. You  type the address in the browser and everything just works. This is not the case with PGP. Look at this guide in the eyes of a normal person: [OpenPGP for a complete beginner](http://zacharyvoase.com/2009/08/20/openpgp/) - it quickly goes into downloading zipfiles, package managers and using the command line to generate keys.
  * **You need to install software on your computer**. Most e-mail providers are moving to the web, having to install a browser plugin just to send e-mail is not the experience we should strive for. I understand that this is means your e-mail provider can read your e-mail, so it won't work for everyone. But I think most people will accept that the same way they accept that their bank can read their bank statement. If we can trade this for usability it's still a HUGE step up for privacy.

Here's how this could be done differently:

**Encryption:**

  1. For each recipient in the To, Cc, and Bcc fields:
      1. Do a lookup against their domain to see if it supports encryption. This should be a new DNS record that points to an address that the e-mail client can use to fetch the public key for a specific user of that domain.
      2. Fetch the public key for each of the users of the domain
      3. If both the domain has encryption support and the public key can be fetched, show a lock symbol beside that e-mail address to show that the message to that recipient will be encrypted. Clicking the lock can show information about the encryption that will be used, just like browsers do today.
  2. When the message is sent, split it into as many parts as the number of recipients and encrypt each part with that recipient's public key. Send it off to each recipient using the normal protocols. Users on domains that don't support encryption will get messages sent in plaintext, just like today. This ensures support can be added gradually.

Note that for the user nothing changes compared to how they send e-mail today, except that the lock shows up. Web users are slowly learning about the importance of the lock symbol when browsing the web, transfering that knowledge to e-mail too will create a push for e-mail server operators to support encryption.

**Decryption:**

  * When the encrypted e-mail reaches the intended recipients e-mail server, that server uses the private key for that user to decrypt the message and (securely) deliver it the the users inbox. The user reads their e-mail like they've always have.

Some may frown reading that I suggest leaving the private key in the hands of your e-mail provider. I agree that this means you lose some privacy to your e-mail provider. The upside here is that we gain a lot of usability. An e-mail provider (such as Gmail) could and an e-mail client (such as Thunderbird) could update all their software tomorrow and **all e-mail sent from Thunderbird to Gmail would be instantly encrypted**. This removes the burden of normal users to learn about cryptography to be safe on the web.

In summary, these are the changes that needs to happen for e-mail move towards being encrypted by default:

## Consequences for e-mail clients

  * **New features needed:**
      * Fetch a DNS record for each receiving domain they want to send an e-mail to
      * Fetch each receiving user's public key in the background
      * And encrypt as much as possible of the outgoing e-mail
      * Send the e-mail using the normal protocols
  * **Ways to pitch this to users:**
      * All e-mail sent to e-mail providers that support this scheme will be encrypted by default, with no effort on your part
      * You can easily see which addresses get encrypted messages with the lock icon that you know from browsers
      * Increased privacy from prying eyes

## Consequences for e-mail providers

  * **New features needed:**
      * Add a DNS record that points to their public keys
      * Serve the public key of a specific user that the e-mail clients ask for
      * Decrypt incoming e-mails using the private key of that user
      * Deliver the e-mail using the normal protocols
  * **Ways to pitch this to users:**
      * All e-mails sent from clients that support this scheme will be encrypted by default, with no effort on your part
      * Increased privacy from prying eyes, do you really trust your local coffee shop as much as your e-mail provider?
  * **Business reasons:**
      * Support privacy without letting go of the chance to serve ads based on the content of the users e-mails. This is a very important point for big players like Gmail that serve ads. Users or course still have the option to use another e-mail provider or add PGP if they want.
      * Nothing in this scheme blocks smaller players from making their users safe using the same methods as the big players will.

## In summary

I think this is a very straightforward way to make all e-mail encrypted. If anyone has a better suggestion that balances the needs of users, e-mail clients and e-mail providers differently I'm all ears. But let's not let this privacy travesty go on much longer…
