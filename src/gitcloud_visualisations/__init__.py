from fastapi import APIRouter, HTTPException

visualise = APIRouter()

@visualise.get("/commits")
async def get_commits_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")

@visualise.get("/langauges")
async def get_langauges_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")

@visualise.get("/issues")
async def get_issues_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")

@visualise.get("/merge_requests")
async def get_merge_request_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")

@visualise.get("/contributors")
async def get_contributors_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")

@visualise.get("/clones")
async def get_clones_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")

@visualise.get("/referers")
async def get_referers_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")

@visualise.get("/dependencies")
async def get_dependencies_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")

@visualise.get("/forks")
async def get_forks_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")

@visualise.get("/datetime")
async def get_datetime_graph():
    raise HTTPException(status_code=501, detail="Not Implemented")
