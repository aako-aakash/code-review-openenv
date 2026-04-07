import random

TASKS = [
    {
        "code": "for i in range(5 print(i)",
        "instruction": "Fix the syntax error in the code",
        "solution": "missing parenthesis"
    },
    {
        "code": """
def find_duplicates(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                result.append(arr[i])
    return result
""",
        "instruction": "Optimize time complexity",
        "solution": "use set"
    },
    {
        "code": """
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
""",
        "instruction": "Improve efficiency",
        "solution": "sqrt optimization"
    }
]

def get_task():
    return random.choice(TASKS)