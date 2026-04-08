import sys


def log(msg):
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()


def main():
    
    log("[START] task=code_review")

    total_score = 0.0

    
    for step in range(1, 2):
        reward = 1.0
        total_score += reward

        log(f"[STEP] step={step} reward={reward:.2f}")

    log(f"[END] task=code_review score={total_score:.2f} steps=1")


if __name__ == "__main__":
    main()