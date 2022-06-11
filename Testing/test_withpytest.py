import time
import pytest
from Example_Demo.MyCrazyCalculator import myCrazyCalclulator


def test_passes():
    assert True


def test_add():
    calculator = myCrazyCalclulator(crazy_mode=False)
    assert calculator.add(a=1, b=3) == 4


def test_div_exception():
    calculator = myCrazyCalclulator(crazy_mode=True)
    # so simple!
    with pytest.raises(RuntimeError):
        calculator.div(a=100, b=2)


@pytest.mark.parametrize("crazy_mode, a,b,result", [
    (False, 1, 2, 3),
    (True, 5, 2, 0),
    (True, 2, 2, 4),
    (True, 1, 2, 3),
],    ids=['testA id', 'testB id','testC id','testD id']
)
def test_many_ways_of_plus(crazy_mode, a, b, result):
    calculator = myCrazyCalclulator(crazy_mode=crazy_mode)
    assert calculator.add(a=a, b=b) == result


#execute with pytest -m "not slow"
@pytest.mark.slow
def test_too_slow_to_run_always():
    print("In slow test")
    time.sleep(5)
    assert True
