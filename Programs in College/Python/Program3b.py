file = open("myfile.txt","r")
print("The contents of the file: ")
print(file.read())
file.close()
file = open("myfile.txt","r")
lines = 0
words = 0
symbols = 0
for line in file:
    lines += 1
    words += len(line.split())
    symbols += len(line.strip('\n'))
print("\nDetails")
print("Lines:", lines)
print("Words:", words) 
print("Symbols:", symbols)
file.close()