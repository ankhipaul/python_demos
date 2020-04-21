##########################################################################
#### Written By: ANKHI PAUL                                           ####
#### Written On: 17-APR-2020                                          ####
#### Modified On 17-APR-2020                                          ####
#### Objective: Validating structure of several excels of a directory ####
##########################################################################

import pandas as pd


class Transformation:
    """
    Initializing class attribute 'files'
      Getting the parameter files from excel_file_reader class
    """

    def __init__(self, files=None):
        self.files = files

    def data_transformation(self):
        """
        Initializing a dataframe to append all data
        """
        all_data_df = pd.DataFrame()
        df = pd.DataFrame()
        """
        Reading the first file for column names to treat that as a template
        """
        first_file_df = pd.read_excel(self.files[0])
        first_file_df['Sheet_Name'], first_file_df['Excel_Name'] = ['A', 'B']
        first_file_col = list(first_file_df.columns)
        """
            For each file in the source directory
             get the data from all sheets of excel
        """
        for fname in self.files:
            df_with_odict = pd.read_excel(fname, sheet_name=None)
            for sheetname, frame in df_with_odict.items():
                """ 
                 Adding two extra columns Sheet_Name and Excel_Name 
                """
                frame['Sheet_Name'] = pd.Series([sheetname for x in range(len(frame.index))])
                frame['Excel_Name'] = pd.Series([fname.split('\\')[-1] for x in range(len(frame.index))])
                """ 
                  If column of excels match with the first excel, 
                  Appending all data to one Data Frame all_data_df
                """
                if list(frame.columns) == first_file_col:
                    all_data_df = all_data_df.append(frame, sort=False). \
                        drop_duplicates('Employeeid', keep='first'). \
                        reindex(list(first_file_df.columns), axis=1)
                else:
                    selected_col = pd.Index(frame.columns) & pd.Index(first_file_col)

                    df = df.reindex(columns=list(first_file_df.columns)). \
                        from_records(frame, columns=list(selected_col)) \
                        .drop_duplicates('Employeeid', keep='first')

                    """ 
                     Find out the missing columns and add 'NA' as value
                    """
                    extra_col = list(set(first_file_col).difference(selected_col))
                    if not extra_col:
                        all_data_df = all_data_df.append(df, sort=False) \
                            .reindex(columns=list(first_file_df.columns))
                    else:
                        for i in extra_col:
                            df[i] = 'NA'
                        """ 
                        Appending all non_mathingdata to one Data Frame all_data_df
                        """
                        all_data_df = all_data_df.append(df, sort=False).reindex(columns=list(first_file_df.columns))
        return all_data_df
