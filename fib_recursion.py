#Write a program in Python to print the Fibonacci series using recursive method.

def fib(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fib(n-2)+fib(n-1)
n=int(input("enter the number of terms"))
for i in range(1,n+1):
    term=fib(i)
    print(term)
