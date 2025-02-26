# Parent Class
class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_day = rental_price_per_day
    
    def displayInfo(self):
        print(f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.rental_price_per_day}/day")

    def calculateRentalCost(self, days):
        return self.rental_price_per_day * days
    
    # getter method for rental price
    def get_rental_price_per_day(self):
        return self.rental_price_per_day
    
    # Setter method for rental price
    def set_rental_price_per_day(self, new_price):
        if new_price > 0:
            self.rental_price_per_day = new_price
        else:
            print("Rental Price must be greater than 0!")
   
# Object car inherited from vehicle     
class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day) #using super() to return a temp object allowing to access the methods
        self.seating_capacity = seating_capacity
        
    # displayInfo() to include seating capacity
    def displayInfo(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.rental_price_per_day}/day")

# Object Bike inherited from vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity
        self.rental_days = 0
        
    # displayInfo() to include engine capacity
    def displayInfo(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.rental_price_per_day}/day")
         
# Function to demonstarte polymorphism       
def show_vehicle_info(vehicle):
    vehicle.displayInfo()              

# Creating instances with sample data
#toyota_car = Car("Toyota", "Corolla", 2024, 50, 5)
#yamaha_bike = Bike("Yamaha", "R1", 2019, 30, 998)

# Display vehicle details using polymorphism
#toyota_car.displayInfo()
#yamaha_bike.displayInfo()

# Calculate rental costs
#rental_days_car = int(input("\nEnter number of days to rent the Toyota Corolla: "))
#rental_days_bike = int(input("Enter number of days to rent the Yamaha R1: "))

#print(f"\nRental cost for {toyota_car.brand} {toyota_car.model} for {rental_days_car} days: ${toyota_car.calculateRentalCost(rental_days_car)}")
#print(f"Rental cost for {yamaha_bike.brand} {yamaha_bike.model} for {rental_days_bike} days: ${yamaha_bike.calculateRentalCost(rental_days_bike)}")

# Modify rental price using setter
#toyota_car.set_rental_price_per_day(55)

# Display updated rental price
#print(f"\nUpdated rental price for {toyota_car.brand} {toyota_car.model}: ${toyota_car.get_rental_price_per_day()}/day")

# Vehicles list
carsList = [Car(brand="Toyota", model="Corolla", year=2024, rental_price_per_day=50, seating_capacity=5)]
bikesList = [Bike(brand="BMW", model="R1", year=2019, rental_price_per_day=30, engine_capacity=998)]

# Creating the menu promp
def prompt():
    print("=======================================================")
    print("""
             Select command from the menu:        
        +--------------------------------------+
        |   1 ==> Add new veicle               |
        |   2 ==> View all cars                |
        |   3 ==> Select car and set rent days |
        |   4 ==> Exit program                 |
        +--------------------------------------+
          """)
    action = int(input(">_: "))
    print("=======================================================")
    return action

def createCar():
    choice = int(input("""
            Choose vehicle:
                1 ==> Car
                2 ==> Bike
                0 ==> Go back to menu
                >_: """))
    if choice == 1:
        brand = input("Brand: ")
        model = input("Model: ")
        year = input("Year: ")
        seats = input("Seats Capacity: ")
        rental_price_per_day = input("Rental Price/d: ")
        car = Car(brand=brand, model=model, year=year, seating_capacity=seats, rental_price_per_day=rental_price_per_day)
        print(f"""
        Car Added Successfully:
            Car: {car.brand} {car.model}
            year: {car.year}
            Seating Capacity: {car.seating_capacity}
            Rental Price Per Day: ${car.rental_price_per_day}/d.
              """)
        return car
    
    elif choice == 2:
        brand = input("Brand: ")
        model = input("Model: ")
        engine_capaxity = ("Engine Capacity: ")
        rental_price_per_day = input("Rental Price/d: ")
        bike = Bike(brand=brand, model=model, engine_capacity=engine_capaxity, rental_price_per_day=rental_price_per_day)
        print(f"""
        Bike Added Successfully:
            Bike: {car.brand} {car.model}
            year: {car.year}
            Engine Capacity: {car.seating_capacity}
            Rental Price : ${car.rental_price_per_day}/d
              """)
        return bike
    else:
        print("Unvalid Choice!")
        
def viewcars():
    pass

def selectCar():
    pass

action = 0
while action != 4:
    action = prompt()
    if action == 1:
        createCar()
    elif action == 2:
        viewcars()
    elif action == 3:
        selectCar()
    elif action == 4:
        print("Goodbye")
        break    
        