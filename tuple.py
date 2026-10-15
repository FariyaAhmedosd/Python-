t1=(10,20,30,40,50,20)
print(t1[0])
print(t1[-1])
print(t1[1:4])
t2=(60,70,80,90,100)
print(t1+t2)#concatenation
print(t1*3)#repetition
#membership test
print(20 in t1)
print(100 in t1)
print(70 in t2)
print(10 in t2)
#tuple method
print(t1.count(20))#how many times the number is present
print(t1.index(50))
print(t2.index(100))#index of the number
#built in function
print(len(t1))
print(max(t1))
print(min(t1))
print(sum(t1))
print(sorted(t1))
print(sorted(t2))
person=("Fariya",21,"student")
name,age,profession = person
print(name)
print(age)
print(profession)
#empty tuple
a=()
print(type(a))
idol = ("Namjoon","29","BTS")
name,age,group = idol
print(name)
print(age)
print(group)