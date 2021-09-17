import Levenshtein as lev
from fuzzywuzzy import fuzz

# for some cases we need to reduce the calculation of similarity, so we have some exclusive conditions when two products cant be the same
def is_similar(product1, product2):
    if lev.distance(product1, product2) < max_distance_to_be_considered_same()\
       and lev.ratio(product1, product2) > min_ratio_to_be_considered_same()\
    :
        return True
    return False


# we add all the possible similarities and we will select the product with the maximum value
def similarity(product1, product2):
    return \
        fuzz.ratio(product1, product2)\
        + fuzz.partial_ratio(product1, product2)\
        + fuzz.token_sort_ratio(product1, product2)\
        + fuzz.token_set_ratio(product1, product2)


def max_distance_to_be_considered_same():
    return 10


def min_ratio_to_be_considered_same():
    return 0.7