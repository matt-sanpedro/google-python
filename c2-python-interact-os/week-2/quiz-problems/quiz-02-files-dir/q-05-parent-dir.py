import os

"""
returns the name of the directory that's located just above the current working directory
remember that ".." is a relative path alias that means "go up to the parent directory"
"""
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
    os.chdir("../")
    return (os.path.abspath(os.getcwd()))

print(parent_directory())
