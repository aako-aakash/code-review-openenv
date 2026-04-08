import sys


def log(line):
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def main():
    task = "code_review"

    
    log(f"[START] task={task}")

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

            
            log(f"[STEP] step={i} reward={reward:.2f}")

            if done:
                break

       
        log(f"[END] task={task} score={total:.2f} steps={steps}")

    except Exception:
        
        log(f"[END] task={task} score=0.00 steps=0")


if __name__ == "__main__":
    main()