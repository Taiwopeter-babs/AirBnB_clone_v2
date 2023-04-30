#!/usr/bin/python3
"""
    This module contains a function that compresses a folder (web_static)
    into .tgz format for deployment to Nginx servers
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ["18.235.234.96", "52.87.216.23"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


@runs_once
def do_pack():
    """This function compresses a folder"""

    local("mkdir -p versions")

    # set the date format of the file version
    format = "%Y%m%d%H%M%S"
    file_date = datetime.now().strftime(format)

    # create the compressed file
    compressed_file = "versions/web_static_{}.tgz".format(file_date)
    to_compress = "web_static/"

    tar_command = "tar -cvzf {} {}".format(compressed_file, to_compress)
    out_result = local(tar_command)

    if not out_result.failed:
        out_dir = "{}".format(compressed_file)
        return out_dir

    return None


def do_deploy(archive_path):
    """This function deploys the compressed file to remote servers
    and processes them

    Args:
        archive_path(str): path to the archive file to be deployed
    Returns:
        True if the deployment succeeds, otherwise False
    """

    archive_file = archive_path.split("/")[1]
    archive_folder = archive_path.split("/")[1].split(".")[0]
    new_release = "/data/web_static/releases/{}".format(archive_folder)

    # check if archive path is available
    if not os.path.exists(archive_path):
        return False

    # upload the archive
    upload = put(archive_path, "/tmp/")
    if upload.failed:
        return False

    # create a directory to which to save the uncompressed files
    create_dir = "sudo mkdir -p {}".format(new_release)
    res = run(create_dir)
    if res.failed:
        return False

    # uncompress the archive file to the new_release directory
    uncompress = "sudo tar -xzf /tmp/{} -C {}".format(archive_file,
                                                      new_release)
    result = run(uncompress)
    if result.failed:
        return False

    # move the uncompressed files into the web_static_date directory
    move = "sudo mv {}/web_static/* {}".format(new_release,
                                               new_release)
    result = run(move)
    if result.failed:
        return False

    # delete the empty folder
    run("sudo rm -rf {}/web_static".format(new_release))

    # delete the compressed file
    delete = "sudo rm /tmp/{}".format(archive_file)
    result = run(delete)
    if result.failed:
        return False

    # delete the symbolic link
    result = run("sudo rm -rf /data/web_static/current")
    if result.failed:
        return False

    # create a new symbolic link
    create_link = "sudo ln -s {} /data/web_static/current".format(new_release)
    result = run(create_link)
    if result.failed:
        return False

    print("New version deployed")

    return True
