# Pelican implementation of felixleong.com

The full [Pelican](https://github.com/pelican) implementation of my own personal website.

# History and Why Pelican?

Previously hosted as a Wordpress blog, then [Hyde](http://hyde.github.io/).

The main reason of switching away from Hyde is pretty much just a lack of Python 3 support and that older version of Hyde has the quirk where you'll have to execute the generation twice just to get the full site generated.

# URL Structure

- / - The home page
- /blog - Listing of the most recent blog posts
- /blog/[year]/[month]/[pagename].html - The blog post entries
- /tags/ - The tag listing
- /tags/[tagname] - List of blog posts with a specific tag
- /blog/pages/[pageno] - Pagination of the listing page
- /feed/ - ATOM and RSS feeds of the blog, currently supports both all posts and category feeds.
- /manga-tutorial/ - My tutorials on drawing manga
- /\*.html - Static pages
