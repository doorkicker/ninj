import random as rnd
import os
from math import *
from decimal import *
from primes import *
from consolemenu import *
from consolemenu.items import *

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










  
'''
#######################################
FINDNS() applies template string manipulation to
product of two unique factors. It attempts to
find a matching value of I and J that cause
a certain solution mod a or mod b, to equal zero.
#######################################
'''
def findNs(a, b, cont=False, debug=True):
  p = a*b
  i = d(floor((log(p)/2)-1))
  #j = int(floor(log(p)*2))
  j = d(floor(((floor(log(p))*2)**2)/2))
  limit = d(ceil((p**d('0.5')) / (floor(logd(p)/2)-1)))
  limit = (ceil(limit**(1/(3**d('0.5')))))
  s = ''
  ns = ''
  n = 0
  k = 0
  
  #ns = str(p)+str(i)+(str(p)[0:-1])+str(j)
  #j = ceil(int(ns)**(1/(e**2))
  if debug == True:
    pause()
  while i <= limit:
    j = floor((d(floor(log(p))*2)**2)/2)
    #var_out(j, 'j', 54)
    while j >= 3:
      ns = str(p)+str(i)+(str(p)[0:-1])+str(j)
      n = d(ns)
      valA = (n%(p-1))%a
      valB = (n%(p-1))%b
      if valA == 0 or valA == 1 or valB == 0 or valB == 1:
        _ = input("found valA or valB that equals either 1 or 0")
      print(f"ns%a: {ns}, val: {valA},  ij: {i}, {j}")
      print(f"ns%b: {ns}, val: {valB},  ij: {i}, {j}")
      if (n%(p-1))%a == 0 or (n%(p-1))%b == 0:
        print(f"found ns value that works!,  total iterations: {k}, ratio over a: {k/a},  ij: {i}, {j}")
        print(f"limit: {limit} , a: {a}, b: {b}")
        print(f"p: {p}, k: {k}")
        
        pause()
        if cont == False:
          return i, j, n, limit
        else:
           k = 0
        
        j = j - 1
        k = k + 1
      else:
        j = j - 1
        k = k + 1
    i = i + 1
  
  #else
  print("no exact match found. Returing None.")
  return None




















'''
#######################################
NSRAND() runs findNs() on a randomly generated set of factor, a, and b.
#######################################
'''
def nsRand(cont=False, pause=True):
  x = primes[rnd.randint(0, len(primes)-1)+2]
  y = primes[rnd.randint(0, len(primes)-1)+2]
  if x > y:
    _ = x
    x = y
    y = _
  findNs(d(x), d(y))
  print(f"a: {x},  b: {y}")
 


























'''
#######################################
TEST_FACTORS() gets user input of some prime numbers for factor x, and factor y.
If the inputs are blank, it selects one from the list of given primes included with nsbase.py
It then asks the user if they want to output the whole set of possible solutions to findNs, or
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
  if output_set in ['', 'no', 'n']: 
    findNs(a, b, False, False)
  else:
    findNS(a, b, True, False)
  
  
  pause()

#TESTS
#nsRand()
#findNs(d(17), d(41))

def main():
  menu = ConsoleMenu("Number Swap Factorization", "Based on factor tree conversion to smooth integer 'palettes'")
  menu_testfactors = FunctionItem("Test factors", test_factors)
  
  
  menu.append_item(menu_testfactors)
  menu.show()

if __name__ == '__main__':
  main()
  