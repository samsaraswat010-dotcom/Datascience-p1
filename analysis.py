import pandas as pd

df = pd.read_csv('archive/Titanic_train.csv')

print("--- Dataset Head ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Missing Values Count ---")
print(df.isnull().sum())
