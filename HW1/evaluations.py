def compute_accuracy(actuals, preds):
    correct_preds = 0
    total = len(actuals)
    for i, val in enumerate(preds):
        if val is actuals[i]:
            correct_preds += 1
    return round(correct_preds / total, 3)

def compute_precision(actuals, preds):
    true_pos = 0
    false_pos = 0
    precision = 0

    for i in range(len(actuals)):
        if preds[i] == actuals[i]:
            true_pos += 1
        else:
            false_pos += 1
    
    if true_pos + false_pos == 0:
        precision = 0
    else:
        precision = true_pos / (true_pos + false_pos)
    return precision

def compute_recall(actuals, preds):
    true_pos = 0
    false_neg = 0

    for i in range(len(actuals)):
        if preds[i] == 0 and actuals[i] == 0:
            true_pos += 1
        elif preds[i] == 1 and actuals[i] == 0:
            false_neg += 1
        else:
            pass
    try:
        recall = true_pos / (true_pos + false_neg)
    except ZeroDivisionError:
        recall = 0
    
    return recall

def compute_f1(actuals, preds):
    precision = compute_precision(actuals, preds)
    recall = compute_recall(actuals, preds)

    f1 = 2 * ((precision * recall) / (precision + recall))

    return f1
        