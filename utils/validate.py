from utils.yaml_parser import whitelist_domains, whitelist_languages, admins, mods, restricted_users
import discord
import re
import tldextract

def validate_url(url):
    if len(url.split()) > 1:
        # Error (invalid command)
        return False
    x = re.search('^https://{1}\S*$', url)
    if x:
        ext = tldextract.extract(url)
        if ext.domain not in whitelist_domains:
            # Error (invalid url)
            return False
        return True

def validate_langs(langs):
    if len(langs) > len(whitelist_languages):
        # Error (invalid command)
        return False
    else:
        for x in langs:
            if x not in whitelist_languages:
                # Error (invalid lang)
                return False
        return True

def validate_staff(interaction: discord.Interaction):
    if str(interaction.user.id) in restricted_users:
        return False
    if str(interaction.user.id) in admins or str(interaction.user.id) in mods:
        return True
    for x in interaction.user.roles:
        if str(x.id) in admins or str(x.id) in mods:
            return True
    return False