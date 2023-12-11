def find_true_intervals(lst: list) -> list:
    intervals = []
    current_interval = []

    for i, value in enumerate(lst):
        if value:
            if not current_interval:
                current_interval.append(i)
        elif current_interval:
            current_interval.append(i - 1)
            intervals.append(current_interval)
            current_interval = []

    if current_interval:
        current_interval.append(len(lst) - 1)
        intervals.append(current_interval)

    return intervals
