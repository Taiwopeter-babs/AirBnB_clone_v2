#!/usr/bin/python3
"""
This module contains a function that compresses a folder (web_static)
into .tgz format for deployment to Nginx servers
"""
from fabric.api import *
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = ["18.235.234.96", "52.87.216.23"]

env.key_filename = "~/.ssh/id_rsa"


def do_pack() -> str:
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


def do_deploy(archive_path) -> bool:
    """This function deploys the compressed file to remote servers"""
    archive_file = archive_path.split("/")[1]
    archive_folder = archive_path.split("/")[1].split(".")[0]
    new_release_dir = f"/data/web_static/releases/{archive_folder}"

    # check if archive path is available
    if not os.path.exists(archive_path):
        return False

    # upload the archive
    upload = put(archive_path, "/tmp/")
    if upload.failed:
        return False

    # create a directory to which to save the uncompressed files
    create_dir = f"sudo mkdir -p {new_release_dir}"
    res = run(create_dir)
    if res.failed:
        return False

    # uncompress the archive file to the new_release directory
    uncompress = f"sudo tar -xzf /tmp/{archive_file} -C {new_release_dir}"
    result = run(uncompress)
    if result.failed:
        return False

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
    create_link = f"sudo ln -s {new_release_dir} /data/web_static/current"
    result = run(create_link)
    if result.failed:
        return False

    print("New version deployed")

    return True
