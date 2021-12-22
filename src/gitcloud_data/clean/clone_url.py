import re

def no_caps(clone_url):
    if clone_url is None:
        return None
    return clone_url.lower()

def ssh_to_https(clone_url):
    if clone_url is None or 'git@' not in clone_url:
        return clone_url
    clone_url = clone_url\
        .replace('ssh://', '')\
        .replace('git@', '')\
        .replace('.com:', '.com/')\
        .replace('https://', '')\
        .replace('.git', '')
    return f'https://{clone_url}.git'

def git_to_https(clone_url):
    if clone_url is None or 'git://' not in clone_url:
        return clone_url
    clone_url = clone_url\
        .replace('git://', '')\
        .replace('https://', '')\
        .replace('.git', '')
    return f'https://{clone_url}.git'

def check_valid_https_url(clone_url):
    if clone_url is None:
        return None
    return bool(re.match(r'https:\/\/[a-z]*\.com\/[a-z-]*\/[a-z-\.]*\.git', clone_url))

def check_git_owner(clone_url):
    if clone_url is None:
        return None
    if 'vikash-kothary' not in clone_url:
        print(clone_url)
        return False
    return True

if __name__ == '__main__':
    ssh_url = 'git://github.com/Cognifide/Maven-Vault-Checkout-Plugin.git'
    ssh_url = lower_letters_clone_url(ssh_url)
    print(git_to_https_clone_url(ssh_url))
