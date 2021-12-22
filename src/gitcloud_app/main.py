import uvicorn
from fastapi import FastAPI, HTTPException

from gitcloud_data import data
from gitcloud_features import features
# from gitcloud_models import models
# from gitcloud_visualisations import visualise
# from getcloud_services import services
from gitcloud_utils import config

app = FastAPI(
    title=config.OPENAPI_TITLE,
    version=config.OPENAPI_VERSION,
    description=config.OPENAPI_DESCRIPTION,
    docs_url='/'
)
app.include_router(data, prefix='/api/v1/data', tags=['Data'])
app.include_router(features, prefix='/api/v1/features', tags=['Features'])
# app.include_router(models, prefix='/api/v1/models', tags=['Models'])
# app.include_router(visualise, prefix='/api/v1/visualisations', tags=['Visualisations'])
# app.include_router(services, prefix='/api/v1/services', tags=['Services'])

if __name__ == '__main__':
    uvicorn.run(app, **config)