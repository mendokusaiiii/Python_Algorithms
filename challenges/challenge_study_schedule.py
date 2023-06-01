def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for input, output in permanence_period:
            if input <= target_time <= output:
                counter += 1
    except TypeError:
        return None
    return counter
