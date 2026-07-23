import streamlit as st

st.title('BGG Score Predictor')


st.markdown('## About this project')
st.markdown('This is my first Data Science project and I wanted to fuse two of my interests: Data Science and board games. I used the BoardGameGeek API to collect data on the 5000 most voted board and card games and built a model to predict their bayesaverage score. This project was not focused on performance optimization but rather on completing a full Data Science project from data collection to deployment.')
st.markdown('### How to use this webapp')
st.markdown('On the Data page you can explore the exploratory data analysis pipeline. Feature Selection shows the feature selection process used to identify the most important features. Model shows the application of different models on the data and compares their performance. Predictor is a small application where you can enter the name of a board game, select the correct one from the search results, and see the feature values, the real bayesaverage score and the predicted bayesaverage score. In addition, you get a plot that shows how each feature influenced the prediction.')

st.markdown('---')
st.markdown('Data provided by [BoardGameGeek](https://boardgamegeek.com). Powered by BGG.')
st.image('assets/powered_by_BGG_01_SM.png')
