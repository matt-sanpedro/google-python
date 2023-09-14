message = 'A kong string with a silly typo'
# TypeError: strings in Python are immutable; below line produces error
# message[2] = 'l'

new_message = message[:2] + 'l' + message[3:]
print(new_message)

# variables in Python support string reassignment
message = 'Message in a bottle'
print(message)

# the "index" method for string data types
print(message.index('M'))

# use the keyword "in" to check if the substring exists
print('in' in message)

# a replace domain example for emails
def replace_domain(email, old_domain, new_domain):
    search_term = '@' + old_domain
    if search_term in email:
        index = email.index(search_term)
        new_email = email[:index] + '@' + new_domain
        return new_email
    return email

print(replace_domain('nobody@google.com', 'google.com', 'tcs.com'))

# Method: isnumeric [returns True if string contains ONLY numbers]
print('1231651561'.isnumeric()) # True
print('99.9'.isnumeric()) # False

# Method: join
print(' '.join(['This', 'is', 'a', 'list', 'joined', 'by', 'spaces']))

# Method: split
print('This is a string that has been split into a list')

# Method: format
name = 'Matthew'
number = len(name) * 3
print('Hello {}, your lucky number is {}'.format(name, number))
# can also pass variable names into the curly braces
print('Your lucky number is {number}, {name}.'.format(name=name, number=len(name)*3))
print('Your lucky number is {number}, {name}.'.format(name=name, number=number))

# format can also print a specified amount of decimals
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
# the "f" in the curly brace indicates that a float number is formatted
print('Base price: ${:.2f}.  With tax: ${:.2f}'.format(price, with_tax))

# format method can utilize ">" to align text to the right
print('\nAligning text with format method:')
def to_celsius(temp):
    return (temp-32)*5/9

for x in range(0,101,10):
    print('{:>3} F | {:>10.2f} C'.format(x, to_celsius(x)))

# format method with placeholders
first = 'apple'
second = 'banana'
third = 'carrot'
formatted_string = '{0} {2} {1}'.format(first, second, third)
print(formatted_string)

# formatting float, rounding numbers
print('{:.0f}'.format(10.11))

# f-string literals with rounding format
item = 'Red Cup'
amount = 10
price = amount * 3.25
print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')
