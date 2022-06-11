import pytest
from coveraged_file import coveraged_file


def test_regular_case():
    target=coveraged_file()
    assert 6==target.mult(a=3,b=2)
'''
def test_c_is_larger_than_one_case():
    target=coveraged_file()
    assert 0==target.mult(a=3,b=2,c=17)


def test_exception():
    target=coveraged_file()
    # so simple!
    with pytest.raises(RuntimeError):
        target.mult(a=1,b=33)
'''

#how to run
#coverage run -m pytest test_coveragefile.py

#coverage report -m
#coverage html

#for pytest-watch
#ptw --onfail flash
