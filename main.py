import vehicle

import parking_lot


car1 = vehicle.Car('Maruti-800', 'Jh-05_DR 8100', '20', '5', 'Suzuki Nishida', '4', '2')
bike1 = vehicle.Bike('Platina', 'UP-31T-1956', '100', '2', 'Bajaj', '2', '0.5')
# print(type(car1).__name__)
# print(bike1.v_manufacturer)
# print(car1.v_name)
# print(parking_lot.check_availability(car1))
print(parking_lot.check_availability(bike1))
parking_lot.de