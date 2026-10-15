def greatest(a,b,c):
   if(a>b and a>c):
      return a
   if(c>b and c>a):
      return c
   else:
      return b
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter a: "))


print(f"greatest number is: {greatest(a,b,c)}")