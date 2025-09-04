
while True:
    n=int(input("Enter the number of rows to display(enter 0 to exit): "))
    if n==0:
        break
    for i in range(1,n+1):
        while i<=n:
            print("* "*i)
            i+=1
        break
