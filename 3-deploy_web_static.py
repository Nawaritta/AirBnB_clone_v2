#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates 
and distributes an archive to your web servers, using the function deploy
"""

from fabric.api import env, local, run, put
from os.path import exists
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ["54.164.126.155", "54.237.40.94"]
env.key_filename = "~/id_rsa"

def do_pack():
    """
    Create a compressed archive of the web_static directory.
    """
    try:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_name = 'versions/web_static_{}.tgz'.format(timestamp)
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(archive_name))
        return archive_name
    except Exception:
        return None

def do_deploy(archive_path):
    """
    Deploy an archive to web servers.
    """
    if not exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split("/")[-1]
        base = archive_filename.split(".")[0]

        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(base))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_filename, base))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(base, base))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(base))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(base))
        return True
    except Exception:
        return False

def deploy():
    """
    Create and distribute an archive to web servers using do_pack and do_deploy.

    Returns:
           True if deployment is successful, False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
