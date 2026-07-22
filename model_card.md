# Model Card

## 1. Model Description
For this project I used a Random Forest model from the scikit-learn library with the following parameters: max_depth = 5 and n_estimators = 50.

## 2. Intended Use
This model was used to predict the bayesaverage of the 5000 most voted board and card games in the BGG dataset, which were published after 1900 and before 2027, with a minimum and maximum number of players above 0, a minimum play time of more than 0 minutes, and a maximum play time of less than 600 minutes.

## 3. Training Data
For this project I used the BGG API and the openly available boardgames_ranks.csv dataset. To predict the value of the target variable bayesaverage I used the features complexity, yearpublished and minplaytime, since those were the most descriptive features based on my feature selection process.

## 4. Performance
- R²: 0.274
- MAE: 0.374
- RMSE: 0.476

## 5. Limitations
This model has some limitations. There are many more features like genre, publisher, designer, etc. that could be used to predict the bayesaverage score. The focus of this project was not on optimization but rather on the workflow and first approaches in using an API. The lack of features is also seen in the residual plot, where there is a positive linear relationship between bayesaverage and the residuals. Also, several games were excluded: games developed before 1900, games published after 2026, games with a minimum or maximum player count of 0, games with a minimum play time of 0, and games with a maximum playtime over 600 minutes.

## 6. Ethical Considerations
Since the score a person gives a game is completely individual, these scores are biased by the people who play them. Also, users of BGG are a specific group of people who are very interested in board and card games. They are not representative of the whole population.