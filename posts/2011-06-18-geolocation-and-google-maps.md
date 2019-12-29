---
author: Emil Stenström
categories:
- JS
- Modern web
date: 2011-06-18 14:11:11
guid: http://friendlybit.com/?p=591
id: 591
permalink: /js/geolocation-and-google-maps/
title: Geolocation and Google maps
---

<div class="zemanta-img">
  <figure style="width: 240px" class="wp-caption alignright"><a href="http://www.flickr.com/photos/57552634@N00/3791431635"><img title="Google Maps Marker in Tokyo" src="/files/post-media/3791431635_c722c1d51a_m.jpg" alt="Google Maps Marker in Tokyo" width="240" height="120" /></a><figcaption class="wp-caption-text">Image by heiwa4126 via Flickr</figcaption></figure>
</div>

Google Maps has has geolocation support for a long time, but I still find people surprised of how it all works. So here's a short writeup, skip it if you already know all about geolocation.

**Lets start** at the <a title="Google Maps" rel="homepage" href="http://maps.google.com/">Google Maps</a> frontpage. Among the zoom controls, above the little old man, there's a button in the form of a small circle. It does not look like much, but what it's doing is incredibly cool. Click it and the map moves to where you are, with an accuracy of ~20 meters. Sci-fi crazy!

**How does it work?** In the newer browsers (all but IE6, IE7, or IE8) may ask you for your positioning information from the browser. It usually shows up as a bar at the top of the browser. The browser then gathers two specific forms of positioning information from your computer: your **IP address** and the **signal strength of any wireless network** near you. That information is then sent, if you approve it, to Google, which returns the coordinates you are at the moment.

Google can do this because they've been driving around with their street view cars all over the world, and measured signal strength of WiFi networks (public and private) at each specific location. Now they can use that information, combined with your local signal strength conditions, to triangulate their way to where you are. And it's both accurate and fast.

If your wireless reciever is turned off, or you're at a stationary computer, all calculations are based on the IP number. These kind of lookups are quite arbitrary and inaccurate, I just get to the nearest big city when trying to use it over a non-wireless line. But mobile connections are slowly taking over landlines, so I guess this problem will solve itself automatically.

The best kind of technology throws you forward in time, and make your realize that we're actually making progress. Geolocation has feel to it.

Looking for the techy explaination of geolocation? Have a look at [Robert Nyman's writeup](http://robertnyman.com/2010/03/15/geolocation-in-web-browsers-to-find-location-google-maps-examples/).
