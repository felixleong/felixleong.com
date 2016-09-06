title: CakePHP 1.2 Documentation in PDF
tags: cakephp, programming
date: 2009-08-27T13:51:19Z
category: Programming

Just recently looked into [CakePHP][cakephp] as well, as I find it to be one of the easier to use MVC frameworks for PHP and that [the manual][cakephpmanual] is really well written.

And, as usual, I do prefer to have offline documentation so I don't have to find myself paralysed when I'm developing on a computer without an Internet connection (which is also a good way to cut off distractions :-)). Luckily, CakePHP does offer such a means by [giving an option to view the whole manual in one page][cakephpmanualsp].

One gripe though: printing the page itself sucks: The text so small it's kind of unreadable and I couldn't tell the headings apart from the text. It's really annoying when I wanted a few printed pages so that I'd refer to them in some physical form (read up the tutorial while I'm on a train, for example).

So what I did is spend some time working on the print CSS and make it pretty enough to be readable and usable by my standards. As much as I wished the page numbers aren't that close to the bottom margin, well, it's Firefox's fault :p. The PDF is generated using [PrimoPDF][primopdf] and you can preview and download the manual from the [Scribd][scribd] applet below:

<iframe class="scribd_iframe_embed" src="https://www.scribd.com/embeds/19139908/content" scrolling="no" id="19139908" width="100%" height="500" frameborder="0"></iframe><script type="text/javascript">
(function() { var scribd = document.createElement("script"); scribd.type = "text/javascript"; scribd.async = true; scribd.src = "https://www.scribd.com/javascripts/embed_code/inject.js"; var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(scribd, s); })()
</script>

![CakePHP 1.2 Manual](http://www.scribd.com/doc/19139908/CakePHP-12-Manual)

Hope you'll find it useful!

[cakephp]: http://cakephp.org/
[cakephpmanual]: http://book.cakephp.org/
[cakephpmanualsp]: http://book.cakephp.org/complete/3
[primopdf]: http://www.primopdf.com/
[scribd]: http://scribd.com/
