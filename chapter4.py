friends=["apple" ,"orange","banana","lichi"]
print(friends[0])
friends[0]="grape"#unlike strings links are changable
print(friends[0])
print(friends [1:4])
friends.append("strawberry")
print(friends)
l1=[23, 45,67,12,2,5,89,4]
print(len(l1))
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(3,100)#insert 100 at index 3
print(l1)
l1.pop(3)
print(l1)
print(max(l1))
print(min(l1))
print(sum(l1))

kpop=["bts","txt","aespa" ,"twice","katseye"]
print(kpop[1])
print(kpop[0:4])
kpop.append("ive")
print(kpop)
kpop.insert(2,"straykids")
print(kpop)
kpop.pop(3)#remove that index element
print(kpop)
kpop.reverse()
print(kpop)
kpop.extend(friends)
print(kpop)
len(kpop)
