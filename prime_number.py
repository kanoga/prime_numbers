def isPrime(number):
    #handle the tests
    if not isinstance(number,int):
        return "The input must be a number only"
    #getting the prime numbers between 0 and the number
    a_list = [2]
    for i in range(3, number + 1):
    	prime = True
    	for j in range(2, i):
    		if i % j == 0:
    			prime = False
    	if prime:
    		a_list.append(i)
    return a_list