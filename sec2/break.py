fruit = input("Guess which fruit I'm thinking of!: ")

tries = 0
max_tries = 5

while fruit != 'apple':
    fruit = input("Nope! Try again: ")
    
    if tries > max_tries:
        break
    tries += 1

print("Nice! You guessed correctly!") # Something is wrong here!
