import os
from flask import Flask
from flask_migrate import Migrate

# https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='Server=tcp:baseball-game-server.database.windows.net,1433;Initial Catalog=baseball_game_db;Persist Security Info=False;User ID=postgres;Password=admin1234!;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;',
        # Try this connection string here:
        # Server=tcp:baseball-game-server.database.windows.net,1433;Initial Catalog=baseball_game_db;Persist Security Info=False;User ID=postgres;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .baseball_models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    from .api import players, teams
    app.register_blueprint(players.bp)
    app.register_blueprint(teams.bp)

    return app
