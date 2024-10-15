dog_age = int(input("Enter dog age"))
in_human = 0

if dog_age <= 2 and dog_age > 0:
  in_human = dog_age * 10.5
elif dog_age > 2:
  in_human = (dog_age - 2) * 4 + 21

print(f"{dog_age} dog age in human is equal {in_human}")