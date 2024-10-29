def f(name):
  output = ''
  for word in name.split(" "):
    output += word[0]
  return output

print(f("Dupa jeża elo"))