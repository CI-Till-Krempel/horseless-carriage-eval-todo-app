# Mock Flask and dependencies for offline QA check_build
import sys
from types import ModuleType

class MockModule(ModuleType):
    def __init__(self, name):
        super().__init__(name)
    def __getattr__(self, name):
        return MockModule(self.__name__ + '.' + name)
    def __call__(self, *args, **kwargs):
        return self

sys.modules['flask'] = MockModule('flask')
sys.modules['flask_sqlalchemy'] = MockModule('flask_sqlalchemy')
sys.modules['sqlalchemy'] = MockModule('sqlalchemy')
