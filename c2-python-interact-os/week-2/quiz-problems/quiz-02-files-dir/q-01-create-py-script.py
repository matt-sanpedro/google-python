import os

"""
create a new python script in current working directory
add the lines of comments declared by the "comments" variable
return the size of the new file
"""
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))