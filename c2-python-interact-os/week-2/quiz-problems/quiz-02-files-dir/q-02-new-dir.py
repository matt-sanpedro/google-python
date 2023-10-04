import os

"""
creates a new directory inside the current working directory,
then creates a new empty file in side the new directory,
and returns the list of files in that directory
"""
def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
#   print(os.path.isdir(directory))
  if os.path.isdir(directory) == False:
    os.mkdir(directory)
#     print("Directory created: {}".format(directory))
#   else:
#     print("Warning directory already exists: {}".format(directory))

  # Create the new file inside of the new directory
  os.chdir(directory)
#   print(os.getcwd())
  with open(filename, "w") as file:
    pass

  # Return the list of files in the new directory
    return os.listdir(os.getcwd())

print(new_directory("PythonPrograms", "script.py"))