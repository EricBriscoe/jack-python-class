import random

wins = 0
loss = 0
ties = 0

valid_moves = ['r', 'p', 's']

while True:
    # Ask the player for a move
    human_move = '' # Set move to empty to enter the loop
    while human_move not in valid_moves: # Check if player entered a valid move
        human_move = input('Enter a valid move (r, p, s): ') # Ask player for their move
   
    # Ask the computer for a move
    computer_move = random.choice(valid_moves)
    print('Computer Move:')
    print(computer_move)

    if human_move == 'r':
        if computer_move == 'r':
            ties += 1
            print("It's a tie!")

        elif computer_move == 'p':
            loss += 1
            print('Computer wins!')

        elif computer_move == 's':
            wins += 1
            print('Human wins!')
    
    elif human_move == 'p':
        if computer_move == 'r':
            wins += 1
            print("Human Wins!")

        elif computer_move == 'p':
            ties += 1
            print("It's a tie!")

        elif computer_move == 's':
            loss += 1
            print("Computer wins!")

    elif human_move == 's':
        if computer_move == 'r':
            loss += 1
            print("Computer wins!")

        elif computer_move == 'p':
            wins += 1
            print("Human Wins!")

        elif computer_move == 's':
            ties += 1
            print("It's a tie!")

    print("Human Score:")
    print(wins)
    print("Compute Score:")
    print(loss)
    print("Ties:")
    print(ties)
