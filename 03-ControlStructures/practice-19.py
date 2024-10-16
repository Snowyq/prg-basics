q_1 = "interested in computer science"
q_2 = "like playing computer games"
q_3 = "have an Instagram account"

print("SURVEY")
a_1 = input(f" Are you {q_1}? (y/n): ")
a_2 = input(f"Do you {q_2}? (y/n): ")
a_3 = input(f"Do you {q_3}? (y/n): ")

if a_1 == "y":
  print(f"{q_1}:", 'Yes')
elif a_1 == "n":
  print(f"{q_1}:", "No")

if a_2 == "y":
  print(f"{q_2}:", 'Yes')
elif a_2 == "n":
  print(f"{q_2}:", "No")

if a_3 == "y":
  print(f"{q_3}:", 'Yes')
elif a_3 == "n":
  print(f"{q_3}:", "No")