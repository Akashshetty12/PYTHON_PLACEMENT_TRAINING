# data which is encapsulated or covered inside the method
# data which is private
# access method - can be accessed by method not directly
# for scenario based question we have to design base class 2. next we have to design logic for main class 3. 2nd class or action class
from datetime import datetime


class Bus:
    def __init__(self,bno,ac,cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno
    def get_ac(self):
        return self.ac
    def get_cap(self):
        return self.cap
    def display(self):
        print(f"Bno: {self.get_bno()}\nAc: {self.get_ac()}\nCap: {self.get_cap()}")


BUSES = [Bus(1,True,2),Bus(2,False,50),Bus(3,True,60)]
BOOKING = []

class Booking:

    def __init__(self):
        name = input("Enter your name: ")
        bno = int(input("Enter your bno: "))
        d = input("Enter your date (dd-mm-yyyy): ")
        date = datetime.strptime(d,"%d-%m-%Y")
        self.name = name
        self.bno = bno
        self.date = date

    def make_booking(self):
        # ✅ FIXED: Removed extra arguments from method call
        if self.is_available():  # previously: self.is_available(BUSES,BOOKING,self.bno,self.date)
            BOOKING.append(self)
            print("Booked Successfully")
        else:
            print("No seats available")


    # ✅ FIXED: Removed parameters and used self, BUSES, and BOOKING directly
    def is_available(self):  # previously: def is_available(self,BUSES,BOOKING)
        capacity = 0
        booked = 0
        for i in BUSES:
            if i.bno == self.bno:
                capacity = i.cap
        for i in BOOKING:
            if i.bno == self.bno and i.date == self.date:
                booked += 1
        return booked < capacity

    def display_booking(self):
        print(f"Name: {self.name}")
        print(f"Bno: {self.bno}")
        print(f"Date: {self.date}")  # Can also use strftime if desired
        print("_____________")


while True:
    print("1.BOOK TICKETS")
    print("2.VIEW BOOKINGS")
    print("3. EXIT")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        b = Booking()
        b.make_booking()
    elif ch == 2:
        if not BOOKING:
            print("No bookings yet")
        else:
            for i in BOOKING:
                i.display_booking()
    elif ch == 3:
        print("Thank you")
    else:
        print("Invalid choice")




