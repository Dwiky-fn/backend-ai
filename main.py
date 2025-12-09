from fastapi import FastAPI
from app.api.status.router import router as status_router
from app.api.learning_style.router import router as learning_style_router
from app.api.engagement.router import router as engagement_router
from app.api.motivational_letter.router import router as motivational_letter
from app.api.progress_mingguan.router import router as progress_mingguan

app = FastAPI(title='AI Microservice')

app.include_router(status_router, prefix='/status')
app.include_router(learning_style_router)
app.include_router(engagement_router)
app.include_router(motivational_letter)
app.include_router(progress_mingguan)

@app.get('/')
def root():
    return {"message": "Backend-AI OK"}
