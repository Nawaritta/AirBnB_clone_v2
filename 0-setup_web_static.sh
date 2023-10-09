#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo aapt-get update
sudo apt-get install -y nginx

# Create the folders if they don’t already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Index file 
echo "AirBnB clone" | sudo tee /data/web_static/releases/test/index.html

# Create the symbolic link 
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Update the Nginx configuration 
sudo sed -i '/server_name _;/a location /hbnb_static {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default

# restart nginx
service nginx restart
