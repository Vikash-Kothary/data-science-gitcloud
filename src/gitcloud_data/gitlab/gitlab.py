
def login_gitlab(username=None, password=None):
    if username is None:
        username = os.getenv('GITLAB_USERNAME')
    if password is None:
        password = os.getenv('GITLAB_PASSWORD')