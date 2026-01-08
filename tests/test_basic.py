import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_imports():
    """Test that we can import our modules"""
    try:
        import src.train
        import src.predict
        assert True
    except ImportError:
        assert False, "Failed to import modules"

def test_dummy():
    """A dummy test to get started"""
    assert 1 + 1 == 2