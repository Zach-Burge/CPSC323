from table import Table
import numpy as np

def train_test_split(X, y, test_size=0.33, random_state=None, shuffle=True):
    if test_size < 1:
        X_test_size = int(np.ceil(len(X)*test_size))
        X_train_size = len(X) - X_test_size
        y_test_size = int(np.ceil(len(y)*test_size))
        y_train_size = len(y) - y_test_size
    else:
        X_test_size = test_size
        X_train_size = len(y) - X_test_size
        y_test_size = test_size
        y_train_size = len(y) - y_test_size
    
    if shuffle:
        X_shuffled = np.random.RandomState(random_state).permutation(len(X))
        y_shuffled = np.random.RandomState(random_state).permutation(len(y))
        X_test_indices = X_shuffled[:X_test_size]
        X_test = [X[val] for val in X_test_indices]

        X_train_indices = X_shuffled[X_test_size:]
        X_train = [X[val] for val in X_train_indices]

        y_test_indices = y_shuffled[:y_test_size]
        y_test = [y[val] for val in y_test_indices]

        y_train_indices = y_shuffled[y_test_size:]
        y_train = [y[val] for val in y_train_indices]
    else:
        X_train_indices = np.arange(X_train_size)
        X_train = [X[val] for val in X_train_indices]

        X_test_indices = np.arange(X_train_size, len(X))
        X_test = [X[val] for val in X_test_indices]

        y_train_indices = np.arange(y_train_size)
        y_train = [y[val] for val in y_train_indices]

        y_test_indices = np.arange(y_train_size, len(y))
        y_test = [y[val] for val in y_test_indices] 

    return X_train, X_test, y_train, y_test

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
    recall = 0

    for i in range(len(actuals)):
        if preds[i] == 0 and actuals[i] == 0:
            true_pos += 1
        elif preds[i] == 1 and actuals[i] == 0:
            false_neg += 1
        else:
            pass
    # try:
    recall = true_pos / (true_pos + false_neg)
    # except ZeroDivisionError:
    #     recall = 0
    
    return recall

def compute_f1(actuals, preds):
    precision = compute_precision(actuals, preds)
    recall = compute_recall(actuals, preds)

    f1 = 2 / ((1 / recall) + (1 / precision))

    return f1

def confusion_matrix(actuals, preds, labels):
    matrix = [[0 for i in range(len(labels))] for i in range(len(labels))]
    for i, val in enumerate(actuals):
        try:
            matrix[labels.index(val)][labels.index(preds[i])] += 1
        except ValueError:
            pass
    return matrix

def print_confusion_matrix(method_used, labels, confusion_matrix):
    """Method to print a confusion matrix"""
    labels.insert(0, "Outcome?")
    labels.append("Total")
    labels.append("Recognition (%)")
    for i in range(2):
        confusion_matrix[i].insert(0, labels[i + 1])
        row_total = sum(confusion_matrix[i][1:3])
        confusion_matrix[i].append(row_total)
        this_recognition = round(100*(confusion_matrix[i][i+1]/row_total)) if row_total != 0 else 0
        confusion_matrix[i].append(this_recognition)
    confusion_matrix_table = Table(labels, confusion_matrix)

    print(method_used + ":")
    print("===========================================")
    confusion_matrix_table.pretty_print()
    print()
        