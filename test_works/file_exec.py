# -*- coding: utf-8 -*-


# Execution example:: $ python this.py abc.pgm def.txt
import subprocess
import os
import os.path
import sys
import numpy as np
import matplotlib.pyplot as plt
import re


# Return minimun value from dict
def get_min_val(param_dict):
    min_number = min(param_dict.values())
    return min_number


# cut the lower value under minimum val
def cut_dict_value_under_min(param_dict, min_number):
    reduced_dict = {}
    for key, val in param_dict.items():
        val -= min_number
        reduced_dict[key] = val
    return reduced_dict


def get_difinition(path):
    dict_def = {}
    list_content_num = []
    with open(path, 'r') as f:
        count = 0
        contents = f.read()
        lines = contents.split("\n")
        for line in lines:
            nums = line.split(" ")
            for num in nums:
                if num.isdigit():
                    num = int(num)
                    if count == 0:
                        dict_def["width"] = num
                    elif count == 1:
                        dict_def["height"] = num
                    elif count == 2:
                        dict_def["max_number"] = num
                    else:
                        list_content_num.append(num)
                    count += 1
    return dict_def, list_content_num


def get_dict_for_fivegrapth(list_number):
    dict_colors_val = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5 and more': 0}

    for element in list_number:
        if element < 1:
            dict_colors_val['0'] += 1
        elif element < 2:
            dict_colors_val['1'] += 1
        elif element < 3:
            dict_colors_val['2'] += 1
        elif element < 4:
            dict_colors_val['3'] += 1
        elif element < 5:
            dict_colors_val['4'] += 1
        elif element >= 5:
            dict_colors_val['5 and more'] += 1
        else:
            print("[DEBUG] Invalid. Element is Not Number")

    return dict_colors_val


# for args[1]
def show_graph_fivecolor(filepath):
    list_elements = []
    dict_pgm_difinition = {}

    # Set the contents
    dict_pgm_difinition, list_elements = get_difinition(filepath)
    # Set dict for the graph
    dict_pgm_difinition = get_dict_for_fivegrapth(list_elements)
    # Set Each params
    list_key = dict_pgm_difinition.keys()
    list_values = dict_pgm_difinition.values()
    x = np.array(list_key)
    y = np.array(list_values)
    # Create graph
    plt.bar(x, y)
    plt.show()


# End of show_graph_fivecolor

# for argss[2]
# for txt
def get_graph_eachlines(path):
    dict_graph = {}
    with open(path, 'r') as f:
        count = 1
        contents = f.read()
        lines = contents.split("\n")
        for number in lines:
            if number.isdigit():
                number = int(number)
                dict_graph[count] = number
                count += 1
    return dict_graph


# for csv
def get_graph_csv(path):
    dict_graph = {}
    with open(path, 'r') as f:
        count = 0
        for row in f:
            columns = row.rstrip().split(',')
            for colum in columns:
                if colum.isdigit():
                    number = int(colum)
                    dict_graph[count] = number
                    count += 1
    return dict_graph


def get_dict_for_fivegrapth_6elements(list_number):
    dict_colors_val = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5 and more': 0}
    element = 0
    for number in list_number:

        if element < 1:
            dict_colors_val['0'] = number
        elif element < 2:
            dict_colors_val['1'] = number
        elif element < 3:
            dict_colors_val['2'] = number
        elif element < 4:
            dict_colors_val['3'] = number
        elif element < 5:
            dict_colors_val['4'] = number
        elif element >= 5:
            dict_colors_val['5 and more'] = number
        else:

            break
        element += 1

    return dict_colors_val


def convert_dict_to_five_grayscale(param_dict):
    gray_dict = {}
    list_values = param_dict.values()
    gray_dict = get_dict_for_fivegrapth_6elements(list_values)
    return gray_dict


def show_graph(param_dict, title, filename):
    Y_AXIS_LIMIT_RANGE = []
    # X_AXIS_LIMIT_RANGE = []
    list_key = param_dict.keys()
    list_value = param_dict.values()
    # Get Possible Max and Min Y values
    max_y_number = max(param_dict.values())
    min_y_number = min(param_dict.values())
    possible_value_range = max_y_number - min_y_number
    # Set Y axis range
    max_y_axis = max_y_number + (possible_value_range // 10)
    min_y_axis = 0
    if min_y_number - (possible_value_range // 10) > 0:
        min_y_axis = (min_y_number - (possible_value_range // 10))
    Y_AXIS_LIMIT_RANGE.append(int(min_y_axis))
    Y_AXIS_LIMIT_RANGE.append(int(max_y_axis))

    x = np.array(list_key)
    y = np.array(list_value)
    # Make Graph
    plt.plot(x, y, label=filename)
    # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=18)
    plt.legend(bbox_to_anchor=(1, 0), loc='lower right', borderaxespad=1, fontsize=10.5)
    # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=18)
    plt.ylim(Y_AXIS_LIMIT_RANGE)
    plt.title(title)
    plt.show()


# ---------class part ---------
class FileDto:
    def __init__(self, path):
        self.path = path
        self.file_name = os.path.basename(path)
        self.file_type = os.path.splitext(path)[1]

    def get_filepath(self):
        return self.path


class GraphHandler:
    def __init__(self, dict_graph_setting):
        self.dict_graph_setting = dict_graph_setting

    def show_graph(self, dict_filecontents):
        dict_graph_setting = self.dict_graph_setting

        list_key = dict_filecontents.keys()
        list_value = dict_filecontents.values()

        x = np.array(list_key)
        y = np.array(list_value)
        # Make Graph
        label_name = str(dict_graph_setting['file_name'])
        plt.plot(x, y, label=label_name)
        plt.title(dict_graph_setting['title'])
        # Optional
        plt.legend(bbox_to_anchor=(1, 0), loc='lower right', borderaxespad=1, fontsize=10.5)
        # Check dict has y_range_setting or not
        if 'y_axis_limit_range' in self.dict_graph_setting.keys():
            plt.ylim(dict_graph_setting['y_axis_limit_range'])

        plt.show()

    def set_y_axis_range_one_tenth(self):
        # Get Possible Max and Min Y values
        Y_AXIS_LIMIT_RANGE = []
        # X_AXIS_LIMIT_RANGE = []
        max_y_number = max(self.dict_graph_setting.values())
        min_y_number = min(self.dict_graph_setting.values())
        possible_value_range = max_y_number - min_y_number
        # Set Y axis range
        max_y_axis = max_y_number + (possible_value_range // 10)
        min_y_axis = 0
        if min_y_number - (possible_value_range // 10) > 0:
            min_y_axis = (min_y_number - (possible_value_range // 10))
            Y_AXIS_LIMIT_RANGE.append(int(min_y_axis))
        Y_AXIS_LIMIT_RANGE.append(int(max_y_axis))
        return Y_AXIS_LIMIT_RANGE


class GraphSetting():
    GRAPH_TYPE = ['bar', 'plot']

    def __init__(self, title, graph_type, file_name):
        self.title = title
        self.file_name = file_name

        if str(graph_type) in self.GRAPH_TYPE:
            self.graph_type = str(graph_type)
        else:
            return

    def get_dict_graph_setting(self):
        dict_graph_setting = {}
        dict_graph_setting['title'] = self.title
        dict_graph_setting['graph_type'] = self.graph_type
        dict_graph_setting['file_name'] = self.file_name

        return dict_graph_setting

    def add_y_axis_limit(self, list_y_axis_limit):
        self.y_axis_limit = list_y_axis_limit
        return


"""  
class FileHandler():
    def __init__(self):
        pass
"""


class CsvFileHandler():

    def __init__(self, csvfilepath):
        self.path = csvfilepath

    def get_graph_csv(self):
        path = self.path
        dict_graph = {}
        with open(path, 'r') as f:
            count = 0
            for row in f:
                columns = row.rstrip().split(',')
                for colum in columns:
                    if colum.isdigit():
                        number = int(colum)
                        dict_graph[count] = number
                        count += 1
        return dict_graph

    # ----------Excecution part ----------


argvs = sys.argv

if os.path.isfile(argvs[1]):

    # Create FirstPath Instance
    first_file = FileDto(argvs[1])

    # PGM Application
    if re.search('^\.pgm$', first_file.file_type):
        PGMFILE_PATH = first_file.path
        # to open irfanview
        APPLICATION_PATH = r"C:\Program Files\IrfanView\i_view64.exe"

        # Execution irFanView Application if pc has
        if os.path.exists(APPLICATION_PATH):
            subprocess.Popen(['start', PGMFILE_PATH], shell=True)

        # Execution pgmfile to graph at five level colors
        show_graph_fivecolor(PGMFILE_PATH)
    # TXT Graph
    elif re.search('^\.txt$', first_file.file_type):
        dict_file = get_graph_eachlines(first_file.path)
        min_number = get_min_val(dict_file)
        dict_file_undercut = cut_dict_value_under_min(dict_file, min_number)
        show_graph(dict_file, "TXT graph\n x=row number, y=each value")

    # CSV Graph
    elif re.search('^\.csv$', first_file.file_type):

        # Make graph for 250 values of csv
        graph_setting_1 = GraphSetting('Value Graph of CSVfile', 'plot', first_file.file_name)
        temp_dict = graph_setting_1.get_dict_graph_setting()
        graph_handler_1 = GraphHandler(temp_dict)
        csv_filehandler = CsvFileHandler(first_file.get_filepath())
        filecontents = csv_filehandler.get_graph_csv()
        graph_handler_1.show_graph(filecontents)

    else:
        print('Invalid. PGM, TXT and CSV are in support')

if len(argvs) > 2:
    if os.path.isfile(argvs[2]):

        second_file = FileDto(argvs[2])
        # get filename
        file_name = os.path.basename(second_file.path)
        # get file type
        name, file_type = os.path.splitext(second_file.path)

        if re.search('^\.txt$', file_type):
            dict_file = get_graph_eachlines(second_file.path)
            min_number = get_min_val(dict_file)
            dict_file_undercut = cut_dict_value_under_min(dict_file, min_number)
            show_graph(dict_file, "TXT graph\n x=row number, y=each value")
        elif re.search('^\.csv$', file_type):
            dict_file = get_graph_csv(second_file.path)
            min_number = get_min_val(dict_file)
            dict_file_undercut = cut_dict_value_under_min(dict_file, min_number)
            show_graph(dict_file_undercut, "CSV graph\n x=order number from left, y=each value")
        else:
            print('Invalid. PGM, TXT and CSV are in support')

