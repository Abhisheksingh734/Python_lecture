# make a class bus 
# set the capacity of bus set the company
# add method to add a passengers
# if capacity is full then show sesats not avaliable
# add a method to show list of passengers

# then add them to the bus- ["Harry", "Ron", "Hermione", "Ginny"]

class Bus:
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger=[]
    
    def seatsLeft(self):
        return self.capacity-len(self.passenger)

    def add_passenger(self,name):
        self.name=name
        if Bus.seatsLeft(self):
            print(f"{name} is added to the bus")
            return self.passenger.append(name)
        else:
            print(f"No seats left, {name} is not added to the bus")
    
    
passengers=["Harry", "Ron", "Hermione", "Ginny"]

Zink=Bus(3)
for i in passengers:
    Zink.add_passenger(i)

print("passengers in the bus:",Zink.passenger)
    

