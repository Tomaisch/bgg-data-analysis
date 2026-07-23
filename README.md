# BGG Score Predictor

## Project Description
In this project I predicted the bayesaverage score of board and card games using the 5000 most rated games on BoardGameGeek.

The bayesaverage score is a score that calculates the average score based on the number of votes. It is based on an additional fictional 1500 neutral scores, which are added by BoardGameGeek. This procedure makes the bayesaverage score a fairer score than just the average score on its own.
There is an interactive Web-App where the whole pipeline is explained in detail and you can also try the model to predict the score of your favorite game
## Approach
For this project I used the BGG API and the available boardgames_ranks.csv to get the data. I merged these two datasets and filtered only the 5000 most voted games, which were then used for further investigation. A heatmap of the correlation matrix and several boxplots showed that some features are more correlated with the target than others and that some features had extreme values and outliers. I deleted the extreme values and used RobustScaler. After that I did five different feature selection approaches to identify the most important features, which I used for training the models. To predict the bayesaverage score I used several approaches: Linear Regression, Lasso, Random Forest, Lasso with cross-validation and grid search, and Random Forest with cross-validation and grid search.

## Results
The model with the best performance was Random Forest with a max depth of 5 and 50 estimators. The model showed an R² of 0.274, a mean absolute error of 0.373 and a root mean squared error of 0.476.

## How to run
1. Clone the repo: `git clone https://github.com/Tomaisch/bgg-data-analysis`
2. Create and activate a virtual environment: `python -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file and add your BGG API token: `BGG_TOKEN=your_token_here`
5. Run the notebook: `jupyter notebook`
6. Start the app: `streamlit run app.py`


## Limitations
This model has some limitations. There are many more features like genre, publisher, designer, etc. that could be used to predict the bayesaverage score. The focus of this project was not on optimization but rather on the workflow and first approaches in using an API. The lack of features is also seen in the residual plot, where there is a positive linear relationship between bayesaverage and the residuals. Also, several games were excluded: games developed before 1900, games published after 2026, games with a minimum or maximum player count of 0, games with a minimum play time of 0, and games with a maximum playtime over 600 minutes.


## Attribution
Data sourced from [BoardGameGeek](https://boardgamegeek.com).

[![Powered by BGG](assets/powered_by_BGG_01_SM.png)](https://boardgamegeek.com)