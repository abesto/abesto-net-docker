#!/usr/bin/env python
import settings


def domain_routing():
    use_backend_tpl = 'use_backend {service}-bck if {service}-acl'
    lines = []
    for service in settings.services:
        lines += [host_acl(acl_name=service, subdomain=service, domain=domain)
                  for domain in settings.domains]
        if service in settings.aliases:
            lines += [host_acl(acl_name=service, subdomain=alias, domain=domain)
                      for domain in settings.domains
                      for alias in settings.aliases[service]
            ]
        lines += [use_backend_tpl.format(service=service), '']
    lines += [host_acl(acl_name=settings.toplevel_service, subdomain=None, domain=domain)
              for domain in settings.domains]
    lines += [use_backend_tpl.format(service=settings.toplevel_service)]
    return '\n'.join(indent(lines))


def my_domain_acl():
    return '\n'.join(indent([
        host_acl(acl_name='my-domain', subdomain=None, domain=domain, function='hdr_end')
        for domain in settings.domains]))

def backends():
    lines = []
    for service in settings.services + [settings.toplevel_service]:
        lines += ['backend {service}-bck'.format(service=service)]
        if service in settings.extra_backend_cfg:
            lines += indent(settings.extra_backend_cfg[service])
        lines += indent(['server {service}-srv {service}:80 weight 1 maxconn 1024 check'.format(service=service),
                         ''])
    return '\n'.join(lines)

def indent(lines):
    return ['    ' + line if len(line.strip()) > 0 else ''
            for line in lines]

def host_acl(acl_name, subdomain, domain, function='hdr'):
    retval = 'acl {service}-acl {function}(Host) -i '.format(service=acl_name, function=function)
    if subdomain is not None:
        retval += subdomain + '.'
    retval += domain
    return retval

if __name__ == '__main__':
    with open('haproxy.cfg.tpl', 'r') as f:
        cfg = f.read()

    with open('haproxy.cfg', 'w') as f:
        f.write(cfg.format(
            my_domain_acl=my_domain_acl(),
            domain_routing=domain_routing(),
            backends=backends()
        ))
