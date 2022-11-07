# from flask import Flask

# def create_app(test_config=None):
#     app = Flask(__name__)
#     from  .routes.planets import planets_bp
#     app.register_blueprint(planets_bp)


#     return app


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    from .routes import moons_bp
    app.register_blueprint(moons_bp)

    from app.models import Planet
    from app.models.moon import Moon 

    return app
