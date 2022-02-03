import random as rnd
import os
from math import *
from decimal import *
from primes import *
from consolemenu import *
from consolemenu.items import *
from statistics import *

rnd.seed()
Dec = Decimal
d = Decimal

mult = 1
getcontext().prec = 64*mult


def floor(n):
  return n-(n%1)
  
  
def ceil(n):
  if n%1 != d(0):
    return floor(n)+1
  else:
    return n
    
def pause(s=None):
  if s == None:
    _ = input("press [ENTER] to continue.")
  else:
    _ = input(s + ". press [ENTER] to continue.")

def type_out(var, s):
  print(f"{s} type floor: {type(var)}")
  pause()

def var_out(var, s, line=None):
  print(f"{s} value: {var}, type: {type(var)}, line: {line}")
  pause()

def logd(var):
  return d(log(var))



z = Decimal('0E-64')


def factor(var):
  i = 0
  factors = []
  current = var
  while i < len(primes):
    #keep dividing it, until it cant be divided anymore, and THEN increment index
    if (current/d(primes[i]))%1 == d('0'):
      factors.append(d(primes[i]))
      current = current/d(primes[i])
    else:
      i = i + 1
  
  
  #print(("current: " + str(current)[:32] + ",  factors: " + str(factors)))
  #return current, factors
  return factors




























first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
					31, 37, 41, 43, 47, 53, 59, 61, 67, 
					71, 73, 79, 83, 89, 97, 101, 103, 
					107, 109, 113, 127, 131, 137, 139, 
					149, 151, 157, 163, 167, 173, 179, 
					181, 191, 193, 197, 199, 211, 223, 
					227, 229, 233, 239, 241, 251, 257, 
					263, 269, 271, 277, 281, 283, 293, 
					307, 311, 313, 317, 331, 337, 347, 349] 

def nBitRandom(n): 
	return rnd.randrange(Dec(2)**(n-1)+1, 2**n - 1) 

def getLowLevelPrime(n): 
	'''Generate a prime candidate divisible 
	by first primes'''
	while True: 
		# Obtain a random number 
		pc = nBitRandom(n) 

		# Test divisibility by pre-generated 
		# primes 
		for divisor in first_primes_list: 
			if pc % divisor == 0 and divisor**2 <= pc: 
				break
		else: return pc 








# Utility function to do 
# modular exponentiation. 
# It returns (x^y) % p 
def power(x, y, p): 
	
	# Initialize result 
	res = 1; 
	
	# Update x if it is more than or 
	# equal to p 
	x = x % p; 
	while (y > 0): 
		
		# If y is odd, multiply 
		# x with result 
		if (y & 1): 
			res = (res * x) % p; 

		# y must be even now 
		y = y>>1; # y = y/2 
		x = (x * x) % p; 
	
	return res; 




# This function is called 
# for all k trials. It returns 
# false if n is composite and 
# returns false if n is 
# probably prime. d is an odd 
# number such that d*2<sup>r</sup> = n-1 
# for some r >= 1 
def miillerTest(d, n): 
	
	# Pick a random number in [2..n-2] 
	# Corner cases make sure that n > 4 
	a = 2 + rnd.randint(1, n - 4); 

	# Compute a^d % n 
	x = power(a, d, n); 

	if (x == 1 or x == n - 1): 
		return True; 

	# Keep squaring x while one 
	# of the following doesn't 
	# happen 
	# (i) d does not reach n-1 
	# (ii) (x^2) % n is not 1 
	# (iii) (x^2) % n is not n-1 
	while (d != n - 1): 
		x = (x * x) % n; 
		d *= 2; 

		if (x == 1): 
			return False; 
		if (x == n - 1): 
			return True; 

	# Return composite 
	return False; 



# It returns false if n is 
# composite and returns true if n 
# is probably prime. k is an 
# input parameter that determines 
# accuracy level. Higher value of 
# k indicates more accuracy. 
def isPrime(n, k): 
	
	# Corner cases 
	if (n <= 1 or n == 4): 
		return False; 
	if (n <= 3): 
		return True; 

	# Find r such that n = 
	# 2^d * r + 1 for some r >= 1 
	d = n - 1; 
	while (d % 2 == 0): 
		d //= 2; 

	# Iterate given nber of 'k' times 
	for i in range(k): 
		if (miillerTest(d, n) == False): 
			return False; 

	return True; 




def getPrime(bits):
  i = 0
  while isPrime(i, 40) == False:
    i = getLowLevelPrime(bits)
  
  return i




#GENERATE PRIMES
def gen_factors(min_ratio=d('10000'), max_ratio=d('1000000')):
  print("begin generating factors....")
  dif = 0
  a_low = 16 * mult
  a_high = 32 * mult
  b_low = 32 * mult
  b_high = 48 * mult
  while True:
    print("generating...")
    a = Dec(getPrime(Dec(rnd.randint(a_low, a_high))))
    b = Dec(getPrime(Dec(rnd.randint(b_low, b_high))))
    if a > b:
      _ = a
      a = b
      b = _
      
    dif = b/a
    print("done generating. ")
    #if dif <= maxRatio and dif >= minRatio:
    #  break
    break
    #if dif >= minRatio and dif <= maxRatio:
    #  break
  
  return a, b



















  
'''
#######################################
FIND_NS() applies template string manipulation to
product of two unique factors. It attempts to
find a matching value of I and J that cause
a certain solution mod a or mod b, to equal zero.
#######################################
'''
def find_ns(a, b, cont=False, debug=True):
  results = []
  p = a*b
  
  #INITIALIZE I
  istart = d(str(floor((logd(p)/2)-1))) #I type0
  #istart = d(0)                    #I type1
  
  i = d(str(istart).split('.')[0])
  
  
  
  #INITIALIZE J
  #jstart = d(floor(logd(p)*2))              #J type0
  jstart = floor(((floor(logd(p))*2)**2)/2) #J type1
  #jstart = ceil(d(ns)**(1/(d(e)**2)))          #J type3 #has to be activated below, along with one of the others
  
  j = d(str(jstart).split('.')[0])
  
  # ###############
  #   LIMITS TYPES
  # ###############
  #these two calls are dependant on eachother.
  #JLIMIT type0
  limit_root = d(ceil((p**d('0.5')) / (floor(logd(p)/2)-1)))
  limit_root = (ceil(limit_root**(1/(3**d('0.5')))))
  
  #limit_root = d(ceil((p**d('0.5')) / (floor(logd(p)/2)-1))) #35
  
  
  '''
  #JLIMIT type0a
  limit_base = (ceil(limit_root**(1/(3**d('0.5'))))) #35
  limit_super = limit_base**2 #1225
  limit_mid = floor(limit_super/2) #612
  limit_upper = ceil((limit_super*limit_mid).sqrt()) #207
  jlimit = floor((limit_base/2)**2)
  j = limit_mid-limit_upper #J type2
  '''
  
  
  # ########
  #  LIMITS
  # ########
  #limit = limit_base = limit_root**2
  limit = limit_root
  jlimit = floor(floor((d(floor(log(p))*2)**2)/2)/2) #JLIMIT type1
  #jlimit = floor((limit_root**2)/2)
  #jlimit = d(0)
  
  
  #MISC
  s = ''
  ns = ''
  n = 0
  k = 0
  ab_type = ''
  ns = str(p)+str(i)+(str(p)[0:-1])+str(j)
  #jstart = ceil(d(ns)**(1/(d(e)**2)))          #J type3
  
  
  # #####
  # BEGIN
  # #####
  if debug == True:
    var_out(j, "j")
    var_out(jlimit, "jlimit")
    var_out(limit, "limit")
    var_out(i, "i")
    pause()
  
  while i <= limit:
    j = jstart
    while j >= jlimit:
      ns = str(p)+str(i)+(str(p)[0:-1])+str(j)
      #print("p, i, p[0:-1], j, ns")
      #var_out(p, "p")
      #var_out(i, "i")
      #var_out(str(p)[0:-1], "str(p)[0:-1]")
      #var_out(j, "j")
      #print(ns)
      #pause()
      n = d(ns)
      valA = (n%(p-1))%a
      valB = (n%(p-1))%b
      #if valA == 0 or valB == 0 :
      #  _ = input("found valA or valB that equals either 1 or 0")
      print(f"ns%a: {ns}, val: {valA},  ij: {i}, {j}")
      print(f"ns%b: {ns}, val: {valB},  ij: {i}, {j}")
      #if (n%(p-1))%a == 0 or (n%(p-1))%b == 0:
      if valA == 0 or valB == 0:
        print(f"found ns value that works!,  total iterations: {k}, ratio over a: {k/a},  ij: {i}, {j}")
        print(f"limit: {limit} , a: {a}, b: {b}")
        print(f"p: {p}, k: {k}")
        if valA == 0:
          abtype = "A"
        else:
          abtype = "B"
        #pause()
        if cont == False:
          results.append({'i': i, 'j': j, 'n': n, 'limit': limit, 'np1': n%(p-1), 'abtype': abtype, 'ktotal': k, 'ratio': k/a})
          print(results)
          return results
        else:
          results.append({'i': i, 'j': j, 'n': n, 'limit': limit, 'np1': n%(p-1), 'abtype': abtype, 'ktotal': k, 'ratio': k/a})
          k = 0
        
        j = j - 1
        k = k + 1
      else:
        j = j - 1
        k = k + 1
    i = i + 1
  
  #else
  if len(results) == 0:
    print("no exact match found")
    #return None
    return results #empty list
  else:
    print(results)
    return results






























def ns_factor(p, cont=False, debug=True):
  
  results = []
  
  #INITIALIZE I
  istart = d(str(floor((logd(p)/2)-1))) #I type0
  #istart = d(0)                    #I type1
  
  i = d(str(istart).split('.')[0])
  
  
  
  #INITIALIZE J
  #jstart = d(floor(logd(p)*2))              #J type0
  jstart = floor(((floor(logd(p))*2)**2)/2) #J type1
  #jstart = ceil(d(ns)**(1/(d(e)**2)))          #J type3 #has to be activated below, along with one of the others
  
  j = d(str(jstart).split('.')[0])
  
  # ###############
  #   LIMITS TYPES
  # ###############
  #these two calls are dependant on eachother.
  #JLIMIT type0
  limit_root = d(ceil((p**d('0.5')) / (floor(logd(p)/2)-1)))
  limit_root = (ceil(limit_root**(1/(3**d('0.5')))))
  
  #limit_root = d(ceil((p**d('0.5')) / (floor(logd(p)/2)-1))) #35
  
  
  '''
  #JLIMIT type0a
  limit_base = (ceil(limit_root**(1/(3**d('0.5'))))) #35
  limit_super = limit_base**2 #1225
  limit_mid = floor(limit_super/2) #612
  limit_upper = ceil((limit_super*limit_mid).sqrt()) #207
  jlimit = floor((limit_base/2)**2)
  j = limit_mid-limit_upper #J type2
  '''
  
  
  # ########
  #  LIMITS
  # ########
  #limit = limit_base = limit_root**2
  limit = limit_root
  jlimit = floor(floor((d(floor(log(p))*2)**2)/2)/2) #JLIMIT type1
  #jlimit = floor((limit_root**2)/2)
  #jlimit = d(0)
  
  
  #MISC
  s = ''
  ns = ''
  n = 0
  k = 0
  ab_type = ''
  total = None
  x = None
  ls = None
  ns = str(p)+str(i)+(str(p)[0:-1])+str(j)
  #jstart = ceil(d(ns)**(1/(d(e)**2)))          #J type3
  
  
  # #####
  # BEGIN
  # #####
  if debug == True:
    var_out(j, "j")
    var_out(jlimit, "jlimit")
    var_out(limit, "limit")
    var_out(i, "i")
    pause()
  
  while i <= limit:
    j = jstart
    while j >= jlimit:
      ns = str(p)+str(i)+(str(p)[0:-1])+str(j)
      n = d(ns)
      
      x = None
      total = n%(p-1)
      ls = factor(n%(p-1))
      for x in ls:
        total = total/x
      
      print(f"n: {ns}, val: {total},  ij: {i}, {j}")
      
      if p%total == 0 and total != p and total > 1:
        x = total
        y = p/total
        if x > y:
          a = y
          b = x
        else:
          a = x
          b = y
        print(f"found factor! p: {p},  a: {p/total},  b: {total}")
        print(f"found ns value that works!,  total iterations: {k}, ratio over a: {k/a},  ij: {i}, {j}")
        if cont == False:
          results.append({'i': i, 'j': j, 'n': n, 'limit': limit, 'np1': n%(p-1), 'ktotal': k, 'ratio': k/a, 'a': a, 'b': b})
          print(results)
          if debug == True:
            pause()
          return results
        else:
          results.append({'i': i, 'j': j, 'n': n, 'limit': limit, 'np1': n%(p-1), 'ktotal': k, 'ratio': k/a, 'a': a, 'b': b})
          #k = 0
        
        j = j - 1
        k = k + 1
      else:
        j = j - 1
        k = k + 1
    i = i + 1
  
  #else
  if len(results) == 0:
    print("no exact match found")
    #return None
    if debug == True:
      pause()
    return results #empty list
  else:
    print(results)
    if debug == True:
      pause()
    return results









'''
#######################################
NSRAND() runs find_ns() on a randomly generated set of factor, a, and b.
#######################################
'''
def nsRand(cont=False, pause=True):
  x = primes[rnd.randint(0, len(primes)-1)+2]
  y = primes[rnd.randint(0, len(primes)-1)+2]
  if x > y:
    _ = x
    x = y
    y = _
  find_ns(d(x), d(y))
  print(f"a: {x},  b: {y}")
 


























'''
#######################################
TEST_FACTORS() gets user input of some prime numbers for factor x, and factor y.
If the inputs are blank, it selects one from the list of given primes included with nsbase.py
It then asks the user if they want to output the whole set of possible solutions to find_ns, or
just return the first generated.
#######################################
'''
def test_factors():
  print("leaving a factor blank will generate one for you")
  factor_x = input("Enter factor to test: ")
  factor_y = input("Enter second factor: ")
  
  swap = ''
  swap = input("swap factors so smallest factor is A and largest factor is B? y/n: ")
  swap = str.lower(swap)
  if swap in ['n', 'no']:
    print("keeping input order.")
  elif swap in ['', 'y', 'yes']:
    print("defaulting to A<B.")
    if factor_x == '':
      factor_x = d(rnd.choice(primes))
    
    if factor_y == '':
      factor_y = d(rnd.choice(primes))
    
    if factor_x > factor_y:
      a = d(factor_y)
      b = d(factor_x)
    else:
      a = d(factor_x)
      b = d(factor_y)
  
  output_set = input("output set of solutions instead of first? y/n (leave blank for 'no'): ")
  
  print(f"factors - a: {a},  b: {b}")
  pause()
  
  results = None
  if output_set in ['', 'no', 'n']: 
    results = find_ns(a, b, False, False)
  else:
    results = find_ns(a, b, True, False)
  
  
  pause()


























'''
#######################################
factor_prod() takes  specific product, without factors, and attempts to use the template method
to find a factor by calling ns_factor
#######################################
'''
def factor_prod():
  p = input("enter a product to factor, leave blank to have one randomly generated for you: ")
  if p == '' or p == None:
    a, b = gen_factors(d(1000), d(10000))
    p = a*b
  else:
    p = d(p)
  result = ns_factor(p)
  
  pause()














#TESTS
#nsRand()
#find_ns(d(17), d(41))

def main():
  menu = ConsoleMenu("Number Swap Factorization", "Based on factor tree conversion to smooth integer 'palettes'")
  menu_testfactors = FunctionItem("Test factors", test_factors)
  menu_factor_rand = FunctionItem("Factor a product of your choosing", factor_prod)
  
  menu.append_item(menu_testfactors)
  menu.append_item(menu_factor_rand)
  menu.show()

if __name__ == '__main__':
  main()
  