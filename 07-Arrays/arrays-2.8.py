
computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

sorted_computer_games = sorted(computer_games)


counter = 0
while counter < len(computer_games) - 1:
  counter += 1
  print(f'{counter + 1}.', sorted_computer_games[counter])

