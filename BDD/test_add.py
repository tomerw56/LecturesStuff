from functools import partial
from pytest import fixture
from pytest_bdd import (
    scenario as bdd_scenario,
    given,
    when,
    then,
    scenarios
)
scenarios('add.feature')


@fixture
def result():
    return {}


@given(name="A number",target_fixture='num1')
def num1():
    return 2


@given(name="Another number",target_fixture='num2')
def num2():
    return 4


@when("I make the sum")
def when_sum(result, num1, num2):
    from .add import add
    result['result'] = add(num1, num2)


@then("The sum matches")
def sum_matches(result, num1, num2):
    assert result['result'] == (num1 + num2)
