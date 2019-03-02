def convert_to_hoshino_format(path_input, path_output):
    import pandas as pd

    df = pd.read_csv(path_input)
    list_lines = df.values.tolist()

    dict_k_col1_v_cols = {}
    for lines in list_lines:
        if lines[0] not in dict_k_col1_v_cols.keys():
            dict_k_col1_v_cols[lines[0]] = []
        for v_cols in lines[1:]:
            dict_k_col1_v_cols[lines[0]].append(v_cols)

    line_str = ""
    for k in dict_k_col1_v_cols.keys():
        line_str += k
        for v in dict_k_col1_v_cols[k]:
            line_str += ','
            line_str += str(v)
        line_str += '\n'

    with open(path_output, 'w') as f:
        f.write(line_str)


# Debug


path_test_result = "/Users/match/Desktop/programming_test/csv_test/no_mode_result.csv"
path_output_csv = "/Users/match/Desktop/programming_test/csv_test/for_hoshino_san_2.csv"
convert_to_hoshino_format(path_test_result, path_output_csv)  # worked well