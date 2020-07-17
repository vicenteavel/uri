def factorial(n):
   return 1 if n < 2 else n*factorial(n-1)

while True:
   try:
      numbers = input().split(" ")
      factorial_sum = 0

      for n in numbers:
         factorial_sum += factorial(int(n))
      
      print(factorial_sum)
   
   except EOFError:
      break