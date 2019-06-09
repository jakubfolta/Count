def count(sequence, item):
  total = 0
  for index in sequence:
    if index == item:
      total += 1
  return total

print(count(['ab', 'dr', 'd', 'ab', 'ut', 'aba', 'd', 'ab'], 'ab'))
