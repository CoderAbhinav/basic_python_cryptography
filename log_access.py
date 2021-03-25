import pandas as pd

name = str(input("Enter the key name : "))
df = pd.read_csv(f'data/{name}/log_{name}.csv')

print(df)