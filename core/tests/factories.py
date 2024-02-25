import factory

from core.product.models import (
    Category,
    Brand,
    Product
)

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "test_category_%d" % n)
    # slug = factory.Sequence(lambda n: "test_slug_%d" % n)

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "test_brand_%d" % n)
    # slug = factory.Sequence(lambda n: "test_slug_%d" % n)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: "test_product_name_%d" % n)
    pid = factory.Sequence(lambda n: "0000_%d" % n)
    description = "test_description"
    is_digital = False
    category = factory.SubFactory(CategoryFactory)
    is_active = True
    product_type = factory.SubFactory(ProductTypeFactory)
    # slug = factory.Sequence(lambda n: "test_slug_%d" % n)
