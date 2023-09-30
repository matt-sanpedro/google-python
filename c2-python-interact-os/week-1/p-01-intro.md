# Getting Ready for Python

### Terminology
- __Operating System__: the software that manages everything that goes on in the computer
    * main OS used today include: Windows, MacOS, Linux
    * Linux is used heavily in business infrastructure
- __Distribution__: flavors of Linux
    * examples include: Ubuntu, Debian, and Red Hat
- __Kernel__: 
    * consists of: system's resources, disk, memory, and network
- __pip__: a cross-platform tool called a package manager used to install, update, or remove external Python modules
- __IDE (Integrated Development Environment)__: code editors with capabilities
- __Scalability__: when more work is added to a system, the system can do whatever it needs to complete the work
    * example: An IT engineer writes a script to compile a report on each machine's uptime and downtime for the day and email it to relevant parties every evening
- __Pareto Principle__: 20% of the system administration tasks performed are responsible for 80% of your work
- __Bit-rot__: the process of software falling out of step with the environment

### Python Modules
- __shutil__: can use the "disk_usage" function to check available disk space

### Concepts
- the shebang line in a Python file can be used to specify beforehand what command to use when running the script
    * example for Linux OS: #!/usr/bin/env python3
- for python modules stored in folder, the "__init__.py" file must exist

### Pitfalls of Automation
- important question: is the time and effort it'll take to write the script worth the potential automation benefits?
    * time_to_automate < (time_to_perform * amount_of_times_done)
