from flask import Flask
from .extensions import db, cache, migrate
from .config import Config
from .resources.game_resource import bp as game_bp
from .resources.player_resource import bp as player_bp
from .resources.score_resource import bp as score_bp

def create_app():
    app = Flask(__name__)
    
    # Load configuration from a config file or environment variables
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    cache.init_app(app)
    migrate.init_app(app, db)

   # Import models after initializing db
    with app.app_context():
        from .models import Player, Game, Score
    
    # Register blueprints/resources
    app.register_blueprint(game_bp)
    app.register_blueprint(player_bp)
    app.register_blueprint(score_bp)

    return app
