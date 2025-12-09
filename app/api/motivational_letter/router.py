from fastapi import APIRouter
from app.api.motivational_letter.schema import (
    MotivationalLetterRequest,
    MotivationalLetterResponse
)
from app.services.ai.motivational_letter.predict import predict_motivational_letter

router = APIRouter(prefix="/motivational-letter", tags=["Motivational Letter"])

@router.post("/", response_model=MotivationalLetterResponse)
def motivational_letter_route(req: MotivationalLetterRequest):
    """
    Predict motivational letter scoring and engagement level.
    """
    result = predict_motivational_letter(req.dict())
    return result
