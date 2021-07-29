# Feedback for Oliver Rankin-Starcevic

## Overall

This was a fantastic project that showcased not only your excellent coding skills but also your ability to communicate findings in a concise way. Good communication abilities combined with your coding skills, is to me, a recipe for quality work. There is no doubt in my mind that you already are a data analyst and that, whichever data path you choose to follow, you have the tools to succeed in it. Excellent work!

## Rubric

| Task Descriptor | Completed | Not Completed | Comments |
| -------- | -------- | -------- | -------- |
| URL to the repository for the project containing an initial README.md file, one file with the project outline and results, and a folder with at least two code files, one for cleaning the data and another for the analysis. Percentage of overall mark: 25% | X |  | Excellent |
| Dataset collected and submitted in a CSV or JSON format. Percentage of overall mark: 20% | X |  | Excellent |
| Successful reproducibility of the cleaning and the analysis code. Percentage of overall mark: 40% | X |  | All files were successfully |
| There are a minimum of 5 visualizations, 3 static ones, and 2 interactive ones, and the axes and title --where appropriate-- are clearly specified. Percentage of overall mark: 15% | X |  | There were fantastic visualisations in the analysis and project notebooks. |



## Constructive Feedback

### Overall
- Excellent README in your repo. Clean and to the point.
- It is good practice to let others know which operating system you are using in case there are issues with some of the libraries being used. The fact that you pointed this out at the very beginning shows the good attention to detail you have. Great work!
- When feasible, it is good practice to describe the variables contained in the dataset about to be analyzed. Great work putting this at the top of your project notebook.

### Cleaning
- The cleaning process was straightforward and concise. Using a notebook isn't mandatory and the fact that you did it both ways, with scripts and within your final notebook, was excellent.
- You could have merged all small games into one category and called them, `small_games`, or something similar, instead of taking them out and do one more comparison between big-name titles versus the smaller ones. Your approach was good nonetheless.
- You could have also replaced the outliers with the mean, median, or another quantity from that same game or similar ones that might have represented reality a bit better.
- Instead of converting your pandas Series' into NumPy arrays for filtering, you might also want to try `.loc[]` or `.iloc[]`.

```python

# the version in the notebook
df['recommendation'].values[df['recommendation'].values == "Recommended"] = 1

# another way of doing it
df.loc[df['recommendation'] == "Recommended", 'recommendation'] = 1

```


### Analysis

- Fantastic questions.
- Awesome visualisations.
- Excellent use of title and axes labels.
- You can also convert a `.groupby()` class back into a dataframe by resetting its index directly. For example,

```python

# one way
avg_playtime = pd.DataFrame(df.groupby('title')['hour_played'].mean())
avg_playtime.reset_index(inplace=True)
avg_playtime.sort_values(by=['hour_played'], inplace=True)

# another way
avg_playtime = df.groupby('title')['hour_played'].mean().reset_index().sort_values('hour_played')

```
- Excellent analysis of the output of your visualisations. Your choice of words was fantastic, there are no concrete facts in the data but indications of which direction things are moving towards. You explained this very well.
- Great work pointing out some possible confounding factors within question 2 (i.e. things that might influence the results but we don't know anything about them).
- The word `significance` in data analysis has a special statistical meaning, and when you compare a measure like the negative movement/shift of reviews with a characteristic such as early access, you could try to use the words large shift, a big shift, a noticeable shift, etc.
- Be cautious with stating strong conclusions such as **it is clear that...**, these are facts taken at a specific point in time, not the ground truth. One way to approach it would be, **based on the analysis above, we found no correlation...** Essentially, you could approach Q4 in the same way you approached Q5.
- Great conclusion!

You did amazing work throughout this project and the feedback above is only meant to help you polish your skills as the data professional you already are. Keep up the awesome work and please let me know if you have any questions regarding the above.