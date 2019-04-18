import math
import time

# Matrix class with functionality added as needed
class Matrix:
	def __init__(self, row = 0, col = 0):
		self.row = row
		self.col = col
		self.matrix = []

	def __str__ (self):
		s = '\n'
		for i in range(self.row):
			for j in range(self.col):
				s = s + str(self.matrix[i][j]).rjust(4) + ' '
			s = s + '\n'
		s = s + '\n'
		return s

	def populate(self, string):
		string = string.split(' ')
		for i in range(self.row):
			new = []
			self.matrix.append(new)
			for j in range(self.col):
				self.matrix[i].append(int(string[(self.col * i) + j]))

class ProblemList:
	def __init__(self):
		self.solved = []
		for name in (dir(self)):
			if name[0] == 'p':
				num = int(name[1:])
				entry = [num]
				self.solved.append(entry)
		self.solved.sort()
		print(self.solved)

	def addName(self, num, s):
		for p in self.solved:
			if p[0] == int(num):
				p.append(s)


	# Prime helper function for future problems(takes an int number and a list of potential
	# prime factors)
	def isPrime(self, x, primes):
		x = int(x)
		limit = math.ceil(math.sqrt(x)) + 1
		for num in primes:
			if num > limit:
				break
			if (x % num == 0) and (x != num):
				return False

		return True

	# Helper function to find the number of factors of a given integer
	def numFactors(self, x):
		factors = 0
		limit = math.ceil(math.sqrt(x))
		for i in range(1, limit):
			if x % i == 0 and x != i:
				factors += 2
		if limit == math.sqrt(x):
			factors += 1
		return factors

	# Returns a list of the factors of a given integer
	def listFactors(self, x):
		if x == 0:
			return [0]
		factors = []
		limit = math.ceil(math.sqrt(x))
		for i in range(1, limit):
			if x % i == 0 and x != i:
				factors.append(i)
				factors.append(x // i)
		if limit == math.sqrt(x):
			factors.append(limit)
		return sorted(factors)

	# Dixon's factorization method to (hopefully) quickly factor large integers
	def dixFactor(self, x, b):
		primes = []
		for i in range(1, b):
			if self.isPrime(i + 1, primes):
				primes.append(i + 1)

		return

	# Finds the sum of all multiples of 3 or 5 below 1000
	def p1(self):
		print('\nWhat is the sum of all multiples of 3 or 5 below 1000?')

		result = 0

		for i in range(1000):

			if (i % 3 == 0 or i % 5 == 0):
				result += i

		return (result)

	# Finds the sum of all the even Fibonacci numbers below four million
	def p2(self):
		print('\nWhat is the sum of all the even Fibonacci numbers below four million?')
		prev1 = 1
		prev2 = 1
		fib = 1
		result = 0
	
		while fib <= 4000000:
	
			if (fib % 2 == 0):
				result += fib
	
			prev2 = prev1
			prev1 = fib
			fib  = prev1 + prev2
	
		return (result)

	# Finds the largest prime factor of 600851475143
	def p3(self):
		print('\nWhat is the largest prime factor of 600851475143?')
		num = 600851475143
		primeFactor = 2
	
		while num != 1:
			if num % primeFactor == 0:
				num = num // primeFactor
			else:
				primeFactor += 1
	
		return(primeFactor)

	# Palindrome helper function for problem 4
	def isPalindrome(self, x):
		x = str(x)
		return x[:] == x[::-1]

	# Finds the largest palindrome made from the product of two 3-digit
	# numbers
	def p4(self):
		print('\nWhat is the largest palindromic number made from the product of two 3-digit numbers?')
		largestPalindrome = 0
		palindromeFactors = [0, 0]
		flag = False
	
		for i in range(1000, 100, -1):
			for j in range(1000, 100, -1):
				product = i * j
				factors = [i, j]
				if self.isPalindrome(product) and product > largestPalindrome:
					largestPalindrome = product
					palindromeFactors = factors
				elif  (factors[0] < palindromeFactors[0] and factors[0] < palindromeFactors[1]) and (factors[1] < palindromeFactors[0] and factors[1] < palindromeFactors[1]):
					flag = True
				if flag:
					break
			if flag:
				break

		return(largestPalindrome)

	# Finds the smallest positive number that is evenly divisible by all
	# of the numbers from 1 to 20
	def p5(self):
		print('\nWhat is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?')
		num = 1
		
		for i in range(20, 1, -1):
			if num % i != 0:
				num = num * i
		
		return num

	# Finds the difference between the sum of the squares of the first one
	# hundred natural numbers and the square of the sum of those numbers
	# abs((1^2 + 2^2 + ... + 100^2) - (1 + 2 + ... + 100)^2)
	def p6(self):
		print('\nWhat is the difference between the sum of the squares of the first one hundred natural numbers, and the square of the sum of those numbers?')
		sumSquares = 0
		squareSum = 0
	
		for i in range(1, 101):
			squareSum = squareSum + i
			val = i * i
			sumSquares = sumSquares + val
	
		squareSum = squareSum * squareSum
		difference = abs(squareSum - sumSquares)

		return(difference)
 
	# Finds the 10001st prime number
	def p7(self):
		print('\nWhat is the 10001st prime number?')
		run = True
		num = 2
		primes = []
		count = 0
		while run:
			if self.isPrime(num, primes):
				count += 1
				primes.append(num)
			if count == 10001:
				run = False
			else:
				num += 1
		return num

	# Finds the 13 adjacent digits in a certain 1000 digit number
	# that have the greatest product
	def p8(self):
		num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
		string = str(num)
		print('\nWhat 13 adjacent digits of the following 1000 digit number have the greatest product?')
		print('number: ' + string)

		maxProduct = 0
		for i in range(987):
			product = 1
			for j in range(13):
				product = product * int(string[i + j])
			if product > maxProduct:
				maxProduct = product

		return maxProduct

	# Finds the Pythagorean triple for which a + b + c = 100,
	# and returns the product abc	
	def p9(self):
		self.addName(9, 'Special Pythagorean triplet')
		print("\nThere is exactly one Pythagorean triple (a^2 + b^2 = c^2) for which a + b + c = 1000. What is the product abc of that triple?")
		squares = []

		for i in range(1, 1001):
			x = i
			squares.append(x * x)

		for i in range(1, 1001):
			for j in range(i + 1, 1001):
				result = (i * i) + (j * j)
				if result in squares:
					c = (squares.index(result)) + 1
					d = i + j + c
					if d == 1000:
						print('triple: ' + str(i) + '^2 + ' + str(j) + '^2 = ' + str(c) + '^2')
						return i * j * c

		return None

	# Finds the sum of all primes below two million
	def p10(self):
		self.addName(10, 'Summation of primes')
		print('\nWhat is the sum of all primes below two million?')
		result = 0
		primes = []

		for i in range(2, 2000001):
			if self.isPrime(i, primes):
				result = result + i
				primes.append(i)

		return result

	# Finds the four adjacent (in a straight line) numbers in a certain grid 
	# that have the largest product
	def p11(self):
		self.addName(11, 'Largest product in a grid')
		print('\nWhat is the largest product of four adjacent numbers (in a straight line) in the following grid?')
		# The grid is 20 by 20
		grid = Matrix(20, 20)
		# I copied the grid from ProjectEuler.net
		string = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
		grid.populate(string)
		print('Grid: ' + str(grid))
		limit = (20 * 20) - 4
		largestProduct = 0
		for i in range(grid.row):
			for j in range(grid.col):
				# Find forward product
				try:
					prod = grid.matrix[i][j] * grid.matrix[i][j + 1] * grid.matrix[i][j + 2] * grid.matrix[i][j + 3]
					if prod > largestProduct:
						largestProduct = prod
				except IndexError:
					pass
				# Find downward product
				try:
					prod = grid.matrix[i][j] * grid.matrix[i + 1][j] * grid.matrix[i + 2][j] * grid.matrix[i + 3][j]
					if prod > largestProduct:
						largestProduct = prod
				except IndexError:
					pass
				# Find left to right diagonal
				try:
					prod = grid.matrix[i][j] * grid.matrix[i + 1][j + 1] * grid.matrix[i + 2][j + 2] * grid.matrix[i + 3][j + 3]
					if prod > largestProduct:
						largestProduct = prod
				except IndexError:
					pass
				# Find left-to right diagonal 
				try:
					prod = grid.matrix[i][j] * grid.matrix[i + 1][j - 1] * grid.matrix[i + 2][j - 2] * grid.matrix[i + 3][j - 3]
					if prod > largestProduct:
						largestProduct = prod
				except IndexError:
					pass
		return largestProduct

	# Helper function for problem 12 that returns the nth triangle number
	def getTriangle(self, n):
		return (n * (n + 1)) // 2

	# Finds the first triangle number to have over five hundred divisors
	def p12(self):
		self.addName(12, 'Highly divisible triangular numbers')
		print('\nWhat is the first triangle number to have over five hundred divisors?')
		count = 1
		while True:
			tri = self.getTriangle(count)
			f = self.numFactors(tri)
			if f > 500:
				return tri
			count += 1

	# Note: rewrite to run more efficiently! Many repeated calculations in this code
	def p14(self):
		self.addName(14, 'Longest Collatz sequence')
		print('\nWhich number under one million produces the longest Collatz sequence?')
		longest = [0, 0]
		for i in range(1000000, 1, -1):
			num = i
			length = 0
			while num != 1:
				if num % 2 == 0:
					num = num // 2
				else:
					num = num * 3 + 1
				length += 1
			if length > longest[1]:
				longest = [i, length]
		return longest[0]

	# Given a 20 x 20 grid, how many routes are there from the top left corner to the bottom
	# right corner, if you can only move down or rightward?
	def xv_Recursive(self, x, y):
		if x < 20 and y < 20:
			self.xv_Recursive(x + 1, y)
			self.xv_Recursive(x, y + 1)
		elif x == 20 and y < 20:
			self.xv_Recursive(x, y + 1)
		elif x < 20 and y == 20:
			self.xv_Recursive(x + 1, y)
		elif x == 20 and y == 20:
			print(self.num_paths, 'paths found')
			self.num_paths += 1
			return


	def p15(self):
		self.addName(15, 'Lattice paths')
		print('How many possible paths are there through a 20x20 lattice using only downward and rightward steps?')
		''' I think the recursive method works, but it takes much too long!!

		self.num_paths = 0
		self.xv_Recursive(1, 1)
		return self.num_paths'''

		'''The path must consist of 20 steps to the right and 20 steps down.
		There are always 40 steps in each route.
		The number of ways to 'place' the 20 rightward steps in
		the 40 'slots' is 20C40, or (40!)/(20! * 20!).
		Once we do this, there is only 1 way to place the downward steps.'''
		
		fact1 = 1
		fact2 = 1
		for i in range(1, 41):
			fact1 = fact1 * i
			if i <= 20:
				fact2 = fact2 * i

		num_paths = (fact1)/(fact2 * fact2)
		return num_paths

	def p16(self):
		self.addName(16, 'Power digit sum')
		print('What is the sum of the digits of two to the one thousandth power?')
		num = 2**1000
		string = str(num)
		result = 0

		for i in range(len(string)):
			digit = int(string[i])
			result += digit

		return result

	def num_to_string(self, x):
		x = str(x)
		for i in range(len(x),0, -1):
			print(i)

	def p16(self):

		return




def main():
	pList = ProblemList()
	run = True
	print('\nSolved problems: ')
	for prob in pList.solved:
		#print(str(prob[0]) + ':', str(prob[1]))
		print(prob)
	while run:
		string = input('\nWhich problem would you like to run?\nEnter a problem number, a range (e.g. "1-3"), or "all": ')
		string = string.lower()
		string = 'p' + string
		start = time.time()
		result = getattr(pList, string)()
		end = time.time()
		elapsed = end - start
		print('\nresult: ' + str(result))
		print('\nThis problem took ' + str(elapsed) + ' seconds to solve.')
		r = input('\nAny other questions(y/n)? ')
		r = r.lower()
		run = (r == 'y')
	
main()