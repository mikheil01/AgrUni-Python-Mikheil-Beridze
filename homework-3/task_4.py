import random

numbers = [random.randint(1, 4) for _ in range(5)]
expanded_list = []

for num in numbers:
    expanded_list.extend([num] * num)

print(f"List - {expanded_list}")
print(f"Length - {len(expanded_list)}")