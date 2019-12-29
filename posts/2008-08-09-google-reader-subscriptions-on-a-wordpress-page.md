---
author: Emil Stenström
categories:
- Other
date: 2008-08-09 17:09:43
guid: http://friendlybit.com/?p=194
id: 194
permalink: /other/google-reader-subscriptions-on-a-wordpress-page/
title: Google Reader subscriptions on a WordPress Page
---

Instead of posting new lists of blogs I follow over and over again I thought I'd make a permanent place for them. So I just **exported all of the blogs I follow** from Google Reader (Settings -> Import/Export) and **imported them to WordPress** (Write -> Links -> Import Links (in the sidebar)). [OPML](http://en.wikipedia.org/wiki/OPML) is a great format!

Then I created a [WordPress Page template](http://codex.wordpress.org/Pages#Page_Templates) that simply printed the content of that page **followed by all my imported links**. This following is the code needed (as a file called links.php in your template directory):

```php
<?php
// Template Name: Links
?>
<?php get_header(); ?>
<div id="content">
  <?php while (have_posts()) : the_post(); ?>
    <div class="post" id="post-<?php the_ID(); ?>">
      <h1><?php the_title(); ?></h1>
      <div class="entry">
        <?php the_content(); ?>
        <?php wp_list_bookmarks(); ?>
      </div>
    </div>
  <?php endwhile; ?>
</div>
<?php get_sidebar(); ?>
<?php get_footer(); ?>
```

Now just create a new page, and select the Page Template "Links" at the bottom. Fill out a page title and an introduction text and press Save. Voilá!

The final touches was adding two new categories, "Blogs I follow" in English and Swedish, moving all links to one of those, and removing everything not related to web development or media. Some bastards also both have great blogs and are my friends, so I removed some duplicates too.
