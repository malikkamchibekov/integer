a = 17391 % 17
b = 546 % 17 
c = 934 % 17

if a > b and b > c:
	print ("3 chislo")
elif a > b and c > b: 
	print ("2 chislo")
elif a < b and b < c: 
	print ("1 chislo")
elif a < b and a < c: 
	print ("1 chislo")    
