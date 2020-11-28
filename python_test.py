import math

def calculate_bearing(X1, Y1, X2, Y2):
    bearing = math.atan2((X2-X1),(Y2-Y1))*(180/(22/7))
    if bearing < 0:
        return bearing + 360
    else:
        return bearing

print(calculate_bearing(1,3,1,1))

#print(calculate_bearing(538570.2,181070.7,538580.7,181041))