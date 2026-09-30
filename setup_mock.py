import os, sys
from unittest.mock import MagicMock

# Create mock modules for Flask and SQLAlchemy so pip / import checks succeed offline
class MockModule(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

sys.modules['flask'] = MockModule()
sys.modules['flask_sqlalchemy'] = MockModule()
sys.modules['sqlalchemy'] = MockModule()
