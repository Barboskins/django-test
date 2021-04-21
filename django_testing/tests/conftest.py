import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args,**kwargs):
        return baker.make('students.Student',*args, **kwargs)
    return factory

@pytest.fixture
def course_factory():
    def factory(*args,**kwargs):
        return baker.make('students.Course',*args, **kwargs)
    return factory
