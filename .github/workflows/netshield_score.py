from datetime import datetime, timezone


def score_ip_entry(ip: str, data: dict, now: datetime):
    """Return NETSHIELD confidence score (0-100) and parsed dates, or None on invalid dates."""
    is_hq = data.get("hq", False)
    feed_count = len(data.get("feeds", []))
    today_count = data.get("today_count", 0)
    days_seen = data.get("days_seen", 0)
    last_seen = data.get("last", "2000-01-01")
    first_seen = data.get("first", last_seen)

    try:
        last_dt = datetime.strptime(last_seen, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        first_dt = datetime.strptime(first_seen, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except Exception:
        return None

    days_since_last = (now - last_dt).days
    days_known = (now - first_dt).days + 1

    if is_hq:
        score_a = 40
    elif today_count >= 5:
        score_a = 35
    elif today_count >= 3:
        score_a = 28
    elif today_count >= 2:
        score_a = 20
    elif feed_count >= 5:
        score_a = 15
    elif feed_count >= 3:
        score_a = 10
    elif feed_count >= 2:
        score_a = 5
    else:
        score_a = 0

    if days_since_last <= 1:
        score_b = 30
    elif days_since_last <= 3:
        score_b = 25
    elif days_since_last <= 7:
        score_b = 20
    elif days_since_last <= 14:
        score_b = 12
    elif days_since_last <= 30:
        score_b = 6
    else:
        score_b = 0

    if days_seen >= 14:
        score_c = 20
    elif days_seen >= 7:
        score_c = 15
    elif days_seen >= 3:
        score_c = 10
    elif days_seen >= 2:
        score_c = 6
    else:
        score_c = 2

    if days_known >= 90:
        score_d = 10
    elif days_known >= 30:
        score_d = 6
    elif days_known >= 14:
        score_d = 3
    else:
        score_d = 0

    conf = min(score_a + score_b + score_c + score_d, 100)
    return {
        "score": conf,
        "last_dt": last_dt,
        "first_dt": first_dt,
        "days_since_last": days_since_last,
        "days_known": days_known,
    }
