import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('D:\momo\excercise_input (1)\excercise_input\input\input_data.csv')
df.columns
pd.DataFrame(df)
# print(df)

user_transaction_success = df['user'].where(df['status'] == 2).value_counts().head(10)
print(user_transaction_success)
df['user'].where(df['status'] == 2).value_counts(10).to_csv('D:\momo\excercise_input (1)\excercise_input\output\output_1.csv')
