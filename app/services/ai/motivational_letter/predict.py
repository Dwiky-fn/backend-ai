import numpy as np
import pandas as pd
import random
from .load_model import (
    scaler_motivational,
    model_motivational,
    feature_cols_motivational,
)

templates = {
    "Low": [
        "{examinees_id}, minggu ini terlihat cukup berat. Coba fokus ulang pada topik {topic} dan ambil jeda belajar yang teratur.",
        "Tetap semangat {examinees_id}! Pelajari kembali materi {tutorial_title} agar pemahamanmu makin kuat."
    ],
    "Medium": [
        "Kerja bagus, {examinees_id}! Kamu berada di jalur yang tepat. Tingkatkan sedikit lagi di bagian {topic}.",
        "{examinees_id}, progresmu bagus! Sedikit konsistensi tambahan akan membuatmu naik level."
    ],
    "High": [
        "Luar biasa, {examinees_id}! Terus pertahankan performa hebat ini.",
        "Keren sekali {examinees_id}! Kamu sudah sangat kuat di materi ini. Coba tantang dirimu dengan soal yang lebih sulit!"
    ]
}

def rule_engagement(data):
    """
    RULE-BASED scoring untuk menggantikan model keras
    """

    time_to_finish = data["time_to_finish"]
    avg_score = data["avg_score"]
    pass_rate = data["pass_rate"]
    difficulty = data["difficulty_num"]
    is_pass = data["is_pass"]

    score = 0

    # waktu pengerjaan
    if time_to_finish > 200: score -= 20
    elif time_to_finish < 100: score += 20

    # nilai
    if avg_score < 60: score -= 30
    elif avg_score < 80: score += 10
    else: score += 30

    # pass rate
    if pass_rate < 0.5: score -= 20
    elif pass_rate < 0.8: score += 10
    else: score += 20

    # difficulty
    score += difficulty * 5

    # lulus/gagal
    if is_pass == 0: score -= 15
    else: score += 10

    # normalisasi biar enak dibaca
    score = max(0, min(100, score))

    return score

def classify(score):
    if score < 40: return "Low"
    if score < 75: return "Medium"
    return "High"

def generate_feedback(level, data):
    template = random.choice(templates[level])
    return template.format(
        examinees_id=data["examinees_id"],
        tutorial_title=data.get("tutorial_title", "materi ini"),
        topic=data.get("topic", "topik ini")
    )

def predict_motivational_letter(data: dict):

    # --- abaikan hasil model keras, tapi tetap panggil biar tidak error ---
    try:
        X = pd.DataFrame([data])[feature_cols_motivational].astype(float)
        X_scaled = scaler_motivational.transform(X)
        keras_output = model_motivational.predict(X_scaled)
        predicted_score = float(keras_output[0].flatten()[0])
    except:
        predicted_score = 0.0  # fallback aman

    # --- pakai RULE-BASED ---
    engagement_score = rule_engagement(data)
    engagement_level = classify(engagement_score)
    feedback = generate_feedback(engagement_level, data)

    return {
        "predicted_score": predicted_score,
        "engagement_score": engagement_score,
        "engagement_level": engagement_level,
        "feedback": feedback
    }
