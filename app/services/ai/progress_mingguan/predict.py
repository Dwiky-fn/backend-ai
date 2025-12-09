import pandas as pd
from .load_model import scaler_progress, model_progress, feature_cols_progress

def classify_progress(pred):
    if pred <= -25:
        return "Major Drop"
    elif pred <= -8:
        return "Drop"
    elif pred < 5:
        return "Stable"
    elif pred < 15:
        return "Improvement"
    return "Strong Improvement"


def generate_feedback(level, score):
    s = round(float(score), 1)

    if level == "Major Drop":
        return f"⚠️ Penurunan besar minggu ini ({s} poin). Yuk evaluasi ritme belajarmu."
    if level == "Drop":
        return f"Ada sedikit penurunan minggu ini ({s} poin). Yuk atur ulang jadwal belajarnya."
    if level == "Stable":
        return f"😐 Progresmu stabil minggu ini ({s} poin). Pertahankan ritmenya!"
    if level == "Improvement":
        return f"🔥 Ada peningkatan minggu ini (+{s} poin). Mantap lanjutin!"
    if level == "Strong Improvement":
        return f"🚀 Progresmu melonjak signifikan (+{s} poin). Pertahankan momentum ini!"

    return "Tetap semangat belajar!"


def predict_progress_mingguan(data: dict):

    score_prev = float(data.get("score_prev", 0))
    pass_rate = float(data.get("pass_rate", 0))

    # 1. Progress dari score sebelumnya
    progress_base = (score_prev - 70) * 0.4

    # 2. Progress dari pass rate
    progress_pass_rate = (pass_rate - 0.5) * 40

    # 3. Final progress
    predicted_progress = progress_base + progress_pass_rate

    # 4. Level
    level = classify_progress(predicted_progress)

    # 5. Feedback
    feedback = generate_feedback(level, predicted_progress)

    return {
        "predicted_progress": predicted_progress,
        "progress_level": level,
        "feedback": feedback
    }
