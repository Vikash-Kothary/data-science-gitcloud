from fastapi import APIRouter, HTTPException

services = APIRouter()

@services.patch("/local/repo")
async def modify_local_repo():
    raise HTTPException(status_code=501, detail="Not Implemented")

@services.patch("/github/repo")
async def modify_github_repo():
    raise HTTPException(status_code=501, detail="Not Implemented")

@services.patch("/gitlab/repo")
async def modify_gitlab_repo():
    raise HTTPException(status_code=501, detail="Not Implemented")