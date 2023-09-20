def increments(start, end):
    return [ number+2 for number in range(start, end+1) ] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
