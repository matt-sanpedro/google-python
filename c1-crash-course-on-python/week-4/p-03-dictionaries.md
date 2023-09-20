# Dictionaries

### Terminology
- __items()__: dictionary method returns a tuple for each element in the dictionary
    * first element is key and second is the value
- __keys()__: dictionary method returns keys from the dictionary
- __values()__: dictionary method returns values from the dictionary
- __set__: data type used when you want to store a bunch of elements and be certain that they're only present once
    * elements of set must be immutable

### Concepts
- utilized as key/value pairs
- use curly braces "{}" to define content
- dictionaryies are mutable, can be modified by adding, removing, and replacing elements in a dictionary
- keys in a dictionary must be an immutable data type
    * numbers
    * booleans
    * strings
    * tuples

### Dictionaries vs. Lists
- list ideal for storing a list of ip addresses to ping
- dictionary for host names paired with ip addresses
- dictionaries when searching for a specific element

### Operations
- len(dictionary) - Returns the number of items in a dictionary.
- for key, in dictionary - Iterates over each key in a dictionary.
- for key, value in dictionary.items() - Iterates over each key,value pair in a dictionary.
- if key in dictionary - Checks whether a key is in a dictionary.
- dictionary[key] - Accesses a value using the associated key from a dictionary.
- dictionary[key] = value - Sets a value associated with a key.
- del dictionary[key] - Removes a value using the associated key from a dictionary.

### Methods
- dictionary.get(key, default) - Returns the value corresponding to a key, or the default value if the specified key is not present.
- dictionary.keys() - Returns a sequence containing the keys in a dictionary.
- dictionary.values() - Returns a sequence containing the values in a dictionary.
- dictionary[key].append(value) - Appends a new value for an existing key.
- dictionary.update(other_dictionary) - Updates a dictionary with the items from another dictionary. Existing entries are updated; new entries are added.
- dictionary.clear() - Deletes all items from a dictionary.
- dictionary.copy() - Makes a copy of a dictionary.
