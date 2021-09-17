import Levenshtein as lev
from fuzzywuzzy import fuzz


def is_similar(product1, product2):
    if lev.distance(product1, product2) < max_distance_to_be_considered_same()\
       and lev.ratio(product1, product2) > min_ratio_to_be_considered_same()\
    :
        return similarity(product1, product2)
    return False


def max_distance_to_be_considered_same():
    return 10


def min_ratio_to_be_considered_same():
    return 0.3


# we add all the possible similarities and we will select the product with the maximum value
def similarity(product1, product2):
    return \
        fuzz.ratio(product1, product2)\
        + fuzz.partial_ratio(product1, product2)\
        + fuzz.token_sort_ratio(product1, product2)\
        + fuzz.token_set_ratio(product1, product2)