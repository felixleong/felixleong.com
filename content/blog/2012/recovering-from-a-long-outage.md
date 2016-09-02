title: Recovering From A Long Outage
tags: announcements, programming, technical
date: 2012-01-12T00:43:08Z
category: Programming
featured_image: http://lh3.ggpht.com/-3TrMksQoH68/Tw2zM4UeOpI/AAAAAAAABUc/oVT6WR9vliA/Flickr-2522811650.jpg
featured_image_credit: The Clean Up! by One Hell Of A Loser, Flickr
featured_image_url: http://www.wylio.com/credits/flickr/2522811650

The whole ordeal started a month ago when my server decided to have temper tantrums and PHP and Nginx just mysteriously decided not to talk to each other again. And with that my Wordpress blogs are taken down with it.

Ouch.

Stress levels rising at an inopportune time when my workload was at an all time high. And it was additional salt rubbed on the injury as I was still scrambling to salvage deleted data from the only backup drive that I have. I totally don't want to get into specifics, it'd probably stress you out as well.

Then again, I've had enough dealing with PHP so that makes the perfect time to migrate my blog away from Wordpress to [Hyde](http://github.com/hyde/hyde) - a static site generator. Yes, you read me correctly, it generates flat HTML files with no database what-so-ever. No more battling with CMS features that I don't need (for a blog like mine, at least) and worrying about performance, caching and whether I remembered to make backups.

### The Gory Details

As much as I'm able to knock everything out within days, it's still a hard process to go through. Here's a list of things that I've done to illustrate the point:

- Restore the database and export the data using a local Wordpress instance *(easy, some hiccups along the way due to the base URL options)*
- Write a XML parser that converts the exported XML file into small files representing every blog posts and pages *(moderate, mostly just me learning [lxml](http://lxml.de) for the first time. You can [grab my script here](http://github.com/felixleong/wp2hyde))*
- Converting an existing [WooThemes template](http://demo.woothemes.com/?name=mainstream) that my old blog uses
- Working out the whole directory structure and baking in all the listings, tag pages and other what nots *(turns out this is the hardest part as Hyde's documentation is pretty bare. I've been referencing [Steve Losh's](http://github.com/sjl/stevelosh) implementation and do a lot of code reading to know where goes where)*
- Writing out the Nginx rewrite rules *(spent hours making it right)*
- Work out the deployment flow *(glad that Steve Losh has a perfectly working Fabric script for that)*

The result? [Everything that I've posted on Github](http://github.com/felixleong/felixleong.com). And the sweet part about it is that it acts as my backup :).

### What's Next?

I'll be doing more writing: the About Me page needs a complete overhaul (read: the current copy is so bad that I can't take it any longer) and I'm excited about writing a new version of it with a different twist. I will need to write the customary 2011 review post for my own reference and stating my plans for 2012.

And I wanted to tackle some of the harder issues head on this year and be more transparent about my stand on certain issues and what I observed and believed.

And yeah, it's going to be a very interesting 2012 all right.
