import math

def isPrime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	elif n % 2 == 0:
		return False

	sqrt = int(math.sqrt(n))
	i = 3
	while i <= sqrt:
		if n % i == 0:
			return False
		i += 2
	return True

values = [isPrime(int(i)) for i in input().split()]
for value in values:
	print("Prime" if value else "Not Prime")
