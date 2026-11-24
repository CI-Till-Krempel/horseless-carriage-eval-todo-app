"""Test configuration and fixtures."""
import pytest


@pytest.fixture
def app():
    """Create and configure a test instance of the app."""
    # Import here to avoid issues if the app module has initialization side effects
    # For US-0001 (documentation story), just verify Flask can be imported
    try:
        import flask
        app = flask.Flask(__name__)
        app.config['TESTING'] = True
        return app
    except ImportError:
        pytest.skip("Flask not available")
        

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
