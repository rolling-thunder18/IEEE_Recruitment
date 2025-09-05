
while True: #starts a loop that continues till user inputs 0
    n=int(input("Enter the number of rows to display(enter 0 to exit): "))
    #adds conditions
    if n==0:
        break #a=breaks the code here aka ends loop with input 0
    for i in range(1,n+1):
        while i<=n: #loops till n
            print("* "*i)
            i+=1
        break


