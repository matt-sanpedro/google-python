'''
The function is recursive and returns the sum of all positive numbers between the number n received and 1.
When n is 3 it should return 1+2+3=6, when n is five it should return 1+2+3+4+5=15
'''
def sum_positive_numbers(n):
  if n == 1:
    return 1
  else:
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
