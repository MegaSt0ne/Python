import math

def median(numbers):
  length = 0
  length = len(numbers)
  numbers = sorted(numbers)
  if length % 2 == 0:
    return ((numbers[length / 2 - 1] + numbers[length / 2 ]) / 2.0)
  else:
    return numbers[length / 2]
