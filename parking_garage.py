import os

class ParkingSim():
    def __init__ (self):
        self.park_spaces = {}
        self.tickets = [10]


    def pick_ticket(self):
        self.tickets-=1
        self.park_spaces+=1

    def leave_lot(self):
        self.tickets+=1
        self.park_spaces-=1

    def pay_parking(self):
        prompt = ("Please enter payment amount. ")
        if prompt > 0:
            print("Thank you for coming!")
        



class UI():
   

    parking_sim = ParkingSim()

    def main(cls):
        while True:
            prompt = input("Thank you for choosing city parking! Please pick from the following options: ticket/pay/leave")
            if prompt.lower() == "ticket":
                cls.parking_sim.pick_ticket()
            if prompt.lower() == "pay":
                cls.parking_sim.pay_parking()
            if prompt.lower() == "leave":
                cls.parking_sim.leave_lot()
                break
if __name__ == "__main__":

    UI.main()


        
    # parking tickets
    # parking spaces
    # people leaving = +1 ticket

