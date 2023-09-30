import os, subprocess, datetime

# function: organize directories and files into a dictionary data type
def collect_types(dir):
    for name in os.listdir(dir):
        fullname = os.path.join(dir, name)

        if os.path.isdir(fullname):
            print("{} is a directory".format(fullname))
        else:
            print("{} is a file".format(fullname))

# restore test files by running shell script
subprocess.call(["sh", "./e-02-restore_test_files.sh"])

# if file DNE, raises a "FileNotFoundError"
os.remove("novel.txt")

# rename method will rename files
os.rename("first_draft.txt", "final_masterpiece.txt")

# os.path contains a "exists" method to check if file is present
print(os.path.exists("final_masterpiece.txt"))

# "getsize" function can check size of file
print(os.path.getsize("spider.txt"))

# "getmtime" function will return the time when file was last modified
# returns unix timestamp, the seconds since January 1, 1970
timestamp = os.path.getmtime("spider.txt")
print(timestamp)

# datetime module easy for human reading
print(datetime.datetime.fromtimestamp(timestamp))

# "abspath" function will output the absolute path of the file
print(os.path.abspath("spider.txt"))

# "getcwd" function will check the current directory Python is running scripts from
print(os.getcwd())

# "mkdir" function will create a directory of designated name
os.mkdir("new_dir")

# "chdir" function will change directory in which Python executes scripts
os.chdir("new_dir")
print(os.getcwd())
os.chdir("../")

# "rmdir" function removes the directory, only if empty (no files exists)
os.rmdir("new_dir")

# "os.listdir" return a list of files and subdirectories
print(os.listdir("./"))

# "os.path.isdir()" function  
collect_types("./")