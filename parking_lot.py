class Lot:
    def __init__(self, width, depth, series, status, number=0):
        self.l_width = width
        self.l_depth = depth
        self.l_series = series
        self.l_status = status
        self.l_number = number


lotA = Lot(100, 200, 'A', "Free")
lotA.l_number = lotA.l_depth * lotA.l_width
lotB = Lot(200, 300, 200, "B", 'Free')
lotB.l_number = lotB.l_depth * lotB.l_width
lotC = Lot(300, 400, 200, "C", 'Free')
lotC.l_number = lotC.l_depth * lotC.l_width
lotD = Lot(100, 200, 200, "D", 'Free')
lotD.l_number = lotD.l_depth * lotD.l_width
