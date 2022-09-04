import yaml

with open('config.yaml', 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

admins = []
mods = []
restricted_users = []
whitelist_domains = []
whitelist_languages = []

keys = []
for x in cfg['config']:
    if (cfg['config'][x] != None):
        if (len(cfg['config'][x]) > 0):
            keys.append(x)

values = []
for x in keys:
    values.append(cfg['config'][x])

if ('administrators' in keys):
    admins = values[keys.index('administrators')]

if ('moderators' in keys):
    mods = values[keys.index('moderators')]

if ('restricted_users' in keys):
    restricted_users = values[keys.index('restricted_users')]

if ('whitelist_domains' in keys):
    whitelist_domains = values[keys.index('whitelist_domains')]

if ('whitelist_languages' in keys):
    whitelist_languages = values[keys.index('whitelist_languages')]