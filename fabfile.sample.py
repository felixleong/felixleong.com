import os
import op as op
import sys
from fabric.api import *
import fabric.contrib.project as project

PROD = [ ]  # Set up the SSH URL settings here
DEST_PATH = '/var/www/website/'
ROOT_PATH = op.abspath(op.dirname(__file__))
DEPLOY_PATH = op.join(ROOT_PATH, 'deploy')
IMG_PATH = '/var/www/website/deploy/media/'

def clean():
    local('rm -rf ./deploy')

def generate(type='development'):
    local('sed -e \'s/\(mode: \).*/\\1{0}/g\' -i\'\' site.yaml'.format(type))
    local('hyde gen')

def regen(type='development'):
    clean()
    generate(type)

def serve():
    local('hyde serve')

def reserve():
    regen()
    serve()

def smush():
    local('smusher ./media/images')

@hosts(PROD)
def publish():
    regen('production')
    project.rsync_project(
        remote_dir=DEST_PATH,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )

@hosts(PROD)
def uploadimage(filename):
    if not op.isfile(filename):
        print >> sys.stderr, 'ERROR: File does not exists'
        return

    today = datetime.now()
    upload_dir= op.join(IMG_PATH, '{0}/{1}/'.format(today.year, today.month))
    upload_file = op.join(upload_dir, op.basename(filename))
    mkdir_cmd = 'mkdir -p {0}'.format(upload_dir)

    run(mkdir_cmd)
    put(filename, upload_dir)
