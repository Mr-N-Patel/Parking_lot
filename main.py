import parking_functionality
import vehicle

import parking_lot


car1 = vehicle.Car('Maruti-800', 'Jh-05_DR 8100', '20', '5', 'Suzuki Nishida', '4', '2')
bike1 = vehicle.Bike('Platina', 'UP-31T-1956', '100', '2', 'Bajaj', '2', '0.5')
lotA = parking_lot.Lot(100, 200, 100, 'A', "Free")
lotA.l_number = lotA.l_depth * lotA.l_width
lotB = parking_lot.Lot(200, 300, 200, "B", 'Free')
lotB.l_number = lotB.l_depth * lotB.l_width
lotC = parking_lot.Lot(300, 400, 200, "C", 'Free')
lotC.l_number = lotC.l_depth * lotC.l_width
lotD = parking_lot.Lot(100, 200, 200, "D", 'Free')
lotD.l_number = lotD.l_depth * lotD.l_width
parking_functionality.parking_alloc(car1)
