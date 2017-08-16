#!/usr/bin/python

def func(value):
	while value >0 :
		if isPrime(value) == 1:
			print value
		value -= 1

def isPrime(value):
	for index in range(2, value+1, 1):
		if value % index == 0:
			if value == index:
				return 1
			return 0
						
print func(15)

	
