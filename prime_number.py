def isPrime(number):
	#getting the prime numbers between 0 and the number
	a_list = [2]
	for i in range(3,number+1):
		prime = True
		for j in range(2,1):
			if i % j == 0:
				print == False
		if prime:
			a_list.append(i)
	return(a_list)
