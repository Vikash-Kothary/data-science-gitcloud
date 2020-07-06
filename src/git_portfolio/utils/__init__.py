
from git_portfolio.utils.status import status

def register_app(app):
    app.register_blueprint(status)
    pass
