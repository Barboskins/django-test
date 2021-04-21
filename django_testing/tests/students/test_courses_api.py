# def test_example():
#     assert False, "Just test example"
import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK


@pytest.mark.django_db
def test_one_course(api_client,course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=course.id)
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    assert resp.json()['id'] == course.id


@pytest.mark.django_db
def test_list_course(api_client,course_factory):
    url = reverse('courses-list')
    course = course_factory(_quantity=4)
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK

