import os
import glob
from pprint import pprint
from git import Repo as Git


def get_client():
    workspace = './workspace'
    local_repos = dict()
    for path in glob.glob('workspace/*/*'):
        if os.path.isdir(f'{path}/.git'):
            local_repos[path] = Git(path)
        else:
            local_repos[path] = None
    return local_repos


def get_count(client):
    return len(client)

# def get_name(client, repo):
#     return client[repo]

def get_clone_url(client, path):
    if len(client[path].remotes) == 1:
        return client[path].remotes[0].url
    elif 'origin' in client[path].remotes:
        return client[path].remotes['origin'].url
    else:
        print(f'{path}: {client[path].remotes}')
        return None

def is_dirty_repo(client, path):
    return client[path].is_dirty()

if __name__ == '__main__':
    client = get_client()
#     get_count(client)

def get_client():
    workspace = './workspace'
    local_repos = dict()
    for path in glob.glob(f'{workspace}/*/*'):
        if os.path.isdir(f'{path}/.git'):
            local_repos[path] = Git(path)
        else:
            local_repos[path] = None
    return local_repos

def get_count(client):
    return len(client)

# def get_name(client, repo):
#     return client[repo]

def get_clone_url(client, path):
    if len(client[path].remotes) == 1:
        return client[path].remotes[0].url
    elif 'origin' in client[path].remotes:
        return client[path].remotes['origin'].url
    else:
        print(f'{path}: {client[path].remotes}')
        return None

def is_dirty_repo(client, path):
    return client[path].is_dirty()

if __name__ == '__main__':
    client = get_client()
#     get_count(client)

def get_client():
    workspace = './workspace'
    local_repos = dict()
    for path in glob.glob(f'{workspace}/*/*'):
        if os.path.isdir(f'{path}/.git'):
            local_repos[path] = Git(path)
        elif os.path.isdir(path):
            local_repos[path] = None
    return local_repos

def get_count(client):
    return len(client)

# def get_name(client, repo):
#     return client[repo]

def get_clone_url(client, path):
    if len(client[path].remotes) == 1:
        return client[path].remotes[0].url
    elif 'origin' in client[path].remotes:
        return client[path].remotes['origin'].url
    else:
        print(f'{path}: {client[path].remotes}')
        return None

def is_dirty_repo(client, path):
    return client[path].is_dirty()

if __name__ == '__main__':
    client = get_client()
#     get_count(client)

def get_client():
    workspace = './workspace'
    local_repos = dict()
    for path in glob.glob(f'{workspace}/*/*'):
        if os.path.isdir(f'{path}/.git'):
            local_repos[path] = Git(path)
        elif os.path.isdir(path):
            local_repos[path] = None
    return local_repos

def get_count(client):
    return len(client)

# def get_name(client, repo):
#     return client[repo]

def get_clone_url(client, path):
    if len(client[path].remotes) == 1:
        return client[path].remotes[0].url
    elif 'origin' in client[path].remotes:
        return client[path].remotes['origin'].url
    else:
        print(f'{path}: {client[path].remotes}')
        return None

def is_dirty_repo(client, path):
    return client[path].is_dirty()

if __name__ == '__main__':
    client = get_client()
#     get_count(client)

def get_client():
    workspace = './workspace'
    local_repos = dict()
    for path in glob.glob(f'{workspace}/*/*'):
        if os.path.isdir(f'{path}/.git'):
            local_repos[path] = Git(path)
        elif os.path.isdir(path):
            local_repos[path] = None
    return local_repos

def get_count(client):
    return len(client)

# def get_name(client, repo):
#     return client[repo]

def get_clone_url(client, path):
    if len(client[path].remotes) == 1:
        return client[path].remotes[0].url
    elif 'origin' in client[path].remotes:
        return client[path].remotes['origin'].url
    else:
        print(f'{path}: {client[path].remotes}')
        return None

def is_dirty_repo(client, path):
    return client[path].is_dirty()

if __name__ == '__main__':
    client = get_client()
#     get_count(client)

def get_client():
    workspace = './workspace'
    local_repos = dict()
    for path in glob.glob(f'{workspace}/*/*'):
        if os.path.isdir(f'{path}/.git'):
            local_repos[path] = Git(path)
        elif os.path.isdir(path):
            local_repos[path] = None
    return local_repos

def get_count(client):
    return len(client)

# def get_name(client, repo):
#     return client[repo]

def get_clone_url(client, path):
    if len(client[path].remotes) == 1:
        return client[path].remotes[0].url
    elif 'origin' in client[path].remotes:
        return client[path].remotes['origin'].url
    else:
        print(f'{path}: {client[path].remotes}')
        return None

def is_dirty_repo(client, path):
    return client[path].is_dirty()

if __name__ == '__main__':
    client = get_client()
#     get_count(client)
