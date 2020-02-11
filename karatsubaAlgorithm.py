from math import log10
import math

def karatsuba(x,y):
  if (x<10) or (y<10):
    return x*y
  else:
    n=max(int(log10(x)+1),int(log10(y)+1))
    print(n)

    n_2 = int(math.ceil(n/2.0))
    if (n%2==0):
      n = n
    else:
      n=n+1
    print(n_2)

    a,b = divmod(x,10**n_2)
    c,d = divmod(y,10**n_2)
    print(a,b,c,d)

    ac=karatsuba(a,c)
    print(ac)
    bd=karatsuba(b,d)
    print(bd)
    ad_bc=(karatsuba((a+b),(c+d)))-ac-bd
    print(ad_bc)

    return (((10**n)*ac+((10**n_2)*(ad_bc))+bd))


print(karatsuba(40045,45234))