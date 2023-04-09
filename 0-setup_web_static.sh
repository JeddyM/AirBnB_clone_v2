#!/usr/bin/env bash
#Bash script that sets up web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Lets do this" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/

#Giving ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

#Update the Nginx configuration to serve the content of
#/data/web_static/current/ to hbnb_static
printf %s "server {
        listen 80;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root   /var/www/html;
        index  index.html index.htm;

        location /hbnb_static/{
                alias /data/web_static/current;
        }

        error_page 404 /404.html;
        location /404 {
            root /var/www/html/404.html;
            internal;
        }
}" > /etc/nginx/sites-available/default
service nginx restart
