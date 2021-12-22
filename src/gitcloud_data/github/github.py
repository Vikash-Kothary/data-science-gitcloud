import os
from github import Github
#from pprint import pprint

def get_client(username, password):
    return Github(username, password)

def get_count(client):
    return client.get_user().get_repos().totalCount

def create_repo(client, repo_name):
    org_name = 'vikash-kothary'
    return client.get_organization(org_name).create_repo(repo_name)

if __name__=='__main__':
    client = get_client(username, password)
    print(get_count(client))
    
