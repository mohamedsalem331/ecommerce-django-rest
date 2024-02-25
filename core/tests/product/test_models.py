import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from core.product.models import Category, Product, ProductLine

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_output(self, category_factory):
        obj = category_factory(name="test_cat")
        assert obj.__str__() == "test_cat"

class TestBrandModel:
    def test_str_output(self, brand_factory):
        obj = brand_factory(name="test_bra")
        assert obj.__str__() == "test_bra"

class TestProductModel:
    def test_str_output(self, product_factory):
        obj = product_factory(name="test_pro")
        assert obj.__str__() == "test_pro"