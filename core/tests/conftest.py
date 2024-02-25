import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import (
    CategoryFactory,
    BrandFactory,
    ProductFactory
)

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

# will be available globally
@pytest.fixture
def api_client():
    return APIClient
