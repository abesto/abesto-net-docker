#!/bin/bash
repos='dockerfile/redis dockerfile/haproxy abesto/blog abesto/abesto-net-haproxy'
for repo in $repos; do
	docker pull $repo
done
