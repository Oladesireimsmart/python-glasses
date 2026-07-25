
basket1 ={"apple", "banana", "orange", "grapes"}
basket2 ={"banana", "kiwi", "mango", "grapes"}
print("basket 1:", basket1)
print("basket 2:", basket2)

basket1.add("pear")
print("basket 1 after adding pear:", basket1)


common_fruits = basket1.intersection(basket2)
print("Common fruits in both baskets:", common_fruits)


import array as arr
fruit_counts = arr.array('i', [5, 3, 2, 4, ])
print("Fruit counts:", fruit_counts)


