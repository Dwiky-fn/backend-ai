from fastapi import APIRouter
from app.api.engagement.schema import EngagementRequest
from app.services.ai.engagement.predict import predict_engagement

router = APIRouter(prefix="/engagement", tags=["Engagement"])

@router.post("/")
def predict_engagement_route(req: EngagementRequest):
    return predict_engagement(req.dict())
