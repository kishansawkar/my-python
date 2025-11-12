def simple_interest(P,r,t):
  p = int(input("enter the principal amount :"))
  r = float(input("enter the rate :"))
  t = int(input("enter the time :"))
  simple_interest = (p * r * t) / 100
  return simple_interest
  print("simple interest is :" , simple_interest)
simple_interest(5,10,15)
