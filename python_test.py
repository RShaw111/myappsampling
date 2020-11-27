import math

def calculate_bearing(X1, Y1, X2, Y2):
    bearing = math.atan2((X2-X1),(Y2-Y1))*(180/(22/7))
    return bearing+360

print(calculate_bearing(527602,178677.3,527600.8,178676))

#print(calculate_bearing(538570.2,181070.7,538580.7,181041))