import sys
import os


sys.stdout.reconfigure(line_buffering=True)

try:
    from env.environment import CodeReviewEnv
    from env.models import Action
except Exception as e:
    
    print("[START] task=code_review", flush=True)
    print("[END] task=code_review score=0.00 steps=0", flush=True)
    sys.exit(0)


def main():
    print("[START] task=code_review", flush=True)

    try:
        env = CodeReviewEnv()
        observation = env.reset()

        total_reward = 0.0
        MAX_STEPS = 5

        for step in range(1, MAX_STEPS + 1):

           
            instruction = observation.instruction.lower()

            if "syntax" in instruction:
                suggestion = "missing parenthesis"
            elif "optimize" in instruction:
                suggestion = "use set"
            elif "efficiency" in instruction:
                suggestion = "sqrt optimization"
            else:
                suggestion = "improve code"

            result = env.step(Action(suggestion=suggestion))

            observation = result.observation
            reward = result.reward
            done = result.done

            total_reward += reward

            print(f"[STEP] step={step} reward={reward}", flush=True)

            if done:
                break

        print(f"[END] task=code_review score={total_reward:.2f} steps={step}", flush=True)

    except Exception:
        
        print("[END] task=code_review score=0.00 steps=0", flush=True)


if __name__ == "__main__":
    main()