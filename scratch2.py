class ParkingSpace:
    def __init__ (self):
        self.space = []
        self.space_amount = [10]

    def get_ticket(self):
        if self.space_amount > 0:
            self.space_amount -= 1
            self.space.append("occupied")
        if self.space_amount == 0:
            print("Sorry, we are full!")
    
    
    
    
class ParkingSim(): 

    
    
    def main():        
        while True:
            prompt = input("Welcome! What would you like to do? ticket/pay/leave")
            if prompt.lower() == "ticket":
                return get_ticket


