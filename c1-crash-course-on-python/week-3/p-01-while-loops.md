# While Loops
- Instruct computer to continuously execute your code based on the value of a condition

### When to use a while loop
- conditions used must evaluate to True or False
- body of while loop must include a change in condition, otherwise may run into infinite loop
- ping command used in Linux uses infinite loop internally to send packets, CTRL + C will exit the loop

### Terminology
- __Initializing__: to give an initial value to a variable
- __Infinite Loop__: a loop that keeps executing and never stops
*   ```
    while x % 2 == 0:
        x = x / 2
    ```

### Good Practice
- a common mistake is initializing variables incorrectly
- good practice to check that variables are initialized before using them
- body of loop modifies the variables used in the condition, loop eventually ends for all possible values of the variables
- preventing an infinite loop includes:
    * use the __break__ keyword
    * adding end criteria to codition part of the while loop

### Math Concepts
- __prime numbers__: integers that have only twwo factors, which are the number itself multiplied by 1, lowest prime number is 2
- __prime factors__: prime numbers that are factors of an integer
    * the prime numbers 2 and 5 are the prime factors of the number 10 (2 x 5 = 10)
    * prime factors of an integer will not produce a remainder when used to divide that integer
- __divisor__: a number (denominator) that is used to divide another number (numerator)
    * if the number 10 is divided by 5, the number 5 is the divisor
- __sum of all divisors of a number__: result of adding all of the divisors of a number together
- __multiplication table__: an integer multiplied by a series of numbers and their results formatted as a table or a list