print(9/3)
print(3*1)
print(9/3 != 3*1)

# python strings have a unique unicode #
print('A' > 'a') # 65 > 97 "False"

# The greater than > operator checks if the left string has a higher 
# Unicode value than the right string. If true, the Python interpreter
# returns a True result. Since W has a Unicode value of 87, and you can 
# easily calculate that F has a Unicode value of 70, this comparison is
# the same as 87 > 70. As this is true, Python will return a True 
# result.
day = "Wednesday"
print(day > "Friday") # Trues

#  built-in functions chr() and ord() are used to convert between Unicode code points and characters
print(chr(65)) # A
print(ord('W')) # 87

# If the strings have the same first few letters, the comparison will 
# cycle through each letter of each string, from left to right until it 
# finds two letters that have different Unicode values. In this example, 
# both strings share the initial substring "sun", but then have 
# different letters with different Unicode values in the fourth place 
# in each string. So, the fourth letters 'b' and 't' of the two
# strings are used for the comparison. Since 'b' does not have a higher
# Unicode value than 't', the comparison returns a False result.
print("sunbathe" > "suntan") # False
