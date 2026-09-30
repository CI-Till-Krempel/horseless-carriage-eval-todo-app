import sys
from unittest.mock import MagicMock

class MockModelMeta(type):
    def __instancecheck__(cls, instance):
        return True

class MockModel(metaclass=MockModelMeta):
    def __init__(self, *args, **kwargs):
        pass
    @classmethod
    def query(cls):
        return MagicMock()

class MockSQLAlchemy(MagicMock):
    Model = MockModel
    def __init__(self, app=None):
        super().__init__()
    def init_app(self, app):
        pass
    def create_all(self):
        pass

class MockFlask(MagicMock):
    def __init__(self, name):
        super().__init__()
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
