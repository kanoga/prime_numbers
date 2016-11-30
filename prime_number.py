def isPrime(number):
    if (number>=1000):
        print "number too large!!!"
    if isinstance(number,float):
        return "The number must be a whole number"
    if isinstance(number,tuple):
        return "The input must not be a tuple"
	#getting the prime numbers between 0 and the number
	a_list = [2]
	for i in range(3,number+1):
		prime = True
		for j in range(2,1):
			if i % j == 0:
				prime == False
		if prime:
			a_list.append(i)
	return(a_list)
    
