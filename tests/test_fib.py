import pytest
from new_template_workshop import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from new_template_workshop import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####

##########################