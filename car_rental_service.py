class VehicelService:
    brand = ''
    model = 0
    year = 0
    seats = 0
    rental_price_per_day = 0.0
    
    def __init__(self, brand, model, year, seats, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.seats = seats
        self.rental_price_per_day = rental_price_per_day
        
    def dislayInfo(self):
        self.rental_days = rental_days
        rental_days = float(input("Enter rental days: "))
        self.rental_price_per_day = rental_price_per_day
        rental_price_per_day = (rental_days * rental_price_per_day)
        print(f"""
        Car: {self.brand}, Year: {self.year}, Seats: {self.seats}, Rental Price: {rental_days}\day
              """)

toyota = VehicelService("Toyota", "Corolla", 2024, 5, 30)
toyota.dislayInfo()

mercedes = VehicelService("Mercedes-Benz", "C-Class", 2024, 5, 50)
mercedes.dislayInfo()

