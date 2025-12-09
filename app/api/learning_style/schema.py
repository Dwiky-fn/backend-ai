from pydantic import BaseModel
from typing import Dict

class LearningStyleRequest(BaseModel):
    days_active: float
    pct_days_active: float
    median_daily_completed: float
    std_daily_completed: float
    cv_daily_completed: float
    max_completed_one_day: float
    total_completed: float
    avg_completion_rate: float
    pct_fast_days: float
    avg_time_per_tutorial: float
    avg_revisits: float
    pct_revisited: float
    median_time_to_complete: float
    avg_quiz_score: float
    quiz_pass_rate: float
    num_quizzes: float
    num_submissions: float
    avg_submission_rating: float


class LearningStyleResponse(BaseModel):
    primary_learning_style: str
    secondary_learning_style: str
    probabilities: Dict[str, float]
    ml_primary: str
    rule_applied: bool
