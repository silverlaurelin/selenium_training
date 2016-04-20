import os

import pytest
from fixture.application import Application
import json
import importlib
import jsonpickle

fixture = None
target = None

@pytest.fixture

def app(request):
    global fixture
    global target
   # if target is None:
    #    with open(request.config.getoption("--target")) as config_file:
     #       target = json.load(config_file)

    if fixture is None:
        fixture = Application(browser = "chrome")

    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)

def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoptions(parser):
    parser.addoption ("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
   return  importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())