
def  getColor(row,col):
    #consider 1,1 as white
    if row%2==0:
        if col%2==0:
            return("white")
        else:
            return("black")
    else:
        if col%2!=0:
            return("white")
        else:
            return("black")

r=int(input())
c=int(input())

print(getColor(r,c))
