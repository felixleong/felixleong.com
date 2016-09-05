title: Fear.Less Magazine – May 2011 Issue on EPUB and Kindle
tags: ebook, fearless, projects, tech
date: 2011-05-21T17:09:32Z
category: Programming
featured_image: images/2011/05/cover-300x231.jpg
featured_image_credit: Fear.Less May 2011 Cover
featured_image_url: http://fearlessstories.com/

For the longest time, I'm curious of how e-books are created – and wondered how much effort does it take to create one.

So to satisfy my curiosity, I took the latest issue of [Fear.Less magazine][fearless] and worked on it, since I hate reading PDFs from Kindle (it's a totally horrible experience). Since [Calibre][calibre] did a horrible job in converting it (due to the complex layout), I used the output from Calibre and worked everything by hand. And here's the end results!

#### Download the magazine for:

- [Kindle (MOBI format) - 3MB](http://www.mediafire.com/file/zbizw1smaa6ex1d/Fear.less%20-%20May%202011%20-%20Fear.less.mobi)
- [iPhone/iPad/Nook/Kobo/etc. (EPUB format) - 3MB](http://www.mediafire.com/file/fy3igcb3c27jpy7/Fear.less%20-%20May%202011%20-%20Fear.less.epub)

## On creating the e-book

For starters, EPUB is indeed a glorified zip file with HTML, CSS, images and some metadata files. And since it's HTML, it's all about learning the quirks and limitation of what a device would support. For the most part, I stuck to using very rudimentary HTML without fancy markups. All I did is to make sure that I use the correct semantics so to make it easier to style.

When it come to tools, I used Calibre for conversion, Sigil for WYSIWYG editing, VIM for all the heavy-lifting and cleanup and ImageMagick to batch covert all images. I also relied on Mac's Preview to extract the ads out so that I can slap them in the final EPUB. Bliss.

The only part I find to be extremely laborious is to copy and paste text from the PDF and deal with a whole can of worms in formatting, which involves everything removing   (HTML blankspaces), handling abrupt line-breaks, getting rid of HTML cruft and hypen-breaks and other annoying stuff. At times like this, I do wish for a pure text file of the manuscript.

What I totally love is that the conversion from EPUB to MOBI (which Kindle supports) is straightforward and both formats looks identical. That means less headache for me to work out the differences.

So yeah, it's really hard work to get a good e-book output and am glad to be able to read it on my Kindle! :)

By the way, do yourself a favour and subscribe to [Fear.Less][fearless], **it's free!**

[fearless]: http://fearlessstories.com/
[calibre]: http://calibre-ebook.com/
