def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    a = set(my_cities)
    b = set(other_cities)

    return len(a ^ b)
