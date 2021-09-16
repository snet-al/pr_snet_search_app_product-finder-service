import Levenshtein as lev

def is_similar(product1, product2):
    if lev.distance(product1, product2) < max_distance_to_be_considered_same()\
       and lev.ratio(product1, product2) > min_ratio_to_be_considered_same()\
    :
        return True
    return False


def max_distance_to_be_considered_same():
    return 10


def min_ratio_to_be_considered_same():
    return 0.3