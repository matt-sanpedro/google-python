# open and print file contents to console
def open_and_print(filename):
    with open(filename) as guests:
        for line in guests:
            print(line.strip())

# write initial guest list to file: guests.txt
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

# check contents of created guests.txt file
open_and_print('guests.txt')

# append the new guests to file
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", 'a') as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

# check contents of created guests.txt file with appended guest names
print('BEFORE:\n')
open_and_print('guests.txt')


"""
Open the file in "read" mode.
Iterate over each line in the file and put each guest's name into a Python list.
Open the file once again in "write" mode.
Add each guest's name in the Python list to the file one by one.
"""
def check_out_guests(filename, checked_out):
    temp_list = []

    with open(filename) as guests:
        for g in guests:
            temp_list.append(g.strip())

    with open(filename, 'w') as guests:
        for name in temp_list:
            if name not in checked_out:
                guests.write(name + "\n")

def check_guests(filename, guests_to_check):
    checked_in = []

    with open(filename,"r") as guests:
        for g in guests:
            checked_in.append(g.strip())
        for check in guests_to_check:
            if check in checked_in:
                print("{} is checked in".format(check))
            else:
                print("{} is not checked in".format(check))

check_out_guests("guests.txt", ["Andrea", "Manuel", "Khalid"])

# check contents of guests.txt file after check out operation
print('AFTER:\n')
open_and_print("guests.txt")

# check guests test
check_guests("guests.txt", ['Bob', 'Andrea'])
