def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    if not all(
        isinstance(s, int) and isinstance(e, int)
        for s, e in permanence_period
    ):
        return None

    for s, e in permanence_period:
        if s <= target_time <= e:
            counter += 1
    return counter
