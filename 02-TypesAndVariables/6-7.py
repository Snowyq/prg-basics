import math

height = input('write height in meters: ')
height = float(height)
distance_to_horizon = 3.57 * math.sqrt(height)
print(f'the distance to the horizon is equal: {round(distance_to_horizon, 2)} km')