import csv

# EXAMPLE 1: Parsing an existing CSV file
# reader funciton to parse file
with open("csv_file.txt") as file:
    csv_f = csv.reader(file)
    print(type(csv_f), csv_f)

    for row in csv_f:
        # print(row)

        # unpack the values: need same amount of variables on left of equal sign
        # good practice: unpacking to name variables makes it easier to understand the code
        name, phone, role = row
        print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

# EXAMPLE 2: Generating CSV file
# writer function to save to file
"""
writerow: will write one row at a time
writerows: write all rows together
"""
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)


# EXAMPLE 3: Parsing CSV file with DictReader
# DictReader function to turn each row as dictionary
with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))

# EXAMPLE 4: Generate CSV file from list of dictionaries
# DictWriter function will write a dictionary to CSV
users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"}
]
# Define list of keys to open the file
keys = ["name", "username", "department"]
with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    # create first line of CSV based on keys
    writer.writeheader()
    # write list of dictionaries into file
    writer.writerows(users)
