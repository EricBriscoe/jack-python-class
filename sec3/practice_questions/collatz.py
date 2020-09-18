def collatz(number):
    """
    Write a function which prints the collatz sequence
    per the specifications on pg. 76
    
    In summary you will create a loop until the number reaches 1
    If the number is even your next number will be number//2
    If the number is odd your next number will be 3 * number + 1
    """
    pass


if __name__ == "__main__":
    starting_num = input("Enter starting number")
    collatz(starting_num)
