# import random module.
import random

# Validate the lowest range
lowest_range = input("Enter the lowest number for range: ")

if lowest_range.isdigit() == True:
    lowest_range = int(lowest_range)
    if lowest_range < 0:
        print("Enter the lowest number greater than or equal to zero next time")
        quit()
else:
    print("Enter a numeric number next time for lowest number")
    quit()

# Validate the highest range
highest_range = input("Enter the maximum number for range: ")
if highest_range.isdigit() == True:
    highest_range = int(highest_range)
    if highest_range <= lowest_range:
        print("Enter the highest number greater than lowest number: {} next time".format(lowest_range))
        quit()
else:
    print("Enter a numeric number next time for highest number")
    quit()

# Generate random numbers from 0 to 11
random_number = random.randint(lowest_range, highest_range)
print("Random number :", random_number)

# Set default guess count.
guess_count = 0
# Check the user input with generated user number.
while True:
    user_input = input("Make a guess: ")
    guess_count += 1
    if user_input.isdigit() == True:
        user_input = int(user_input)
    else:
        print("Enter a number next time.")
        continue
    if user_input == random_number:
        print("You guessed right")
        break
    elif user_input > random_number:
        print("You have entered the number higher than random number")
    else:
        print("You have entered the number lower than random number")
# Print the result
print("You guessed the answer in the {} guess".format(guess_count))

# Print the end of the game statement.
print("Guessing game is over")