
import os
# for root, dirs, files in os.walk('/User/match/Desktop/programming_test/csv_test'): Did not work well..
for root, dirs, files in os.walk('.'):
    print("root={}, \t dirs={}, \t files={}".format(root, dirs, files))  # worked well


