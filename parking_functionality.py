"""Check"""
from vehicle import Car, Bus, Bike

SA = {'car': 60, 'bus': 10, 'bike': 30}
SB = {'car': 120, 'bus': 20, 'bike': 60}
SC = {'car': 30, 'bus': 5, 'bike': 15}
SD = {'car': 180, 'bus': 30, 'bike': 90}


def parking_alloc():
    pass


# in time = time.now()

def parking_de_alloc():
    pass


def check_availability(obj):
    """Check the availability of vehicle"""
    if isinstance(obj, Bike):
        if SA['bike'] > 0 or SB['bike'] > 0 or SC[
                'bike'] > 0 and obj.v_length <= 2 and obj.v_width <= 1:
            return True
        return False
    if isinstance(obj, Car):
        if SA['car'] > 0 or SB['car'] > 0 or SC[
                'car'] > 0 and obj.v_length <= 5 and obj.v_width <= 3:
            return True
        return False
    if isinstance(obj, Bus):
        if SA['bus'] > 0 or SB['bus'] > 0 or SC[
                'bus'] > 0 and obj.v_length <= 15 and obj.v_width <= 5:
            return True
        return False
    return "No Available For Parking"
