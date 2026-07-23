import streamlit as st
import joblib
import requests
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import shap


token = os.getenv('BGG_TOKEN')
headers = {'Authorization': f'Bearer {token}'}

model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')

def search_game_name(game_name):
    url = f'https://boardgamegeek.com/xmlapi2/search?query={game_name}&type=boardgame'
    response = requests.get(url, headers=headers)
    root = ET.fromstring(response.text)
    games = []
    for item in root.findall('item'):
        name_tag = item.find("name[@type='primary']")
        if name_tag is None:
            continue
        game = {}
        game['id'] = int(item.get('id'))
        game['name'] = name_tag.get('value')
        game['yearpublished'] = item.find('yearpublished').get('value')
        games.append(game)
    return games
def get_game_details(game_id):
    url = f"https://boardgamegeek.com/xmlapi2/thing?id={game_id}&type=boardgame&stats=1"
    response = requests.get(url, headers=headers)
    root = ET.fromstring(response.text)
    for item in root.findall('item'):
        try:
            game_details = {}
            game_details['id'] = item.get('id')
            game_details['name'] = item.find("name[@type='primary']").get('value')
            game_details['yearpublished'] = item.find('yearpublished').get('value')
            game_details['minplaytime'] = item.find('minplaytime').get('value')
            stats = item.find('statistics/ratings')
            game_details['bayesaverage'] = stats.find('bayesaverage').get('value')
            game_details['complexity'] = stats.find('averageweight').get('value')
            return game_details
        except:
            return None



st.title('BGG Score Predictor')

st.markdown('## How to use')
st.markdown('Enter a board game name below, select the correct game from the dropdown list, and the model will predict its bayesaverage score based on its complexity, year published and minimum playtime.')

game_name = st.text_input('Enter a game name')

if game_name:
    results = search_game_name(game_name)
    if results:
        options = {f"{g['name']} ({g['yearpublished'] if g['yearpublished'] else 'unknown'})": g['id'] for g in results}
        selected = st.selectbox('Select a game', options.keys())
        game_id = options[selected]

        details = get_game_details(game_id)
        if details is None:
            st.warning('Could not load details for this game. Please select another one.')

        else:
            st.write(f"Year published: {details['yearpublished']}")
            st.write(f"Complexity: {details['complexity']}")
            st.write(f"Min playtime: {details['minplaytime']}")
            st.write(f"Bayesaverage (real): {details['bayesaverage']}")

            features = np.array([[details['minplaytime'], details['yearpublished'], details['complexity']]], dtype=float)
            features_scaled = scaler.transform(features)
            st.markdown('### Game details')
            prediction = model.predict(features_scaled)
            st.write(f"Predicted bayesaverage: {round(prediction[0], 2)}")

            st.markdown('### Predicted score')
            st.markdown('### Why this score?')
            st.markdown('The waterfall plot below shows how each feature contributed to the predicted score. The base value is the average prediction of the model. Each feature then pushes the prediction up or down.')
            explainer = joblib.load('explainer.pkl')
            features_df = pd.DataFrame([[float(details['minplaytime']), float(details['yearpublished']), float(details['complexity'])]], 
                                        columns=['minplaytime', 'yearpublished', 'complexity'])
            features_scaled = scaler.transform(features_df)
            shap_values = explainer.shap_values(features_scaled)

            fig, ax = plt.subplots()
            base_value = float(explainer.expected_value) if np.ndim(explainer.expected_value) == 0 else float(explainer.expected_value[0])
            shap.waterfall_plot(shap.Explanation(values=shap_values[0], 
                                                base_values = base_value,
                                                data=features_df.values[0],
                                                feature_names=['minplaytime', 'yearpublished', 'complexity']))
            st.pyplot(fig)