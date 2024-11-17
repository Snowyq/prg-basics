import math

def max(arr , n = 1):
  return sorted(arr, reverse=True)[n - 1]

def min(arr):
  return sorted(arr)[0]

def amplitude(arr):
  return max(arr) - sorted(arr)[0]

def median(arr):
  sorted_arr = sorted(arr)
  middle = len(arr) / 2
  if len(arr) % 2 == 0:
    return (sorted_arr[math.floor(middle)] + sorted_arr[math.ceil(middle)]) / 2 
  else:
    return sorted_arr[math.floor(middle)]


def get_min_max(arr):
  return [min(arr),max(arr)]


def arr_seperated(arr):
  return '-'.join(map(lambda el: str(el),arr))



