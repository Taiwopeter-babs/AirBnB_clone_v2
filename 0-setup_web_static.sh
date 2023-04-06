#!/usr/bin/env bash
# This script configures a Nginx server to create directories
#+ and files to serve static content

sudo apt-get -y update
sudo apt-get -y install nginx
# creates the directories if they don't exist
sudo mkdir -p /data/web_static/{releases/"test",shared}

# create a test html file
if [[ ! -e /data/web_static/releases/test/index.html ]]
then
	echo "Test content" | sudo tee -a /data/web_static/releases/"test"/index.html > /dev/null
fi

# check if symbolic link exists, and remove it
if [[ -L /data/web_static/current ]]
then
	sudo rm /data/web_static/current
fi

# create the symbolic link
sudo ln -s /data/web_static/releases/"test" /data/web_static/current

# change owner and group
sudo chown -R ubuntu:ubuntu /data

# configure location block to serve content requested from a URI
sudo sed -i "40i \\\tlocation \/hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-enabled/default

# restart the server
sudo service nginx restart
