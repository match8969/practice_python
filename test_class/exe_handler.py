import sys
import os
import args_handler

"""
Image:
class: 
ArgsHandler 
FileHandler -> CsvFileHandler, TxtFileHandler, and more...
StrategyHandler(hypo) -> LowerCut, Adjust X,Y axis range and more ... 
GraphHandler -> BarGraphHandler, PlotGraphHandler and more...
"""

# Execution Part
argvs = sys.argv
args_handler = args_handler.ArgsHandler(argvs)

count_args = args_handler.count_args()

if count_args == 1:
    print('Confirm the argument')
elif count_args ==2:
    print('you have something ... ')

# image
dict_args = {}
dict_args = args_handler.



# test
# args_handler = args_handler.ArgsHandler(argvs)
# args_handler.show_args()

# test
print('count_args =')
print(count_args)