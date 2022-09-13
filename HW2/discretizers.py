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