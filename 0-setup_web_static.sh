#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if ! [ -x "$(command -v nginx)" ]; then
	apt update -y
	apt install -y nginx
fi

if [ ! -d "/data" ]; then
	sudo mkdir /data
fi

if [ ! -d "/data/web_static" ]; then
	sudo mkdir /data/web_static
fi

if [ ! -d "/data/web_static/releases" ]; then
	sudo mkdir /data/web_static/releases
fi

if [ ! -d "/data/web_static/shared" ]; then
	sudo mkdir /data/web_static/shared
fi

if [ ! -d "/data/web_static/releases/test" ]; then
	sudo mkdir /data/web_static/releases/test
fi

echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>" | tee /data/web_static/releases/test/index.html

if [ -d "/data/web_static/current" ]; then
	rm -rf /data/web_static/current
	ln -s /data/web_static/releases/test/ /data/web_static/current
else
	ln -s /data/web_static/releases/test/ /data/web_static/current
fi

chown -R ubuntu:ubuntu /data
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
