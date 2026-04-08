from env.models import Observation, StepResult
from env.tasks import get_task
from env.graders import grade


class CodeReviewEnv:
    def __init__(self):
        self.task = None
        self.step_count = 0
        self.max_steps = 5

    def reset(self):
        self.task = get_task()
        self.step_count = 0

        return Observation(
            code=self.task["code"],
            instruction=self.task["instruction"],
            step_count=self.step_count,
            last_action_error=None
        )

    def step(self, action):
        self.step_count += 1

        
        reward = grade(self.task, action.suggestion)

        done = False
        if reward >= 1.0 or self.step_count >= self.max_steps:
            done = True

        obs = Observation(
            code=self.task["code"],
            instruction=self.task["instruction"],
            step_count=self.step_count,
            last_action_error=None
        )

        return StepResult(
            observation=obs,
            reward=reward,
            done=done,
            info={
                "expected_solution": self.task["solution"],
                "your_suggestion": action.suggestion
            }
        )

    def state(self):
        return {
            "task": self.task,
            "step_count": self.step_count
        }