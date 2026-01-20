import random

def coin_toss_game():
    sides = ['head', 'tail']
    wins1, wins2 = 0, 0
    while True:
        print("\n--- New Round ---")
        player1_guess = input("Player 1, guess head or tail: ").lower().strip()
        if player1_guess == 'quit':
            break
        if player1_guess not in sides:
            print("Player 1: Invalid! Use 'head' or 'tail'.")
            continue
        
        player2_guess = input("Player 2, guess head or tail: ").lower().strip()
        if player2_guess == 'quit':
            break
        if player2_guess not in sides:
            print("Player 2: Invalid! Use 'head' or 'tail'.")
            continue
        
        result = random.choice(sides)
        print(f"\nCoin toss: {result}")
        
        p1_win = (player1_guess == result)
        p2_win = (player2_guess == result)
        
        if p1_win and p2_win:
            print("Tie! Both guessed correctly.")
        elif p1_win:
            print("Player 1 wins this round!")
            wins1 += 1
        elif p2_win:
            print("Player 2 wins this round!")
            wins2 += 1
        else:
            print("Tie! Neither guessed correctly.")
        
        print(f"Score: Player 1={wins1}, Player 2={wins2}")
    
    print(f"\nFinal Score: Player 1={wins1}, Player 2={wins2}")
    if wins1 > wins2:
        print("Player 1 is the overall winner!")
    elif wins2 > wins1:
        print("Player 2 is the overall winner!")
    else:
        print("It's a tie overall!")

coin_toss_game()
