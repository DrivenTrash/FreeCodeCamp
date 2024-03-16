import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")
df['overweight'] = df['overweight'] = df["weight"] / df["height"] / df["height"] * 10000 > 25
df['gluc'] = pd.read_csv("medical_examination.csv")["gluc"] > 1
df['cholesterol'] = pd.read_csv("medical_examination.csv")["cholesterol"] > 1
print(df.describe())
clean_df = df[(df["height"] >= df["height"].quantile(0.025)) &
              (df["height"] <= df["height"].quantile(0.975)) &
              (df["weight"] >= df["weight"].quantile(0.025)) &
              (df["weight"] <= df["weight"].quantile(0.975))]
print(clean_df)
corr = clean_df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
fig, ax = plt.subplots(figsize=(12, 12))
sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=0.5, square=True, cbar_kws={"shrink": 0.5})
fig.savefig('heatmap.png')
print(corr)
