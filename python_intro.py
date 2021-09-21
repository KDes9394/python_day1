###Excercise 1
for i in range(20):
    if i**3> 1000: 
        break
    print(i**3)

        


###Exercise 2
# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

#1 is not prime.
# prime numbers need to be divisible by smaller number.
# number/x 
    
for number in range(1,101):
    x = 2
    if number > 1:
        for x in range(2,number):
            if(number%x)==0:
                break
        else:print(number)





###Exercise 3
age = int(input("How old are you? "))

if age < 18: 
    print ("You are a child.")
elif age < 65: 
    print("You are an adult.")
else: print ("You're a senior")
