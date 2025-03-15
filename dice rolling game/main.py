import random


while True:
    user_input=input("Roll the dice? (y/n)").lower()
    if user_input=="y":
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1},{die2})")
    elif user_input=="n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")