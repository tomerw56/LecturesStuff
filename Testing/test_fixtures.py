import pytest
import os
import shutil
import tempfile


# region regular use
class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# endregion

# region reuse
# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


# why does order act this way?
def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]


# endregion

#region scope

'''
# function: the default scope, the fixture is destroyed at the end of the test.

# class: the fixture is destroyed during teardown of the last test in the class.

# module: the fixture is destroyed during teardown of the last test in the module.

# package: the fixture is destroyed during teardown of the last test in the package.

# session: the fixture is destroyed at the end of the test session.
'''
@pytest.fixture(scope="session")
def just_another_fixture():
    pass


# region detrmine_scope
def determine_scope(fixture_name, config):
    if config.getoption("--keep-containers", None):
        return "session"
    return "function"


def complex_creation():
    return "blablabla"


@pytest.fixture(scope=determine_scope)
def docker_container():
    yield complex_creation()


# endregion detrmine_scope

# endregion


# region cleaningUp
class DBOperations():
    def create_db(self):
        print("DB created")

    def delete_db(self):
        print("DB deleted")

    def do_stuff(self):
        return True


@pytest.fixture()
def db_container():
    container = DBOperations()
    container.create_db()
    yield container
    print("Clear DB")
    container.delete_db()


def test_db_operations(db_container):
    assert db_container.do_stuff()


# endregion

# region passing data to fixture
import pytest


@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("test_data")
    if marker is None:
        # Handle missing marker in some way...
        data = None
    else:
        data = marker.args[0]

    # Do something with the data
    return data


@pytest.mark.test_data(42)
def test_fixt(fixt):
    assert fixt == 42


# endregion

# region fixtures as factories
@pytest.fixture
def make_customer_record():
    created_records = []

    def _make_customer_record(name):
        record = {'name': name, 'orders': []}
        created_records.append(record)
        return record

    yield _make_customer_record

    for record in created_records:
        record.clear()


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")


# endregion

#region parametrizing fixtures
@pytest.fixture(scope="module", params=[1, 2, 3])
def number_generator(request):
    print(f"called with {request.param}")
    yield request.param * 3


def test_fixture_params(number_generator):
    value_to_inspect = number_generator
    print(f"called with {value_to_inspect}")
    assert (value_to_inspect % 3) == 0

#region skipping


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    pass
#endregion

# endregion

#region use fixtures

@pytest.fixture
def cleandir():
    old_cwd = os.getcwd()
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    yield
    os.chdir(old_cwd)
    shutil.rmtree(newpath)

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
#endregion
