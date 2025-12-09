from pydantic import BaseModel

class MotivationalLetterRequest(BaseModel):
    examinees_id: str
    time_to_finish: float
    difficulty_num: float
    avg_score: float
    exam_count_log1p: float
    pass_rate: float
    is_pass: int

    # optional context for feedback template (biar tidak error)
    tutorial_title: str | None = None
    topic: str | None = None

class MotivationalLetterResponse(BaseModel):
    predicted_score: float
    engagement_score: float
    engagement_level: str
    feedback: str
