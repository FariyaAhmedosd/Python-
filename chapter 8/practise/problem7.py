def rem(l,word):
  for item in l:
    l.remove(word)
    return l

l=["Harry","Roman","Nafis","Bal"]
print(rem(l,"Bal"))
