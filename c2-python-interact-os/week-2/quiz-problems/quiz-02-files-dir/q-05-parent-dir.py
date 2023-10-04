import os

"""
returns the name of the directory that's located just above the current working directory
remember that ".." is a relative path alias that means "go up to the parent directory"
"""
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
    # print(os.getcwd())
    # print(os.chdir("../"))
    return (os.path.abspath(os.getcwd()))

#   relative_parent = os.path.join(os.path.getcwd(), )

  # Return the absolute path of the parent directory
#   return ___

print(parent_directory())