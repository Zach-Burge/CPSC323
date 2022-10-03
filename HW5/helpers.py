import matplotlib.pyplot as plt

def discretize_gender(col):
    new_vals = []
    for val in col:
        if val == "Male":
            new_vals.append('0')
        else:
            new_vals.append('1')
    return new_vals

def discretize_married(col):
    new_vals = []
    for val in col:
        if val == "Yes":
            new_vals.append('1')
        else:
            new_vals.append('0')
    return new_vals

def discretize_work_type(col):
    new_vals = []
    for val in col:
        if val == "Private":
            new_vals.append('0')
        elif val == "Self-employed":
            new_vals.append('1')
        elif val == "Govt_job":
            new_vals.append('2')
        else:
            new_vals.append('3')
    return new_vals

def discretize_residence_type(col):
    new_vals = []
    for val in col:
        if val == "Urban":
            new_vals.append('0')
        else:
            new_vals.append('1')
    return new_vals

def discretize_smoking_status(col):
    new_vals = []
    for val in col:
        if val == "formerly smoked":
            new_vals.append('0')
        elif val == "never smoked":
            new_vals.append('1')
        elif val == "smokes":
            new_vals.append('2')
        else:
            new_vals.append('3')
    return new_vals

def replace_col_vals(table, new_vals, col_name):
    col_idx = table.column_names.index(col_name)
    for i, row in enumerate(table.data):
        row[col_idx] = new_vals[i]

def scatter_plot(x, y, x_label, y_label, caption=""):
    """Plots a scatter plot

    Args:
        x (list of float) : the list of independent values
        y (list of float) : the list of dependent values
        x_label (str) : the label for the x-axis
        y_label (str) : the label for the y-axis
    """
    plt.figure(figsize=(20, 10)) # make a new current figure
    plt.scatter(x, y, marker=".", s=50, c="blue")
    plt.title(x_label + " vs " + y_label, fontsize = 24)
    plt.text(500, 0, caption, fontsize="x-large", ha="center")
    plt.xlabel(x_label, fontsize=20)
    plt.ylabel(y_label, fontsize=20)
    # you can save a figure to a file
    plt.tight_layout() # nice function to call right before rendering
    plt.show()