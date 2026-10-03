 #can we do it in a little polished way!! lets gooo..
     
import random
number = random.randint(1,10)
print(number)
attempt = 0
think=int(input("enter any number ,but it need to lie in the limit up to 10 which need to be started from 0"))
while True:
    if think == number:
        print(f"you guessed it right in {attempt} attempt")
        attempt +=1
        break
    elif think < number:
        print("think higher")
        attempt +=1
        think = int(input("try again"))
    else:
        print("think lower")
        attempt +=1
        think = int(input("try again"))
    