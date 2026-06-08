import requests
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('BGG_TOKEN')

headers = {
    'Authorization': f'Bearer {token}'
}
url = 'https://boardgamegeek.com/xmlapi2/thing?id=13&type=boardgame'

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text[:500])