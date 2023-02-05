#Write a program in Python to print the Fibonacci series using iterative method

n=int(input("enter how many terms you want"))
first=0
second=1
for i in range(n):
  print(first,end=" ")
  third=first+second
  first=second
  second=third
