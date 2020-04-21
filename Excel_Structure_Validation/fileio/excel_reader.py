##########################################################################
#### Written By: ANKHI PAUL                                           ####
#### Written On: 17-APR-2020                                          ####
#### Modified On 17-APR-2020                                          ####
#### Objective: To read excels from a directory based on a pattern    ####
##########################################################################

import glob
import os


class ExcelFileReader:
    """
    Initializing class attribute
    """

    def __init__(self, currentdirectory=None, pattern=None):
        self.currentdirectory = currentdirectory
        self.pattern = pattern

    def read_files(self):
        """
        Getting the current directory of the .py script and the respective subdirectories
        reference:https://www.pythonlearn.com/html-008/cfbook017.html
        """

        subdirectories = [f.name for f in os.scandir(self.currentdirectory) if f.is_dir()]

        """
        Searching for the source files subdirectories and assign the path to read files
        """
        for i in subdirectories:
            if i == 'Source_excel_files':
                path = '{}\\{}\\*{}'.format(self.currentdirectory, i, self.pattern)
            else:
                continue
        """
         Sorting the files in source directory based on time to get the first file 
            reference:https://stackoverflow.com/questions/23430395/glob-search-files-in-date-order
         """

        files = glob.glob(path)
        files.sort(key=os.path.getmtime)
        """
          Return the list of files to main function in the form of a list
        """
        return files
