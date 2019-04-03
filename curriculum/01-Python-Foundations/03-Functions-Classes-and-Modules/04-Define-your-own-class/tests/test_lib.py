"""
Tests
"""
import glob
import importlib
import inspect
import os

import pytest


@pytest.fixture
def module_paths():
    search_path = os.path.join('src', '*.py')
    files = glob.glob(search_path)
    modules = [f.replace('/', '.')[:-3] for f in files]  # remove .py ext
    module_paths = [m for m in modules if m.split('.')[-1] != 'interface']
    return module_paths


@pytest.fixture
def classes(module_paths):
    classes_ = []
    for module_path in module_paths:
        module_name = module_path.split('.')[-1]
        class_name = module_name.capitalize()
        module = importlib.import_module(module_path)
        try:
            cls_ = getattr(module, class_name)
        except AttributeError:
            cls_ = None
        if cls_ is not None:
            classes_.append(cls_)
    return classes_


def test_module_exists(module_paths):
    assert len(module_paths) > 0, "Did you create the modules?"


def test_class(classes):
    assert len(classes) >= 0, (
        "Did you name your class name the same way as your module but "
        "following the CamelCase convention and using singular?")


def test_it_should_have_a_docstring(classes):
    for cls in classes:
        assert cls.__doc__ is not None, (
            "Your class '{}' should have a docstring".format(cls.__name__))


def test_it_should_implement_init(classes):
    for cls in classes:
        assert cls.__init__ is not object.__init__, (
            "Did you implement the __init__ method?")


def test_it_should_have_at_least_one_instance_method(classes):
    for cls in classes:
        method_list = [f for f in dir(cls) if callable(getattr(cls, f))
                       and not f.startswith("__")]
        instance_methods = [f for f in method_list if 'self' in
                            inspect.getargspec(getattr(cls, f)).args]
        assert len(instance_methods) > 0, (
            f"{cls.__name__} should implement at least one instance method")
