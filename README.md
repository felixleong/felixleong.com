# Hyde implementation of felixleong.com

Previously hosted as a Wordpress blog -- here's comes my Hyde implementation with static HTML generating goodness!

# Caveats

On a fresh instance, you'll need to execute `hyde gen` twice: the first execution will fail but the first-run will generate the blog tags HTML files,and hyde will be able to generate the site proper after that. 

# Credits and copyright notice

The theme in use is [Mainstream](http://www.woothemes.com/2009/07/mainstream/) by [WooThemes](http://www.woothemes.com/), with some theme elements are stripped away based on my usage.  

The current implementation is heavily referenced from [Steve Losh's](http://stevelosh.com/) work and I had lifted his Fabric deployment script.

# URL Structure

- / - The home page, currently just a simple landing page with my short bio
- /blog - Listing of the most recent blog posts
- /blog/[year]/[month]/[pagename].html - The blog post entries
- /blog/tags/[tagname] - The tag listing
- /blog/pages/[pageno] - Pagination of the listing page
- /blog/feed/ - ATOM feed of the blog
- /blog/feed/pages/[pageno] - Pagination for the feed
- /manga-tutorial/ - My tutorials on drawing manga
- /\*.html - Static pages
