#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ["54.237.40.94", "54.164.126.155"]
env.key_filename = "~/id_rsa"


def do_deploy(archive_path):
    """
    distributes and deploy an archive
    """
    if not os.path.exists(archive_path):
        return False
    try:
        archive_filename = os.path.basename(archive_path)
        base = os.path.splitext(archive_filename)[0]
        put(archive_path, '/tmp/')
        release_directory = "/data/web_static/releases/{}".format(base)
        sudo('mkdir -p {}'.format(release_directory))
        sudo('tar -xzf /tmp/{} -C {}/'.format(archive_filename, release_directory))
        sudo('rm /tmp/{}'.format(archive_filename))
        sudo('mv {}/web_static/* {}/'.format(release_directory, release_directory))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {} "/data/web_static/current"'.format(release_directory))
        
        return True
    except Exception as e:
        return False
