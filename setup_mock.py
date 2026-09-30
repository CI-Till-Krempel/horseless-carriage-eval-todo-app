import sys
from unittest.mock import MagicMock

class MockBase:
    def __init__(self, *args, **kwargs):
        pass

class MockModel(MockBase):
    @classmethod
    def __class_getitem__(cls, item):
        return cls
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
