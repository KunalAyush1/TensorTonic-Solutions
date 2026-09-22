import numpy as np
def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    encoding = np.zeros(len(targets))
    counter = np.zeros(len(targets))

    for i in range(len(encoding)):
        for j in range(len(encoding)):
            if categories[i] == categories[j]:
                encoding[i] += targets[j]
                counter[i] += 1


    finalencoding = np.zeros(len(targets))

    for i in range(len(encoding)):
        finalencoding[i] = encoding[i] / counter[i]


    return list(finalencoding)

    