---
author: Emil Stenström
categories:
- CSS
- HTML
- JS
date: 2006-01-06 01:16:59
guid: http://friendlybit.com/css/make-a-tooltip-out-of-some-columns-in-a-table/
id: 31
permalink: /css/make-a-tooltip-out-of-some-columns-in-a-table/
title: Make a tooltip out of some columns in a table
---

A worried user joins the #CSS channel on EFNet. He has a big problem with the site he's currently working on and wonders if there might be a problem with his markup. Let's see what he wants.

The site sells some kind of houses and each house has a few "options" (let's pretend a bigger door is one option) that the user should be able to select among. Each of these options has a name and costs a certain amount of money. When you move your mouse over one of the options, he wants more info to pop up in a small box. In the box there should be an image, a store name and strange number. What HTML should he use to mark that up?

We talked for a while and thought about definition lists containing a div with the extra info in, perhaps a two-column table with a div in the second column? After looking again it became pretty clear, if we just look at his data and not think about the design, all that was left was one big table. Everything that he wants in the tooltip are things that could as well be shown in a big table. So why not use exactly that markup and then use javascript to make some cells only pop up when the row was hovered?

This is the markup I propose:

```html
<table summary="Options for your house">
  <thead>
    <tr>
      <th>Option</th>
      <th>Price</th>
      <th class="tooltip">Image</th>
      <th class="tooltip">Store</th>
      <th class="tooltip">SKU#</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bush</td>
      <td>$3</td>
      <td class="tooltip a1"><img src="/files/post-media/bush.jpg" alt="An alabama bush"></td>
      <td class="tooltip a2">Alabama</td>
      <td class="tooltip a3">#23535151</td>
    </tr>
    <tr>
      <td>Bush</td>
      <td>$3</td>
      <td class="tooltip a1"><img src="/files/post-media/bush.jpg" alt="An alabama bush"></td>
      <td class="tooltip a2">Alabama</td>
      <td class="tooltip a3">#23535151</td>
    </tr>
  </tbody>
</table>
```

What you see there is a plain five column table with some classes spread out to make it easier to fetch what we want with the javascript later on. The whole table is given the id "info", this makes us able to separate it from other tables on the same page. Each cell that are going to be in the tooltip get the class "tooltip" and an aditional a1-a3 class that simply is used to position the specific cell later on.

Next we need to do two of things:

  1. Loop over the table and hide everything with the class "tooltip"
  2. Loop over all table rows and add a mouseover function to each of them that makes them show all hidden cells in that particular row

To fetch all elements that has a certain className we will use Jonathan Snook's fabulous getElementsByClassName. It takes two arguments, the element whose children it should loop through and the className it should look for. The function looks like this:

```js
function getElementsByClassName(node, classname) {
   var a = [];
   var re = new RegExp('\\b' + classname + '\\b');
   var els = node.getElementsByTagName("*");
   for(var i=0,j=els.length; ij; i++)
      if(re.test(els[i].className))a.push(els[i]);
   return a;
}
```

Next we need to write the code that fulfils the list we wrote previously:

```js
// Hide all classes with the className "tooltip"
var tooltips = getElementsByClassName(
   document.getElementsByTagName("body")[0], "tooltip");
for (var i = 0; i  tooltips.length; i++) {
   tooltips[i].className += " hide";
}

var tbodies = document.getElementsByTagName("tbody");
for (var i = 0; i < tbodies.length; i++) {
   var trows = tbodies[i].getElementsByTagName("tr");
   // Add a function to each tr that makes it show it's cells on mouseover
   for (var j = 0; j < trows.length; j++) {
      trows[j].onmouseover=function() {
         var childtooltips = getElementsByClassName(this, "tooltip");
         for (var k = 0; k < childtooltips.length; k++) {
            childtooltips[k].className+=" hooover";
         }
      }
      // And hides all child cells on mouseout
      trows[j].onmouseout=function() {
         var childtooltips = getElementsByClassName(this, "tooltip");
         for (var k = 0; k < childtooltips.length; k++) {
            childtooltips[k].className =
               childtooltips[k].className.replace(new RegExp(" hooover\\b"), "");
         }
      }
   }
}
```

A note here is that we don't loop over the first table row. That one contains the table headers and shouldn't react to us hovering it.

Last but not least we need a few lines of CSS to make the page behave like we want it to. Without either Javascript or CSS enabled a plain table should be shown with all cells visible. If you have both enabled you don't want the cells that contain the tooltip to take up space in the table. Here's the code:

```css
.hide {
   left: -10000px;
   position: absolute;
}
.hooover { left: 80px; }
tr { position: relative; }
.a1 {
   border: 1px solid Black;
   width: 300px;
}
.a2 { padding: 20px 0 0 120px; }
.a3 { padding: 20px 0 0 200px; }
```

The "hide" class is added to any element with the class "tooltip". Why not make the tooltip class hide the cells right away you ask? The answer is that then a non js user would not see those cells at all. This way we get the best of both worlds. To remove the hidden cells from taking up space we remove them from the flow with `position: absolute;` and to hide them we use `left: -10000px`.

The "hooover" class get enabled when we mouseover one of the table rows. It just sets the left value to a far more visible 100px. Lastly we set some styles on the a1-a3 classes that makes the tooltip look a little better. We use a1 as a background and place the other two classes on top of it to make it look like they are in the same box.

And that's it, a [table turned into a tooltip](/files/table-tooltip/), another user is a little bit happier and all would be fine... Unless of course the user had left the channel before I could show him my solution. Damn.
