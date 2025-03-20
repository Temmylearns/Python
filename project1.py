import random

def check(RangeA,RangeB):
    # print("range : ", RangeA, RangeB)
            if RangeB > RangeA:
                random_int = random.randint(RangeA, RangeB)
                random_int19 = random.randint(RangeA, RangeB)
                print("range : ", RangeA, RangeB)
                randomizer(RangeA,RangeB)    
            elif RangeB < RangeA:
                while RangeB < RangeA: #less than 
                    RangeB=int (input(" you entered a number lesser than.Select the end of a range of numbers :"))
                    if RangeB > RangeA:  #greater
                        random_int = random.randint(RangeA, RangeB)
                        print("range : ", RangeA, RangeB)
                        #print(random_int)  
                        randomizer(RangeA,RangeB) 
                        break
                    
                   

def randomizer(RangeA, RangeB):
    print("i have guessed the number now you have 3 tries to guess") 
    random_int = random.randint(RangeA, RangeB)
    for _ in range(3):
        guess = int(input("what did i guess:"))    
        if guess == random_int:
            print("correct")
            print("the number is", random_int)
            break
        else:
            print("you dumb mumu, you guess wrong now cry!!!")
    print("the number is", random_int)      

def main():
        
            print("choose a number between 1-50 ")
            RangeA =int( input("Select the start of a range of  numbers: "))
            print("choose a number greater than the number you chose above ")
            RangeB = int(input("Select the end of a range of numbers :"))
            check(RangeA,RangeB)
           
                           
                   
if __name__ == "__main__":
        main()
        