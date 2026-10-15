s={1,7,5}
e=set()#dont use s={} it will create empty dictionary
s1={1,2,3,4,5,6,5,7,8,50}
s2={10,20,30,40,50,6,70,8}
s3={100,200,300}
print(s,type(s))
s1.add(555)#insert new element
print(s,type(s))
s1.remove(6)
print(s,type(s))
print(len(s))
print(s1.union(s2))#all
print(s1.intersection(s2))#overlap value
print(s1.difference(s2))#first set e ache kintu second set e nai
print(s1.symmetric_difference(s2))#common elements bade 2 set er unique elements niye
print(s.issubset(s1))#s er shb elements s1 e thakle true
print(s1.isdisjoint(s3))#2 ti set er modhdhe kono common elements na thakle
print(s1.issuperset(s))#s er shb elemets s1 e thakle s1 holo s er superset
print(max(s1))
print(min(s1))
print(sum(s))
print(s1-s)

