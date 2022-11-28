import random

rand_num = random.randint(1,1000000)
count = 0
print("Totally Random One-Million-to-One")
print()

while True:
  guess = int(input("What is your guess? "))
  if guess > rand_num:
    print("Too high.")
    print()
  elif guess < rand_num:
    print("Too Low")
    print()
  elif guess == rand_num:
    print("Correct!")
    break
  else:
    print("Invalid entry. Please enter a number")
  count += 1

print(f"It took you {count} guesse(s) to get the number correct. Click 'run' to try again with a different number.")