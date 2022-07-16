HARDNESS = {"V1": 8.8, "V2": 6.1, "O1": 2.0, "O2": 4.2, "O3": 5.0}
JANCOSTS = {"V1": 110, "V2": 120, "O1": 130, "O2": 110, "O3": 115}
FEBCOSTS = {"V1": 130, "V2": 130, "O1": 110, "O2": 90, "O3": 115}
MARCOSTS = {"V1": 110, "V2": 140, "O1": 130, "O2": 100, "O3": 95}
APRCOSTS = {"V1": 120, "V2": 110, "O1": 120, "O2": 120, "O3": 125}
MAYCOSTS = {"V1": 100, "V2": 120, "O1": 150, "O2": 110, "O3": 105}
JUNCOSTS = {"V1": 90, "V2": 100, "O1": 140, "O2": 80, "O3": 135}

class Blender:
    def __init__(self, UB, LB):
        self.UB = UB
        self.LB = LB
        self.ProfitFunc = lambda v1, v2, o1, o2, o3, n: -110(v1) - 120(v2) - 130(o1) - 110(o2) - 115(o3) + 150(n)
        self.VegOilConstraint = lambda v1, v2, n: (v1+v2)*n 
        self.OilConstraint = lambda o1, o2, o3, n: (o1+o2+o3)*n 
        self.UpperHardness = lambda v1, v2, o1, o2, o3, n: 8.8(v1) + 6.1(v2) + 2.0(o1) + 4.2(o2) + 5.0(o3) - self.UB(n)
        self.LowerHardness = lambda v1, v2, o1, o2, o3, n: 8.8(v1) + 6.1(v2) + 2.0(o1) + 4.2(o2) + 5.0(o3) - self.LB(n)
        self.WeightContinuity = lambda v1, v2, o1, o2, o3, n: v1 + v2 + o1 + o2 + o3 - n == 0
    
    def CheckConstraints(self, v1, v2, o1, o2, o3, n) -> int: #returns -1 if constraint check failed
        if self.VegOilConstraint(v1, v2, n) and self.OilConstraint(o1, o2, o3, n) and self.UpperHardness(v1, v2, o1, o2, o3, n) and self.LowerHardness(v1, v2, o1, o2, o3, n):
            return self.ProfitFunc(v1, v2, o1, o2, o3, n)
    
    def Optimise(self):
        