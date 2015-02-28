#stings 

#palindrome 

def palindrome(strtocheck):
	l = len(strtocheck)
	for i in range(0,l):
		if(strtocheck[i]=!strtocheck[l-i-1]):	
			return false 
	return true 

#reverse a string 
def reverse(strtorev):
	rev = ""
	for i in range(0, len(strtorev)):
		rev +=strtorev[i-1]
	return rev 
