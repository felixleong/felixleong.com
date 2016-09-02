# coding: utf-8
"""
Unicode Emojis for Python-Markdown
==================================

Converts defined emoticon symbols to Unicode emojis, supported on a
variety of devices [1].

[1]: http://apps.timwhitlock.info/emoji/tables/unicode#block-1-emoticons

Usage:

    >>> from __future__ import print_function
    >>> from markdown import markdown
    >>> text = 'I <3 you! Just kidding. :P'
    >>> print(markdown(text, ['unimoji']))    # doctest: +NORMALIZE_WHITESPACE
    <p>I <span class="emoji" style="color:red">❤</span> you! \
    Just kidding. <span class="emoji">😛</span></p>

**NOTE**: The emojis are only replaced when whitespace-delimited on both sides!

The following options are accepted:

 - `emoji`, the emoticon-to-list-of-aliases mapping,
 - `span_class`, the class name of the encompassing `<span>` element
   (default: 'emoji'). No element is created if `None`.

An example with these custom settings:

    >>> from mdx_unimoji import UnimojiExtension
    >>> img_heart = '<img alt="love" src="heart.png"/>'
    >>> img_tongue = '<img alt=":P" src="tongue.png"/>'
    >>> overrides = UnimojiExtension.EMOJI
    >>> overrides.update({img_heart: ['<3'],
    ...                   img_tongue: ':p :P :-p :-P'.split()})
    >>> print(markdown(text,
    ...                extensions=[UnimojiExtension(span_class='other',
    ...                                             emoji=overrides)]))
    ... # doctest: +NORMALIZE_WHITESPACE
    <p>I <img alt="love" class="other" src="heart.png" /> you! \
    Just kidding. <img alt=":P" class="other" src="tongue.png" /></p>

You can use the `span_class` value in your CSS, e.g.:

    .emoji {
        font-family: "Apple Color Emoji", "Segoe UI Emoji",
                     "Noto Color Emoji", EmojiSymbols, "DejaVu Sans", Symbola;
    }

HF!

"""
from __future__ import unicode_literals
from markdown import Extension
from markdown.util import etree
from markdown.inlinepatterns import Pattern

class UnimojiExtension(Extension):
    EMOJI = {
        '😊': ':) :-) :] :-] =) =] ^^ ^_^ ☺'.split(),
        '😉': ';) ;-) ;] ;-]'.split(),
        '😄': ':D :-D =D'.split(),
        '😂': ":,D :'D =,D ='D".split(),
        '😆': 'xD XD'.split(),
        '😛': ':p :-p :P :-P =p =P'.split(),
        '😜': ';p ;-p ;P ;-P'.split(),
        '😏': ':> :->'.split(),
        '😞': ':( :-( ;( ;-( =( =[ ☹'.split(),
        '😣': 'x( X('.split(),
        '😢': ":,( :'( =,( ='(".split(),
        '😠': '>:( >=('.split(),
        '😲': ':O :-O 8-O =O'.split(),
        '😵': 'x-O X-O'.split(),
        '😳': ':$ :-$ :">'.split(),
        '😴': ':zzz:'.split(),
        '😓': ':-X :X :-# :# :-& :&'.split(),
        '😇': 'O:) O:-)'.split(),
        '😈': '3:) 3:-) >:) >:-) >;) >;-)'.split(),
        '😎': '8)'.split(),
        '😖': ':s :-s :S :-S'.split(),
        '😒': ':/ :-/ :\\ :-\\ =/ =\\ :L'.split(),
        '😚': ':* :-*'.split(),
        '😘': ';* ;-*'.split(),
        '❤': '<3'.split(),
        '💔': '</3'.split(),
        '👍': ':y: :Y: :+1:'.split(),
        '👎': ':n: :N: :-1:'.split(),
        '🙌': '\\o/'.split(),
        '🍰': ':cake:'.split(),
        '😸': ':^) :} :-} :3 :-3'.split(),
        '😺': ':^D =^D'.split(),
        '😿': ':^( :{'.split(),
    }
    STYLES = {
        '❤': 'color:red',
        '💔': 'color:red',
        '🍰': 'color:maroon',
    }
    config = {
        'emoji': [
            EMOJI,
            'A mapping from emoticon symbols to a list of aliases.'
        ],
        'styles': [
            STYLES,
            'A mapping from emoticon symbol to a CSS style string. '
            'Only works if span_class is enabled.'
        ],
        'span_class': [
            'emoji',
            'A CSS class (default: "emoji") for the emoticons-encompassing'
            '<span>. Disabled if None.'
        ],
    }

    def __init__ (self, *args, **kwargs):
        super(UnimojiExtension, self).__init__(*args, **kwargs)
        # Set keys as aliases so they get processed the same
        for k, v in self.getConfig('emoji').items(): v.append(k)
        # Inverse the emoji mapping
        aliases = {}
        for emoticon, alias in self.getConfig('emoji').items():
            for a in alias:
                aliases[a] = emoticon
        self.config['aliases'] = [aliases, '']

    def extendMarkdown(self, md, md_globals):
        import re
        RE = r'((?<=\s)|(?<=^))(?P<emoticon>%s)(?=\s|$)' % '|'.join(map(re.escape, self.getConfig('aliases')))
        md.inlinePatterns['emoji'] = UnimojiPattern(RE, md, self)


class UnimojiPattern(Pattern):
    def __init__ (self, pattern, md, extension):
        super(UnimojiPattern, self).__init__(pattern, md)
        self.ext = extension

    def handleMatch(self, m):
        # Get the preferred Unicode emoticon, or override
        emoticon = self.ext.getConfig('aliases')[m.group('emoticon')]
        # Try to parse it as HTML in case it's overriden
        try: element = etree.fromstring(emoticon.encode('utf-8'))
        except etree.ParseError:
            pass
        # Apply class name if needed
        span_class = self.ext.getConfig('span_class')
        if span_class:
            try: element
            except NameError:
                element = etree.Element('span')
                element.text = emoticon
            element.set('class', span_class)
            # Apply style formatting
            style = self.ext.getConfig('styles').get(emoticon)
            if style: element.set('style', style)
        try:
            return element
        except NameError:
            return emoticon


def makeExtension(*args, **kwargs):
    return UnimojiExtension(*args, **kwargs)


if __name__ == '__main__':
    import doctest; doctest.testmod()
