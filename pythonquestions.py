#Exercise 1
#Cube Number Test... Print out all cubed
#numbers up to the total value 1000. Meaning 
#that if the cubed number is over 1000 break 
#the loop

list_num = [1,2,3,4,5,6,7,8,9,10]

for x in list_num:
    print(x * x * x)
    if x >= 1000:
        break



#Exercise 2
#Get first prime numbers up to 100

for x in range(2,101): 
    for y in range(2,101):
        if x%y == 0:
            break
    if x == y:
        print(x)



#Exercise 3
#Take in a users input for their age, if they 
# #are younger than 18 print kids, if they're 18 
#to 65 print adults, else print seniors

x = int(input("what is your age?"))

if x < 18:
    print("kids")
elif x <= 65:
    print("adults")
else:
    print("seniors")