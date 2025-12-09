def time_category(hour: int) -> str:
    if hour is None:
        return "tidak diketahui"

    # Mapping waktu yang lebih natural
    if 0 <= hour < 5:
        return "larut malam"
    if 5 <= hour < 12:
        return "pagi hari"
    if 12 <= hour < 17:
        return "siang hari"
    if 17 <= hour < 21:
        return "sore hari"
    if 21 <= hour <= 23:
        return "malam hari"

    return "tidak diketahui"


def generate_time_insight(hour: int) -> str:
    category = time_category(hour)
    return f"Kamu paling aktif belajar di {category}."
