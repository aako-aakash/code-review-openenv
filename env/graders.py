def grade_action(task, action):
    suggestion = action.suggestion.lower()

    score = 0.0

    # reward for matching expected keywords
    matches = sum(1 for kw in task["expected_keywords"] if kw in suggestion)

    if matches == len(task["expected_keywords"]):
        score = 1.0
    elif matches > 0:
        score = 0.5
    else:
        score = 0.1

    return score