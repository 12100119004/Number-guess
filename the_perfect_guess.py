import random
randNo = random.randint(1, 100)

guess = 0
userguess = None
while(userguess!=randNo):
    guess+=1
    userguess = int(input("Enter a number"))
    if(userguess>randNo):
      print("You guess it wrong, please guess lesser number")
    elif(userguess<randNo):
      print("you guess it wrong, please guess greater number")
    else:
        print("****You gussed it right****")

print(f" @ You Guess it in {guess} attempts")

with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(hiscore>guess):
        print("you break the hiscore!")
        with open("hiscore.txt","w") as f:
            f.write(str(guess))
