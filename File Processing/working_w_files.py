myfile = open("fruits.txt")
print("Printing out directly from read method")
print (myfile.read())
myfile.close()
# storing the content in a variable
myfile2 = open("fruits.txt")
content = myfile2.read()
print ("Priting out from variable: ")
print(content)
print("###############################################################")

#Opening files using "with"
with open("fruits.txt") as myfile3:
    content2 = myfile3.read()
# No needed to close the file since is done by content manager
print ("Open file using with:")
print (content2)
print("###############################################################")

#Different filepaths
with open("Files/fruits2.txt") as myfile4:
    content3 = myfile4.read()
# No needed to close the file since is done by content manager
print ("Open file using with in different path:")
print (content3)
print("###############################################################")
#Writing text to a file
print ("Writing text to a file: ")
with open("Files/vegetables.txt","w") as myfile5:
    myfile5.write("Tomato \n")
    myfile5.write("Onion \n")

print ("please check the file vegetables in Files directory")
print("###############################################################")
#Reading a specific number of characters from a file
print ("Reading a specific number of characters from a file")
file = open("Files/bear.txt")
content = file.read()
file.close()
print(content[:90])    
print("###############################################################")
#File Processing Inside Function
#Define a function that gets a single string character and a filepath 
#as parameters and returns the number of occurences of that character in the file
print ("File Processing Inside Function and couting ocurrences or a character in the file bear.txt")
def count_ocurrences(character, filepath="Files/bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

char_input = input("Write the character to count: ")
print ("the character to check is: ",char_input)
result=count_ocurrences(character=char_input)
print("Number of ocurrences",result)

# Appending Text to an existing file
print ("Appending Text to Existing File")

with open ("Files/fruits.txt","a+") as myfile:
    myfile.seek(0)
    content_now = myfile.read()
    print ("The current data on the file",content_now)
    # Appending new line
    myfile.write("\ngrapes")
    # Moving the cursor at the begging
    myfile.seek(0)
    content_updated = myfile.read()
    print("The new file",content_updated)

print("###############################################################")

#Read and Append (E)
#Append the text of bear1.txt to bear2.txt. In other words, 
#bear2.txt should contain its text and the text of bear1.txt after that.

with open ("Files/bear1.txt") as myfile:
    myfile.seek(0)
    content_bear1 = myfile.read()
    print ("The content of bear1.txt is: \n",content_bear1)

with open ("Files/bear2.txt","a+") as myfile2:
    myfile2.seek(0)
    content_bear2 = myfile2.read()
    print ("The content of bear2.txt is: \n",content_bear2)
  
with open ("Files/bear2.txt","a") as myfile3:  
    content_bear_concatenate = myfile3.write(content_bear2)
    print ("The text of two files concatenate is: \n",content_bear_concatenate)


print("###############################################################")


    

           
           





