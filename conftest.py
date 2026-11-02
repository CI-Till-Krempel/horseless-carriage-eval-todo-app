import sys
import os

# Ensure the root directory and src directory are in sys.path for proper test imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
if os.path.exists(os.path.join(os.path.dirname(__file__), 'src')):
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
