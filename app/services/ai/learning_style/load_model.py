from pathlib import Path
import joblib

CURRENT_DIR = Path(__file__).parent
MODEL_PATH = CURRENT_DIR.parents[3] / "app" / "models" / "joblib" / "learning_style_model.joblib"

learning_style_model = joblib.load(MODEL_PATH)

rf_model = learning_style_model["rf"]
scaler_rf = learning_style_model["scaler_rf"]
feature_cols = learning_style_model["feature_cols"]
label_encoder = learning_style_model["le"]
