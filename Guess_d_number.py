import random
print ("Guess the number between 1 - 20")
x = random.randint (1,20)
y = input("Input  you'r guess number here: ")
valid = True
while y not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']:
	print("please input only neumeric values between 1- 20 ")
	y = input("Input  you'r guess number here: ")

print (x)

if int(y) == int(x) :
	print ("Hurray you won")
elif int(x) > int(y):
	print ("Too low")
elif int(x) < int(y) :
	print ("Too high")  
