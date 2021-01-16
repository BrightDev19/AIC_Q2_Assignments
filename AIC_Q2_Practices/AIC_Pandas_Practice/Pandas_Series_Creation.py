import pandas as pd
import numpy as np

# Python Data Structure
py_tpl = tuple(range(10, 101, 10))
py_lst = [5, 10, 15, 45, 15, np.nan, 20, 45, 50, 25]
print("Pandas Series with Python Tuple")
ps_with_tpl = pd.Series(py_tpl, index=range(1, len(py_tpl) + 1), dtype='i4')
print(ps_with_tpl)
print(ps_with_tpl.values)

print('*' * 50)
print("Pandas Series with Python List")
ps_with_lst = pd.Series(py_lst, index=range(1, len(py_lst)), dtype=np.float)
print(ps_with_lst)
print("Unique Values Count\n{0}".format(ps_with_lst.value_counts(dropna=False)))
