import os
import joblib
from tensorflow import keras

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# scaler masih tetap di joblib_models dalam services/ai
SCALER_PATH = os.path.join(BASE_DIR, "..", "..", "..", "models", "joblib", "progress_mingguan.save")

# model keras pindah ke app/models/keras
MODEL_PATH = os.path.join(BASE_DIR, "..", "..", "..", "models", "keras", "progress_mingguan.keras")

feature_cols_progress = ["score_prev", "pass_rate"]
scaler_progress = joblib.load(SCALER_PATH)
model_progress  = keras.models.load_model(MODEL_PATH)

