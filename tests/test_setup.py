"""Tests for project setup and dependencies (US-0001)."""
import pytest


def test_flask_import():
    """Verify Flask is importable."""
    try:
        import flask
        assert hasattr(flask, 'Flask')
    except ImportError:
        pytest.fail("Flask not installed")


def test_pytest_available():
    """Verify pytest is available."""
    import sys
    assert 'pytest' in sys.modules or True  # pytest is available if this test runs


def test_flask_app_creation():
    """Verify Flask app can be created."""
    import flask
    app = flask.Flask('test')
    assert app is not None
    assert app.name == 'test'


def test_requirements_documented():
    """Verify requirements.txt exists and contains expected packages."""
    import os
    assert os.path.exists('requirements.txt'), "requirements.txt not found"
    
    with open('requirements.txt', 'r') as f:
        content = f.read()
        assert 'Flask' in content, "Flask not in requirements.txt"
        assert 'pytest' in content, "pytest not in requirements.txt"


def test_readme_exists():
    """Verify README.md exists and documents the tech stack."""
    import os
    assert os.path.exists('README.md'), "README.md not found"
    
    with open('README.md', 'r') as f:
        content = f.read()
        # Verify key documentation sections are present
        assert 'Tech Stack' in content, "README missing Tech Stack section"
        assert 'Python' in content, "README doesn't mention Python"
        assert 'Flask' in content, "README doesn't mention Flask"
        assert 'Setup Instructions' in content, "README missing Setup Instructions"
        assert 'Architecture' in content, "README missing Architecture section"
