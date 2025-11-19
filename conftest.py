import pytest
from django.urls import reverse

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def create_user(db):
    from django.contrib.auth.models import User
    def make_user(username, password):
        user = User.objects.create_user(username=username, password=password)
        return user
    return make_user

@pytest.fixture
def sample_data():
    return {
        'name': 'Sample',
        'description': 'This is a sample data.'
    }