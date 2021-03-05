# %%
import pandas as pd

dt = pd.read_csv('Q2_Pandas_Assignments\states0.csv', index_col=[0])
print(dt.head())

# %%

data = pd.DataFrame(np.random.randn(1000, 4))
print(data)