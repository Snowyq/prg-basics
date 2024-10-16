facebook = True
twitter = False
instagram = False

socials__num = 0

if facebook:
  socials__num += 1
if twitter:
  socials__num += 1
if instagram:
  socials__num += 1

if socials__num >= 2:
  print("You are good influencer!")
