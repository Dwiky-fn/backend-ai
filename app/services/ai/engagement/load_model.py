import joblib
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
MODEL_PATH = CURRENT_DIR.parents[3] / "app" / "models" / "joblib" / "engagement_model_stable.joblib"

_loaded = joblib.load(MODEL_PATH)

scaler_engagement = _loaded["scaler"]
model_engagement = _loaded["model"]
feature_cols_engagement = _loaded["feature_cols"]  # <-- key benar
