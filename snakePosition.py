def findRow(dimension,number):
    rowNum=0
    while True:
        if number<=dimension:
            return rowNum
        else:
            number-=dimension 
            rowNum+=1
            
def snake(dimension,number):
    row=findRow(dimension,number)
    if row%2==0:
        col=dimension-1 if number%dimension==0 else (number%dimension)-1 
    else:
        col=number%dimension if number%dimension==0 else dimension-(number%dimension)
    print(row,col)

dimension=int(input("Dimension:"))
snake(dimension,int(input("Number:")))