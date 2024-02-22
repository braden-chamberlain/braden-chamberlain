import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

ADJECTIVES
NOUNS
prod = Product('Test Product')
pytest


def test_default_product_price():
    '''Test default product price being 10.'''
    assert prod.price == 10


def test_name():
    '''testing the product name'''
    assert prod.name == 'Test Product'


def test_stealability():
    '''testing the products stealability'''
    assert prod.stealability() == "Kinda stealable."


def test_explode():
    '''testing the default explode method'''
    assert prod.explode() == "...boom!"


def test_generate_products():
    '''
    makes sure the default generate products function
    returns a list with 30 items in it
    '''
    test = generate_products()
    assert len(test) == 30
    assert isinstance(test, list)
