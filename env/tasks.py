TASKS = [
    {
        "id": "easy_1",
        "difficulty": "easy",
        "code": "for i in range(5 print(i)",
        "instruction": "Fix the syntax error in the code",
        "expected_keywords": ["missing parenthesis", "add )"]
    },
    {
        "id": "medium_1",
        "difficulty": "medium",
        "code": "for i in range(n):\n  for j in range(n):\n    print(i, j)",
        "instruction": "Optimize the time complexity",
        "expected_keywords": ["reduce to o(n)", "avoid nested loop"]
    },
    {
        "id": "hard_1",
        "difficulty": "hard",
        "code": "def isPrime(n):\n  for i in range(2, n):\n    if n % i == 0:\n      return False\n  return True",
        "instruction": "Optimize and improve readability",
        "expected_keywords": ["sqrt", "early break", "efficient"]
    }
]

import random

def get_random_task():
    return random.choice(TASKS)