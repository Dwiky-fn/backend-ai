from pydantic import BaseModel

class ProgressInput(BaseModel):
    score_prev: float
    pass_rate: float

class ProgressOutput(BaseModel):
    predicted_progress: float
    progress_level: str
    feedback: str
