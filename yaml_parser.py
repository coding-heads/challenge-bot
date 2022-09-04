import yaml

with open('config.yaml', 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

admins = []
mods = []
restricted_users = []

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