import yaml

with open('config.yaml', 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

print(cfg['config'])

admins = []
mods = []
restricted_users = []

# Get all keys from YAML
keys = []
for x in cfg['config']:
    if (cfg['config'][x] != None):
        if (len(cfg['config'][x]) > 0):
            keys.append(x)

print(keys)

# Get all values from YAML
values = []
for x in keys:
    values.append(cfg['config'][x])

print(values)

# 
if ('roles' in keys):
    roles = values[keys.index('roles')]
    print(roles)