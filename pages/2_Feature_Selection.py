import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Feature Selection')
st.markdown('## About the feature selection process')
st.markdown('I tried 5 differnt feature selection processes: \n' \
'- **SelectKBest**: A filtering method that selects the k features with the highest statistical relationship to the target variable, independently of any model \n'
'- **Embedded Lasso**: Lasso regression penalizes large coefficients and sets unimportant features to exactly zero, performing feature selection during model training \n'
'- **Embedded Random Forest**: Random Forest measures how much each feature reduces prediction error across all trees, giving a feature importance score \n'
'- **Wrapper Linear Regression (RFECV)**: Recursively removes the weakest feature and uses cross validation to find the optimal number of features for a linear regression model \n'
'- **Wrapper Random Forest (RFECV)**: Same as above but using a Random Forest as the estimator')

st.title('Feature Selection')
st.markdown('### RFECV Linear Regression')
st.markdown('This plot shows how the cross validation score changes as more features are added to the linear regression model. The score stabilizes after 3 features, meaning additional features do not improve the model.')


st.image('assets/rfecv_linear_regression.png')

st.markdown('### RFECV Random Forest')
st.markdown('The same process applied to a Random Forest model. The score keeps increasing with more features, but the improvement becomes smaller. This suggests that linear regression benefits more from feature reduction than Random Forest.')


st.image('assets/rfecv_random_forest.png')

st.markdown('### Comparison of all methods')
st.markdown('This table shows which features were selected by each method. Features selected by multiple methods are the most reliable choices. Based on this analysis, complexity, yearpublished and minplaytime were selected as the final features.')


df_features = pd.read_csv('assets/feature_selection_results.csv', index_col=0)

df_features_display = df_features.replace({True: '✅'})
st.dataframe(df_features_display)
