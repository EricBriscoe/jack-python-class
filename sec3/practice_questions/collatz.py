def collatz(number):
    """
    Write a function which prints the collatz sequence
    per the specifications on pg. 76
    
    In summary you will create a loop until the number reaches 1
    If the number is even your next number will be number//2
    If the number is odd your next number will be 3 * number + 1
    """
    number = int(number)
    while number > 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = number * 3 + 1
            print(number)


if __name__ == "__main__":
    starting_num = input("Enter starting number")
    collatz(starting_num)
