msg=input("Enter  the comment: ")
p1="make a lot of money"
p2="buy now"#case sensitive python
p3="subscribe this"
p4="click this"
if ((p1 in msg) or (p2 in msg) or(p3 in msg) or (p4 in msg)):
   print("The comment is spam")
else:
   print("The comment is  not a spam")

#problem 4
username=input("enter a user name: ")
if(len(username)<10):
   print("Your username contains less than 10 characters")
else:
   print("your username is less or greater than 10 characters")
  #problem 5
l =["Harry", "Rohan","Punom","Tanjina"]#list[],tuple(),set{},string("")
name = input("Enter your name: ")
if(name in l ):
   print("Your name is in the list")
else:
   print("Your name is not in the list")
   #problem 6
post=input("enter the post: ")
if("fariya" in post.lower()):#post e fariya jei form ei thakuk sheta identify hbe
   print("this post is about fariya")
else:
   print("this post is not about fariya")