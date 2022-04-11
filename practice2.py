a = int(input("Enter first integer:"))
b = int(input("Enter second integer:"))
c = int(input("Enter third integer:"))
if a > b and b > c:  
	print ("First integer is a biggest") 
elif a > b and a < c:
	print ("Third  integer is biggest")
elif a < b and b > c: 
	print ("Second integer is biggest")
elif a < b and b < c: 
	print ("Third integer is biggest")
elif a > c and a < b: 
	print ("Second integer is biggest")



