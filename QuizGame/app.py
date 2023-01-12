print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's play.")
score = 0

answer = input("What does VPC stand for? ")
if answer.lower() == "virtual private cloud":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect! :(")

answer = input("What does SSH stand for? ")
if answer.lower() == "secure shell":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect! :(")

answer = input("What does EC2 stand for? ")
if answer.lower() == "elastic compute cloud":
    print("Correct!!!") 
    score += 1  
else:
    print("Incorrect! :(")

answer = input("What does RDS stand for? ")
if answer.lower() == "relational database":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect! :(")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")






