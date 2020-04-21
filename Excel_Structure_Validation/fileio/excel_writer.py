##########################################################################
#### Written By: ANKHI PAUL                                           ####
#### Written On: 17-APR-2020                                          ####
#### Modified On 17-APR-2020                                          ####
#### Objective: To read excels from a directory based on a pattern    ####
##########################################################################
import pandas as pd


class ExcelWriter:
    """
    Initializing class attribute 'currentdirectory' and 'all_data_df'
    currentdirectory is passed from excel_reader.py
    all_data_df is passed from transformation.py
    """

    def __init__(self, currentdirectory=None, all_data_df=None):
        self.currentdirectory = currentdirectory
        self.all_data_df = all_data_df

    def excel_writer(self):
        writer = pd.ExcelWriter('{}\\pandas_multiple.xlsx'.format(self.currentdirectory))
        """
        Exporting the data frame with all data to one target excel 
        """
        self.all_data_df.to_excel(writer, index=False, header=True)
        writer.save()
