import os
import csv

"""
complete content_of_file to process data without turning it into a dictionary
hint: skip over the header redcord with the fieldnames
"""

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file
    rows = csv.reader(file)

    # # check is header exists
    # file.seek(0)
    # has_header = csv.Sniffer().has_header(file.read(1024))
    # print("Has header: {}".format(has_header))

    # skip header row
    next(rows)

    # Process each row
    for row in rows:
      # Format the return string for data rows only
      name, color, type = row

      return_string += "a {} {} is {}\n".format(color, name, type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))