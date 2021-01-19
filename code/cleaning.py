import pandas as pd
import numpy as np

df = pd.read_csv('../datasets/steam_reviews.csv', parse_dates=['date_posted'])

# Remove small title samples
title_count = pd.DataFrame(df.groupby('title')['date_posted'].count())
title_count.reset_index(inplace=True)
for title, count in title_count.iterrows():
    if count[1] < 200:
        df = df[df['title'] != count[0]]

# Replace outliers with 0
df['funny'].values[df['funny'].values > 1000000] = 0.0

# Delete column which we are not using and contains NaNs
del df['review']

# Convert catagorical data to numerical
df['recommendation'].values[df['recommendation'].values == "Recommended"] = 1
df['recommendation'].values[df['recommendation'].values == "Not Recommended"] = 0
df['recommendation'] = df['recommendation'].astype('Int64')

df.to_csv('steam-reviews-clean.csv', index=False)

