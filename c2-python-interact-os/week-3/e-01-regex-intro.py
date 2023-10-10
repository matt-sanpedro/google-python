import re

log = 'July 31 07:51:48 mycompter bad_process[12345]: ERROR Performing package upgrade'

# brittle solution, can break if process id gets larger
index = log.index("[")
# do not know how long the process ID is in all cases
print(log[index+1:index+6])

# regex solution
regex = r"\[(\d+)]"
result = re.search(regex, log)
print(result[1])