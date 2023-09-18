# append method adds an element to the end
fruits = ['Pineapple', 'Banana', 'Apple', 'Watermelon']
fruits.append('Guava')
print(fruits)

# insert method adds an element to specified index
fruits.insert(0, 'Orange')
print(fruits)
# if the specified index is larger than the list, will add to end
fruits.insert(100, 'Peach')
print(fruits)

# removed specified element from list [will raise ValueError if element is not in list]
fruits.remove('Banana')
print(fruits)

# pop method removes the specified index from the list and its value is returned
removed_element = fruits.pop(-3)
print(f"Element was removed: {removed_element}")
print(fruits)

# can reassign elements in list different values
fruits[0] = 'Dragonfruit'
print(fruits)

# tuples are like lists but the order matters
# tuples can be unpacked
hours, minutes, seconds = (1, 23, 20)
print(hours, minutes, seconds)

# tuple example
animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
chars = 0
for animal in animals:
    chars += len(animal)
print('Total characters: {}, Average length: {}'.format(chars, chars/len(animals)))

# enumerate function
winners = ['Ashley', 'Dylan', 'Reese']
for index, person in enumerate(winners):
    print('{} - {}'.format(index, person))

# example of tuple unpacking with a function
def full_emails(people):
    result = []

    for email, name in people:
        result.append('{} <{}>'.format(name, email))

    return result

people_data = [('alex@example.com', 'Alex Fernandez'), ('shay@example.com', 'Shay Brandt')]
print(full_emails(people_data))

# for loops: multiples of 7
multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

# list comprehension: multiples of 7
multiples = [x*7 for x in range(1,11)]
print(multiples)

# list comprehension: with len function
languages = ['Python', 'Perl', 'Ruby', 'Go', 'Java', 'C']
lengths = [len(language) for language in languages]
print(lengths)

# list comprehension: factors of 3
z = [x for x in range(0,101) if x % 3 == 0]
print(z)

# list comprehension: odd numbers
def odd_numbers(n):
	return [x for x in range(n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

# list comprehension exercise
'''
This exercise will walk you through how to write a list comprehension to create a list of squared numbers (n*n). It needs to return a list of squares of consecutive numbers between “start” and “end” inclusively. For example, squares(2, 3) should return a list containing [4, 9].

1. The function receives the variables “start” and “end” through the function parameters. 
2. In the return line, start by entering the list brackets [ ]
3. Between the brackets [ ], enter the arithmetic expression to square a variable “n”. 
4. To the right of the square expression, write a for loop that iterates over “n” in a range from the “start” to “end” variables.
5. Ensure the “end” range value is included in the range() by adding 1 to it.
'''
def squares(start, end):
    return [x**2 for x in range(start, end+1)] 


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# This block of code also changes the year on a list of dates using a
# different approach than demonstrated in Skill Group 1. By using a 
# list comprehension, you can see how it is possible to refactor the
# code to a shorter, more efficient code block. 

# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024". This action will be executed if
# the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]


print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]


# This function splits a given string into a list of elements. Then, it
# modifies each element by moving the first character to the end of the 
# element and adds a dash between the element and the moved character. 
# For example, the element "2two" will be changed to "two-2". Finally,
# the function converts the list back to a string, and returns the
# new string.
def change_string(given_string):

# Initialize "new_string" as a string data type by using empty quotes.
    new_string = ""
    # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:

        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items: 
        # + Each list "element" (starting at index position [1:]), 
        # + a dash "-", 
        # + append the first character of the "element" (using the index 
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-"  + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string


print(change_string("1one 2two 3three 4four 5five")) 
# Should print "one-1 two-2 three-3 four-4 five-5"  
