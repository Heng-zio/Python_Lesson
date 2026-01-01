#open file

'''
mode:
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does
    "x" - Create - Creates the specified file, returns an error if the file exists
    "b" - Binary - Binary mode
    "t" - Text - Text mode (default)
    
'''
'''
file_object = open(file = "test.txt", mode = "w")
file_object.write("Hello World\n")
file_object.write("Welcome to File Handling in Python\n")
file_object.close()

'''

lines = ["First Line\n", "Second Line\n", "Third Line\n"]
file_object = open(file = "test.txt", mode = "r")
file_object.readlines()
for line in lines:
    print(line)
file_object.close()