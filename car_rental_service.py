class VehicelService:
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
        self.rental_days = rental_days
    
    def calculateRentalCost(self):
        self.rental_price_per_day = (self.rental_price_per_day * self.rental_days)
        
    def dislayInfo(self):
        print(f"""  Car: {self.brand}, Year: {self.year}, Seats: {self.seats}, Rental Price: {self.rental_price_per_day}\day""")

toyota = VehicelService("Toyota", "Corolla", 2024, 5, 30, 3)
toyota.dislayInfo()

mercedes = VehicelService("Mercedes-Benz", "C-Class", 2024, 5, 50, 3)
mercedes.dislayInfo()

bmw = VehicelService("BMW", "3 Series", 2024, 5, 50, 3)
bmw.dislayInfo()