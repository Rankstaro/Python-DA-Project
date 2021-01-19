import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool

df = pd.read_csv('steam-reviews-clean.csv', parse_dates=['date_posted'])

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

helpful_time = figure(
    title='Relationship between Helpfulness and Time Played',
    x_axis_label='Helpfulness',
    y_axis_label='Time Played')

helpful_time.circle(df['helpful'], 
             df['hour_played'],
             size=4)

show(helpful_time)

# Vis 5
output_file('graph5.html')

helpful_funny = figure(
    title='Relationship between Helpfulness and Funniness',
    x_axis_label='Helpfulness',
    y_axis_label='Funniness')

helpful_funny.diamond(df['helpful'], 
             df['funny'],
             size=4)

show(helpful_funny)
