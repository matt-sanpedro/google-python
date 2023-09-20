# initialize dictionary
file_counts = {'jpg': 3, 'csv': 15, 'py': 26, 'txt': 32}
print(file_counts)

# can overwrite entries
file_counts['py'] = 11
print(file_counts)

# del: keyword used to delete dictionary content
del file_counts['jpg']
print(file_counts)

# in: keyword used to check if key is contained in dictionary
print('py' in file_counts)

# for loops to iterate over dictionary
for extension in file_counts:
    print(extension, file_counts[extension])

for ext, amount in file_counts.items():
    print(ext, amount)

# count letters from a string and store in dictionary
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters('supercalifragilisticexpealidocious'))
