# %%
import numpy as np
import pandas as pd
from pandas.core.indexes.range import RangeIndex

print('*'*10,'Series to DataFrame','*'*10)
oranges = [45,63,85,96,45]
apples = [63,52,41,78,99]
org_start = max(oranges) 
step = 2
org_stop = max(oranges)+len(oranges)*step
# index starts from the maximum value of the sequence, endsn = after addtion of number of elements in the sequence product of step 
ind_org = range(org_start,org_stop,step)
oranges_sr = pd.Series(apples )
print(oranges_sr)
aple_start = max(apples) 
apl_stop = max(apples)+len(apples)*step
ind_apl = RangeIndex(aple_start,apl_stop,step=2)
apples_sr = pd.Series(apples)
print("\u001b[30;1m Printing Apple Series")
print('\u001b[32;1m',apples_sr)

# ********** Merging Series *********

mergSr = pd.DataFrame(apples_sr,oranges).reset_index()
print('\u001b[30;1m Merged Series to Dataframe',mergSr)
print('\u001b[33;1m',"Now Merging Series with Dif Index to by using dic")
merg_dic = {'Apples':apples,'Oranges':oranges}
merg_dic_sr= {'Apple':apples_sr,'Oranges':oranges_sr}
pdf_seriesMerge = pd.DataFrame(merg_dic)
print('\u001b[32;1m',pdf_seriesMerge)
print('\u001b[32;1m',pdf_seriesMerge.columns)
print('\u001b[32;1m',pdf_seriesMerge.index)

# Retrieval of Column either by Dict-like notation or Attribute.
print('\u001b[34;1mCol Retrieval With Dic-Like Notation',pdf_seriesMerge['Apples'],sep='\n')
print('\u001b[33;4mCol Retrieval With Attribute Notation',pdf_seriesMerge.Oranges,sep='\n')
print(pdf_seriesMerge.loc[1])

# %%

import re
txt = 'foo   bar\t baz \tqux'
smpl = txt.split()
print(smpl)
rgx = re.compile('\s*')
splitted = rgx.split(txt)
# print(splitted)

# %%
oranges = [45,63,85,96,45]
apples = [63,52,41,78,99]
or_sr = pd.Series(oranges)
ap_sr = pd.Series(apples)

merged= pd.DataFrame(apples,oranges,apples).reset_index()
print("Combined Apples and oranges")
print(merged)

# %%
