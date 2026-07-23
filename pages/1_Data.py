import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Exploratory Data Analysis')

df = pd.read_csv('bgg_clean_data.csv')

st.markdown('## About the data')
st.markdown('This dataset contains the **5000 most rated** board and card games on BoardGameGeek.')

st.markdown('### Target distribution')
st.markdown('This is a distribution plot of the target variable. We can see that the target variable bayesaverage is right skewed .')
fig, ax = plt.subplots()
sns.histplot(df['bayesaverage'], kde=True, ax=ax)
st.pyplot(fig)
plt.close()



st.markdown('### Complexity vs bayesaverage')
st.markdown('This plot shows the feature complexity against bayesaverage. We can detect a positive relationship. We can infer that a higher complexity results in a higher bayesaverage score')
fig, ax = plt.subplots()
ax.scatter(df['complexity'], df['bayesaverage'], alpha=0.5)
ax.set_xlabel('complexity')
ax.set_ylabel('bayesaverage')
ax.set_title('Complexity vs. bayesaverage')
st.pyplot(fig)
plt.close()


st.markdown('### Correlation matrix')
st.markdown('In this plot we can identify the correlations between the features and also between the target variable. The features with the higest correlation regarding the target are: complexity, yearpublished and minage.')
corr = df.corr(numeric_only=True)
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
ax.set_title('Correlation matrix')
st.pyplot(fig)
plt.close()