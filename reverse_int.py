#Write a program to reverse an integer in Python

integer=int(input("enter the integer you want to reverse"))
sum=0
while integer>0:
  num=integer%10
  sum=sum*10 +num
  integer=integer//10
print(sum)
