import os
from openai import OpenAI
from env.environment import CodeReviewEnv
from env.models import Action

# ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=OPENAI_API_KEY
)

MAX_STEPS = 5


def run_episode():
    env = CodeReviewEnv()
    obs = env.reset()

    total_reward = 0.0

    for step in range(MAX_STEPS):

        prompt = f"""
You are a senior code reviewer.

Code:
{obs.code}

Task:
{obs.instruction}

Give a clear improvement suggestion.
"""

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )
            suggestion = response.choices[0].message.content

        except Exception as e:
            print("Model error:", e)
            suggestion = "No suggestion"

        action = Action(suggestion=suggestion)

        result = env.step(action)

        obs = result.observation
        total_reward += result.reward

        print(f"Step {step+1}")
        print("Suggestion:", suggestion)
        print("Reward:", result.reward)
        print("Done:", result.done)
        print("-" * 40)

        if result.done:
            break

    print("Final Score:", total_reward)


if __name__ == "__main__":
    run_episode()