---
id: 394
title: 'Downloading MySQL: How bad can it get?'
date: 2009-01-25T03:31:10
author: Emil Stenström
layout: post
guid: http://friendlybit.com/?p=394
permalink: /other/downloading-mysql-how-bad-can-it-get/
btc_comment_counts:
  - 'a:0:{}'
btcnew_comment_counts:
  - 'a:0:{}'
dsq_thread_id:
  - "207559669"
btcnew_comment_summary:
  - 'a:0:{}'
categories:
  - Other
---
MySQL is quite popular on the web these days. Lots of frameworks have support for it, and some frameworks **only** support MySQL. So lots of people must be downloading it right? So what do you do when you have a website where most people will be looking for completing one simple task?

Well, you make that task really, and I mean **really**, annoying to complete. No? Yes you do, just look at this:

  1. **Surf to [mysql.com](http://mysql.com)**. Note the two horizontal navigation menus, one vertical menu, followed by a seven step banner, and five more columns of links. Note how the top navigaton has the same style as the bottom column headers, and that one is clickable, and the other is not.
  2. **Click &#8220;Downloads&#8221;**, which is the second item, in the second horizontal menu, first tab. Watch how the menu changes to highlight that you&#8217;re now at the second tab. Watch how the left menu is a list of products, which was the first link in the menu you just clicked, and note that you didn&#8217;t click products. You&#8217;re given two choices now, denoted by lots and lots of text, instead of two descriptive headers at the bottom of the page: MySQL Community Server, and MySQL Enterprise.
  3. **Decide that you want MySQL Community Server**, ignore the &#8220;community downloads&#8221;-link that makes you have to choose again, and click the &#8220;Download&#8221;-button. You&#8217;re now on the same page as if you would have clicked &#8220;community downloads&#8221;, and now are given information about the product you didn&#8217;t choose, MySQL Enterprise.
  4. **Note in the left menu** that you have somehow chosen version 5.1 of the product, even though you didn&#8217;t make that choice, and that you get arguments against using MySQL 4.0 if you go to the  &#8220;Important Platform Support Updates&#8221; page. You also get a warning that some enterprise support feature won&#8217;t work with that version.
  5. Ignore the &#8220;NOTE&#8221; about MySQL Cluster community edition, the 5.1 changelist, and the suggestion to use MD5 checksums to verify your download. **Now choose your operating system, processor architecture, and packaging option** combinations from a list of 33 options. If you&#8217;re on windows, and don&#8217;t know if your processor architecture is denoted &#8220;x86&#8221; or &#8220;x64&#8221;, you just have to guess now.
  6. You&#8217;re now take further down the page, showing you both the option you chose and the next option, you didn&#8217;t chose. If you guessed the last time, now is a chance to change your mind. If you&#8217;re on windows, **select if you want Windows Essentials, a Zip file/setup.exe combination, or a windows installer**. Find that it isn&#8217;t Windows installer, but Without installer. Read your options again. Get really confused, since essentials and packaging options doesn&#8217;t seem to be mutually exclusive.
  7. Guess that you want the first file, and note how that option isn&#8217;t clickable. Instead, review the version number and MD5 checksum, and **click &#8220;Pick a mirror&#8221;**. Not because you want to do that, but because there are no other options except a signature link that&#8217;s smaller.
  8. You&#8217;re now given the filename of the file you are about to download, and are **asked to register on the site**. The menu shows you&#8217;re on the DevZone. Since you don&#8217;t have an account, click &#8220;New user&#8221;, and fill out the seven required fields, including which company you work for. Did you chose Enterprise after all?
  9. At the end of the form, note the link &#8220;**No thanks, just take me to the downloads!**&#8221; and click it.
 10. Again, you&#8217;re moved further down the page, to a **list of 150 countries**, denoted by their flag. Read the note that says that this is a list which is sorted by the countries closest to you, and note that it&#8217;s completely wrong, and ordered alphabetically.
 11. Now **select which protocol** you want to download over, HTTP or FTP. Why on earth would you want to download via FTP from a web browser?! Anyway, select HTTP and you finally get to download the damn file.

How can downloading a file be this hard? What did they think? Did they not learn anything from the [firefox](http://getfirefox.com/) website? One big green button is all you need, is that too hard for you MySQL devs?
