import os
import joblib
from tensorflow import keras

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCALER_PATH = os.path.join(
    BASE_DIR, "..", "..", "..", "models", "joblib", "motivational_letter.save"
)

MODEL_PATH = os.path.join(
    BASE_DIR, "..", "..", "..", "models", "keras", "motivational_letter.keras"
)

scaler_motivational = joblib.load(SCALER_PATH)
model_motivational = keras.models.load_model(MODEL_PATH)

feature_cols_motivational = [
    "time_to_finish",
    "difficulty_num",
    "avg_score",
    "exam_count_log1p",
    "pass_rate",
    "is_pass",
]
