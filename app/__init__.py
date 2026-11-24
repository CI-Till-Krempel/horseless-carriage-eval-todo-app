"""Flask application factory and initialization."""
from flask import Flask
from app.data import DataStore


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    
    # Initialize the data store (in-memory, global instance)
    app.store = DataStore()
    
    # Register blueprints
    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Serve the main HTML page from the root
    @app.route('/')
    def index():
        """Serve the main index page."""
        return app.send_static_file('index.html')
    
    @app.route('/<path:filename>')
    def serve_static(filename):
        """Serve static files (fallback to index for SPA routing)."""
        return app.send_static_file(filename)
    
    @app.errorhandler(404)
    def not_found(error):
        """Return index.html for SPA routing."""
        return app.send_static_file('index.html')
    
    return app
