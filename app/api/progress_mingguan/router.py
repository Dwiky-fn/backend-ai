from fastapi import APIRouter
from .schema import ProgressInput, ProgressOutput
from app.services.ai.progress_mingguan.predict import predict_progress_mingguan

router = APIRouter(prefix="/weekly-progress", tags=["Progress Mingguan"])

@router.post("/", response_model=ProgressOutput)
def predict_progress_route(req: ProgressInput):
    result = predict_progress_mingguan(req.dict())
    return ProgressOutput(**result)
