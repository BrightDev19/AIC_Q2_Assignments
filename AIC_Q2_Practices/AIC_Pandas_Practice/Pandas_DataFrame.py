
# %%
from numpy.core.fromnumeric import transpose
import pandas as pd
import numpy as np
import time as tm

from pandas.core.groupby.generic import pin_whitelisted_properties
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
print('\u001b[31;1m')
print('*' * 10,"DataFrame",'*'*10)
pdf_states_pop = pd.DataFrame(py_dict_states)
print('First DataFrame:',pdf_states_pop,sep='\n')
pdf_rearranged_cols = pd.DataFrame(py_dict_states, columns=['Population','Year','State','Debt'])
print('Cols Re-organized DataFrame:',pdf_rearranged_cols,sep='\n')

"""This method returns the top n rows of the series or DataFrame
    by default it returns top 5 rows
"""
top_row_pdf = pdf_states_pop.head(1)
print("Head of the DF",top_row_pdf,sep='\n')

# Getting the length(number of row) of dataframe
# pdf_rearranged_cols.Debt = np.around(np.random.rand(pdf_rearranged_cols.__len__())*100,0)
pdf_rearranged_cols.Debt = np.random.random_integers(5,size=pdf_rearranged_cols.__len__())
print('\u001b[32;1mFilled Debt\n',pdf_rearranged_cols)

pdf_rearranged_cols['Ohio'] = pdf_rearranged_cols['State'] =='Ohio'
print('\u001b[32;1mAppending Ohio\n',pdf_rearranged_cols)
del pdf_rearranged_cols['Ohio']
print('\u001b[32;1mDeleting Ohio\n',pdf_rearranged_cols)

# %%


# Measurement of execution time
print('*' * 10,"Execution Time",'*'*10)
end_time = tm.time()
print("Start time:", start_time)
print("End Time:", end_time)
consumed_time = end_time - start_time
print("Time Taken:",consumed_time)



# %%
# Nested Dictionary
nest_dic = {'Punjab':{'2010' :800,2011:950,2012:1110},'Sindh':{'2010' :800,2011:950,2012:1110},'Punjab':{'2010' :800,2011:950,2013:1110}}
pd_prvince= pd.DataFrame(nest_dic)
pd_prvince.index.name = "Year"
pd_prvince.columns.name = "State"

print('\u001b[37;1m',pd_prvince.values)
# Transposing DataFrame
print('\u001b[37;1m',pd_prvince.transpose())

# %%

# index and column object in pandas
# 
pd_prv_indexes = pd_prvince.index # Returns an object of indexes, so with array operations you can get/ find index without knowing its name.
print('\u001b[38;1m',type(pd_prv_indexes))
print('\u001b[38;1m')
pd_prv_cols = pd_prvince.columns
print(pd_prv_cols.dtype)

# %%
