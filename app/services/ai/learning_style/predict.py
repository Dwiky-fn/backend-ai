import numpy as np
from app.services.ai.learning_style.load_model import rf_model, scaler_rf, label_encoder, feature_cols

def predict_learning_style(features: dict):
    # ---- ML Predict ----
    X = [features[col] for col in feature_cols]
    X_scaled = scaler_rf.transform([X])

    proba = rf_model.predict_proba(X_scaled)[0]
    primary_idx = int(np.argmax(proba))
    primary_ml = label_encoder.inverse_transform([primary_idx])[0]

    # secondary ML
    sorted_idx = np.argsort(proba)[::-1]
    secondary_idx = int(sorted_idx[1])
    secondary_ml = label_encoder.inverse_transform([secondary_idx])[0]

    probability_dict = {
        label_encoder.inverse_transform([i])[0]: float(proba[i])
        for i in range(len(proba))
    }

    # ---- RULE OVERRIDE (FAST) ----
    is_fast_behavior = (
        features["pct_fast_days"] > 0.7 and
        features["avg_time_per_tutorial"] < 60 and
        features["avg_revisits"] < 1 and
        features["pct_revisited"] < 0.10
    )

    if is_fast_behavior:
        primary_final = "fast"
        secondary_final = primary_ml      # fallback ML
    else:
        primary_final = primary_ml
        secondary_final = secondary_ml

    return {
        "primary_learning_style": primary_final,
        "secondary_learning_style": secondary_final,
        "probabilities": probability_dict,
        "ml_primary": primary_ml,             # tambahan untuk debugging
        "rule_applied": is_fast_behavior      # true/false
    }
