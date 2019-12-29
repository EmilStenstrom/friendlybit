---
author: Emil Stenström
categories:
- JS
date: 2007-02-21 22:13:21
guid: http://friendlybit.com/js/improving-interactivity-with-javascript/
id: 113
permalink: /js/improving-interactivity-with-javascript/
title: Improving interactivity with Javascript
---

Push buttons, radio buttons, check boxes, select boxes, and text inputs. That's the controls HTML allows us to use to interact with our users.

A small dedicated group of people at the office (I work at [Valtech](http://www.valtech.se)) sat down and listed all controls we could think of. The list below is basically that list, completed with examples where possible. Let me stress that the below controls are meant as **inspiration**. They are not all free, or even available for download. If you decide to use one of the ideas, google for them first and pick the best one. While selecting one, make sure it supports some kind of fallback for users without javascript enabled.

## Slider

Slider control meant to let users select values from a range of options.

[![Slider control](/files/ajaxexamples/slider.png)](http://webfx.eae.net/dhtml/slider/slider.html)

## Date picker

What format should this date be? What weekday is the 15:th of august? A good date picker helps the user answer those questions and makes filling in dates much more delighful.

[![Date picker](/files/ajaxexamples/datepicker.png)](http://www.basicdatepicker.com/)

## Smart text boxes

It's easy to make some text boxes only allow certain kinds of characters. Why allow letters in the age field?

[![Text box that only allows numbers](/files/ajaxexamples/smarttextbox.png)](http://www.cambiaresearch.com/c4/029c978b-aac5-472e-97a8-95b256f5febd/How-Can-I-Use-Javascript-to-Allow-Only-Numbers-to-Be-Entered-in-a-TextBox.aspx)

## Mixing text inputs with select boxes

Allow users to both input text and pick common options.

[![Google Suggest](/files/ajaxexamples/gsuggest.png)](http://www.google.com/webhp?complete=1&amp;hl=en)

![Ingredience picker with AJAX](/files/ajaxexamples/extratasty.png)

## Drag and Drop

Users are used to dragging and dropping things from their operating systems. Letting them do the same on the web makes for a great affect! Don't forget about a fallback though, not everyone uses a mouse (A buy-button is enough).

![Example shop with drag and drop](/files/ajaxexamples/dragdrop.png)

[![Real shop with drag and drop](/files/ajaxexamples/panic.png)](http://www.panic.com/goods/)

## Collapse and expand control

Makes it possible to quickly show less important information on demand. Just make sure everything is open by default (with no javascript).

![Toggling a block is easy](/files/ajaxexamples/expand.png)

## Advanced tooltips

When the title attribute is not enough. Use images, fine-tune the delay, make them sticky if you click them, it's all up to you!

![Tool tips with a little spice](/files/ajaxexamples/tooltip.png)

## Autosaving form fields

If you write an email with [Gmail](http://www.gmail.com) and the browser crashes, you'll appreciate that Gmail automatically saves your text regularly. It's done with a simple piece of javascript that periodically sends all your text off to the server, and saves it away. Simple and **very** useful.

## Auto validation

While filling in some forms you'll notice a little green check on the side. I can't begin to praise how much faster this makes filling out forms. Directly after you've written enough letters in the password field you'll find that it's ok. No more trial and error against a slow server (unless you have javascript off, of course).

[![Early notification that the password is correct](/files/ajaxexamples/autovalid.png)](http://www.zapatec.com/website/ajax/zpform/doc/demo.html#ajax.html)

## Controls affecting each other

In complex forms it's not unusual to want the user to fill in either one set of fields or another. The showing and hiding of what fields are available is a another perfect case of where javascript really helps.

## Image handling

It's time to get easy handling of images in browsers. Javascript can help there too, by combining drag and drop with resizing and so on. Photoshop, here we come!

[![Images you can move and resize in the browser](/files/ajaxexamples/images.png)](http://www.walterzorn.com/dragdrop/dragdrop_e.htm)

## Search-based or structured navigation

Sometimes new navigation schemes can be useful. Using search instead of navigation is an interesting idea. Another is letting the user pick categories and using them in search.

[![Menu that allows expanding and searching](/files/ajaxexamples/searchstructure.png)](http://www.vitvarumaklarna.se/)

## Better **looking** form fields

Javascript also allows you to enhance existing form fields with prettier equivalents.

![Pretty form controls](/files/ajaxexamples/checkboxes.png)

## Sortable items

Sometimes you want drag and drop in a more controllable manner. Why not use it to make it easier to sort your lists?

![Sortable list items](/files/ajaxexamples/sortable.png)

That's all! Hope I've given you some ideas of widgets/controls you can use to enhance user experience. Good luck!
