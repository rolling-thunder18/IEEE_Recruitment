x=input("enter the paragraph: ")
y=x.split()

pld=[word for word in y if word==word[::-1] and len(word)>1]
if pld:
    print("the palindromes are: ",pld)
else:
    print(0)
