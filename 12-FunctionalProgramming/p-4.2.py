measured_speeds = [48, 47, 54, 50, 42, 68, 39, 46]

too_high = list(filter(lambda speed: speed > 50, measured_speeds))

print(too_high)
