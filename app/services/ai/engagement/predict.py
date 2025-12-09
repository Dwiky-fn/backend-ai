import numpy as np
from .load_model import model_engagement, feature_cols_engagement, scaler_engagement
from .insight import time_category, generate_time_insight

def predict_engagement(payload: dict):

    # build vector with correct feature order
    X = np.array([[payload.get(col, 0) for col in feature_cols_engagement]], dtype=float)

    # scale first
    X_scaled = scaler_engagement.transform(X)

    # classes
    classes = model_engagement.classes_
    proba = model_engagement.predict_proba(X_scaled)[0]
    pred = int(model_engagement.predict(X_scaled)[0])

    # check if broken model (only 1 class)
    if len(classes) == 1:
        pred = model_engagement.predict(X_scaled)[0]
        return {
            "status": "warning",
            "message": "Model hanya memiliki 1 kelas, fallback enabled.",
            "fallback_prediction": int(pred),
            "classes": classes.tolist()
        }

    # ---- ADD THIS PART ----
    peak_hour = int(payload.get("peak_hour", 0))  # if provided
    time_cat = time_category(peak_hour)
    insight = generate_time_insight(peak_hour)
    # ------------------------

    return {
        "prediction": pred,
        "probabilities": {
            str(classes[i]): float(proba[i]) for i in range(len(classes))
        },

        # NEW KEYS
        "peak_hour": peak_hour,
        "time_cat": time_cat,
        "insight": insight
    }
