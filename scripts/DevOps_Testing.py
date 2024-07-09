file_name = "file.txt"
text = "Test data"

with open(file_name,'w') as file:
    file.write(text)

print("File '{file_name}' has been created and the message has been written.")