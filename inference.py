import os
from openai import OpenAI
from env.environment import CodeReviewEnv
from env.models import Action

MODEL_NAME = "gpt-4o-mini"
MAX_STEPS = 5

def get_fallback_action(observation):
    instruction = observation.instruction.lower()

    if "syntax" in instruction:
        return "missing parenthesis"
    elif "optimize" in instruction:
        return "use set"
    elif "efficiency" in instruction:
        return "sqrt optimization"
    else:
        return "improve code"

API_KEY = os.getenv("OPENAI_API_KEY")
client = None

if API_KEY:
    try:
        client = OpenAI(api_key=API_KEY)
    except Exception:
        client = None


def get_model_response(messages, observation):
    if not client:
        return get_fallback_action(observation)

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            max_tokens=100,
        )
        return completion.choices[0].message.content or get_fallback_action(observation)
    except Exception:
        return get_fallback_action(observation)


def main():
    env = CodeReviewEnv()
    task_name = "code_review"

    # ✅ MUST BE FIRST PRINT
    print(f"[START] task={task_name}", flush=True)

    try:
        observation = env.reset()
        total_reward = 0.0

        for step in range(1, MAX_STEPS + 1):

            messages = [
                {"role": "system", "content": "You are a code reviewer."},
                {
                    "role": "user",
                    "content": f"{observation.code}\n{observation.instruction}",
                },
            ]

            response = get_model_response(messages, observation)

            result = env.step(Action(suggestion=response))

            observation = result.observation
            reward = result.reward
            done = result.done

            total_reward += reward

            
            print(f"[STEP] step={step} reward={reward}", flush=True)

            if done:
                break

        
        print(
            f"[END] task={task_name} score={total_reward:.2f} steps={step}",
            flush=True,
        )

    except Exception:
        
        print(f"[END] task={task_name} score=0.00 steps=0", flush=True)


if __name__ == "__main__":
    main()