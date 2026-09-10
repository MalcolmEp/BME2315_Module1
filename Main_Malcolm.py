import pandas as pd

df = pd.read_csv("/Users/malcolmepstein/Desktop/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv")

for col in df.columns:
    print(col)

# Test