import os
import click
from flask.cli import FlaskGroup
from webapp import create_app
from webapp.config import DevConfig

def create_web_app(info):
    cfg = eval(os.environ.get('APP_CONFIG', 'DevConfig'))
    app = create_app(cfg)
    return app


@click.group(cls=FlaskGroup, create_app=create_web_app)
def cli():
    ...

if __name__ == '__main__':
    cli()
    # app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)