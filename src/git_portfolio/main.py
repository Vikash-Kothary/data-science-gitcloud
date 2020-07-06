from flask import Flask

from git_portfolio import data
from git_portfolio import features
from git_portfolio import models
from git_portfolio import visualise
from git_portfolio import utils


def create_app():
    app = Flask(__name__)
    data.register_app(app)
    features.register_app(app)
    models.register_app(app)
    visualise.register_app(app)
    utils.register_app(app)
    return app
    

if __name__ == '__main__':
    create_app()
