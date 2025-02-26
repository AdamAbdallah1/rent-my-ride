class Vehicle:
    brand = ''
    model = 0
    year = 0
    seats = 0
    rental_days = 0
    rental_price_per_day = 0.0
    
    def __init__(self, brand, model, year, seats, rental_price_per_day, rental_days):
        self.brand = brand
        self.model = model
        self.year = year
        self.seats = seats
        self.rental_price_per_day = rental_price_per_day
    
    def calculateRentalCost(self, days):
        return self.rental_price_per_day * days
    
    def get_rental_price_per_day(self):
        return self.rental_price_per_day
    
    def set_rental_price_per_day(self, new_price):
        if new_price > 0:
            self.rental_price_per_day = new_price
        else:
            print("Rental Price must be greater than 0!")
        
    def dislayInfo(self):
        print(f"""  Car: {self.brand}, Year: {self.year}, Seats: {self.seats}, Rental Price: {self.rental_price_per_day}\day""")

class Car(Vehicle):
    def __init__(self, brand, model, year, seats, rental_price_per_day, rental_days):
        super().__init__(brand, model, year, seats, rental_price_per_day, rental_days) #using super() to return a temp object allowing to access the methods
        self.seating_capacity = seats
        
    def displayInfo(self):
        print(f"""  Car: {self.brand}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.rental_price_per_day}/day""")

class Bike(Vehicle):
    def __init__(self, brand, model, year, seats, rental_price_per_day, rental_days, engine_capacity):
        super().__init__(brand, model, year, seats, rental_price_per_day, rental_days)
        self.engine_capacity = engine_capacity
        
    def dislayInfo(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.rental_price_per_day}/day")
                
def show_vehicle_info():
    Vehicle.displayInfo()              

toyota_car = Vehicle("Toyota", "Corolla", 2024, 5, 30, 3)
yamaha_bike = Bike("Yamaha", "R1", 2019, 30, 998)

show_vehicle_info(toyota_car)
show_vehicle_info(yamaha_bike)
