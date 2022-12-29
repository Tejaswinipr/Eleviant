def blackWhite(n):
    arr=[]
    for columns in range(n):
        row=[]
        for rows in range(n):
            if columns%2!=0 and columns!=n-1 and rows%2!=0 and rows!=n-1:
                color="white"
            else: 
                color="black"
            row.append(color)
        arr.append(row)
    for i in arr:
        print(i)

    

blackWhite(int(input("Enter the dimension:")))
