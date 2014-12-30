#!/bin/bash -e

if [[ $# -ne 0 && $1 == prod ]]; then
	ngx_log=/var/log/nginx
	redis_store=/opt/redis
else
	ngx_log=$PWD/log/nginx
	redis_store=$PWD/data/redis
	mkdir -p $ngx_log $redis_store
fi

set -x

# Blog
docker run -d --name blog \
	-v $ngx_log:/var/log/nginx \
	abesto/blog

# Are you board?
docker run -d --name are-you-board-redis \
	-v $redis_store/are-you-board:/data \
	dockerfile/redis \
	redis-server --appendonly yes

docker run -d --name are-you-board \
	--link are-you-board-redis:redis \
	abesto/are-you-board

# HAProxy
docker run -d --name haproxy \
	-p 80:80 \
	--link blog:blog \
	--link are-you-board:are-you-board \
	 abesto/abesto-net-haproxy
