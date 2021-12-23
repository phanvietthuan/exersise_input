import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('D:\momo\excercise_input (1)\excercise_input\input\input_data.csv')
df.columns
pd.DataFrame(df)


user_transaction = df['user'].where(df['status'] >= 0).value_counts()
df['timestamp'] = pd.to_datetime(df['timestamp'], unit = 'ms')
