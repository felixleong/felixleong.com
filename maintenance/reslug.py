from fnmatch import fnmatch
import os, os.path
import urllib
from HTMLParser import HTMLParser
from slugify import slugify

def print_fnmatches(pattern, dir, files):
    parser = HTMLParser()
    for filename in files:
        if fnmatch(filename, pattern):
            (orig_fn, ext) = os.path.splitext(filename)

            unquote_fn = urllib.unquote(orig_fn).decode('utf-8')
            unescaped_fn = parser.unescape(unquote_fn)
            new_slug = slugify(unescaped_fn).strip('-')

            new_fn = '{0}{1}'.format(new_slug, ext)

            old_path = os.path.join(dir, filename)
            new_path = os.path.join(dir, new_fn)
            os.rename(old_path, new_path)

            print os.path.join(dir, new_fn)

os.path.walk('content/blog', print_fnmatches, '*%*.html')
