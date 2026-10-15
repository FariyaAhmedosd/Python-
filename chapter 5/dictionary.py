marks={
  "Harry":100,
  "Punom":70,
  "Shohan":80
}
print(marks,type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
#print(marks["Harry2"])#error
print(marks.get("Harry2"))#none

#dictionary(like list,strig,tuple)
#like struct
kpop={
  "BTS":3,
  "TXT":4,
  "Twice":3
}
print(kpop,type(kpop))
print(kpop.items())
print(kpop.keys())
print(kpop.values())
kpop.update({"TXT":5, "Enhypen":6})
print(kpop.get("TXT"))# by get we can get the value not the key
print(kpop)
a={
  "name":"punom",
   "age":24,
   "CGPA":3.68,
   "marks":[80,85,90,95]
}
print(a,type(a))
print(a.items())
print(a.keys())
print(a.values())
print(a.get("CGPA"))
a.update({"CGPA":3.75})
print(a.get("CGPA"))
print(a)
a.pop("marks")#delete 
print(a)
print(len(a))#koyti key-value pair ache ta dekhay
print(str(a))#dictionary k string format e convert kore
