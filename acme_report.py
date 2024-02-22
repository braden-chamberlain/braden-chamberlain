from acme import Product
import random
import numpy as np

ADJECTIVES = ['Awesome', 'Shiney', 'Impressive', 'Protable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    generates a list of the specified amount of
    randomized product attributes
    '''
    product_list = []
    for _ in range(num_products):
        product_name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        product = Product(name=product_name,
                          price=random.randint(5, 100),
                          weight=random.randint(5, 100),
                          flammability=random.uniform(0.0, 2.5)
                          )
        product_list.append(product)
    return product_list


def inventory_report(products):
    '''
    given a list of products, this function returns
    a tuple that has the number of unique items,
    mean price, mean weight, and mean flammability
    of the items given.
    '''
    product_names = []
    product_prices = []
    product_weights = []
    product_flammabilities = []

    for product in products:
        product_names.append(product.name)
        product_prices.append(product.price)
        product_weights.append(product.weight)
        product_flammabilities.append(product.flammability)

    product_set = set(product_names)
    unique_products = len(product_set)
    mean_price = np.mean(product_prices)
    mean_weight = np.mean(product_weights)
    mean_flammability = np.mean(product_flammabilities)

    return (unique_products, mean_price, mean_weight, mean_flammability)
