# nbx2ue

import pandas as pd

df = pd.read_csv("/Users/brook/OneDrive/Desktop/COMP/Mod 1/Metadata and Protein Data for Module 1.csv")

for column in df.columns:
    print(column)