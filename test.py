parking_dict = {}
time_dict = {}
lot_series = ["a", "b", "c", "d"]
series_sections = [1, 2, 3]

for i in lot_series:
    for j in series_sections:
        parking_dict[i, j] = []
print(parking_dict)
