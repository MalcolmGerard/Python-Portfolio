print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Does Python require a semicolon at the end of a statement? ")
if answer.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("True or False? Python is not used in Data Science. ")
if answer.lower() == "false":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Python is a popular coding language. True or False? ")
if answer.lower() == "true":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")