from random import randint

# a = qar
# b = mkrat
# c = tuxt

flag = True

while flag:
    player_coice = input("Player choice: [A/B/C]: ").lower()
    
    if player_coice not in ["a","b","c"]:
        print("Incorrect input. Try again!")
        continue
    
    gen = {1:"a", 2:"b", 3:"c"}
    computer_choice = gen[randint(1,3)]
    
    print(computer_choice)    
    
    win_comb = [("a","b"),("b","c"),("c","a")]
    
    if (player_coice,computer_choice) in win_comb:
        print("Congrats! You are win!")
    else:
        if computer_choice == player_coice:
            print("A draw!")
        else:
            print("Computer wins!")
    
    response = input("Do you want to exit ? [Y/N] ").lower()
    
    if response == "y":
        flag = False
    else:
        flag = True
    