results = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]


def min_pts(limit):
    return lambda pts: pts >= limit


treshold_70 = list(filter(min_pts(70), results))
treshold_40 = list(filter(min_pts(40), results))
treshold_30 = list(filter(min_pts(30), results))

print("min 70", treshold_70)
print("min 40", treshold_40)
print("min 30", treshold_30)
