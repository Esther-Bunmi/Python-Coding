import random
friends_pick = random.randint(0, 4)
friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

print(friends[friends_pick])

# OR

friends = random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Emmanuel'])
print(friends)

#Or

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
print(random.choice(friends))