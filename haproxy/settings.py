#!/usr/bin/env python

domains = ['abesto.net', 'abesto.tech']
toplevel_service = 'blog'
services = ['board', 'mastermind', 'algo', 'lychee', 'static']
aliases = {
    'static': ['releases']
}
extra_backend_cfg = {
    'board': [
        '# The huge timeout is so that websocket connections can go through haproxy',
        '# In the future websocket connections should go through a separate port,',
        '# directly to the appropriate application',
        'timeout queue 5000',
        'timeout server 86400000',
        'timeout connect 86400000'
    ]
}
