import assertpy
import pytest
import logging
import itertools



class AssertDemo():
    def __init__(self):
        self.log=logging.getLogger("BlaBla")

    def exception_handeling_function(self):
        try:
            raise RuntimeError("Wow bet you cant test me")
        except RuntimeError as ex:
            self.log.error(f"got this strange error , says it know you")

    def assertpy_demo(self,a:int , name:str)->list:
        return list(itertools.repeat(name,a))


def test_logging(caplog):
    caplog.set_level(logging.ERROR)
    demo = AssertDemo()
    demo.exception_handeling_function()
    assert 'got this strange error , says it know you' in caplog.text

def test_assertpy():
    demo = AssertDemo()
    result=demo.assertpy_demo(a=5,name='Test')
    assertpy.assert_that(result).is_type_of(list).contains('Test').is_length(5)

