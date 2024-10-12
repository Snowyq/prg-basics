import random

dice_roll = random.randint(1,6)
is_special_num = dice_roll == 1 or dice_roll == 2

print('dice rolled: ', dice_roll)
print('Special number (1 or 6):', is_special_num)