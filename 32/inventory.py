from copy import deepcopy
items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]


def duplicate_items(items):
    return deepcopy(items[:])

if __name__ == '__main__':
   items_copy = duplicate_items(items)
   items_copy[0]['name'] = 'POOOOOOOOPP'

   print(items_copy)
   print(duplicate_items(items))
