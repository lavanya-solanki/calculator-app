import random
while True: # loop (play again)
   number = random.randint(1,100)
   for i in range(5):
       print(f"chances left : {5-i}")
       guess = int(input("Enter your guess :"))
       if guess > number:
          print("TOO HIGH")
       elif guess < number :
          print(" TOO LOW")
       else:
          print(" CORRECT GUESS")
          print(" you win!")
          break
   else:
    print("SORRY! YOU USED ALL 5 CHANCES TO GUESS")
    print(" The number was:", number)
    # play again option
    choice = input("DO YOU WANT TO PLAY AGAIN?(yes/no):").lower()
    if choice != "yes":
          print(" THANKS FOR PLAYING!")
          break
          
