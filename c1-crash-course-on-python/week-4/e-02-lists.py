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