# EXAMPLE 1:
# This loop iterates on the value of the "x" variable in a range
# of 2 to -1 (the end-of-range index -2 is excluded). The third 
# parameter is also a negative number, making it a decremental value
# of -1. The print() function will output the resulting value of
# "x" as it starts at 2 and counts down to -1 (index -2).

for x in range(2, -2, -1):
    print(x)

# The loop should print 2, 1, 0, -1

# EXAMPLE 2
# nested for loops with domino tiles
# without "end" in the print statement, it will print the newline character
for left in range(7):
    for right in range(left, 7):
        print(f"[{left}|{right}]", end = " ")
    print()


# EXAMPLE 3
# running a local basketball team match up
# output all possible team pairings
# first name -> home team, second name -> away team
# do NOT want to pair a team with itself
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home in teams:
    for away in teams:
        if home != away:
            print(f"[{home} vs {away}]", end = " ")
    print()


# EXAMPLE 4:
# logical progression of nested for loops
# This code demonstrates the outer and inner loop iterations of a pair 
# of nested for loops. Click "Run" to see the results. The outer loop
# will run twice for the range pointer positions [0, 1] in range(2).
# The inner loop will run 4 times for the range pointer positions 
# [0, 1, 2, 3] in range(3+1) or range(4) each time the outer loop runs.
# So, the inner loop will execute 8 times in total.

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop") 