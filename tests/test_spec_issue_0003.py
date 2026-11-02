import sys
import os

def test_sys_path():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(root_dir)
    # Check that root or parent is in sys.path
    assert any(os.path.abspath(p) in sys.path for p in ['.', '..', root_dir])
