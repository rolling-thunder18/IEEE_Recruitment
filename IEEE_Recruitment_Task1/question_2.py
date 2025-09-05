x=input("enter the paragraph: ")
y=x.split() #splits the strings into individual words or list

pld=[word for word in y if word==word[::-1] and len(word)>1] #ignores single letter words 
if pld:
    print("the palindromes are: ",pld)
else:
    print(0)

