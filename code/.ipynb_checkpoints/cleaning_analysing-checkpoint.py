import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool

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

# Set matplotlib params
plt.rcParams['figure.figsize'] = [5.0, 5.0]
plt.rcParams['figure.dpi'] = 500
plt.style.use('seaborn-paper')

# Vis 1
avg_playtime = pd.DataFrame(df.groupby('title')['hour_played'].mean())
avg_playtime.reset_index(inplace=True)
avg_playtime.sort_values(by=['hour_played'], inplace=True)
plt.barh(avg_playtime['title'], avg_playtime['hour_played'], color='#bbee44')
plt.title('Mean playtime by Game')
plt.xlabel('Hours')
plt.ylabel('Game')
plt.show()

# Vis 2
avg_recommend = pd.DataFrame(df.groupby('title')['recommendation'].mean())
avg_recommend.reset_index(inplace=True)
avg_recommend.sort_values(by=['recommendation'], inplace=True)
plt.barh(avg_recommend['title'], avg_recommend['recommendation']*100, color='#bb4411')
plt.title('Percentage of positive reviews by Game')
plt.xlabel('Recommendation Percentage (%)')
plt.ylabel('Game')
plt.show()

# Vis 3
ea_true = df[df['is_early_access_review'] == True]
ea_false = df[df['is_early_access_review'] == False]
avg_recommend_ea_true = pd.DataFrame(ea_true.groupby(['title'])['recommendation'].mean())
avg_recommend_ea_false = pd.DataFrame(ea_false.groupby(['title'])['recommendation'].mean())
avg_recommend_ea_true.reset_index(inplace=True)
avg_recommend_ea_false.reset_index(inplace=True)
avg_ea_merge = pd.merge(avg_recommend_ea_true, avg_recommend_ea_false, on='title', how='inner')

fig, ax = plt.subplots()

ax.barh(avg_ea_merge['title'], avg_ea_merge['recommendation_x'], label="Early Access = True", color='red', alpha=0.5, align='center')
ax.barh(avg_ea_merge['title'], avg_ea_merge['recommendation_y'], label="Early Access = False", color='blue', alpha=0.5, align='center')

plt.title('Percentage of positive reviews in early access vs not early access')
plt.xlabel('Recommendation Percentage (%)')
plt.ylabel('Game')
plt.legend()
plt.show()

# Vis 4
output_file('graph4.html')

pd.set_option('display.max_columns', None)

hover = HoverTool(tooltips=None, mode='hline')

# the crosshair option gives us a cross to hover with
helpful_time = figure(
    title='Relationship between Helpfulness and Time Played',
    x_axis_label='Helpfulness',
    y_axis_label='Time Played')

# we can add color to the hover tool with hover_color parameter
helpful_time.circle(df['helpful'], 
             df['hour_played'],
             size=4)

show(helpful_time)

# Vis 5
output_file('graph5.html')
# the crosshair option gives us a cross to hover with
helpful_funny = figure(
    title='Relationship between Helpfulness and Funniness',
    x_axis_label='Helpfulness',
    y_axis_label='Funniness')

# we can add color to the hover tool with hover_color parameter
helpful_funny.diamond(df['helpful'], 
             df['funny'],
             size=4)

show(helpful_funny)