def natural_sum(n):
   if(n==1):
      return 1
   return n*(n+1)/2
n=int(input("Enter n: "))
print(f"Sum of  first 10{n} natural number is {natural_sum(n)}")