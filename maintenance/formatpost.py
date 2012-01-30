#! /usr/bin/env python

from datetime import datetime
import os
import os.path as op
import sys
from slugify import slugify

CONTENT_DIR = 'content/blog'

def generate_post(filename, title, created_on, tags, content_file):
    """Generate the post for Hyde"""

    # Confirm the override if the file exists
    if op.isfile(content_file):
        confirm = raw_input('File exists. Overwrite? (y/n) ').upper()
        if confirm != 'Y' or confirm != 'YES':
            return

    # Create the necessary directory if it doesn't exists
    dir_name = op.dirname(content_file)
    if not op.isdir(dir_name):
        print 'Dir name', dir_name
        os.makedirs(dir_name, 0755)

    # Read the contents out
    fhdl = open(filename, 'r')
    if not fhdl:
        print >> sys.stderr, 'ERROR: Cannot find {0}'.format(filename)
        sys.exit(1)
    content = fhdl.read()

    # Print the Hyde output
    fhdl = open(content_file, 'w')
    if not fhdl:
        print >> sys.stderr, 'ERROR: Cannot write to {0}'.format(filename)
        sys.exit(1)

    fhdl.write('---\n')
    fhdl.write('title: {0}\n'.format(title))
    fhdl.write('created: !!timestamp "{0}"\n'.format(created_on))
    if tags:
        fhdl.write('tags:\n')
        for tag in tags:
            fhdl.write('    - {0}\n'.format(tag))
    fhdl.write('---\n\n')
    fhdl.write('{% mark post %}')
    fhdl.write(content)
    fhdl.write('{% endmark %}\n')


# MAIN LINE
if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        if not op.isfile(filename):
            print >> sys.stderr, 'ERROR: Cannot find {0}'.format(filename)
            sys.exit(1)

        if not op.isdir(CONTENT_DIR):
            print >> sys.stderr, 'ERROR: Cannot find the content directory'
            sys.exit(1)

        # Retrieve the title and list of tags for the post
        title = raw_input('Enter the title of the post: ')
        tags_list = raw_input('Enter the list of tags: ')

        tags = [ slugify(unicode(x).strip())
                for x in tags_list.split(',') if x ]
        print 'title:', title
        print 'tags:', tags

        # Get the creation time
        created = datetime.now()
        created_year = created.year
        created_month = str(created.month).zfill(2)
        created_on = created.strftime('%Y-%m-%d %H:%M:%S')

        # Generate the file
        post_filename = u'{0}/{1}/{2}/{3}.html'.format(
                CONTENT_DIR, created_year, created_month, slugify(unicode(title)))
        generate_post(filename, title, created_on, tags, post_filename)
        print 'Blog post created as', post_filename
