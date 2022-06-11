import pytest
from angle import angle

def test_twelve():
    item=angle()
    assert item.between(12, 00) == 0
