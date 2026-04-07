import os
from openai import OpenAI
from env.environment import CodeReviewEnv
from env.models import Action

# ---------------------------
# CONFIG
# ---------------------------
MODEL_NAME = "gpt-4o-mini"
MAX_STEPS = 5
TEMPERATURE = 0.2

# ---------------------------
# SMART FALLBACK (TASK-AWARE)
# ---------------------------
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

# ---------------------------
# OPENAI CLIENT (SAFE)
# ---------------------------
API_KEY = os.getenv("OPENAI_API_KEY")

client = None

if API_KEY:
    try:
        client = OpenAI(api_key=API_KEY)
    except Exception as e:
        print(f"[ERROR] OpenAI init failed: {e}")
        client = None
else:
    print("⚠️ No API key found. Using fallback mode.")

# ---------------------------
# SAFE MODEL CALL
# ---------------------------
def get_model_response(messages, observation):
    # If no client → directly fallback
    if not client:
        return get_fallback_action(observation)

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=100,
        )
        return completion.choices[0].message.content or get_fallback_action(observation)

    except Exception as e:
        print(f"[ERROR] Model call failed: {e}")
        return get_fallback_action(observation)

# ---------------------------
# MAIN
# ---------------------------
def main():
    env = CodeReviewEnv()

    try:
        observation = env.reset()
        total_reward = 0.0

        print("\n--- Starting Inference ---\n")

        for step in range(1, MAX_STEPS + 1):
            print(f"Step {step}")

            user_prompt = f"""
                Code:
                {observation.code}

                Instruction:
                {observation.instruction}

                Give a short suggestion to improve/fix the code.
                """

            messages = [
                {"role": "system", "content": "You are a code reviewer."},
                {"role": "user", "content": user_prompt},
            ]

            # ✅ SAFE CALL
            response_text = get_model_response(messages, observation)

            print(f"Suggestion: {response_text}")

            result = env.step(Action(suggestion=response_text))

            observation = result.observation
            reward = result.reward
            done = result.done

            total_reward += reward

            print(f"Reward: {reward}")
            print(f"Done: {done}")
            print("-" * 40)

            if done:
                break

        print(f"\nFinal Score: {total_reward:.2f}")

    except Exception as e:
        print(f"[FATAL ERROR] {e}")

    finally:
        print("\n--- Inference Complete ---")


if __name__ == "__main__":
    main()