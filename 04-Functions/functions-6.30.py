def sum_natural(n):
  if n == 1:
    return 1
  return n + sum_natural(n-1)
