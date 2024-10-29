def f(n):
  prime_count = 0
  number = 2
  while prime_count < n:
    is_prime = True
    for i in range(2, number):
      if number % i == 0:
        is_prime = False
        break
    if is_prime:
      prime_count += 1
      if prime_count == n:
        return number
    number += 1
 
print(f(13))