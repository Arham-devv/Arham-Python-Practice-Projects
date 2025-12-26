from random import randint
attempts=0
#loop to guesss number between 1,10
for i in range(0,10):
    Guess_num=int(input("Guess a number between 1 and 10 : "))
    Random_num=(randint(0,10))#function to print a random number on screen 
    attempts+=1
    print("Random number was : ",Random_num)
    if Guess_num==Random_num:#condional statment
        print("Correct Guess..")
        print(f"You have tried {attempts} times ... ")
        exit()#exit program if the user as guessed correct number 
    else:
        print("Not a correct guess please retry...")

