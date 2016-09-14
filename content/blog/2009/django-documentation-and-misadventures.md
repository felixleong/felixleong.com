title: Django Documentation and Misadventures
tags: django, programming
date: 2009-08-01T22:18:16Z
category: Programming

Currently am learning [Django][django], which is a popular web framework in Python. And whichever framework I chose to learn, I greatly preferred having my documentation offline as I didn’t really find myself constantly offline (it helps to concentrate on my work, actually). In the case of Django, the documentation was provided in ReST text format (refer to the [FAQ entry][djfaq]) and it’s possible to generate a PDF version out of it.

… Well, until the fact that I found out that there’s no explicit mention on what to get to generate it.

Cutting a long story short (I'll save the grueling details to myself), now you’d two options:

1. [Download the PDF version here (Aug 1, 2009)][djpdf], which I generated from the recent Django 1.1 package
2. Do it yourself

For the brave ones that chose the Do-It-Yourself route, here’s the instructions for Ubuntu 9.04 (Jaunty Jackelope):


1. Get the following packages: texlive, texlive-latex-extra, python-setuptools[^1]

    #!bash
    sudo aptitude install texlive texlive-latex-extra python-setuptools

2. If you have python-sphinx package installed, uninstall it

    #!bash
    sudo aptitude remove python-sphinx

3. Install the latest Sphinx EGG package

    #!bash
    sudo easy_install -U Sphinx

4. Go to the “docs” directory Django package folder
5. Execute `make latex`
6. Once completed, go into the “\_build/latex” directory and execute `make all-pdf`

[**Django Documentation (Aug 1, 2009): PDF (Hosted at Box.net)**][djpdf]

[^1]: the TexLive/LaTeX stuff is over 150MB
[django]: http://www.djangoproject.com/
[djfaq]: http://docs.djangoproject.com/en/dev/faq/general/#how-can-i-download-the-django-documentation-to-read-it-offline
[djpdf]: http://www.box.net/shared/vo4fklk21i
