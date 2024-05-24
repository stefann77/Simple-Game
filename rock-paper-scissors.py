rock = "Rock"
paper = "Paper"
scissors = "Scissors"

print("----------A simple rock-scissors-paper game---------------------")
print()
answer = ""
while answer != "no":
    answer = input("You want to play? yes/no  ")
    if answer == "yes":
        choice = input("Play with computer(1) or play with second player(2)?  ")
        if choice == "1":
            player = input("Rock, Paper or Scissors?  ")
            print("Computer's turn")
            import random
            computer = random.choice([rock, paper, scissors])
            print(computer)
            if player == computer:
                print("Draw")
            elif player == "Rock" and computer == "Scissors":
                print("You win")
            elif player == "Paper" and computer == "Rock":
                print("You win")
            elif player == "Scissors" and computer == "Paper":
                print("You win")
            else:
                print("You lose")
            if choice == "2":
                print("Player 1's turn")
                player1 = input("Rock, Paper or Scissors?")
                print("Player 2's turn")
                player2 = input("Rock, Paper or Scissors?")
                if player1 == player2:
                    print("Draw")
                elif player1 == "Rock" and player2 == "Scissors":
                    print("Player 1 wins")
                elif player1 == "Paper" and player2 == "Rock":
                    print("Player 1 wins")
                elif player1 == "Scissors" and player2 == "Paper":
                    print("Player 1 wins")
                else:
                    print("Player 2 wins")
    else:
        break