def prime_nums():
	#We define the range between 0 and 100
	for num in range(0,100):
   	#All prime numbers are greater than 1
	    if num > 1:
	        for i in range(2, num):
	        	#If number is not prime we skip it
	            if (num % i) == 0:
	            	break
	        else:
	        	print(num)

prime_nums()