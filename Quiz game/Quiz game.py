# Enter the welcome message.
print("Welcome to the quiz game")

# Get the user input
user_input = input("Do you want to play? ")

# Convert the user input to proper case.
user_input= user_input.title()

# Default user score
score = 0

# Number of questions
number_of_question = 0

# Validate the user input
if user_input != "Yes":
    print("User entered: {}, so game is over".format(user_input))
    quit()
print("Okay! let's play :)")

# First question.
answer = input("What does CPU stands for? ")

if answer.lower() == "central processing unit":
    score += 1
    number_of_question += 1
    print("Correct answer")
else:
    print("Wrong answer")

# Second question
answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    number_of_question += 1
    score += 1
    print("Correct answer")
else:
    print("Wrong answer")

# Third question
answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    number_of_question += 1
    score += 1
    print("Correct answer")
else:
    print("Wrong answer")

# Fourth question
answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    number_of_question += 1
    score += 1
    print("Correct answer")
else:
    print("Wrong answer")

# Display the final score.
print("You have answered correctly for {} questions out of {} questions".format(score,number_of_question))
print("Your percentage {:.2%}".format(score/number_of_question))