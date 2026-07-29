import pandas as pd

# Sample DataFrame
data = {'Sales': [100, 200, 300, 400, 500],
        'Profit': [20, 40, 60, 80, 100]}

df = pd.DataFrame(data)

# Summary statistics for all numeric columns
print(df.describe().T)
