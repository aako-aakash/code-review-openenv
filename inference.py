import sys
import os


sys.path.append(os.getcwd())


sys.stdout.write("[START] task=code_review\n")
sys.stdout.flush()

try:
    
    from env.environment import CodeReviewEnv
    from env.models import Action

    env = CodeReviewEnv()
    obs = env.reset()

    total = 0.0
    steps = 0

    for i in range(1, 6):
        steps = i

        instr = obs.instruction.lower()

        if "syntax" in instr:
            suggestion = "missing parenthesis"
        elif "optimize" in instr:
            suggestion = "use set"
        elif "efficiency" in instr:
            suggestion = "sqrt optimization"
        else:
            suggestion = "improve code"

        result = env.step(Action(suggestion=suggestion))

        obs = result.observation
        reward = float(result.reward)
        done = result.done

        total += reward

        sys.stdout.write(f"[STEP] step={i} reward={reward:.2f}\n")
        sys.stdout.flush()

        if done:
            break

    sys.stdout.write(f"[END] task=code_review score={total:.2f} steps={steps}\n")
    sys.stdout.flush()

except Exception:
    
    sys.stdout.write("[END] task=code_review score=0.00 steps=0\n")
    sys.stdout.flush()