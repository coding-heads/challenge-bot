import yaml

with open('config.yaml', 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

print(cfg['config'])