from fastapi import APIRouter

features = APIRouter()

@features.get("/providers")
async def get_providers():
    providers = {}
    providers['github'] = 'github.com'
    providers['gitlab'] = 'gitlab.com'
    return {'data': providers}

@features.get("/organisations")
async def get_organisations():
    orgs = {}
    return {"data": orgs}

@features.get("/groups")
async def get_groups():
    return {"message": "Hello World"}

@features.get("/repos")
async def get_repositories():
    repos = []
    repos.append({'id': '0', 'name': 'data-science-gitcloud'})
    repos.append({'id': '1', 'name': 'backend-gitcloud'})
    repos.append({'id': '2', 'name': 'frontend-gitcloud'})
    return {"data": repos}

@features.get("/repos/{repo_id}")
async def get_repositorie_by_id(repo_id: int):
    if (repo_id != 0):
        raise HTTPException(status_code=404, detail="Repo not found")

    repo = {}
    repo['repo_id'] = 0
    repo['protocol'] = 'https'
    repo['provider'] = 'gitlab.com'
    repo['organisation'] = 'vikash-kothary'
    repo['group'] = 'data-sciece-projects'
    repo['name'] = 'data-science-gitcloud'
    repo['private'] = True
    return {"data": repo}

@features.get("/templates")
async def get_templates():
    templates = []
    templates.append({'id': '0', 'name': 'data-science'})
    templates.append({'id': '1', 'name': 'backend'})
    templates.append({'id': '2', 'name': 'frontend'})
    return {"data": templates}
