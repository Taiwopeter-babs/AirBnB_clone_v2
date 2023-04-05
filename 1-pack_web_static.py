#!/usr/bin/python3
"""
This module contains a function that compresses a folder (web_static)
into .tgz format for deployment to Nginx servers
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """This functions compresses a folder"""

    local("mkdir -p versions")

    # set the date format of the file version
    format = "%Y%m%d%H%M%S"
    file_date = datetime.now().strftime(format)

    # create the compressed file
    compressed_file = "versions/web_static_{}.tgz".format(file_date)
    to_compress = "web_static/"

    tar_command = "tar -cvzf {} {}".format(compressed_file, to_compress)
    out_result = local(tar_command)

    if out_result.return_code == 0:
        out_dir = "{}".format(compressed_file)
        return out_dir

    return None
