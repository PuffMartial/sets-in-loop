# Using curly braces
my_set = {1, 2, 3, 4, 5}

# Using the set() constructor
another_set = set([3, 4, 5, 6, 7])

# Adding elements
my_set.add(6)
my_set.update([7, 8, 9])

# Removing elements
my_set.remove(3)
my_set.discard(10)  # Discard will not raise an error if the element is not present


# Union of sets
union_set = my_set.union(another_set)

# Intersection of sets
intersection_set = my_set.intersection(another_set)

# Difference between sets
difference_set = my_set.difference(another_set)

# Check if an element is in the set
if 6 in my_set:
    print("6 is in the set")

# Get the length of the set
length = len(my_set)

# Clear all elements from the set
my_set.clear()


print(my_set[0])
