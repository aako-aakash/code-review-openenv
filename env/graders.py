def grade(task, suggestion: str):
    suggestion = suggestion.lower()
    solution = task["solution"].lower()

    if solution in suggestion:
        return 1.0
    elif any(word in suggestion for word in solution.split()):
        return 0.6
    else:
        return 0.2