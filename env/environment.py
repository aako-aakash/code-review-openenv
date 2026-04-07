from env.models import Observation, StepResult
from env.tasks import get_random_task
from env.graders import grade_action

class CodeReviewEnv:

    def __init__(self):
        self.current_task = None
        self.step_count = 0
        self.max_steps = 5

    def reset(self):
        self.current_task = get_random_task()
        self.step_count = 0
        return self._get_observation()

    def step(self, action):
        self.step_count += 1

        try:
            reward = grade_action(self.current_task, action)
            error = None
        except Exception as e:
            reward = 0.0
            error = str(e)

        done = self.step_count >= self.max_steps or reward >= 0.9

        obs = self._get_observation()
        obs.last_action_error = error

        return StepResult(
            observation=obs,
            reward=reward,
            done=done,
            info={
                "reason": "task_completed" if reward >= 1.0 else "in_progress"
            }
        )

    def state(self):
        return {
            "task": self.current_task,
            "step_count": self.step_count
        }

    def _get_observation(self):
        return Observation(
            code=self.current_task["code"],
            instruction=self.current_task["instruction"],
            step_count=self.step_count
        )