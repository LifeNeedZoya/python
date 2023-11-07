print("Hello my first projects")

name = input("what is your name? ")
age = int(input("what is your age? "))
txt = "i am {0}  name  i am  {1} years old"
print(txt.format(name, age))

#IF CONDITION

if age < 18:
    print("You are minor")
else:
    print("you are adult") 

want_to_play = input("wanna play (yes/no)").lower() 

if want_to_play == "yes":
    print("lets play ")

# WHILE LOOP

fruitslist = [ "apple", "mango", "lemon"]
i = 0
while i < len(fruitslist):
    print(fruitslist[i])
    i = i + 1
   
# ONE LINE IF CONDITION
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

