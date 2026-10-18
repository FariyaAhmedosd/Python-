st="Hey Punom you are amazing"
f=open("myfile.txt", "w")#ekta notun file "myfile.txt" create hbe 
f.write(st)
f.close()
st="Hey Punom you are amazing"
f=open("myfile.txt",  "a")#a=append same text abr line e add hbe
f.write(st)
f.close()
st="Hey Punom you are amazing"
f=open("myfile.txt","+")#file update kora jabe 
f.write(st)
f.close()
st="Hey Punom you are amazing"
f=open("myfile.txt","rb")#ekta notun file "myfile.txt" create hbe 
f.write(st)
f.close()