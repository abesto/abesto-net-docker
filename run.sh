#!/bin/bash

if [ $1 == 'prod' ]; then
	ngx_log=/var/log/nginx
else
	ngx_log=log/ngx
fi

docker run -d --name blog abesto/blog
docker run -d --name haproxy -p 80:80 --link blog:blog -v$ngx_log:/var/log/nginx abesto/abesto-net-haproxy
