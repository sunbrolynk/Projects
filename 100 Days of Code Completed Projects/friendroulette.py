import random
from typing import List

friends: list[str] = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_name = random.choice(friends)

print(random_name)