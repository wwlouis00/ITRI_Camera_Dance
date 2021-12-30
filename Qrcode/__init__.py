import os
if not os.path.isdir('./xlsx_result'):
    print("Directory 'para' does not exist.")
    os.mkdir('./xlsx_result')
    print("Directory 'para' is established.")
if not os.path.isdir('./image'):
    print("Directory 'result' does not exist.")
    os.mkdir('./image')
    print("Directory 'result' is established.")
