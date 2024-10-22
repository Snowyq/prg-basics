given_num= int(input("Enter num to check"))

is_prime = True

for i in range(2, given_num - 1):
  print(i)
  if given_num % i == 0:
    is_prime = False 
    break

print(is_prime)