import settings
import copy

domains = copy.copy(settings.domains)

for domain in settings.domains:
    for service in settings.services:
        domains.append(service + '.' + domain)
    for aliases in settings.aliases.values():
        for alias in aliases:
            domains.append(alias + '.' + domain)

print ' '.join(domains)
