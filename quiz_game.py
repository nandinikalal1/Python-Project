#Intro
print("Welcome to the Quiz!")
play = input("Are you ready to play the Quiz? Types yes to continue ")
if play.lower != "yes":
    print("Okay! Lets start :)")
else:
    quit()

score = 0 

#question 1#
user_answer = input("Q1: How many planets does our Solar System consist? - ")
if user_answer.lower() == "8":
    print("Correct! :)")
    score += 1
else:
    print("Incorrect :( ")
#question 2
user_answer = input("Q2: Which planet is closest to the Sun? - ")
if user_answer.lower() == "mercury":
    print("Correct! :)")
    score += 1
else:
    print("Incorrect :( ")
#question 3
user_answer = input("Q3: What is the hottest planet in the Solar System? - ")
if user_answer.lower() == "venus":
    print("Correct! :)")
    score += 1
else:
    print("Incorrect :( ")
#question 4
user_answer = input("Q4: Venus has more atmospheric pressure than Earth? True or false? - ")
if user_answer.lower() == "true":
    print("Correct! :)")
    score += 1
else:
    print("Incorrect :( ")
#question 5
user_answer = input("Q5: What is the third planet from the Sun? - ")
if user_answer.lower() == "earth":
    print("Correct! :)")
    score += 1
else:
    print("Incorrect :( ")

#finalscore
print("Your Final Score is " + str(score) +"/5")

print("You got "+ str((score/5)*100) + "%")