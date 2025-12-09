from pydantic import BaseModel

class EngagementRequest(BaseModel):
    user_id: float
    total_study_time_seconds: float
    sessions_count: float
    avg_session_seconds: float
    distinct_tutorials_viewed: float
    tutorial_completed_count: float
    completion_rate: float
    total_submissions: float
    _t: float
    _s: float
    _c: float
    engagement_score: float
    peak_hour: int
