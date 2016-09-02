from markdown import Extension
from markdown.inlinepatterns import (
    IMAGE_LINK_RE,
    ImagePattern,
    dequote,
    handleAttributes,
    util)
from urllib.parse import urljoin
import re

import logging
logger = logging.getLogger('MARKDOWN')

LINK = r'\{(?P<img_loc>.+?)\}(?P<src>.*)'


class PelicanImagePattern(ImagePattern):
    LINK_RE = re.compile(LINK)

    def handleMatch(self, m):
        el = util.etree.Element("img")
        src_parts = m.group(9).split()
        if src_parts:
            src = src_parts[0]
            if src[0] == "<" and src[-1] == ">":
                src = src[1:-1]

            src = self.processSrc(src)
            el.set('src', self.sanitize_url(self.unescape(src)))
        else:
            el.set('src', "")
        if len(src_parts) > 1:
            el.set('title', dequote(self.unescape(" ".join(src_parts[1:]))))

        if self.markdown.enable_attributes:
            truealt = handleAttributes(m.group(2), el)
        else:
            truealt = m.group(2)

        el.set('alt', self.unescape(truealt))
        return el

    def processSrc(self, src):
        match = self.LINK_RE.match(src)
        if not match:
            return src

        img_loc = match.group('img_loc')
        if img_loc in self.config['mappings']:
            return urljoin(
                self.config['mappings'][img_loc], match.group('src'))

        return src


class PelicanImageExtension(Extension):
    DEFAULT_MAPPINGS = {}

    config = {
        'mappings': [
            DEFAULT_MAPPINGS,
            'A mapping of URL roots to be replaced'
        ]
    }

    def extendMarkdown(self, md, md_globals):
        """ Add an instance of FigcaptionProcessor to BlockParser. """
        pattern = PelicanImagePattern(IMAGE_LINK_RE, md)
        pattern.config = self.getConfigs()
        md.inlinePatterns.add('pelican_image', pattern, '<image_link')


def makeExtension(*args, **kwargs):
    return PelicanImageExtension(configs={'mappings': kwargs})
