#stings 

#palindrome 

def palindrome(strtocheck):
	l = len(strtocheck)
	for i in range(0,l):
		if(strtocheck[i]=!strtocheck[l-i-1]):	
			return false 
	return true 