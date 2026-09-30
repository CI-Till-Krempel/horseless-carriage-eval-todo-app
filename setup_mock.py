import sys
from unittest.mock import MagicMock

class MockColumn:
    def __init__(self, *args, **kwargs):
        pass

class MockRelationship:
    def __init__(self, *args, **kwargs):
        pass

class MockForeignKey:
    def __init__(self, *args, **kwargs):
        pass

class MockModelMeta(type):
    def __instancecheck__(cls, instance):
        return True

class MockModel:
    pass

class MockSQLAlchemy:
    Model = MockModel
    Column = MockColumn
    Integer = int
    String = str
    Boolean = bool
    ForeignKey = MockForeignKey
    relationship = MockRelationship
    
    def __init__(self, app=None):
        pass
    def init_app(self, app):
        pass
    def create_all(self):
        pass
    @property
    def session(self):
        return MagicMock()

class MockFlask:
    def __init__(self, name):
        self.name = name
    def route(self, *args, **kwargs):
        return lambda f: f
    def app_context(self):
        return self
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

mock_flask = MagicMock()
mock_flask.Flask = MockFlask

mock_sqlalchemy = MagicMock()
mock_sqlalchemy.SQLAlchemy = MockSQLAlchemy

sys.modules['flask'] = mock_flask
sys.modules['flask_sqlalchemy'] = mock_sqlalchemy
sys.modules['sqlalchemy'] = MagicMock()
