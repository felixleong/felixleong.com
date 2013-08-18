import os.path as op
from fabric.api import env, hosts, local
import fabric.contrib.project as project

env.use_ssh_config = True

PROD = []  # Set up the SSH URL settings here
DEST_PATH = '/var/www/website/'
ROOT_PATH = op.abspath(op.dirname(__file__))
DEPLOY_PATH = op.join(ROOT_PATH, 'deploy')
IMG_PATH = '/var/www/website/deploy/media/'


def clean():
    local('rm -rf ./deploy')


def generate(type='development', gen_dir=None):
    gen_cmd = 'hyde gen'
    if isinstance(gen_dir, str) and op.isdir(gen_dir):
        gen_cmd = '{0} -d {1}'.format(gen_cmd, gen_dir)

    local('sed -e \'s/\(mode: \).*/\\1{0}/g\' -i\'\' site.yaml'.format(type))
    local(gen_cmd)


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
        extra_opts="--checksum",
        delete=True
    )
