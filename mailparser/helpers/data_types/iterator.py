def get_nth_from_generator(iterator, n: int):
    """Gets the nth element from a generator"""
    for i in range(n):
        nth = next(iterator)
    return nth


def get_all_from_generator(iterator) -> list:
    """Gets all the elements from a generator and returns them in a list"""
    all_iterator_items = []
    while True:
        try:
            all_iterator_items.append(next(iterator))
        except StopIteration:
            return all_iterator_items
