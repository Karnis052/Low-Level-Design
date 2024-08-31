from rentalSystem import RentalSystem
from customer import Customer
from car import Car
from datetime import date, timedelta

class RentalSystemDemo:
    @staticmethod
    def run():
        rentalSystem = RentalSystem.getInstance()
        rentalSystem.addCar(Car("Toyota", "Camry", 2022, "ABC123", 50.0))
        rentalSystem.addCar(Car("Honda", "Civic", 2021, "XYZ789", 45.0))
        rentalSystem.addCar(Car("Ford", "Mustang", 2023, "DEF456", 80.0))
        rentalSystem.addCar(Car("Toyota", "Camry", 2024, "MNO123", 60.0))
        
        customer1 = Customer("John Doe", "john@example.com", "DL1234")
        customer2 = Customer("Jane Smith", "jane@example.com", "DL5678")
        
        startDate = date.today()
        endDate = startDate  + timedelta(days=3)
        availableCars = rentalSystem.searchCars("Toyota", "Camry", startDate, endDate)
        if availableCars:
                selected_car = availableCars[0]
                reservation = rentalSystem.makeReservation(customer1, selected_car, startDate, endDate)
                if reservation is not None:
                    payment_success = rentalSystem.processPayment(reservation)
                    if payment_success:
                        print(f"Reservation successful. Reservation ID: {reservation.getReservationId()}")
                    else:
                        print("Payment failed. Reservation canceled.")
                        rentalSystem.cancelReservation(reservation.getReservationId())
                else:
                    print("Selected car is not available for the given dates.")
        else:
            print("No available cars found for the given criteria.")
        
if __name__ == "__main__":
    RentalSystemDemo.run()