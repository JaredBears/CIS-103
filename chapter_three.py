def main():
    print("This program will calculate the sum and average of a series of numbers.")
    print("Press enter to finish providing inputs.")
    print()
    total = 0.0
    count = 0
    while(True):
        number = input("Enter a number: ")
        if number == "":
            break
        try:
            total += float(number)
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    if count > 0:
        average = total / count
        print("The sum of the numbers is", total)
        print("The average of the numbers is", average)
        print()
    response = input("Would you like to start over? (y/n): ")
    if response == "y":
        main()
    else:
        print("Goodbye.")
        return
    
main()