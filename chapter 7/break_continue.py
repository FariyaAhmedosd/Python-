for i in range(100):
  if(i==34):
    break#exit the loop right now
  print(i)

for i in range(100):
  if(i==34):
    continue#skip this current iteration
  print(i)
#multiplication table
num=int(input("enter a number: "))
for i in range(1,11):#loop will run from 1 to 10
  print(f"{num}X{i}={num*i}")
#sum of even numbers
k=0
for i in range(1,51):
  if(i%2==0):
    k=k+i

print(k)
#countdown
i=10
while(i>=1):
  print(i)
  i-=1