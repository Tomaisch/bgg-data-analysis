import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Model Training and Comparison')

st.markdown('## Models')
st.markdown('Three models were trained and compared: \n'
'- **Linear Regression**: Used as a baseline model. It is the simplest model and gives a reference point to evaluate whether more complex models actually improve performance \n'
'- **Lasso**: A linear regression model with regularization. It penalizes large coefficients and can set unimportant features to zero. It was included to see if regularization improves on the baseline \n'
'- **Random Forest**: A non-linear ensemble model that builds many decision trees and averages their predictions. It was included as a more powerful alternative to the linear models')

st.markdown('## Hyperparameter Tuning')
st.markdown('GridSearchCV was used instead of RandomizedSearchCV because the dataset is relatively small and the number of hyperparameters is limited. GridSearchCV tests every possible combination of hyperparameters, which guarantees finding the best combination within the defined search space. With a larger dataset or more hyperparameters, RandomizedSearchCV would have been the better choice due to its lower computational cost.')

st.markdown('## Results')
st.image('assets/model_comparison.png')
df_results = pd.read_csv('assets/model_results.csv', index_col=0)
st.markdown('Detailed results for all models:')
st.dataframe(df_results)

st.markdown('After tuning, all three models perform similarly. The optimized Random Forest was selected as the final model with an R2 of 0.274, a MAE of 0.373 and an RMSE of 0.476. The relatively low R2 is expected given that the bayesaverage score is based on subjective user ratings and several potentially important features such as genre and publisher are not included in the dataset.')