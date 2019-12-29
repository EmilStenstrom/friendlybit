---
author: Emil Stenström
categories:
- CSS
date: 2006-06-11 15:15:58
guid: http://friendlybit.com/css/real-hackers-dont-use-css/
id: 68
permalink: /css/real-hackers-dont-use-css/
title: Real hackers don’t use CSS
---

<p class="first">
  Back in the old days of 1996 there were two kinds of people. Those who understood the web, often referred to as "hackers", and those that didn't. A <em>hacker</em> could throw together a website in a few minutes, filled with the latest possibilities that the web offered: animated gifs, scrolling marquee text and blinking red text for the really important stuff. It was a glorious time and the hackers really ruled the web. It started growing.
</p>

## Hackers and designers

With growth came the _designers_. They wanted to use the web just like the unlimited piece of paper it was. So they sent their designs, the same designs they had previously printed, to the hackers and said: "I want this on the web". The hackers looked at the designs and didn't like them at all. But the designers were the ones paying their salaries so they had no chance but to do what the designers wanted.

When the hackers started working they quickly came to the conclusion that this was harder than they had predicted. Then a smart guy that really knew his way around the web found a tutorial describing how to do something called "image maps". The hackers cheered! They could take the dreaded designs and put them up on the web as images. Then add transparent clickable areas on top of the images that linked to other images. The hackers' status had been reinstated and the designers looked at the results and were happy, "It looks just like we want" they said.

### How to make a website, a hacker’s guide:

  1. Convert the designers images to JPG
  2. Add an image-map to each one of them
  3. Make sure all links work
  4. Show the designers

## Hackers and customers

Here entered the _customers_. The company website, that looked just like the designers wanted and was coded just like the hackers wanted, was very slow. Sometimes it took over 15 minutes for the customers to get the info they wanted from the site. Phones started ringing in the hackers' offices and they all gathered to try to solve the problem. This was when the major breakthrough in the web history came.

One clever hacker suggested that they split the images in many parts and used tables to put them back together. The older hackers scratched their heads, "Tables? Where did they hear of them before?”. After some research they found that tables were sometimes used in research reports to show a grid of values. “Just put some images in those cells instead and it will look just like before”, explained the clever hacker. He continued, "… but that doesn't make anything faster. To make the page faster we split it so that we can remove some parts. If there is a large block of blue somewhere we can remove that image and set a background-color on the cell instead!". There was much rejoice and the hackers got to work. Many had problems dealing with splitting the images in the image programs, but after a couple of weeks of training they mastered it.

The years passed by and the hackers got better and better at taming tables to do just want they wanted. Someone came with the idea of putting another table inside the first one. That made the code a little easier to maintain since they didn't require the use of row- and colspan. Additionally that made it possible to add margins to your text, something that made the designers happy. Someone came with the clever suggestion that sometimes text can be removed from the image and written in the cell instead. This made the designers a bit annoyed since sometimes the customers got the wrong font but it wasn't an issue big enough to start a fight over.

### How to make a website, a hacker’s guide (_version 2_):

  1. Convert the designers images to JPG
  2. Slice the images so that the big one-colored areas can be replaced with a table cell
  3. See if any of the text can be removed from the image and set in a cell
  4. Link each individual image correctly or use an image-map.
  5. Make sure all links work
  6. Show the designers
  7. Show the customers

## Hackers and standardists

The earth shook and the _web standardists_ entered the scene. The standardists said to the hackers, "You are doing things all wrong, you need to redo your sites and learn everything from scratch again". The hackers laughed. Their customers were happy, the designers were happy, they were happy, why should they change? The standardists spoke again, "but your page will load faster with standards". The hackers looked back and remembered how slow their sites once were, they looked at the adoption of high speed internet connections and they reckoned that speed wasn't a problem.

The standardists were now annoyed, why couldn't the hackers understand why standards were better? They gave it one last chance and said "But if you use CSS for layout your sites will be much easier to maintain!". In reply the hackers showed all their table skills they had acquired over the years. One guy had 16 nested tables to show. Another guy used frames to layout his site and had a whopping 25 frames in a spectacular pattern which all the other hackers envied. The hackers really knew what they were doing. They said, "There’s no need learning this new stuff, it will just take a lot of my time and it isn't any better".

### How to make a website, a standardist’s guide:

  1. Look at the design the designer gave you, figure out what parts the design consists of.
  2. Start writing the HTML corresponding to those parts. Try to avoid adding elements to the HTML just for the sake of design. Make sure all content in the design is represented in the HTML (text preferable).
  3. Link a CSS file to your HTML and start adding style to the document. Test in the modern browsers and read guides with common bugs to fix problems you encounter.
  4. Show the designers and explain why they can't have it look just like it would on paper.
  5. Do user testing to determine things work or not.
  6. Release it to the customers and be open to feedback.

## Conclusion

When you, as a standardist, talk to hackers about standards, keep in mind that they are good at what they do. There's a reason they are doing it a certain way and it works. Just throwing out a "Tables are so -96" won't bite; you need to be smarter than that. Don’t forget that you were once in the same seat, and use the same arguments that made you switch.

<p class="first">
  And yes, that guy using frames for layout in the text above, was me.
</p>
