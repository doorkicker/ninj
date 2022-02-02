import random as rnd
import os
from math import *
from decimal import *
from primes import *

rnd.seed()
Dec = Decimal
d = Decimal



def floor(n):
  return n-(n%1)
  
  
def ceil(n):
  if n%1 != d(0):
    return floor(n)+1
  else:
    return n



#assume decimals
def findNs(a, b, cont=False, debug=False):
  p = a*b
  i = d(floor((log(p)/2)-1))
  #j = int(floor(log(p)*2))
  j = d(floor(((floor(log(p))*2)**2)/2))
  limit = d(ceil((p**d('0.5')) / d(floor(log(p)/2)-1)))
  limit = d(ceil(limit**(1/(3**d('0.5')))))
  s = ''
  ns = ''
  n = 0
  k = 0
  
  #ns = str(p)+str(i)+(str(p)[0:-1])+str(j)
  #j = ceil(int(ns)**(1/(e**2))

  while i <= limit:
    j = int((int(floor(log(p))*2)**2)/2)
    while j >= 3:
      ns = str(p)+str(i)+(str(p)[0:-1])+str(j)
      n = int(ns)
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
        
        _ = input("press [ENTER] to continue or type 'exit' to quit: ")
        #if _ == 'exit':
        #  return i, j, n, limit
        #else:
        #  k = 0
        if cont == False or _ == 'exit' or _ == 'e':
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


def nsRand(cont=False, pause=True):
  x = primes[rnd.randint(0, len(primes)-1)+2]
  y = primes[rnd.randint(0, len(primes)-1)+2]
  if x > y:
    _ = x
    x = y
    y = _
  findNs(x, y)
  print(f"a: {x},  b: {y}")
 

#TESTS
#nsRand()
findNs(d(17), d(41))