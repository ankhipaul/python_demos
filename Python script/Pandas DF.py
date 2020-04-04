import pandas as pd
import numpy as np

filepath = "sales_2016_2017.csv"

def convert_currency(val):
    """
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)

def convert_percent(val):
    new_val = val.replace('%', '')
    return float(new_val)/100

sales_df_2 = pd.read_csv(filepath,
                   dtype={'Customer Number': 'int'},
                   converters={'2016': convert_currency,
                               '2017': convert_currency,
                               'Percent Growth': convert_percent,
                               'Jan Units': lambda x: pd.to_numeric(x, errors='coerce'),
                               'Active': lambda x: np.where(x == "Y", True, False)
                              })

print(sales_df_2.dtypes)