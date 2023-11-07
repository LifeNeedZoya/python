print("Quiz game")

score = 0

answer = input("What does the CPU stands for ? ").lower()
if answer == "Central processing unit".lower() :
    print("Correct")
    score += 1
else: 
    print("Incorrect")

answer2 = input("What does the Gpu stands for ? ").lower()
if answer2 == "Graphic processing unit".lower() :
    print("Correct")
    score += 1
else: 
    print("Incorrect")

print("score is", score)

print("you got " + str(score) + " questions correct")