import uvicorn
from fastapi import FastAPI

from gitcloud_data import data
from gitcloud_features import features
from gitcloud_models import models
from gitcloud_visualisations import visualise
from gitcloud_services import services
from gitcloud_utils import config

app = FastAPI(
    title=config.OPENAPI_TITLE,
    version=config.OPENAPI_VERSION,
    description=config.OPENAPI_DESCRIPTION,
    docs_url='/'
)
app.include_router(data, prefix='/api/v1/data', tags=['data'])
app.include_router(features, prefix='/api/v1/features', tags=['features'])
app.include_router(models, prefix='/api/v1/models', tags=['models'])
app.include_router(visualise, prefix='/api/v1/visualisations', tags=['visualisations'])
app.include_router(services, prefix='/api/v1/services', tags=['services'])

if __name__ == '__main__':
    uvicorn.run(app, **config)