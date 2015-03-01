#arrays 

#sum of x and y is z

def issumbruteforce(x, sum):
	l = length(x)
	found = 0
	for i in xrange(l):
		for j in xrange(l);
			if i!=j:
				if x[i]+x[j]==sum:
					found +=1
					print "sum of %d and %d is %d" %(x[i], x[j], sum)
	print "No of pairs found is %d" %(found)

def issumhashmap(x,sum):
	match = {} #keys are values stored in the array and the values are indices of the array
	found = 0
	counter = 0 
	for i in xrange(len(x)):
		if sum-x[i] in match.keys():
			if len(match[sum-x[i]]):
				counter = counter+1
			for t in match[sum-x[i]]: #sum-x[i] is the key, t are all the positions for this key; iterate over all the psoitions for the key
				found +=1
				print "%d: [%d]=%d - [%d]=%d"%(found, t, x[t], i, x[i])
		if x[i] in match.keys():
			match[x[i]].append(i)
		else:
			match[x[i]] = [i]
	print match.keys()
	print match.values()
	print counter
	return found

#sort union of two sorted arrays 

def sortunion(x,y):	
	i = j = k = 0
	sortedunion = []
	while (i<len(x) and j <len(y)):
		if (x[i]<y[j]):
			sortedunion[k]=x[i]
			k = k+1
			i = i+1
		if (y[j]>x[i]]):
			sortedunion[k]=y[j]
			k = k+1
			j = j+1
	while(i<len(x)):	
		sortedunion[k]=x[i]
			k = k+1
			i = i+1
	while(j<len(y)):	
		sortedunion[k]=y[j]
			k = k+1
			j = j+1
	return(sortedunion)
	