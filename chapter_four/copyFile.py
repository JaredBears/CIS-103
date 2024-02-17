print("This program will copy the contents of a file to a new file.")
filename = input("Enter the filename to copy: ")
newFilename = input("Enter the new filename: ")

f = open(filename, "r")
contents = f.read()
f.close()

f = open(newFilename, "w")
f.write(contents)
f.close()

print("The contents of", filename, "have been copied to", newFilename + ".")