#!/bin/bash
# Compares a url as served by the old (non-docker) and the new (dockerized) abesto.net
# Usage: diff.sh domain [path]
# Example: diff.sh board.abesto.net /

old_ip=176.58.112.96
new_ip=45.56.90.109

host=$1
path=$2
vimdiff <(curl $old_ip/$path -H "Host: $host") <(curl $new_ip/$path -H "Host: $host")
