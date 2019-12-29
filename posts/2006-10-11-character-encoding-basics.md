---
author: Emil Stenström
categories:
- Other
date: 2006-10-11 20:06:28
guid: http://friendlybit.com/other/character-encoding-basics/
id: 96
permalink: /other/character-encoding-basics/
title: Character encoding basics
---

Character encodings is something that developers tend to push away as something too hard to bother with. It's **not** hard. It's just that there's several ways of storing letters in a file. This article is my way of trying to explain how it works.

At first developers thought that 256 letters must be enough. Computers were for English speaking people only and few special characters where allowed. There were good reasons for this: memory was expensive and a fixed size for characters made the programming easier. This first way of storing things were called ASCII.

Time went by and people discovered that they needed letters that were not among the original 256. So what they did was replace a few special characters with the ones they needed. But different people needed different characters and soon we had hundreds of sets to select from. This mess is what you see if you select View -> (Character) encodings -> More (encodings) in your browser.

Encodings is just about mapping a certain number to the correct character. The first characters are often placed at similar spots, so your site does not necessarily break if you pick the wrong one. Very rarely do you need to know all of them. Just knowing that **latin-1** (sometimes called **iso-8859-1**) is the most popular one, but that there are better options out there, will get you far.

Having that many sets was clearly the wrong way to go, and smart people sat down together to come up with something better. They presented **UTF-8**, a way to store "all" possible characters in a single format. The idea is to save the first characters with just one letter, the next set with two numbers, three numbers, and so on. The exact [technical details](http://en.wikipedia.org/wiki/UTF-8 "technical details of UTF-8") does not matter, all you need to know is how it works in browsers and your favourite text editor.

## Setting the right encoding

First you need to find out what encoding your HTML/CSS/JS editor produces. I highly recommend you to use UTF-8 if it's available, why be limited to just 256 letters? In my favourite editor right now, [Notepad++](http://sourceforge.net/projects/notepad-plus/), there's a "Format"-menu where I can select "UTF-8 without BOM". You probably have something similar in your settings.

When in UTF-8 mode you don't need to use HTML entities (those things that look like `&#345;`) that usually are used to produce strange characters. UTF-8 supports the character you need, just type it in, copy it from somewhere, or pick it from some list of available chars. If you use the correct charset selected everything will work alright. Good, you now have a file locally with some exotic characters in it (if not, you can use this string: "Iñtërnâtiônàlizætiøn").

In the browser world things works somewhat different. If the server sends a certain encoding, you can't do anything about it in your HTML. Many of you probably set the encoding using the meta element in HTML, something I find somewhat strange, how can the browser start reading the page at all if it doesn't know what encoding it's in? So, rely on your server to send the right encoding.

Start by checking what version your server sends by default: In the [Web Developer Toolbar](http://chrispederick.com/work/webdeveloper/), just go to the page you want to examine and select Information -> View Response headers. Look for Content-Type or Content-Encoding and se what it's set to.

If it's the wrong one (something other than iso-8859-1 and UTF-8 is probably wrong), you can change it like this:

Setting encoding to UTF-8 with **PHP**:

```php
header('Content-Type: text/html; charset=utf-8');
```

Setting encoding to UTF-8 with **ASP** and **ASP.Net**:

```aspx-cs
<%Response.charset="utf-8"%>
```

Setting encoding to UTF-8 with **JSP**:

```jsp
<%@ page contentType="text/html; charset=UTF-8" %>
```

Setting encoding to UTF-8 with **Java Servlets**:

```java
resource.setContentType ("text/html;charset=utf-8");
```

Setting encoding to UTF-8 with **Python**:

```python
response.headers["Content-Type"] = "text/html; charset=utf-8"
```

Setting encoding to UTF-8 with **Ruby on Rails**:

```ruby
@headers["Content-Type"] = "text/html; charset=utf-8"
```

You probably have to include the snippet of code for the language you use in some template-file that's loaded before everything else. Test that everything works by reloading your sample page from your server and check the response with webdev toolbar.

Hope that helps someone!
