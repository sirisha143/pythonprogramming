a=int(input("enter a year"))
if a%4==0 and a%400==0 and a%100==0:
  print("yes")
else:
  print("no")
