#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from
    the contents of the web_static folder.
"""
from fabric.api import local, env, put, run
from datetime import datetime
import os

env.hosts = ['52.87.255.240', '52.86.177.0']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """ Generates .tgz archive """
    try:
        local("mkdir -p versions")

        now = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "web_static_{}.tgz".format(now)

        local(f"tar -cvzf versions/{name} web_static/")

        return f"versions/{name}"
    except Exception:
        return None


def do_deploy(archive_path):
    """ Distributes archive to web server """
    if not os.path.exists(archive_path):
        return False

    try:
        fname = os.path.basename(archive_path)
        name = fname.replace('.tgz', '')
        path = f"/data/web_static/releases/{name}/"

        # load archive to server
        put(archive_path, '/tmp/')

        # create new path without .tgz extension
        run(f"mkdir -p {path}")

        # extract archive content to the new path
        run(f"tar -xzf /tmp/{fname} -C {path}")

        # remove archive
        run(f"rm /tmp/{fname}")

        # move files to correct location
        run(f"mv {path}web_static/* {path}")

        # remove web_static folder
        run(f"rm -rf {path}web_static")

        # remove symbolic link current
        run('rm -rf /data/web_static/current')

        # update symbolic link
        run(f"ln -s {path} /data/web_static/current")

        return True
    except Exception:
        return False


def deploy():
    """ Creates and distributes an archive to web servers """
    archive_path = do_pack()
    if not archive_path or not os.path.isfile(archive_path):
        return False
    return do_deploy(archive_path)
