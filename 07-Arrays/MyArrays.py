import math

def largest(arr):
  return sorted(arr, reverse=True)[0]

def amplitude(arr):
  return largest(arr) - sorted(arr)[0]

def median(arr):
  return sorted(arr)[len(arr)/2] if len(arr) % 2 == 0 else (sorted(arr)[math.floor(len(arr)/2)] + sorted(arr)[math.ceil(len(arr)/2)/2)])


median([3,2,1])
median([3,2,2,1])