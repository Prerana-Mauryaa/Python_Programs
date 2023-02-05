#Write a program in Python to check whether an integer is Armstrong number or not.

num=int(input("enter the number"))
sum=0
temp=num
while num>0:
  rem=num%10
  cube=rem**3
  sum=sum+cube
  num=num//10
num=temp
if sum==temp:
  print("armstrong number")
else:
  print("not a armstrong number")
