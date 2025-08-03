import random
print ("*************Welcome to Sanke, water and gun game*************")
user = int(input("for sanke 0, water 1 and gun 2 :\n "))
def check (user, comp):
    if comp == user:
        return 0
    if comp == 0 and user ==1:
        return -1
    if comp == 1 and user ==2:
        return -1
    if comp == 2 and user ==0:
        return -1
    
    return 1

comp = random.randint(0,2)  # Random integer between 0 and 2
print (comp)

score = check(comp ,user)
if (score== 0 ):
    print("It's Draw")
elif (score== -1):
    print("You lose")
else: 
    print("You Won")


print("you:"  ,user)
print("computer:"  ,comp)
 