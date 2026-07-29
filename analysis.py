import pandas as pd

# 1. Load the dataset downloaded from Kaggle
df = pd.read_csv('archive/Titanic_train.csv')

# 2. Display basic dataset details
print("--- Dataset Head ---")
print(df.head())

# 3. Structural Information
print("\n--- Dataset Info ---")
print(df.info())

# 4. Summary Statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# 5. Missing Values Count
print("\n--- Missing Values Count ---")
print(df.isnull().sum())
