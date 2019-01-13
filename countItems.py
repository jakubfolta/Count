def countItems(sequence, item):
  total = 0
  for index in sequence:
    if index == item:
      total += 1
  return total

print(countItems(['ab', 'ddr', 'dfg', 'afb', 'udt', 'aba', 'd', 'ab'], 'ab'))


def countHowManyItemsAppear(sequence, item):
    total = 0
    for x in sequence:
        if x == item:
            total += 1
    return total

print(countHowManyItemsAppear(['ab', 'ddr', 'dfg', 'afb', 'udt', 'aba', 'd', 'ab'], 'ab'))
