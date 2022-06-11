import pytest
import os
import requests
from datetime import datetime
import time

#region monkeypatch

def get_current_dir():
    """Simple function to return expanded homedir ssh path."""
    return os.getcwdb()

def test_getssh(monkeypatch):
    print(f"\n without patch {get_current_dir()}")

    # mocked return function to replace Path.home
    def mock_get_current_dir():
        return "Not really your buisness"

    # Application of the monkeypatch to replace Path.home
    # with the behavior of mockreturn defined above.
    monkeypatch.setattr(os, "getcwdb", mock_get_current_dir)

    # for this test with the monkeypatch.
    x = get_current_dir()
    print(f" with patch {get_current_dir()}")

    assert x == "Not really your buisness"
#endregion

#region use with fixtures

def get_json(url):
    """Takes a URL, and returns the JSON."""
    r = requests.get(url)
    return r.json()

class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

#endregion
#region  monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


# notice our test uses the custom fixture instead of monkeypatch directly
def test_get_json(mock_response):
    result = get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"

#endregion


#region prevent everywhere

'''
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")
'''
#endregion

#region environment veriabels
# contents of our test file e.g. test_code.py
def get_os_user_lower():
    """Simple retrieval function.
    Returns lowercase USER or raises OSError."""
    username = os.getenv("USER")

    if username is None:
        raise OSError("USER environment is not set.")

    return username.lower()

@pytest.fixture
def mock_env_user(monkeypatch):
    monkeypatch.setenv("USER", "TestingUser")


@pytest.fixture
def mock_env_missing(monkeypatch):
    monkeypatch.delenv("USER", raising=False)


# notice the tests reference the fixtures for mocks
def test_upper_to_lower(mock_env_user):
    assert get_os_user_lower() == "testinguser"


def test_raise_exception(mock_env_missing):
    with pytest.raises(OSError):
        _ = get_os_user_lower()
#endregion


#region mock called times
def sleep_awhile(duration):
    """sleep for couple of seconds"""
    time.sleep(duration)
    # some other processing steps

def test_sleep_awhile(mocker):
    called_time=3600
    #intersting syntex
    m = mocker.patch("Mocking.test_mocking_example.time.sleep", return_value=None)
    sleep_awhile(called_time)
    m.assert_called_once_with(called_time)

#endregion

#region spy
def test_spy_method(mocker):
    class Foo(object):
        def bar(self, v):
            return v * 2

    foo = Foo()
    spy = mocker.spy(foo, 'bar')
    assert foo.bar(21) == 42

    spy.assert_called_once_with(21)
    assert spy.spy_return == 42
#endregion

#region datetime-mock
def get_time_of_day():
    """return string Night/Morning/Afternoon/Evening depending on the hours range"""
    time = datetime.now()
    if 0 <= time.hour <6:
        return "Night"
    if 6 <= time.hour < 12:
        return "Morning"
    if 12 <= time.hour <18:
        return "Afternoon"
    return "Evening"

@pytest.mark.parametrize(
    "datetime_obj, expect",
    [
        (datetime(2016, 5, 20, 0, 0, 0), "Night"),
        (datetime(2016, 5, 20, 1, 10, 0), "Night"),
        (datetime(2016, 5, 20, 6, 10, 0), "Morning"),
        (datetime(2016, 5, 20, 12, 0, 0), "Afternoon"),
        (datetime(2016, 5, 20, 14, 10, 0), "Afternoon"),
        (datetime(2016, 5, 20, 18, 0, 0), "Evening"),
        (datetime(2016, 5, 20, 19, 10, 0), "Evening"),
    ],ids=['Night-1','Night-2','Morning-3','Afternoon-1','Afternoon-2','Evening-1','Evening-2']
)
def test_get_time_of_day(datetime_obj, expect, mocker):
    mock_now = mocker.patch("test_mocking_example.datetime")
    mock_now.now.return_value = datetime_obj
    assert get_time_of_day() == expect
#endregion

#region patch -Mock where it is used, and not where it’s defined
def load_data():
    time.sleep(4)
    # loading data...
    return {"key1":"val1", "key2":"val2"}
def process_data():
    data = load_data()
    # process the data in certain ways ...
    processed_data = data["key1"]
    return processed_data
def test_process_data(mocker):

    mocker.patch("test_mocking_example.load_data", return_value={"key1": "valy", "key2": "val2"})

    assert process_data() == "valy"

#endregion

