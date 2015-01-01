#!/bin/bash
repos='dockerfile/redis dockerfile/haproxy abesto/blog abesto/abesto-net-haproxy abesto/are-you-board abesto/mastermind abesto/algo'
for repo in $repos; do
	docker pull $repo
done
