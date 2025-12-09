from fastapi import APIRouter
from app.api.learning_style.schema import LearningStyleRequest, LearningStyleResponse
from app.services.ai.learning_style.predict import predict_learning_style

router = APIRouter(prefix="/learning-style", tags=["Learning Style"])


@router.post("/", response_model=LearningStyleResponse)
def predict_learning_style_route(req: LearningStyleRequest):
    """
    Predict user learning style (fast / consistent / reflective)
    """
    data = req.dict()
    result = predict_learning_style(data)
    return result
