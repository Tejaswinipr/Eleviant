def blackWhite(n):
    arr=[]
    for columns in range(n):
        row=[]
        for rows in range(n):
            if columns==0 or columns==n-1 or rows==0 or rows==n-1:
                color="black"
            else: 
                color="white"
            row.append(color)
        arr.append(row)
    for i in arr:
        print(i)
    

blackWhite(int(input("Enter the dimension:"))) 