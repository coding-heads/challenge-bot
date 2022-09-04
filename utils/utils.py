from yaml_parser import whitelist_domains, whitelist_languages
import tldextract
import re

def validateUrl(url):
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

def validateLangs(langs):
    if len(langs) > len(whitelist_languages):
        # Error (invalid command)
        return False
    else:
        for x in langs:
            if x not in whitelist_languages:
                # Error (invalid lang)
                return False
        return True