def altbw(n):
    arr=[]
    for columns in range(n):
        row=[]
        for rows in range(n):
            color="black" if columns%2==0 else "white"
            row.append(color)
        arr.append(row)
    for i in arr:
        print(i)


altbw(int(input("Enter the Dimension:")))