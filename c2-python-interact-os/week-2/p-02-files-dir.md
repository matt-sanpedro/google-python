# Managing Files and Directories

### Python Modules
- __os__: provides layer of abstraction between Python and OS
    * can use __remove__ function from module to delete a file

### Concepts
- paths can be different across different operating systems
    * when using absolute path in code, need to make sure can provide alternatives for the platforms
- in Linux and MacOS, the portions of a file are split using a forward slash ("/")
- in Windows, portions are split with backward slash ("\")
- the "os.path.join" function ensures that the paths work with ALL operating systems
    * It creates a string containing cross-platform concatenated directories
