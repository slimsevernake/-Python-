from modeltranslation.translator import translator, TranslationOptions

from shop.catalogue.models import ProductAttribute, ProductClass, Category, ProductAttributeValue
from .models import Product


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class ProductAttributeTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProductClassTranslationOptions(TranslationOptions):
    fields = ('name',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'description_title')


class ProductAttributeValueTranslationOptions(TranslationOptions):
    fields = ('value_text', 'value_richtext',)


translator.register(Product, ProductTranslationOptions)
translator.register(ProductAttribute, ProductAttributeTranslationOptions)
translator.register(ProductClass, ProductClassTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(ProductAttributeValue, ProductAttributeValueTranslationOptions)
