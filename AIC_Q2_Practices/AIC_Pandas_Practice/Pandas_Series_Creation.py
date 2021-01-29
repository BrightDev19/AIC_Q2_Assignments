import pandas as pd
import numpy as np

# Python Data Structure
py_tpl = tuple(range(10, 101, 20))
py_lst = [5, 10, 15, 45, 15, np.nan, 20]
print("Pandas Series with Python Tuple")
ps_with_tpl = pd.Series(py_tpl, index=range(1, len(py_tpl) + 1), dtype='i4')
print(ps_with_tpl)
print("Series Values:", ps_with_tpl.values)
print("Series Index:", ps_with_tpl.index)

print('*' * 50)
print("Pandas Series with Python List")
ps_with_lst = pd.Series(py_lst, index=range(1, len(py_lst) + 1), dtype=np.float)
print(ps_with_lst)
print("Series Values:", ps_with_lst.values)
print("Series Index:", ps_with_lst.index)
# Altering index inplace with assignment
# number of new indexes must be same as previous indexes
ps_with_lst.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("ps_with_lst with new indexes", ps_with_lst, sep='\n')
# print("Unique Values Count\n{0}".format(ps_with_lst.value_counts(dropna=False)))


print("{0}SeriesWithDictionary{0}".format('*' * 10))
# While feeding data to pandas series with Python Dictionary
# Keys of the dictionary becomes the index (in sorted order) and values remain values in pandas series.
states_with_pop = {"Lahore": 500, "Islamabad": 700, "Karachi": 1500, "Peshawar": 600}
ps_with_dict = pd.Series(states_with_pop)
print("Dict Series:", ps_with_dict, sep="\n")
# by reindexing you can add more indexes, rearrange previous indexes
ps_with_dict = ps_with_dict.reindex(['Lahore', 'Karachi', "Islamabad", 'Multan', "Peshawar","Quetta"])
print("After Reindexing of the Series")
# Performs slicing of the series. Note: For indexing you have to exactly specify the index of the series.
print("Series Slicing:", ps_with_dict[0:2], sep="\n")
# Numpy ndarray like filtering on pandas series.
filt_sr = ps_with_dict[ps_with_dict > 800]
print("Filterd Series:", filt_sr,sep='\n')
# Create a third series by stacking two of them
sr_concat = pd.Series(np.hstack((ps_with_tpl.values, ps_with_dict.values)),
                      index=np.hstack((ps_with_tpl.index, ps_with_dict.index)))
print("Concatenated Series", sr_concat, sep="\n")
# Finds the null value if series contains
print("where value is not null",ps_with_lst.notnull(),sep='\n')
# Series can behave like python dictionary,in which 'in' operator can be used to find out any index in the series.
index_position = 2
index_lbl = ps_with_dict.index[index_position]
print("{0} is indexed in ps_with_dict {1}".format(index_lbl,index_lbl in ps_with_dict))

# Name attribute
ps_with_dict.name = "Population"
ps_with_dict.index.name = "State"
print(ps_with_dict)