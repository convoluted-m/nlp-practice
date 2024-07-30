# Read a text file using the "with" statement
# "with" auto-closes the file once you're finished using it
with  open('sample_text.txt') as file:
    file_data = file.read()
    print(file_data)



## Not prefferred
# Reading a text file using the open() function 
# requires a string with the filepath
file = open('sample_text.txt') 
# read()method takes the text from the file and puts it into a string
# Assign the string to the file_data variable
file_data = file.read() 
print(file_data)
# close() ensures the file is closed to free up computer resources
file.close()
