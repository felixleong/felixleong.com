from fabric.api import *
import os
import fabric.contrib.project as project

PROD = 'sl'
DEST_PATH = '/var/www/stevelosh.com/'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'deploy')

def clean():
    local('rm -rf ./deploy')

def generate(type='development'):
    local('sed -e \'s/\(mode: \).*/\\1{0}/g\' -i \'\' site.yaml'.format(type))
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
