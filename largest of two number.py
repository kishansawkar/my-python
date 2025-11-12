def largest_of_two_numbers(a,b):
  a = int(input("enter the first number :"))
  b = int(input("enter the second number"))
  if a > b and b < a:
    print("largest number is :" , a)
    print(a)
  else:
    print("largest number is :" , b)
    print(b)
  return a , b
largest_of_two_numbers(a,b)
