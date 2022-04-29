from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #deal with database
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres@localhost:5432/planets_development"

    from app.models.planets import Planet

    db.init_app(app) #initials sqalchemy object the database
    migrate.init_app(app, db)

    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app
