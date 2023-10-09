#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""
import os
from fabric.api import *

env.hosts = ["54.237.40.94", "54.164.126.155"]


def do_clean(number=0):
    """
    Delete out-of-date archives.
    """
    if int(number) == 0:
        number_to_keep = 1
    else:
        number_to_keep = int(number)

    local_archive_dir = "versions"
    local_archives = sorted(os.listdir(local_archive_dir))
    for _ in range(len(local_archives) - number_to_keep):
        archive_to_delete = local_archives.pop(0)
        local("rm -f {}/{}".format(local_archive_dir, archive_to_delete))

    remote_archive_dir = "/data/web_static/releases"
    with cd(remote_archive_dir):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        for _ in range(len(remote_archives) - number_to_keep):
            archive_to_delete = remote_archives.pop(0)
            run("rm -rf {}/{}".format(remote_archive_dir, archive_to_delete))
