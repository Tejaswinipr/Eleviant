

def printPascal(n):
    digits=1
    for i in range (1,n+1):
        for j in range (1,(n-i)+1):
            print("  ",end="")
        midVal=digits//2    
        for k in range (digits):            #k=Position
            d=k+i
            if k>midVal:
                val=digits-(k-midVal)
                if val>9:
                    print(reduce(val),end=" ")

                else: 
                    print(val,end=" ")
            else:
                if d>9:
                    print(reduce(d),end=" ")
                else:
                    print(d,end=" ")
        print("\n")
        digits+=2

def reduce(x):
    while x>9:
        x=x-10
    return x


printPascal(int(input()))