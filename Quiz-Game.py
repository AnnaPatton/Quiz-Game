print("Welcome to the Quiz Game")

# adding a prompt asking a user to input y/n if they want to play - whatever they type after the prompt + press enter will be included
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay, let's begin the quiz!")

# defined score as equal to 0
score = 0

# for each question, .lower() was added to convert the text to lowercase - can be applied to the answer input or after if statement
# Question 1
answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    # if answer is correct, take the value of the score and add 1 (e.g., score = score + 1)
    score += 1
else: 
    print("Incorrect!")

# Question 2
answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


# Question 3
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


# Question 4
answer = input("What does PSU stand for? ")

if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

# Question 5
answer = input("What does VPN stand for? ")

if answer.lower() == "virtual private network":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

# converted score (integer) to a string
# score and percentage results
print("Thank you for playing! You got " + str(score) + " questions correct!")
print("You got " + str((score)/5 * 100) + "%.")