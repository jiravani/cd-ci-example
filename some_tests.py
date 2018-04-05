import sys
sys.path.insert(0,'..')
import pytest
from some import some_fn

def initial_test():
    assert some_fn() == 'abc_123'

def test_2():
    assert some_fn(some_input='123') == '123'
