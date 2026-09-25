def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    classes = set(y_true) | set(y_pred)

    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for cls in classes:
        for i in range(len(y_true)):
            if y_true[i] == cls and y_pred[i] == cls:
                true_positives += 1
            elif y_true[i] != cls and y_pred[i] == cls:
                false_positives += 1
            elif y_true[i] == cls and y_pred[i] != cls:
                false_negatives += 1

    if 2 * true_positives + false_positives + false_negatives == 0:
        return 0.0

    f1_micro = (
        2 * true_positives
        / (2 * true_positives + false_positives + false_negatives)
    )

    return round(f1_micro, 4)