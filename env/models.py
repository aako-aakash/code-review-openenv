from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    code: str
    instruction: str
    step_count: int
    last_action_error: Optional[str] = None

class Action(BaseModel):
    suggestion: str  # agent suggests improvements

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict