def percent_change(series):
    per_change = []
    
    for i in range(1, len(series)):
        if series[i - 1] == 0:
            per_change.append(0)
        else:
            change = (series[i] - series[i - 1]) / series[i - 1]
            per_change.append(change)
    
    return per_change