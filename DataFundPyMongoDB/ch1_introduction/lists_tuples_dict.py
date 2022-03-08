import numpy as np

if __name__ == "__main__":
    ls = ["orange", "banana", 10, "leaf", 77.009, "tree", "cat"]
    print("list length:", len(ls), "items")
    print("cat count:", ls.count("cat"), ",", "cat index:", ls.index("cat"))
    print("\nmanipulate list:")
    cat = ls.pop(6)
    print("cat:", cat, ", list:", ls)
    ls.insert(0, "cat")
    ls.append(99)
    print(ls)
    ls[7] = "11"
    print(ls)
    ls.pop(1)
    print(ls)
    ls.pop()
    print(ls)
    print("\nslice list:")
    print("1st 3 elements:", ls[:3])
    print("last 3 elements:", ls[3:])
    print("start at 2nd to index 5:", ls[1:5])
    print("start 3 from end to end of list:", ls[-3:])
    print("start from 2nd to next to end of list:", ls[1:-1])
    print("\ncreate new list from another list:")
    print("list:", ls)
    fruit = ["orange"]
    more_fruit = ["apple", "kiwi", "pear"]
    fruit.append(more_fruit)
    print("appended:", fruit)
    fruit.pop(1)
    fruit.extend(more_fruit)
    print("extended:", fruit)
    a, b = fruit[2], fruit[1]
    print("slices:", a, b)
    print("\ncreate matrix from two lists:")
    matrix = np.array([ls, fruit])
    print(matrix)
    print("1st row:", matrix[0])
    print("2nd row:", matrix[1])

# OUTPUT
"""
list length: 7 items
cat count: 1 , cat index: 6

manipulate list:
cat: cat , list: ['orange', 'banana', 10, 'leaf', 77.009, 'tree']
['cat', 'orange', 'banana', 10, 'leaf', 77.009, 'tree', 99]
['cat', 'orange', 'banana', 10, 'leaf', 77.009, 'tree', '11']
['cat', 'banana', 10, 'leaf', 77.009, 'tree', '11']
['cat', 'banana', 10, 'leaf', 77.009, 'tree']

slice list:
1st 3 elements: ['cat', 'banana', 10]
last 3 elements: ['leaf', 77.009, 'tree']
start at 2nd to index 5: ['banana', 10, 'leaf', 77.009]
start 3 from end to end of list: ['leaf', 77.009, 'tree']
start from 2nd to next to end of list: ['banana', 10, 'leaf', 77.009]

create new list from another list:
list: ['cat', 'banana', 10, 'leaf', 77.009, 'tree']
appended: ['orange', ['apple', 'kiwi', 'pear']]
extended: ['orange', 'apple', 'kiwi', 'pear']
slices: kiwi apple

create matrix from two lists:
lists_tuples_dict.py:36: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
  matrix = np.array([ls, fruit])
[list(['cat', 'banana', 10, 'leaf', 77.009, 'tree'])
 list(['orange', 'apple', 'kiwi', 'pear'])]
1st row: ['cat', 'banana', 10, 'leaf', 77.009, 'tree']
2nd row: ['orange', 'apple', 'kiwi', 'pear']
"""
