from yaml_parser import whitelist_domains, whitelist_languages
import tldextract
import re

def validateUrl(url):
    # verify url
    if len(url.split()) > 1:
        # Error (invalid command)
        return False
    else:
        x = re.search('^https://{1}\S*$', url)
        if x:
            ext = tldextract.extract(url)
            if ext.domain not in whitelist_domains:
                # Error (invalid url)
                return False
            else:
                return True

def validateLangs(langs):