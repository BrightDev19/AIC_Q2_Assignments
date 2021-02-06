# %%
# Function Mapping 
import numpy as np
from numpy.core.defchararray import index
import pandas as pd
rand_nd = np.random.randn(4,3)
frame = pd.DataFrame(rand_nd,columns=list('ABC'),index=['Apples','Bat','Cat','Duck'])
print('\u001b[34;1m',frame)
# Finds the maximum from x
f = lambda x : x.max()
print(frame.apply(f))
# print(frame.apply(f,axis=1))
# %%
# ************User Function************

# This method take a single row or column of the dataframe which is specified in apply method, then generates a sereis of that row or column.
def min_max(x):
    rt =pd.Series([x.min(),x.max()],index=['min','max'])
    print(type(rt))
    return rt
df = frame.apply(min_max,result_type=None,axis=0)
print(df)

# %%
# This works same as axis = 0 is supplied to apply method.
# How can I apply to axis 1 by using this method.
min_max_df = pd.DataFrame([frame.min(),frame.max()],index=['min','max'],)
print(min_max_df)
# %%
# Under standing of apply method

df_to_test = pd.DataFrame(np.array([[5,6,3]]*3)**2, columns=['P','Q','R'])
print(df_to_test)
rst =df_to_test.apply(np.sqrt,axis=0,result_type='reduce')
print(rst)
print(type(rst))

# %%
