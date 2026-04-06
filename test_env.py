from env.environment import CodeReviewEnv
from env.models import Action

env = CodeReviewEnv()

# Reset environment
obs = env.reset()
print("Initial Observation:")
print(obs)

# Take a sample action
action = Action(suggestion="Add missing parenthesis")

result = env.step(action)

print("\nStep Result:")
print(result)