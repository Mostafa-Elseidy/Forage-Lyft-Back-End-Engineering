from car_factory import CarFactory
from datetime import date

current_date = date.today()
last_service_date = date(2022, 1, 1)
current_mileage = 10000
last_service_mileage = 5000
tire_wear = [0.8, 0.8, 0.8, 0.7]

car = CarFactory.create_calliope(
    current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

# Check if the car needs service
if car.needs_service():
    print("The car needs service.")
else:
    print("The car does not need service.")
