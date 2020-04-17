import glob
import pandas as pd
import os

#reference https://stackoverflow.com/questions/14262405/loop-through-all-csv-files-in-a-folder
path = r"C:\Users\H337845\Documents\Laptop to Drive\Studies\Python case studies\Python_Workspace\Problem_Excel_Structure_Validation\Source_excel_files\*.xlsx"

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(r"C:\Users\H337845\Documents\Laptop to Drive\Studies\Python case studies\Python_Workspace\Problem_Excel_Structure_Validation\pandas_multiple.xlsx")

#sorting the files in directory based on time
#reference  :https://stackoverflow.com/questions/23430395/glob-search-files-in-date-order
files = glob.glob(path)
files.sort(key=os.path.getmtime)

#initializing a dataframe to append all data
all_data_df =pd.DataFrame()
df = pd.DataFrame()
#reading the first file for column names
first_file_df = pd.read_excel(files[0])
first_file_df['Sheet_Name'], first_file_df['Excel_Name'] =['A', 'B']
first_file_col = list(first_file_df.columns)

for fname in files :

##reference :https://stackoverflow.com/questions/44286797/export-dataframe-with-sheetname-as-column
    df_with_odict = pd.read_excel(fname, sheet_name=None)
    #print(df_with_odict)

    for sheetname, frame in df_with_odict.items():
        # frame.assign(Sheet_Name= sheetname, Excel_Name= fname.split('\\')[9])
        # reference:https://stackoverflow.com/questions/24039023/add-column-with-constant-value-to-pandas-dataframe
        frame['Sheet_Name'] = pd.Series([sheetname for x in range(len(frame.index))])
        frame['Excel_Name'] = pd.Series([fname.split('\\')[9] for x in range(len(frame.index))])
        # Can also use
        # reference:https://stackoverflow.com/questions/46113078/pandas-add-value-at-specific-iloc-into-new-dataframe-column
        # frame.loc[range(len(frame.index)), 'Sheet_Name']= sheetname
        if list(frame.columns) == first_file_col:
            all_data_df = all_data_df.append(frame, sort=False).drop_duplicates('Employeeid',keep='first').reindex(list(first_file_df.columns), axis=1)


        else:
             frame['Sheet_Name'] = pd.Series([sheetname for x in range(len(frame.index))])
             frame['Excel_Name'] = pd.Series([fname.split('\\')[9] for x in range(len(frame.index))])

            #reference: https://stackoverflow.com/questions/47278064/python-how-to-dynamically-exclude-a-column-name-from-a-list-of-columns-of-a-pa
             #selected_col = set(list(frame.columns)).intersection(set(first_file_col))
             # Did not use set operation as the order cannot be guaranteed
             #reference:https://stackoverflow.com/questions/1653970/does-python-have-an-ordered-set/1653974
             selected_col = pd.Index(frame.columns) &  pd.Index(first_file_col)


             #reference:https://thispointer.com/python-pandas-how-to-convert-lists-to-a-dataframe/
            # frame = frame.from_records(frame, columns=list(selected_col)).drop_duplicates('Employeeid',keep='first')
             df = df.reindex(columns= list(first_file_df.columns)).from_records(frame, columns=list(selected_col)).drop_duplicates('Employeeid', keep='first')


             extra_col = list(set(first_file_col).difference(selected_col))

             if not extra_col:
                all_data_df = all_data_df.append(df, sort=False).reindex(columns= list(first_file_df.columns))

             else :
                for i in extra_col:
                    df[i] = 'NA'
                all_data_df = all_data_df.append(df, sort=False).reindex(columns=list(first_file_df.columns))


#dataframe to excel
all_data_df.to_excel (writer, index = False, header=True)
writer.save()




