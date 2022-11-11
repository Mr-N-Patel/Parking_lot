"""Check"""
import parking_lot
from vehicle import Car, Bus, Bike

CAR_AREA = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
BIKE_AREA = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
BUS_AREA = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

CAR_AREA["A"] = parking_lot.lotA.l_number * 0.6
CAR_AREA["B"] = parking_lot.lotB.l_number * 0.6
CAR_AREA["C"] = parking_lot.lotC.l_number * 0.6
CAR_AREA["D"] = parking_lot.lotD.l_number * 0.6
BIKE_AREA['A'] = parking_lot.lotA.l_number * 0.3
BIKE_AREA['B'] = parking_lot.lotB.l_number * 0.3
BIKE_AREA['C'] = parking_lot.lotC.l_number * 0.3
BIKE_AREA['D'] = parking_lot.lotD.l_number * 0.3
BUS_AREA['A'] = parking_lot.lotA.l_number * 0.1
BUS_AREA['B'] = parking_lot.lotB.l_number * 0.1
BUS_AREA['C'] = parking_lot.lotB.l_number * 0.1
BUS_AREA['D'] = parking_lot.lotB.l_number * 0.1


def parking_alloc(obj):
    if check_availability(obj):
        pass


def parking_de_alloc():
    pass


def check_availability(obj):
    """Check the availability of vehicle"""
    pass
