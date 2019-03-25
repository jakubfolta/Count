def count_item(sequence, item_to_count):
    return sequence.count(item_to_count)

print(count_item(['dada', 'dsadef', 'das', 'dade', 'asa', 'fsdf', 'asa'], 'asa'))

def count_items(sequence, item):
    total = 0
    for x in sequence:
        if x == item:
            total += 1
    return total

print(count_items(['dada', 'dsadef', 'das', 'dade', 'asa', 'fsdf', 'asa'], 'asa'))

def count_items(sequence, item):
    
