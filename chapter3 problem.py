name=input("enter your name: ")
print("good afternoon "+name+" ")
name=input("What is your name? ")
print(f"Good Afternoon {name}")
#problem 2
letter = ''' Dear<|Name|>,
You are selected!
<|Date|> '''
print(letter.replace("<|Name|>", "harry").replace("<|Date|>", "24 september 2026"))
#double space detect
name=" harry is a good boy  "
print(name.find(" .."))
#string detect
name="punom is a good boy"
print(name.find(" good"))
name="Harry is a good boy and "
print (name.replace(" "," "))
print(name)
#problem 5
letter="Dear harry ,\n\t this python course is nice .Thanks!"
print(letter)
       

