---
author: Emil Stenström
categories:
- API
- Python
date: 2012-01-08 22:07:29
guid: http://friendlybit.com/python/what-movies-on-piratebay-will-you-like-the-most/
id: 851
permalink: /python/what-movies-on-piratebay-will-you-like-the-most/
title: What movies on Piratebay will you like the most?
---

Christmas, and the weeks thereafter, are times for coding. And I've been playing around with [piratebay](http://thepiratebay.org) and [filmtipset](http://filmtipset.se) (a Swedish movie recommendation) a little bit. I just pushed it to the [filmtipset-piratebay project on GitHub](https://github.com/EmilStenstrom/filmtipset-piratebay), if you want to take a look.

## CSS for screen scraping

The script is using **CSS for screen scraping**; something that works extremely well:

```python
from lxml import html
import requests
response = requests.get("http://thepiratebay.org/browse/207/0/7")
document = html.document_fromstring(response.content)
links = document.cssselect(".detLink")
print [link.text_content() for link in links]
```

Note: You need [lxml](http://lxml.de/) and [requests](http://docs.python-requests.org) to run the above example.

Saving the above snippet to a py-file and running it will give you a list of all torrents on the given url. Play around with the CSS selector to get some other data from the page.

## Extracting movie titles from torrent names

It's surprisingly easy to convert torrent names to movie titles. Just follow this simple algorithm:

  1. Split the torrent name into words by treating all non-alphanumeric characters as space.
  2. Loop over the remaining words, and look for a predefined set of "torrent endings".
  3. When you find an ending, cut the name from there
  4. (Optional) Remove the year if there is one at the end of the remaining string
  5. (Optional) Remove all movies which really are bundles of movies, and not single movies. This is easily done by looking for a set of common strongs such as "trilogy" and "series"

Result: "Real.Steel.2011.720p.BluRay.x264-REFiNED" -> "Real Steel"

You can find my movie title finder implementation in parse.py on GitHub.

## Cache all HTTP Request

To both save time, and be nice to the services we're querying, the script caches all HTTP requests for a number of days. I do this by simply saving the returned HTML/JSON to a file, and checking the file system for that file before making a new request. Saving the HTML/JSON, and not the processed result, makes it possible to experiment with the parsing, without having to wait for new requests from the server.

My caching implementation is of course also on GitHub.

\***

All and all, this has been a fun little project, and I've learned a lot. But I'm sure we can make this even better. Feel free to send pull requests!
