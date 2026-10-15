def InchtoCenti(inch):
   return inch*2.54

n = int(input("enter value in inches: "))
print(f"The corresponding value in cms is {InchtoCenti(n)}")