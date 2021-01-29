
# %%
import pandas as pd
import numpy as np
import time as tm
# from AIC_Q2_Practices import ANSIColors as clr

# print(clr.COLORS['default'])
"""
What is DataFrame?
A DataFrame is a rectangular table a data and contains an ordered collection of columns, each of which can be different value type. The DataFrame has both row ans columsn index; it can be thought of a dictionary of Series all sharing the same index.
>> Concept:
While a DataFrame is physically two-dimensional, you can use it to
represent higher dimensional data in a tabular format using hier‐
archical indexing.

There are many ways to construct a DataFrame, though one of the most common is
from a dict of *equal-length* lists or NumPy arrays:
"""
# Main execution time starts from here
start_time = tm.time()  # returns the current time in milliseconds

# This Dictionary contains three keys with list of same size as values
# if we create a Pandas Series from this; there will be three indexes
#  If this dictionary fed to Pandas Dataframe then; there will be three
# Series stacked horizontally in DataFrame
py_dict_states = {'State': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
                  'Year': [2000, 2001, 2002, 2000, 2001, 2003], 'Population': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
ps_dict_states = pd.Series(py_dict_states,name='State Population Summary')
print("Pandas Series from Dictionary:",ps_dict_states)

# %%
import pandas as pd
print('*' * 10,"DataFrame",'*'*10)
pdf_states_pop = pd.DataFrame(py_dict_states)
print('First DataFrame:',pdf_states_pop,sep='\n')
pdf_rearranged_cols = pd.DataFrame(py_dict_states, columns=['Year','State','Population','Pop'])
print('Cols Re-organized DataFrame:',pdf_rearranged_cols,sep='\n')

"""This method returns the top n rows of the series or DataFrame
    by default it returns top 5 rows
"""
top_row_pdf = pdf_states_pop.head(1)
print("Head of the DF",top_row_pdf,sep='\n')

# %%


# Measurement of execution time
print('*' * 10,"Execution Time",'*'*10)
end_time = tm.time()
print("Start time:", start_time)
print("End Time:", end_time)
consumed_time = end_time - start_time
print("Time Taken:",consumed_time)



# %%
