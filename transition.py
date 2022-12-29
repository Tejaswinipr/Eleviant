class Kid:   
    places={"Home":["School","TrainingCenter","PlayGround",0],"School":["Home","PlayGround",0],"TrainingCenter":["Home",0],"PlayGround":["Home",0]}
    
    def __init__(self,name,currentPos,destination):
        self.name=name
        self.currentPos=currentPos
        self.destination=destination
    
    def goTo(self):
        currentPosition=self.places[self.currentPos]
        if(self.destination in currentPosition):
            print(self.currentPos,"to",self.destination)
        else:
            print(self.currentPos,"to",self.places[self.currentPos][0],"to",self.destination)
            
    def canGoTo(self):
        if self.destination in self.places:
            if self.currentPos!=self.destination:
                self.goTo()
            else:
                print("You're in destination")
        else:
            print("You can't go there")

    def noOfPerson(self):
        if self.currentPos in self.places:
            if self.places[self.currentPos][-1]==0:
                self.places[self.currentPos][-1]==0
            else:   
                self.places[self.currentPos][-1]-=1
        self.places[self.destination][-1]+=1
        print(self.places[self.destination][-1])

class Adult:   
    places={"Home":["WorkSpot","AnywhereElse","Bar",0],"Workspot":["Home","Bar",0],"Bar":["Home",0],"AnywhereElse":["Home",0]}
    
    def __init__(self,name,currentPos,destination):
        self.name=name
        self.currentPos=currentPos
        self.destination=destination
    

    def goTo(self):
        currentPosition=self.places[self.currentPos]
        if(self.destination in currentPosition):
            print(self.currentPos,"to",self.destination)
        else:
            print(self.currentPos,"to",self.places[self.currentPos][0],"to",self.destination)
            
    def canGoTo(self):
        if self.destination in self.places:
            if self.currentPos!=self.destination:
                self.goTo()
            else:
                print("You're in destination")
        else:
            print("You can't go there")

    def noOfPerson(self):
        if self.currentPos in self.places:
            if self.places[self.currentPos][-1]==0:
                self.places[self.currentPos][-1]==0
            else:   
                self.places[self.currentPos][-1]-=1
        self.places[self.destination][-1]+=1
        print(self.places[self.destination][-1])
pos=[]
kid1=Kid("Niru","TrainingCenter","School")
kid2=Kid("Teju","TrainingCenter","School")
pos.append({"Niru":"School"})
pos.append({"Teju":"School"})
kid1.canGoTo()
kid1.noOfPerson()
kid2.canGoTo()
kid2.noOfPerson()
adult1=Adult("Viji","Home","AnywhereElse")
adult2=Adult("Rama","Bar","Home")
pos.append({"Viji":"AnywhereElse"})
pos.append({"Rama":"Bar"})
adult1.canGoTo()
adult1.noOfPerson()
adult2.canGoTo()
adult2.noOfPerson()
print(pos)