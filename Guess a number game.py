#Game code
import random
import math
l=int(input("Enter lower range "))
h=int(input("Enter higher range "))
r=random.randint(l, h)
chance=math.ceil(math.log(h-l+1,2))
print(chance)
c=0
flag=False
while c<chance:
    c+=1
    guess=int(input("Guess a number "))
    if r==guess:
        print("Congratulation ")
        print("Game Over")
        flag=True
        break
    elif r<guess:
        print("Too high ")
    else:
        print("Too low ")
if not flag:
    print("Try again")
    print("The result is %d" % r)
    print("Game Over")

# Time Complexity: 
# The time complexity of this code is O(log2n) 
# Space Complexity:
# The space complexity of this code is O(1) 
