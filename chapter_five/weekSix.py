def main():
    filename = input("Enter the name of the file: ")
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    print("The file has", len(lines), "lines.")
    while True:
        lineNum = int(input("Enter a line number (0 to quit): "))
        if lineNum == 0:
            break
        elif lineNum < 0 or lineNum > len(lines):
            print("Invalid line number.")
        else:
            print(lines[lineNum - 1])
    print("Goodbye.")

if __name__ == "__main__":
    main()