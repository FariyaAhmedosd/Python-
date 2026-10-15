words ={
  "biral":"cat",
  "Kutta":"Dog",
  "belaja":"shameless",
  "ammu":"mother"
}
word = input("Enter the word you want to know the meaning:")
print(words[word])
#problem 2
s= set()
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
print(s)
#problem 3
s1=set()
s1.add(10)
s1.add("10")#same  value but one int and one string
print(s1)
print(len(s1))#2 ti alada type er value tai length 2 ashbe
#problem 5
s5={}
print(type(s5))#empty dictionary
#problem 6
d={}
name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name: lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name: lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name: lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name: lang})# dictionary te notun key:value add korte
#add diye kora jabe na..set e shudhu add use hoy
print(d)
#problem 9
s={8,"Punom",12,[20]}#error cz list k set er moddhe enter e kora jay na and set unmutable(change kora jabe na)


