# Buying a Game on Steam
## Summary
I want to play games on gaming platform and store Steam, but I want to be sure that I invest my time and money wisely. I will use data collected from Steam to answer some questions I have about games and the validity of the review system, and try to figure out what the best indicator is to determine the quality of a game.
## Data
I shall be using steam_reviews.csv for the project. You can download it from the following link:

https://www.kaggle.com/luthfim/steam-reviews-dataset

If there isn't currently a folder called "datasets" in your working directory, create one. Extract the CSV file from the downloaded zip and place it in the datasets folder.
## Project Document
The project document goes through my entire process of cleaning and analysing the data. 
### Cleaning
* I removed any game titles which had sample sizes too small
* Checked for duplicates
* Removed anomalies and outliers
* Removed missing values
* Converted catagorical data into numerical values

### Analysis
#### Static Visualizations
* What games have the highest mean playtime by reviewers?
* What games have the highest percentage of positive reviews?
* Does a game get better reviews after leaving early access?

#### Dynamic Visualizations
* Is a review rated more helpful if the reviewer has played for longer?
* Is there a correlation between funniness and helpfulness?

### Results
To me, the best game should not be in early access, as this indicates that reviews may be inaccurate. I don't believe the credibility of a positive or negative review should come into question depending on how long that user has played the game for. Finally, I think that just because a review is humourous, it does not imply that it is not credible.