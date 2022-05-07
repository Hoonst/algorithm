from collections import Counter

word = input()
counter = Counter(word.lower())

counter_max = max(counter.values())

max_key = [key.upper() for key in counter if counter[key] == counter_max]

if len(max_key) > 1:
    print('?')
else:
    print(max_key.pop())