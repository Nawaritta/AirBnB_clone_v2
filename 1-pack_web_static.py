#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""


import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive"""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(time)
    try:
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return ("versions/{}".format(archive_name))
    except Exception as e:
        return None
