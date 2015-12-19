global
    tune.ssl.default-dh-param 2048

defaults
    mode http
    timeout server 5000
    timeout connect 1000

frontend all-frn
    bind 0.0.0.0:80
    bind 0.0.0.0:443 ssl crt /cert.pem
    redirect scheme https if !{{ ssl_fc }}

    # The huge timeout is so that websocket connections can go through haproxy
    # In the future websocket connections should go through a separate port,
    # directly to the appropriate application
    timeout client 86400000

{my_domain_acl}
    use_backend not-my-domain-bck if ! my-domain-acl

    # http://www.gnuterrypratchett.com/
    http-response set-header X-Clacks-Overhead GNU\ Terry\ Pratchett

{domain_routing}

{backends}

backend not-my-domain-bck
    errorfile 503 /usr/local/etc/haproxy/unknown-domain.html
