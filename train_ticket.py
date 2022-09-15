class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("*******")   
        print(f"The Name of the train is {self.name}")
        print(f"The seats available are {self.seats}")
        print("*******")

    def fareInfo(self):
        print(f"The price of the ticket is {self.fare}")  

    def bookTicket(self):
        if (self.seats>0):  
           print(f"Your ticket has been booked! Your seat number is {self.seats}")  
           self.seats = self.seats -1
        else:
            print("Sorry the seat is full please try in tatkal")
    
Intercity = Train("Intercity Express  140165",90,2)    
Intercity.getStatus()
Intercity.bookTicket()
Intercity.bookTicket()
Intercity.getStatus()






         