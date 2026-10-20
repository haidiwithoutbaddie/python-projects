print("==== Guess the value game ====")
import random
computer = random.randint(1,10)
count = 0
while True:
    try:
        a = int(input("Guess a number between 1-10: "))
    except ValueError:
        print("Enter a integer value")
        continue
    if a < 1 or a > 10:
          print("The number should be between 1-10")
          continue
    count += 1
    if a == computer:
            print("you win")
            break
    elif a > computer:
            print("Too High")
    elif a < computer:
            print("Too Low")
    else:
            print("invalid output")

print(f"You complete this game in: ", count)
    
