from fastapi import APIRouter

data = APIRouter()

@data.get("/local")
async def get_local_integration_details():
    local = {}
    return {"data": local}

@data.post("/local")
async def create_local_integration():
    local = {}
    return {"data": local}

@data.get("/local/data")
async def get_local_data():
    local = {}
    return {"data": local}

@data.get("/github")
async def get_github_integration_details():
    github = {}
    return {"data": github}

@data.post("/github")
async def create_github_integration():
    github = {}
    return {"data": github}

@data.get("/github/data")
async def get_github_data():
    github = {}
    return {"data": github}

@data.get("/gitlab")
async def get_gitlab_integration_details():
    gitlab = {}
    return {"data": gitlab}

@data.post("/gitlab")
async def create_gitlab_integration():
    gitlab = {}
    return {"data": gitlab}

@data.get("/gitlab/data")
async def get_gitlab_data():
    gitlab = {}
    return {"data": gitlab}