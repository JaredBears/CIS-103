def main():
    n = int(input("Which Fibonacci number do you want? "))
    print(f'The {ordinal(n)} Fibonacci number is {fibonacci(n)}.')

def fibonacci(n):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#This is just to clean up the text output
def ordinal(n):
    suffix = ["th", "st", "nd", "rd"]

    if n % 10 in [1, 2, 3] and n not in [11, 12, 13]:
        return f'{n}{suffix[n % 10]}'
    else:
        return f'{n}{suffix[0]}'
    
if __name__ == "__main__":
    main()