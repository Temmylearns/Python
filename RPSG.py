import random 
def computer(dd):
    if dd == 1:
     print("Computer chose: Rock")
    elif dd == 2:
     print("Computer chose: Paper")
    elif dd == 3:
     print("Computer chose: Scissors")
        
def main():
        x = True
        print("lets play Rock, Paper, Scissors")
        print(" choose 0 to end game")
        print("choose between Rock, paper scissor")
        print(" 1 = Rock, 2 = paper, 3 = scissor, 0 = quit ")
        score1 = 0
        score2 = 0
        while x:
            player_choice = int(input("choose between Rock, paper scissor :"))
            if player_choice not in [1, 2, 3, 0]:
                    print("Invalid choice. Please choose 1, 2, or 3.")
                    continue
            dd = random.randint(1,3)
            match player_choice:
                
                        case 1:
                            print("Rock")
                            if  dd == 3:
                                #rock beats scissor 
                                print("you Win!!! yayyyyyy")
                                score1 += 1
                            elif dd == 2:
                                print("you lose the Computer wins")
                                score2 +=1
                            elif dd == 1:
                                print("tie")
                            
                            computer(dd)

                        case 2:
                            print("Paper")
                            if  dd == 3:
                                print("you lose the Computer wins")
                                score2 +=1
                            elif dd == 2:
                                    print("tie")
                            elif dd == 1:
                                print("you Win!!! yayyyyyy")
                                score1 += 1
                            computer(dd)

                        case 3:
                            print("scissors")
                            if  dd == 3:
                                print("tie")
                            elif dd == 2:
                                print("you Win!!! yayyyyyy")
                                score1 += 1
                            elif dd == 1:
                                print("you lose the Computer wins")
                                score2 +=1
                            
                            computer(dd)

                        case 0:
                            x=False
                    
            
            if score1 == 3:
                print("you win against the computer")
                print("you are a Good player")
                x= False
            elif score2 ==3:
                print("Computer wins")
                print("you lose... cry now!")
                x= False
            


if __name__ == "__main__":
        main()