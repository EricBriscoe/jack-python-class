fruit = input("Guess which fruit I'm thinking of!: ")

tries = 2
max_tries = 5
winner = True

while fruit != 'apple':
    fruit = input("Nope! Try again: ")
    
    if tries >= max_tries:
        winner = False
        break
    tries += 1

print(winner)
if winner == False:
    print("You Lose!")

if winner == True:
    print("You Win!")
