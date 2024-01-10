#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

if ! [ -x "$(command -v nginx)" ];
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html><head></head><body>Testing</body></html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

sed -i "35i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

service nginx restart
exit 0
