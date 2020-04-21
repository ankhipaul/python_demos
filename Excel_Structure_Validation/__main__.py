##############################################################
#### Written By: ANKHI PAUL                               ####
#### Written On: 20-APR-2020                              ####
#### Modified On 20-APR-2020                              ####
#### Objective: Main calling script                       ####
##############################################################

import os
from fileio.transformation import Transformation
from fileio.excel_reader import ExcelFileReader
from fileio.excel_writer import ExcelWriter

currentdirectory = os.getcwd()

if __name__ == '__main__':
    e1 = ExcelFileReader(currentdirectory, 'ankhi.xlsx')
    t1 = Transformation(e1.read_files())
    ExcelWriter(currentdirectory, t1.data_transformation()).excel_writer()
    print('Excel File Validation Complete')
