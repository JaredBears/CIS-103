print("This program will encrypt a line of text using a Caesar cipher.")
plaintext = input("Enter the text to encrypt: ")
while True:
    distance = int(input("Enter the distance value: "))
    if distance == 0 or distance > 94 or distance < -94:
        print("Invalid distance value. Please enter a non-zero value between -94 and 94.")
    else:
        break
encrypted = ""
for ch in plaintext:
    if ch.isprintable():
        new = ord(ch) + distance
        #wraparound if new value is out of range
        if new > 126:
            new -= 95
        elif new < 32:
            new += 95
        encrypted += chr(new)
print("The encrypted text is:", encrypted)