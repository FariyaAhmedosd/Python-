#start pattern 
''' 
    * 
  *  *  *
*  *  *  *  *

*
* *
* * *
* * * *
* * * * *

* * *
*   *
* * *
'''
n=int(input("Enter a number: "))
for i in range(1, n+1):
   print(" "*(n-i), end="")
   print("*"* (2*i-1),end="")#3 line er formula (2*n-1)
   print("")
#2
n=int(input("Enter a number: "))
for i in range(1, n+1):
   print("*"*(i), end="")
   #print("*"* (2*i-1),end="")#3 line er formula (2*n-1)
   print("")
#3
n=int(input("Enter a number: "))
for i in range(1, n+1):
   if(i==1 or i==n):
     print("*"*n, end="")
   else:
     print("*", end="")
     print(" "* (n-2), end="")
     print("*", end="")
   print(" ")
   