

'''
lines=f.readlines()#line gulo k list akare dekhabes lines=f.readlines()#line gulo k list akare dekhabes
print(lines, type(lines))
line1=f.readline()
print(line1, type(line1))
line2=f.readline()
print(line2, type(line2))
line3=f.readline()
print(line3, type(line3))
'''
f = open("file.txt")
line=f.readline()#line variable e rakhsi file er text readline()diye read kori
while(line!=""):#jotokhkhon na file er text shesh hbe totokhkhon print hbe
    print( line)#read kora line print korbo
    line=f.readline()
f.close()

