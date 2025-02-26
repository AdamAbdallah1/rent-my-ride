class Vehicel:
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

class Car(Vehicel):
    def __init__(self, brand, model, year, seats, rental_price_per_day, rental_days):
        super().__init__(brand, model, year, seats, rental_price_per_day, rental_days) #using super() to return a temp object allowing to access the methods
        self.seating_capacity = seats
        

                
toyota = Vehicel("Toyota", "Corolla", 2024, 5, 30, 3)
toyota.dislayInfo()

mercedes = Vehicel("Mercedes-Benz", "C-Class", 2024, 5, 50, 3)
mercedes.dislayInfo()

bmwbike = Vehicel("BMW", "S 100 RR", 2024, 5, 50, 3)
bmwbike.dislayInfo()